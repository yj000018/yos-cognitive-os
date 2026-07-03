# MPM Full Body — KAP WP1-R Addendum — Source Lifecycle & Project Knowledge Phase Correction

> **Source:** MPM-Full-Body-Capture-Pack-Bootstrap-Session.md (MPM-012)
> **Status:** FULL_BODY_PERSISTED
> **Capture date:** 2026-07-03

---

KAP WP1-R Addendum — Source Lifecycle & Project Knowledge Phase Correction

**Capture status:** FULL_NON_MPM_ADDENDUM  
**Notes:** Full body available and included because the session capture listed it among MPM-like handoff artifacts; source title does not start with '# MPM'.


# KAP WP1-R Addendum — Source Lifecycle & Project Knowledge Phase Correction

**Program:** KAP — Knowledge Assimilation Program  
**Sprint:** WP1-R — Source Registry Reconciliation & Freeze Map  
**Document Type:** Architect Addendum  
**Audience:** Manus Desktop / yOS Execution Partner  
**Authority:** Yannick + ChatGPT Architect  
**Status:** Mandatory addendum before WP1-R execution or patch  
**Style:** Simple, robust, modular, extensible. No over-engineering.

---

## 1. Purpose

This addendum corrects and extends the WP1-R instructions.

WP1-R must not produce a static one-time source list.

WP1-R must create a living Source Registry and Freeze Map that allows KAP to:

1. activate a source;
2. deactivate a source;
3. defer a source;
4. exclude a source;
5. add a new source later;
6. classify the source by phase and domain;
7. attach a connector/adaptor strategy;
8. decide whether it contributes to yOS/MyOS, Project Knowledge, YOUniverse, Telemetry, Archive, or Mem0 candidates.

Current priority remains:

**PHASE 1 — yOS / MyOS self-knowledge consolidation.**

But WP1-R must already define Phase 2 correctly.

Phase 2 is not only project artifacts and deliverables.

Phase 2 is dynamic project self-knowledge.

---

## 2. Core Architectural Rule

KAP Core Engine is a general acquisition, preservation, routing, delta, and distillation backbone.

It must be capable of acquiring from many possible source families, but only activated sources should be acquired now.

KAP must support future sources such as:

- Gemini;
- Grok;
- Perplexity;
- Readwise;
- YouTube favorites and playlists;
- Home Assistant logs;
- sensors;
- project folders;
- design assets;
- local files;
- repositories;
- websites;
- monitoring streams;
- future personal data feeds.

However, capability does not mean immediate acquisition.

WP1-R must distinguish:

- source known;
- source enabled;
- source active now;
- source disabled by choice;
- source disabled due to low quality;
- source deferred for later;
- source deferred for YOUniverse;
- source deferred for telemetry;
- source excluded;
- source blocked by auth or connector.

---

## 3. Source Lifecycle Management

Each source registry entry must support lifecycle management.

Extend the Source Registry entries with these fields:

| field | purpose |
|---|---|
| source_id | Stable identifier |
| source_name | Human-readable name |
| source_family | Type of source |
| source_instance | Specific account/system/feed/repo/log |
| connector_type | API, export, manual, file, git, webhook, MQTT, etc. |
| connector_status | Available, blocked, needs auth, future connector, etc. |
| enabled | Whether the source is enabled in KAP |
| activation_status | Current activation decision |
| activation_reason | Why it is active/enabled |
| deactivation_reason | Why it is disabled if applicable |
| scope_phase | KAP phase where it belongs |
| primary_domain | Main destination domain |
| allowed_domains | Other possible routing domains |
| acquisition_priority | High, medium, low, later |
| quality_status | Good, uncertain, low quality, unused |
| usage_status | Used, unused, occasional, future |
| privacy_level | Public, private, restricted, secret |
| retention_policy | Keep raw, metadata-only, exclude, restricted |
| next_review_date | Date or condition for review |
| owner_decision_required | Whether Yannick/Architect must decide |

Allowed activation_status values:

