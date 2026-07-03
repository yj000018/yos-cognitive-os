---
gate: OBSIDIAN-SCOPE-DECISION-GATE
stream: OBSIDIAN
version: v1.0
date: 2026-07-03
---

# Obsidian Scope Decision Matrix

## Summary

| Surface | MD Count | Decision | Next Gate |
|---|---|---|---|
| LOCAL-OBS-001 LUDIVINE | 1842 | `DISCOVERED_NOT_AUTHORIZED_PENDING_SCOPE_DECISION` | DRY-RUN if authorized |
| LOCAL-OBS-002 LUDIVINE BACKUP | 1418 | `BACKUP_EXCLUDE_BY_DEFAULT` | None |
| ICLOUD-OBS-001 Y-World iCloud | 17 | `DISCOVERED_LOW_PRIORITY` | GitHub pipeline |
| ICLOUD-OBS-002 Test | 8 | `EXCLUDED_BY_DEFAULT` | None |
| LOCAL-OBS-003 testing | 5 | `EXCLUDED_BY_DEFAULT` | None |
| GDRIVE-OBS-001 Obsidian Vault | unknown | `DISCOVERED_NOT_AUTHORIZED` | GDrive gate if authorized |
| GDRIVE-OBS-002 Obsidian Vault 2 | unknown | `DISCOVERED_NOT_AUTHORIZED` | GDrive gate if authorized |
| GDRIVE-OBS-003 .obsidian Y-WORLD | n/a | `DISCOVERED_LOW_PRIORITY` | GitHub pipeline |
| GITHUB-OBS-001 Y-World GitHub | 61 | `HANDLE_UNDER_GITHUB_PIPELINE` | GitHub gate |

## Guardian Actions Required

| Surface | Required Decision |
|---|---|
| LOCAL-OBS-001 LUDIVINE | Authorize or keep NOT_AUTHORIZED |
| GDRIVE-OBS-001 Obsidian Vault | Authorize probe, classify as backup, or exclude |
| GDRIVE-OBS-002 Obsidian Vault 2 | Same as above |
| GDrive Y-OS fragmentation | Declare canonical folder |

## Preserved Blocker

`YOS_GDRIVE_FRAGMENTATION_REQUIRES_SCOPE_DECISION`

Folders: `01_Y_OS_CORE`, `Y-OS`, `yOS`, `YOS Vision` — all at GDrive root. Deferred to GDrive acquisition gate.
