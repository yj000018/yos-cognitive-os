# Obsidian Source Surface Map

**Gate:** OBSIDIAN-FINAL-SOURCE-SURFACE-MAP-GATE  
**Version:** v1.0  
**Date:** 2026-07-04  
**Mode:** Metadata-only — no content read, no source mutation  

---

## Source Surface Map

| Surface ID | Surface Name | Storage | Approx MD Count | Role | Status | Pipeline | Authorization |
|---|---|---|---:|---|---|---|---|
| OBS-LOCAL-01 | LUDIVINE | Local Mac | 1842 | Primary local vault | `DISCOVERED_NOT_AUTHORIZED_PENDING_SCOPE_DECISION` | OBS_PIPELINE_PENDING | GUARDIAN REQUIRED |
| OBS-LOCAL-02 | LUDIVINE BACKUP | Local Mac | 1418 | Backup copy | `BACKUP_EXCLUDE_BY_DEFAULT` | EXCLUDED | NOT AUTHORIZED |
| OBS-LOCAL-03 | Local Test Vault | Local Mac | 5 | Test vault | `EXCLUDE_BY_DEFAULT` | EXCLUDED | NOT AUTHORIZED |
| OBS-ICLOUD-01 | Y-World iCloud | iCloud | 17 | Small experimental vault | `SMALL_EXPERIMENTAL_LOCAL_VAULT` | OBS_PIPELINE_LOW_PRIORITY | METADATA ONLY |
| OBS-ICLOUD-02 | Test iCloud | iCloud | 8 | Test vault | `EXCLUDE_BY_DEFAULT` | EXCLUDED | NOT AUTHORIZED |
| OBS-GDRIVE-01 | GDrive Obsidian Vault | Google Drive | UNKNOWN | Possible LUDIVINE backup | `DISCOVERED_NOT_AUTHORIZED` | EXCLUDED_PENDING_BACKUP_REVIEW | NOT AUTHORIZED |
| OBS-GDRIVE-02 | GDrive Obsidian Vault 2 | Google Drive | UNKNOWN | Possible LUDIVINE backup | `DISCOVERED_NOT_AUTHORIZED` | EXCLUDED_PENDING_BACKUP_REVIEW | NOT AUTHORIZED |
| OBS-GDRIVE-03 | GDrive .obsidian Y-WORLD | Google Drive | UNKNOWN | Obsidian config folder | `DISCOVERED_LOW_PRIORITY` | OBS_PIPELINE_LOW_PRIORITY | METADATA ONLY |
| GDRIVE-YOS-01 | GDrive Y-OS Folders | Google Drive | UNKNOWN | Fragmented Y-OS folders | `GDRIVE_PIPELINE_NOT_OBSIDIAN_PIPELINE` | GDRIVE_YOS_PIPELINE | METADATA ONLY |
| GITHUB-YWORLD-01 | Y-World GitHub | GitHub | 61 | Current likely primary Y-World | `HANDLE_UNDER_GITHUB_PIPELINE` | GITHUB_PIPELINE | METADATA ONLY |

---

## Notes

**LUDIVINE** is the largest known surface (1842 md files) but remains `DISCOVERED_NOT_AUTHORIZED_PENDING_SCOPE_DECISION`. Guardian must explicitly authorize before any content access, frontmatter parsing, or dry-run.

**GDrive Y-OS Folders** are classified as `GDRIVE_PIPELINE_NOT_OBSIDIAN_PIPELINE` — they are not confirmed Obsidian vaults. No `.obsidian` folder evidence found in `01_Y_OS_CORE`, `Y-OS`, `yOS`, or `YOS Vision`. Fragmentation blocker `YOS_GDRIVE_FRAGMENTATION_REQUIRES_METADATA_COMPARISON` preserved.

**Y-World GitHub** is the current likely primary Y-World source but must be validated by the GitHub-specific gate. It is not to be merged with the iCloud Y-World vault.
