# Y-OS Memory Capability Registry

> Status: ACTIVE
> Last updated: 2026-08-14
> Canonical module root: `03_Modules/YOS_Memory/`

This registry indexes native Y-OS memory capabilities. It is a routing/index surface, not a separate memory layer.

| Capability ID | Natural command | Owner | State | Escalation | Offline fallback | Status |
|---|---|---|---|---|---|---|
| `YOS_MEMORY_PRESERVE_SAVE` | canonical: `preserve` = `save`; secondary aliases: `préserve`, `archive`, equivalents | `03_Modules/YOS_Memory` | `.yos/state/preserve.json` | `key-memory-preserve` for critical checkpoint/handoff | `yj000018/new-to-be-merged/Git-Recovery-Queue` | ACTIVE |

## `YOS_MEMORY_PRESERVE_SAVE`

Purpose: preserve the **durable conversational delta** into Git-backed memory, not the transcript.

### Canonical invocation

`preserve` and `save` are strict synonyms. Both invoke the same capability, transaction semantics, routing and state machine. No behavioral distinction is permitted between them.

The L1 Kernel / Constitution / Custom Instructions layer only exposes this global intent and routes it to YOS Memory. It does not duplicate the preservation engine.

Secondary natural-language aliases such as `préserve` and `archive` may resolve to the same intent, but are not canonical command names.

Canonical contract:

- architecture: `02_Architecture/Memory/YOS-PRESERVE-SAVE-ARCHITECTURE.md`
- runtime engine: `03_Modules/YOS_Memory/preserve.py`
- command manifest: `03_Modules/YOS_Memory/PRESERVE-COMMAND.yaml`
- state schema: `03_Modules/YOS_Memory/preserve_state.schema.json`
- tests: `03_Modules/YOS_Memory/tests/test_preserve.py`

Required invariants: inspect Git before writing; amend existing living documents first; preserve provenance/contradiction/supersession; no verified success without a remote SHA; boundary advances only after remote verification; otherwise use `STAGED — NOT COMMITTED` Offline Queue semantics.
