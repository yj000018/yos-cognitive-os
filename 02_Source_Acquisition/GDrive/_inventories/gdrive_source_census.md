---
gate: OBSIDIAN-SOURCE-CENSUS-GDRIVE-ICLOUD-PATCH
stream: OBSIDIAN
version: v1.0
date: 2026-07-03
account: yannick.jolliet@gmail.com
content_read: false
source_mutation: false
---

# Google Drive + iCloud Source Census

## Access

| Source | Method | Status |
|---|---|---|
| Google Drive | Browser authenticated | CONFIRMED |
| iCloud | Mac FUSE (prior scan) | CONFIRMED_PREVIOUSLY |
| iCloud (current) | Mac desktop session | UNRESPONSIVE — prior data used |

**Storage:** 979.76 GB of 5 TB used

---

## Google Drive — Top-Level Folders

| Folder | Modified | KAP Relevant | Status |
|---|---|---|---|
| 01_Y_OS_CORE | May 4 | YES | `CANDIDATE_REQUIRES_SCOPE_DECISION` |
| Y-OS | Jun 15 | YES | `CANDIDATE_REQUIRES_SCOPE_DECISION` |
| yOS | May 17 | YES | `CANDIDATE_REQUIRES_SCOPE_DECISION` — possible Y-OS duplicate |
| YOS Vision | Jun 20 | YES | `CANDIDATE_REQUIRES_SCOPE_DECISION` |
| 05_ARCHIVES_BACKUPS | May 4 | NO | `BACKUP_EXCLUDE_BY_DEFAULT` |
| Backup Google Drive | May 7 | NO | `BACKUP_EXCLUDE_BY_DEFAULT` |
| ARCHE-TYPES | May 23 | MAYBE | `CANDIDATE_REVIEW_LATER` |
| All others | — | NO | `OUT_OF_SCOPE` |

**Note:** Y-OS, yOS, YOS Vision = 3 separate folders at root. Possible fragmentation or staging/production split. Guardian must decide which is canonical before any acquisition.

---

## Google Drive — Obsidian Vaults Discovered

| ID | Name | Location | Modified | Status |
|---|---|---|---|---|
| GDRIVE-OBS-001 | Obsidian Vault | (APPS FOLDERS) | May 11 | `DISCOVERED_NOT_AUTHORIZED` |
| GDRIVE-OBS-002 | Obsidian Vault 2 | (APPS FOLDERS) | May 11 | `DISCOVERED_NOT_AUTHORIZED` |
| GDRIVE-OBS-003 | .obsidian (Y-WORLD) | Y-WORLD folder | May 28 | `DISCOVERED_LOW_PRIORITY` |

**Note:** "Obsidian Vault" and "Obsidian Vault 2" in (APPS FOLDERS) are likely Google Drive backups of local Mac vaults (possibly LUDIVINE). They are **not authorized** for access — Guardian scope decision required.

The Y-WORLD `.obsidian` folder confirms Y-World vault is backed up to Google Drive, but remains under the GitHub pipeline.

---

## iCloud — Vaults (from prior scan 2026-07-03)

| ID | Alias | MD Files | Status |
|---|---|---|---|
| ICLOUD-OBS-001 | ICLOUD://YWORLD/ | 17 | `DISCOVERED_LOW_PRIORITY` |
| ICLOUD-OBS-002 | ICLOUD://TEST/ | 8 | `EXCLUDED_BY_DEFAULT` |

No new iCloud vaults discovered. Prior data confirmed valid.

---

## Notable Root-Level Files (Google Drive)

| File | Type | Date | Note |
|---|---|---|---|
| Export_Gemini_Architecture_Export_et_Skill_Archive_2026-06-23 | Google Doc | Jun 23 | Y-OS architecture export |
| Export_Gemini_Configuration_Architecture_Export_YOS_2026-06-23 | Google Doc | Jun 23 | Y-OS config export |
| Export_Gemini_Session_Archivage_YOS_2026-06-23 | Google Doc | Jun 23 | Y-OS session archive |
| FinDash — Strategic Financial Dashboard | Google Sheet | May 27 | Financial — out of scope |
| Worldchanging — Resource Database (1032 resources) | Google Sheet | May 18 | Y-World candidate |
| Raindrop.io-Export.csv | CSV | May 20 | Bookmarks — candidate |

---

## Compliance

- No Markdown content read
- No frontmatter parsed
- No wikilinks parsed
- No attachments opened
- No source files copied
- No source mutation
- No import, merge, normalization, or synthesis
- Private paths: not applicable (Google Drive folder names are metadata)
- Backups excluded by default

---

## Gate Status

```
GDRIVE_ICLOUD_CENSUS_PASS_READY_FOR_GUARDIAN_REVIEW
```

**Next gate:** OBSIDIAN-SCOPE-DECISION-GATE (Guardian must decide on LUDIVINE, GDrive vaults, and Y-OS GDrive fragmentation before any acquisition)
