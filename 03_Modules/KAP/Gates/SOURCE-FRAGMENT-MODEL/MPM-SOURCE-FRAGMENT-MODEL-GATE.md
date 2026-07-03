# MPM Full Body — SOURCE-FRAGMENT-MODEL-GATE

> **Source:** MPM-FULL-BODY-CAPTURE-PACK-CURRENT-CHATGPT-YOS-KAP.md (MPM-005)
> **Status:** FULL_BODY_PERSISTED
> **Capture date:** 2026-07-03

---

SOURCE-FRAGMENT-MODEL-GATE

```markdown
# MPM — SOURCE-FRAGMENT-MODEL-GATE

## Role

You are Manus acting as **YOS/KAP Executor** under the supervision of the **ChatGPT Guardian Architect**.

You must execute the gate:

```text
SOURCE-FRAGMENT-MODEL-GATE
```

This is a cognitive architecture gate.

This gate must define the minimal traceable unit of future knowledge acquisition before any broad extraction, normalization, synthesis, or merge.

---

# 0. Context

The YOS Control Plane has now been created in:

```text
yj000018/yos-cognitive-os
```

KAP is now treated as a module/process inside YOS.

The validated doctrine is:

```text
Architecture cognitive avant absorption massive.
```

Meaning:

```text
No broad acquisition before cognitive architecture.
No synthesis before merge model.
No normalization before provenance model.
No current-best synthesis before decision-thread model.
No scale-up before pilot validation.
```

The next architectural need is to define the **Source Fragment Model**.

A Source Fragment is the smallest traceable source unit that YOS/KAP may later ingest, classify, link, score, review, and eventually use as evidence.

This model must be defined before extracting content from Notion, Manus, ChatGPT, Obsidian, Git, Markdown, Google Drive, Web, Mem0, or other sources.

---

# 1. Absolute Rules

1. Do not perform broad source acquisition.
2. Do not import Notion, Manus, ChatGPT, Obsidian, Git, or other source corpora.
3. Do not run full extraction pipelines.
4. Do not generate current-best synthesis.
5. Do not normalize source content into final knowledge.
6. Do not merge old sources.
7. Do not mutate source systems.
8. Do not delete, rewrite, or restructure existing source material.
9. Do not treat any source fragment as canonical truth.
10. Do not collapse duplicates.
11. Do not create final Thought Lines yet.
12. Do not create final Claims yet.
13. Do not create final Decision Threads yet.
14. Do not use ZIP as primary corpus.
15. Preserve Git/Markdown-first persistence.
16. All durable outputs must be written inside the Git-backed YOS structure.
17. If existing files already define related concepts, inspect and extend them instead of duplicating blindly.
18. If uncertainty exists, mark it clearly.

---

# 2. Mission

Design the **Source Fragment Model** for YOS/KAP.

The gate must answer:

1. What is a Source Fragment?
2. What is not a Source Fragment?
3. What source systems can produce fragments?
4. What metadata must every fragment preserve?
5. How should provenance be represented?
6. How should timestamps be handled?
7. How should fragment IDs be generated?
8. How should fragments relate to future Claims, Thought Lines, Decision Threads, Impasses, and Syntheses?
9. What fragment statuses are allowed?
10. How should source confidence and authority be represented?
11. How should privacy/sensitivity flags be represented?
12. How should fragments remain useful for both human review and AI retrieval?
13. What must be validated before fragment extraction is authorized?

---

# 3. Scope

This gate defines the model only.

Allowed:

```text
architecture documentation
schema definition
registry skeleton
lifecycle definition
status taxonomy
example fragments
validation checklist
gate report
```

Forbidden:

```text
real source extraction
bulk import
full ChatGPT export processing
Notion workspace dump
Manus task body ingestion
Obsidian real vault scan
current-best synthesis
claim extraction at scale
decision-thread reconstruction
```

---

# 4. Required Conceptual Model

Define Source Fragment as:

```text
A Source Fragment is a traceable, bounded unit of source material preserved with provenance, timestamps, source-system metadata, extraction context, and future linkage capacity.
```

A Source Fragment may be:

```text
Notion page
Notion database row
Manus report
Manus MPM
Manus durable output
ChatGPT session capture pack
ChatGPT conversation segment
Obsidian note
Markdown file
Git commit
Git file
Gate report
Registry entry
Architecture decision record
Uploaded report
Web reference
Google Drive document
Mem0 memory item
Tool output
```

A Source Fragment is not:

```text
canonical synthesis
final truth
deduplicated conclusion
merged knowledge
current-best understanding
claim automatically treated as true
decision automatically treated as active
```

---

# 5. Required Source Fragment Fields

Define a canonical metadata model with at least:

```yaml
fragment_id:
fragment_title:
source_system:
source_type:
source_subtype:
source_path_or_url:
source_repo:
source_branch:
source_commit:
source_created_at:
source_modified_at:
source_observed_at:
extracted_at:
captured_by:
capture_method:
content_boundary:
content_hash:
language:
project_scope:
domain_tags:
candidate_thought_lines:
candidate_claims:
candidate_decisions:
candidate_impasses:
maturity_hint:
authority_hint:
provenance_confidence:
sensitivity_level:
canonical_status:
review_status:
merge_status:
supersession_status:
related_fragments:
notes:
```

---

# 6. Required Controlled Vocabularies

Define allowed values for the following fields.

## 6.1 source_system

At minimum:

```text
ChatGPT
Manus
Notion
Obsidian
Markdown
Git
Google_Drive
Mem0
Web
Uploaded_File
Manual_Note
Unknown
```

## 6.2 source_type

At minimum:

```text
conversation
session_capture_pack
mpm
gate_report
architecture_doc
decision_log
registry
notion_page
notion_database
obsidian_note
markdown_file
git_file
git_commit
web_reference
memory_item
tool_output
report
unknown
```

## 6.3 canonical_status

```text
not_canonical
candidate_evidence
active_control_plane
historical_source
implementation_evidence
superseded_source
requires_review
```

## 6.4 review_status

```text
unreviewed
metadata_reviewed
content_reviewed
approved_for_claim_extraction
approved_for_decision_threading
rejected
needs_human_review
```

## 6.5 merge_status

```text
not_merged
staged
linked_to_claim
linked_to_thought_line
linked_to_decision_thread
linked_to_impasse
merged_into_synthesis
merge_blocked
```

## 6.6 supersession_status

```text
unknown
active
historical
superseded
supersedes_other
contradicted
needs_supersession_review
```

## 6.7 maturity_hint

```text
raw
rough_note
exploratory
proposal
validated_gate_output
implementation_evidence
active_doctrine
canonical_candidate
deprecated
unknown
```

## 6.8 authority_hint

```text
user_directive
guardian_architect_decision
manus_execution_report
git_commit_evidence
source_document
memory_hint
external_reference
unknown
```

## 6.9 provenance_confidence

```text
high
medium
low
unknown
```

## 6.10 sensitivity_level

```text
public
internal
private
sensitive
secret_reference_only
unknown
```

Do not store secrets.

---

# 7. Required Lifecycle

Define Source Fragment lifecycle:

```text
1. discovered
2. registered
3. metadata_captured
4. content_captured
5. reviewed
6. linked
7. claim_extraction_ready
8. decision_thread_ready
9. synthesis_ready
10. archived_or_superseded
```

Important:

A fragment may remain useful even if superseded.  
Superseded fragments preserve history and rationale.

---

# 8. Required Relationship Model

Define how Source Fragments later connect to:

```text
Claims
Thought Lines
Decision Threads
Evolution Events
Impasse Registry
Current Best Knowledge
Human Views
AI Indexes
```

Rules:

1. One fragment may support many claims.
2. One claim may be supported by many fragments.
3. One fragment may belong to several candidate thought lines.
4. One fragment may provide implementation evidence for a decision.
5. One fragment may become an impasse example.
6. One fragment must never be erased by synthesis.
7. Synthesis must point back to fragments.
8. Fragments may contradict each other without either being deleted.
9. Source chronology must be preserved.
10. Later fragments are not automatically more correct.

---

# 9. Required Output Files

Create or update the following files inside `yj000018/yos-cognitive-os`.

If a file already exists, update it carefully and preserve prior content.

## 9.1 Main Model Document

```text
02_Architecture/Synthesis/SOURCE-FRAGMENT-MODEL.md
```

Must include:

1. Definition.
2. Purpose.
3. What is / is not a Source Fragment.
4. Field model.
5. Controlled vocabularies.
6. Lifecycle.
7. Relationship model.
8. Human review implications.
9. AI retrieval implications.
10. Examples.
11. Validation rules.
12. Open questions.

## 9.2 JSON Schema

```text
02_Architecture/Synthesis/_schemas/source_fragment.schema.json
```

Create a minimal but usable JSON schema matching the model.

Schema must include:

```text
required fields
allowed enums
string/date fields
arrays for tags and relationships
basic validation constraints
```

Do not over-engineer.

## 9.3 Source Fragment Registry Skeleton

```text
05_Registries/SOURCE-FRAGMENT-REGISTRY.md
```

Create a registry table with columns:

| Fragment ID | Title | Source System | Source Type | Canonical Status | Review Status | Merge Status | Related Thought Lines | Path/URL | Notes |
|---|---|---|---|---|---|---|---|---|---|

Seed only with known control-plane artifacts from existing Git files if safe.

Do not invent source fragments from unavailable sources.

At minimum, include entries for:

```text
CURRENT-CHATGPT-YOS-KAP-SESSION-CAPTURE.md
YOS-KAP-SESSION-CAPTURE-PACK-Control-Plane-Bootstrap-2026-07-02.md
YOS-CONTROL-PLANE-BOOTSTRAP-GATE-REPORT.md
ARCHITECTURE-BEFORE-ABSORPTION.md
YOS-STRATEGIC-DOCTRINE.md
```

Only include them if files exist in the repo.

## 9.4 Source Fragment Intake Policy

```text
02_Architecture/Synthesis/SOURCE-FRAGMENT-INTAKE-POLICY.md
```

Must define:

1. What can be registered as a fragment.
2. What cannot be registered yet.
3. Metadata-only intake.
4. Content intake.
5. Review requirements.
6. How to handle missing timestamps.
7. How to handle unclear source origin.
8. How to handle duplicates.
9. How to handle private/sensitive material.
10. How to prevent premature synthesis.

## 9.5 Source Fragment Examples

```text
02_Architecture/Synthesis/SOURCE-FRAGMENT-EXAMPLES.md
```

Provide examples for:

1. ChatGPT session capture pack.
2. Manus gate report.
3. Notion page.
4. Obsidian note.
5. Git commit.
6. MPM document.
7. Architecture decision record.
8. Memory item.

Examples must be illustrative and clearly marked as examples.

Do not represent examples as real source data unless actually present.

## 9.6 AI Index Stub

```text
07_AI_Indexes/source_fragment_index.json
```

Create a minimal machine-readable index.

It may include known control-plane files already present.

If no safe real entries are available, create an empty index with schema notes.

## 9.7 Gate Report

```text
06_Reports/Gates/SOURCE-FRAGMENT-MODEL-GATE-REPORT.md
```

Must include:

1. Gate summary.
2. Files created/updated.
3. Model summary.
4. Controlled vocabularies summary.
5. Lifecycle summary.
6. Relationship model summary.
7. Registry summary.
8. Schema summary.
9. Compliance matrix.
10. Gaps.
11. Blockers.
12. Recommendation.
13. Explicit final status.

---

# 10. Required Compliance Matrix

The gate report must include:

| Rule | Status | Evidence |
|---|---|---|

At minimum:

```text
No broad acquisition occurred.
No source corpus was imported.
No current-best synthesis was generated.
No source mutation occurred.
No legacy repo merge occurred.
Source Fragment model was defined.
JSON schema was created.
Registry skeleton was created.
AI index stub was created.
Git/Markdown-first persistence respected.
Git status checked.
```

---

# 11. Required Git Proof

At the end, run:

```text
git rev-parse --show-toplevel
git status --short
git log --oneline -5
```

Commit if appropriate and allowed by existing workflow.

Recommended commit message:

```text
define source fragment model for YOS KAP cognitive architecture
```

Final report must include:

1. Git root.
2. Commit hash if committed.
3. Files created.
4. Files modified.
5. Git status.
6. Any uncommitted changes.

---

# 12. Final Status Options

Use exactly one:

## Full Pass

```text
SOURCE_FRAGMENT_MODEL_GATE_PASS_READY_FOR_CLAIM_MODEL_GATE
```

Use if model, schema, registry, examples, intake policy, AI index, and gate report are complete.

## Pass With Minor Gaps

```text
SOURCE_FRAGMENT_MODEL_GATE_PASS_WITH_MINOR_GAPS_READY_FOR_CLAIM_MODEL_GATE
```

Use if model is coherent but minor examples/index/registry gaps remain.

## Partial Pass

```text
SOURCE_FRAGMENT_MODEL_GATE_PARTIAL_PASS_REQUIRES_MODEL_PATCH
```

Use if the model exists but schema or policy is incomplete.

## Hold

```text
SOURCE_FRAGMENT_MODEL_GATE_HOLD_REQUIRES_SCOPE_DECISION
```

Use if the model cannot be defined because source boundaries or repo architecture are unresolved.

## Fail

```text
SOURCE_FRAGMENT_MODEL_GATE_FAIL_BOUNDARY_BREACHED
```

Use if broad acquisition, source mutation, unauthorized merge, or current-best synthesis occurred.

---

# 13. Final Response Required From Manus

Return a concise execution report containing:

1. Final gate status.
2. Git repo root.
3. Commit hash if committed.
4. Files created/updated.
5. Source Fragment definition.
6. Controlled vocabularies created.
7. Lifecycle defined.
8. Registry entries created.
9. Schema path.
10. AI index path.
11. Compliance matrix.
12. Gaps.
13. Blockers.
14. Confirmation that no broad acquisition occurred.
15. Confirmation that no current-best synthesis was generated.
16. Confirmation that no source mutation occurred.
17. Recommendation for next gate.

Do not return only a narrative summary.

Do not package as ZIP-only.

Do not claim full pass unless the required files actually exist in Git.
```

