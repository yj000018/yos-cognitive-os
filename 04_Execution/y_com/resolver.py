from __future__ import annotations

from .model import make_interaction_act


def resolve_affirmative(*, modality: str, surface: str, interaction_context: dict) -> dict | None:
    kind = interaction_context.get("question_kind")
    question_id = interaction_context.get("active_question_id")
    recommended = interaction_context.get("recommended_option_id")

    context = {}
    if question_id is not None:
        context["active_question_id"] = question_id

    if kind == "choice":
        if recommended is None:
            return None
        context["recommended_option_id"] = recommended
        return make_interaction_act(
            direction="human_to_ai",
            act="ACCEPT",
            value={"option_id": recommended},
            modality=modality,
            surface=surface,
            context=context,
        )

    if kind == "binary":
        return make_interaction_act(
            direction="human_to_ai",
            act="ACCEPT",
            modality=modality,
            surface=surface,
            context=context,
        )

    if kind == "continue":
        return make_interaction_act(
            direction="human_to_ai",
            act="CONTINUE",
            modality=modality,
            surface=surface,
            context=context,
        )

    return None


def resolve_negative(*, modality: str, surface: str, interaction_context: dict) -> dict | None:
    kind = interaction_context.get("question_kind")
    question_id = interaction_context.get("active_question_id")
    recommended = interaction_context.get("recommended_option_id")

    context = {}
    if question_id is not None:
        context["active_question_id"] = question_id

    if kind == "binary":
        return make_interaction_act(
            direction="human_to_ai",
            act="REJECT",
            modality=modality,
            surface=surface,
            context=context,
        )

    if kind == "choice" and recommended is not None:
        context["recommended_option_id"] = recommended
        return make_interaction_act(
            direction="human_to_ai",
            act="REJECT",
            value={"option_id": recommended},
            modality=modality,
            surface=surface,
            context=context,
        )

    return None


def resolve_cancel(*, modality: str, surface: str, interaction_context: dict) -> dict | None:
    flow_id = interaction_context.get("current_flow_id")
    if flow_id is None:
        return None

    return make_interaction_act(
        direction="human_to_ai",
        act="CANCEL",
        modality=modality,
        surface=surface,
        context={"current_flow_id": flow_id},
    )
