# YOS Execution — CO-002 Pilot

CO-002 is an opt-in architecture pilot proving the smallest Canonical Object execution round trip.

```text
pack.execution → YARP-inspired pilot envelope → deterministic executor → pack.result + artifact.evidence → ExecutionTrace
```

## Authority boundaries

- YARP remains owned by `yj000018/YOS/01_BACKBONE/YARP`.
- CO-002 reuses YARP v1 identity/correlation conventions as a pilot projection only; the resulting envelope is **not** asserted to be a canonical YARP v1 message.
- Canonical YARP v1 `EXECUTE_MP` remains Mega-Prompt-specific (`mp_id`, `mp_content`, `mp_mode`, `correlation_id`).
- EHS remains owner of production execution/result payload semantics; these pilot profiles are projections only.
- Execution Trace is a derived read model, not a Task Ledger and has no lifecycle authority.
- The deterministic executor has no external-world authority: no network, shell, browser, Home Assistant, device, provider, or BUS actions.
- CO-001 Preserve and `YOS_Memory` are consumed read-only.

## Follow-up gate

Generalizing YARP from Mega-Prompt-specific `EXECUTE_MP` semantics to generic Canonical Object transport is explicitly deferred to a separate YARP-owner-domain architecture gate. CO-002 must not silently widen YARP v1.

## Identity

`object_id`, `envelope_id`, `correlation_id`, `trace_id`, `task_id`, `run_id`, and `attempt_id` are intentionally distinct. Retrying transport changes envelope/attempt identity without changing the semantic `pack.execution` identity.

## Error boundary

A malformed CO-002 transport envelope raises `YarpTransportError` before execution and produces no domain result. An executor-domain failure produces an explicit `pack.result` with `outcome = failure`.

## Rollback

Deleting `03_Modules/YOS_Execution/` restores pre-CO-002 behavior. No existing runtime component is modified by this pilot.
