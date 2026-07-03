# Y-OS Memory Blueprint

**Document type:** Technical architecture + capability blueprint + public positioning draft  
**Module:** Y-OS Memory / Personal Cognitive Memory OS  
**Status:** Working blueprint v0.1  
**Purpose:** Define the architecture, feature set, product boundaries, killed products, implementation layers, and public narrative for the Y-OS memory module.

---

## 1. Executive summary

Y-OS Memory is not just an agent memory layer, a vector database, or a personal notes system.

It is a **Personal Cognitive Memory OS**: a memory lifecycle system for capturing, consolidating, canonicalizing, routing, and injecting personal and project knowledge across LLMs, agents, tools, files, automations, and human workflows.

The core thesis:

> **We do not need a better vector DB. We need a better capture → consolidation → context pipeline.**

The positioning:

> **Y-OS is a personal cognitive memory OS, not just an agent memory layer.**

The operating formula:

```text
Recall captures.
Git syncs.
mem0 serves.
LangMem extracts.
Manus consolidates.
Obsidian remembers.
Git protects.
Agents receive context packs.
```

A shorter mantra:

```text
Capture → Recall → Consolidate → Canonicalize → Route → Inject → Govern
```

Y-OS Memory is closer to an **operating system for cognition** than to a memory database.

---

## 2. Strategic positioning

Most current AI memory products focus on:

```text
Store → Retrieve → Personalize
```

Y-OS Memory focuses on:

```text
Capture → Clean → Resolve → Validate → Canonicalize → Version → Route → Inject
```

### 2.1 Core differentiators

Y-OS Memory must explicitly solve:

1. **Raw capture**  
   Capture full raw sessions, documents, chats, pages, screen activity, files, repositories, and sensor streams before summarization or extraction.

2. **Cross-LLM / cross-session continuity**  
   Maintain durable continuity across ChatGPT, Claude, Manus, Cursor, local agents, and future LLM clients.

3. **Canonical memory graph**  
   Maintain a validated knowledge graph in Obsidian Markdown, with typed notes, links, metadata, lifecycle status, and Git-backed history.

4. **Dedupe and contradiction cleanup**  
   Detect duplicates, obsolete memories, contradictions, conflicting versions, and unclear claims.

5. **Runtime context packs**  
   Compile task-specific context packs for Manus, GPT, Claude, Cursor, custom agents, and automation workflows.

6. **Agent routing**  
   Route the right memories to the right model, agent, workflow, or tool based on task type and context.

7. **Git-backed personal knowledge filesystem**  
   Treat canonical memory as readable, scriptable, diffable, portable Markdown files rather than trapped SaaS objects.

8. **Memory lifecycle management**  
   Manage memory as a lifecycle, not an append-only pile of embeddings.

---

## 3. Core architecture

```text
┌─────────────────────────────────────────────────────────────┐
│                      Y-OS MEMORY OS                         │
├─────────────────────────────────────────────────────────────┤
│  1. Capture Layer                                           │
│     Screenpipe, Recall, raw LLM sessions, docs, chats,      │
│     pages, files, Git repos, sensors, phone data, APIs       │
├─────────────────────────────────────────────────────────────┤
│  2. Raw Capture Lake                                        │
│     Immutable/raw source archive with timestamps, sources,   │
│     provenance, privacy level, and extraction status         │
├─────────────────────────────────────────────────────────────┤
│  3. Recall / Memory Service Layer                           │
│     mem0, Recall, Obsidian access, Git pull, MCP memory      │
├─────────────────────────────────────────────────────────────┤
│  4. Extraction + Graph Intelligence                         │
│     LangMem primitives, entity/relation extraction,          │
│     document → knowledge graph extraction, GraphRAG patterns │
├─────────────────────────────────────────────────────────────┤
│  5. Consolidation Engine                                    │
│     Manus/Y-OS skills: dedupe, merge, contradiction,         │
│     summary, validation, lifecycle status, promotion         │
├─────────────────────────────────────────────────────────────┤
│  6. Canonical Memory Graph                                  │
│     Obsidian Markdown vault + metadata + backlinks + Git     │
├─────────────────────────────────────────────────────────────┤
│  7. Runtime Context Compiler                                │
│     Task-specific packs for Manus, GPT, Claude, Cursor,      │
│     agents, scripts, workflows, dashboards                   │
├─────────────────────────────────────────────────────────────┤
│  8. Governance Layer                                        │
│     Review queues, memory policies, privacy, versioning,     │
│     deletion, stale memory audits, contradiction audits      │
└─────────────────────────────────────────────────────────────┘
```

---

## 4. Final stack decisions

