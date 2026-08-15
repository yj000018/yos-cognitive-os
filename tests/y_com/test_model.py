from pathlib import Path
import sys
import unittest

EXECUTION_ROOT = Path(__file__).resolve().parents[2] / "04_Execution"
sys.path.insert(0, str(EXECUTION_ROOT))

from y_com.model import ALLOWED_ACTS, make_interaction_act


class InteractionActModelTests(unittest.TestCase):
    def test_v01_vocabulary_is_exact(self):
        self.assertEqual(
            ALLOWED_ACTS,
            frozenset({
                "ACCEPT",
                "REJECT",
                "CONTINUE",
                "CHOOSE",
                "REQUEST_CHOICE",
                "RECOMMEND",
            }),
        )

    def test_make_interaction_act_returns_canonical_shape(self):
        act = make_interaction_act(
            direction="human_to_ai",
            act="ACCEPT",
            value={"option_id": "2"},
            modality="text",
            surface="O",
            context={"active_question_id": "q1"},
        )
        self.assertEqual(act["version"], "0.1")
        self.assertEqual(act["direction"], "human_to_ai")
        self.assertEqual(act["act"], "ACCEPT")
        self.assertEqual(act["value"], {"option_id": "2"})
        self.assertEqual(act["source"], {"modality": "text", "surface": "O"})
        self.assertEqual(act["context"], {"active_question_id": "q1"})

    def test_unknown_act_is_rejected(self):
        with self.assertRaises(ValueError):
            make_interaction_act(direction="human_to_ai", act="MAYBE")

    def test_invalid_confidence_is_rejected(self):
        with self.assertRaises(ValueError):
            make_interaction_act(direction="human_to_ai", act="ACCEPT", confidence=1.1)


if __name__ == "__main__":
    unittest.main()
