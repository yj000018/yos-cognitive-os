# Active Decision Log

> Y-OS Control Plane — All active decisions
> Last updated: 2026-07-03 (CAPTURE-PATCH from 2 ChatGPT session packs)

---

## Decisions from Manus KAP Sessions (2026-07-03)

| ID | Decision | Status | Domain |
|---|---|---|---|
| DEC-YOS-001 | YOS is the global container; KAP is a module inside YOS | CONFIRMED | Architecture |
| DEC-YOS-002 | Architecture cognitive avant absorption massive — no broad acquisition before model validation | CONFIRMED | Governance |
| DEC-YOS-003 | Git + Markdown is the durable authority for all knowledge | CONFIRMED | Persistence |
| DEC-YOS-004 | New doctrine → Control Plane; recovered sources → Source Staging | CONFIRMED | Repository |
| DEC-YOS-005 | Master repo `yos-cognitive-os` + linked repos + mandatory REPO-REGISTRY + repo_index.json | CONFIRMED | Git architecture |
| DEC-YOS-006 | Session doctrine capture is mandatory; uncaptured items must be listed in backlog | CONFIRMED | Workflow |
| DEC-YOS-007 | Phase 1 = yOS/KAP self-knowledge; Phase 2 = Project Knowledge & State; Phase 3 = YOUniverse | CONFIRMED | Phases |
| DEC-YOS-008 | LLM Internal Memory extraction deferred until full taxonomy is known | DEFERRED | Source |
| DEC-YOS-009 | Mem0 = ACQUIRED; derivative source; no dedicated gate needed | CONFIRMED | Source |
| DEC-YOS-010 | YOUniverse sources catalogued now; connectors built in Phase 3 | DEFERRED | Source |
| DEC-YOS-011 | ZIPs are transport only, not source of truth | CONFIRMED | Governance |
| DEC-YOS-012 | Scope is a tag on fragments (scope:yos / scope:youniverse / scope:both), not a pipeline branch | CONFIRMED | Engine |

---

## Decisions from ChatGPT Session — CURRENT-CHATGPT-YOS-KAP-SESSION-CAPTURE.md (2026-07-03)

| ID | Decision | Status | Domain |
|---|---|---|---|
| DEC-CGPT-001 | Proceed through gates, not uncontrolled acquisition | ACTIVE | KAP roadmap |
| DEC-CGPT-002 | KAP must be repositioned as a YOS module | ACTIVE | Architecture |
| DEC-CGPT-003 | Create YOS Control Plane as durable Git-backed authority | ACTIVE | Repository |
| DEC-CGPT-004 | Recovered sources go to Source Staging, not canonical truth | ACTIVE | Source governance |
| DEC-CGPT-005 | Do not leave doctrines only in ChatGPT | ACTIVE | Persistence |
| DEC-CGPT-006 | Use master repo + linked/submodule repos + mandatory repo registry | ACTIVE_CANDIDATE | Git architecture |
| DEC-CGPT-007 | Confidentiality is not a limiting constraint for repo architecture | ACTIVE_USER_CONSTRAINT | Repo |
| DEC-CGPT-008 | Capture all current and parallel KAP session outputs | ACTIVE | Session capture |

---

## Decisions from ChatGPT Session — YOS-KAP-SESSION-CAPTURE-PACK-Control-Plane-Bootstrap-2026-07-02.md (2026-07-02)

