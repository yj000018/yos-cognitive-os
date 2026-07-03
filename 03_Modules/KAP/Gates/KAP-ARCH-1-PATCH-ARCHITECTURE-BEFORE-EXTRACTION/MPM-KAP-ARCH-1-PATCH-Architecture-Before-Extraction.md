# MPM Full Body — KAP-ARCH-1-PATCH — Architecture Before Extraction

> **Source:** MPM-Full-Body-Capture-Pack-Bootstrap-Session.md (MPM-009)
> **Status:** FULL_BODY_PERSISTED
> **Capture date:** 2026-07-03

---

KAP-ARCH-1-PATCH — Architecture Before Extraction

**Capture status:** FULL  
**Notes:** Full body extracted from standalone Markdown file.


# MPM — KAP-ARCH-1-PATCH — Architecture Before Extraction

**Program:** KAP — Knowledge Assimilation Program  
**Sprint:** KAP-ARCH-1-PATCH — Architecture Before Extraction  
**Mode:** roadmap correction / gate hardening / anti-premature-extraction patch  
**Execution Partner:** Manus Desktop  
**Authority:** Yannick + ChatGPT Guardian Architect  
**Status:** Ready for execution  
**Style:** simple, robust, modular, extensible — no over-engineering  
**Core rule:** This is a patch sprint only. Do not acquire sources. Do not run WP2-MANUS-FINAL-BULK. Do not run WP2-NOTION. Do not run WP3. Do not launch bulk extraction. Patch KAP-ARCH-1 so the roadmap clearly prioritizes structure, protocols, registries, gates, roles, and connector design before extraction.

---

## 1. Execution Wrapper

Execute this patch now.

You are Manus executing under KAP / yOS architectural control.

Goal:

Patch KAP-ARCH-1 to remove any implication that the next urgent step is full extraction, bulk acquisition, or immediate WP3 preparation.

The current priority is:

> Build and validate the machine before feeding it the full corpus.

This means:

1. validate structures;
2. validate protocols;
3. validate registries;
4. validate agent/team roles;
5. validate connector and pipeline readiness;
6. validate Git/MD/Obsidian structure;
7. validate gates;
8. define progressive activation rules;
9. only then decide minimal targeted acquisitions.

Do not acquire anything.

Do not migrate Notion.

Do not run Manus bulk extraction.

Do not run WP3.

Do not push to Mem0.

Do not treat Notion as active repository.

Do not rewrite KAP-ARCH-1 from scratch.

Patch only what is needed.

---

## 2. Canonical Correction

KAP-ARCH-1 is accepted as the architecture consolidation base, but its recommended next sprint must be corrected.

The previous recommendation implied:

`WP2-MANUS-FINAL-BULK → WP2-NOTION → Gate 1 → WP3`

This is too extraction-oriented and too fast.

Correct canon:

`KAP-ARCH-1-PATCH → STRUCTURE-GATE → CONNECTOR-DESIGN-GATE → PHASE-1-SEED-PLAN → targeted acquisition only if approved`

Extraction is not urgent.

Building the machine is urgent.

---

## 3. Root Folder

Create:

`/home/ubuntu/KAP/00_Infrastructure/KAP-ARCH-1_PATCH_Architecture_Before_Extraction/`

Create subfolders:

- `00_REPORTS/`
- `01_ROADMAP_CORRECTION/`
- `02_STRUCTURE_GATE/`
- `03_CONNECTOR_DESIGN_GATE/`
- `04_PHASE1_SEED_PLAN/`
- `05_AGENT_ROLE_REGISTRY_PATCH/`
- `06_NO_EXTRACTION_POLICY/`
- `07_KAP_ARCH_1_PATCHED_STATUS/`
- `08_GIT_PROOF/`
- `09_READY_FOR_ARCHITECT_REVIEW/`

All reports must be Markdown.

All gates/registries/status files must also be JSON where useful.

---

## 4. Roadmap Correction

Create:

- `01_ROADMAP_CORRECTION/KAP-ARCH-1-PATCH-Roadmap-Correction.md`
- `01_ROADMAP_CORRECTION/KAP-ARCH-1-PATCH-Roadmap-Correction.json`

Purpose:

Correct the roadmap after KAP-ARCH-1.

Required table:

| old_step_or_implication | problem | corrected_step | reason |
|---|---|---|---|

Must explicitly supersede any implication that these are immediate next steps:

- WP2-MANUS-FINAL-BULK;
- WP2-NOTION migration;
- WP3 opening;
- full automatic extraction;
- bulk acquisition.

