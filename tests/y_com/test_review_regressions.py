from pathlib import Path
import sys
import unittest

EXECUTION_ROOT = Path(__file__).resolve().parents[2] / "04_Execution"
sys.path.insert(0, str(EXECUTION_ROOT))

from y_com.model import make_interaction_act
from y_com.renderer import render_text


class ReviewRegressionTests(unittest.TestCase):
    def test_numeric_recommendation_id_matches_numeric_option_id(self):
        request = make_interaction_act(
            direction="ai_to_human",
            act="REQUEST_CHOICE",
            value={"options": [{"id": 1, "label": "A"}, {"id": 2, "label": "B"}]},
        )
        recommend = make_interaction_act(
            direction="ai_to_human",
            act="RECOMMEND",
            value={"option_id": 2},
        )
        self.assertEqual(render_text([request, recommend]), "Choose\n1. A\n★ 2. B")

    def test_boolean_confidence_is_rejected(self):
        for value in (True, False):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    make_interaction_act(
                        direction="human_to_ai",
                        act="ACCEPT",
                        confidence=value,
                    )


if __name__ == "__main__":
    unittest.main()
