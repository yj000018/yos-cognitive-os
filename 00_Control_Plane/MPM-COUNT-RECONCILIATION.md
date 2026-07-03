# MPM Count Reconciliation

> **Trigger:** Guardian Architect validation patch — FULL-BODY-CAPTURE-PATCH  
> **Date:** 2026-07-03  
> **Issue:** Inconsistent MPM counts across FULL-BODY-CAPTURE-PATCH report, SESSION-CAPTURE-REGISTRY, and UNCAPTURED-ITEMS-BACKLOG ("14 of 20 / 6 stubs" vs "14 full / 7 stubs")

---

## Canonical Taxonomy Decision

**Addenda and Handoff prompts are NOT counted as MPMs.**

| Artifact type | Definition | Counted as MPM? |
|---|---|---|
| **MPM (Manus Program Module)** | A gate execution prompt with Role, Rules, Required Actions, and Final Status options | ✅ YES |
| **Addendum** | A supplementary instruction appended to an MPM to strengthen or extend it | ❌ NO — separate artifact |
| **Handoff prompt** | A Manus execution handoff document (not a gate MPM) | ❌ NO — separate artifact |

---

## Canonical MPM Inventory — 17 MPMs total

### Gates (03_Modules/KAP/Gates/)

| # | MPM ID | Title | Status |
|---|---|---|---|
| 1 | MPM-WP2-M2 | Remaining Manus Surface Map & Human-Assisted Extraction Plan | ✅ FULL BODY |
| 2 | MPM-WP2-M3 | Full Manus Knowledge Capture | ✅ FULL BODY |
| 3 | MPM-WP2-M4 | Full Manus Tasks and Outputs Capture | ✅ FULL BODY |
| 4 | MPM-WP2-M5 | Manus Website URL Recovery and Content Deep Capture | ✅ FULL BODY |
| 5 | MPM-WP2-M6 | Manus Memory Hub / Notion Bridge Acquisition | ✅ FULL BODY |
| 6 | MPM-WP2-M7 | Manus Completion Gate and Capsule Closure | ✅ FULL BODY |
| 7 | MPM-WP2-MANUS-FINAL | Manus Branch Closure Gate | ✅ FULL BODY |
| 8 | MPM-KAP-ARCH-1 | Workflow, Pipeline & Protocol Consolidation | ✅ FULL BODY |
| 9 | MPM-KAP-ARCH-1-PATCH | Architecture Before Extraction | ✅ FULL BODY |
| 10 | MPM-STRUCTURE-GATE | KAP Machine Structure Validation | ✅ FULL BODY |
| 11 | MPM-CONNECTOR-DESIGN-GATE | Connector & Pipeline Design Validation | ✅ FULL BODY |
| 12 | MPM-EVOLUTIONARY-KNOWLEDGE-MERGE | Evolutionary Knowledge Merge Architecture Gate | ✅ FULL BODY |
| 13 | MPM-YOS-CONTROL-PLANE-BOOTSTRAP | YOS Control Plane Bootstrap + Session Doctrine Capture Gate | ✅ FULL BODY |
| 14 | MPM-SOURCE-FRAGMENT-MODEL | Source Fragment Model Gate | ✅ FULL BODY |
| 15 | MPM-AGENT-ROLE-GATE | Agent Role Gate + Manus Session Grab Metadata Census | ⏳ STUB ONLY |
| 16 | MPM-CONNECTOR-IMPLEMENTATION-GATE | Connector Implementation Gate | ⏳ STUB ONLY |
| 17 | MPM-PIPELINE-FEASIBILITY-GATE | Pipeline Feasibility Gate | ⏳ STUB ONLY |

### Pipelines (03_Modules/KAP/Pipelines/)

| # | MPM ID | Title | Status |
|---|---|---|---|
| 18 | MPM-OBSIDIAN-PIPELINE-VALIDATION-GATE | Obsidian Pipeline Validation Gate | ⏳ STUB ONLY |
| 19 | MPM-OBSIDIAN-PIPELINE-PATCH-GATE | Obsidian Pipeline Patch Gate | ⏳ STUB ONLY |
| 20 | MPM-NOTION-PIPELINE-CONTROLLED-EXECUTION-GATE | Notion Pipeline Controlled Execution Gate | ⏳ STUB ONLY |

**Total: 20 MPMs — 14 FULL BODY / 6 STUB ONLY**

---

## Separate Artifacts (NOT counted as MPMs)

| Artifact | Type | Status | Path |
|---|---|---|---|
| ADDENDUM-WP1-R — Source Lifecycle & Project Knowledge Phase Correction | Addendum | ✅ FULL BODY | `03_Modules/KAP/Gates/WP2-M2-REMAINING-MANUS-SURFACE-MAP/` |
| ADDENDUM — Mandatory Session Doctrine Capture and Git Persistence | Addendum | ✅ FULL BODY | `03_Modules/KAP/Gates/YOS-CONTROL-PLANE-BOOTSTRAP/` |
| ADDENDUM — Executive Feasibility Matrix | Addendum | ⏳ STUB ONLY | `03_Modules/KAP/Gates/PIPELINE-FEASIBILITY-GATE/` |
| Manus Handoff — YOS/KAP Session Capture Persistence v1 | Handoff | ✅ FULL BODY | `00_Control_Plane/` |
| Manus Handoff — YOS/KAP Session Capture Persistence v2 | Handoff | ✅ FULL BODY | `00_Control_Plane/` |

---

## Correction to Previous Report

The FULL-BODY-CAPTURE-PATCH report contained an inconsistency:

| Location | Previous count | Corrected count |
|---|---|---|
| Report summary line 1 | "14 of 20 / 6 stubs" | **14 FULL BODY / 6 STUB ONLY / 20 MPMs total** ✅ CORRECT |
| Report MPM table | "14 FULL BODY / 7 STUB ONLY" | ❌ INCORRECT — the Executive Feasibility Matrix Addendum was incorrectly counted as an MPM |

**Root cause:** The PIPELINE-FEASIBILITY-GATE Addendum (Executive Feasibility Matrix) was listed in the MPM table as a separate entry, inflating the stub count to 7. It is an addendum, not an MPM.

**Canonical answer: 20 MPMs — 14 FULL BODY — 6 STUB ONLY**

---

## Files Requiring Update

- `00_Control_Plane/Session_Captures/UNCAPTURED-ITEMS-BACKLOG.md` — MPM table corrected (remove Addendum row)
- `05_Registries/SESSION-CAPTURE-REGISTRY.md` — notes updated
