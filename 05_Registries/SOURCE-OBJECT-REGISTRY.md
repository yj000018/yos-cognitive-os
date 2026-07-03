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

---

## OBSIDIAN-MARKDOWN-METADATA-DRY-RUN-GATE — Registered Objects

> Added: 2026-07-03 — Y-WORLD vault (Git-backed, Case C)
> 235 Markdown notes scanned via GitHub API — metadata only, no body content

### CH-004 / INST-OBS-002 — Y-WORLD Obsidian Vault (Git-backed)

> Full inventory in: `03_Modules/KAP/Pipelines/Obsidian/Indexes/markdown_file_inventory.json`
> IDs: SO-OBS-YWLD-0001 → SO-OBS-YWLD-0235

| Source Object ID | Instance ID | Channel | Object Type | Folder | Status | Content Ingested | Notes |
|---|---|---|---|---|---|---|---|
| SO-OBS-YWLD-0001→0235 | INST-OBS-002 | CH-004 | `obsidian_note` | 21 folders | `METADATA_REGISTERED` | false | 235 notes — full index in markdown_file_inventory.json |
| SO-OBS-YWLD-FOLDER-001 | INST-OBS-002 | CH-004 | `folder` | / (root) | `REGISTERED` | false | Root vault |
| SO-OBS-YWLD-FOLDER-002 | INST-OBS-002 | CH-004 | `folder` | 00_System | `REGISTERED` | false | System rules |
| SO-OBS-YWLD-FOLDER-003 | INST-OBS-002 | CH-004 | `folder` | 01_Cockpit | `REGISTERED` | false | Dashboard |
| SO-OBS-YWLD-FOLDER-004 | INST-OBS-002 | CH-004 | `folder` | 02_Maps | `REGISTERED` | false | Maps |
| SO-OBS-YWLD-FOLDER-005 | INST-OBS-002 | CH-004 | `folder` | 03_Dashboards | `REGISTERED` | false | Dashboards |
| SO-OBS-YWLD-FOLDER-006 | INST-OBS-002 | CH-004 | `folder` | 04_Templates | `REGISTERED` | false | Templates |
| SO-OBS-YWLD-FOLDER-007 | INST-OBS-002 | CH-004 | `folder` | 05_Registries | `REGISTERED` | false | Registries |
| SO-OBS-YWLD-FOLDER-008 | INST-OBS-002 | CH-004 | `folder` | 06_Workflows | `REGISTERED` | false | Workflows |
| SO-OBS-YWLD-FOLDER-009 | INST-OBS-002 | CH-004 | `folder` | 07_Agent_Operations | `REGISTERED` | false | Agent ops |
| SO-OBS-YWLD-FOLDER-010 | INST-OBS-002 | CH-004 | `folder` | 10_Inbox | `REGISTERED` | false | Inbox |
| SO-OBS-YWLD-FOLDER-011 | INST-OBS-002 | CH-004 | `folder` | 20_Life | `REGISTERED` | false | Life |
| SO-OBS-YWLD-FOLDER-012 | INST-OBS-002 | CH-004 | `folder` | 30_Knowledge | `REGISTERED` | false | Knowledge |
| SO-OBS-YWLD-FOLDER-013 | INST-OBS-002 | CH-004 | `folder` | 40_K-Cards | `REGISTERED` | false | K-Cards |
| SO-OBS-YWLD-FOLDER-014 | INST-OBS-002 | CH-004 | `folder` | 50_Projects | `REGISTERED` | false | Projects |
| SO-OBS-YWLD-FOLDER-015 | INST-OBS-002 | CH-004 | `folder` | 60_Y-OS | `REGISTERED` | false | Y-OS |
| SO-OBS-YWLD-FOLDER-016 | INST-OBS-002 | CH-004 | `folder` | 70_CasaTAO | `REGISTERED` | false | CasaTAO |
| SO-OBS-YWLD-FOLDER-017 | INST-OBS-002 | CH-004 | `folder` | 71_ARC_Anandaz | `REGISTERED` | false | Anandaz |
| SO-OBS-YWLD-FOLDER-018 | INST-OBS-002 | CH-004 | `folder` | 80_Archetypes | `REGISTERED` | false | Archetypes |
| SO-OBS-YWLD-FOLDER-019 | INST-OBS-002 | CH-004 | `folder` | 81_Y-Publishing | `REGISTERED` | false | Publishing |
| SO-OBS-YWLD-FOLDER-020 | INST-OBS-002 | CH-004 | `folder` | 90_Reality_Interfaces | `REGISTERED` | false | Reality interfaces |

### CH-004 / INST-OBS-LOCAL — Local Mac Vaults (BLOCKED)

| Source Object ID | Instance ID | Channel | Status | Blocker | Next Gate |
|---|---|---|---|---|---|
| SO-OBS-LOCAL-PENDING | INST-OBS-LOCAL | CH-004 | `BLOCKED_PENDING_MAC_UNLOCK` | Mac screen locked — FUSE not mounted | OBSIDIAN-LOCAL-VAULT-DISCOVERY-GATE (after Mac unlock) |