Corrected roadmap:

| order | step | purpose | acquisition_allowed | gate_required_before_next |
|---:|---|---|---|---|
| 1 | KAP-ARCH-1-PATCH | correct roadmap and harden anti-extraction policy | NO | Architect review |
| 2 | STRUCTURE-GATE | validate Git/MD/Obsidian structure, indexes, registries, folders | NO | structure pass |
| 3 | CONNECTOR-DESIGN-GATE | validate connector statuses and pipeline reuse decisions | NO | connector design pass |
| 4 | AGENT-ROLE-GATE | validate Team OS roles, Guardian Architect, Manus Executor, future agents | NO | role registry pass |
| 5 | PHASE-1-SEED-PLAN | decide minimal targeted Phase 1 acquisitions, not bulk | NO, planning only | Architect approval |
| 6 | TARGETED-WP2-SOURCE-SPRINTS | run approved minimal acquisitions only | YES, targeted only | source-specific gate |
| 7 | PHASE-1-GATE-REVIEW | decide if enough Phase 1 corpus exists for WP3 dry run | NO | all required Phase 1 gates |
| 8 | WP3-N1 DRY RUN | normalization dry run on limited approved corpus | YES, limited corpus only | Architect approval |

---

## 5. Structure Gate

Create:

- `02_STRUCTURE_GATE/KAP-ARCH-1-PATCH-Structure-Gate.md`
- `02_STRUCTURE_GATE/KAP-ARCH-1-PATCH-Structure-Gate.json`

Purpose:

Define the gate that validates the machine structure before any new acquisition.

Required checks:

| check | expected_condition | status | evidence | blocker |
|---|---|---|---|---|

Include at minimum:

1. Git/MD source-of-truth structure defined.
2. Obsidian consultation rules defined.
3. Notion frozen/decommission rule defined.
4. Mem0 semantic-only rule defined.
5. Source Registry exists.
6. Protocol Registry exists.
7. Pipeline Registry exists.
8. Connector Readiness Matrix exists.
9. Team OS / Agent Role location exists or is defined.
10. Guardian Architect role is stored in Git.
11. Git persistence rules are defined.
12. Folder/index conventions are defined.
13. No extraction has been launched during this patch.

Allowed status:

- PASS
- PASS_WITH_MINOR_GAPS
- FAIL_BLOCKING
- NOT_APPLICABLE

---

## 6. Connector Design Gate

Create:

- `03_CONNECTOR_DESIGN_GATE/KAP-ARCH-1-PATCH-Connector-Design-Gate.md`
- `03_CONNECTOR_DESIGN_GATE/KAP-ARCH-1-PATCH-Connector-Design-Gate.json`

Purpose:

Validate that sources/connectors/pipelines are designed before executing acquisition.

Required source family table:

| source_family | connector_status | pipeline_status | reuse_decision | extraction_allowed_now | reason | next_design_action |
|---|---|---|---|---|---|---|

Must include at least:

- Manus Sessions;
- Manus Skills;
- Manus Websites;
- Manus Internal Knowledge;
- Manus Tasks;
- Notion legacy;
- GitHub KAP;
- GitHub yOS/MyOS;
- Obsidian vaults;
- Mem0;
- ChatGPT exports;
- Claude exports;
- Gemini;
- Grok;
- Perplexity;
- local project folders;
- project assets/logos/docs;
- Readwise;
- YouTube playlists/favorites;
- email/calendar;
- Home Assistant;
- sensors/telemetry;
- browser history;
- shell history;
- secrets/tokens.

Extraction should be `NO` for all during this patch.

Use statuses:

- TESTED_WORKING
- DESIGNED_READY_TO_TEST
- PARTIAL_BLOCKER
- BLOCKED_AUTH
- BLOCKED_CONNECTOR
- DISABLED_BY_CHOICE
- DISABLED_BY_LOW_QUALITY
- DISABLED_BY_NON_USE
- DEFERRED_LATER
- DEFERRED_YOUNIVERSE
- DEFERRED_TELEMETRY
- EXCLUDED_BY_POLICY
- RESTRICTED_SECRET_SURFACE
- UNKNOWN_REVIEW_REQUIRED

---

## 7. Phase 1 Seed Plan

Create:

- `04_PHASE1_SEED_PLAN/KAP-ARCH-1-PATCH-Phase1-Seed-Plan.md`
- `04_PHASE1_SEED_PLAN/KAP-ARCH-1-PATCH-Phase1-Seed-Plan.json`

Purpose:

