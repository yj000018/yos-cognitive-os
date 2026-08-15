from pathlib import Path
import sys
import unittest

EXECUTION_ROOT = Path(__file__).resolve().parents[2] / "04_Execution"
sys.path.insert(0, str(EXECUTION_ROOT))

from y_com.universal_input_adapter import interaction_from_input_event


class UniversalInputAdapterTests(unittest.TestCase):
    def test_text_and_voice_inputs_converge_on_same_semantic_act(self):
        context = {
            "question_kind": "choice",
            "active_question_id": "q1",
            "recommended_option_id": "2",
        }
        text_act = interaction_from_input_event(
            {"channel": {"type": "text"}, "object": {"body": "O"}},
            interaction_context=context,
        )
        voice_act = interaction_from_input_event(
            {"channel": {"type": "voice"}, "object": {"body": "oui"}},
            interaction_context=context,
        )

        self.assertEqual(text_act["act"], "ACCEPT")
        self.assertEqual(voice_act["act"], "ACCEPT")
        self.assertEqual(text_act["value"], voice_act["value"])
        self.assertEqual(text_act["value"], {"option_id": "2"})
        self.assertEqual(text_act["source"]["modality"], "text")
        self.assertEqual(voice_act["source"]["modality"], "voice")

    def test_text_and_voice_negative_inputs_converge_on_reject(self):
        context = {
            "question_kind": "binary",
            "active_question_id": "q-neg",
            "recommended_option_id": None,
        }
        text_act = interaction_from_input_event(
            {"channel": {"type": "text"}, "object": {"body": "N"}},
            interaction_context=context,
        )
        voice_act = interaction_from_input_event(
            {"channel": {"type": "voice"}, "object": {"body": "non"}},
            interaction_context=context,
        )

        self.assertEqual(text_act["act"], "REJECT")
        self.assertEqual(voice_act["act"], "REJECT")
        self.assertEqual(text_act["source"]["modality"], "text")
        self.assertEqual(voice_act["source"]["modality"], "voice")

    def test_text_and_voice_cancel_inputs_converge_on_cancel(self):
        context = {
            "question_kind": None,
            "active_question_id": None,
            "recommended_option_id": None,
            "current_flow_id": "flow-1",
        }
        text_act = interaction_from_input_event(
            {"channel": {"type": "text"}, "object": {"body": "X"}},
            interaction_context=context,
        )
        voice_act = interaction_from_input_event(
            {"channel": {"type": "voice"}, "object": {"body": "stop"}},
            interaction_context=context,
        )

        self.assertEqual(text_act["act"], "CANCEL")
        self.assertEqual(voice_act["act"], "CANCEL")
        self.assertEqual(text_act["context"], {"current_flow_id": "flow-1"})
        self.assertEqual(voice_act["context"], {"current_flow_id": "flow-1"})
        self.assertEqual(text_act["source"]["modality"], "text")
        self.assertEqual(voice_act["source"]["modality"], "voice")

    def test_sensor_payload_is_not_magically_interpreted_as_y_com(self):
        act = interaction_from_input_event(
            {"channel": {"type": "sensor"}, "object": {"temperature_c": 31}},
            interaction_context={"question_kind": None},
        )
        self.assertIsNone(act)

    def test_unknown_text_is_unresolved_not_invented(self):
        act = interaction_from_input_event(
            {"channel": {"type": "text"}, "object": {"body": "perhaps"}},
            interaction_context={"question_kind": "binary"},
        )
        self.assertIsNone(act)


if __name__ == "__main__":
    unittest.main()
