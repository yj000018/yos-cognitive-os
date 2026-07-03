# KAP-SOURCE-MATRIX

> Y-OS / KAP — Source Status Matrix
> **PATCHED:** SOURCE-TAXONOMY-ALIGNMENT-PATCH 2026-07-03
> Tracks readiness of every channel and source instance across the full KAP pipeline.
> **Four-Level Model:** L0 Channel → L1 Instance → L2 Object → L3 Fragment
> See: `SOURCE-CHANNEL-REGISTRY.md` (L0) · `SOURCE-INSTANCE-REGISTRY.md` (L1) · `SOURCE-OBJECT-REGISTRY.md` (L2) · `SOURCE-FRAGMENT-REGISTRY.md` (L3)
> Last Updated: 2026-07-03
> **Living document — update after every gate execution.**

---

## Special Role Flags

| Flag | Channels | Constraint |
|---|---|---|
| `SIGNAL_ONLY` | CH-006 Mem0 | Not a corpus. No claim extraction without durable source artifact. |
| `HEURISTIC_CONTEXT_ONLY` | CH-007 LLM Internal | Not canonical evidence. Never used for claims without source-linked artifacts. |
| `PROVENANCE_CENSUS_ONLY` | CH-009, CH-010 | Provenance/URL/code census only. No content acquisition. No claims. |
| `DEFERRED_FOR_LATER_KAP_YOUNIVERSE_EXTENSION` | CH-011, CH-012, CH-013, CH-014 | Out of scope Phase 1. |

---

## KAP Source Matrix

| Channel | Source Instance | In Scope | Role | Access | Pipeline | L2 Objects | L3 Fragments | Claims | Thought Lines | Decision Threads | Current Best | Next Safe Gate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CH-001 Git | INST-GIT-001 yos-cognitive-os | phase-1 | — | accessible | ready | registered | not-started | not-started | not-started | not-started | `ACQUIRED` | GITHUB-SOURCE-ACQUISITION-GATE |
| CH-001 Git | INST-GIT-002 KAP | phase-1 | — | accessible | ready | registered | not-started | not-started | not-started | not-started | `ACQUIRED` | GITHUB-SOURCE-ACQUISITION-GATE |
| CH-001 Git | INST-GIT-003→006 YOS branches | phase-1 | — | accessible | pending-gate | not-registered | not-started | not-started | not-started | not-started | `CATALOGUED` | GITHUB-SOURCE-ACQUISITION-GATE |
| CH-001 Git | INST-GIT-007→009 ELYSIUM repos | phase-1 | — | accessible | pending-gate | not-registered | not-started | not-started | not-started | not-started | `CATALOGUED` | GITHUB-SOURCE-ACQUISITION-GATE |
| CH-001 Git | INST-GIT-010→015 yos-* core | phase-1 | — | accessible | pending-gate | not-registered | not-started | not-started | not-started | not-started | `CATALOGUED` | GITHUB-SOURCE-ACQUISITION-GATE |
| CH-001 Git | INST-GIT-016→035 yos-* peripheral | phase-1 | — | accessible | pending-gate | not-registered | not-started | not-started | not-started | not-started | `CATALOGUED` | GITHUB-SOURCE-ACQUISITION-GATE |
| CH-001 Git | INST-GIT-036→041 youniverse/legacy | deferred | — | accessible | not-started | n/a | n/a | n/a | n/a | n/a | `DEFERRED` | — |
| CH-002 ChatGPT | INST-GPT-001 Bootstrap Pack | phase-1 | — | accessible | ready | registered | not-started | not-started | not-started | not-started | `ACQUIRED` | PROCESS-DOCS-RUNBOOK-GATE |
| CH-002 ChatGPT | INST-GPT-002 Current Pack | phase-1 | — | accessible | ready | registered | not-started | not-started | not-started | not-started | `ACQUIRED` | PROCESS-DOCS-RUNBOOK-GATE |
| CH-002 ChatGPT | INST-GPT-003 Parallel Sessions (6+) | phase-1 | — | partial | blocked | not-registered | not-started | not-started | not-started | not-started | `PENDING` | CAPTURE-PATCH-2 |
| CH-002 ChatGPT | INST-GPT-004 General Sessions | phase-1 | — | partial | blocked | not-registered | not-started | not-started | not-started | not-started | `PENDING` | CAPTURE-PATCH-2 |
| CH-003 Manus | INST-MAN-001 Durable Gate Reports | phase-1 | — | accessible | ready | registered | not-started | not-started | not-started | not-started | `ACQUIRED` | PROCESS-DOCS-RUNBOOK-GATE |
| CH-003 Manus | INST-MAN-002 Historical Tasks (194) | phase-1 | — | accessible | pending-gate | not-registered | not-started | not-started | not-started | not-started | `CATALOGUED` | MANUS-HISTORICAL-ACQUISITION-GATE |
| CH-004 Obsidian | INST-OBS-001 Y-WORLD (YOS repo) | phase-1 | — | accessible | pending-gate | not-registered | not-started | not-started | not-started | not-started | `CATALOGUED` | OBSIDIAN-MARKDOWN-METADATA-DRY-RUN-GATE |
| CH-004 Obsidian | INST-OBS-002 Y-WORLD (standalone) | phase-1 | — | accessible | pending-gate | not-registered | not-started | not-started | not-started | not-started | `CATALOGUED` | OBSIDIAN-MARKDOWN-METADATA-DRY-RUN-GATE |
| CH-004 Obsidian | INST-OBS-003 Local vaults (7) | phase-1 | — | blocked | blocked | not-registered | not-started | not-started | not-started | not-started | `BLOCKED` | OBSIDIAN-VAULT-DISCOVERY-GATE |
| CH-005 Notion | INST-NOT-001 Y-World workspace | phase-1 | — | accessible | pending-gate | not-registered | not-started | not-started | not-started | not-started | `CATALOGUED` | NOTION-METADATA-INVENTORY-GATE |
| CH-005 Notion | INST-NOT-002 Yannick personal | phase-1 | — | partial | blocked | not-registered | not-started | not-started | not-started | not-started | `DISCOVERED` | NOTION-METADATA-INVENTORY-GATE |
| CH-005 Notion | INST-NOT-003 Namaste-Welfare | deferred | — | partial | not-started | n/a | n/a | n/a | n/a | n/a | `DEFERRED` | — |
| CH-006 Mem0 | INST-MEM-001 Mem0 store | phase-1 | `SIGNAL_ONLY` | accessible | n/a | n/a | n/a | n/a | n/a | n/a | `SIGNAL_ONLY` | — |
| CH-007 LLM Internal | INST-LLM-001→005 All LLMs | phase-1 | `HEURISTIC_CONTEXT_ONLY` | partial | blocked | n/a | n/a | n/a | n/a | n/a | `HEURISTIC_ONLY` | LLM-HEURISTIC-CONTEXT-USAGE-POLICY |
| CH-008 Other LLM | INST-SES-001→004 | phase-1 | — | blocked | blocked | not-registered | not-started | not-started | not-started | not-started | `BLOCKED` | CAPTURE-PATCH-2 |
| CH-009 Sites | INST-SITE-001/002 Git-backed | phase-1 | `PROVENANCE_CENSUS_ONLY` | accessible | pending-gate | not-registered | n/a | n/a | n/a | n/a | `CATALOGUED` | MANUS-SITES-INVENTORY-GATE |
| CH-009 Sites | INST-SITE-004 Deployed (no Git) | phase-1 | `PROVENANCE_CENSUS_ONLY` | blocked | blocked | not-registered | n/a | n/a | n/a | n/a | `BLOCKED` | MANUS-SITES-INVENTORY-GATE |
| CH-010 Apps | INST-APP-001/002 | phase-1 | `PROVENANCE_CENSUS_ONLY` | blocked | blocked | not-registered | n/a | n/a | n/a | n/a | `BLOCKED` | REPLIT-LOVABLE-INVENTORY-GATE |
| CH-011 General Web | — | — | — | — | — | — | — | — | — | — | `DEFERRED_FOR_LATER_KAP_YOUNIVERSE_EXTENSION` | — |
| CH-012 Google Drive | — | phase-2 | — | — | — | — | — | — | — | — | `DEFERRED_FOR_LATER_KAP_YOUNIVERSE_EXTENSION` | — |
| CH-013 Generic Uploads | — | — | — | — | — | — | — | — | — | — | `DEFERRED_FOR_LATER_KAP_YOUNIVERSE_EXTENSION` | Files must be persisted to Git to become canonical |
| CH-014 Unknown Legacy | — | — | — | — | — | — | — | — | — | — | `DEFERRED_FOR_LATER_KAP_YOUNIVERSE_EXTENSION` | — |