Define how to later choose the minimum useful seed corpus for yOS/MyOS self-knowledge, without bulk extraction.

This is a planning file only.

Required table:

| candidate_seed | purpose | source_family | why_needed | bulk_required | recommended_scope | approval_required |
|---|---|---|---|---|---|---|

Seed candidates may include:

- KAP-ARCH-1 outputs;
- WP0-CORE-1;
- WP1-R;
- Guardian Architect role definition;
- prior work audit;
- protocol registry;
- pipeline registry;
- connector readiness matrix;
- current Manus architecture reports;
- selected yOS/KAP project state files;
- selected existing protocol/pipeline reports.

Rules:

1. Seed corpus must be minimal.
2. Seed corpus must be enough for yOS to find/recover more.
3. Seed corpus must avoid bulk acquisition.
4. Seed corpus must be Git/MD first.
5. Seed corpus must preserve provenance.
6. Seed corpus is not WP3.
7. Seed corpus is not Mem0 injection.
8. Seed corpus must be approved before extraction.

---

## 8. Agent Role Registry Patch

Create:

- `05_AGENT_ROLE_REGISTRY_PATCH/KAP-ARCH-1-PATCH-Agent-Role-Registry-Patch.md`
- `05_AGENT_ROLE_REGISTRY_PATCH/KAP-ARCH-1-PATCH-Agent-Role-Registry-Patch.json`

Purpose:

Ensure the ChatGPT Guardian Architect role is linked into KAP-ARCH-1 and future Team OS consolidation.

Reference the existing role file:

`/home/ubuntu/KAP/00_Infrastructure/Team_OS/Agents/CHATGPT-Guardian-Architect.md`

Required table:

| role | tool_context | status | source_file | responsibility | future_merge_required |
|---|---|---|---|---|---|

Must include at minimum:

- ChatGPT Guardian Architect / Architecte des gardiens;
- Manus Executor;
- Mem0 Memory Layer;
- Obsidian Navigation Layer;
- future Connector Agents;
- future Pipeline Agents;
- future Gatekeeper / QA role if already defined or to be recovered.

If existing Team OS role registries are found, do not overwrite them. Create a patch note and mark `MERGE_REQUIRED`.

---

## 9. No Extraction Policy

Create:

- `06_NO_EXTRACTION_POLICY/KAP-ARCH-1-PATCH-No-Extraction-Policy.md`
- `06_NO_EXTRACTION_POLICY/KAP-ARCH-1-PATCH-No-Extraction-Policy.json`

Purpose:

Define a clear temporary policy:

> No new acquisition or bulk extraction until structure/protocol/connector gates are accepted.

Required policy statements:

1. No full automatic extraction now.
2. No Manus bulk archive now.
3. No Notion migration now.
4. No ChatGPT/Claude/Gemini/Grok/Perplexity acquisition now.
5. No YOUniverse personal data acquisition now.
6. No telemetry/sensor acquisition now.
7. No Mem0 injection now.
8. No WP3 now.
9. Only architecture/protocol/registry/gate work is allowed.
10. Any exception requires Architect approval and must be scoped as minimal targeted acquisition.

Required exception table:

| possible_exception | allowed_now | condition | approval_required |
|---|---|---|---|

---

## 10. KAP-ARCH-1 Patched Status

Create:

- `07_KAP_ARCH_1_PATCHED_STATUS/KAP-ARCH-1-PATCH-Patched-Status.md`
- `07_KAP_ARCH_1_PATCHED_STATUS/KAP-ARCH-1-PATCH-Patched-Status.json`

Must state:

1. KAP-ARCH-1 remains accepted as architecture base.
2. Recommended next sprint is corrected.
3. Extraction urgency is removed.
4. WP2-MANUS-FINAL-BULK is deferred behind Structure/Connector/Seed gates.
5. WP2-NOTION-DECOMMISSION is deferred behind Structure/Connector/Seed gates.
6. WP3 remains blocked.
7. Next immediate action after patch is Architect review, then Structure Gate / Connector Design Gate.
8. Git/MD remains source of truth.
9. Notion remains frozen legacy.
10. Obsidian remains consultation layer.
11. Mem0 remains future distilled semantic memory only.

---

## 11. Gates

Create:

- `09_READY_FOR_ARCHITECT_REVIEW/KAP-ARCH-1-PATCH-Gates.md`
- `09_READY_FOR_ARCHITECT_REVIEW/KAP-ARCH-1-PATCH-Gates.json`

Evaluate:

| gate | status | evidence | blocker | required_fix |
|---|---|---|---|---|

