# OBSIDIAN-SOURCE-SURFACE-REGISTRY

**Gate:** OBSIDIAN-FINAL-SOURCE-SURFACE-MAP-GATE  
**Version:** v1.0  
**Date:** 2026-07-04  
**Mode:** Metadata-only — no content accessed, no source mutation  

---

## Registry

| ID | Surface Name | Storage | MD Count | Status | Pipeline | Guardian Auth | Next Gate |
|---|---|---|---:|---|---|---|---|
| OBS-LOCAL-01 | LUDIVINE | Local Mac | 1842 | `DISCOVERED_NOT_AUTHORIZED_PENDING_SCOPE_DECISION` | OBS_PIPELINE_PENDING | REQUIRED | OBSIDIAN-DRY-RUN-GATE (after auth) |
| OBS-LOCAL-02 | LUDIVINE BACKUP | Local Mac | 1418 | `BACKUP_EXCLUDE_BY_DEFAULT` | EXCLUDED | NOT REQUIRED | None |
| OBS-LOCAL-03 | Local Test Vault | Local Mac | 5 | `EXCLUDE_BY_DEFAULT` | EXCLUDED | NOT REQUIRED | None |
| OBS-ICLOUD-01 | Y-World iCloud | iCloud | 17 | `SMALL_EXPERIMENTAL_LOCAL_VAULT` | OBS_PIPELINE_LOW_PRIORITY | NOT REQUIRED | Future low-priority gate |
| OBS-ICLOUD-02 | Test iCloud | iCloud | 8 | `EXCLUDE_BY_DEFAULT` | EXCLUDED | NOT REQUIRED | None |
| OBS-GDRIVE-01 | GDrive Obsidian Vault | GDrive | UNKNOWN | `DISCOVERED_NOT_AUTHORIZED` | EXCLUDED_PENDING_BACKUP_REVIEW | REQUIRED | GDRIVE-OBSIDIAN-BACKUP-REVIEW-GATE (future) |
| OBS-GDRIVE-02 | GDrive Obsidian Vault 2 | GDrive | UNKNOWN | `DISCOVERED_NOT_AUTHORIZED` | EXCLUDED_PENDING_BACKUP_REVIEW | REQUIRED | GDRIVE-OBSIDIAN-BACKUP-REVIEW-GATE (future) |
| OBS-GDRIVE-03 | GDrive .obsidian Y-WORLD | GDrive | UNKNOWN | `DISCOVERED_LOW_PRIORITY` | OBS_PIPELINE_LOW_PRIORITY | NOT REQUIRED | Future low-priority gate |
| GDRIVE-YOS-01 | GDrive Y-OS Folders | GDrive | UNKNOWN | `GDRIVE_PIPELINE_NOT_OBSIDIAN_PIPELINE` | GDRIVE_YOS_PIPELINE | REQUIRED | GDRIVE-YOS-METADATA-COMPARISON-GATE |
| GITHUB-YWORLD-01 | Y-World GitHub | GitHub | 61 | `HANDLE_UNDER_GITHUB_PIPELINE` | GITHUB_PIPELINE | NOT REQUIRED | GITHUB-SOURCE-METADATA-PILOT-GATE |

---

## Active Blockers

| Blocker | Description | Resolution |
|---|---|---|
| `LUDIVINE_SCOPE_DECISION_PENDING` | LUDIVINE not authorized for content access | Guardian explicit authorization required |
| `YOS_GDRIVE_FRAGMENTATION_REQUIRES_METADATA_COMPARISON` | 4 GDrive Y-OS folders — canonical not decided | GDRIVE-YOS-METADATA-COMPARISON-GATE |
| `GDRIVE_OBSIDIAN_VAULT_ROLE_UNKNOWN` | GDrive Obsidian Vault 1 & 2 — backup vs active unknown | GDRIVE-OBSIDIAN-BACKUP-REVIEW-GATE (future) |

---

## Total Surface Count

| Category | Count | Total MD Files |
|---|---|---|
| Local Mac | 3 | 3265 |
| iCloud | 2 | 25 |
| Google Drive (Obsidian candidates) | 3 | UNKNOWN |
| Google Drive (Y-OS, non-Obsidian) | 4 | UNKNOWN |
| GitHub | 1 | 61 |
| **TOTAL** | **13** | **3351+** |