| Layer | Chosen component | Role | Status |
|---|---|---|---|
| Passive desktop capture | **Screenpipe** | Local-first screen/audio/OCR/activity capture | Core |
| PKM capture | **Recall** | Save articles, PDFs, videos, pages, summaries, personal knowledge | Core / likely YOUniverse PKM layer |
| Programmable memory service | **mem0** | Agent memory API, MCP memory server, add/search/update/delete memory | Core |
| Memory extraction primitives | **LangMem** | Conversation/document extraction, memory tools, prompt/procedural memory refinement | Tactical component |
| Agent workflow primitives | **LangGraph** | Optional short-term state, checkpointers, long-running custom Python agent workflows | Tactical / optional |
| Consolidation engine | **Manus / Y-OS skills** | Dedupe, merge, contradictions, validation, canonical promotion | Core |
| Canonical memory | **Obsidian Markdown vault** | Source of truth, typed notes, graph, metadata, direct file access | Core |
| Versioning / backup | **Git** | History, rollback, diff, audit, sync | Core |
| Runtime delivery | **Context packs** | Inject relevant compiled memory into agents/LLMs/tools | Core |
| Temporal graph server | **Zep / Graphiti** | Not added now; copy temporal metadata pattern | Not core for v1 |
| GraphRAG platform | **Cognee** | Not added now; copy extraction/retrieval patterns | Not core for v1 |
| MCP memory UX | **ButlerBrain** | Optional only if it has a uniquely better UX | Not core |
| Legacy note DB | **Notion / Tana** | Replaced as canonical memory by Obsidian/Git | Out |
| Commercial lifelogging | **Rewind / Limitless** | Not reliable path; replaced by Screenpipe | Out |

---

## 5. Memory types

Y-OS Memory uses three main long-term memory types plus a short-term runtime state layer.

### 5.1 Short-term memory

```text
short-term memory = session/thread state
```

Examples:

- current conversation context
- temporary planning state
- active task state
- tool call state
- current agent run state
- in-progress decisions

Storage:

- LLM thread context
- Manus active state
- LangGraph checkpointer if custom agents need it
- ephemeral local runtime state

### 5.2 Long-term memory

```text
long-term memory = persistent user/project/application memory
```

This includes semantic, episodic, and procedural memory.

Storage:

- Obsidian canonical Markdown vault
- mem0 memory service
- raw capture lake
- Recall PKM
- Git history

### 5.3 Episodic memory

```text
episodic memory = experiences/raw sessions/events
```

Examples:

- raw ChatGPT conversations
- Claude conversations
- Manus sessions
- meetings
- screen activity streams
- browser activity
- documents as encountered
- project decisions as they happened
- sensor events
- home events
- phone/location/health events where appropriate

Purpose:

- preserve provenance
- allow future re-extraction
- support audits
- avoid losing detail during premature summarization

### 5.4 Semantic memory

```text
semantic memory = facts/preferences/concepts
```

Examples:

- user preferences
- project architecture decisions
- stable facts
- product decisions
- principles
- conceptual models
- definitions
- reusable knowledge cards

Purpose:

- give agents durable knowledge
- reduce repeated explanation
- support cross-session continuity
- provide high-value retrieval

### 5.5 Procedural memory

```text
procedural memory = prompts/rules/workflows/skills
```

Examples:

- Manus prompts
- Y-OS routing rules
- agent workflows
- n8n workflows
- consolidation policies
- extraction prompts
- publishing procedures
- memory hygiene scripts
- context-pack compiler rules

Purpose:

- make Y-OS improve its own operating procedures
- preserve reusable methods
- support automation and agent routing

---

## 6. Memory lifecycle model

Y-OS Memory must not treat all retrieved memories as equal. Every memory has a lifecycle.

```text
raw → extracted → candidate → validated → canonical → superseded / archived
```

### 6.1 Raw

Unprocessed source material.

Examples:

- full transcript
- full document
- raw screen capture event
- raw PDF
- raw browser page
- raw Git file

Properties:

- immutable where possible
- source-linked
- timestamped
- not trusted as canonical

### 6.2 Extracted

Candidate facts, entities, decisions, preferences, tasks, relationships, or summaries extracted from raw material.

Examples:

- “User selected Screenpipe for passive desktop capture.”
- “mem0 is the preferred programmable memory service.”
- “Obsidian/Git replaces Notion/Tana as canonical memory.”

### 6.3 Candidate

A memory that looks useful but has not yet been validated or merged.

Use cases:

- new preference
- new architecture choice
- potential duplicate
- possible contradiction
- unclear status

### 6.4 Validated

A memory confirmed as useful, accurate, and coherent with the existing canonical graph.

Validation can be:

- automatic when confidence is high
- user-confirmed for critical decisions
- source-backed for external claims
- deduped against existing memories

### 6.5 Canonical

A memory promoted into the Obsidian canonical graph.

Properties:

- stable title
- typed note
- metadata
- backlinks
- source references
- lifecycle status
- Git-tracked

### 6.6 Superseded / Archived

Old memories should not remain silently active.

Examples:

- Notion/Tana canonical memory decision superseded by Obsidian/Git.
- ButlerBrain core status superseded by mem0.
- Rewind/Limitless capture path superseded by Screenpipe.

---

## 7. Temporal metadata model

