# Manus Exclusion / Noise Candidates

> Y-OS / KAP Cognitive Architecture
> Gate: MANUS-HIGH-VALUE-DURABLE-OUTPUT-CENSUS-GATE
> Status: ACTIVE

---

## 1. Exclusion Criteria
Outputs are excluded from the durable knowledge base if they are:
- Raw chat transcripts without structured deliverables.
- Intermediate drafts that were explicitly superseded in the same session.
- Failed task outputs (e.g., script errors, connection timeouts).
- Duplicate requests resulting in identical artifacts.

## 2. Excluded Categories

### A. Raw Transcripts
- **Reason:** Low signal-to-noise ratio. The valuable decisions are already captured in Decision Threads or Gate Reports.
- **Action:** Retain in Manus history, do not ingest into KAP.

### B. Failed Tool Executions
- **Reason:** Dead ends.
- **Action:** If the failure led to an architectural change, record it in the `IMPASSE-REGISTRY.md`. Otherwise, ignore.

### C. Temporary Work Files
- **Reason:** Ephemeral.
- **Action:** Ignore files in `/tmp/` or temporary text buffers unless explicitly promoted to a durable path.
