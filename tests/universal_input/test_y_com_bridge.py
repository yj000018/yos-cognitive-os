from pathlib import Path
import sys
import unittest

EXECUTION_ROOT = Path(__file__).resolve().parents[2] / "04_Execution"
sys.path.insert(0, str(EXECUTION_ROOT))

from universal_input.event import make_input_event
from y_com.universal_input_adapter import interaction_from_input_event


class UniversalInputYComBridgeTests(unittest.TestCase):
    def test_text_and_voice_converge_to_same_y_com_meaning(self):
        context = {
            "question_kind": "choice",
            "active_question_id": "q1",
            "recommended_option_id": "2",
        }
        text_event = make_input_event(channel_type="text", body="O", source_ref="chat:1")
        voice_event = make_input_event(channel_type="voice", body="oui", source_ref="voice:1")

        text_act = interaction_from_input_event(text_event, interaction_context=context)
        voice_act = interaction_from_input_event(voice_event, interaction_context=context)

        self.assertEqual(text_act["act"], "ACCEPT")
        self.assertEqual(voice_act["act"], "ACCEPT")
        self.assertEqual(text_act["value"], {"option_id": "2"})
        self.assertEqual(text_act["value"], voice_act["value"])
        self.assertEqual(text_act["source"]["modality"], "text")
        self.assertEqual(voice_act["source"]["modality"], "voice")

    def test_sensor_event_without_interaction_surface_does_not_enter_y_com(self):
        event = make_input_event(
            channel_type="sensor",
            body=None,
            source_ref="weather:sensor-1",
            object_type="sensor_reading",
            object_metadata={"temperature_c": 31},
        )
        self.assertIsNone(
            interaction_from_input_event(
                event,
                interaction_context={"question_kind": None},
            )
        )


if __name__ == "__main__":
    unittest.main()
