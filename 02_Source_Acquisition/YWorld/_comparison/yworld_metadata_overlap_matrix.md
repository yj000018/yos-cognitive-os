# Y-WORLD Metadata Overlap Matrix

## 1. Top-Level Folder Overlap (GitHub vs GDrive)

| Folder | GITHUB-YWORLD | GDRIVE-OBS-003 | Match Status |
|---|---|---|---|
| `.obsidian` | YES | YES | MATCH |
| `00_System` | YES | YES | MATCH |
| `01_Cockpit` | YES | YES | MATCH |
| `02_Maps` | YES | YES | MATCH |
| `03_Dashboards` | YES | YES | MATCH |
| `04_Templates` | YES | YES | MATCH |
| `05_Registries` | YES | YES | MATCH |
| `06_Workflows` | YES | YES | MATCH |
| `07_Agent_Operations` | YES | YES | MATCH |
| `20_Life` | YES | YES | MATCH |
| `30_Knowledge` | YES | YES | MATCH |
| `50_Projects` | YES | YES | MATCH |
| `60_Y-OS` | YES | YES | MATCH |
| `70_CasaTAO` | YES | YES | MATCH |
| `71_ARC_Anandaz` | YES | YES | MATCH |
| `80_Archetypes` | YES | YES | MATCH |
| `81_Y-Publishing` | YES | YES | MATCH |
| `90_Reality_Interfaces` | YES | YES | MATCH |
| `.github` | YES | NO | GITHUB ONLY (CI/CD) |
| `10_Inbox` | YES | NO | GITHUB ONLY (7 MD) |
| `40_K-Cards` | YES | NO | GITHUB ONLY (10 MD) |

## 2. iCloud Retained Files Overlap

| File | ICLOUD-YWORLD | GITHUB-YWORLD | Match Status |
|---|---|---|---|
| `yos_memory_blueprint.md` | YES | NO | ICLOUD ONLY |
| `Tool Intelligence Layer.md` | YES | NO | ICLOUD ONLY |
| `Excalidraw/ExcaliBrain Snapshot...` | YES | NO | ICLOUD ONLY |

## 3. Key Findings
- **GDrive MD Count Correction:** The previously reported "235 MD files" for GDrive was incorrectly attributed. It came from an earlier GitHub API scan that included a `.canvas` file. The true GitHub MD count is 234. The true GDrive MD count remains unknown (bounded probe only confirmed >100).
- **High Folder Overlap:** 18 out of 21 GitHub folders are present in GDrive.
- **GitHub Exclusives:** `.github` (CI/CD), `10_Inbox`, and `40_K-Cards` are present in GitHub but missing from GDrive.
- **iCloud Uniqueness:** The 3 retained files from the iCloud micro-vault do NOT exist in the GitHub repo, confirming they are unique fragments.
