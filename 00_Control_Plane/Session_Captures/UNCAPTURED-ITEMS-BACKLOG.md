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
