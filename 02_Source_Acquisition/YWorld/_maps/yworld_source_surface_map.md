# Y-WORLD Source Surface Map

**Date:** 2026-07-04
**Gate:** LOCAL-OBSIDIAN-SOURCE-SURFACE-DETECTION-GATE
**Correction Patch:** 2026-07-04 Overnight Batch — GDrive count corrected to 61 MD, GitHub confirmed canonical candidate.
**Author:** Manus AI

## Table 9.1 — Y-WORLD Source Surface Map

| Surface ID | Surface Name | Storage | Type | Known MD Count | Known Folder Count | Evidence Level | Current Status | Likely Role | Pipeline |
| ---------- | ------------ | ------- | ---- | -------------: | -----------------: | -------------- | -------------- | ----------- | -------- |
| **GITHUB-YWORLD** | Y-WORLD GitHub Repo | GitHub (`yj000018/Y-WORLD`, private) | Git Repository | 234 | 21 | `GIT_METADATA_ONLY` | `LIKELY_ACTIVE_CANDIDATE` | Active Sync / Canonical Candidate | GITHUB_PIPELINE |
| **GDRIVE-OBS-003** | Y-WORLD (GDrive — BACKUP) | Google Drive | Obsidian Vault | **61** (corrected) | 18 | `FULL_QUARANTINE_EXTRACTION` | `GDRIVE_YWORLD_PARTIAL_SNAPSHOT` | Partial older snapshot — Backup excluded | EXCLUDED |
| **ICLOUD-YWORLD** | iCloud Y-World Micro-Vault | iCloud (`ICLOUD://obsidian/Y-World`) | Micro Vault | 17 | 6 | `MICRO_EXTRACTION_QUARANTINE` | `KEEP_FOR_FUTURE_COMPARISON` | Fragment / Comparison Source | ICLOUD_PIPELINE |
| **LOCAL-YWORLD** | Local Y-World (Mac) | Mac / Local filesystem | Unknown | Unknown | Unknown | `INSUFFICIENT` | `LOCAL_YWORLD_UNPROBED_SCOPE_UNCONFIRMED` | Unknown | LOCAL_PIPELINE |
| **LOCAL-GIT-YW** | Y-WORLD (Local Git — BACKUP) | Mac / Local filesystem | Git Clone | 61 | Unknown | `METADATA_ONLY` | `LOCAL_GIT_YW_PARTIAL_SNAPSHOT` | Partial older snapshot — Backup excluded | EXCLUDED |

### Notes
- GITHUB-YWORLD: `yj000018/Y-WORLD`, private repo. Default branch: `main`. Latest commit: `7d07b459d1fc` (2026-05-29). Workflow: `compile-graph.yml`. No README. 324 total files, 234 MD.
- GDRIVE-OBS-003: GDrive folder ID `1i2ADPpj6LyTHhBHbm8BCCwpe-IjlrFkE`. **CORRECTED:** Full rclone extraction confirmed 61 MD files (not 235). 100% are a subset of GitHub. 0 GDrive-only files. Backup excluded final.
- ICLOUD-YWORLD: 17 MD processed, 3 retained: `yos_memory_blueprint.md`, `Tool Intelligence Layer.md`, `ExcaliBrain Snapshot - Tool Intelligence Layer.excalidraw.md`.
- LOCAL-YWORLD: No distinct local vault path identified in vault discovery. Likely the local Git clone being synced to GitHub and GDrive. Cannot be safely probed without broad filesystem scan.