Y-OS should not add Zep/Graphiti as a core dependency in v1, but should copy the temporal metadata model into Obsidian frontmatter.

Reason:

- Zep/Graphiti is valuable for temporal knowledge graphs.
- But adding a dedicated temporal graph backend now adds complexity and another possible source of truth.
- Obsidian + YAML metadata + Git is sufficient for v1.

### 7.1 Recommended Obsidian frontmatter

```yaml
---
id: mem_2026_06_05_001
title: "mem0 as Y-OS programmable memory service"
type: semantic_memory
status: canonical
lifecycle: canonical
memory_type: semantic
valid_from: 2026-06-05
valid_until:
confidence: high
source_refs:
  - chat:2026-06-05-yos-memory-architecture
supersedes:
  - "ButlerBrain as core memory service"
superseded_by:
last_verified: 2026-06-05
owner: yannick
projects:
  - Y-OS
  - YOUniverse
tags:
  - yos/memory
  - memory/service
  - mem0
privacy: private
routing:
  agents:
    - Manus
    - GPT
    - Claude
    - Cursor
  context_packs:
    - yos-memory-architecture
---
```

### 7.2 Required status values

```text
raw
extracted
candidate
validated
canonical
uncertain
contradicted
superseded
archived
```

### 7.3 Required relation fields

```yaml
supersedes:
superseded_by:
related:
depends_on:
conflicts_with:
derived_from:
source_refs:
```

This copies the strongest practical idea from Zep/Graphiti: memory should know **when it was true**, **what it replaced**, and **what replaced it**.

---

## 8. Capture architecture

Capture is the highest-leverage part of Y-OS Memory.

The goal is not to summarize everything immediately. The goal is to build a trustworthy raw capture substrate that can feed extraction, consolidation, canonicalization, and context injection.

### 8.1 Capture sources

```text
Capture Layer

├─ Screenpipe
│  ├─ screen activity
│  ├─ OCR
│  ├─ audio
│  ├─ meeting transcripts
│  ├─ app activity
│  └─ browser context
│
├─ Recall
│  ├─ articles
│  ├─ PDFs
│  ├─ videos
│  ├─ webpages
│  ├─ summaries
│  └─ PKM graph
│
├─ LLM sessions
│  ├─ ChatGPT
│  ├─ Claude
│  ├─ Manus
│  ├─ Cursor
│  └─ local agents
│
├─ File systems
│  ├─ Obsidian vault
│  ├─ Git repositories
│  ├─ project folders
│  ├─ PDFs / docs / notes
│  └─ exported chats
│
├─ APIs and services
│  ├─ Gmail
│  ├─ Calendar
│  ├─ Contacts
│  ├─ Notion legacy exports
│  ├─ GitHub
│  ├─ n8n workflows
│  └─ Home Assistant
│
├─ Phone and personal data
│  ├─ health data
│  ├─ location data where appropriate
│  ├─ reminders
│  ├─ photos metadata
│  └─ mobile usage events
│
└─ CasaTAO / environment sensors
   ├─ Home Assistant events
   ├─ Frigate camera events
   ├─ presence
   ├─ energy
   ├─ climate
   ├─ security
   └─ device states
```

### 8.2 Screenpipe decision

Screenpipe is the preferred passive desktop capture substrate because it is:

- open-source
- local-first
- desktop-native
- screen/audio/OCR capable
- searchable
- automation-friendly
- compatible with agent workflows
- less fragile than closed commercial lifelogging platforms

Screenpipe should feed the raw capture lake, not directly become canonical truth.

### 8.3 Recall decision

Recall becomes a core PKM/capture layer for YOUniverse.

Role:

```text
Recall = semantic capture ocean / PKM intake
```

It captures and structures external knowledge:

- articles
- PDFs
- videos
- podcasts
- webpages
- saved notes
- research material

But Recall is not canonical truth. It feeds Y-OS consolidation.

### 8.4 Git pull as capture

Git is not only backup. Git pull is also a capture/sync mechanism.

Y-OS should regularly pull from:

- Obsidian memory vault
- project repositories
- prompt repositories
- script repositories
- app repositories
- Y-OS configuration repositories

Then it can extract:

- changed files
- new decisions
- changed prompts
- updated specs
- modified workflows
- deprecated modules

---

## 9. Memory service layer

### 9.1 mem0 role

mem0 is the Y-OS programmable memory service.

Role:

```text
mem0 = agent memory service / retrieval API / MCP memory layer
```

Use mem0 for:

- add memory
- search memory
- update memory
- delete memory
- expose memory to MCP-compatible tools
- agent/user/app/run scoped memories
- cross-agent memory access
- runtime retrieval

mem0 is not the canonical source of truth. It serves memory operationally.

### 9.2 mem0 + Obsidian relationship

```text
Obsidian = canonical truth
mem0 = serving/retrieval layer
```

Possible flows:

```text
Obsidian canonical note → indexed into mem0
mem0 retrieved memory → points back to Obsidian source
new mem0 memory → candidate note in Obsidian
mem0 conflict → consolidation queue
```

