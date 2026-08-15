# InteractionAct Contract v0.1

`InteractionAct` is the minimal canonical semantic object of Y-COM.

It represents human-AI interaction meaning, independent of the physical channel used to express it.

InteractionAct is a human-AI semantic object.
It is not an MTP envelope, BUS packet, execution authorization, project-routing object, or sensor telemetry object.

V0.1 canonical acts are exactly:

- `ACCEPT`
- `REJECT`
- `CONTINUE`
- `CHOOSE`
- `REQUEST_CHOICE`
- `RECOMMEND`

Surface forms such as `O`, `Oui`, and `OK` are not canonical semantics. They must be resolved by explicit interaction context.
