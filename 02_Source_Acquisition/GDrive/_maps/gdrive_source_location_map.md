---
gate: OBSIDIAN-SOURCE-CENSUS-GDRIVE-ICLOUD-PATCH
stream: OBSIDIAN
version: v1.0
date: 2026-07-03
---

# Google Drive Source Location Map

## Instance Registry

| Instance ID | Description | Status |
|---|---|---|
| INST-GDRIVE-YOS | Google Drive Y-OS content (Y-OS + yOS + YOS Vision + 01_Y_OS_CORE) | `CANDIDATE_REQUIRES_SCOPE_DECISION` |
| INST-GDRIVE-BACKUP | Google Drive backups (05_ARCHIVES_BACKUPS + Backup Google Drive) | `BACKUP_EXCLUDE_BY_DEFAULT` |
| INST-GDRIVE-OBS | Google Drive Obsidian vault backups (Obsidian Vault + Obsidian Vault 2) | `DISCOVERED_NOT_AUTHORIZED` |

## Source Object Map

```
Google Drive Root (yannick.jolliet@gmail.com)
├── 01_Y_OS_CORE/          → INST-GDRIVE-YOS  [CANDIDATE]
├── Y-OS/                  → INST-GDRIVE-YOS  [CANDIDATE]
├── yOS/                   → INST-GDRIVE-YOS  [CANDIDATE — possible Y-OS duplicate]
├── YOS Vision/            → INST-GDRIVE-YOS  [CANDIDATE]
├── (APPS FOLDERS)/
│   ├── Obsidian Vault/    → INST-GDRIVE-OBS  [NOT_AUTHORIZED]
│   │   └── .obsidian/     → vault config
│   └── Obsidian Vault 2/  → INST-GDRIVE-OBS  [NOT_AUTHORIZED]
├── Y-WORLD/
│   └── .obsidian/         → Y-World vault config [LOW_PRIORITY — GitHub pipeline]
├── 05_ARCHIVES_BACKUPS/   → INST-GDRIVE-BACKUP [EXCLUDED]
└── Backup Google Drive/   → INST-GDRIVE-BACKUP [EXCLUDED]
```

## Fragmentation Alert

Three Y-OS folders exist at Google Drive root:
- `Y-OS` (Jun 15)
- `yOS` (May 17)
- `YOS Vision` (Jun 20)
- `01_Y_OS_CORE` (May 4)

**Guardian must resolve which is canonical before any GDrive acquisition.**

## Privacy

No file paths contain private user identifiers. Google Drive folder names are metadata.
Account alias: `GDRIVE://yannick.jolliet@gmail.com/`
