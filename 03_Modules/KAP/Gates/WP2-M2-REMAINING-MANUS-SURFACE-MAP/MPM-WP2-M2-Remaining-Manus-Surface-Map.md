# MPM Full Body — KAP WP2-M2 — Remaining Manus Surface Map & Human-Assisted Extraction Plan

> **Source:** MPM-Full-Body-Capture-Pack-Bootstrap-Session.md (MPM-001)
> **Status:** FULL_BODY_PERSISTED
> **Capture date:** 2026-07-03

---

KAP WP2-M2 — Remaining Manus Surface Map & Human-Assisted Extraction Plan

**Capture status:** FULL  
**Notes:** Full body extracted from KAP-Finish-Manus-Roadmap-and-MPM-Pack.md lines 149–375.


# MPM — KAP WP2-M2 — Remaining Manus Surface Map & Human-Assisted Extraction Plan

**Program:** KAP — Knowledge Assimilation Program  
**Phase:** Phase 1 / WP2 — Controlled Source Acquisition  
**Sprint:** WP2-M2 — Remaining Manus Surface Map & Human-Assisted Extraction Plan  
**Execution Partner:** Manus Desktop  
**Authority:** Yannick + ChatGPT / yOS Architect  
**Status:** Ready for execution  
**Mode:** Access mapping / gap closure / human-in-the-loop plan  
**Core rule:** Do not claim completion unless content was actually acquired. If blocked, produce exact user-input instructions.

---

## EXECUTION WRAPPER — RUN THIS MPM NOW

Do not rewrite or summarize this MPM.

Execute it.

Return only execution results, files created, blockers, user-input requests, and recommended next step.

All content domains are in scope, including personal, health, finance, real estate, credentials, private sessions, prototypes and peripheral projects. Do not exclude content because it is personal or secret-bearing. Yannick manages security.

Do not proceed to GitHub, Notion full acquisition, Mem0, ChatGPT, Claude, Gemini or Perplexity in this sprint.

Do not process browser history, shell history, caches, emails, or unrelated system traces.

---

## 0. Current Context

Prior sprints:

- WP2-E1 acquired GitHub/skills/local artifacts baseline.
- WP2-E2 acquired memory pipeline docs/scripts, but local `/home/ubuntu/manus_pipeline/` was absent.
- WP2-E2B extracted Manus control-plane metadata via DOM/probing.
- WP2-M1 attempted Complete Manus Harvest.
- WP2-M1C corrected the bundle and confirmed: `MANUS_INCOMPLETE_ACCESS_REQUIRED`.

Known gaps:

- Manus Knowledge = metadata only.
- 15 Knowledge entries visible, 42+ not rendered.
- Manus Tasks = 52 metadata entries, not full task bodies.
- Task outputs = 8 found, likely incomplete.
- Websites = 33 entries, only 3 URLs resolved.
- Website content = 3 captured, 30 unresolved.
- Session archives = likely 325+ in Notion Memory Hub.
- Source cards/manifests/checksums missing or incomplete.

---

## 1. Mission

Produce a precise, truthful remaining Manus acquisition map.

The output must answer:

1. What exact Manus surfaces remain?
2. What is directly accessible to Manus now?
3. What is blocked by API/DOM/UI/auth/connector limitations?
4. What can be acquired with user screenshots?
5. What can be acquired with user copy-paste?
6. What requires Notion Memory Hub?
7. What requires valid Manus API access?
8. What can be finished now without new access?

---

## 2. Root Folder

Create:

`/home/ubuntu/KAP/02_Source_Acquisition/WP2-M2_Remaining_Manus_Surface_Map/`

Create subfolders:

- `00_REPORTS/`
- `01_ACCESS_MAP/`
- `02_USER_INPUT_REQUESTS/`
- `03_REMAINING_SURFACES/`
- `04_NEXT_MPM_INPUTS/`
- `05_BLOCKERS/`

---

## 3. Surfaces To Inspect

Inspect only explicit Manus/KAP/yOS/project acquisition surfaces, not unrelated system traces.

Check:

1. Manus Knowledge UI/data
2. Manus Memory/internal context
3. Manus Tasks UI/data
4. Manus archived/completed tasks
5. Manus task files/outputs
6. Manus deployed websites list
7. Manus website URLs and settings
8. Website build/source folders
9. Manus generated files/downloads
10. Manus remote/persistent folders
11. Manus integrations/connectors status
12. Notion Memory Hub references
13. Mem0 references
14. prior KAP folders E2B/M1/M1C
15. memory-pipeline scripts/docs
16. session exporter/session extractor tools
17. local generated ZIPs/reports

---

## 4. Required Access Matrix

Create:

`KAP-WP2-M2-Manus-Access-Matrix.md`

Table columns:

| surface_id | surface_name | expected_content | current_access_method | accessible_now | acquired_already | missing_content | blocker | best_next_method | user_input_needed |
|---|---|---|---|---|---|---|---|---|---|

Use statuses:

- `ACCESSIBLE_NOW`
- `METADATA_ONLY`
- `BLOCKED_API`
- `BLOCKED_DOM`
- `BLOCKED_CONNECTOR`
- `USER_SCREENSHOT_REQUIRED`
- `USER_COPYPASTE_REQUIRED`
- `NOTION_REQUIRED`
- `UNKNOWN`

---

## 5. Required Remaining Work Map

Create:

`KAP-WP2-M2-Remaining-Manus-Work-Map.md`

Table columns:

| priority | work_item | source_surface | current_state | target_state | estimated_effort | dependency | next_mpm |
|---|---|---|---|---|---|---|---|

Priorities:

- P0 = required to finish Manus
- P1 = important but can follow after P0
- P2 = useful/peripheral
- P3 = optional

---

## 6. User Input Request Pack

Create:

`KAP-WP2-M2-User-Input-Request-Pack.md`

This must be written directly to Yannick.

For each requested user action, include:

| request_id | screen_to_open | action | preferred_format | exact_steps | why_needed | after_user_provides |
|---|---|---|---|---|---|---|

Possible requests:

1. Screenshot full Manus Knowledge list.
2. Open each Knowledge entry and copy-paste full content.
3. Screenshot Tasks list with filters.
4. Open P0/P1 tasks and copy-paste final output.
5. Download task files if UI allows.
6. Screenshot/deep open Websites page/card/settings.
7. Copy website URLs.
8. Export or share Notion Memory Hub if connector blocked.
9. Provide Notion DB/page links for Manus Memory Hub.
10. Provide any ZIPs downloaded from Manus.

Be exact. Do not say “send screenshots” generically.

---

## 7. Next MPM Recommendation

Create:

`KAP-WP2-M2-Recommended-Next-MPM.md`

Choose one:

- `RUN_WP2-M3_KNOWLEDGE_FULL_CAPTURE`
- `RUN_WP2-M4_TASKS_FULL_CAPTURE`
- `RUN_WP2-M5_WEBSITE_URL_RECOVERY`
- `RUN_WP2-M6_NOTION_MEMORY_HUB_AS_MANUS_ARCHIVE`
- `REQUEST_USER_INPUT_FIRST`
- `MANUS_SURFACE_COMPLETE_PROCEED_TO_M7_GATE`

Explain why.

---

## 8. Final Response Required

Return only:

1. execution status
2. root folder
3. surfaces inspected
4. accessible surfaces
5. metadata-only surfaces
6. blocked surfaces
7. user input required: yes/no
8. user input request file path
9. recommended next MPM
10. blockers

End with exactly:

> KAP WP2-M2 complete. Remaining Manus surface map ready for Architect review.

---
