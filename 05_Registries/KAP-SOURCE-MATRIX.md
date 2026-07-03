# KAP-SOURCE-MATRIX

> Y-OS / KAP — Source Status Matrix
> Tracks readiness of every channel and source instance across the full KAP pipeline.
> **Level 1:** `SOURCE-CHANNEL-REGISTRY.md` | **Level 2:** `SOURCE-INSTANCE-REGISTRY.md`
> **Pipelines:** `SOURCE-PIPELINE-REGISTRY.md` | **Access:** `SOURCE-ACCESS-READINESS-MATRIX.md`
> Last Updated: 2026-07-03
> **Living document — update after every gate execution.**

---

## Status Vocabulary

| Column | Values |
|---|---|
| In Scope | `phase-1` / `phase-2` / `deferred` |
| Access Status | `accessible` / `partial` / `blocked` / `unknown` |
| Pipeline Status | `ready` / `pending-gate` / `blocked` / `not-started` |
| Metadata Status | `complete` / `partial` / `pending` / `blocked` / `n/a` |
| Content Status | `acquired` / `pending` / `blocked` / `not-started` / `n/a` |
| Fragment Status | `extracted` / `pending` / `blocked` / `not-started` |
| Claim Status | `extracted` / `pending` / `blocked` / `not-started` |
| Thought Line Status | `seeded` / `pending` / `blocked` / `not-started` |
| Decision Thread Status | `seeded` / `pending` / `blocked` / `not-started` |
| Current Best Status | `ACQUIRED` / `CATALOGUED` / `DISCOVERED` / `PENDING` / `BLOCKED` / `DEFERRED` |

---

## KAP Source Matrix

