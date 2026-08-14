import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from canonical_objects import (
    CanonicalLineage,
    CanonicalObject,
    build_conversation_delta_object,
    build_preservation_event_object,
    content_sha256,
)
from preserve import Candidate, GitDocument, PreservationState, plan_preservation


class CanonicalObjectCoreTests(unittest.TestCase):
    def test_content_hash_is_deterministic_for_mapping_order(self):
        self.assertEqual(content_sha256({"b": 2, "a": 1}), content_sha256({"a": 1, "b": 2}))

    def test_content_hash_changes_when_semantic_content_changes(self):
        self.assertNotEqual(content_sha256({"a": 1}), content_sha256({"a": 2}))

    def test_to_dict_serializes_lineage_and_context_as_json_lists(self):
        obj = CanonicalObject(
            object_id="co:test:1",
            object_type="artifact.document",
            schema_version="1.0",
            created_at="2026-08-14T09:00:00+02:00",
            created_by="test-suite",
            provenance={"source": "unit-test"},
            lineage=CanonicalLineage(source_refs=("source:1",)),
            context_refs=("project:YOS",),
            payload={"title": "Example"},
            integrity={"content_sha256": content_sha256({"title": "Example"})},
            governance={"mutation_strategy": "VERSIONED"},
            record_state="active",
        )
        data = obj.to_dict()
        self.assertEqual(data["lineage"]["source_refs"], ["source:1"])
        self.assertEqual(data["context_refs"], ["project:YOS"])

    def test_invalid_record_state_is_rejected(self):
        with self.assertRaises(ValueError):
            CanonicalObject(
                "co:test:2",
                "artifact.document",
                "1.0",
                "2026-08-14T09:00:00+02:00",
                "test",
                {},
                CanonicalLineage(),
                (),
                {},
                {},
                {},
                "verified",
            )


class PreserveProjectionTests(unittest.TestCase):
    def test_delta_projection_has_stable_identity_hash_and_mutations(self):
        candidate = Candidate(
            "c1",
            "Durable delta",
            topic="YOS",
            marker="m2",
            proposed_path="delta.md",
            provenance="session:42",
        )
        tx = plan_preservation([candidate], {}, PreservationState(last_marker="m1"))
        obj1 = build_conversation_delta_object(
            transaction=tx,
            candidates=[candidate],
            created_by="chatgpt",
            source_refs=("session:42",),
        )
        obj2 = build_conversation_delta_object(
            transaction=tx,
            candidates=[candidate],
            created_by="chatgpt",
            source_refs=("session:42",),
        )
        self.assertEqual(obj1.object_id, obj2.object_id)
        self.assertEqual(obj1.object_type, "pack.conversation_delta")
        self.assertEqual(obj1.payload["transaction_id"], tx.transaction_id)
        self.assertEqual(obj1.payload["mutations"][0]["path"], "delta.md")
        self.assertEqual(obj1.lineage.source_refs, ("session:42",))
        self.assertEqual(len(obj1.integrity["content_sha256"]), 64)

    def test_no_delta_projection_is_valid_audit_object_without_mutations(self):
        tx = plan_preservation([], {}, PreservationState(last_marker="m1"))
        obj = build_conversation_delta_object(
            transaction=tx,
            candidates=[],
            created_by="chatgpt",
            source_refs=("session:42",),
        )
        self.assertEqual(obj.payload["candidate_count"], 0)
        self.assertEqual(obj.payload["mutations"], [])

    def test_supersession_is_preserved_in_lineage(self):
        candidate = Candidate(
            "c1",
            "Use B",
            topic="routing",
            target_path="routing.md",
            relation="superseding",
            supersedes="decision-A",
        )
        tx = plan_preservation(
            [candidate],
            {"routing.md": GitDocument("routing.md", "Use A")},
            PreservationState(),
        )
        obj = build_conversation_delta_object(
            transaction=tx,
            candidates=[candidate],
            created_by="chatgpt",
            source_refs=("session:42",),
        )
        self.assertIn("decision-A", obj.lineage.supersedes)

    def test_contradiction_preserves_git_target_in_lineage(self):
        candidate = Candidate(
            "c1",
            "Do not use A",
            topic="routing",
            target_path="routing.md",
            relation="contradiction",
        )
        tx = plan_preservation(
            [candidate],
            {"routing.md": GitDocument("routing.md", "Use A")},
            PreservationState(),
        )
        obj = build_conversation_delta_object(
            transaction=tx,
            candidates=[candidate],
            created_by="chatgpt",
            source_refs=("session:42",),
        )
        self.assertTrue(obj.payload["mutations"][0]["preserve_history"])
        self.assertIn("git:routing.md", obj.lineage.related_objects)

    def test_offline_event_never_implies_remote_verification(self):
        candidate = Candidate("c1", "Delta", topic="YOS", proposed_path="x.md")
        tx = plan_preservation([candidate], {}, PreservationState(), github_available=False)
        delta = build_conversation_delta_object(
            transaction=tx,
            candidates=[candidate],
            created_by="chatgpt",
            source_refs=("session:42",),
        )
        event = build_preservation_event_object(
            transaction=tx,
            conversation_delta=delta,
            created_by="chatgpt",
        )
        self.assertEqual(event.object_type, "event.preservation")
        self.assertEqual(event.payload["status"], "STAGED — NOT COMMITTED")
        self.assertNotIn("verified_remote_sha", event.payload)
        self.assertEqual(event.lineage.derived_from, (delta.object_id,))

    def test_verified_event_carries_supplied_remote_sha_only(self):
        candidate = Candidate("c1", "Delta", topic="YOS", proposed_path="x.md")
        tx = plan_preservation([candidate], {}, PreservationState())
        delta = build_conversation_delta_object(
            transaction=tx,
            candidates=[candidate],
            created_by="chatgpt",
            source_refs=("session:42",),
        )
        event = build_preservation_event_object(
            transaction=tx,
            conversation_delta=delta,
            created_by="chatgpt",
            verified_remote_sha="abc123",
        )
        self.assertEqual(event.payload["verified_remote_sha"], "abc123")
        self.assertEqual(event.payload["status"], "VERIFIED")


if __name__ == "__main__":
    unittest.main()
