# Local Obsidian Source Surface Detection

**Date:** 2026-07-04
**Gate:** LOCAL-OBSIDIAN-SOURCE-SURFACE-DETECTION-GATE
**Author:** Manus AI

## Table 8.1 — Local OBS Source Surface Map

| Surface ID | Alias | Type | `.obsidian` Present | `.git` Present | Approx MD Count | Top-Level Folder Count | Candidate Class | Status | Authorization |
| ---------- | ----- | ---- | ------------------: | -------------: | --------------: | ---------------------: | --------------- | ------ | ------------- |
| **LOCAL-OBS-001** | `LOCAL://LUDI/LUDIVINE_VAULT` | Obsidian Vault | YES | UNKNOWN | 1842 | 6 | `large_vault_candidate` | `DISCOVERED_NOT_AUTHORIZED_PENDING_SCOPE_DECISION` | Metadata only |
| **LOCAL-OBS-002** | `LOCAL://LUDI/LUDIVINE_BACKUP` | Obsidian Vault | YES | UNKNOWN | 1418 | UNKNOWN | `backup_candidate` | `BACKUP_EXCLUDED_FINAL` | Metadata only |
| **LOCAL-OBS-003** | `LOCAL://TESTS/testing` | Obsidian Vault | YES | UNKNOWN | 5 | UNKNOWN | `test_candidate` | `TEST_EXCLUDED_FINAL` | Metadata only |
| **LOCAL-YWORLD** | `LOCAL://YWORLD_UNPROBED` | Unknown | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | `unknown_requires_review` | `LOCAL_YWORLD_UNPROBED_SCOPE_UNCONFIRMED` | Metadata only |
| **LOCAL-GIT-YW** | `GITHUB://yj000018/Y-WORLD` | Git Clone | YES | YES | 61 | UNKNOWN | `git_clone_candidate` | `HANDLE_UNDER_GITHUB_PIPELINE` | Metadata only |

## Table 8.2 — Local Y-World Check

| Check | Result | Evidence Level | Notes |
| ----- | ------ | -------------- | ----- |
| local Y-World folder found? | UNCONFIRMED | `INSUFFICIENT` | No direct path discovered beyond the iCloud fragment and the Git clone. |
| local Y-WORLD folder found? | UNCONFIRMED | `INSUFFICIENT` | Same as above. Broad scan forbidden. |
| local Git clone found? | YES | `METADATA_ONLY` | Previous discovery recorded `GITHUB://yj000018/Y-WORLD` as a local git working copy with 61 MD files. |
| local Obsidian vault found? | YES | `METADATA_ONLY` | The local Git clone has `.obsidian` present. |
| local sync mirror found? | YES | `METADATA_ONLY` | Likely syncing to GitHub and GDrive. |

## Table 8.3 — Exclusion Table

| Surface | Decision | Reason | Future Gate Required |
| ------- | -------- | ------ | -------------------- |
| **LOCAL-OBS-002** (`LUDIVINE_BACKUP`) | `BACKUP_EXCLUDED_FINAL` | Older snapshot of LUDIVINE vault. 424 fewer md files. | None |
| **LOCAL-OBS-003** (`testing`) | `TEST_EXCLUDED_FINAL` | Test vault. Minimal content (5 files). | None |
| **ICLOUD-TEST** (`Test`) | `TEST_EXCLUDED_FINAL` | Test vault. Minimal md content (8 files). | None |

## Table 8.4 — Authorization Matrix

| Surface | Metadata Discovery | Content Read | File Copy | Extraction | Dry-Run | Merge | Source Mutation |
| ------- | -----------------: | -----------: | --------: | ---------: | ------: | ----: | --------------: |
| **LOCAL-OBS-001** | YES | NO | NO | NO | NO | NO | NO |
| **LOCAL-OBS-002** | YES | NO | NO | NO | NO | NO | NO |
| **LOCAL-OBS-003** | YES | NO | NO | NO | NO | NO | NO |
| **LOCAL-YWORLD** | YES | NO | NO | NO | NO | NO | NO |
| **LOCAL-GIT-YW** | YES | NO | NO | NO | NO | NO | NO |
