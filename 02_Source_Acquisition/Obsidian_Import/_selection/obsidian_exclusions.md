# Obsidian Exclusions

**Gate:** OBSIDIAN-SOURCE-CENSUS-GATE  
**Version:** v1.0  
**Date:** 2026-07-03

---

## Excluded Sources

| Source ID | Display Name | Reason | Status | Future Review |
|---|---|---|---|---|
| OBS-SRC-002 | LUDIVINE BACKUP | Backup duplicate of primary vault | `BACKUP_EXCLUDE_BY_DEFAULT` | Only if primary vault is lost |
| OBS-SRC-004 | Test (iCloud) | Test vault, minimal content (~8 md) | `EXCLUDED_BY_DEFAULT` | No |
| OBS-SRC-005 | testing (local) | Test vault, minimal content (~5 md) | `EXCLUDED_BY_DEFAULT` | No |

---

## Exclusion Rules Applied

1. **Backup vaults** — excluded by default unless primary is lost or explicitly authorized.
2. **Test vaults** — excluded by default. No KAP-relevant content expected.
3. **Y-World iCloud** — not excluded, but marked low priority. Canonical Y-World is GitHub.
4. **Google Drive** — not excluded, but census not run. Requires separate gate.

---

## Not Excluded (Pending Decision)

- OBS-SRC-001 LUDIVINE — `DISCOVERED_NOT_AUTHORIZED` — pending Guardian scope decision
- OBS-SRC-003 Y-World iCloud — `DISCOVERED_LOW_PRIORITY` — pending Guardian scope decision
