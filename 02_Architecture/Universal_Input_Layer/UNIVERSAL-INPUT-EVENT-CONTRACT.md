# Universal Input Event Contract v0.1

The Universal Input Event is the canonical ingress envelope for Y-OS.

```text
EVENT = CHANNEL × MODE × INTENT × CONTEXT × OBJECT
```

The envelope contains:

- `event_id` — deterministic identifier derived from normalized ingress identity;
- `received_at` — adapter-supplied timestamp or `null` when unavailable;
- `channel` — how the signal entered;
- `mode` — broad processing posture with source/confidence; v0.1 defaults to `yos`;
- `intent` — explicit or inferred intent with source/confidence; v0.1 defaults to `auto`;
- `context` — bounded contextual hints;
- `object` — normalized payload surface/object;
- `routing` — neutral placeholders for later cognition/routing enrichment;
- `provenance` — stable source reference identifying the ingress occurrence.

## Ownership boundary

The Universal Input Layer does **not** interpret human conversational meaning. That belongs to Y-COM.

It does **not** decide workflows or actions. That belongs to cognition/routing.

It does **not** transport machine messages. That belongs to MTP/BUS.

## Determinism

For the same normalized ingress identity, `event_id` is stable. Every adapter must supply a non-empty `raw_source_ref` so repeated identical surfaces remain distinguishable occurrences. `received_at` and downstream `context` enrichment are intentionally not part of identity.
