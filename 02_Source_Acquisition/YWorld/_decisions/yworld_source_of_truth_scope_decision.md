# Y-WORLD Source of Truth Scope Decision

**Date:** 2026-07-04
**Gate:** YWORLD-SOURCE-OF-TRUTH-SCOPE-GATE (v2)
**Author:** Manus AI

## Table 9.2 — Source Role Decision Matrix

| Surface | Active Candidate | Backup Candidate | Sync/Mirror Candidate | Fragment Candidate | Canonical Candidate | Evidence Level | Decision |
| ------- | :--------------: | :--------------: | :-------------------: | :----------------: | :-----------------: | -------------- | -------- |
| **GITHUB-YWORLD** | YES | NO | YES | NO | YES | `GIT_METADATA_ONLY` | `REQUIRES_BOUNDED_COMPARISON` |
| **GDRIVE-OBS-003** | YES | NO | YES | NO | YES | `BOUNDED_CONTENT_SAMPLE` | `REQUIRES_BOUNDED_COMPARISON` |
| **ICLOUD-YWORLD** | NO | NO | NO | YES | NO | `MICRO_EXTRACTION_QUARANTINE` | `SMALL_FRAGMENT_COMPARISON_SOURCE` |
| **LOCAL-YWORLD** | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | `INSUFFICIENT` | `LOCAL_YWORLD_UNPROBED_SCOPE_UNCONFIRMED` |

## Table 9.3 — Pipeline Delegation Matrix

| Surface | Delegated Pipeline | Reason | Next Gate |
| ------- | ------------------ | ------ | --------- |
| **GITHUB-YWORLD** | GITHUB_PIPELINE | Private Git repo, metadata-only access confirmed. Workflow `compile-graph.yml` suggests auto-sync from local vault. | `YWORLD-BOUNDED-METADATA-COMPARISON-GATE` |
| **GDRIVE-OBS-003** | GDRIVE_PIPELINE | GDrive Obsidian vault, bounded sample confirmed high-value Y-WORLD content. Likely mirror of local/GitHub. | `YWORLD-BOUNDED-METADATA-COMPARISON-GATE` |
| **ICLOUD-YWORLD** | ICLOUD_PIPELINE | Closed micro-vault, 3 files quarantined for future comparison. No further extraction authorized. | `YWORLD-BOUNDED-METADATA-COMPARISON-GATE` (comparison source only) |
| **LOCAL-YWORLD** | LOCAL_PIPELINE | Unconfirmed. Likely the local Git clone being synced. Cannot probe without broad filesystem scan. | N/A — `LOCAL_YWORLD_UNPROBED_SCOPE_UNCONFIRMED` |

## Evidence Analysis

**GITHUB-YWORLD vs GDRIVE-OBS-003:** The GitHub API confirms 234 MD files across 21 top-level folders (last push: 2026-05-29). The GDrive vault shows 235 MD files across 18 folders with an identical folder structure. The 1-file discrepancy and the presence of a `compile-graph.yml` workflow strongly suggest that the local vault is the source, GitHub is the remote canonical backup, and GDrive is a live sync mirror. Neither can be definitively declared the canonical Source of Truth without a bounded file-tree comparison.

**ICLOUD-YWORLD:** Confirmed as a fragment/micro-source. The 3 retained files (`yos_memory_blueprint.md`, `Tool Intelligence Layer.md`, `ExcaliBrain Snapshot`) are high-value but represent a small subset of the full vault. This surface is closed and will serve only as a comparison reference.

**LOCAL-YWORLD:** No distinct local vault path was identified in the vault discovery registry. The local source is presumed to be the Git clone being synced, but it cannot be safely probed without broad filesystem scanning (which is forbidden by the MPM).

## Final Scope Decision

`YWORLD_SOURCE_OF_TRUTH_NOT_DECIDED_REQUIRES_BOUNDED_COMPARISON`