| value | meaning |
|---|---|
| ACTIVE_NOW | Source is currently in acquisition scope |
| ENABLED_READY | Source can be acquired but is not current priority |
| DISABLED_BY_CHOICE | Deliberately disabled |
| DISABLED_BY_LOW_QUALITY | Disabled because outputs are not valuable enough |
| DISABLED_BY_NON_USE | Disabled because source is not actively used |
| DEFERRED_LATER | Future source, not now |
| DEFERRED_YOUNIVERSE | Future personal/life/user/environment source |
| DEFERRED_TELEMETRY | Future logs/sensors/monitoring source |
| BLOCKED_AUTH | Needs authentication |
| BLOCKED_CONNECTOR | Needs connector/adaptor |
| EXCLUDED_BY_POLICY | Excluded unless Architect explicitly changes scope |
| REQUIRES_ARCHITECT_DECISION | Cannot decide automatically |

---

## 4. Correct Scope Phases

Use these scope phases:

| scope_phase | definition |
|---|---|
| PHASE_1_YOS_MYOS_SELF_KNOWLEDGE | Consolidate yOS/MyOS knowledge about itself |
| PHASE_2_PROJECT_KNOWLEDGE_AND_STATE | Consolidate dynamic project knowledge, state, deltas, assets, resources |
| PHASE_3_YOUNIVERSE_PERSONAL_DATA | Personal/life/user/environment data |
| PHASE_4_TELEMETRY_AND_SENSORS | Logs, sensors, monitoring, home automation, event streams |
| OPTIONAL_FUTURE | Possible future source, not needed now |
| EXCLUDED | Out of scope unless manually reopened |

---

## 5. Phase 1 — Current Focus

Phase 1 is the current active priority.

Focus:

Consolidate yOS / MyOS self-knowledge.

This includes:

- KAP process;
- yOS process;
- MyOS architecture;
- agents;
- skills;
- workflows;
- gates;
- scripts;
- prompts;
- self-improvement rules;
- system logs when relevant;
- operational decisions;
- source registries;
- acquisition protocols;
- delta protocols;
- memory architecture;
- Manus/yOS/KAP execution state;
- GitHub/KAP state;
- Notion/Mem0/yOS memory infrastructure state.

Phase 1 is about enabling the system to know itself and improve its own processes.

---

## 6. Phase 2 — Corrected Project Layer

Do not define Phase 2 as only "project artifacts and deliverables."

Phase 2 is:

**PHASE_2_PROJECT_KNOWLEDGE_AND_STATE**

It includes dynamic consolidation of:

1. project knowledge;
2. project state;
3. project decisions;
4. project architecture;
5. project strategy;
6. project open questions;
7. project blockers;
8. project next actions;
9. project deltas;
10. project timelines;
11. project fact sheets;
12. project source maps;
13. project resource catalogs;
14. project assets;
15. project logos;
16. project documents;
17. project deliverables;
18. project files and links;
19. project memory candidates.

Phase 2 is project self-knowledge.

It answers:

- What is this project?
- Where is it now?
- What changed?
- What decisions were made?
- What sources mention it?
- What assets exist?
- What files/logos/documents/resources belong to it?
- What should update its project fact sheet?
- What should become a future memory candidate?
- What is blocked?
- What is the next action?

---

## 7. Project Fact Sheet Mechanism

WP1-R must anticipate that later KAP phases will maintain living Project Fact Sheets.

A Project Fact Sheet is not just a summary.

It is a dynamic state object for a project.

Each future project fact sheet should include:

| field | purpose |
|---|---|
| project_id | Stable project identifier |
| project_name | Canonical project name |
| aliases | Alternate names |
| domain | yOS, KOSMOS, ELYSIUM, Y World, YOUniverse, KAP, other |
| essence | Short definition |
| current_state | Where the project stands now |
| last_delta | What changed recently |
| key_decisions | Durable decisions |
| open_questions | Unresolved questions |
| blockers | Current blockers |
| next_actions | Recommended next actions |
| related_sources | Source files/sessions that informed it |
| related_assets | Logos, files, docs, links, visuals |
| related_projects | Connections to other projects |
| memory_candidates | Future Mem0 candidates |
| confidence | Confidence level |
| last_updated | Last consolidation date |

