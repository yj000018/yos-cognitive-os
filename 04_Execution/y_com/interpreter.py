from __future__ import annotations

from .resolver import resolve_affirmative, resolve_cancel, resolve_negative

_AFFIRMATIVE_SURFACES = frozenset({"o", "oui", "ok"})
_NEGATIVE_SURFACES = frozenset({"n", "non", "no"})
_CANCEL_SURFACES = frozenset({"x", "stop", "annule", "cancel"})


def classify_surface(surface: str) -> str | None:
    normalized = surface.strip().casefold()
    if normalized in _AFFIRMATIVE_SURFACES:
        return "AFFIRMATIVE"
    if normalized in _NEGATIVE_SURFACES:
        return "NEGATIVE"
    if normalized in _CANCEL_SURFACES:
        return "CANCEL"
    return None


def interpret_interaction(*, surface: str, modality: str, interaction_context: dict) -> dict | None:
    candidate = classify_surface(surface)
    if candidate == "AFFIRMATIVE":
        return resolve_affirmative(
            modality=modality,
            surface=surface,
            interaction_context=interaction_context,
        )
    if candidate == "NEGATIVE":
        return resolve_negative(
            modality=modality,
            surface=surface,
            interaction_context=interaction_context,
        )
    if candidate == "CANCEL":
        return resolve_cancel(
            modality=modality,
            surface=surface,
            interaction_context=interaction_context,
        )
    return None