Required gates:

1. Roadmap Correction Gate.
2. Structure Gate Definition Gate.
3. Connector Design Gate Definition Gate.
4. Phase 1 Seed Plan Gate.
5. Agent Role Registry Patch Gate.
6. No Extraction Policy Gate.
7. Git Persistence Gate.
8. No Acquisition During Patch Gate.
9. WP3 Blocked Gate.

Allowed statuses:

- PASS
- PASS_WITH_MINOR_GAPS
- FAIL_BLOCKING
- NOT_APPLICABLE

---

## 12. Git Commit / Push

After all outputs are created:

From `/home/ubuntu/KAP/` run:

`git status`

Add only KAP-ARCH-1-PATCH outputs.

Commit message:

`KAP: patch roadmap to prioritize architecture before extraction`

Push to GitHub main.

Create:

`08_GIT_PROOF/KAP-ARCH-1-PATCH-Git-Proof.md`

Required table:

| repo_url | branch | previous_commit | new_commit | push_success | files_added | files_modified | blockers |
|---|---|---|---|---|---:|---:|---|

Do not commit raw tokens, cookies, secrets, restricted files, browser history, shell history, caches, temp files, or external raw corpus.

---

## 13. Required Outputs

Create at minimum:

1. `00_REPORTS/KAP-ARCH-1-PATCH-Execution-Report.md`
2. `01_ROADMAP_CORRECTION/KAP-ARCH-1-PATCH-Roadmap-Correction.md`
3. `01_ROADMAP_CORRECTION/KAP-ARCH-1-PATCH-Roadmap-Correction.json`
4. `02_STRUCTURE_GATE/KAP-ARCH-1-PATCH-Structure-Gate.md`
5. `02_STRUCTURE_GATE/KAP-ARCH-1-PATCH-Structure-Gate.json`
6. `03_CONNECTOR_DESIGN_GATE/KAP-ARCH-1-PATCH-Connector-Design-Gate.md`
7. `03_CONNECTOR_DESIGN_GATE/KAP-ARCH-1-PATCH-Connector-Design-Gate.json`
8. `04_PHASE1_SEED_PLAN/KAP-ARCH-1-PATCH-Phase1-Seed-Plan.md`
9. `04_PHASE1_SEED_PLAN/KAP-ARCH-1-PATCH-Phase1-Seed-Plan.json`
10. `05_AGENT_ROLE_REGISTRY_PATCH/KAP-ARCH-1-PATCH-Agent-Role-Registry-Patch.md`
11. `05_AGENT_ROLE_REGISTRY_PATCH/KAP-ARCH-1-PATCH-Agent-Role-Registry-Patch.json`
12. `06_NO_EXTRACTION_POLICY/KAP-ARCH-1-PATCH-No-Extraction-Policy.md`
13. `06_NO_EXTRACTION_POLICY/KAP-ARCH-1-PATCH-No-Extraction-Policy.json`
14. `07_KAP_ARCH_1_PATCHED_STATUS/KAP-ARCH-1-PATCH-Patched-Status.md`
15. `07_KAP_ARCH_1_PATCHED_STATUS/KAP-ARCH-1-PATCH-Patched-Status.json`
16. `08_GIT_PROOF/KAP-ARCH-1-PATCH-Git-Proof.md`
17. `09_READY_FOR_ARCHITECT_REVIEW/KAP-ARCH-1-PATCH-Gates.md`
18. `09_READY_FOR_ARCHITECT_REVIEW/KAP-ARCH-1-PATCH-Gates.json`
19. `09_READY_FOR_ARCHITECT_REVIEW/KAP-ARCH-1-PATCH-Architect-Review-Packet.md`
20. `09_READY_FOR_ARCHITECT_REVIEW/KAP-ARCH-1-PATCH-Recommended-Next-Step.md`

---

## 14. Final Response Required

Return only:

1. execution status;
2. root folder;
3. roadmap correction status;
4. structure gate status;
5. connector design gate status;
6. Phase 1 seed plan status;
7. agent role registry patch status;
8. no extraction policy status;
9. KAP-ARCH-1 patched status;
10. WP2-MANUS-FINAL-BULK allowed now: yes/no;
11. WP2-NOTION-DECOMMISSION allowed now: yes/no;
12. WP3 allowed now: yes/no;
13. files created;
14. commit hash;
15. push success;
16. GitHub URL;
17. blockers;
18. recommended next step.

End with exactly:

KAP-ARCH-1-PATCH complete. Architecture-before-extraction roadmap ready for Architect review.
