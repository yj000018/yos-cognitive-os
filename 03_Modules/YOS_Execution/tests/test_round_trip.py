from __future__ import annotations

from pathlib import Path
import sys
import unittest

MODULE_DIR = Path(__file__).resolve().parents[1]
ROOT = MODULE_DIR.parents[1]
MEMORY_DIR = ROOT / "03_Modules" / "YOS_Memory"
for path in (str(MODULE_DIR), str(MEMORY_DIR)):
    if path not in sys.path:
        sys.path.insert(0, path)

from canonical_execution import ExecutionIntegrityError, ExecutionRequest, build_evidence_object, build_execution_object, build_execution_trace, build_result_object
from test_executor import DeterministicExecutor
from yarp_adapter import YarpEnvelope, YarpTransportError, build_execution_transport_envelope, retry_envelope

CORRELATION = "YARP-CORR-11111111-1111-4111-8111-111111111111"


def request(capability="echo", payload=None):
    return ExecutionRequest("task-42", "run-7", "trace-9", CORRELATION, capability, {"value": "hello"} if payload is None else payload, ("execution_receipt",))


class RoundTripTests(unittest.TestCase):
    def setUp(self):
        self.executor = DeterministicExecutor()

    def execute(self, req: ExecutionRequest):
        execution = build_execution_object(req, created_by="co-002-test")
        envelope = build_execution_transport_envelope(execution, sender_id="agent-chatgpt-ag", receiver_id="agent-test-executor")
        return execution, envelope, self.executor.execute(envelope, execution)

    def test_success_round_trip_and_trace(self):
        execution, envelope, receipt = self.execute(request())
        result = build_result_object(execution, receipt, created_by="co-002-test")
        evidence = build_evidence_object(result, receipt, created_by="co-002-test")
        trace = build_execution_trace(execution, result, (evidence,), (envelope,))
        self.assertEqual("success", receipt.outcome)
        self.assertEqual({"echo": "hello"}, receipt.output)
        self.assertEqual((execution.object_id,), result.lineage.derived_from)
        self.assertEqual((result.object_id,), evidence.lineage.derived_from)
        self.assertEqual("trace-9", trace.trace_id)
        self.assertEqual(CORRELATION, trace.correlation_id)
        self.assertEqual(execution.object_id, trace.execution_object_id)
        self.assertEqual(result.object_id, trace.result_object_id)
        self.assertEqual((evidence.object_id,), trace.evidence_object_ids)
        self.assertEqual((envelope.envelope_id,), trace.yarp_envelope_ids)
        self.assertEqual((envelope.attempt_id,), trace.attempt_ids)

    def test_retry_keeps_one_semantic_execution(self):
        execution = build_execution_object(request(), created_by="co-002-test")
        first = build_execution_transport_envelope(execution, sender_id="agent-chatgpt-ag", receiver_id="agent-test-executor")
        second = retry_envelope(first)
        receipt = self.executor.execute(second, execution)
        result = build_result_object(execution, receipt, created_by="co-002-test")
        evidence = build_evidence_object(result, receipt, created_by="co-002-test")
        trace = build_execution_trace(execution, result, (evidence,), (first, second))
        self.assertEqual(execution.object_id, first.payload["canonical_object_id"])
        self.assertEqual(execution.object_id, second.payload["canonical_object_id"])
        self.assertEqual(2, len(trace.yarp_envelope_ids))
        self.assertEqual(2, len(trace.attempt_ids))

    def test_controlled_execution_failure_becomes_result(self):
        execution, _envelope, receipt = self.execute(request("fail", {"message": "boom"}))
        result = build_result_object(execution, receipt, created_by="co-002-test")
        self.assertEqual("failure", receipt.outcome)
        self.assertEqual("failure", result.payload["outcome"])
        self.assertEqual("CO002_CONTROLLED_FAILURE", result.payload["error"]["code"])

    def test_invalid_domain_input_becomes_failure_receipt_not_exception(self):
        execution, _envelope, receipt = self.execute(request("echo", {"unexpected": "value"}))
        result = build_result_object(execution, receipt, created_by="co-002-test")
        self.assertEqual("failure", receipt.outcome)
        self.assertEqual("CO002_INVALID_INPUT", receipt.error["code"])
        self.assertEqual("failure", result.payload["outcome"])

    def test_unsupported_capability_becomes_failure_receipt_not_exception(self):
        execution, _envelope, receipt = self.execute(request("unknown-capability", {}))
        result = build_result_object(execution, receipt, created_by="co-002-test")
        self.assertEqual("failure", receipt.outcome)
        self.assertEqual("CO002_UNSUPPORTED_CAPABILITY", receipt.error["code"])
        self.assertEqual("failure", result.payload["outcome"])

    def test_transport_failure_raises_before_domain_execution(self):
        execution = build_execution_object(request(), created_by="co-002-test")
        good = build_execution_transport_envelope(execution, sender_id="agent-chatgpt-ag", receiver_id="agent-test-executor")
        malformed = YarpEnvelope(**{**good.__dict__, "envelope_id": "bad"})
        with self.assertRaises(YarpTransportError):
            self.executor.execute(malformed, execution)

    def test_mutated_canonical_payload_is_rejected_before_execution(self):
        execution = build_execution_object(request(), created_by="co-002-test")
        envelope = build_execution_transport_envelope(execution, sender_id="agent-chatgpt-ag", receiver_id="agent-test-executor")
        execution.payload["capability"] = "fail"
        with self.assertRaises(ExecutionIntegrityError):
            self.executor.execute(envelope, execution)

    def test_envelope_execution_snapshot_must_match_canonical_object(self):
        execution = build_execution_object(request(), created_by="co-002-test")
        good = build_execution_transport_envelope(execution, sender_id="agent-chatgpt-ag", receiver_id="agent-test-executor")
        tampered_payload = {**good.payload, "execution": {**good.payload["execution"], "capability": "fail"}}
        malformed = YarpEnvelope(**{**good.__dict__, "payload": tampered_payload})
        with self.assertRaises(YarpTransportError):
            self.executor.execute(malformed, execution)


if __name__ == "__main__":
    unittest.main()
