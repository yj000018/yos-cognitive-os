# Obsidian / Markdown Final Source-Surface Map

**Last Updated:** 2026-07-04 (Overnight Batch — Registry Correction Patch v3)
**Correction:** GDrive Y-WORLD count corrected to 61 MD (not 235 or >100). GitHub Y-WORLD = 234 MD = canonical candidate.

## 1. Final OBS / MD Source-Surface Map

| Surface ID | Alias | Storage | Type | Known MD Count | Known Folder Count | `.obsidian` | `.git` | Class | Status | Pipeline | Authorization |
| ---------- | ----- | ------- | ---- | -------------: | -----------------: | ----------: | -----: | ----- | ------ | -------- | ------------- |
| ICLOUD-YWORLD | iCloud Y-World | iCloud | Obsidian vault | 17 | N/A | YES | NO | `fragment_comparison_source` | `KEEP_FOR_FUTURE_COMPARISON` | `HANDLE_UNDER_ICLOUD_PIPELINE` | `METADATA_AND_LIMITED_PROBE_ONLY` |
| ICLOUD-TEST | iCloud Test | iCloud | Test vault | Unknown | N/A | YES | NO | `test_excluded` | `TEST_EXCLUDED_FINAL` | `EXCLUDED` | `METADATA_ONLY` |
| GDRIVE-OBS-001 | Obsidian Vault | GDrive | Config skeleton | 1 | 5 | YES | NO | `configuration_only_excluded` | `CONFIGURATION_ONLY_EXCLUDE` | `EXCLUDED` | `METADATA_AND_LIMITED_PROBE_ONLY` |
| GDRIVE-OBS-002 | Obsidian Vault 2 | GDrive | Empty folder | 0 | 0 | NO | NO | `out_of_scope_excluded` | `OUT_OF_SCOPE_EXCLUDE` | `EXCLUDED` | `METADATA_AND_LIMITED_PROBE_ONLY` |
| GDRIVE-OBS-003 | Y-WORLD (GDrive — BACKUP) | GDrive | Obsidian vault | 61 | 17 | YES | NO | `backup_excluded` | `BACKUP_EXCLUDED_FINAL` | `EXCLUDED` | `CLOSED` |
| GITHUB-YWORLD | Y-WORLD (GitHub) | GitHub | Git repository | 234 | 21 | YES | YES | `canonical_candidate` | `CANONICAL_CANDIDATE_CONFIRMED` | `GITHUB_PIPELINE` | `AUTHORIZED` |
| LOCAL-OBS-001 | LUDIVINE principal | Local | Obsidian vault | 1842 | N/A | YES | NO | `large_vault_candidate` | `DISCOVERED_NOT_AUTHORIZED_PENDING_SCOPE_DECISION` | `PENDING_SCOPE` | `METADATA_ONLY` |
| LOCAL-OBS-002 | LUDIVINE BACKUP | Local | Backup vault | 1418 | N/A | YES | NO | `backup_excluded` | `BACKUP_EXCLUDED_FINAL` | `EXCLUDED` | `METADATA_ONLY` |
| LOCAL-OBS-003 | testing | Local | Test vault | 5 | N/A | YES | NO | `test_excluded` | `TEST_EXCLUDED_FINAL` | `EXCLUDED` | `METADATA_ONLY` |
| LOCAL-GIT-YW | Y-WORLD (Local Git — BACKUP) | Local | Git working copy | 61 | N/A | YES | YES | `backup_excluded` | `BACKUP_EXCLUDED_FINAL` | `EXCLUDED` | `CLOSED` |
| LOCAL-YWORLD | Y-WORLD (Local) | Local | Unconfirmed | Unknown | N/A | Unknown | Unknown | `local_unconfirmed` | `LOCAL_YWORLD_UNPROBED_SCOPE_UNCONFIRMED` | `PENDING_SCOPE` | `UNAUTHORIZED` |
