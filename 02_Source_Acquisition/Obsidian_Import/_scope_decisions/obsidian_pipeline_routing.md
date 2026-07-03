---
gate: OBSIDIAN-SCOPE-DECISION-GATE
stream: OBSIDIAN
version: v1.0
date: 2026-07-03
---

# Obsidian Pipeline Routing

## Pipeline Assignment

| Surface | Pipeline | Status |
|---|---|---|
| LOCAL-OBS-001 LUDIVINE | OBSIDIAN-LOCAL-PIPELINE | PENDING_AUTHORIZATION |
| LOCAL-OBS-002 LUDIVINE BACKUP | EXCLUDED | BACKUP_EXCLUDE_BY_DEFAULT |
| ICLOUD-OBS-001 Y-World iCloud | GITHUB-PIPELINE | LOW_PRIORITY |
| ICLOUD-OBS-002 Test | EXCLUDED | EXCLUDED_BY_DEFAULT |
| LOCAL-OBS-003 testing | EXCLUDED | EXCLUDED_BY_DEFAULT |
| GDRIVE-OBS-001 Obsidian Vault | GDRIVE-PIPELINE (if authorized) | NOT_AUTHORIZED |
| GDRIVE-OBS-002 Obsidian Vault 2 | GDRIVE-PIPELINE (if authorized) | NOT_AUTHORIZED |
| GDRIVE-OBS-003 .obsidian Y-WORLD | GITHUB-PIPELINE | LOW_PRIORITY |
| GITHUB-OBS-001 Y-World GitHub | GITHUB-PIPELINE | ACTIVE |

## Gate Sequence (if LUDIVINE authorized)

```
OBSIDIAN-SCOPE-DECISION-GATE (current)
    ↓ (Guardian authorizes LUDIVINE)
OBSIDIAN-DRY-RUN-EXECUTION-GATE
    ↓
OBSIDIAN-METADATA-SCAN-GATE
    ↓
OBSIDIAN-CONTENT-PILOT-GATE (limited)
```

## Gate Sequence (if LUDIVINE NOT authorized)

```
OBSIDIAN-SCOPE-DECISION-GATE (current)
    ↓
PAUSE — no Obsidian acquisition in this phase
    ↓
Revisit after Notion + GitHub pipelines complete
```

## Cross-Pipeline Dependencies

| Dependency | Status |
|---|---|
| Y-World GitHub → GitHub pipeline | Active — GITHUB-SOURCE-METADATA-PILOT-GATE |
| GDrive Y-OS fragmentation → GDrive gate | Blocked — YOS_GDRIVE_FRAGMENTATION |
| LUDIVINE → Obsidian pipeline | Blocked — NOT_AUTHORIZED |
