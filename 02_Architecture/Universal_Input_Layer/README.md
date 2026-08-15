# Y-OS Universal Input Layer

## Canonical boundary

```text
External signal / human / device / service
                ↓
        Universal Input Layer
                ↓
        Universal Input Event
                ↓
              Y-COM
                ↓
       Cognition / Routing
                ↓
              MTP
                ↓
              BUS
```

- **Universal Input Layer** normalizes where/how a signal enters.
- **Y-COM** normalizes what a human-AI interaction means.
- **Cognition/Routing** decides what the system should do.
- **MTP** transports machine messages.
- **BUS** moves them through the runtime.

This v0.1 slice does not choose a production bus, provider, device SDK, email gateway, router, storage destination, or execution engine.

## Principle

**One brain, many doors.** Text, voice, email, sharing, messaging, browser, API, and sensors may all produce the same Universal Input Event envelope. Channel-specific adapters remain outside the semantic core.

## Runtime v0.1

`04_Execution/universal_input/event.py` provides one deterministic constructor:

```python
make_input_event(...)
```

It creates a provider-neutral event envelope. Y-COM can consume the normalized `channel.type` and `object.body` without knowing the originating device or transport.

Raw telemetry is not automatically Y-COM. A sensor event with no interaction surface remains outside Y-COM until cognition/interpreters turn it into an interaction-relevant act.
