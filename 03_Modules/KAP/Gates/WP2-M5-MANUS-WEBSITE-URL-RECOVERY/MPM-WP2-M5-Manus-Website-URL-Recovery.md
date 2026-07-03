# MPM Full Body — KAP WP2-M5 — Manus Website URL Recovery and Content Deep Capture

> **Source:** MPM-Full-Body-Capture-Pack-Bootstrap-Session.md (MPM-004)
> **Status:** FULL_BODY_PERSISTED
> **Capture date:** 2026-07-03

---

KAP WP2-M5 — Manus Website URL Recovery and Content Deep Capture

**Capture status:** FULL  
**Notes:** Full body extracted from KAP-Finish-Manus-Roadmap-and-MPM-Pack.md lines 716–877.


# MPM — KAP WP2-M5 — Manus Website URL Recovery and Content Deep Capture

**Program:** KAP — Knowledge Assimilation Program  
**Phase:** Phase 1 / WP2 — Controlled Source Acquisition  
**Sprint:** WP2-M5 — Manus Website URL Recovery and Content Deep Capture  
**Execution Partner:** Manus Desktop  
**Authority:** Yannick + ChatGPT / yOS Architect  
**Status:** Conditional ready  
**Mode:** URL recovery / website capture / source artifact capture  
**Core rule:** A website title without URL is not acquired. Recover URLs or ask Yannick for exact UI input.

---

## EXECUTION WRAPPER

Execute after WP2-M2 or when websites surface is accessible.

All website domains are in scope.

---

## 1. Mission

Complete Manus deployed website acquisition.

Known current state:

- 33 website titles listed.
- 3 URLs found:
  - `https://youniverse.manus.space/`
  - `https://human-progress.manus.space/`
- 30 websites unresolved.
- content captured only for found URLs.

Target state:

- URLs for every website if accessible
- visibility/status
- deployment metadata
- source task if identifiable
- source/build artifacts if available
- HTML/text/screenshots for every reachable public site
- user-input request for unresolved websites

---

## 2. Root Folder

Create:

`/home/ubuntu/KAP/02_Source_Acquisition/WP2-M5_Manus_Website_URL_Recovery_Content_Capture/`

Subfolders:

- `00_REPORTS/`
- `01_WEBSITE_INVENTORY/`
- `02_URL_RECOVERY/`
- `03_HTML_SNAPSHOTS/`
- `04_TEXT_EXTRACTS/`
- `05_SCREENSHOTS/`
- `06_SOURCE_BUILD_ARTIFACTS/`
- `07_USER_INPUT/`
- `08_CHECKSUMS/`
- `09_BLOCKERS/`

---

## 3. URL Recovery Methods

Try:

1. Manus website UI/card/settings
2. task pages that created/deployed the website
3. local website build/source folders
4. previous reports/ZIPs
5. deployment logs/metadata if explicit
6. known Manus domain patterns
7. browser-accessible probing if URL is known
8. user screenshots/copy-paste

Do not fabricate URLs.

---

## 4. Required Outputs

Create:

1. `KAP-WP2-M5-Corrected-Websites-Inventory.md`
2. `KAP-WP2-M5-Corrected-Websites-Inventory.json`
3. `KAP-WP2-M5-URL-Recovery-Report.md`
4. `KAP-WP2-M5-Website-Content-Capture-Report.md`
5. `KAP-WP2-M5-Website-Source-Build-Artifacts-Report.md`
6. `KAP-WP2-M5-User-Input-Needed.md`
7. `KAP-WP2-M5-Blockers.md`
8. `KAP-WP2-M5-Checksum-Manifest.json`

---

## 5. Required Table

| website_id | title | url | url_source | reachable | content_captured | html | text | screenshot | source_artifacts | linked_task | limitations |
|---|---|---|---|---|---|---|---|---|---|---|---|

---

## 6. Capture Rules

For each reachable website:

- save HTML
- save rendered text
- save screenshot if possible
- list visible routes
- capture source/build artifacts if present locally
- compute checksum

For unreachable or URL-missing websites:

- do not mark content captured
- request user input

---

## 7. User Input Request

If URLs are missing, ask Yannick for:

1. screenshot of the Manus Websites list
2. screenshot/open view for each unresolved card
3. copy-paste URL if visible
4. screenshots of deployment settings if available
5. any downloaded website ZIP/source folders

Create exact request file:

`KAP-WP2-M5-User-Input-Needed.md`

---

## 8. Final Response Required

Return only:

1. execution status
2. websites inspected
3. URLs recovered
4. reachable websites
5. website captures created
6. source/build artifacts found
7. unresolved websites
8. user input required
9. output folder
10. blockers
11. recommended next MPM

End with exactly:

> KAP WP2-M5 complete. Manus website acquisition ready for Architect review.

---