### 9.3 MCP memory access

mem0 should expose memory to:

- Claude
- Cursor
- Claude Code
- VS Code
- OpenCode
- custom Manus/Y-OS agents
- other MCP-compatible clients

But memory writes should be governed.

Recommended rule:

```text
Agents may create candidate memories.
Only consolidation promotes canonical memories.
```

---

## 10. LangMem / LangGraph tactical integration

Because Manus/Y-OS has or will have Python agent services, LangMem and LangGraph should be reused tactically as maintained primitives.

They should not become the Y-OS core OS.

### 10.1 LangMem use

Use LangMem for:

- conversation → memory extraction
- document → memory candidate extraction
- semantic / episodic / procedural classification
- memory update suggestions
- prompt/procedural memory refinement
- memory tools inside agents
- evaluating which memories should be written

Flow:

```text
raw session/doc
→ LangMem extraction primitive
→ candidate memories
→ Manus consolidation skill
→ Obsidian canonical note or mem0 candidate
```

### 10.2 LangGraph use

Use LangGraph only when custom Python agents need:

- short-term thread state
- workflow checkpoints
- long-running agent loops
- resumable processes
- stateful memory-aware workflows
- custom memory tools

Do not let LangGraph replace Manus/Y-OS orchestration.

Correct framing:

```text
Y-OS core architecture stays yours.
LangMem = maintained memory primitives.
LangGraph = optional agent-state runtime for custom Python agents.
```

---

## 11. Graph intelligence patterns to copy

Y-OS should copy these patterns from Cognee / GraphRAG / Zep / LangMem ecosystems without necessarily adding those platforms as core dependencies.

### 11.1 Required patterns

```text
document → knowledge graph extraction
entity/relation extraction
graph-aware retrieval
memory search via MCP
structured graph traversal
```

### 11.2 Implementation in Y-OS

```text
Document / transcript / page
→ extraction skill
→ entities
→ relations
→ claims
→ decisions
→ timelines
→ candidate Obsidian notes
→ backlink graph
→ mem0 searchable memory
→ context-pack compiler
```

### 11.3 Example extraction output

```yaml
entities:
  - Y-OS
  - mem0
  - Obsidian
  - Git
  - Screenpipe
  - Recall
relations:
  - subject: mem0
    relation: serves_as
    object: Y-OS programmable memory service
  - subject: Obsidian
    relation: serves_as
    object: canonical memory graph
  - subject: Screenpipe
    relation: captures
    object: desktop activity
claims:
  - "Y-OS is a personal cognitive memory OS, not just an agent memory layer."
decisions:
  - "Use Obsidian/Git instead of Notion/Tana for canonical memory."
status_changes:
  - object: ButlerBrain
    status: optional/peripheral
```

---

## 12. Consolidation engine

The consolidation engine is the part most memory products do not solve.

It is responsible for turning noisy recall into governed memory.

### 12.1 Core tasks

```text
dedupe
merge
contradiction detection
summary
source attribution
confidence scoring
lifecycle status assignment
canonical promotion
supersession
archival
cleanup
```

### 12.2 Consolidation workflow

```text
1. Ingest raw source
2. Extract candidate memories
3. Classify memory type
4. Match against existing memories
5. Detect duplicates
6. Detect contradictions
7. Merge compatible memories
8. Assign lifecycle status
9. Create or update Obsidian note
10. Index or update mem0
11. Commit changes to Git
12. Update context-pack indexes
```

### 12.3 Contradiction queue

Y-OS must maintain a contradiction queue.

Example:

```yaml
contradiction_id: contradiction_2026_06_05_001
new_claim: "ButlerBrain should be core Y-OS memory."
old_claim: "mem0 should be core Y-OS programmable memory service."
status: resolved
resolution: "ButlerBrain is optional/peripheral; mem0 is core."
updated_notes:
  - Memory Service Architecture
  - Killed Products and Optional Tools
```

### 12.4 Dedupe policy

Memories should be merged when they refer to the same stable decision, preference, fact, or procedure.

Dedupe keys:

- entity
- project
- date
- source
- semantic similarity
- lifecycle status
- contradiction relation

### 12.5 Human confirmation policy

Y-OS should avoid asking the user too often, but some cases require confirmation.

Ask the user when:

- a high-impact architectural decision changes
- personal/health/legal/financial memory is uncertain
- two canonical memories conflict
- an automation would delete or overwrite important memory
- a memory has privacy implications

Do not ask when:

- merging obvious duplicates
- archiving obsolete raw candidates
- updating source references
- adding low-risk candidate memories

---

## 13. Canonical memory graph

### 13.1 Obsidian as canonical memory filesystem

Obsidian is the canonical memory layer because it gives:

- direct Markdown access
- local-first ownership
- Git versioning
- fast file manipulation
- readable/editable memory
- backlinks and graph structure
- metadata/frontmatter
- plugin extensibility
- agent-operable files
- no SaaS lock-in

