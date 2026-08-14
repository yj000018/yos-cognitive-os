from __future__ import annotations

from hashlib import sha256
from typing import Any
import json

from canonical_execution import ExecutionReceipt, verify_canonical_object_integrity
from canonical_objects import CanonicalObject
from yarp_adapter import YarpEnvelope, YarpTransportError, validate_yarp_envelope


class DeterministicExecutor:
    def execute(self, envelope: YarpEnvelope, execution: CanonicalObject) -> ExecutionReceipt:
        validate_yarp_envelope(envelope)
        if envelope.payload.get("canonical_object_id") != execution.object_id:
            raise YarpTransportError("envelope canonical_object_id does not match execution")
        if envelope.payload.get("execution") != execution.payload:
            raise YarpTransportError("envelope execution snapshot does not match canonical object")
        verify_canonical_object_integrity(execution)

        capability = execution.payload.get("capability")
        inputs = execution.payload.get("input_payload")
        if not isinstance(inputs, dict):
            return self._receipt(execution, envelope, None, {"code": "CO002_INVALID_INPUT", "message": "input_payload must be an object"}, "failure")

        if capability == "echo":
            if "value" not in inputs:
                return self._receipt(execution, envelope, None, {"code": "CO002_INVALID_INPUT", "message": "echo requires value"}, "failure")
            output, error, outcome = {"echo": inputs["value"]}, None, "success"
        elif capability == "add":
            a, b = inputs.get("a"), inputs.get("b")
            if not isinstance(a, int) or isinstance(a, bool) or not isinstance(b, int) or isinstance(b, bool):
                output, error, outcome = None, {"code": "CO002_INVALID_INPUT", "message": "add requires integer a and b"}, "failure"
            else:
                output, error, outcome = {"sum": a + b}, None, "success"
        elif capability == "fail":
            message = str(inputs.get("message", "controlled failure"))[:512]
            output, error, outcome = None, {"code": "CO002_CONTROLLED_FAILURE", "message": message}, "failure"
        else:
            output, error, outcome = None, {"code": "CO002_UNSUPPORTED_CAPABILITY", "message": str(capability)[:128]}, "failure"
        return self._receipt(execution, envelope, output, error, outcome)

    @staticmethod
    def _receipt(execution: CanonicalObject, envelope: YarpEnvelope, output: dict[str, Any] | None, error: dict[str, Any] | None, outcome: str) -> ExecutionReceipt:
        semantic: dict[str, Any] = {
            "execution_object_id": execution.object_id,
            "attempt_id": envelope.attempt_id,
            "outcome": outcome,
            "output": output,
            "error": error,
        }
        raw = json.dumps(semantic, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        receipt_id = "co002-receipt:" + sha256(raw.encode("utf-8")).hexdigest()[:24]
        return ExecutionReceipt(receipt_id=receipt_id, outcome=outcome, output=output, error=error)
