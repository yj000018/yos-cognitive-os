# Obsidian Local Vault Discovery Inventory

> Gate: OBSIDIAN-LOCAL-VAULT-DISCOVERY-GATE
> Date: 2026-07-03
> Machine: macOS (redacted)
> Scan method: `find -name .obsidian -type d` via Manus desktop bridge
> Content extracted: **NONE**
> Source mutated: **NONE**

---

## Summary

| Metric | Value |
|---|---|
| Total vaults discovered | 5 |
| Total MD files (all vaults) | ~3,290 |
| Unique MD files (excl. backup) | ~1,872 |
| Authorized for KAP | 0 (pending Guardian review) |
| Excluded by default | 3 (backup + 2 test) |
| Low priority | 1 (Y-World iCloud) |
| Pending authorization | 1 (LUDIVINE) |

---

## Vault Inventory (Redacted Paths)

### 1. LUDIVINE — Principal Local Vault Candidate

| Field | Value |
|---|---|
| Instance ID | INST-OBS-LUDIVINE |
| SO ID | SO-OBS-VAULT-0001 |
| Alias | `LOCAL://LUDI/LUDIVINE_VAULT` |
| Sync | Local only |
| MD files | **1842** |
| Status | `DISCOVERED_NOT_AUTHORIZED` |
| Canvases | Present |
| Media | Present |
| JSON indexes | Present (_index.json, _structure.json, _credo_analysis.json) |

**Top-level sections:** BUSINESS & ACTIONS, COSMOLOGIE, LUDIVINE, MULTIMEDIA, MULTIMEDIA & RESEARCH, RESEARCH

**Root metadata files (names only):** _ARCHITECTURE_SERIE.md, _AUDIT_COMPLET.md, _CREDO_MATRIX.md, _FORMES_MATRIX.md, _HISTOIRES_MATRIX.md, _MESSAGES_FONDAMENTAUX.md, _RAPPORT_COMPLET_2026.md, _README_VAULT.md, _YAML_SCHEMA.md, MIND MAP — Ludivine.md

**Note:** Structured creative/intellectual project vault. NOT a Y-OS system vault. Guardian must authorize before any content access.

---

### 2. LUDIVINE BACKUP — Backup Duplicate

| Field | Value |
|---|---|
| Instance ID | INST-OBS-LUDIVINE-BACKUP |
| SO ID | SO-OBS-VAULT-0002 |
| Alias | `LOCAL://LUDI/LUDIVINE_BACKUP` |
| Sync | Local only |
| MD files | 1418 |
| Status | `BACKUP_EXCLUDE_BY_DEFAULT` |

**Note:** Older snapshot. 424 fewer md files than primary. Excluded unless Guardian authorizes for diff analysis.

---

### 3. Y-World iCloud — Small Experimental Vault

| Field | Value |
|---|---|
| Instance ID | INST-OBS-YWORLD-ICLOUD |
| SO ID | SO-OBS-VAULT-0003 |
| Alias | `ICLOUD://obsidian/Y-World` |
| Sync | iCloud |
| MD files | 17 |
| Status | `DISCOVERED_LOW_PRIORITY` |

**Subdirs:** Projects, Tags, TaskNotes, Test, Yyy, Excalidraw

**Notable files:** yos_memory_blueprint.md (42KB), excalibrain.md, Tool Intelligence Layer.md

**Note:** Mostly empty/placeholder files. Real Y-World content is on GitHub (INST-GITHUB-YWORLD).

---

### 4. Test — Test Vault (iCloud)

| Field | Value |
|---|---|
| Instance ID | INST-OBS-TEST |
| SO ID | SO-OBS-VAULT-0004 |
| Alias | `ICLOUD://obsidian/Test` |
| Sync | iCloud |
| MD files | ~8 |
| Status | `EXCLUDE_BY_DEFAULT` |

---

### 5. testing — Test Vault (Local)

| Field | Value |
|---|---|
| Instance ID | INST-OBS-TESTING |
| SO ID | SO-OBS-VAULT-0005 |
| Alias | `LOCAL://TESTS/testing` |
| Sync | Local only |
| MD files | ~5 |
| Status | `EXCLUDE_BY_DEFAULT` |

---

## Excluded Non-Vaults

| Name | Alias | MD Files | Status | Note |
|---|---|---|---|---|
| Y-WORLD (GitHub clone) | `GITHUB://yj000018/Y-WORLD` | 61 | `HANDLE_UNDER_GITHUB_PIPELINE` | Local git clone. Source of truth = GitHub remote. Already registered as INST-GITHUB-YWORLD. |

---

## Classification Summary

| Vault | Role | Status |
|---|---|---|
| LUDIVINE | Principal local vault candidate | `DISCOVERED_NOT_AUTHORIZED` |
| LUDIVINE BACKUP | Backup duplicate candidate | `BACKUP_EXCLUDE_BY_DEFAULT` |
| Y-World iCloud | Small experimental vault | `DISCOVERED_LOW_PRIORITY` |
| Test | Test vault | `EXCLUDE_BY_DEFAULT` |
| testing | Test vault | `EXCLUDE_BY_DEFAULT` |
| Y-World GitHub | Real Y-World source | `HANDLE_UNDER_GITHUB_PIPELINE` |
