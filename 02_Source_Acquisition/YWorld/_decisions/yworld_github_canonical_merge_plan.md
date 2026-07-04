# Y-WORLD Canonical Merge Plan

**Date:** 2026-07-04
**Executor:** Manus (KAP Executor)
**Status:** `YWORLD_GITHUB_CANONICAL_MERGE_PLAN_PASS_READY_FOR_GUARDIAN_DECISION`

## 1. Executive Summary

This document outlines the strategy for establishing `GITHUB-YWORLD` as the primary canonical source of truth for the Y-WORLD vault. It defines how to handle the 6 files with size differences found in the older GDrive snapshot and how to integrate the 3 unique high-value fragments recovered from iCloud.

**No merge execution or source mutation has occurred.** This is a planning document only.

## 2. Canonical Source Designation

| Source | Role | Justification |
|---|---|---|
| **GITHUB-YWORLD** | **Primary Canonical Candidate** | Contains 234 MD files. Superset of all other snapshots. Active workflow indicators present. |
| **GDRIVE-OBS-003** | Excluded Backup | Only 61 MD files. Exact subset of GitHub. |
| **LOCAL-GIT-YW** | Excluded Backup | Only 61 MD files. Exact subset of GitHub. |

## 3. Delta File Resolution Plan

Six files exist in both GitHub and GDrive but have different sizes.

### 3.1 GDrive-Larger File (Requires Merge)
- **File:** `01_Cockpit/Weekly Review Surface.md`
- **GitHub Size:** 297B
- **GDrive Size:** 703B
- **Analysis:** The GDrive version contains a more developed template structure (Metrics, Checklist, Inbox Zero, Project Review, etc.), whereas the GitHub version is a stub.
- **Action Plan:** **OVERWRITE** the GitHub version with the GDrive version in the canonical staging branch.

### 3.2 GitHub-Larger Files (Keep GitHub)
- `01_Cockpit/HOME.md` (GitHub is +476B)
- `02_Maps/Y-WORLD ROOT MAP.md` (GitHub is +1057B)
- `03_Dashboards/Y-WORLD Dashboard.md` (GitHub is +894B)
- `07_Agent_Operations/Manus Task Queue.md` (GitHub is +15B)
- `50_Projects/Projects Log.md` (GitHub is +641B)
- **Analysis:** The GitHub versions contain significantly more content, expanded tables, and active project data.
- **Action Plan:** **KEEP** the GitHub versions. Discard the GDrive versions.

## 4. iCloud Fragment Integration Plan

Three high-value files were recovered from iCloud that do not exist in GitHub or GDrive.

| Fragment | Target Canonical Path | Rationale |
|---|---|---|
| `yos_memory_blueprint.md` | `60_Y-OS/yos_memory_blueprint.md` | Core Y-OS architectural document. Belongs in the Y-OS domain folder. |
| `Tool Intelligence Layer.md` | `60_Y-OS/Tool Intelligence Layer.md` | Maps tool capabilities and routing. Belongs in the Y-OS domain folder. |
| `ExcaliBrain Snapshot...` | `60_Y-OS/Excalidraw/ExcaliBrain Snapshot - Tool Intelligence Layer.excalidraw.md` | Visual map of the Tool Intelligence Layer. Needs an Excalidraw subfolder. |

## 5. Execution Staging Protocol

When authorized by Guardian, the merge will be executed as follows:

1. Clone `GITHUB-YWORLD` into a local staging directory.
2. Copy `Weekly Review Surface.md` from GDrive delta quarantine and overwrite the GitHub version.
3. Copy the 3 iCloud fragments into the `60_Y-OS/` folder of the staging directory.
4. Run a final validation script to ensure 237 total MD files (234 original - 1 overwrite + 1 GDrive overwrite + 3 iCloud additions = 237).
5. Commit to a new branch `canonical-merge-candidate` on GitHub.

**Current Status:** Awaiting Guardian authorization to execute the staging protocol.
