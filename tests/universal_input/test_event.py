from pathlib import Path
import sys
import unittest

EXECUTION_ROOT = Path(__file__).resolve().parents[2] / "04_Execution"
sys.path.insert(0, str(EXECUTION_ROOT))

from universal_input.event import ALLOWED_CHANNEL_TYPES, make_input_event


class UniversalInputEventTests(unittest.TestCase):
    def test_core_channel_set_is_modality_neutral(self):
        self.assertEqual(
            ALLOWED_CHANNEL_TYPES,
            frozenset({"text", "voice", "email", "share", "messaging", "browser", "api", "sensor"}),
        )

    def test_builds_canonical_minimal_event(self):
        event = make_input_event(
            channel_type="text",
            body="O",
            source_ref="chat:message-1",
            received_at="2026-08-15T14:37:00+02:00",
        )
        self.assertTrue(event["event_id"].startswith("evt_"))
        self.assertEqual(event["received_at"], "2026-08-15T14:37:00+02:00")
        self.assertEqual(event["channel"]["type"], "text")
        self.assertEqual(event["mode"], {"value": "yos", "source": "default"})
        self.assertEqual(event["intent"], {"value": "auto", "source": "default"})
        self.assertEqual(event["object"], {"type": "text", "body": "O", "metadata": {}})
        self.assertEqual(event["provenance"]["raw_source_ref"], "chat:message-1")

    def test_same_input_has_same_event_id(self):
        kwargs = {
            "channel_type": "voice",
            "body": "oui",
            "source_ref": "voice:utterance-1",
            "received_at": "2026-08-15T14:37:00+02:00",
        }
        self.assertEqual(make_input_event(**kwargs)["event_id"], make_input_event(**kwargs)["event_id"])

    def test_source_ref_is_required_to_distinguish_event_occurrences(self):
        with self.assertRaises(ValueError):
            make_input_event(channel_type="text", body="O", source_ref=None)

    def test_context_enrichment_does_not_change_ingress_identity(self):
        base = dict(channel_type="text", body="O", source_ref="chat:message-1")
        first = make_input_event(**base, context={"project": "A"})
        second = make_input_event(**base, context={"project": "B"})
        self.assertEqual(first["event_id"], second["event_id"])

    def test_unknown_channel_is_rejected(self):
        with self.assertRaises(ValueError):
            make_input_event(channel_type="telepathy", body="O", source_ref="test:1")


if __name__ == "__main__":
    unittest.main()