---

## Matrix Summary

| Status | Count | Notes |
|---|---|---|
| `ACQUIRED` (pipeline-ready) | 5 | GIT-001/002, GPT-001/002, MAN-001 |
| `SIGNAL_ONLY` | 1 | MEM-001 — not a corpus |
| `HEURISTIC_CONTEXT_ONLY` | 1 | LLM Internal — not canonical |
| `CATALOGUED` (pending gate) | 41+ | All remaining Git repos, Obsidian Git, Notion Y-World, MAN-002 |
| `PENDING` (user action) | 6 | GPT-003/004, LLM-001→005 |
| `BLOCKED` | 8 | OBS-003, SES-001→004, SITE-004, APP-001/002 |
| `DEFERRED` | 8+ | Legacy repos, Namaste, YOUniverse sources |
| `DEFERRED_FOR_LATER_KAP_YOUNIVERSE_EXTENSION` | 4 channels | Web, GDrive, Uploads, Legacy |

### ID Normalization Status

| Level | Status |
|---|---|
| L0 Channel IDs (CH-*) | ✅ CANONICAL — no change |
| L1 Instance IDs (GIT-*, GPT-*, MAN-*, etc.) | ✅ CANONICAL — confirmed |
| L2 Object IDs (SO-*) | ✅ CANONICAL — 27 objects registered |
| L3 Fragment IDs (SF-*) | ✅ CANONICAL — 9 legacy IDs mapped, 0 unresolved |

### Corrected Next Gate Sequence (SOURCE-TAXONOMY-ALIGNMENT-PATCH)
1. `SOURCE-TAXONOMY-ALIGNMENT-PATCH` ← current
2. `SOURCE-FRAGMENT-ID-NORMALIZATION-PATCH`
3. `PROCESS-DOCS-RUNBOOK-GATE`
4. `OBSIDIAN-MARKDOWN-METADATA-DRY-RUN-GATE`
5. `NOTION-METADATA-INVENTORY-GATE`