### 13.2 Why Obsidian beats Notion/Tana for Y-OS Memory

Notion and Tana are strong structured knowledge UIs, but for Y-OS canonical memory they are weaker because:

- data is less file-native
- APIs are slower and more constrained
- agent manipulation is less direct
- versioning is weaker than Git
- source-of-truth becomes SaaS-dependent
- bulk refactoring is harder
- local scripts cannot manipulate everything as plain files

Decision:

```text
Notion/Tana = out for canonical memory
Obsidian/Git = canonical memory filesystem
```

Notion may remain useful for:

- presentation
- public databases
- team dashboards
- temporary project views

But not as the source of truth.

### 13.3 Recommended Obsidian folder structure

```text
/Y-OS-Memory

├─ 00_Inbox
│  ├─ raw-candidates
│  ├─ extracted-candidates
│  └─ review-queue
│
├─ 10_Episodic
│  ├─ llm-sessions
│  ├─ meetings
│  ├─ screenpipe-events
│  ├─ recall-captures
│  └─ daily-logs
│
├─ 20_Semantic
│  ├─ people
│  ├─ projects
│  ├─ concepts
│  ├─ decisions
│  ├─ preferences
│  └─ facts
│
├─ 30_Procedural
│  ├─ prompts
│  ├─ skills
│  ├─ workflows
│  ├─ routing-policies
│  ├─ extraction-rules
│  └─ context-pack-rules
│
├─ 40_Context_Packs
│  ├─ yos-memory-architecture.md
│  ├─ casa-tao.md
│  ├─ anandaz.md
│  ├─ y-travel.md
│  ├─ health.md
│  └─ active-projects.md
│
├─ 50_Governance
│  ├─ contradiction-queue.md
│  ├─ dedupe-queue.md
│  ├─ stale-memory-audit.md
│  ├─ privacy-policy.md
│  └─ deletion-policy.md
│
├─ 60_Indexes
│  ├─ entity-index.md
│  ├─ project-index.md
│  ├─ decision-index.md
│  ├─ source-index.md
│  └─ context-pack-index.md
│
└─ 90_Archive
   ├─ superseded
   ├─ deprecated
   └─ old-imports
```

---

## 14. Runtime context packs

Runtime context packs are one of Y-OS Memory's core differentiators.

The goal is not simply to retrieve memories. The goal is to compile the correct working context for the current task, agent, and model.

### 14.1 Context-pack compiler

Inputs:

- user task
- active project
- target agent/model
- relevant canonical memories
- recent episodic context
- procedural rules
- routing policies
- constraints
- current files
- current Git state

Output:

```text
minimal high-signal context bundle
```

### 14.2 Example context packs

```text
yos-memory-architecture
casa-tao-architecture
arc-anandaz-infrastructure
y-travel-product
health-protocol
ai-tools-stack
publishing-strategy
active-week-context
```

### 14.3 Context pack structure

```yaml
---
id: context_pack_yos_memory_architecture
title: Y-OS Memory Architecture Context Pack
target_agents:
  - Manus
  - GPT
  - Claude
  - Cursor
source_notes:
  - Memory Blueprint
  - mem0 Service Decision
  - Obsidian Canonical Graph Decision
  - Screenpipe Capture Decision
last_compiled: 2026-06-05
max_tokens: 8000
---

# Purpose

# Current Decisions

# Architecture

# Active Constraints

# Recent Changes

# Open Questions

# Do Not Use / Killed Products

# Next Actions
```

### 14.4 Injection targets

```text
Manus
GPT
Claude
Cursor
Claude Code
VS Code agents
n8n workflows
local Python agents
MCP clients
future Y-OS web dashboard
```

---

## 15. Agent routing

Memory should not be injected blindly.

Y-OS should route memories according to:

- task type
- project
- model capabilities
- privacy level
- current user intent
- recency
- canonical status
- confidence
- agent role

### 15.1 Example routing policy

```yaml
routing_policy:
  if_task: "architecture design"
  include:
    - canonical semantic memories
    - active project decisions
    - procedural design rules
    - recent contradictions
  exclude:
    - raw screen events unless requested
    - archived memories
    - private health data
  target_agents:
    - GPT
    - Claude
    - Manus
```

---

## 16. Product / tool decisions

### 16.1 Keep core

#### mem0

Keep as the Y-OS programmable memory service.

Why:

- designed for AI agent long-term memory
- API-first
- MCP server available
- supports add/search/update/delete memory flows
- can serve multiple agents and clients
- better architectural fit than ButlerBrain

#### Screenpipe

Keep as passive desktop capture substrate.

Why:

- open-source
- local-first
- screen/audio/OCR capture
- searchable computer activity memory
- automation-friendly
- safer than depending on a commercial lifelogging platform

#### Recall

Keep as PKM/capture ocean.

Why:

- captures external knowledge
- useful for articles, PDFs, videos, pages
- good YOUniverse PKM layer
- feeds consolidation

