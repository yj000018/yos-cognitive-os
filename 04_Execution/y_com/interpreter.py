from __future__ import annotations

from .resolver import resolve_affirmative

_AFFIRMATIVE_SURFACES = frozenset({"o", "oui", "ok"})


def classify_surface(surface: str) -> str | None:
    normalized = surface.strip().casefold()
    if normalized in _AFFIRMATIVE_SURFACES:
        return "AFFIRMATIVE"
    return None


def interpret_interaction(*, surface: str, modality: str, interaction_context: dict) -> dict | None:
    candidate = classify_surface(surface)
    if candidate == "AFFIRMATIVE":
        return resolve_affirmative(
            modality=modality,
            surface=surface,
            interaction_context=interaction_context,
        )
    return None
