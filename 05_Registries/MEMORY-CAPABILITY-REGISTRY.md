# Y-OS Memory Capability Registry

> Status: ACTIVE
> Last updated: 2026-08-12
> Canonical module root: `03_Modules/YOS_Memory/`

This registry indexes native Y-OS memory capabilities. It is a routing/index surface, not a separate memory layer.

| Capability ID | Natural command | Owner | State | Escalation | Offline fallback | Status |
|---|---|---|---|---|---|---|
| `YOS_MEMORY_PRESERVE_SAVE` | `préserve` / `preserve` / `save` / `archive` / equivalents | `03_Modules/YOS_Memory` | `.yos/state/preserve.json` | `key-memory-preserve` for critical checkpoint/handoff | `yj000018/new-to-be-merged/Git-Recovery-Queue` | ACTIVE |

## `YOS_MEMORY_PRESERVE_SAVE`

Purpose: preserve the **durable conversational delta** into Git-backed memory, not the transcript.

Canonical contract:

- architecture: `02_Architecture/Memory/YOS-PRESERVE-SAVE-ARCHITECTURE.md`
- runtime engine: `03_Modules/YOS_Memory/preserve.py`
- command manifest: `03_Modules/YOS_Memory/PRESERVE-COMMAND.yaml`
- state schema: `03_Modules/YOS_Memory/preserve_state.schema.json`
- tests: `03_Modules/YOS_Memory/tests/test_preserve.py`

Required invariants: inspect Git before writing; amend existing living documents first; preserve provenance/contradiction/supersession; no verified success without a remote SHA; boundary advances only after remote verification; otherwise use `STAGED — NOT COMMITTED` Offline Queue semantics.