#### Obsidian + Git

Keep as canonical memory graph.

Why:

- local Markdown
- direct agent access
- fast manipulation
- versioning
- no lock-in
- canonical source of truth

#### Manus / Y-OS skills

Keep as consolidation engine.

Why:

- Y-OS-specific logic lives here
- handles dedupe, merge, contradiction, validation
- compiles context packs
- orchestrates memory lifecycle

#### LangMem / LangGraph

Use tactically.

Why:

- useful maintained primitives
- avoids rebuilding extraction tools from zero
- fits Python agent services
- supports short-term / long-term memory separation
- can improve memory extraction and procedural memory refinement

### 16.2 Copy patterns, do not add as core

#### Zep / Graphiti

Do not add as v1 core.

Copy:

- temporal knowledge graph model
- valid_at / invalid_at concept
- evolving facts
- relationship-aware retrieval
- context assembly ideas

Why not core now:

- adds another backend
- adds complexity
- risks another source of truth
- Obsidian metadata + Git is sufficient for v1

Future trigger to reconsider:

- if Obsidian graph becomes too large
- if temporal multi-hop queries become critical
- if millions of memories require graph-native serving
- if context-pack compiler needs real-time graph traversal at scale

#### Cognee

Do not add as v1 core.

Copy:

- document → graph extraction
- entity/relation extraction
- graph-aware retrieval
- MCP memory search
- structured graph traversal

Why not core now:

- overlaps with Obsidian + mem0 + Manus consolidation
- adds another graph/RAG layer
- may reduce flexibility
- likely too much architecture for v1

### 16.3 Optional / probably out

#### ButlerBrain

Status: optional/peripheral only.

Why not core:

- mem0 also provides MCP memory access
- mem0 is more programmable
- ButlerBrain is more productized UX than infrastructure
- likely redundant if mem0 + Recall + Obsidian are working

Keep only if:

- UX is dramatically better
- it offers a useful manual memory browser
- it bridges an MCP client better than mem0
- it proves better retrieval in practice

#### Notion / Tana

Status: out for canonical memory.

Why:

- direct Markdown + Git is better for Y-OS
- Obsidian is more agent-operable
- Notion/Tana are less suitable as canonical filesystem
- SaaS lock-in and API friction

Possible remaining use:

- dashboard
- public presentation
- team-facing database
- lightweight UI

#### Rewind / Limitless

Status: out.

Why:

- closed commercial path
- not reliable as core infrastructure
- Rewind became Limitless
- Limitless was acquired by Meta and reporting says Rewind app capture is being discontinued
- Screenpipe is open-source/local-first and better aligned

---

## 17. Feature and capability blueprint

### 17.1 Capture capabilities

- Capture full LLM sessions.
- Capture raw documents and PDFs.
- Capture browser pages and external research.
- Capture screen/audio/OCR activity via Screenpipe.
- Capture Recall PKM items.
- Pull changed files from Git.
- Import legacy Notion/Tana data.
- Capture project decisions from chats.
- Capture procedural knowledge from prompts/workflows.
- Capture environmental events from CasaTAO/Home Assistant where relevant.

### 17.2 Extraction capabilities

- Extract entities.
- Extract relations.
- Extract claims.
- Extract decisions.
- Extract preferences.
- Extract tasks.
- Extract procedures.
- Extract contradictions.
- Classify memory type: episodic / semantic / procedural.
- Generate source references.
- Generate candidate Obsidian notes.

### 17.3 Consolidation capabilities

- Merge duplicates.
- Detect contradictions.
- Mark superseded memories.
- Promote canonical memories.
- Archive stale memories.
- Link related memories.
- Update frontmatter.
- Generate indexes.
- Commit to Git.
- Update mem0 index.

### 17.4 Retrieval capabilities

- Semantic search through mem0.
- Graph search through Obsidian links/metadata.
- Raw source lookup.
- Recent episodic recall.
- Project-specific memory retrieval.
- Procedural memory retrieval.
- MCP memory search.
- Context-pack retrieval.

### 17.5 Runtime context capabilities

- Compile context packs.
- Inject memory into Manus.
- Inject memory into GPT.
- Inject memory into Claude.
- Inject memory into Cursor.
- Create task-specific prompts.
- Select memory by model/agent capability.
- Exclude sensitive/private memory where not needed.
- Include current project state.

### 17.6 Governance capabilities

- Dedupe queue.
- Contradiction queue.
- Stale memory audit.
- Privacy classification.
- Source audit.
- Git diff review.
- Memory deletion workflow.
- Confidence scoring.
- Lifecycle tracking.
- Human confirmation for high-impact changes.

---

## 18. Implementation roadmap

### Phase 1 — Foundation

Goal: establish canonical memory and retrieval layer.

Tasks:

- Create Obsidian memory vault structure.
- Add YAML frontmatter schema.
- Initialize Git repo.
- Set up mem0 service.
- Set up mem0 MCP access.
- Define memory types and lifecycle statuses.
- Create first context pack: `yos-memory-architecture`.
- Import current Y-OS memory decisions manually.

