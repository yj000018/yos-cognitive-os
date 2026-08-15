from __future__ import annotations

ALLOWED_ACTS = frozenset({
    "ACCEPT",
    "REJECT",
    "CONTINUE",
    "CHOOSE",
    "REQUEST_CHOICE",
    "RECOMMEND",
    "CANCEL",
})

ALLOWED_DIRECTIONS = frozenset({"human_to_ai", "ai_to_human"})


def make_interaction_act(
    *,
    direction: str,
    act: str,
    value=None,
    confidence: float = 1.0,
    modality: str = "unknown",
    surface: str | None = None,
    context: dict | None = None,
) -> dict:
    if direction not in ALLOWED_DIRECTIONS:
        raise ValueError(f"unsupported direction: {direction}")
    if act not in ALLOWED_ACTS:
        raise ValueError(f"unsupported Y-COM act: {act}")
    if isinstance(confidence, bool) or not 0.0 <= confidence <= 1.0:
        raise ValueError("confidence must be a number between 0.0 and 1.0")

    return {
        "version": "0.1",
        "direction": direction,
        "act": act,
        "value": value,
        "confidence": confidence,
        "source": {"modality": modality, "surface": surface},
        "context": dict(context or {}),
    }
