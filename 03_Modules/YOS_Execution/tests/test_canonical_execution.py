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

from canonical_execution import (
    ExecutionReceipt,
    ExecutionRequest,
    build_evidence_object,
    build_execution_object,
    build_result_object,
)

CORRELATION = "YARP-CORR-11111111-1111-4111-8111-111111111111"


class CanonicalExecutionContractTests(unittest.TestCase):
    def request(self) -> ExecutionRequest:
        return ExecutionRequest(
            task_id="task-42",
            run_id="run-7",
            trace_id="trace-9",
            correlation_id=CORRELATION,
            capability="echo",
            input_payload={"value": "hello"},
            expected_evidence=("execution_receipt",),
        )

    def test_execution_identity_is_semantic_and_deterministic(self):
        first = build_execution_object(self.request(), created_by="co-002-test")
        second = build_execution_object(self.request(), created_by="co-002-test")
        self.assertEqual("pack.execution", first.object_type)
        self.assertEqual(first.object_id, second.object_id)
        self.assertEqual("trace-9", first.payload["trace_id"])
        self.assertEqual("task-42", first.payload["task_id"])

    def test_result_and_evidence_preserve_lineage(self):
        execution = build_execution_object(self.request(), created_by="co-002-test")
        receipt = ExecutionReceipt("receipt-1", "success", {"echo": "hello"}, None)
        result = build_result_object(execution, receipt, created_by="co-002-test")
        evidence = build_evidence_object(result, receipt, created_by="co-002-test")
        self.assertEqual("pack.result", result.object_type)
        self.assertEqual((execution.object_id,), result.lineage.derived_from)
        self.assertEqual(CORRELATION, result.payload["correlation_id"])
        self.assertEqual("artifact.evidence", evidence.object_type)
        self.assertEqual((result.object_id,), evidence.lineage.derived_from)
        self.assertEqual("receipt-1", evidence.payload["receipt_id"])

    def test_result_identity_changes_when_receipt_content_changes(self):
        execution = build_execution_object(self.request(), created_by="co-002-test")
        first = build_result_object(execution, ExecutionReceipt("receipt-1", "success", {"echo": "hello"}, None), created_by="co-002-test")
        second = build_result_object(execution, ExecutionReceipt("receipt-2", "success", {"echo": "HELLO"}, None), created_by="co-002-test")
        self.assertNotEqual(first.object_id, second.object_id)


if __name__ == "__main__":
    unittest.main()
