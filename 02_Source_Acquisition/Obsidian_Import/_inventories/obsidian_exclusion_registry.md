# Obsidian Exclusion Registry

**Gate:** OBSIDIAN-FINAL-SOURCE-SURFACE-MAP-GATE  
**Version:** v1.0  
**Date:** 2026-07-04  

---

## Exclusion Registry

| Surface | Exclusion Status | Reason | Reversible? | Future Gate Required |
|---|---|---|---|---|
| LUDIVINE BACKUP | `BACKUP_EXCLUDE_BY_DEFAULT` | Backup duplicate of LUDIVINE — not a primary source | YES — if primary LUDIVINE is authorized and backup comparison needed | None required |
| Local Test Vault | `EXCLUDE_BY_DEFAULT` | Test vault — no production content | YES — if test content becomes relevant | None required |
| Test iCloud | `EXCLUDE_BY_DEFAULT` | Test vault in iCloud — no production content | YES | None required |
| GDrive Obsidian Vault | `DISCOVERED_NOT_AUTHORIZED` | Possible LUDIVINE backup on GDrive — not authorized | YES — if backup review gate authorized | GDRIVE-OBSIDIAN-BACKUP-REVIEW-GATE (future, optional) |
| GDrive Obsidian Vault 2 | `DISCOVERED_NOT_AUTHORIZED` | Possible second LUDIVINE backup on GDrive | YES — if backup review gate authorized | GDRIVE-OBSIDIAN-BACKUP-REVIEW-GATE (future, optional) |

---

## Surfaces Pending Authorization (not excluded, not authorized)

| Surface | Status | Required Authorization |
|---|---|---|
| LUDIVINE | `DISCOVERED_NOT_AUTHORIZED_PENDING_SCOPE_DECISION` | Guardian explicit authorization for content access |
