# MPM Full Body — Mandatory Session Doctrine Capture and Git Persistence Addendum

> **Source:** MPM-FULL-BODY-CAPTURE-PACK-CURRENT-CHATGPT-YOS-KAP.md (MPM-003)
> **Status:** FULL_BODY_PERSISTED
> **Capture date:** 2026-07-03

---

Mandatory Session Doctrine Capture and Git Persistence Addendum

```markdown
# MPM Addendum — Mandatory Session Doctrine Capture and Git Persistence

## Purpose

This addendum strengthens the `YOS-CONTROL-PLANE-BOOTSTRAP + SESSION-DOCTRINE-CAPTURE-GATE`.

The gate must not only create the YOS Control Plane structure.

It must also preserve all high-value doctrines, MPMs, gates, decisions, roadmap decisions, architecture rules, and knowledge-control decisions produced in the current ChatGPT KAP/YOS sessions and related Manus KAP sessions.

Nothing strategic should remain only in ChatGPT conversation history.

---

# 1. Mandatory Capture Rule

All new strategic doctrine must be persisted into the Git-backed YOS Control Plane.

ChatGPT may generate doctrine.

Manus must persist doctrine.

Git is the durable authority.

If an item cannot be captured during this gate, Manus must list it in an explicit uncaptured-items backlog.

---

# 2. Required Capture Sources

Manus must capture from all available inputs:

1. Current ChatGPT KAP/YOS session capture pack.
2. Parallel ChatGPT KAP session capture packs if provided.
3. Manus KAP reports already present in the KAP tree.
4. Manus MPMs and gate reports already generated.
5. Uploaded Markdown reports and review packets.
6. Existing KAP ZIP snapshot, if provided, treated only as transport/snapshot.
7. Any explicit user-provided doctrine text.

If a source is unavailable, mark it as:

`SOURCE_NOT_AVAILABLE_YET`

Do not fake capture.

---

# 3. Required Capture Output Folder

Create:

```text
00_Control_Plane/Session_Captures/
```

Inside it, create:

```text
00_Control_Plane/Session_Captures/CURRENT-CHATGPT-KAP-YOS-SESSION-CAPTURE.md
00_Control_Plane/Session_Captures/PARALLEL-KAP-SESSIONS-CAPTURE-INDEX.md
00_Control_Plane/Session_Captures/MANUS-KAP-SESSION-CAPTURE-INDEX.md
00_Control_Plane/Session_Captures/UNCAPTURED-ITEMS-BACKLOG.md
```

---

# 4. Required Capture Registry

Create or update:

```text
05_Registries/SESSION-CAPTURE-REGISTRY.md
```

Required columns:

| Capture ID | Source Session / Report | Source Type | Captured Items | Git Path | Status | Missing Items | Notes |
|---|---|---|---|---|---|---|---|

Allowed statuses:

```text
CAPTURED
PARTIALLY_CAPTURED
SOURCE_NOT_AVAILABLE_YET
REQUIRES_USER_EXPORT
REQUIRES_MANUS_LOOKUP
REQUIRES_CHATGPT_CAPTURE_PACK
```

---

# 5. Required Documents to Preserve from Current Session

At minimum, preserve the following items as active control-plane knowledge:

## Current Session Core Decisions

1. YOS is the global container.
2. KAP is a module/process inside YOS.
3. KAP handles knowledge assimilation, source acquisition, merge architecture, and synthesis workflows.
4. YOS includes memory, agents, pipelines, decisions, contexts, routing matrices, self-improvement, coordinated agent teams, automation, capability expansion, cognitive RAM, model routing, agent routing, and human/AI exploitation.
5. Architecture cognitive avant absorption massive.
6. No broad source absorption before cognitive architecture.
7. No current-best synthesis before model validation.
8. New doctrines must not remain only in ChatGPT.
9. Git is the durable authority.
10. Control Plane stores active doctrines and decisions.
11. Source Staging stores recovered historical sources pending review.
12. Recovered sources are not automatically canonical truth.
13. Future merge must link active doctrines to supporting, contradicting, or superseded historical sources.
14. Master repo plus linked/submodule repos is acceptable if agent navigation is explicit.
15. Repo registry and machine-readable repo index are mandatory.

## Current Session MPMs / Gate Artifacts to Preserve

1. CONNECTOR-DESIGN-GATE MPM.
2. AGENT-ROLE-GATE + MANUS-SESSION-GRAB-METADATA-CENSUS MPM.
3. CONNECTOR-IMPLEMENTATION-GATE MPM.
4. PIPELINE-FEASIBILITY-GATE MPM.
5. PIPELINE-FEASIBILITY executive matrix addendum.
6. OBSIDIAN-PIPELINE-VALIDATION-GATE doctrine.
7. OBSIDIAN-PIPELINE-PATCH-GATE MPM.
8. NOTION-PIPELINE-CONTROLLED-EXECUTION-GATE MPM.
9. EVOLUTIONARY-KNOWLEDGE-MERGE-ARCHITECTURE-GATE MPM.
10. YOS-CONTROL-PLANE-BOOTSTRAP + SESSION-DOCTRINE-CAPTURE-GATE MPM.

## Pipeline Decisions to Preserve

1. Manus is high-value execution corpus, not low-value.
2. Manus must not be blindly imported as flat task corpus.
3. Manus strategy: metadata census, relevance scoring, durable output detection, noise filtering, selective deep extraction after gate authorization.
4. Obsidian is high-feasibility and technically easy, but real vault scan/import remains gated.
5. Notion cleanup/access is reported complete and pipeline is active controlled, but full dump/canonical merge remains forbidden.
6. ChatGPT exports are core but require capture packs/export/schema handling.
7. Git/Markdown-first remains mandatory.
8. ZIP is transport/snapshot only, not primary corpus.

---

# 6. Required Git Persistence Proof

The gate report must include a Git persistence proof.

If Git is available, run:

```text
git status --short
git rev-parse --show-toplevel
```

Do not commit unless explicitly authorized.

Report:

1. Git root.
2. Files created.
3. Files modified.
4. Untracked files.
5. Recommended commit message.
6. Whether any required capture item remains outside Git.

Recommended commit message:

```text
bootstrap YOS control plane and capture KAP session doctrines
```

---

# 7. Required Uncaptured Items Backlog

Create:

```text
00_Control_Plane/Session_Captures/UNCAPTURED-ITEMS-BACKLOG.md
```

Must include:

| Item | Source | Why Not Captured | Required Action | Priority |
|---|---|---|---|---|

Include entries for:

- parallel ChatGPT KAP sessions not yet exported;
- any Manus session reports not yet available;
- any doctrine mentioned but not present in current input;
- any old KAP/Wild World repo not yet inventoried;
- any ChatGPT export not yet processed.

---

# 8. Required Gate Report Update

Update the final gate report to include:

1. Control Plane structure created.
2. Session capture files created.
3. Doctrines captured.
4. MPMs captured.
5. Registries updated.
6. Uncaptured items backlog.
7. Git persistence proof.
8. Confirmation that no broad source acquisition occurred.
9. Confirmation that no current-best synthesis was generated.
10. Confirmation that no legacy repo merge occurred.
11. Recommendation for next gate.

---

# 9. Correct Final Status Criteria

The gate may only return full pass if:

1. YOS Control Plane structure exists.
2. Core current-session doctrines are written to Markdown.
3. MPMs/gates from this session are captured or listed in backlog.
4. Session capture registry exists.
5. Uncaptured items backlog exists.
6. Git persistence proof is provided.
7. No broad acquisition occurred.
8. No current-best synthesis was generated.

If not all session materials are available, use:

```text
YOS_CONTROL_PLANE_BOOTSTRAP_GATE_PASS_WITH_CAPTURE_GAPS_READY_FOR_CAPTURE_PATCH
```
```

---
