# UNCAPTURED-ITEMS-BACKLOG

> Y-OS Control Plane — Items identified but not yet captured into Git
> Last updated: 2026-07-03 — FULL-BODY-CAPTURE-PATCH

## Purpose

This backlog tracks all doctrine, MPMs, gate artifacts, and session outputs that have been identified but are not yet available for Git capture. Items here must not be considered lost — they must be recovered and captured in a future CAPTURE-PATCH gate.

---

## Active Backlog — Still Uncaptured

| Item | Source | Why Not Captured | Required Action | Priority |
|---|---|---|---|---|
| AGENT-ROLE-GATE + MANUS-SESSION-GRAB-METADATA-CENSUS MPM full body | ChatGPT parallel KAP session | Full body not in either capture pack | Recover from ChatGPT session or provide capture pack | HIGH |
| CONNECTOR-IMPLEMENTATION-GATE MPM full body | ChatGPT parallel KAP session | Full body not in either capture pack | Recover from ChatGPT session or provide capture pack | HIGH |
| PIPELINE-FEASIBILITY-GATE MPM full body | ChatGPT parallel KAP session | Full body not in either capture pack | Recover from ChatGPT session or provide capture pack | HIGH |
| PIPELINE-FEASIBILITY executive matrix addendum full body | ChatGPT parallel KAP session | Full body not in either capture pack | Recover from ChatGPT session or provide capture pack | HIGH |
| OBSIDIAN-PIPELINE-VALIDATION-GATE MPM full body | ChatGPT parallel KAP session | Full body not in either capture pack | Recover from ChatGPT session or provide capture pack | MEDIUM |
| OBSIDIAN-PIPELINE-PATCH-GATE MPM full body | ChatGPT parallel KAP session | Full body not in either capture pack | Recover from ChatGPT session or provide capture pack | MEDIUM |
| NOTION-PIPELINE-CONTROLLED-EXECUTION-GATE MPM full body | ChatGPT parallel KAP session | Full body not in either capture pack | Recover from ChatGPT session or provide capture pack | MEDIUM |
| ChatGPT full conversations.json export | ChatGPT | Not yet provided by user | User to export from ChatGPT settings | HIGH |
| Obsidian vault content (9 vaults) | Local filesystem | Vault scan not yet authorized | Run OBSIDIAN-MULTI-VAULT-GATE | MEDIUM |
| Architecture synthesis model stubs (8 files) | Future gates | Defined as future gates, not yet executed | Create skeletons with TO_BE_DEFINED_BY_GATE status | MEDIUM |
| Git architecture mechanism decision (submodules vs linked repos) | OPEN-002 | Not yet decided | Architect decision needed | HIGH |
| Parallel ChatGPT KAP sessions (count unknown) | ChatGPT | Not yet identified/captured | User to identify all parallel sessions and generate capture packs | HIGH |
| Actual Notion access/inventory state | Notion | Notion pipeline gate not yet executed | Run NOTION-PIPELINE-CONTROLLED-EXECUTION-GATE | MEDIUM |
| Actual Obsidian harness files and fake-vault test outputs | Local | Not yet executed | Run OBSIDIAN-PIPELINE-PATCH-GATE | MEDIUM |

---

## Recovery Protocol

When a user provides a capture pack or export:
1. Move item from this backlog to `PARALLEL-KAP-SESSIONS-CAPTURE-INDEX.md`.
2. Normalize content into appropriate Control Plane files.
3. Commit to Git.
4. Mark item as CAPTURED.

---

## Confirmed Captured — FULL-BODY-CAPTURE-PATCH (2026-07-03)

### Bootstrap Session Pack (MPM-Full-Body-Capture-Pack-Bootstrap-Session.md)

