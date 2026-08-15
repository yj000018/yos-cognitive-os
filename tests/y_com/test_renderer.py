from pathlib import Path
import sys
import unittest

EXECUTION_ROOT = Path(__file__).resolve().parents[2] / "04_Execution"
sys.path.insert(0, str(EXECUTION_ROOT))

from y_com.model import make_interaction_act
from y_com.renderer import render_text


class RendererTests(unittest.TestCase):
    def test_choice_renderer_numbers_options_and_marks_recommendation(self):
        request = make_interaction_act(
            direction="ai_to_human",
            act="REQUEST_CHOICE",
            value={
                "options": [
                    {"id": "1", "label": "Minimal patch"},
                    {"id": "2", "label": "Hybrid patch"},
                    {"id": "3", "label": "Full redesign"},
                ]
            },
        )
        recommend = make_interaction_act(
            direction="ai_to_human",
            act="RECOMMEND",
            value={"option_id": "2"},
        )

        self.assertEqual(
            render_text([request, recommend]),
            "Choose\n1. Minimal patch\n★ 2. Hybrid patch\n3. Full redesign",
        )

    def test_renderer_without_recommendation_has_no_star(self):
        request = make_interaction_act(
            direction="ai_to_human",
            act="REQUEST_CHOICE",
            value={"options": [{"id": "1", "label": "A"}, {"id": "2", "label": "B"}]},
        )
        rendered = render_text([request])
        self.assertEqual(rendered, "Choose\n1. A\n2. B")
        self.assertNotIn("★", rendered)

    def test_recommendation_must_reference_existing_option(self):
        request = make_interaction_act(
            direction="ai_to_human",
            act="REQUEST_CHOICE",
            value={"options": [{"id": "1", "label": "A"}]},
        )
        recommend = make_interaction_act(
            direction="ai_to_human",
            act="RECOMMEND",
            value={"option_id": "9"},
        )
        with self.assertRaises(ValueError):
            render_text([request, recommend])

    def test_renderer_rejects_unsupported_extra_act(self):
        request = make_interaction_act(
            direction="ai_to_human",
            act="REQUEST_CHOICE",
            value={"options": [{"id": "1", "label": "A"}]},
        )
        extra = make_interaction_act(
            direction="human_to_ai",
            act="ACCEPT",
        )
        with self.assertRaises(ValueError):
            render_text([request, extra])


if __name__ == "__main__":
    unittest.main()