| ID | Decision | Status | Domain |
|---|---|---|---|
| DEC-BOOT-001 | WP0-CORE-1 = ACCEPTED (lean KAP Core Engine backbone) | ACCEPTED | Architecture |
| DEC-BOOT-002 | WP1-R Addendum = ACCEPTED_WITH_MINOR_CORRECTIONS (Source Registry is living lifecycle catalog) | ACCEPTED | Source registry |
| DEC-BOOT-003 | KAP-ARCH-1 = ACCEPTED_WITH_REQUIRED_CORRECTION (roadmap too extraction-oriented; corrected flow required) | ACCEPTED | Roadmap |
| DEC-BOOT-004 | KAP-ARCH-1-PATCH = ACCEPTED (removed extraction urgency, reinforced architecture-before-extraction) | ACCEPTED | Roadmap |
| DEC-BOOT-005 | STRUCTURE-GATE = ACCEPTED_WITH_CONDITION; status: `STRUCTURE_GATE_PASS_WITH_MINOR_GAPS_READY_FOR_CONNECTOR_DESIGN_GATE` | ACCEPTED | Gate |
| DEC-BOOT-006 | CONNECTOR-DESIGN-GATE defined and MPM created | DEFINED | Gate |
| DEC-BOOT-007 | ConvoFlow = REFERENCE_ONLY + SANDBOX_TEST; not canon; requires CONVOFLOW-AUDIT-1 | REFERENCE | Tool |
| DEC-BOOT-008 | All future Architect → Manus handoffs must be real downloadable Markdown files | ACTIVE | Workflow |
| DEC-BOOT-009 | Notion is frozen legacy / future migration target / future decommission target | ACTIVE | Source |
| DEC-BOOT-010 | ChatGPT2Notion deprecated as active path; new pipelines must target Git/MD | DEPRECATED | Pipeline |
| DEC-BOOT-011 | WP2-NOTION-DECOMMISSION sprint needed (future, not now) | PLANNED | Sprint |
| DEC-BOOT-012 | Corrected roadmap: `KAP-ARCH-1-PATCH → STRUCTURE-GATE → CONNECTOR-DESIGN-GATE → PHASE-1-SEED-PLAN → targeted acquisition only if approved` | ACTIVE | Roadmap |

---

## Repo / Git Decisions (from CURRENT-CHATGPT-YOS-KAP-SESSION-CAPTURE.md)

| ID | Decision | Status |
|---|---|---|
| REPO-001 | Root repo should be YOS-level, not KAP-level; suggested name: `yos-cognitive-os` | CONFIRMED (done) |
| REPO-002 | KAP becomes module inside YOS at `03_Modules/KAP/` | CONFIRMED (done) |
| REPO-003 | Use master repo + submodules/linked repos (mechanism to finalize) | CANDIDATE |
| REPO-004 | Repo registry mandatory: `05_Registries/REPO-REGISTRY.md` + `07_AI_Indexes/repo_index.json` | CONFIRMED (done) |
| REPO-005 | New strategic documents must be captured in Git immediately | CONFIRMED (done) |

---

## Pipeline Decisions (from CURRENT-CHATGPT-YOS-KAP-SESSION-CAPTURE.md)

| ID | Pipeline | Decision | Status |
|---|---|---|---|
| PIPE-001 | Manus | High-value, selective, gated; metadata census + relevance scoring + selective extraction | ACTIVE |
| PIPE-002 | ChatGPT/OpenAI | Core source; capture packs now; later export schema processing | ACTIVE |
| PIPE-003 | Obsidian/Markdown | High-feasibility; fake-vault testing allowed; real scan gated | ACTIVE |
| PIPE-004 | Notion | Active controlled pipeline; verification required | ACTIVE_WITH_VERIFICATION |
| PIPE-005 | Git/Repos | Master YOS repo + linked repos + mandatory registry; no legacy merge yet | ACTIVE |
| PIPE-006 | Mem0/Memory | Hint layer, not source of truth | ACTIVE |
| PIPE-007 | Web/External | Controlled metadata/citation only | ACTIVE |

---

## Human/AI Exploitation Decisions (from CURRENT-CHATGPT-YOS-KAP-SESSION-CAPTURE.md)

| ID | Decision | Status |
|---|---|---|
| HAI-001 | KAP/YOS must support human navigation (project views, decision trails, dashboards, review queues) | ACTIVE |
| HAI-002 | KAP/YOS must support AI exploitation (machine-readable registries, routing indexes, decision graphs) | ACTIVE |
| HAI-003 | The goal is not document accumulation — it is provenance, chronology, maturity, decisions, supersessions | ACTIVE |
