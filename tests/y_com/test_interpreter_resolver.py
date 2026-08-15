from pathlib import Path
import sys
import unittest

EXECUTION_ROOT = Path(__file__).resolve().parents[2] / "04_Execution"
sys.path.insert(0, str(EXECUTION_ROOT))

from y_com.interpreter import classify_surface, interpret_interaction


class InterpreterResolverTests(unittest.TestCase):
    def test_affirmative_surface_aliases_are_equivalent(self):
        for surface in ("O", "Oui", "oui", "OK", "Ok", "ok"):
            with self.subTest(surface=surface):
                self.assertEqual(classify_surface(surface), "AFFIRMATIVE")

    def test_choice_context_accepts_explicit_recommendation(self):
        act = interpret_interaction(
            surface="O",
            modality="text",
            interaction_context={
                "question_kind": "choice",
                "active_question_id": "q1",
                "recommended_option_id": "2",
            },
        )
        self.assertEqual(act["act"], "ACCEPT")
        self.assertEqual(act["value"], {"option_id": "2"})

    def test_binary_context_resolves_to_accept(self):
        act = interpret_interaction(
            surface="oui",
            modality="voice",
            interaction_context={
                "question_kind": "binary",
                "active_question_id": "q2",
                "recommended_option_id": None,
            },
        )
        self.assertEqual(act["act"], "ACCEPT")
        self.assertIsNone(act["value"])

    def test_continue_context_resolves_to_continue(self):
        act = interpret_interaction(
            surface="OK",
            modality="voice",
            interaction_context={
                "question_kind": "continue",
                "active_question_id": "q3",
                "recommended_option_id": None,
            },
        )
        self.assertEqual(act["act"], "CONTINUE")

    def test_choice_without_recommendation_is_unresolved(self):
        act = interpret_interaction(
            surface="O",
            modality="text",
            interaction_context={
                "question_kind": "choice",
                "active_question_id": "q4",
                "recommended_option_id": None,
            },
        )
        self.assertIsNone(act)

    def test_affirmative_without_active_context_is_unresolved(self):
        act = interpret_interaction(
            surface="O",
            modality="text",
            interaction_context={
                "question_kind": None,
                "active_question_id": None,
                "recommended_option_id": None,
            },
        )
        self.assertIsNone(act)


if __name__ == "__main__":
    unittest.main()
