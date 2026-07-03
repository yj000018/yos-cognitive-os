# Y-WORLD Source Surface Map

**Date:** 2026-07-04
**Gate:** LOCAL-OBSIDIAN-SOURCE-SURFACE-DETECTION-GATE
**Author:** Manus AI

## Table 9.1 — Y-WORLD Source Surface Map

| Surface ID | Surface Name | Storage | Type | Known MD Count | Known Folder Count | Evidence Level | Current Status | Likely Role | Pipeline |
| ---------- | ------------ | ------- | ---- | -------------: | -----------------: | -------------- | -------------- | ----------- | -------- |
| **GITHUB-YWORLD** | Y-WORLD GitHub Repo | GitHub (`yj000018/Y-WORLD`, private) | Git Repository | 234 | 21 | `GIT_METADATA_ONLY` | `LIKELY_ACTIVE_CANDIDATE` | Active Sync / Canonical Candidate | GITHUB_PIPELINE |
| **GDRIVE-OBS-003** | GDrive Y-WORLD Obsidian Vault | Google Drive | Obsidian Vault | 235 | 18 | `BOUNDED_CONTENT_SAMPLE` | `HIGH_VALUE_HOLD_FOR_SCOPE_DECISION` | Active Candidate / Sync Mirror | GDRIVE_PIPELINE |
| **ICLOUD-YWORLD** | iCloud Y-World Micro-Vault | iCloud (`ICLOUD://obsidian/Y-World`) | Micro Vault | 17 | 6 | `MICRO_EXTRACTION_QUARANTINE` | `KEEP_FOR_FUTURE_COMPARISON` | Fragment / Comparison Source | ICLOUD_PIPELINE |
| **LOCAL-YWORLD** | Local Y-World (Mac) | Mac / Local filesystem | Unknown | Unknown | Unknown | `INSUFFICIENT` | `LOCAL_YWORLD_UNPROBED_SCOPE_UNCONFIRMED` | Unknown | LOCAL_PIPELINE |
| **LOCAL-GIT-YW** | Y-WORLD Git Clone | Mac / Local filesystem | Git Clone | 61 | Unknown | `METADATA_ONLY` | `HANDLE_UNDER_GITHUB_PIPELINE` | Local Git working copy | GITHUB_PIPELINE |

### Notes
- GITHUB-YWORLD: `yj000018/Y-WORLD`, private repo. Default branch: `main`. Latest commit: `7d07b459d1fc` (2026-05-29). Workflow: `compile-graph.yml`. No README. 324 total files, 234 MD.
- GDRIVE-OBS-003: GDrive folder ID `1i2ADPpj6LyTHhBHbm8BCCwpe-IjlrFkE`. 18 folders including `.obsidian`. Sampled `Y-WORLD Architecture.md`. MD count derived from prior local scan inventory (235 files).
- ICLOUD-YWORLD: 17 MD processed, 3 retained: `yos_memory_blueprint.md`, `Tool Intelligence Layer.md`, `ExcaliBrain Snapshot - Tool Intelligence Layer.excalidraw.md`.
- LOCAL-YWORLD: No distinct local vault path identified in vault discovery. Likely the local Git clone being synced to GitHub and GDrive. Cannot be safely probed without broad filesystem scan.
