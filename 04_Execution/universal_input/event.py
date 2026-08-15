from __future__ import annotations

import hashlib
import json

ALLOWED_CHANNEL_TYPES = frozenset({
    "text",
    "voice",
    "email",
    "share",
    "messaging",
    "browser",
    "api",
    "sensor",
})


def _stable_event_id(payload: dict) -> str:
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "evt_" + hashlib.sha256(encoded).hexdigest()[:24]


def make_input_event(
    *,
    channel_type: str,
    body: str | None,
    source_ref: str,
    received_at: str | None = None,
    object_type: str = "text",
    object_metadata: dict | None = None,
    context: dict | None = None,
) -> dict:
    if channel_type not in ALLOWED_CHANNEL_TYPES:
        raise ValueError(f"unsupported input channel: {channel_type}")
    if body is not None and not isinstance(body, str):
        raise ValueError("body must be a string or None")
    if not isinstance(source_ref, str) or not source_ref.strip():
        raise ValueError("source_ref must be a non-empty string")

    metadata = dict(object_metadata or {})
    event_identity = {
        "channel_type": channel_type,
        "body": body,
        "source_ref": source_ref,
        "object_type": object_type,
        "object_metadata": metadata,
    }

    return {
        "event_id": _stable_event_id(event_identity),
        "received_at": received_at,
        "channel": {
            "type": channel_type,
            "metadata": {},
        },
        "mode": {
            "value": "yos",
            "source": "default",
        },
        "intent": {
            "value": "auto",
            "source": "default",
        },
        "context": dict(context or {}),
        "object": {
            "type": object_type,
            "body": body,
            "metadata": metadata,
        },
        "routing": {
            "workflow": None,
            "agents": [],
            "destinations": [],
        },
        "provenance": {
            "raw_source_ref": source_ref,
        },
    }
