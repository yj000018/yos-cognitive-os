from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
from typing import Any
import json

SCHEMA_VERSION = "1.0"
RECORD_STATES = {"draft", "active", "historical", "invalidated"}


def _canonical_bytes(value: Any) -> bytes:
    if isinstance(value, str):
        return value.encode("utf-8")
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def content_sha256(value: Any) -> str:
    return sha256(_canonical_bytes(value)).hexdigest()


@dataclass(frozen=True)
class CanonicalLineage:
    source_refs: tuple[str, ...] = ()
    derived_from: tuple[str, ...] = ()
    transformed_by: tuple[str, ...] = ()
    supersedes: tuple[str, ...] = ()
    superseded_by: tuple[str, ...] = ()
    related_objects: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, list[str]]:
        return {
            "source_refs": list(self.source_refs),
            "derived_from": list(self.derived_from),
            "transformed_by": list(self.transformed_by),
            "supersedes": list(self.supersedes),
            "superseded_by": list(self.superseded_by),
            "related_objects": list(self.related_objects),
        }


@dataclass(frozen=True)
class CanonicalObject:
    object_id: str
    object_type: str
    schema_version: str
    created_at: str
    created_by: str
    provenance: dict[str, Any]
    lineage: CanonicalLineage
    context_refs: tuple[str, ...]
    payload: dict[str, Any]
    integrity: dict[str, str]
    governance: dict[str, Any]
    record_state: str

    def __post_init__(self) -> None:
        if self.record_state not in RECORD_STATES:
            raise ValueError(f"invalid record_state: {self.record_state}")
        if not self.object_id:
            raise ValueError("object_id is required")
        if not self.object_type:
            raise ValueError("object_type is required")

    def to_dict(self) -> dict[str, Any]:
        return {
            "object_id": self.object_id,
            "object_type": self.object_type,
            "schema_version": self.schema_version,
            "created_at": self.created_at,
            "created_by": self.created_by,
            "provenance": self.provenance,
            "lineage": self.lineage.to_dict(),
            "context_refs": list(self.context_refs),
            "payload": self.payload,
            "integrity": self.integrity,
            "governance": self.governance,
            "record_state": self.record_state,
        }


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _stable_object_id(transaction_id: str, object_type: str) -> str:
    digest = sha256(f"{transaction_id}|{object_type}".encode("utf-8")).hexdigest()[:24]
    return f"co:{object_type}:{digest}"


def _mutation_dict(mutation: Any) -> dict[str, Any]:
    return {
        "action": mutation.action,
        "path": mutation.path,
        "candidate_id": mutation.candidate_id,
        "preserve_history": mutation.preserve_history,
        "lineage_ref": mutation.lineage_ref,
    }


def build_conversation_delta_object(*, transaction: Any, candidates: list[Any], created_by: str, source_refs: tuple[str, ...], context_refs: tuple[str, ...] = ()) -> CanonicalObject:
    mutations = [_mutation_dict(m) for m in [*transaction.amend, *transaction.create]]
    candidate_payload = [
        {
            "candidate_id": c.candidate_id,
            "topic": c.topic,
            "fingerprint": c.fingerprint,
            "relation": c.relation,
            "supersedes": c.supersedes,
            "provenance": c.provenance,
        }
        for c in candidates
    ]
    supersedes = tuple(dict.fromkeys(c.supersedes for c in candidates if c.supersedes))
    payload = {
        "transaction_id": transaction.transaction_id,
        "status": transaction.status,
        "candidate_count": len(candidates),
        "candidates": candidate_payload,
        "reconciliation": transaction.reconciliation,
        "mutations": mutations,
        "final_marker": transaction.final_marker,
        "offline_queue_package_id": transaction.offline_queue_package_id,
    }
    return CanonicalObject(
        object_id=_stable_object_id(transaction.transaction_id, "pack.conversation_delta"),
        object_type="pack.conversation_delta",
        schema_version=SCHEMA_VERSION,
        created_at=_utc_now_iso(),
        created_by=created_by,
        provenance={"producer": "YOS_Memory.Preserve", "transaction_id": transaction.transaction_id},
        lineage=CanonicalLineage(source_refs=source_refs, transformed_by=("YOS_Memory.Preserve",), supersedes=supersedes),
        context_refs=context_refs,
        payload=payload,
        integrity={"content_sha256": content_sha256(payload)},
        governance={"mutation_strategy": "VERSIONED", "domain_owner": "YOS_Memory"},
        record_state="active",
    )


def build_preservation_event_object(*, transaction: Any, conversation_delta: CanonicalObject, created_by: str, verified_remote_sha: str | None = None, context_refs: tuple[str, ...] = ()) -> CanonicalObject:
    status = "VERIFIED" if verified_remote_sha else transaction.status
    payload: dict[str, Any] = {
        "transaction_id": transaction.transaction_id,
        "status": status,
        "conversation_delta_object_id": conversation_delta.object_id,
        "offline_queue_package_id": transaction.offline_queue_package_id,
    }
    if verified_remote_sha:
        payload["verified_remote_sha"] = verified_remote_sha
    return CanonicalObject(
        object_id=_stable_object_id(transaction.transaction_id, "event.preservation"),
        object_type="event.preservation",
        schema_version=SCHEMA_VERSION,
        created_at=_utc_now_iso(),
        created_by=created_by,
        provenance={"producer": "YOS_Memory.Preserve", "transaction_id": transaction.transaction_id},
        lineage=CanonicalLineage(derived_from=(conversation_delta.object_id,), transformed_by=("YOS_Memory.Preserve",)),
        context_refs=context_refs,
        payload=payload,
        integrity={"content_sha256": content_sha256(payload)},
        governance={"mutation_strategy": "IMMUTABLE", "domain_owner": "YOS_Memory", "verification_required": True},
        record_state="active",
    )
