# Y-OS Preserve / Save Architecture

> Status: ACTIVE
> Date: 2026-08-12
> Owner: `03_Modules/YOS_Memory`
> Invocation surfaces: ChatGPT, Project Pilot, Manus, Codex, future Y-OS conversational surfaces

## Decision

`Preserve / Save` is a native **YOS_Memory write transaction**, not a standalone application, not a ChatGPT-only skill, and not a new orchestration layer.

The memory module owns the transaction contract and preservation boundary. Existing Y-OS components keep their existing authority:

- **Project Pilot / PPM-PDD** supplies project/session identity and local context when available.
- **ChatGPT / Guardian Architect** performs semantic rereading, durable-delta distillation, ambiguity detection and architecture-sensitive reconciliation.
- **Y-OS Agency / Manus** executes broader multi-file or cross-repository persistence work.
- **Codex** executes code-heavy repository changes and tests when Preserve contains software implementation deltas.
- **KAP/KRE synthesis policies** supply non-destructive deduplication, contradiction, supersession and provenance semantics.
- **Key Memory Preserve** receives high-value checkpoints, handoffs, architecture authority and cross-session bootstrap artifacts.
- **Git** is durable authority.
- **Git Offline Queue** is the fallback when remote persistence cannot be verified.

This is the smallest integration that satisfies the required behavior while preserving existing ownership boundaries.

## User contract

The following are global natural-language memory-write triggers:

`préserve`, `preserve`, `save`, `archive`, `remember this`, `capture le delta`, plus natural modifiers.

A bare `préserve` means: infer project and scope, reread accessible context, identify the last verified preservation boundary, distill only durable new value, reconcile against Git truth, amend existing living documents first, persist, verify the remote SHA, advance the boundary, and return a compact receipt.

It does **not** mean transcript export or ordinary conversation summary.

## Transaction lifecycle

1. **CAPTURE** — resolve project/session/scope and load last verified preservation state.
2. **DISTILL** — semantic executor extracts durable candidates: decisions, architecture, definitions, stable project state, constraints, workflows, validated discoveries, rationale and unresolved items worth retaining.
3. **RECONCILE** — inspect relevant Git truth and classify each candidate as duplicate, additive, conflicting, superseding or genuinely new.
4. **PERSIST** — amend existing living documents by default; create only when semantically necessary; preserve provenance and lineage.
5. **VERIFY** — verify remote commit SHA. Only then advance the preservation boundary and issue `VERIFIED` receipt.

If GitHub is unavailable or remote verification fails, stage an immutable package in the existing `yj000018/new-to-be-merged/Git-Recovery-Queue` mechanism and return exactly `STAGED — NOT COMMITTED`. The verified boundary does not advance until the queued mutation is later pushed and remotely verified.

## Preservation state

Runtime hosts persist a small JSON state sidecar. Recommended project-local path:

`.yos/state/preserve.json`

State fields:

- `last_marker` — last accessible conversation marker included in a verified transaction;
- `last_git_sha` — last verified remote SHA;
- `last_transaction_id` — last verified Preserve transaction;
- `preserved_fingerprints` — semantic-candidate fingerprints used as a secondary duplicate guard;
- `pending_queue_ids` — staged offline packages not yet verified remotely.

Priority for finding the delta boundary:

1. verified explicit state marker;
2. previous verified Preserve receipt/transaction;
3. reconciliation against current Git documents;
4. conservative semantic comparison if no explicit state exists.

State is an optimization and continuity aid, never a substitute for Git reconciliation. A boundary may only advance after a verified remote SHA.

## Amend-first reconciliation

For every durable candidate:

1. inspect Git for an existing living document in the same project/topic/lineage;
2. if semantically already present, record `duplicate` and make no content mutation;
3. if it extends or clarifies that living document, `amend` it;
4. if it contradicts or replaces prior truth, amend while preserving the older state, provenance and explicit contradiction/supersession relationship;
5. create a new document only for a new subject, independent architecture/decision lineage, standalone operational artifact, checkpoint/handoff, or when amendment would make the target incoherent.

The engine reuses `02_Architecture/Synthesis/DEDUPLICATION-AND-MERGE-POLICY.md` and `02_Architecture/Synthesis/CONTRADICTION-SUPERSESSION-POLICY.md`. It must not invent a second contradiction model.

## Key Memory escalation

Escalate from ordinary Preserve to `key-memory-preserve` when any of the following holds:

- explicit checkpoint/handoff/transfer request;
- critical architecture/canon decision needing cross-session bootstrap;
- context saturation or recovery risk;
- project restart must be possible from one durable artifact;
- user marks the material as key/critical/canonical.

Ordinary project deltas should remain lightweight and should normally amend the project’s existing living documents instead of producing a Key Document.

## Execution routing

| Work shape | Primary execution | Notes |
|---|---|---|
| Conversation reread, semantic delta, ambiguity/provenance | ChatGPT / Guardian Architect | Default cognitive front end |
| Project identity, local state, specialist routing | Project Pilot | Context provider / invocation surface, not memory owner |
| Broad multi-file or multi-repo Git mutation | Manus through Y-OS Agency | Executor, not architecture authority |
| Code/config/tests/repository implementation delta | Codex | Can be delegated by Pilot/Manus/ChatGPT |
| Contradiction / merge semantics | Existing KAP/KRE policies | Reuse canonical models |
| Critical checkpoint / handoff | key-memory-preserve | Escalation path |
| Git unavailable/unverifiable | Git Offline Queue | Must report `STAGED — NOT COMMITTED` |

## Persistence receipt

A successful user-facing receipt should contain only the useful evidence:

- durable delta captured;
- amended files;
- newly created files only if necessary;
- repository/path;
- verified remote SHA(s);
- unresolved contradictions/ambiguities;
- optional resume pointer.

A no-delta transaction is valid and should say no durable delta was found; it must not duplicate content merely to produce a commit.

## CasaTAO reference behavior

The first live reference remains canonical: the conversation’s new Spatial Reality / CasaTAO concepts were reconciled against Git and amended into the existing living document `spatial-reality/10-ENVIRONMENTS/CASATAO.md`, rather than creating another summary. Reference commits: `a57500e3e1a84996da6e4367950d567d7d12572b`; terminology correction `futur MUZEE`: `3fb40dd80d2d4010de58e782e5767479cf6bc069`.

## Failure modes and guards

- **Transcript dumping:** forbidden; distill durable delta only.
- **Document proliferation:** amend-first is mandatory.
- **False consensus:** contradictions remain explicit until resolved by authority/policy.
- **False persistence claim:** no `VERIFIED` without remote SHA proof.
- **Boundary drift:** advance state only after verified persistence.
- **Offline loss:** stage Git-ready immutable queue package and keep it pending.
- **Architectural duplication:** Project Pilot, KAP/KRE, Key Memory and Agency are composed, not reimplemented.
