import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from preserve import (  # noqa: E402
    Candidate,
    GitDocument,
    PreservationState,
    is_preserve_command,
    plan_preservation,
)


class PreserveTests(unittest.TestCase):
    def test_natural_language_aliases_are_global_triggers(self):
        for text in [
            "préserve",
            "Preserve",
            "save",
            "archive",
            "remember this",
            "capture le delta",
            "préserve seulement les décisions",
        ]:
            self.assertTrue(is_preserve_command(text), text)
        self.assertFalse(is_preserve_command("résume cette conversation"))

    def test_scenario_a_additive_delta_amends_existing_document(self):
        candidates = [Candidate("c1", "New CasaTAO principle", topic="CasaTAO", target_path="spatial-reality/10-ENVIRONMENTS/CASATAO.md")]
        truth = {"spatial-reality/10-ENVIRONMENTS/CASATAO.md": GitDocument("spatial-reality/10-ENVIRONMENTS/CASATAO.md", "Existing CasaTAO truth")}
        tx = plan_preservation(candidates, truth, PreservationState())
        self.assertEqual([m.path for m in tx.amend], ["spatial-reality/10-ENVIRONMENTS/CASATAO.md"])
        self.assertEqual(tx.create, [])
        self.assertEqual(tx.reconciliation["additive"], ["c1"])

    def test_scenario_b_repetition_produces_no_mutation(self):
        text = "CasaTAO is the Spatial Reality living laboratory"
        candidates = [Candidate("c1", text, topic="CasaTAO", target_path="spatial-reality/10-ENVIRONMENTS/CASATAO.md")]
        truth = {"spatial-reality/10-ENVIRONMENTS/CASATAO.md": GitDocument("spatial-reality/10-ENVIRONMENTS/CASATAO.md", text)}
        tx = plan_preservation(candidates, truth, PreservationState())
        self.assertEqual(tx.amend, [])
        self.assertEqual(tx.create, [])
        self.assertEqual(tx.reconciliation["duplicate"], ["c1"])

    def test_scenario_c_contradiction_preserves_lineage(self):
        candidates = [Candidate("c1", "Use design B", topic="routing", target_path="routing.md", relation="superseding", supersedes="decision-A")]
        truth = {"routing.md": GitDocument("routing.md", "Use design A")}
        tx = plan_preservation(candidates, truth, PreservationState())
        self.assertEqual(tx.reconciliation["superseding"], ["c1"])
        self.assertEqual(tx.amend[0].lineage_ref, "decision-A")
        self.assertTrue(tx.amend[0].preserve_history)

    def test_scenario_d_new_topic_creates_one_document(self):
        candidates = [Candidate("c1", "Standalone new architecture", topic="NewArch", proposed_path="02_Architecture/Memory/NEW-ARCH.md")]
        tx = plan_preservation(candidates, {}, PreservationState())
        self.assertEqual(tx.amend, [])
        self.assertEqual(len(tx.create), 1)
        self.assertEqual(tx.create[0].path, "02_Architecture/Memory/NEW-ARCH.md")

    def test_scenario_e_checkpoint_escalates_to_key_memory(self):
        candidates = [Candidate("c1", "Critical recoverable state", topic="YOS")]
        tx = plan_preservation(candidates, {}, PreservationState(), checkpoint=True)
        self.assertTrue(tx.escalate_key_memory)

    def test_scenario_f_github_unavailable_stages_offline_queue(self):
        candidates = [Candidate("c1", "Delta", topic="YOS", proposed_path="delta.md")]
        tx = plan_preservation(candidates, {}, PreservationState(), github_available=False)
        self.assertEqual(tx.status, "STAGED — NOT COMMITTED")
        self.assertIsNotNone(tx.offline_queue_package_id)
        self.assertFalse(tx.remote_verified)

    def test_boundary_makes_successive_preserves_differential(self):
        state = PreservationState(last_marker="m1", preserved_fingerprints=set())
        first = Candidate("c1", "First durable idea", marker="m2", topic="YOS", proposed_path="first.md")
        tx1 = plan_preservation([first], {}, state)
        self.assertEqual(len(tx1.create), 1)
        state2 = tx1.next_state(last_git_sha="abc123", transaction_id="tx-1")
        tx2 = plan_preservation([first], {}, state2)
        self.assertEqual(tx2.create, [])
        self.assertEqual(tx2.reconciliation["duplicate"], ["c1"])
        self.assertEqual(state2.last_marker, "m2")
        self.assertEqual(state2.last_git_sha, "abc123")


class PreserveStatePersistenceTests(unittest.TestCase):
    def test_state_roundtrip_persists_boundary_and_pending_queue(self):
        from preserve import load_state, save_state
        state = PreservationState(
            last_marker="m9",
            last_git_sha="sha9",
            last_transaction_id="tx9",
            preserved_fingerprints={"fp1"},
            pending_queue_ids={"GQ-1"},
        )
        with tempfile.TemporaryDirectory() as td:
            path = os.path.join(td, "preserve-state.json")
            save_state(path, state)
            loaded = load_state(path)
        self.assertEqual(loaded.last_marker, "m9")
        self.assertEqual(loaded.last_git_sha, "sha9")
        self.assertEqual(loaded.preserved_fingerprints, {"fp1"})
        self.assertEqual(loaded.pending_queue_ids, {"GQ-1"})

    def test_boundary_only_advances_after_verified_remote_persistence(self):
        candidate = Candidate("c1", "Durable", marker="m2", topic="YOS", proposed_path="x.md")
        tx = plan_preservation([candidate], {}, PreservationState(last_marker="m1"))
        with self.assertRaises(ValueError):
            tx.advance_state(PreservationState(last_marker="m1"), verified_sha=None)
        advanced = tx.advance_state(PreservationState(last_marker="m1"), verified_sha="abc")
        self.assertEqual(advanced.last_marker, "m2")
        self.assertEqual(advanced.last_git_sha, "abc")


class PreserveRoutingAndOfflineTests(unittest.TestCase):
    def test_routing_uses_codex_for_code_delta_and_manus_for_broad_git_mutation(self):
        from preserve import route_executor
        self.assertEqual(route_executor(code_change=True, broad_git_mutation=False), "Codex")
        self.assertEqual(route_executor(code_change=False, broad_git_mutation=True), "Manus")
        self.assertEqual(route_executor(code_change=False, broad_git_mutation=False), "ChatGPT")

    def test_offline_manifest_is_git_ready_and_keeps_target_and_mutations(self):
        from preserve import build_offline_queue_manifest
        candidate = Candidate("c1", "Delta", topic="YOS", proposed_path="x.md", provenance="session:42")
        tx = plan_preservation([candidate], {}, PreservationState(), github_available=False)
        manifest = build_offline_queue_manifest(tx, target_repository="yj000018/yos-cognitive-os")
        self.assertEqual(manifest["status"], "STAGED — NOT COMMITTED")
        self.assertEqual(manifest["target_repository"], "yj000018/yos-cognitive-os")
        self.assertEqual(manifest["queue_package_id"], tx.offline_queue_package_id)
        self.assertEqual(manifest["mutations"][0]["path"], "x.md")


if __name__ == "__main__":
    unittest.main()
