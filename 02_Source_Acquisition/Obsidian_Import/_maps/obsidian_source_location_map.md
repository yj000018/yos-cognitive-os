# Obsidian Source Location Map

**Gate:** OBSIDIAN-SOURCE-CENSUS-GATE  
**Version:** v1.0  
**Date:** 2026-07-03

> All local paths aliased. No private paths stored.

---

## Location Tree

```
OBSIDIAN / MARKDOWN SOURCES
│
├── LOCAL MAC
│   ├── OBS-SRC-001 — LUDIVINE (1842 md) ← PRIMARY CANDIDATE [NOT AUTHORIZED]
│   ├── OBS-SRC-002 — LUDIVINE BACKUP (1418 md) ← BACKUP [EXCLUDED]
│   └── OBS-SRC-005 — testing (5 md) ← TEST [EXCLUDED]
│
├── APPLE iCLOUD
│   ├── OBS-SRC-003 — Y-World iCloud (17 md) ← SMALL EXPERIMENTAL [LOW PRIORITY]
│   └── OBS-SRC-004 — Test (8 md) ← TEST [EXCLUDED]
│
├── GITHUB
│   └── OBS-SRC-006 — Y-World GitHub (61 md) ← CANONICAL Y-WORLD [GITHUB PIPELINE]
│
├── GOOGLE DRIVE
│   └── OBS-SRC-007 — Unknown (not scanned) ← ACCESS NOT CONFIRMED
│
└── EXTERNAL / ARCHIVE
    └── (none detected in current session)
```

---

## Source Count Summary

| Location Class | Sources | Total MD Files | Authorized |
|---|---|---|---|
| local_mac | 3 | ~2847 | 0 |
| apple_icloud | 2 | 25 | 0 |
| github | 1 | 61 | via GitHub pipeline |
| google_drive | 1 | unknown | not confirmed |
| external/archive | 0 | 0 | N/A |
| **TOTAL** | **7** | **~2933+** | **0 (Obsidian pipeline)** |

---

## Key Decision Points for Guardian

1. **LUDIVINE authorization** — 1842 md files, primary candidate. Requires explicit scope decision before any deeper scan.
2. **Y-World iCloud vs GitHub** — iCloud has 17 files, GitHub has 61. GitHub is canonical. iCloud may be a staging/sync artifact.
3. **Google Drive** — census not run. May contain Obsidian exports or Markdown archives. Requires separate gate.
