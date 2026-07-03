# MPM Full Body — KAP WP2-M6 — Manus Memory Hub / Notion Bridge Acquisition

> **Source:** MPM-Full-Body-Capture-Pack-Bootstrap-Session.md (MPM-005)
> **Status:** FULL_BODY_PERSISTED
> **Capture date:** 2026-07-03

---

KAP WP2-M6 — Manus Memory Hub / Notion Bridge Acquisition

**Capture status:** FULL  
**Notes:** Full body extracted from KAP-Finish-Manus-Roadmap-and-MPM-Pack.md lines 880–1029.


# MPM — KAP WP2-M6 — Manus Memory Hub / Notion Bridge Acquisition

**Program:** KAP — Knowledge Assimilation Program  
**Phase:** Phase 1 / WP2 — Controlled Source Acquisition  
**Sprint:** WP2-M6 — Manus Memory Hub / Notion Bridge Acquisition  
**Execution Partner:** Manus Desktop  
**Authority:** Yannick + ChatGPT / yOS Architect  
**Status:** Conditional ready  
**Mode:** Manus memory archive acquisition through Notion bridge  
**Core rule:** This is still part of finishing Manus. Notion is treated here as the archive mirror/projection of Manus sessions, not as a separate broad Notion harvest.

---

## EXECUTION WRAPPER

Execute only after WP2-M2 confirms Notion/Memory Hub is required or when Yannick provides Notion access/export/link.

Do not perform broad Notion workspace acquisition.

Acquire only the Manus Memory Hub / Manus sessions/cards / Memory Pipeline-related databases/pages.

All content domains inside Manus memory are in scope.

---

## 1. Mission

Acquire the Manus Memory Hub / Notion bridge content that contains the 325+ archived Manus sessions and related session cards.

Known from previous pipeline docs:

- Manus sessions processed: 325
- sessions archived in Notion: 325/325
- verbatim pages updated: 278
- project clusters identified: 7
- possible sessions DB ID: `0720db9b-5e1d-41a2-bd0c-6721fe0dab94`
- possible hub DB ID: `4ea5d9b7-1919-4ed6-974a-3e73049fe9bf`

Verify these; do not assume if inaccessible.

---

## 2. Root Folder

Create:

`/home/ubuntu/KAP/02_Source_Acquisition/WP2-M6_Manus_Memory_Hub_Notion_Bridge/`

Subfolders:

- `00_REPORTS/`
- `01_NOTION_ACCESS/`
- `02_DATABASE_INVENTORY/`
- `03_SESSION_CARDS/`
- `04_VERBATIM_PAGES/`
- `05_PROJECT_CLUSTERS/`
- `06_EXPORTS/`
- `07_USER_INPUT/`
- `08_CHECKSUMS/`
- `09_BLOCKERS/`

---

## 3. Access Methods

Try:

1. Notion connector if available
2. known database/page IDs
3. exported Notion ZIP/Markdown/CSV if provided by Yannick
4. copied Notion table data
5. screenshots as last resort

If connector is disabled, create exact manual export instructions.

---

## 4. Required Outputs

Create:

1. `KAP-WP2-M6-Notion-Access-Report.md`
2. `KAP-WP2-M6-Manus-Memory-Hub-Inventory.md`
3. `KAP-WP2-M6-Manus-Session-Cards-Registry.md`
4. `KAP-WP2-M6-Verbatim-Pages-Registry.md`
5. `KAP-WP2-M6-Project-Clusters-Registry.md`
6. `KAP-WP2-M6-User-Input-Needed.md`
7. `KAP-WP2-M6-Blockers.md`
8. `KAP-WP2-M6-Checksum-Manifest.json`

---

## 5. Required Tables

Database inventory:

| db_id | db_name | type | accessible | record_count | fields | acquisition_method | limitations |
|---|---|---|---|---|---|---|---|

Session cards:

| session_id | title | date | source | project | content_acquired | verbatim_page | files | checksum | limitations |
|---|---|---|---|---|---|---|---|---|---|

Project clusters:

| cluster_id | cluster_name | session_count | domain | representative_sessions | status |
|---|---|---|---|---|---|

---

## 6. If Connector Blocked

Create manual instructions for Yannick:

`KAP-WP2-M6-Manual-Notion-Export-Instructions.md`

Include:

1. exact Notion page/database to open
2. export format preferred: Markdown + CSV
3. whether to include subpages
4. how to zip export
5. what file name to use
6. where to upload it
7. what Manus will do next

---

## 7. Final Response Required

Return only:

1. execution status
2. Notion/Memory Hub accessible: yes/no
3. databases found
4. session cards acquired
5. verbatim pages acquired
6. project clusters acquired
7. user export required: yes/no
8. output folder
9. blockers
10. recommended next MPM

End with exactly:

> KAP WP2-M6 complete. Manus Memory Hub bridge ready for Architect review.

---
