# Source Fragment Registry

> Y-OS / KAP Cognitive Architecture
> Gate: SOURCE-FRAGMENT-MODEL-GATE
> Status: SKELETON — seeded with known control-plane artifacts only
> Last updated: 2026-07-03

---

## Registry Table

| Fragment ID | Title | Source System | Source Type | Canonical Status | Review Status | Merge Status | Related Thought Lines | Path / URL | Notes |
|---|---|---|---|---|---|---|---|---|---|
| FRAG-20260703-CP01 | CURRENT-CHATGPT-YOS-KAP-SESSION-CAPTURE (2026-07-03) | ChatGPT | session_capture_pack | active_control_plane | metadata_reviewed | not_merged | TL-ARCHITECTURE-BEFORE-ABSORPTION, TL-GIT-AS-CANON | `00_Control_Plane/Session_Captures/CURRENT-CHATGPT-YOS-KAP-SESSION-CAPTURE.md` | Persisted verbatim. 10 doctrines, 8 decisions, 11 MPM stubs extracted. |
| FRAG-20260702-CP02 | YOS-KAP-SESSION-CAPTURE-PACK-Control-Plane-Bootstrap-2026-07-02 | ChatGPT | session_capture_pack | active_control_plane | metadata_reviewed | not_merged | TL-ARCHITECTURE-BEFORE-ABSORPTION, TL-GIT-AS-CANON | `00_Control_Plane/Session_Captures/YOS-KAP-SESSION-CAPTURE-PACK-Control-Plane-Bootstrap-2026-07-02.md` | Persisted verbatim. 10 doctrines, 12 decisions, 5 MPM stubs extracted. |
| FRAG-20260703-GR01 | YOS-CONTROL-PLANE-BOOTSTRAP-GATE-REPORT | Manus | gate_report | active_control_plane | metadata_reviewed | not_merged | TL-ARCHITECTURE-BEFORE-ABSORPTION | `06_Reports/Gates/YOS-CONTROL-PLANE-BOOTSTRAP-GATE-REPORT.md` | Gate PASS. 55 files bootstrapped. |
| FRAG-20260703-GR02 | EVOLUTIONARY-KNOWLEDGE-MERGE-ARCHITECTURE-GATE-REPORT | Manus | gate_report | active_control_plane | metadata_reviewed | not_merged | TL-ARCHITECTURE-BEFORE-ABSORPTION | `yj000018/KAP: 06_Reports/Gates/EVOLUTIONARY-KNOWLEDGE-MERGE-ARCHITECTURE-GATE-REPORT.md` | Gate PASS. 4 registries (28 TLs, 14 DTs, 12 impasses, 28 synthesis areas). |
| FRAG-20260703-AD01 | ARCHITECTURE-BEFORE-ABSORPTION | Manus | architecture_doc | active_control_plane | metadata_reviewed | not_merged | TL-ARCHITECTURE-BEFORE-ABSORPTION | `01_Strategy/ARCHITECTURE-BEFORE-ABSORPTION.md` | Core doctrine document. |
| FRAG-20260703-AD02 | YOS-STRATEGIC-DOCTRINE | Manus | architecture_doc | active_control_plane | metadata_reviewed | not_merged | TL-YOS-STRATEGY | `01_Strategy/YOS-STRATEGIC-DOCTRINE.md` | Strategic doctrine summary. |
| FRAG-20260703-AD03 | YOS-REPOSITORY-ARCHITECTURE-DECISION | Manus | architecture_doc | active_control_plane | metadata_reviewed | not_merged | TL-REPO-ARCHITECTURE | `02_Architecture/Decisions/YOS-REPOSITORY-ARCHITECTURE-DECISION.md` | Master repo + linked repos decision. |
| FRAG-20260703-AD04 | SOURCE-FRAGMENT-MODEL | Manus | architecture_doc | active_control_plane | content_reviewed | not_merged | TL-ARCHITECTURE-BEFORE-ABSORPTION | `02_Architecture/Synthesis/SOURCE-FRAGMENT-MODEL.md` | This gate output. |
| FRAG-20260703-AD05 | SOURCE-FRAGMENT-INTAKE-POLICY | Manus | architecture_doc | active_control_plane | content_reviewed | not_merged | TL-ARCHITECTURE-BEFORE-ABSORPTION | `02_Architecture/Synthesis/SOURCE-FRAGMENT-INTAKE-POLICY.md` | This gate output. |

---

## Registry Notes

- This registry is seeded with control-plane artifacts only (files confirmed to exist in Git as of commit `1e29c8c`).
- Illustrative examples from `SOURCE-FRAGMENT-EXAMPLES.md` are NOT included here.
- Real source fragments from Notion, Obsidian, ChatGPT export, and other sources will be added when their respective pipeline gates pass.
- Fragment IDs follow the pattern: `FRAG-YYYYMMDD-XXXX`

---

## Pending Registrations (known sources not yet extracted)

| Source | Gate Required | Status |
|---|---|---|
| Notion pages (1300+) | NOTION-PIPELINE-CONTROLLED-EXECUTION-GATE | PENDING |
| Obsidian notes (9 vaults, ~4400+) | OBSIDIAN-PIPELINE-PATCH-GATE | PENDING |
| ChatGPT full export | ChatGPT export gate (TBD) | PENDING |
| GitHub repos (36) | GITHUB-SOURCE-ACQUISITION-GATE | PENDING |
| Mem0 entries | Mem0 extraction gate (TBD) | PENDING |
| LLM Internal Memory | LLM-INTERNAL-MEMORY-EXTRACTION-GATE | DEFERRED |
