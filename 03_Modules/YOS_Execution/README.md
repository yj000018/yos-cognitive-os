# YOS Execution — CO-002 Pilot

CO-002 is an opt-in architecture pilot proving the smallest Canonical Object execution round trip.

```text
pack.execution → YARP envelope → deterministic executor → pack.result + artifact.evidence → ExecutionTrace
```

## Authority boundaries

- YARP remains owned by `yj000018/YOS/01_BACKBONE/YARP`.
- EHS remains owner of production execution/result payload semantics; these pilot profiles are projections only.
- Execution Trace is a derived read model, not a Task Ledger and has no lifecycle authority.
- The deterministic executor has no external-world authority: no network, shell, browser, Home Assistant, device, provider, or BUS actions.
- CO-001 Preserve and `YOS_Memory` are consumed read-only.

## Identity

`object_id`, `envelope_id`, `correlation_id`, `trace_id`, `task_id`, `run_id`, and `attempt_id` are intentionally distinct. Retrying transport changes envelope/attempt identity without changing the semantic `pack.execution` identity.

## Error boundary

A malformed YARP envelope raises `YarpTransportError` before execution and produces no domain result. An executor-domain failure produces an explicit `pack.result` with `outcome = failure`.

## Rollback

Deleting `03_Modules/YOS_Execution/` restores pre-CO-002 behavior. No existing runtime component is modified by this pilot.