WP1-R does not need to generate all project fact sheets now.

WP1-R must classify Phase 2 correctly so later phases can generate and update them.

---

## 8. Project Delta Mechanism

Whenever a source item mentions or affects a project, KAP must be able to classify it as a potential project delta.

Examples:

| source item | possible project delta |
|---|---|
| LLM session about KOSMOS | updates KOSMOS ontology/fact sheet |
| Manus sprint about KAP | updates KAP project state |
| logo file for ELYSIUM | updates ELYSIUM resource catalog |
| Notion page about Y World | updates Y World source map |
| GitHub commit | updates yOS/KAP implementation state |
| design artifact | updates project assets |
| strategy discussion | updates project decisions/open questions |
| project meeting notes | updates current state and next actions |

Required future flags:

| flag | meaning |
|---|---|
| PROJECT_DELTA_CANDIDATE | Item may change project state |
| PROJECT_FACT_SHEET_UPDATE_CANDIDATE | Item may update a project fact sheet |
| PROJECT_RESOURCE_CATALOG_CANDIDATE | Item references assets/resources |
| PROJECT_MEMORY_CANDIDATE | Item may become distilled project memory |
| PROJECT_SOURCE_MAP_CANDIDATE | Item reveals where project data lives |

---

## 9. Project Resource Catalog

Phase 2 must also track project resources.

A project resource catalog is separate from the Project Fact Sheet but linked to it.

Future resource catalog fields:

| field | purpose |
|---|---|
| resource_id | Stable resource identifier |
| project_id | Related project |
| resource_type | Logo, image, document, prompt, report, code, website, design, video, audio, dataset, link, other |
| title | Human title |
| path_or_url | Location |
| source_system | GitHub, Notion, local file, Manus, Obsidian, website, etc. |
| status | Active, draft, obsolete, archived, missing |
| notes | Context |

Allowed resource_type examples:

- LOGO
- IMAGE
- DOCUMENT
- PROMPT
- REPORT
- CODE
- WEBSITE
- DESIGN
- VIDEO
- AUDIO
- DATASET
- LINK
- OTHER_ASSET

---

## 10. Connector Backlog

WP1-R must create a connector backlog.

Create these files:

- `02_SOURCE_REGISTRY/KAP-WP1-R-Connector-Backlog.md`
- `02_SOURCE_REGISTRY/KAP-WP1-R-Connector-Backlog.json`

Required table:

| connector_id | source_family | source_instance | connector_type | current_status | required_for_phase | priority | blocker | next_action |
|---|---|---|---|---|---|---|---|---|

Allowed current_status values:

| value | meaning |
|---|---|
| AVAILABLE_NOW | Connector usable now |
| AVAILABLE_BUT_DISABLED | Connector exists but source not active |
| NEEDS_AUTH | Needs authentication |
| NEEDS_API_KEY | Needs API key |
| NEEDS_EXPORT | Requires export |
| NEEDS_MANUAL_PROCESS | Manual process required |
| FUTURE_CONNECTOR | Future connector |
| NOT_WORTH_BUILDING_NOW | Not useful enough now |
| EXCLUDED | Explicitly excluded |

---

## 11. Current Acquisition Scope Filter

WP1-R must create a current scope filter.

Create these files:

- `03_FREEZE_MAP/KAP-WP1-R-Current-Acquisition-Scope.md`
- `03_FREEZE_MAP/KAP-WP1-R-Current-Acquisition-Scope.json`

Required table:

| source_id | source_name | include_now | phase | reason | excluded_or_deferred_reason |
|---|---|---|---|---|---|

Current include-now rule:

Include sources that help consolidate yOS / MyOS self-knowledge, KAP process state, memory architecture, workflows, agents, gates, scripts, and operational project-system knowledge.

