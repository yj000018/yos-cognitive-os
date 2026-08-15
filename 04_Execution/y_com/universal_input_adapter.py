from __future__ import annotations

from .interpreter import interpret_interaction


def interaction_from_input_event(event: dict, *, interaction_context: dict) -> dict | None:
    channel = event.get("channel") or {}
    obj = event.get("object") or {}
    surface = obj.get("body")
    if not isinstance(surface, str):
        return None

    modality = str(channel.get("type") or "unknown")
    return interpret_interaction(
        surface=surface,
        modality=modality,
        interaction_context=interaction_context,
    )
