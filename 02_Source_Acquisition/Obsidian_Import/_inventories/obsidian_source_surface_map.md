# Obsidian Source Surface Map

**Gate:** LOCAL-OBSIDIAN-SOURCE-SURFACE-DETECTION-GATE  
**Version:** v2.0  
**Date:** 2026-07-04  
**Mode:** Metadata-only — no content read, no source mutation  

---

## Source Surface Map

| Surface ID | Surface Name | Storage | Approx MD Count | Role | Status | Pipeline | Authorization |
|---|---|---|---:|---|---|---|---|
| **LOCAL-OBS-001** | LUDIVINE | Local Mac | 1842 | Primary local vault | `DISCOVERED_NOT_AUTHORIZED_PENDING_SCOPE_DECISION` | LOCAL_PIPELINE | GUARDIAN REQUIRED |
| **LOCAL-OBS-002** | LUDIVINE BACKUP | Local Mac | 1418 | Backup copy | `BACKUP_EXCLUDED_FINAL` | EXCLUDED | NOT AUTHORIZED |
| **LOCAL-OBS-003** | testing | Local Mac | 5 | Test vault | `TEST_EXCLUDED_FINAL` | EXCLUDED | NOT AUTHORIZED |
| **ICLOUD-TEST** | Test | iCloud | 8 | Test vault | `TEST_EXCLUDED_FINAL` | EXCLUDED | NOT AUTHORIZED |
| **ICLOUD-YWORLD** | Y-World | iCloud | 17 | Small fragment | `KEEP_FOR_FUTURE_COMPARISON` | ICLOUD_PIPELINE | METADATA ONLY |
| **GDRIVE-OBS-001** | Obsidian Vault | Google Drive | 1 | Skeleton | `CONFIGURATION_ONLY_EXCLUDE` | EXCLUDED | NOT AUTHORIZED |
| **GDRIVE-OBS-002** | Obsidian Vault 2 | Google Drive | 0 | Empty | `OUT_OF_SCOPE_EXCLUDE` | EXCLUDED | NOT AUTHORIZED |
| **GDRIVE-OBS-003** | Y-WORLD | Google Drive | 235 | Active Sync Mirror | `HIGH_VALUE_HOLD_FOR_SCOPE_DECISION` | GDRIVE_PIPELINE | METADATA ONLY |
| **LOCAL-YWORLD** | YWORLD_UNPROBED | Local Mac | Unknown | Unknown | `LOCAL_YWORLD_UNPROBED_SCOPE_UNCONFIRMED` | LOCAL_PIPELINE | METADATA ONLY |
| **LOCAL-GIT-YW** | Y-WORLD Git Clone | Local Mac | 61 | Local Git working copy | `HANDLE_UNDER_GITHUB_PIPELINE` | GITHUB_PIPELINE | METADATA ONLY |
| **GITHUB-YWORLD** | Y-WORLD GitHub | GitHub | 234 | Active Canonical Candidate | `REQUIRES_BOUNDED_COMPARISON` | GITHUB_PIPELINE | METADATA ONLY |
