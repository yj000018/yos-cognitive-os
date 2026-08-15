from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "02_Architecture" / "Universal_Input_Layer" / "schemas" / "universal_input_event.schema.json"


class UniversalInputSchemaTests(unittest.TestCase):
    def test_schema_declares_core_event_shape_and_channels(self):
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertEqual(
            set(schema["required"]),
            {"event_id", "received_at", "channel", "mode", "intent", "context", "object", "routing", "provenance"},
        )
        self.assertEqual(
            set(schema["properties"]["channel"]["properties"]["type"]["enum"]),
            {"text", "voice", "email", "share", "messaging", "browser", "api", "sensor"},
        )


if __name__ == "__main__":
    unittest.main()