---

# Missing / Partial Items

| MPM | Missing Content | Reason | Recommended Action |
|---|---|---|---|
| CONNECTOR-DESIGN-GATE | Full MPM body | Referenced in this conversation but full body not visible in current recoverable context | Recover from original ChatGPT session or Manus/KAP repo; replace stub |
| AGENT-ROLE-GATE + MANUS-SESSION-GRAB-METADATA-CENSUS | Full MPM body | Referenced in this conversation but full body not visible in current recoverable context | Recover from original ChatGPT session or Manus/KAP repo; replace stub |
| CONNECTOR-IMPLEMENTATION-GATE | Full MPM body | Referenced in this conversation but full body not visible in current recoverable context | Recover from original ChatGPT session or Manus/KAP repo; replace stub |
| PIPELINE-FEASIBILITY-GATE | Full MPM body | Referenced in this conversation but full body not visible in current recoverable context | Recover from original ChatGPT session or Manus/KAP repo; replace stub |
| PIPELINE-FEASIBILITY Executive Matrix Addendum | Full addendum body | Referenced in this conversation but full body not visible in current recoverable context | Recover from original ChatGPT session or Manus/KAP repo; replace stub |
| OBSIDIAN-PIPELINE-VALIDATION-GATE | Full MPM/addendum body | Referenced in this conversation but full body not visible in current recoverable context | Recover from original ChatGPT session or Manus/KAP repo; replace stub |
| OBSIDIAN-PIPELINE-PATCH-GATE | Full MPM body | Referenced in this conversation but full body not visible in current recoverable context | Recover from original ChatGPT session or Manus/KAP repo; replace stub |
| NOTION-PIPELINE-CONTROLLED-EXECUTION-GATE | Full MPM body | Referenced in this conversation but full body not visible in current recoverable context | Recover from original ChatGPT session or Manus/KAP repo; replace stub |

