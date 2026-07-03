# SOURCE-OBJECT-REGISTRY

> Y-OS / KAP — Level L2: Source Objects
> **PATCHED:** SOURCE-FRAGMENT-ID-NORMALIZATION-PATCH 2026-07-03
> A **Source Object** is an internal object inside a Source Instance.
> See `SOURCE-CHANNEL-REGISTRY.md` for L0 · `SOURCE-INSTANCE-REGISTRY.md` for L1 · `SOURCE-FRAGMENT-REGISTRY.md` for L3
> **ID Format:** `SO-<CHANNELCODE>-<INSTANCESEQ>-<OBJECTSEQ>`
> Last Updated: 2026-07-03

---

## Four-Level Taxonomy

```
L0 Source Channel     (SOURCE-CHANNEL-REGISTRY.md)
  └── L1 Source Instance  (SOURCE-INSTANCE-REGISTRY.md)
        └── L2 Source Object  (this file)
              └── L3 Source Fragment  (SOURCE-FRAGMENT-REGISTRY.md)
```

---

## Pre-Registered Objects (ACQUIRED instances only)

### CH-001 / GIT-001 — yos-cognitive-os

| Source Object ID | Instance ID | Channel | Object Type | Title / Path | Status | Fragment Status | Notes |
|---|---|---|---|---|---|---|---|
| SO-GIT-001-0001 | GIT-001 | CH-001 | `folder` | 00_Control_Plane/ | `REGISTERED` | not-started | Control plane root |
| SO-GIT-001-0002 | GIT-001 | CH-001 | `folder` | 02_Architecture/Synthesis/ | `REGISTERED` | not-started | Models + schemas |
| SO-GIT-001-0003 | GIT-001 | CH-001 | `folder` | 05_Registries/ | `REGISTERED` | not-started | All registries |
| SO-GIT-001-0004 | GIT-001 | CH-001 | `folder` | 06_Reports/Gates/ | `REGISTERED` | not-started | Gate reports |
| SO-GIT-001-0005 | GIT-001 | CH-001 | `folder` | 07_AI_Indexes/ | `REGISTERED` | not-started | AI indexes |
| SO-GIT-001-0006 | GIT-001 | CH-001 | `gate_report` | CLAIM-MODEL-GATE-REPORT.md | `REGISTERED` | not-started | Gate report |
| SO-GIT-001-0007 | GIT-001 | CH-001 | `gate_report` | SOURCE-FRAGMENT-MODEL-GATE-REPORT.md | `REGISTERED` | not-started | Gate report |
| SO-GIT-001-0008 | GIT-001 | CH-001 | `gate_report` | THOUGHT-LINE-MODEL-GATE-REPORT.md | `REGISTERED` | not-started | Gate report |
| SO-GIT-001-0009 | GIT-001 | CH-001 | `gate_report` | DECISION-THREAD-MODEL-GATE-REPORT.md | `REGISTERED` | not-started | Gate report |
| SO-GIT-001-0010 | GIT-001 | CH-001 | `gate_report` | CONTRADICTION-SUPERSESSION-POLICY-GATE-REPORT.md | `REGISTERED` | not-started | Gate report |
| SO-GIT-001-0011 | GIT-001 | CH-001 | `gate_report` | SOURCE-ACCESS-PIPELINE-READINESS-AUDIT-GATE-REPORT.md | `REGISTERED` | not-started | Gate report |
| SO-GIT-001-0012 | GIT-001 | CH-001 | `gate_report` | SOURCE-TAXONOMY-ALIGNMENT-PATCH-REPORT.md | `REGISTERED` | not-started | Patch report |
| SO-GIT-001-0013 | GIT-001 | CH-001 | `gate_report` | YOS-CONTROL-PLANE-BOOTSTRAP-GATE-REPORT.md | `REGISTERED` | not-started | Gate report |
| SO-GIT-001-0014 | GIT-001 | CH-001 | `file` | README.md | `REGISTERED` | not-started | Repo README |
| SO-GIT-001-0015 | GIT-001 | CH-001 | `file` | 04_Roadmap/YOS-KAP-COGNITIVE-ARCHITECTURE-ROADMAP.md | `REGISTERED` | not-started | Roadmap |
| SO-GIT-001-0016 | GIT-001 | CH-001 | `file` | 00_Control_Plane/CANONICAL-DOCTRINE-REGISTRY.md | `REGISTERED` | not-started | 20 doctrines |
| SO-GIT-001-0017 | GIT-001 | CH-001 | `file` | 00_Control_Plane/ACTIVE-DECISION-LOG.md | `REGISTERED` | not-started | Decision log |
| SO-GIT-001-0018 | GIT-001 | CH-001 | `file` | 01_Strategy/ARCHITECTURE-BEFORE-ABSORPTION.md | `REGISTERED` | legacy_mapped | Legacy: FRAG-20260703-AD01 |
| SO-GIT-001-0019 | GIT-001 | CH-001 | `file` | 01_Strategy/YOS-STRATEGIC-DOCTRINE.md | `REGISTERED` | legacy_mapped | Legacy: FRAG-20260703-AD02 |
| SO-GIT-001-0020 | GIT-001 | CH-001 | `file` | 02_Architecture/Decisions/YOS-REPOSITORY-ARCHITECTURE-DECISION.md | `REGISTERED` | legacy_mapped | Legacy: FRAG-20260703-AD03 |
| SO-GIT-001-0021 | GIT-001 | CH-001 | `file` | 02_Architecture/Synthesis/SOURCE-FRAGMENT-MODEL.md | `REGISTERED` | legacy_mapped | Legacy: FRAG-20260703-AD04 |
| SO-GIT-001-0022 | GIT-001 | CH-001 | `file` | 02_Architecture/Synthesis/SOURCE-FRAGMENT-INTAKE-POLICY.md | `REGISTERED` | legacy_mapped | Legacy: FRAG-20260703-AD05 |

