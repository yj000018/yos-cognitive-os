# YOS_Memory — Preserve / Save

`YOS_Memory` owns the native Y-OS conversation-to-Git memory write primitive.

## Runtime contract

The reference engine in `preserve.py` provides deterministic mechanics for:

- global Preserve command recognition;
- preservation-state persistence;
- duplicate/additive/conflicting/superseding/new-topic classification;
- amend-first mutation planning;
- historical-lineage protection for contradiction/supersession;
- Key Memory escalation signal;
- Offline Queue staging status;
- verified-boundary advancement.

Semantic extraction from a raw conversation is intentionally performed by the active cognitive executor (ChatGPT or another Y-OS-compatible LLM). The deterministic engine consumes structured durable candidates; this separation avoids pretending a string heuristic can replace semantic judgment.

## CO-001 Canonical Object projection

`canonical_objects.py` adds an optional, side-effect-free projection layer for Preserve transactions. It does not replace Preserve planning, reconciliation, routing, Git persistence, or verification.

CO-001 exposes two Canonical Object profiles:

- `pack.conversation_delta` — an auditable projection of the durable delta, reconciliation result, mutations, provenance, lineage, and content hash;
- `event.preservation` — an immutable preservation lifecycle event derived from the conversation-delta object.

Important invariants:

- Canonical Object identity is semantic and independent of YARP/BUS transport identities;
- object IDs are deterministically derived from Preserve transaction ID + profile;
- contradiction and supersession lineage is preserved;
- no-delta Preserve may emit an audit object but does not create duplicate Git content;
- `verified_remote_sha` appears only when an actually verified SHA is supplied;
- offline transactions remain exactly `STAGED — NOT COMMITTED` and never imply remote verification;
- the projection module performs no Git I/O and no conversation parsing.

Contracts:

- `canonical_object.schema.json`
- `preserve_canonical_profiles.schema.json`

## State

Recommended per-project runtime state: `.yos/state/preserve.json`.

The boundary advances only after a verified remote SHA. Offline queue packages remain pending and do not become canonical truth until pushed and verified.

## Policy dependencies

- `02_Architecture/Synthesis/DEDUPLICATION-AND-MERGE-POLICY.md`
- `02_Architecture/Synthesis/CONTRADICTION-SUPERSESSION-POLICY.md`
- `02_Architecture/Memory/YOS-PRESERVE-SAVE-ARCHITECTURE.md`
- external fallback: `yj000018/new-to-be-merged/Git-Recovery-Queue`
- escalation: `key-memory-preserve`

Run tests:

```bash
python -m unittest discover -s 03_Modules/YOS_Memory/tests -v
```
