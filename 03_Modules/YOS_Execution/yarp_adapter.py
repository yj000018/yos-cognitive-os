from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any
import re
import uuid

from canonical_objects import CanonicalObject

UUID_RE = r"[0-9a-f-]{36}"
ENVELOPE_RE = re.compile(rf"^YARP-ENV-{UUID_RE}$")
CORRELATION_RE = re.compile(rf"^YARP-CORR-{UUID_RE}$")
ATTEMPT_RE = re.compile(rf"^YARP-ATT-{UUID_RE}-[0-9]{{3}}$")
SUPPORTED_MESSAGE_TYPES = {"EXECUTE_MP"}


class YarpTransportError(ValueError):
    pass


@dataclass(frozen=True)
class YarpEnvelope:
    yarp_version: str
    envelope_id: str
    message_type: str
    correlation_id: str
    conversation_id: str | None
    sender_id: str
    receiver_id: str
    sent_at: str
    attempt_id: str
    attempt_number: int
    ttl_seconds: int | None
    transport_id: str | None
    payload: dict[str, Any]


def _uuid() -> str:
    return str(uuid.uuid4())


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _attempt_id(number: int) -> str:
    return f"YARP-ATT-{_uuid()}-{number:03d}"


def build_execute_envelope(execution: CanonicalObject, *, sender_id: str, receiver_id: str, attempt_number: int = 1, conversation_id: str | None = None) -> YarpEnvelope:
    envelope = YarpEnvelope(
        yarp_version="1.0",
        envelope_id=f"YARP-ENV-{_uuid()}",
        message_type="EXECUTE_MP",
        correlation_id=execution.payload["correlation_id"],
        conversation_id=conversation_id,
        sender_id=sender_id,
        receiver_id=receiver_id,
        sent_at=_now(),
        attempt_id=_attempt_id(attempt_number),
        attempt_number=attempt_number,
        ttl_seconds=300,
        transport_id="co-002-in-process",
        payload={"canonical_object_id": execution.object_id, "execution": execution.payload},
    )
    validate_yarp_envelope(envelope)
    return envelope


def retry_envelope(previous: YarpEnvelope) -> YarpEnvelope:
    number = previous.attempt_number + 1
    envelope = YarpEnvelope(
        yarp_version=previous.yarp_version,
        envelope_id=f"YARP-ENV-{_uuid()}",
        message_type=previous.message_type,
        correlation_id=previous.correlation_id,
        conversation_id=previous.conversation_id,
        sender_id=previous.sender_id,
        receiver_id=previous.receiver_id,
        sent_at=_now(),
        attempt_id=_attempt_id(number),
        attempt_number=number,
        ttl_seconds=previous.ttl_seconds,
        transport_id=previous.transport_id,
        payload=previous.payload,
    )
    validate_yarp_envelope(envelope)
    return envelope


def validate_yarp_envelope(envelope: YarpEnvelope) -> None:
    if envelope.yarp_version != "1.0":
        raise YarpTransportError("unsupported YARP version")
    if envelope.message_type not in SUPPORTED_MESSAGE_TYPES:
        raise YarpTransportError("unsupported message type")
    if not ENVELOPE_RE.fullmatch(envelope.envelope_id):
        raise YarpTransportError("invalid envelope_id")
    if not CORRELATION_RE.fullmatch(envelope.correlation_id):
        raise YarpTransportError("invalid correlation_id")
    if envelope.attempt_number < 1:
        raise YarpTransportError("attempt_number must be >= 1")
    if not ATTEMPT_RE.fullmatch(envelope.attempt_id):
        raise YarpTransportError("invalid attempt_id")
    if not envelope.sender_id or not envelope.receiver_id:
        raise YarpTransportError("sender_id and receiver_id are required")
    if not isinstance(envelope.payload, dict) or not envelope.payload.get("canonical_object_id"):
        raise YarpTransportError("canonical_object_id is required")
