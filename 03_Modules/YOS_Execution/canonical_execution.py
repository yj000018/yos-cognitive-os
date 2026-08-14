from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
from typing import Any
import json

from canonical_objects import CanonicalLineage, CanonicalObject, SCHEMA_VERSION, content_sha256


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _stable_id(object_type: str, semantic: Any) -> str:
    raw = json.dumps(semantic, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    digest = sha256(f"{object_type}|{raw}".encode("utf-8")).hexdigest()[:24]
    return f"co:{object_type}:{digest}"


@dataclass(frozen=True)
class ExecutionRequest:
    task_id: str
    run_id: str
    trace_id: str
    correlation_id: str
    capability: str
    input_payload: dict[str, Any]
    expected_evidence: tuple[str, ...] = ()


@dataclass(frozen=True)
class ExecutionReceipt:
    receipt_id: str
    outcome: str
    output: dict[str, Any] | None
    error: dict[str, Any] | None


@dataclass(frozen=True)
class ExecutionTrace:
    trace_id: str
    correlation_id: str
    task_id: str
    run_id: str
    execution_object_id: str
    result_object_id: str
    evidence_object_ids: tuple[str, ...]
    yarp_envelope_ids: tuple[str, ...]
    attempt_ids: tuple[str, ...]
    outcome: str


def _object(*, object_type: str, semantic: Any, payload: dict[str, Any], created_by: str, lineage: CanonicalLineage, domain_owner: str) -> CanonicalObject:
    return CanonicalObject(
        object_id=_stable_id(object_type, semantic),
        object_type=object_type,
        schema_version=SCHEMA_VERSION,
        created_at=_utc_now_iso(),
        created_by=created_by,
        provenance={"producer": "YOS_Execution.CO-002"},
        lineage=lineage,
        context_refs=(),
        payload=payload,
        integrity={"content_sha256": content_sha256(payload)},
        governance={"mutation_strategy": "IMMUTABLE", "domain_owner": domain_owner},
        record_state="active",
    )


def build_execution_object(request: ExecutionRequest, *, created_by: str) -> CanonicalObject:
    payload = {
        "task_id": request.task_id,
        "run_id": request.run_id,
        "trace_id": request.trace_id,
        "correlation_id": request.correlation_id,
        "capability": request.capability,
        "input_payload": request.input_payload,
        "expected_evidence": list(request.expected_evidence),
    }
    return _object(object_type="pack.execution", semantic=payload, payload=payload, created_by=created_by, lineage=CanonicalLineage(transformed_by=("YOS_Execution.CO-002",)), domain_owner="EHS")


def build_result_object(execution: CanonicalObject, receipt: ExecutionReceipt, *, created_by: str) -> CanonicalObject:
    payload = {
        "task_id": execution.payload["task_id"],
        "run_id": execution.payload["run_id"],
        "trace_id": execution.payload["trace_id"],
        "correlation_id": execution.payload["correlation_id"],
        "execution_object_id": execution.object_id,
        "outcome": receipt.outcome,
        "receipt_id": receipt.receipt_id,
        "output": receipt.output,
        "error": receipt.error,
    }
    semantic = {"execution_object_id": execution.object_id, "receipt": payload}
    return _object(object_type="pack.result", semantic=semantic, payload=payload, created_by=created_by, lineage=CanonicalLineage(derived_from=(execution.object_id,), transformed_by=("YOS_Execution.CO-002",)), domain_owner="EHS")


def build_evidence_object(result: CanonicalObject, receipt: ExecutionReceipt, *, created_by: str) -> CanonicalObject:
    evidence = receipt.output if receipt.output is not None else {"error": receipt.error}
    payload = {
        "trace_id": result.payload["trace_id"],
        "correlation_id": result.payload["correlation_id"],
        "result_object_id": result.object_id,
        "receipt_id": receipt.receipt_id,
        "evidence": evidence,
    }
    semantic = {"result_object_id": result.object_id, "receipt_id": receipt.receipt_id, "evidence": evidence}
    return _object(object_type="artifact.evidence", semantic=semantic, payload=payload, created_by=created_by, lineage=CanonicalLineage(derived_from=(result.object_id,), transformed_by=("YOS_Execution.CO-002",)), domain_owner="Executor")


def build_execution_trace(execution: CanonicalObject, result: CanonicalObject, evidence: tuple[CanonicalObject, ...], envelopes: tuple[Any, ...]) -> ExecutionTrace:
    return ExecutionTrace(
        trace_id=execution.payload["trace_id"],
        correlation_id=execution.payload["correlation_id"],
        task_id=execution.payload["task_id"],
        run_id=execution.payload["run_id"],
        execution_object_id=execution.object_id,
        result_object_id=result.object_id,
        evidence_object_ids=tuple(item.object_id for item in evidence),
        yarp_envelope_ids=tuple(item.envelope_id for item in envelopes),
        attempt_ids=tuple(item.attempt_id for item in envelopes),
        outcome=result.payload["outcome"],
    )
