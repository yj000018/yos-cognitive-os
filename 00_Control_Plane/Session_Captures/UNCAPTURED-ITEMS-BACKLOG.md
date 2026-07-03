# Uncaptured Items Backlog

> Y-OS Control Plane — Items identified but not yet captured into Git
> Last updated: 2026-07-03

## Purpose

This backlog tracks all doctrine, MPMs, gate artifacts, and session outputs that have been identified but are not yet available for Git capture. Items here must not be considered lost — they must be recovered and captured in a future CAPTURE-PATCH gate.

---

## Backlog

| Item | Source | Why Not Captured | Required Action | Priority |
|---|---|---|---|---|
| CONNECTOR-DESIGN-GATE MPM | ChatGPT parallel KAP session | Session not exported | User to export ChatGPT session or provide capture pack | HIGH |
| AGENT-ROLE-GATE + MANUS-SESSION-GRAB-METADATA-CENSUS MPM | ChatGPT parallel KAP session | Session not exported | User to export ChatGPT session or provide capture pack | HIGH |
| CONNECTOR-IMPLEMENTATION-GATE MPM | ChatGPT parallel KAP session | Session not exported | User to export ChatGPT session or provide capture pack | HIGH |
| PIPELINE-FEASIBILITY-GATE MPM | ChatGPT parallel KAP session | Session not exported | User to export ChatGPT session or provide capture pack | HIGH |
| PIPELINE-FEASIBILITY executive matrix addendum | ChatGPT parallel KAP session | Session not exported | User to export ChatGPT session or provide capture pack | HIGH |
| OBSIDIAN-PIPELINE-VALIDATION-GATE doctrine | ChatGPT parallel KAP session | Session not exported | User to export ChatGPT session or provide capture pack | MEDIUM |
| OBSIDIAN-PIPELINE-PATCH-GATE MPM | ChatGPT parallel KAP session | Session not exported | User to export ChatGPT session or provide capture pack | MEDIUM |
| NOTION-PIPELINE-CONTROLLED-EXECUTION-GATE MPM | ChatGPT parallel KAP session | Session not exported | User to export ChatGPT session or provide capture pack | MEDIUM |
| Old KAP repo (yj000018/KAP legacy) | GitHub | Repo exists but legacy content not inventoried | Run GITHUB-SOURCE-ACQUISITION-GATE | LOW |
| Wild World repo | GitHub | Legacy repo, content unknown | Inventory and move to 99_Legacy/ | LOW |
| ChatGPT conversations.json export | ChatGPT | Not yet provided by user | User to export from ChatGPT settings | HIGH |
| Obsidian vault content (9 vaults) | Local filesystem | Vault scan not yet authorized | Run OBSIDIAN-MULTI-VAULT-GATE | MEDIUM |

---

## Recovery Protocol

When a user provides a capture pack or export:
1. Move item from this backlog to `PARALLEL-KAP-SESSIONS-CAPTURE-INDEX.md`.
2. Normalize content into appropriate Control Plane files.
3. Commit to Git.
4. Mark item as CAPTURED.

---

## Update 2026-07-03 — CAPTURE-PATCH from 2 ChatGPT session packs

Items newly identified from the two persisted capture packs:

| Item | Source | Why Not Captured | Required Action | Priority |
|---|---|---|---|---|
| WP1-R MPM full body | BOOTSTRAP-2026-07-02 pack | Full body not in capture pack | Recover from ChatGPT session | HIGH |
| KAP-WP1-R Addendum full body | BOOTSTRAP-2026-07-02 pack | Full body not in capture pack | Recover from ChatGPT session | HIGH |
| WP2-MANUS-FINAL MPM full body | BOOTSTRAP-2026-07-02 pack | Full body not in capture pack | Recover from ChatGPT session | MEDIUM |
| KAP-ARCH-1 MPM full body | BOOTSTRAP-2026-07-02 pack | Full body not in capture pack | Recover from ChatGPT session | MEDIUM |
| KAP-ARCH-1-PATCH MPM full body | BOOTSTRAP-2026-07-02 pack | Full body not in capture pack | Recover from ChatGPT session | MEDIUM |
| Architecture synthesis model stubs (8 files) | CURRENT-CHATGPT-2026-07-03 pack | Defined as future gates, not yet executed | Create skeletons with `TO_BE_DEFINED_BY_GATE` status | MEDIUM |
| ChatGPT full export / project conversation history | ChatGPT | Not yet provided by user | User to export from ChatGPT settings → future gate | HIGH |
| Uploaded KAP ZIP snapshot full contents | ZIP transport | ZIP is transport only | Verify what was in ZIP vs what is in Git | LOW |
| Existing repo inventory completeness (Wild World, old KAP) | GitHub | Partial — 36 repos catalogued | Verify Wild World and old KAP repos | MEDIUM |
| Actual Notion access/inventory state | Notion | Notion pipeline gate not yet executed | Run NOTION-PIPELINE-CONTROLLED-EXECUTION-GATE | MEDIUM |
| Actual Obsidian harness files and fake-vault test outputs | Local | Not yet executed | Run OBSIDIAN-PIPELINE-PATCH-GATE | MEDIUM |
| Git architecture mechanism decision (submodules vs linked repos) | OPEN-002 | Not yet decided | Architect decision needed | HIGH |
| Parallel ChatGPT KAP sessions (count unknown) | ChatGPT | Not yet identified/captured | User to identify all parallel sessions and generate capture packs | HIGH |

## Confirmed Captured (2026-07-03 CAPTURE-PATCH)

| Item | Status | Location |
|---|---|---|
| CURRENT-CHATGPT-YOS-KAP-SESSION-CAPTURE.md (verbatim) | ✅ PERSISTED | `00_Control_Plane/Session_Captures/` |
| YOS-KAP-SESSION-CAPTURE-PACK-Control-Plane-Bootstrap-2026-07-02.md (verbatim) | ✅ PERSISTED | `00_Control_Plane/Session_Captures/` |
| 20 doctrines extracted | ✅ REGISTERED | `00_Control_Plane/CANONICAL-DOCTRINE-REGISTRY.md` |
| 35+ decisions extracted | ✅ LOGGED | `00_Control_Plane/ACTIVE-DECISION-LOG.md` |
| 11 MPM stubs (CURRENT pack) | ✅ CREATED | `03_Modules/KAP/Gates/`, `02_Architecture/Synthesis/Gates/`, `00_Control_Plane/Gates/` |
| 5 MPM stubs (BOOTSTRAP pack) | ✅ CREATED | Various paths |
| DOCTRINE-REGISTRY.md | ✅ CREATED | `05_Registries/` |
| DECISION-THREAD-REGISTRY.md | ✅ CREATED | `05_Registries/` |
| CHATGPT-Guardian-Architect.md | ✅ CREATED | `00_Infrastructure/Team_OS/Agents/` |
| TOOLS-REGISTRY-TEMP-ConvoFlow.md | ✅ CREATED | `00_Infrastructure/Bootstrap_Temporary_Registries/` |