Defer sources whose primary purpose is personal-life modeling for YOUniverse.

Defer telemetry/log/sensor sources unless directly needed for current yOS/KAP self-knowledge.

Defer optional general knowledge sources unless currently used for yOS/KAP/project architecture.

---

## 12. Required Source Classifications

WP1-R must classify at least these examples:

| source | expected current classification |
|---|---|
| Manus / yOS / KAP sessions | PHASE_1_YOS_MYOS_SELF_KNOWLEDGE |
| GitHub KAP repo | PHASE_1_YOS_MYOS_SELF_KNOWLEDGE |
| Notion/Mem0 related to yOS/KAP | PHASE_1_YOS_MYOS_SELF_KNOWLEDGE |
| Project discussions about KOSMOS/ELYSIUM/Y World | PHASE_2_PROJECT_KNOWLEDGE_AND_STATE |
| Project logos/assets/docs | PHASE_2_PROJECT_KNOWLEDGE_AND_STATE |
| Gemini if unused or low quality | DISABLED_BY_NON_USE or DISABLED_BY_LOW_QUALITY |
| Grok if occasionally useful | DEFERRED_LATER |
| Perplexity if used for research | OPTIONAL_FUTURE or PHASE_2_PROJECT_KNOWLEDGE_AND_STATE |
| Home Assistant logs | DEFERRED_TELEMETRY |
| future sensors | DEFERRED_TELEMETRY |
| Readwise | DEFERRED_YOUNIVERSE or PHASE_2_PROJECT_KNOWLEDGE_AND_STATE depending usage |
| YouTube favorite playlists | DEFERRED_YOUNIVERSE |
| personal playlists/favorites | DEFERRED_YOUNIVERSE |
| emails/calendar | DEFERRED_YOUNIVERSE or RESTRICTED_FUTURE_SOURCE |
| browser/shell history | EXCLUDED_BY_POLICY unless Architect requests forensic audit |
| secrets/tokens | RESTRICTED_SECRET_SURFACE and not Git corpus |

---

## 13. Routing Logic Update

Update routing logic as follows:

If an item contains durable information about yOS/MyOS/KAP processes, route to:

**YOS_CORE**

If an item contains durable information about a project, route to:

**PROJECT_KNOWLEDGE**

If it changes the known state of a project, mark:

**PROJECT_DELTA_CANDIDATE = true**

If it may update a project fact sheet, mark:

**PROJECT_FACT_SHEET_UPDATE_CANDIDATE = true**

If it references project files/assets/logos/deliverables, mark:

**PROJECT_RESOURCE_CATALOG_CANDIDATE = true**

If it belongs to user/life/environment modeling, route to:

**YOUNIVERSE**

If it is telemetry/log/sensor data, route to:

**TELEMETRY**

If it contains stable distilled knowledge useful to future agents, mark:

**MEM0_CANDIDATE_LATER = true**

Do not push directly to Mem0 during WP1-R.

---

## 14. Updated WP1-R Completion Criteria

WP1-R is complete only if it produces:

1. central Source State Registry;
2. Global Freeze Map;
3. Source Branch Mapping;
4. Remote Manus filesystem decision;
5. Connector Backlog;
6. Current Acquisition Scope filter;
7. explicit lifecycle status for each source;
8. correct Phase 1 focus;
9. correct Phase 2 project knowledge/state definition;
10. clear deferral of YOUniverse personal data sources unless explicitly activated;
11. clear deferral of telemetry/sensors unless explicitly activated;
12. WP3 impact assessment.

WP3 remains blocked unless Phase 1 yOS/MyOS self-knowledge sources are either acquired, explicitly frozen, or assigned to a later phase with Architect approval.

---

## 15. Final Instruction to Manus

Do not expand this into a huge framework.

Do not acquire future sources.

Do not start WP3.

Apply this addendum to WP1-R so that the Source Registry becomes manageable over time, not a static source list.

End of addendum.