| Channel | Source Instance | In Scope | Access | Pipeline | Metadata | Content | Fragment | Claim | Thought Line | Decision Thread | Current Best | Next Safe Gate | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CH-001 Git | INST-GIT-001 yos-cognitive-os | phase-1 | accessible | ready | complete | acquired | not-started | not-started | not-started | not-started | `ACQUIRED` | THOUGHT-LINE-SEEDING-GATE | Master control plane |
| CH-001 Git | INST-GIT-002 KAP | phase-1 | accessible | ready | complete | acquired | not-started | not-started | not-started | not-started | `ACQUIRED` | THOUGHT-LINE-SEEDING-GATE | KAP module repo |
| CH-001 Git | INST-GIT-003 YOS (main) | phase-1 | accessible | pending-gate | partial | pending | not-started | not-started | not-started | not-started | `CATALOGUED` | GITHUB-SOURCE-ACQUISITION-GATE | 229+ Obsidian .md files |
| CH-001 Git | INST-GIT-004→006 YOS branches | phase-1 | accessible | pending-gate | partial | pending | not-started | not-started | not-started | not-started | `CATALOGUED` | GITHUB-SOURCE-ACQUISITION-GATE | Doctrine, phase-iii, master |
| CH-001 Git | INST-GIT-007→009 ELYSIUM repos | phase-1 | accessible | pending-gate | partial | pending | not-started | not-started | not-started | not-started | `CATALOGUED` | GITHUB-SOURCE-ACQUISITION-GATE | Ontology + book |
| CH-001 Git | INST-GIT-010→015 yos-* core repos | phase-1 | accessible | pending-gate | partial | pending | not-started | not-started | not-started | not-started | `CATALOGUED` | GITHUB-SOURCE-ACQUISITION-GATE | bus, project, llm-pipeline, skills, continuity, governance |
| CH-001 Git | INST-GIT-016→035 yos-* peripheral repos | phase-1 | accessible | pending-gate | partial | pending | not-started | not-started | not-started | not-started | `CATALOGUED` | GITHUB-SOURCE-ACQUISITION-GATE | Voice, scripts, extensions, tools |
| CH-001 Git | INST-GIT-036→041 youniverse/legacy | deferred | accessible | not-started | n/a | n/a | n/a | n/a | n/a | n/a | `DEFERRED` | — | Phase 2 or legacy |
| CH-002 ChatGPT | INST-GPT-001 Bootstrap Pack | phase-1 | accessible | ready | complete | acquired | not-started | not-started | not-started | not-started | `ACQUIRED` | THOUGHT-LINE-SEEDING-GATE | In Git verbatim |
| CH-002 ChatGPT | INST-GPT-002 Current Pack | phase-1 | accessible | ready | complete | acquired | not-started | not-started | not-started | not-started | `ACQUIRED` | THOUGHT-LINE-SEEDING-GATE | In Git verbatim |
| CH-002 ChatGPT | INST-GPT-003 Parallel Sessions (6+) | phase-1 | partial | blocked | pending | pending | not-started | not-started | not-started | not-started | `PENDING` | CAPTURE-PATCH-2 | Awaiting user export |
| CH-002 ChatGPT | INST-GPT-004 General Sessions | phase-1 | partial | blocked | pending | pending | not-started | not-started | not-started | not-started | `PENDING` | CAPTURE-PATCH-2 | conversations.json not provided |
| CH-003 Manus | INST-MAN-001 Durable Gate Reports | phase-1 | accessible | ready | complete | acquired | not-started | not-started | not-started | not-started | `ACQUIRED` | THOUGHT-LINE-SEEDING-GATE | All in Git |
| CH-003 Manus | INST-MAN-002 Historical Tasks (194) | phase-1 | accessible | pending-gate | partial | pending | not-started | not-started | not-started | not-started | `CATALOGUED` | MANUS-HISTORICAL-ACQUISITION-GATE | Non-primary corpus |
| CH-004 Obsidian | INST-OBS-001 Y-WORLD (YOS repo) | phase-1 | accessible | pending-gate | partial | pending | not-started | not-started | not-started | not-started | `CATALOGUED` | OBSIDIAN-PIPELINE-VALIDATION-GATE | Via GitHub API |
| CH-004 Obsidian | INST-OBS-002 Y-WORLD (standalone) | phase-1 | accessible | pending-gate | partial | pending | not-started | not-started | not-started | not-started | `CATALOGUED` | OBSIDIAN-PIPELINE-VALIDATION-GATE | May overlap OBS-001 |
| CH-004 Obsidian | INST-OBS-003 Local vaults (7) | phase-1 | blocked | blocked | blocked | blocked | not-started | not-started | not-started | not-started | `BLOCKED` | OBSIDIAN-VAULT-DISCOVERY-GATE | Paths unknown |
| CH-005 Notion | INST-NOT-001 Y-World workspace | phase-1 | accessible | pending-gate | partial | pending | not-started | not-started | not-started | not-started | `CATALOGUED` | NOTION-PIPELINE-CONTROLLED-EXECUTION-GATE | API accessible, census incomplete |
| CH-005 Notion | INST-NOT-002 Yannick personal | phase-1 | partial | blocked | pending | pending | not-started | not-started | not-started | not-started | `DISCOVERED` | NOTION-PIPELINE-CONTROLLED-EXECUTION-GATE | May contain yOS content |
| CH-005 Notion | INST-NOT-003 Namaste-Welfare | deferred | partial | not-started | n/a | n/a | n/a | n/a | n/a | n/a | `DEFERRED` | — | Phase 2 only |
| CH-006 Mem0 | INST-MEM-001 Mem0 store | phase-1 | accessible | ready | complete | acquired | n/a | n/a | n/a | n/a | `ACQUIRED` | — | Signal/index only. 316 entries. |
| CH-007 LLM Internal | INST-LLM-001→005 All LLMs | phase-1 | partial | blocked | n/a | pending | not-started | not-started | not-started | not-started | `PENDING` | LLM-INTERNAL-MEMORY-EXTRACTION-GATE | Deferred until taxonomy |
| CH-008 Other LLM | INST-SES-001→004 Claude/Gemini/Grok/Perplexity | phase-1 | blocked | blocked | blocked | blocked | not-started | not-started | not-started | not-started | `BLOCKED` | CAPTURE-PATCH-2 | No export API |
| CH-009 Sites | INST-SITE-001→002 Git-backed sites | phase-1 | accessible | pending-gate | partial | pending | not-started | not-started | not-started | not-started | `CATALOGUED` | GITHUB-SOURCE-ACQUISITION-GATE | Code in Git |
| CH-009 Sites | INST-SITE-004 Deployed (no Git) | phase-1 | blocked | blocked | blocked | blocked | not-started | not-started | not-started | not-started | `BLOCKED` | MANUS-SITES-INVENTORY-GATE | URLs unknown |
| CH-010 Apps | INST-APP-001→002 Replit/Lovable | phase-1 | blocked | blocked | blocked | blocked | not-started | not-started | not-started | not-started | `BLOCKED` | REPLIT-LOVABLE-INVENTORY-GATE | No inventory |
| CH-013 Uploads | INST-UPL-001 Session uploads | phase-1 | accessible | ready | complete | acquired | not-started | not-started | not-started | not-started | `ACQUIRED` | THOUGHT-LINE-SEEDING-GATE | All persisted to Git |

---

## Matrix Summary

| Status | Count | Instances |
|---|---|---|
| `ACQUIRED` (ready for seeding) | 7 | GIT-001/002, GPT-001/002, MAN-001, MEM-001, UPL-001 |
| `CATALOGUED` (pending gate) | 41+ | GIT-003→035, OBS-001/002, NOT-001, MAN-002, SITE-001/002 |
| `PENDING` (user action required) | 6 | GPT-003/004, LLM-001→005 |
| `BLOCKED` (access issue) | 8 | OBS-003, SES-001→004, SITE-004, APP-001/002 |
| `DEFERRED` | 8 | GIT-036→041, NOT-003 |

### Immediate next gates (no blockers)
1. `THOUGHT-LINE-SEEDING-GATE` — seed from 7 ACQUIRED instances
2. `GITHUB-SOURCE-ACQUISITION-GATE` — metadata-only scan of 39 remaining repos
3. `NOTION-PIPELINE-CONTROLLED-EXECUTION-GATE` — metadata-only census

### Blocked — requires user input
1. `CAPTURE-PATCH-2` — ChatGPT parallel sessions export
2. `OBSIDIAN-VAULT-DISCOVERY-GATE` — 7 vault paths on Mac
3. `LLM-INTERNAL-MEMORY-EXTRACTION-GATE` — after taxonomy complete
