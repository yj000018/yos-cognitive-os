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

from canonical_execution import ExecutionRequest, build_execution_object
from yarp_adapter import build_execution_transport_envelope, retry_envelope, validate_yarp_envelope

CORRELATION = "YARP-CORR-11111111-1111-4111-8111-111111111111"


def attempt_base(attempt_id: str) -> str:
    return attempt_id.rsplit("-", 1)[0]


class YarpAdapterTests(unittest.TestCase):
    def setUp(self):
        self.execution = build_execution_object(
            ExecutionRequest("task-42", "run-7", "trace-9", CORRELATION, "echo", {"value": "hello"}, ("execution_receipt",)),
            created_by="co-002-test",
        )

    def test_generic_execution_uses_yarp_envelope_compatibility_without_claiming_execute_mp(self):
        first = build_execution_transport_envelope(self.execution, sender_id="agent-chatgpt-ag", receiver_id="agent-test-executor")
        second = retry_envelope(first)
        self.assertEqual("CO002_EXECUTION_PILOT", first.message_type)
        self.assertNotEqual("EXECUTE_MP", first.message_type)
        self.assertEqual(self.execution.object_id, first.payload["canonical_object_id"])
        self.assertEqual(CORRELATION, first.correlation_id)
        self.assertEqual(first.correlation_id, second.correlation_id)
        self.assertNotEqual(first.envelope_id, second.envelope_id)
        self.assertNotEqual(first.attempt_id, second.attempt_id)
        self.assertEqual(attempt_base(first.attempt_id), attempt_base(second.attempt_id))
        self.assertEqual(2, second.attempt_number)
        self.assertEqual(self.execution.object_id, second.payload["canonical_object_id"])
        self.assertRegex(first.envelope_id, r"^YARP-ENV-[0-9a-f-]{36}$")
        self.assertRegex(first.attempt_id, r"^YARP-ATT-[0-9a-f-]{36}-001$")
        validate_yarp_envelope(first)
        validate_yarp_envelope(second)


if __name__ == "__main__":
    unittest.main()