---

# Recommended Manus Persistence Targets

Persist this file as:

```text
00_Control_Plane/Session_Captures/MPM-FULL-BODY-CAPTURE-PACK-CURRENT-CHATGPT-YOS-KAP.md
```

Persist each full MPM body separately as:

```text
02_Architecture/Synthesis/Gates/MPM-EVOLUTIONARY-KNOWLEDGE-MERGE-ARCHITECTURE-GATE.md
00_Control_Plane/Gates/MPM-YOS-CONTROL-PLANE-BOOTSTRAP-GATE.md
00_Control_Plane/Gates/ADDENDUM-SESSION-DOCTRINE-CAPTURE-GIT-PERSISTENCE.md
00_Control_Plane/Gates/MANUS-HANDOFF-YOS-KAP-SESSION-CAPTURE-PERSISTENCE.md
02_Architecture/Synthesis/Gates/MPM-SOURCE-FRAGMENT-MODEL-GATE.md
```

Update:

```text
05_Registries/SESSION-CAPTURE-REGISTRY.md
00_Control_Plane/Session_Captures/UNCAPTURED-ITEMS-BACKLOG.md
```

Recommended status after persistence:

```text
MPM_FULL_BODY_CAPTURE_PARTIAL_PASS_REMAINING_STUBS_PENDING_ORIGINAL_SESSION_RECOVERY
```
