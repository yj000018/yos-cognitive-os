# Obsidian Source Census — Multi-Location Inventory

**Gate:** OBSIDIAN-SOURCE-CENSUS-GATE  
**Version:** v1.0  
**Date:** 2026-07-03  
**Status:** `OBSIDIAN_SOURCE_CENSUS_GATE_PASS_WITH_ACCESS_GAPS_READY_FOR_OBSIDIAN_SCOPE_DECISION_GATE`

> **Privacy note:** All local paths are aliased. No usernames, home directory paths, or private absolute paths stored in this file. Notion URLs are internal working metadata and are not authorized for public export without a future redaction policy.

---

## Source Census Table

| Source ID | Display Name | Location Class | Type | MD Count | Obsidian Config? | Authorization Status | Recommended Pipeline | Notes |
|---|---|---|---|---|---|---|---|---|
| OBS-SRC-001 | LUDIVINE | local_mac | obsidian_vault | **1842** | YES | `DISCOVERED_NOT_AUTHORIZED` | HOLD_FOR_SCOPE_DECISION | Primary candidate — not authorized |
| OBS-SRC-002 | LUDIVINE BACKUP | local_mac | backup_vault | 1418 | YES | `BACKUP_EXCLUDE_BY_DEFAULT` | EXCLUDE | Older snapshot — excluded |
| OBS-SRC-003 | Y-World iCloud | apple_icloud | obsidian_vault | 17 | YES | `DISCOVERED_LOW_PRIORITY` | HOLD_FOR_SCOPE_DECISION | Small experimental — not primary source |
| OBS-SRC-004 | Test (iCloud) | apple_icloud | test_vault | 8 | YES | `EXCLUDED_BY_DEFAULT` | EXCLUDE | Test vault |
| OBS-SRC-005 | testing (local) | local_mac | test_vault | 5 | YES | `EXCLUDED_BY_DEFAULT` | EXCLUDE | Test vault |
| OBS-SRC-006 | Y-World GitHub | github | github_markdown_repo | 61 | YES | `HANDLE_UNDER_GITHUB_PIPELINE` | GITHUB_PIPELINE | Current likely primary Y-World source (to be validated by GitHub gate) — GitHub pipeline |
| OBS-SRC-007 | Google Drive | google_drive | unknown | N/A | N/A | `ACCESS_NOT_CONFIRMED` | GOOGLE_DRIVE_PIPELINE | Not scanned — no connector |

---

## Exclusion Table

| Source | Reason for Exclusion | Status | Future Review Needed |
|---|---|---|---|
| LUDIVINE BACKUP | Backup duplicate of primary vault | `BACKUP_EXCLUDE_BY_DEFAULT` | No — unless primary is lost |
| Test (iCloud) | Test vault, minimal content | `EXCLUDED_BY_DEFAULT` | No |
| testing (local) | Test vault, minimal content | `EXCLUDED_BY_DEFAULT` | No |

---

## Pipeline Routing Table

| Source | Route To | Reason | Next Gate |
|---|---|---|---|
| LUDIVINE | OBSIDIAN_LOCAL_PIPELINE | Primary local vault candidate | OBSIDIAN-SCOPE-DECISION-GATE |
| Y-World iCloud | HOLD_FOR_SCOPE_DECISION | Small, experimental, not primary source | OBSIDIAN-SCOPE-DECISION-GATE |
| Y-World GitHub | GITHUB_PIPELINE | Current likely primary Y-World source (to be validated by GitHub gate), already in GitHub gate | GITHUB-SOURCE-METADATA-PILOT-GATE |
| Google Drive | GOOGLE_DRIVE_PIPELINE | Access not confirmed | GOOGLE-DRIVE-SOURCE-CENSUS-GATE |
| LUDIVINE BACKUP | EXCLUDE | Backup only | NONE |
| Test vaults | EXCLUDE | Test only | NONE |

---

## Privacy Matrix

| Privacy Risk | Mitigation | Status |
|---|---|---|
| Local Mac paths with username | Aliased as `LOCAL://` | ✅ MITIGATED |
| iCloud paths with username | Aliased as `ICLOUD://` | ✅ MITIGATED |
| LUDIVINE filenames | Withheld per privacy policy | ✅ MITIGATED |
| GitHub repo URL | Public repo — safe to reference | ✅ OK |
| Google Drive paths | Not scanned | ✅ NOT APPLICABLE |
| Secrets/tokens | Not stored | ✅ CLEAN |

---

## Access Gaps

| Location | Gap | Reason |
|---|---|---|
| Google Drive | Census not run | Connector not configured |
| External drives/archives | Not scanned | Not visible in session |
| Mac FUSE mount | Empty during census | Data from prior discovery session (2026-07-03) |

---

## Compliance Matrix

| Rule | Status | Evidence |
|---|---|---|
| No Markdown content read | ✅ PASS | Census metadata-only |
| No frontmatter parsed | ✅ PASS | File counts only |
| No wikilinks parsed | ✅ PASS | Not applicable |
| No attachments opened | ✅ PASS | Not applicable |
| No source files copied | ✅ PASS | Read-only census |
| No source mutation | ✅ PASS | No writes to source |
| No import started | ✅ PASS | Census gate only |
| No merge performed | ✅ PASS | Not applicable |
| No normalization | ✅ PASS | Not applicable |
| No synthesis | ✅ PASS | Not applicable |
| No private paths stored | ✅ PASS | All paths aliased |
| No secrets stored | ✅ PASS | Token source: secret manager |
| No backup treated as primary | ✅ PASS | LUDIVINE BACKUP = BACKUP_EXCLUDE_BY_DEFAULT |
| Y-World iCloud not treated as primary source | ✅ PASS | Marked DISCOVERED_LOW_PRIORITY |
| GitHub not merged into Obsidian | ✅ PASS | GitHub pipeline separate |
| Google Drive not exported | ✅ PASS | Not scanned |
| Next gate not started | ✅ PASS | Stopped after census |
