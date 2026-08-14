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

from canonical_execution import ExecutionRequest, build_evidence_object, build_execution_object, build_execution_trace, build_result_object
from test_executor import DeterministicExecutor
from yarp_adapter import YarpEnvelope, YarpTransportError, build_execute_envelope, retry_envelope

CORRELATION = "YARP-CORR-11111111-1111-4111-8111-111111111111"


def request(capability="echo", payload=None):
    return ExecutionRequest("task-42", "run-7", "trace-9", CORRELATION, capability, payload or {"value": "hello"}, ("execution_receipt",))


class RoundTripTests(unittest.TestCase):
    def setUp(self):
        self.executor = DeterministicExecutor()

    def test_success_round_trip_and_trace(self):
        execution = build_execution_object(request(), created_by="co-002-test")
        envelope = build_execute_envelope(execution, sender_id="agent-chatgpt-ag", receiver_id="agent-test-executor")
        receipt = self.executor.execute(envelope, execution)
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
        first = build_execute_envelope(execution, sender_id="agent-chatgpt-ag", receiver_id="agent-test-executor")
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
        execution = build_execution_object(request("fail", {"message": "boom"}), created_by="co-002-test")
        envelope = build_execute_envelope(execution, sender_id="agent-chatgpt-ag", receiver_id="agent-test-executor")
        receipt = self.executor.execute(envelope, execution)
        result = build_result_object(execution, receipt, created_by="co-002-test")
        self.assertEqual("failure", receipt.outcome)
        self.assertEqual("failure", result.payload["outcome"])
        self.assertEqual("CO002_CONTROLLED_FAILURE", result.payload["error"]["code"])

    def test_transport_failure_raises_before_domain_execution(self):
        execution = build_execution_object(request(), created_by="co-002-test")
        good = build_execute_envelope(execution, sender_id="agent-chatgpt-ag", receiver_id="agent-test-executor")
        malformed = YarpEnvelope(**{**good.__dict__, "envelope_id": "bad"})
        with self.assertRaises(YarpTransportError):
            self.executor.execute(malformed, execution)


if __name__ == "__main__":
    unittest.main()
