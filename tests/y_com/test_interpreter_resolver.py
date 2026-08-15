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

    def test_negative_surface_aliases_are_equivalent(self):
        for surface in ("N", "n", "non", "Non", "no", "NO"):
            with self.subTest(surface=surface):
                self.assertEqual(classify_surface(surface), "NEGATIVE")

    def test_cancel_surface_aliases_are_equivalent(self):
        for surface in ("X", "x", "stop", "STOP", "annule", "Annule", "cancel", "CANCEL"):
            with self.subTest(surface=surface):
                self.assertEqual(classify_surface(surface), "CANCEL")

    def test_numeric_surfaces_classify_as_choice(self):
        for surface in ("1", "2", "10", " 2 "):
            with self.subTest(surface=surface):
                self.assertEqual(classify_surface(surface), "CHOICE")

    def test_numeric_natural_language_variants_remain_unresolved(self):
        for surface in ("option 2", "the second", "deux", "2 please", "2."):
            with self.subTest(surface=surface):
                self.assertIsNone(classify_surface(surface))

    def test_active_numeric_option_resolves_to_choose(self):
        act = interpret_interaction(
            surface="2",
            modality="text",
            interaction_context={
                "question_kind": "choice",
                "active_question_id": "q-choice-1",
                "recommended_option_id": "1",
                "active_option_ids": ["1", "2", "3"],
            },
        )
        self.assertEqual(act["act"], "CHOOSE")
        self.assertEqual(act["value"], {"option_id": "2"})
        self.assertEqual(act["context"], {"active_question_id": "q-choice-1"})

    def test_numeric_choice_strips_only_surrounding_whitespace(self):
        act = interpret_interaction(
            surface=" 10 ",
            modality="text",
            interaction_context={
                "question_kind": "choice",
                "active_question_id": "q-choice-2",
                "active_option_ids": ["10", "11"],
            },
        )
        self.assertEqual(act["act"], "CHOOSE")
        self.assertEqual(act["value"], {"option_id": "10"})
        self.assertEqual(act["source"]["surface"], " 10 ")

    def test_non_member_numeric_choice_is_unresolved(self):
        act = interpret_interaction(
            surface="7",
            modality="text",
            interaction_context={
                "question_kind": "choice",
                "active_question_id": "q-choice-3",
                "active_option_ids": ["1", "2", "3"],
            },
        )
        self.assertIsNone(act)

    def test_numeric_input_outside_choice_context_is_unresolved(self):
        act = interpret_interaction(
            surface="1",
            modality="text",
            interaction_context={
                "question_kind": "binary",
                "active_question_id": "q-binary-1",
                "active_option_ids": ["1", "2"],
            },
        )
        self.assertIsNone(act)

    def test_numeric_choice_without_active_option_ids_is_unresolved(self):
        act = interpret_interaction(
            surface="2",
            modality="text",
            interaction_context={
                "question_kind": "choice",
                "active_question_id": "q-choice-4",
                "active_option_ids": None,
            },
        )
        self.assertIsNone(act)

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

    def test_binary_context_resolves_negative_to_reject(self):
        act = interpret_interaction(
            surface="N",
            modality="text",
            interaction_context={
                "question_kind": "binary",
                "active_question_id": "q-neg-1",
                "recommended_option_id": None,
            },
        )
        self.assertEqual(act["act"], "REJECT")
        self.assertEqual(act["context"], {"active_question_id": "q-neg-1"})

    def test_recommended_choice_resolves_negative_to_reject(self):
        act = interpret_interaction(
            surface="non",
            modality="voice",
            interaction_context={
                "question_kind": "choice",
                "active_question_id": "q-neg-2",
                "recommended_option_id": "2",
            },
        )
        self.assertEqual(act["act"], "REJECT")
        self.assertEqual(act["value"], {"option_id": "2"})

    def test_negative_without_rejectable_context_is_unresolved(self):
        act = interpret_interaction(
            surface="N",
            modality="text",
            interaction_context={
                "question_kind": None,
                "active_question_id": None,
                "recommended_option_id": None,
            },
        )
        self.assertIsNone(act)

    def test_current_flow_resolves_cancel(self):
        act = interpret_interaction(
            surface="X",
            modality="text",
            interaction_context={
                "question_kind": None,
                "active_question_id": None,
                "recommended_option_id": None,
                "current_flow_id": "flow-1",
            },
        )
        self.assertEqual(act["act"], "CANCEL")
        self.assertEqual(act["context"], {"current_flow_id": "flow-1"})

    def test_cancel_without_current_flow_is_unresolved(self):
        act = interpret_interaction(
            surface="X",
            modality="text",
            interaction_context={
                "question_kind": None,
                "active_question_id": None,
                "recommended_option_id": None,
                "current_flow_id": None,
            },
        )
        self.assertIsNone(act)

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