| Item | Status | Location |
|---|---|---|
| MPM-WP2-M2 — Remaining Manus Surface Map | ✅ FULL BODY PERSISTED | `03_Modules/KAP/Gates/WP2-M2-REMAINING-MANUS-SURFACE-MAP/` |
| MPM-WP2-M3 — Full Manus Knowledge Capture | ✅ FULL BODY PERSISTED | `03_Modules/KAP/Gates/WP2-M3-FULL-MANUS-KNOWLEDGE-CAPTURE/` |
| MPM-WP2-M4 — Full Manus Tasks and Outputs Capture | ✅ FULL BODY PERSISTED | `03_Modules/KAP/Gates/WP2-M4-FULL-MANUS-TASKS-OUTPUTS-CAPTURE/` |
| MPM-WP2-M5 — Manus Website URL Recovery | ✅ FULL BODY PERSISTED | `03_Modules/KAP/Gates/WP2-M5-MANUS-WEBSITE-URL-RECOVERY/` |
| MPM-WP2-M6 — Manus Memory Hub / Notion Bridge | ✅ FULL BODY PERSISTED | `03_Modules/KAP/Gates/WP2-M6-MANUS-MEMORY-HUB-NOTION-BRIDGE/` |
| MPM-WP2-M7 — Manus Completion Gate | ✅ FULL BODY PERSISTED | `03_Modules/KAP/Gates/WP2-M7-MANUS-COMPLETION-GATE/` |
| MPM-WP2-MANUS-FINAL — Branch Closure Gate | ✅ FULL BODY PERSISTED | `03_Modules/KAP/Gates/WP2-MANUS-FINAL-BRANCH-CLOSURE/` |
| MPM-KAP-ARCH-1 — Workflow Pipeline Protocol Consolidation | ✅ FULL BODY PERSISTED | `03_Modules/KAP/Gates/KAP-ARCH-1-WORKFLOW-PIPELINE-PROTOCOL/` |
| MPM-KAP-ARCH-1-PATCH — Architecture Before Extraction | ✅ FULL BODY PERSISTED | `03_Modules/KAP/Gates/KAP-ARCH-1-PATCH-ARCHITECTURE-BEFORE-EXTRACTION/` |
| MPM-STRUCTURE-GATE — KAP Machine Structure Validation | ✅ FULL BODY PERSISTED | `03_Modules/KAP/Gates/STRUCTURE-GATE-MACHINE-STRUCTURE-VALIDATION/` |
| MPM-CONNECTOR-DESIGN-GATE (stub → full body) | ✅ FULL BODY PERSISTED | `03_Modules/KAP/Gates/CONNECTOR-DESIGN-GATE/` |
| ADDENDUM-WP1-R — Source Lifecycle & Project Knowledge Phase Correction | ✅ FULL BODY PERSISTED | `03_Modules/KAP/Gates/WP2-M2-REMAINING-MANUS-SURFACE-MAP/` |
| Manus Handoff — YOS/KAP Session Capture Persistence | ✅ FULL BODY PERSISTED | `00_Control_Plane/` |

### Current ChatGPT Session Pack (MPM-FULL-BODY-CAPTURE-PACK-CURRENT-CHATGPT-YOS-KAP.md)

| Item | Status | Location |
|---|---|---|
| MPM-EVOLUTIONARY-KNOWLEDGE-MERGE-ARCHITECTURE-GATE | ✅ FULL BODY PERSISTED | `03_Modules/KAP/Gates/EVOLUTIONARY-KNOWLEDGE-MERGE-ARCHITECTURE/` |
| MPM-YOS-CONTROL-PLANE-BOOTSTRAP + SESSION-DOCTRINE-CAPTURE-GATE | ✅ FULL BODY PERSISTED | `03_Modules/KAP/Gates/YOS-CONTROL-PLANE-BOOTSTRAP/` |
| ADDENDUM — Mandatory Session Doctrine Capture and Git Persistence | ✅ FULL BODY PERSISTED | `03_Modules/KAP/Gates/YOS-CONTROL-PLANE-BOOTSTRAP/` |
| Manus Handoff — YOS/KAP Session Capture Persistence v2 | ✅ FULL BODY PERSISTED | `00_Control_Plane/` |
| MPM-SOURCE-FRAGMENT-MODEL-GATE | ✅ FULL BODY PERSISTED | `03_Modules/KAP/Gates/SOURCE-FRAGMENT-MODEL/` |

