# LUDIVINE Scope Decision Framework

> Y-OS / KAP Cognitive Architecture
> Status: DRAFT

---

## 1. The Problem
The LUDIVINE vault (1842 MD files) is massive. Ingesting it entirely into the KAP pipeline without scoping will overwhelm the Source Fragment extraction process and introduce massive amounts of non-architectural noise (e.g., daily notes, personal logs, raw clippings).

## 2. Decision Options

### Option A: Full Ingestion (Not Recommended)
- **Pros:** Comprehensive.
- **Cons:** High noise, high processing cost, likely contains sensitive/irrelevant data.

### Option B: Strict Path Exclusion
- **Mechanism:** Identify high-noise folders (e.g., `Daily Notes`, `Clippings`, `Archive`) and exclude them entirely.
- **Pros:** Reduces volume significantly while capturing potential value in core folders.
- **Cons:** Might miss architectural insights buried in daily notes.

### Option C: Whitelist Only
- **Mechanism:** Only ingest specific folders known to contain Y-OS/KAP relevant data (e.g., `Architecture`, `Projects/Y-OS`).
- **Pros:** Safest, lowest noise.
- **Cons:** High risk of missing unfiled but valuable fragments.

### Option D: Tag-Based Extraction (Requires Content Scan)
- **Mechanism:** Scan all files for specific tags (e.g., `#yos`, `#architecture`).
- **Pros:** Highly targeted.
- **Cons:** Requires violating the "No Content Access" rule to perform the initial scan.

## 3. Recommendation for Next Gate
Proceed with **Option B (Strict Path Exclusion)** combined with a metadata-only directory tree analysis to identify the exclusion paths before any content is read.