Deliverables:

- Obsidian vault
- Git repo
- mem0 working memory service
- first canonical notes
- first context pack

### Phase 2 — Capture integration

Goal: feed raw material into Y-OS.

Tasks:

- Set up Screenpipe.
- Define raw capture folder or database.
- Connect Recall export/API/manual capture flow.
- Pull Obsidian/Git repos into indexing pipeline.
- Export/import key LLM sessions.
- Create source reference format.

Deliverables:

- Screenpipe raw capture flow
- Recall-to-Y-OS intake flow
- Git pull/index flow
- raw session archive pattern

### Phase 3 — Extraction pipeline

Goal: turn raw material into candidate memories.

Tasks:

- Add LangMem extraction primitives.
- Create extraction prompts for episodic/semantic/procedural memories.
- Extract entities and relations.
- Generate candidate YAML notes.
- Add candidate queue.

Deliverables:

- extraction script/service
- candidate memory format
- entity/relation extraction output
- review queue

### Phase 4 — Consolidation engine

Goal: create the actual memory lifecycle management system.

Tasks:

- Build Manus/Y-OS consolidation skills.
- Add dedupe workflow.
- Add contradiction workflow.
- Add lifecycle promotion workflow.
- Add Obsidian note updater.
- Add Git commit automation.
- Add mem0 sync from canonical notes.

Deliverables:

- dedupe skill
- contradiction skill
- canonical promotion skill
- Obsidian updater
- mem0 sync

### Phase 5 — Runtime context compiler

Goal: make memory useful at runtime.

Tasks:

- Create context-pack compiler.
- Define packs by project/domain.
- Define target agent formats.
- Add routing policies.
- Add privacy filters.
- Add context freshness checks.

Deliverables:

- Manus context packs
- GPT context packs
- Claude context packs
- Cursor context packs
- routing rules

### Phase 6 — Governance and productization

Goal: make the system safe, reusable, and sellable.

Tasks:

- Add memory dashboard.
- Add contradiction/stale/duplicate review UI.
- Add export/import tools.
- Package scripts.
- Create public blog series.
- Create GitHub repo or private repo template.
- Prepare paid components/scripts/workflows.

Deliverables:

- memory dashboard
- reusable scripts
- templates
- blog article
- future product landing page

---

## 19. Public blog architecture

This blueprint can become a public article teasing Y-OS and future components.

### 19.1 Recommended article title options

1. **We Do Not Need a Better Vector DB. We Need a Memory OS.**
2. **From Agent Memory to a Personal Cognitive Memory OS**
3. **Y-OS Memory: Capture, Consolidate, Canonicalize, Route, Inject**
4. **Why AI Memory Needs Lifecycle Management, Not Just Retrieval**
5. **Building an Operating System for Cognition**

Recommended title:

> **We Do Not Need a Better Vector DB. We Need a Memory OS.**

### 19.2 Article thesis

Current AI memory products mostly solve retrieval. They let agents remember user facts, search past conversations, or personalize responses.

But real personal AI infrastructure needs something deeper:

```text
capture → consolidation → canonicalization → routing → injection → governance
```

That is the difference between an agent memory layer and a Personal Cognitive Memory OS.

### 19.3 Suggested article outline

```text
1. The problem with current AI memory
2. Why vector databases are not enough
3. The missing layer: memory lifecycle management
4. Y-OS Memory architecture
5. Capture: Screenpipe, Recall, raw sessions, Git, sensors
6. Serve: mem0 and MCP memory
7. Consolidate: Manus/Y-OS skills
8. Remember: Obsidian/Git as canonical graph
9. Inject: runtime context packs
10. Govern: dedupe, contradictions, privacy, lifecycle
11. Why this is an operating system for cognition
12. What will be released next: scripts, templates, workflows, components
```

### 19.4 Where to publish

Recommended publishing stack:

#### Primary home

**Personal/Y-OS website**

Reason:

- own the canonical article
- build SEO around Y-OS
- create product funnel
- link to scripts/components/templates
- avoid platform dependency

#### Distribution layer

**LinkedIn**

Reason:

- best audience for AI infrastructure / founder / architecture positioning
- good for teasing Y-OS
- strong professional reach

#### Developer credibility layer

**GitHub README / technical repo**

Reason:

- publish architecture diagrams, scripts, templates
- attract builders
- make components sellable or reusable

#### Optional essay layer

**Substack or Medium**

Reason:

- good for long-form followers
- less important than own site

Recommended sequence:

```text
1. Publish canonical article on Y-OS / personal site.
2. Publish shortened LinkedIn post with diagram and thesis.
3. Publish GitHub README with technical skeleton and scripts.
4. Later turn it into a paid component/template/workflow pack.
```

### 19.5 Blog teaser copy

