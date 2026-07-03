# Y-WORLD Future Comparison Plan

**Date:** 2026-07-04
**Gate:** YWORLD-SOURCE-OF-TRUTH-SCOPE-GATE (v2)
**Author:** Manus AI

## Table 9.4 — Comparison Need Matrix

| Comparison | Needed? | Purpose | Allowed Now? | Future Gate |
| ---------- | :-----: | ------- | :----------: | ----------- |
| GDrive Y-WORLD vs GitHub Y-World | YES | Determine if GDrive is a 1:1 mirror of GitHub, or if one is ahead/stale/incomplete. | NO | `YWORLD-BOUNDED-COMPARISON-GATE` |
| iCloud Y-World retained files vs GitHub Y-World | YES | Check if the 3 retained iCloud files exist or are newer in GitHub. | NO | `YWORLD-BOUNDED-COMPARISON-GATE` |
| iCloud Y-World retained files vs GDrive Y-WORLD | YES | Check if the 3 retained iCloud files exist or are newer in GDrive. | NO | `YWORLD-BOUNDED-COMPARISON-GATE` |
| GDrive Y-WORLD vs Local Y-World | NO | Local source unconfirmed/inaccessible. Presumed identical to GDrive/GitHub. | NO | N/A — `LOCAL_YWORLD_UNPROBED_SCOPE_UNCONFIRMED` |
| GDrive Y-WORLD vs LUDIVINE | NO | Not authorized. LUDIVINE is excluded final. | NO | N/A |

---

## Authorized Actions for `YWORLD-BOUNDED-COMPARISON-GATE`

### Step 1 — Metadata Comparison
Compare file counts, folder structures, and overall size between GitHub and GDrive.

### Step 2 — File Tree Comparison
Generate and compare full file trees from GDrive and GitHub. Identify exact filename matches, missing files, and unique files across surfaces.

### Step 3 — Filename Overlap
Produce a three-column overlap matrix: files only in GitHub, files only in GDrive, files in both.

### Step 4 — Modified-Date Comparison
Compare `updated_at` or `last_modified` timestamps for overlapping files to determine which surface holds the latest version.

### Step 5 — iCloud Fragment Comparison
Check whether the 3 retained iCloud files (`yos_memory_blueprint.md`, `Tool Intelligence Layer.md`, `ExcaliBrain Snapshot`) exist in GitHub and GDrive, and compare modification dates.

### Step 6 — Hash Comparison (BLOCKED)
Requires explicit Guardian authorization. Do not execute until authorized.

### Step 7 — Bounded Content Comparison (BLOCKED)
Requires explicit Guardian authorization. Do not execute until authorized.

### Step 8 — Duplicate Detection
Identify files with identical names across surfaces. Flag potential duplicates for Guardian review.

### Step 9 — Canonical Candidate Decision
Based on steps 1–8, produce a recommendation for the canonical Source of Truth. This is a recommendation only — final decision requires Guardian approval.

### Step 10 — User / Guardian Review
Deliver comparison report to Guardian. Await explicit authorization before any merge, synthesis, or canonicalization.

---

## Strictly Forbidden Actions (until Guardian approval)

- NO semantic synthesis.
- NO current-best knowledge generation.
- NO normalization of filenames or paths.
- NO merging of files or folders.
- NO destructive deduplication.
- NO canonicalization of data.
- NO source mutation (no pushes, no uploads, no deletions).
- NO broad local filesystem scan.
- NO LUDIVINE access.
