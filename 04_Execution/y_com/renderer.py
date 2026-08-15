from __future__ import annotations


def render_text(acts: list[dict]) -> str:
    requests = [act for act in acts if act.get("act") == "REQUEST_CHOICE"]
    recommendations = [act for act in acts if act.get("act") == "RECOMMEND"]

    if len(requests) != 1 or len(recommendations) > 1:
        raise ValueError("v0.1 text renderer expects one REQUEST_CHOICE and at most one RECOMMEND")

    options = requests[0].get("value", {}).get("options", [])
    if not options:
        raise ValueError("REQUEST_CHOICE requires at least one option")

    recommended_id = None
    if recommendations:
        recommended_id = recommendations[0].get("value", {}).get("option_id")
        if recommended_id not in {str(option["id"]) for option in options}:
            raise ValueError("recommended option does not exist")

    lines = ["Choose"]
    for option in options:
        option_id = str(option["id"])
        prefix = "★ " if option_id == recommended_id else ""
        lines.append(f"{prefix}{option_id}. {option['label']}")
    return "\n".join(lines)
