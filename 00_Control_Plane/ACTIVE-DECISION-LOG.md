# Active Decision Log

> Y-OS Control Plane — Decisions requiring action or tracking
> Last updated: 2026-07-03

| Decision ID | Decision | Status | Date | Rationale | Next Action |
|---|---|---|---|---|---|
| DEC-YOS-001 | Y-OS is master container; KAP is module/process | CONFIRMED | 2026-07-03 | Prevents confusion between engine and system | Enforce in all new docs |
| DEC-YOS-002 | New doctrine must be persisted to Git at creation time | CONFIRMED | 2026-07-03 | ChatGPT history is ephemeral | Enforce via SESSION-CAPTURE-INBOX |
| DEC-YOS-003 | Use Control Plane for active doctrine | CONFIRMED | 2026-07-03 | Separates canonical from staging | All new doctrine → 00_Control_Plane/ |
| DEC-YOS-004 | Use Source Staging for recovered sources | CONFIRMED | 2026-07-03 | Staging ≠ canonical truth | All imports → 06_Source_Staging/ |
| DEC-YOS-005 | Master repo (yos-cognitive-os) + linked/submodule repos | CONFIRMED | 2026-07-03 | Balances monorepo simplicity with modularity | Create REPO-REGISTRY + repo_index.json |
| DEC-YOS-006 | REPO-REGISTRY and repo_index.json are mandatory | CONFIRMED | 2026-07-03 | Agent navigation requires machine-readable index | Created in 05_Registries/ and 07_AI_Indexes/ |
| DEC-YOS-007 | Capture current and parallel KAP session doctrines | IN_PROGRESS | 2026-07-03 | Doctrines must not remain in ChatGPT only | Complete SESSION-CAPTURE-INBOX |
| DEC-YOS-008 | KAP scope: yOS knowledge consolidation (Phase 1) | CONFIRMED | 2026-07-03 | Prevents scope creep | YOUniverse sources catalogued, connectors deferred |
| DEC-YOS-009 | YOUniverse = Phase 2 (same engine, broader scope) | CONFIRMED | 2026-07-03 | One engine, multiple scopes | Catalogue YOUniverse sources now, activate later |
| DEC-YOS-010 | LLM Internal Memory extraction deferred until taxonomy complete | CONFIRMED | 2026-07-03 | Batch extraction more efficient after full taxonomy | Trigger after THOUGHT-LINE-SEEDING-GATE |
| DEC-YOS-011 | Mem0 acquisition confirmed complete | CONFIRMED | 2026-07-03 | All entries captured in previous sessions | Verify delta at THOUGHT-LINE-SEEDING-GATE |
| DEC-YOS-012 | ZIP files are transport/snapshot only, never primary corpus | CONFIRMED | 2026-07-03 | Git/Markdown-first is mandatory | Enforce in all pipeline gates |
