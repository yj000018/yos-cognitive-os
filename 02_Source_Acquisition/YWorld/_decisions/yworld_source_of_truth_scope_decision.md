# Y-WORLD Source Role Decision Matrix

**Date:** 2026-07-04
**Gate:** YWORLD-SOURCE-OF-TRUTH-SCOPE-GATE
**Author:** Manus AI

| Surface | Active Candidate | Backup Candidate | Sync/Mirror Candidate | Fragment Candidate | Canonical Candidate | Evidence Level | Decision |
| ------- | ---------------: | ---------------: | --------------------: | -----------------: | ------------------: | -------------- | -------- |
| **GITHUB-YWORLD** | YES | NO | YES | NO | YES | `GIT_METADATA_ONLY` | `REQUIRES_COMPARISON` |
| **GDRIVE-OBS-003** | YES | NO | YES | NO | YES | `BOUNDED_CONTENT_SAMPLE` | `REQUIRES_COMPARISON` |
| **ICLOUD-YWORLD** | NO | NO | NO | YES | NO | `MICRO_EXTRACTION_QUARANTINE` | `FRAGMENT_CONFIRMED` |
| **LOCAL-YWORLD** | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | `INSUFFICIENT` | `UNCONFIRMED` |

### Evidence & Analysis

1. **GITHUB-YWORLD vs GDRIVE-OBS-003:**
   - GitHub API confirms `yj000018/Y-WORLD` has 234 MD files across 21 top-level folders. Last push was May 29, 2026.
   - Previous local scan data (now identified as the GDrive source) shows 235 MD files.
   - The close MD file count (234 vs 235) and identical folder structures strongly suggest that **GDrive is a live sync mirror of the local repository that pushes to GitHub**.
   - Neither can be definitively declared the canonical Source of Truth without a bounded metadata/filename comparison.

2. **ICLOUD-YWORLD:**
   - Confirmed as a fragment/micro-source containing only 17 files. 
   - 3 high-value files retained for future comparison.

3. **LOCAL-YWORLD:**
   - The vault discovery JSON does not contain a dedicated entry for a distinct local Y-WORLD vault (other than the iCloud fragment).
   - It is highly probable that the local Git clone (previously labeled `INST-GITHUB-YWORLD`) is the source being synced to both GDrive and GitHub.
   - Status remains unconfirmed without direct Mac filesystem access.

### Final Decision Output

`YWORLD_SOURCE_OF_TRUTH_NOT_DECIDED_REQUIRES_BOUNDED_COMPARISON`