### Previous CAPTURE-PATCH (2026-07-03)

| Item | Status | Location |
|---|---|---|
| CURRENT-CHATGPT-YOS-KAP-SESSION-CAPTURE.md (verbatim) | ✅ PERSISTED | `00_Control_Plane/Session_Captures/` |
| YOS-KAP-SESSION-CAPTURE-PACK-Control-Plane-Bootstrap-2026-07-02.md (verbatim) | ✅ PERSISTED | `00_Control_Plane/Session_Captures/` |
| MPM-Full-Body-Capture-Pack-Bootstrap-Session.md (verbatim) | ✅ PERSISTED | `00_Control_Plane/Session_Captures/` |
| MPM-FULL-BODY-CAPTURE-PACK-CURRENT-CHATGPT-YOS-KAP.md (verbatim) | ✅ PERSISTED | `00_Control_Plane/Session_Captures/` |
| 20 doctrines extracted | ✅ REGISTERED | `00_Control_Plane/CANONICAL-DOCTRINE-REGISTRY.md` |
| 35+ decisions extracted | ✅ LOGGED | `00_Control_Plane/ACTIVE-DECISION-LOG.md` |
| DOCTRINE-REGISTRY.md | ✅ CREATED | `05_Registries/` |
| DECISION-THREAD-REGISTRY.md | ✅ CREATED | `05_Registries/` |
| CHATGPT-Guardian-Architect.md | ✅ CREATED | `00_Infrastructure/Team_OS/Agents/` |

---

## MPM Capture Summary

| MPM | Title | Status |
|---|---|---|
| MPM-WP2-M2 | Remaining Manus Surface Map | ✅ FULL BODY |
| MPM-WP2-M3 | Full Manus Knowledge Capture | ✅ FULL BODY |
| MPM-WP2-M4 | Full Manus Tasks and Outputs Capture | ✅ FULL BODY |
| MPM-WP2-M5 | Manus Website URL Recovery | ✅ FULL BODY |
| MPM-WP2-M6 | Manus Memory Hub / Notion Bridge | ✅ FULL BODY |
| MPM-WP2-M7 | Manus Completion Gate | ✅ FULL BODY |
| MPM-WP2-MANUS-FINAL | Branch Closure Gate | ✅ FULL BODY |
| MPM-KAP-ARCH-1 | Workflow Pipeline Protocol Consolidation | ✅ FULL BODY |
| MPM-KAP-ARCH-1-PATCH | Architecture Before Extraction | ✅ FULL BODY |
| MPM-STRUCTURE-GATE | KAP Machine Structure Validation | ✅ FULL BODY |
| MPM-CONNECTOR-DESIGN-GATE | Connector & Pipeline Design Validation | ✅ FULL BODY |
| MPM-EVOLUTIONARY-KNOWLEDGE-MERGE | Evolutionary Knowledge Merge Architecture Gate | ✅ FULL BODY |
| MPM-YOS-CONTROL-PLANE-BOOTSTRAP | YOS Control Plane Bootstrap + Session Doctrine Capture Gate | ✅ FULL BODY |
| MPM-SOURCE-FRAGMENT-MODEL | Source Fragment Model Gate | ✅ FULL BODY |
| MPM-AGENT-ROLE-GATE | Agent Role Gate + Manus Census | ⏳ STUB ONLY |
| MPM-CONNECTOR-IMPLEMENTATION-GATE | Connector Implementation Gate | ⏳ STUB ONLY |
| MPM-PIPELINE-FEASIBILITY-GATE | Pipeline Feasibility Gate | ⏳ STUB ONLY |
| MPM-OBSIDIAN-PIPELINE-VALIDATION | Obsidian Pipeline Validation Gate | ⏳ STUB ONLY |
| MPM-OBSIDIAN-PIPELINE-PATCH | Obsidian Pipeline Patch Gate | ⏳ STUB ONLY |
| MPM-NOTION-PIPELINE-CONTROLLED-EXECUTION | Notion Pipeline Controlled Execution Gate | ⏳ STUB ONLY |
