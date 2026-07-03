# MPM Full Body — KAP WP2-M3 — Full Manus Knowledge Capture

> **Source:** MPM-Full-Body-Capture-Pack-Bootstrap-Session.md (MPM-002)
> **Status:** FULL_BODY_PERSISTED
> **Capture date:** 2026-07-03

---

KAP WP2-M3 — Full Manus Knowledge Capture

**Capture status:** FULL  
**Notes:** Full body extracted from KAP-Finish-Manus-Roadmap-and-MPM-Pack.md lines 380–522.


# MPM — KAP WP2-M3 — Full Manus Knowledge Capture

**Program:** KAP — Knowledge Assimilation Program  
**Phase:** Phase 1 / WP2 — Controlled Source Acquisition  
**Sprint:** WP2-M3 — Full Manus Knowledge Capture  
**Execution Partner:** Manus Desktop  
**Authority:** Yannick + ChatGPT / yOS Architect  
**Status:** Conditional ready  
**Mode:** Knowledge content acquisition / user-assisted fallback  
**Core rule:** Metadata is not enough. Acquire full content or request exact user input.

---

## EXECUTION WRAPPER

Execute this sprint only after WP2-M2 identifies Manus Knowledge as accessible or user-assisted.

All content domains are in scope. Do not exclude content because it is personal, sensitive, private, peripheral, or secret-bearing.

---

## 1. Mission

Acquire the full content of Manus Knowledge / Memory entries.

Known from E2B/M1C:

- 15 entries visible in DOM metadata.
- 42+ additional entries not rendered.
- Current state is metadata only.

Target state:

- full title
- full body/content
- creation/update date if visible
- enabled/canonical/status if visible
- source/context links if visible
- associated files if visible
- category/domain
- acquisition method
- limitations

---

## 2. Root Folder

Create:

`/home/ubuntu/KAP/02_Source_Acquisition/WP2-M3_Full_Manus_Knowledge_Capture/`

Subfolders:

- `00_REPORTS/`
- `01_KNOWLEDGE_INVENTORY/`
- `02_RAW_CONTENT/`
- `03_USER_INPUT/`
- `04_SCREENSHOT_TRANSCRIPTS/`
- `05_MANIFESTS/`
- `06_CHECKSUMS/`
- `07_BLOCKERS/`

---

## 3. Acquisition Methods

Try in this order:

1. direct internal data source if available
2. Manus UI DOM expansion/click-through
3. visible content scraping
4. local stored knowledge files
5. exported files
6. user copy-paste
7. user screenshots
8. Notion Memory Hub reference if knowledge was mirrored there

Do not stop at metadata unless all content methods fail.

---

## 4. Required Outputs

Create:

1. `KAP-WP2-M3-Full-Knowledge-Inventory.md`
2. `KAP-WP2-M3-Full-Knowledge-Inventory.json`
3. `KAP-WP2-M3-Knowledge-Content-Registry.md`
4. `KAP-WP2-M3-User-Input-Needed.md`
5. `KAP-WP2-M3-Blockers.md`
6. `KAP-WP2-M3-Checksum-Manifest.json`

For each entry, create one raw markdown file:

`02_RAW_CONTENT/KAP-KNO-###_<safe_title>.md`

---

## 5. Required Table

| knowledge_id | title | status | date | content_acquired | acquisition_method | content_file | domain | linked_sources | limitations |
|---|---|---|---|---|---|---|---|---|---|

---

## 6. If Blocked

If full content is inaccessible, create exact user request:

`KAP-WP2-M3-User-Input-Needed.md`

Format:

| request_id | entry_title | screen_to_open | preferred_input | exact_user_action | why_needed |
|---|---|---|---|---|---|

Preferred input order:

1. copy-paste full entry text
2. screenshot full entry
3. screen recording only if needed

---

## 7. Final Response Required

Return only:

1. execution status
2. entries visible
3. entries full-content acquired
4. hidden entries found
5. entries requiring user input
6. output folder
7. blockers
8. recommended next MPM

End with exactly:

> KAP WP2-M3 complete. Manus Knowledge capture ready for Architect review.

---
