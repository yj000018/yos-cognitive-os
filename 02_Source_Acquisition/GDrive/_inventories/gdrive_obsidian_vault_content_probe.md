# GDrive Obsidian Vault Content Probe Inventory

> Gate: GDRIVE-OBSIDIAN-VAULT-CONTENT-SCOPE-PROBE-GATE
> Mode: bounded_content_scope_probe
> Date: 2026-07-03

## 1. GDrive Vault Scope Table

| Surface ID | Name | MD Count | Folder Count | `.obsidian` Present | Sample Read Count | Content Profile | Scope Decision | Recommendation |
| ---------- | ---- | -------: | -----------: | ------------------- | ----------------: | --------------- | -------------- | -------------- |
| GDRIVE-OBS-001 | Obsidian Vault | 1 | 5 | Yes | 0 | OBSIDIAN_CONFIG_ONLY | CONFIGURATION_ONLY_EXCLUDE | Exclude |
| GDRIVE-OBS-002 | Obsidian Vault 2 | 0 | 0 | No | 0 | TEST_OR_EMPTY | OUT_OF_SCOPE_EXCLUDE | Exclude |
| GDRIVE-OBS-003 | Y-WORLD | >100 | 18 | Yes | 1 | YWORLD_RELATED, YOS_RELATED | HIGH_VALUE_HOLD_FOR_SCOPE_DECISION | Hold for Guardian review |

## 2. Sampled Files Table

| Surface ID | Filename | Reason Sampled | Topic Hint | Sensitive Flag | Value Signal | Recommended Action |
| ---------- | -------- | -------------- | ---------- | -------------- | ------------ | ------------------ |
| GDRIVE-OBS-003 | Y-WORLD Architecture.md | Core architectural document | Y-WORLD subsystems map | False | HIGH | Ingest in future pilot |

## 3. Exclusion / Hold Table

| Surface | Decision | Reason | Future Gate Required |
| ------- | -------- | ------ | -------------------- |
| LUDIVINE BACKUP | LUDIVINE_BACKUP_EXCLUDED_FINAL | Backup duplicate candidate | None |
| iCloud Test | ICLOUD_TEST_EXCLUDED_FINAL | Test vault | None |
| iCloud Y-World | ICLOUD_YWORLD_CONFIRMED_17_MD_MICRO_EXTRACTION_CLOSEOUT_AUTHORIZED_SEPARATELY | Confirmed 17 MD files | ICLOUD-YWORLD-MICRO-EXTRACTION-CLOSEOUT-GATE |
| GDRIVE-OBS-001 | CONFIGURATION_ONLY_EXCLUDE | Plugin config skeleton | None |
| GDRIVE-OBS-002 | OUT_OF_SCOPE_EXCLUDE | Empty folder | None |
| GDRIVE-OBS-003 | HIGH_VALUE_HOLD_FOR_SCOPE_DECISION | Primary live Y-WORLD vault | OBSIDIAN-SCOPE-DECISION-GATE |

## 4. Authorization Matrix

| Surface | Metadata Discovery | Limited Content Probe | Full Extraction | Import | Merge | Synthesis | Source Mutation |
| ------- | -----------------: | --------------------: | --------------: | -----: | ----: | --------: | --------------: |
| GDRIVE-OBS-001 | YES | YES | NO | NO | NO | NO | NO |
| GDRIVE-OBS-002 | YES | YES | NO | NO | NO | NO | NO |
| GDRIVE-OBS-003 | YES | YES | NO | NO | NO | NO | NO |
