# SOURCE-OBJECT-REGISTRY

> Y-OS / KAP — Level L2: Source Objects
> A **Source Object** is an internal object inside a Source Instance.
> Examples: file, folder, commit, Notion page, database, block, Obsidian note, ChatGPT message, MPM, gate report, URL, app module.
> See `SOURCE-CHANNEL-REGISTRY.md` for L0 (channels).
> See `SOURCE-INSTANCE-REGISTRY.md` for L1 (instances).
> Source Fragments (L3) are created from Source Objects only after approved intake.
> Last Updated: 2026-07-03
> **Living document — populate during acquisition gates. Do not pre-populate with content.**

---

## Four-Level Taxonomy

```
L0 Source Channel     (SOURCE-CHANNEL-REGISTRY.md)
  └── L1 Source Instance  (SOURCE-INSTANCE-REGISTRY.md)
        └── L2 Source Object  (this file)
              └── L3 Source Fragment  (SOURCE-FRAGMENT-REGISTRY.md)
                    └── Claim → Thought Line → Decision Thread
```

---

## Object Type Vocabulary

| Object Type | Examples |
|---|---|
| `file` | .md, .py, .json, .ts, README |
| `folder` | Directory / vault folder |
| `commit` | Git commit with message + diff |
| `notion_page` | Notion page |
| `notion_database` | Notion database |
| `notion_block` | Notion block within a page |
| `obsidian_note` | Obsidian .md note |
| `obsidian_attachment` | Image, PDF, audio in vault |
| `chatgpt_message` | Single ChatGPT turn |
| `mpm` | Master Prompt Module document |
| `gate_report` | KAP gate report |
| `session_capture` | Session capture pack |
| `url` | External URL reference |
| `app_module` | Code module in a generated app |
| `other` | Unclassified object |

## Object Status Vocabulary

| Status | Meaning |
|---|---|
| `REGISTERED` | Object identified and registered — not yet extracted |
| `INTAKE_APPROVED` | Approved for fragment extraction |
| `FRAGMENT_EXTRACTED` | L3 fragment created from this object |
| `SKIPPED` | Intentionally excluded from extraction |
| `BLOCKED` | Cannot access object |
| `DEFERRED` | Out of scope for current phase |

---

## Pre-Registered Objects (Control Plane — ACQUIRED instances only)

> These objects are pre-registered because their parent instances are ACQUIRED and already in Git.
> All other objects will be registered during acquisition gates — not here.

### CH-001 / INST-GIT-001 — yos-cognitive-os

| obj_id | inst_id | Object Type | Name / Path | Status | Notes |
|---|---|---|---|---|---|
| OBJ-001 | INST-GIT-001 | `folder` | 00_Control_Plane/ | `REGISTERED` | Control plane root |
| OBJ-002 | INST-GIT-001 | `folder` | 02_Architecture/Synthesis/ | `REGISTERED` | Models + schemas |
| OBJ-003 | INST-GIT-001 | `folder` | 05_Registries/ | `REGISTERED` | All registries |
| OBJ-004 | INST-GIT-001 | `folder` | 06_Reports/Gates/ | `REGISTERED` | Gate reports |
| OBJ-005 | INST-GIT-001 | `folder` | 07_AI_Indexes/ | `REGISTERED` | AI indexes |
| OBJ-006 | INST-GIT-001 | `gate_report` | CLAIM-MODEL-GATE-REPORT.md | `REGISTERED` | Gate report |
| OBJ-007 | INST-GIT-001 | `gate_report` | SOURCE-FRAGMENT-MODEL-GATE-REPORT.md | `REGISTERED` | Gate report |
| OBJ-008 | INST-GIT-001 | `gate_report` | THOUGHT-LINE-MODEL-GATE-REPORT.md | `REGISTERED` | Gate report |
| OBJ-009 | INST-GIT-001 | `gate_report` | DECISION-THREAD-MODEL-GATE-REPORT.md | `REGISTERED` | Gate report |
| OBJ-010 | INST-GIT-001 | `gate_report` | CONTRADICTION-SUPERSESSION-POLICY-GATE-REPORT.md | `REGISTERED` | Gate report |

### CH-002 / INST-GPT-001 — ChatGPT Bootstrap Session Pack

| obj_id | inst_id | Object Type | Name / Path | Status | Notes |
|---|---|---|---|---|---|
| OBJ-011 | INST-GPT-001 | `session_capture` | YOS-KAP-SESSION-CAPTURE-PACK-Control-Plane-Bootstrap-2026-07-02.md | `REGISTERED` | Verbatim in Git |
| OBJ-012 | INST-GPT-001 | `mpm` | MPM-WP2-M2 through MPM-WP2-MANUS-FINAL (13 MPMs) | `REGISTERED` | Full bodies in Git |

### CH-002 / INST-GPT-002 — ChatGPT Current Session Pack

| obj_id | inst_id | Object Type | Name / Path | Status | Notes |
|---|---|---|---|---|---|
| OBJ-013 | INST-GPT-002 | `session_capture` | CURRENT-CHATGPT-YOS-KAP-SESSION-CAPTURE.md | `REGISTERED` | Verbatim in Git |
| OBJ-014 | INST-GPT-002 | `mpm` | MPM-EVOLUTIONARY-MERGE through MPM-SOURCE-FRAGMENT-MODEL (5 MPMs) | `REGISTERED` | Full bodies in Git |

### CH-003 / INST-MAN-001 — Manus Durable Gate Reports

| obj_id | inst_id | Object Type | Name / Path | Status | Notes |
|---|---|---|---|---|---|
| OBJ-015 | INST-MAN-001 | `gate_report` | EVOLUTIONARY-KNOWLEDGE-MERGE-ARCHITECTURE-GATE-REPORT.md | `REGISTERED` | In KAP repo |
| OBJ-016 | INST-MAN-001 | `gate_report` | YOS-CONTROL-PLANE-BOOTSTRAP-GATE-REPORT.md | `REGISTERED` | In yos-cognitive-os |
| OBJ-017 | INST-MAN-001 | `gate_report` | SOURCE-ACCESS-PIPELINE-READINESS-AUDIT-GATE-REPORT.md | `REGISTERED` | This session |

---

## Pending Population

> The following instances have objects that will be registered during their acquisition gates.
> Do NOT pre-populate — register only during controlled gate execution.

| Instance | Gate | Object Types Expected |
|---|---|---|
| INST-GIT-003→035 (39 repos) | GITHUB-SOURCE-ACQUISITION-GATE | file, folder, commit, README |
| INST-OBS-001/002 (Obsidian Git) | OBSIDIAN-MARKDOWN-METADATA-DRY-RUN-GATE | obsidian_note, folder, attachment |
| INST-OBS-003 (local vaults) | OBSIDIAN-VAULT-DISCOVERY-GATE → OBSIDIAN-MARKDOWN-METADATA-DRY-RUN-GATE | obsidian_note, folder |
| INST-NOT-001 (Notion Y-World) | NOTION-METADATA-INVENTORY-GATE | notion_page, notion_database, notion_block |
| INST-GPT-003/004 (pending sessions) | CAPTURE-PATCH-2 | session_capture, chatgpt_message |
| INST-MAN-002 (194 sessions) | MANUS-HISTORICAL-ACQUISITION-GATE | session_capture, gate_report |