```text
Most AI memory systems are still retrieval systems.
They store fragments, embed them, and search them later.

But personal AI does not only need memory retrieval.
It needs memory lifecycle management.

Raw capture.
Cross-LLM/session continuity.
Canonical memory graph.
Dedupe and contradiction cleanup.
Runtime context packs.
Agent routing.
Git-backed personal knowledge filesystem.

That is the direction of Y-OS Memory:
a Personal Cognitive Memory OS.
```

---

## 20. Sellable components and scripts

Y-OS Memory can become a product/component ecosystem.

### 20.1 Possible components

1. **Obsidian Memory Vault Template**
   - folder structure
   - YAML schemas
   - note templates
   - indexes
   - context pack templates

2. **Memory Extraction Scripts**
   - raw chat → candidate memories
   - document → entities/relations
   - meeting → decisions/tasks/memories

3. **mem0 + Obsidian Sync Layer**
   - canonical notes → mem0
   - mem0 candidates → Obsidian review queue
   - source references

4. **Screenpipe → Y-OS Capture Pipeline**
   - desktop activity ingestion
   - OCR/audio event filtering
   - privacy filters
   - high-signal extraction

5. **Context Pack Compiler**
   - Obsidian + mem0 + Git → target-specific context
   - GPT/Claude/Manus/Cursor output formats

6. **Memory Governance Toolkit**
   - dedupe queue
   - contradiction queue
   - stale memory audit
   - supersession manager

7. **Y-OS Memory Dashboard**
   - active memories
   - candidates
   - contradictions
   - context packs
   - source coverage

### 20.2 Potential product ladder

```text
Free article
→ GitHub repo / basic templates
→ paid Obsidian vault template
→ paid scripts/workflows
→ hosted/local Y-OS memory module
→ advisory / implementation service
```

---

## 21. Key design principles

1. **Canonical truth must be file-native.**  
   Memory should be inspectable, editable, scriptable, and Git-backed.

2. **Vector search is not governance.**  
   Retrieval does not solve contradiction, freshness, or truth.

3. **Raw capture must be preserved.**  
   Summaries are useful but lossy. Keep source material where possible.

4. **Agents write candidates, not truth.**  
   Canonical memory requires consolidation and lifecycle governance.

5. **Memory must have status.**  
   Active, uncertain, contradicted, superseded, archived.

6. **Memory must have time.**  
   A fact may be true only during a period.

7. **Memory must route.**  
   The right context must go to the right agent at the right time.

8. **Memory must compile.**  
   Context packs are better than dumping search results.

9. **Simplicity first.**  
   Do not add graph databases, Zep, Cognee, or extra platforms until Obsidian/Git/mem0/Manus hit real limits.

10. **Y-OS is the operating layer.**  
    Tools are components. Y-OS owns lifecycle, routing, and governance.

---

## 22. External references and rationale

These references informed the current technical choices:

- mem0 MCP exposes memory tools to MCP-compatible agents/clients and supports saving, searching, and updating memory: https://docs.mem0.ai/platform/mem0-mcp
- mem0 MCP repository describes add/search/update/delete long-term memories across Claude Desktop, Cursor, custom agents, and other MCP clients: https://github.com/mem0ai/mem0-mcp
- LangChain documentation distinguishes short-term thread-scoped memory from long-term cross-session memory: https://docs.langchain.com/oss/python/langchain/long-term-memory
- LangMem provides primitives for extracting information from conversations, prompt refinement, and long-term memory with optional LangGraph storage integration: https://github.com/langchain-ai/langmem
- Screenpipe is open-source, local-first, and continuously captures screen/audio to create searchable desktop memory: https://github.com/screenpipe/screenpipe
- Screenpipe product site describes local screen/audio/app/browser memory for people and agents: https://screenpipe.com/about
- Zep/Graphiti provides a temporal knowledge graph model with valid/invalid dates and relationship-aware retrieval: https://github.com/getzep/zep
- Graphiti is Zep's open-source temporal knowledge graph framework for context graphs with real-time updates and hybrid retrieval: https://help.getzep.com/graphiti/getting-started/welcome
- Reporting on Limitless/Rewind says Meta acquired Limitless and Rewind app capture was being discontinued: https://9to5mac.com/2025/12/05/rewind-limitless-meta-acquisition/

---

## 23. Final architecture statement

Y-OS Memory is a **Personal Cognitive Memory OS**.

It is not a vector DB, not a note app, not an agent memory plugin, and not a simple retrieval system.

It is a memory lifecycle management architecture:

```text
Capture
→ Recall
→ Extract
→ Consolidate
→ Canonicalize
→ Version
→ Route
→ Inject
→ Govern
```

It combines:

```text
Screenpipe for passive activity capture.
Recall for PKM capture.
mem0 for programmable memory serving.
LangMem for extraction primitives.
Manus/Y-OS skills for consolidation.
Obsidian for canonical memory.
Git for versioning and protection.
Context packs for runtime intelligence.
```

The final pitch:

> **Y-OS is an operating system for cognition.**

