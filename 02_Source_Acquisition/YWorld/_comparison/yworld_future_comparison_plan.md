# Y-WORLD Future Comparison Plan

**Date:** 2026-07-04
**Gate:** YWORLD-SOURCE-OF-TRUTH-SCOPE-GATE
**Author:** Manus AI

## 1. Objective

To execute a strictly bounded comparison between the high-value Y-WORLD source surfaces to definitively establish the canonical Source of Truth, without performing any unauthorized data mutation, merging, or canonicalization.

## 2. Comparison Need Matrix

| Comparison | Needed? | Purpose | Allowed Now? | Future Gate |
| ---------- | ------: | ------- | -----------: | ----------- |
| GDrive Y-WORLD vs GitHub Y-World | YES | Determine if GDrive is a 1:1 mirror of GitHub, or if one is ahead. | NO | `YWORLD-BOUNDED-COMPARISON-GATE` |
| iCloud Y-World retained files vs GitHub Y-World | YES | Check if the 3 retained iCloud files exist or are newer in GitHub. | NO | `YWORLD-BOUNDED-COMPARISON-GATE` |
| iCloud Y-World retained files vs GDrive Y-WORLD | YES | Check if the 3 retained iCloud files exist or are newer in GDrive. | NO | `YWORLD-BOUNDED-COMPARISON-GATE` |
| GDrive Y-WORLD vs Local Y-World | NO | Local source unconfirmed/inaccessible; likely identical to GDrive/GitHub. | NO | N/A |
| GDrive Y-WORLD vs LUDIVINE | NO | Not authorized. | NO | N/A |

## 3. Future Gate Definition: `YWORLD-BOUNDED-COMPARISON-GATE`

If authorized by the Guardian, the next gate will execute the following bounded comparison steps:

### 3.1 Authorized Actions
- **Metadata Comparison:** Compare file counts, folder structures, and overall size.
- **File Tree Comparison:** Generate and compare full file trees from GDrive and GitHub.
- **Filename Overlap:** Identify exact filename matches, missing files, and unique files across surfaces.
- **Modified-Date Comparison:** Compare `updated_at` or `last_modified` timestamps for overlapping files to determine which surface holds the latest version.
- **Hash Comparison:** ONLY if explicitly authorized by Guardian (requires full file read).
- **Bounded Content Comparison:** ONLY if explicitly authorized by Guardian (requires content extraction).

### 3.2 Strictly Forbidden Actions
- NO synthesis of content.
- NO merging of files or folders.
- NO normalization of filenames or paths.
- NO canonicalization of data.
- NO source mutation (no pushes, no uploads, no deletions).

### 3.3 Expected Output
A definitive recommendation on which surface should be treated as the canonical Source of Truth, and a proposed ingestion strategy for the KAP pipeline.