### CH-002 / GPT-001 — ChatGPT Bootstrap Session Pack

| Source Object ID | Instance ID | Channel | Object Type | Title / Path | Status | Fragment Status | Notes |
|---|---|---|---|---|---|---|---|
| SO-GPT-001-0011 | GPT-001 | CH-002 | `session_capture` | YOS-KAP-SESSION-CAPTURE-PACK-Control-Plane-Bootstrap-2026-07-02.md | `REGISTERED` | legacy_mapped | Legacy: FRAG-20260702-CP02 |
| SO-GPT-001-0012 | GPT-001 | CH-002 | `mpm` | MPM-WP2-M2 through MPM-WP2-MANUS-FINAL (13 MPMs) | `REGISTERED` | not-started | Full bodies in Git |

### CH-002 / GPT-002 — ChatGPT Current Session Pack

| Source Object ID | Instance ID | Channel | Object Type | Title / Path | Status | Fragment Status | Notes |
|---|---|---|---|---|---|---|---|
| SO-GPT-002-0013 | GPT-002 | CH-002 | `session_capture` | CURRENT-CHATGPT-YOS-KAP-SESSION-CAPTURE.md | `REGISTERED` | legacy_mapped | Legacy: FRAG-20260703-CP01 |
| SO-GPT-002-0014 | GPT-002 | CH-002 | `mpm` | MPM-EVOLUTIONARY-MERGE through MPM-SOURCE-FRAGMENT-MODEL (5 MPMs) | `REGISTERED` | not-started | Full bodies in Git |

### CH-003 / MAN-001 — Manus Durable Gate Reports

| Source Object ID | Instance ID | Channel | Object Type | Title / Path | Status | Fragment Status | Notes |
|---|---|---|---|---|---|---|---|
| SO-MAN-001-0015 | MAN-001 | CH-003 | `gate_report` | EVOLUTIONARY-KNOWLEDGE-MERGE-ARCHITECTURE-GATE-REPORT.md (KAP repo) | `REGISTERED` | legacy_mapped | Legacy: FRAG-20260703-GR02 |
| SO-MAN-001-0016 | MAN-001 | CH-003 | `gate_report` | YOS-CONTROL-PLANE-BOOTSTRAP-GATE-REPORT.md | `REGISTERED` | legacy_mapped | Legacy: FRAG-20260703-GR01 |
| SO-MAN-001-0017 | MAN-001 | CH-003 | `gate_report` | SOURCE-ACCESS-PIPELINE-READINESS-AUDIT-GATE-REPORT.md | `REGISTERED` | not-started | This session |

---

## Next Available Sequence Numbers

| Instance | Next SO Seq |
|---|---|
| GIT-001 | 0023 |
| GPT-001 | 0013 |
| GPT-002 | 0015 |
| MAN-001 | 0018 |
| All others | 0001 |

---

## Pending Population

> Objects for the following instances will be registered during their acquisition gates only.

| Instance | Gate | Object Types Expected |
|---|---|---|
| GIT-002 KAP repo | GITHUB-SOURCE-ACQUISITION-GATE | file, folder |
| GIT-003→035 (39 repos) | GITHUB-SOURCE-ACQUISITION-GATE | file, folder, commit, README |
| OBS-001/002 (Obsidian Git) | OBSIDIAN-MARKDOWN-METADATA-DRY-RUN-GATE | obsidian_note, folder |
| OBS-003 (local vaults) | OBSIDIAN-VAULT-DISCOVERY-GATE → DRY-RUN | obsidian_note, folder |
| NOT-001 (Notion Y-World) | NOTION-METADATA-INVENTORY-GATE | notion_page, notion_database |
| GPT-003/004 (pending sessions) | CAPTURE-PATCH-2 | session_capture, chatgpt_message |
| MAN-002 (194 sessions) | MANUS-HISTORICAL-ACQUISITION-GATE | session_capture, gate_report |
