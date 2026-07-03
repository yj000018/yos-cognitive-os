# MPM Full Body — KAP WP2-M4 — Full Manus Tasks and Outputs Capture

> **Source:** MPM-Full-Body-Capture-Pack-Bootstrap-Session.md (MPM-003)
> **Status:** FULL_BODY_PERSISTED
> **Capture date:** 2026-07-03

---

KAP WP2-M4 — Full Manus Tasks and Outputs Capture

**Capture status:** FULL  
**Notes:** Full body extracted from KAP-Finish-Manus-Roadmap-and-MPM-Pack.md lines 525–713.


# MPM — KAP WP2-M4 — Full Manus Tasks and Outputs Capture

**Program:** KAP — Knowledge Assimilation Program  
**Phase:** Phase 1 / WP2 — Controlled Source Acquisition  
**Sprint:** WP2-M4 — Full Manus Tasks and Outputs Capture  
**Execution Partner:** Manus Desktop  
**Authority:** Yannick + ChatGPT / yOS Architect  
**Status:** Conditional ready  
**Mode:** Task body / output / deliverable capture  
**Core rule:** Task metadata is not enough. Capture final outputs, files, websites, and deliverables.

---

## EXECUTION WRAPPER

Execute after WP2-M2 or when task access is available.

All task domains are in scope, including personal/private/peripheral content.

Do not acquire browser history, shell history, caches, or unrelated traces.

---

## 1. Mission

Upgrade Manus Tasks from metadata-only to full task acquisition.

Known current state:

- 52 tasks inventoried.
- Mostly metadata only.
- 8 outputs found.
- Many task final outputs/livrables likely not acquired.

Target state:

- all task metadata
- full final answer if accessible
- attached/generated files
- linked websites
- linked repos
- linked Notion pages
- output artifacts
- screenshots if needed
- user input request for inaccessible tasks

---

## 2. Root Folder

Create:

`/home/ubuntu/KAP/02_Source_Acquisition/WP2-M4_Full_Manus_Tasks_Outputs_Capture/`

Subfolders:

- `00_REPORTS/`
- `01_TASK_INVENTORY/`
- `02_TASK_FULL_TEXT/`
- `03_TASK_OUTPUTS/`
- `04_LINKED_WEBSITES/`
- `05_LINKED_FILES/`
- `06_USER_INPUT/`
- `07_MANIFESTS/`
- `08_CHECKSUMS/`
- `09_BLOCKERS/`

---

## 3. Priority Order

P0 first:

- KAP
- yOS
- KRE
- memory
- context continuity
- Manus pipeline
- Notion exporter
- session extractor
- Y-WORLD
- Living Backbone
- COSA
- agent architecture
- LLM/tool routing
- Program OS
- MOP amendments

P1 next:

- ELYSIUM
- KOSMOS
- OneShift
- civilization
- Human Awakening
- Divine Spiritual Library
- archetypes
- knowledge graphs
- websites

P2/P3 after:

- finance
- health
- real estate
- travel
- apps
- prototypes
- personal/private
- experiments
- all remaining tasks

No domain is excluded.

---

## 4. Required Outputs

Create:

1. `KAP-WP2-M4-Full-Tasks-Inventory.md`
2. `KAP-WP2-M4-Full-Tasks-Inventory.json`
3. `KAP-WP2-M4-Task-Outputs-Registry.md`
4. `KAP-WP2-M4-Linked-Websites-Registry.md`
5. `KAP-WP2-M4-Linked-Files-Registry.md`
6. `KAP-WP2-M4-User-Input-Needed.md`
7. `KAP-WP2-M4-Blockers.md`
8. `KAP-WP2-M4-Checksum-Manifest.json`

For each acquired task body:

`02_TASK_FULL_TEXT/KAP-TASK-###_<safe_title>.md`

For each output:

`03_TASK_OUTPUTS/<task_id>/<filename>`

---

## 5. Required Task Table

| task_id | title | date | status | priority | full_text_acquired | final_output_acquired | files_acquired | linked_website | linked_repo | linked_notion | acquisition_method | limitations |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

---

## 6. If Blocked

Create exact user request:

`KAP-WP2-M4-User-Input-Needed.md`

Format:

| request_id | task_title | screen_to_open | preferred_input | exact_user_action | why_needed |
|---|---|---|---|---|---|

Ask Yannick for:

1. screenshots of task page
2. copy-paste final output
3. downloaded task files
4. website links
5. exported ZIPs

---

## 7. Final Response Required

Return only:

1. execution status
2. tasks inspected
3. full task bodies acquired
4. final outputs acquired
5. files acquired
6. linked websites found
7. user input required
8. output folder
9. blockers
10. recommended next MPM

End with exactly:

> KAP WP2-M4 complete. Manus Tasks and outputs capture ready for Architect review.

---
