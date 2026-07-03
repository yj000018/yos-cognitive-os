# YOS/KAP Master Operating Protocol

> Y-OS / KAP Cognitive Architecture
> Gate: PROCESS-DOCS-RUNBOOK-GATE
> Last Updated: 2026-07-03

## 1. Operating Principles

1. **Acquisition is NOT Synthesis:** Acquiring a source does not make it truth.
2. **Memory is NOT Authority:** What an LLM remembers is not evidence. Evidence must be traced to a Source Object.
3. **Git is the Canonical Truth:** If it is not in Git/Markdown, it does not exist in the Control Plane.
4. **Provenance is Absolute:** Every Claim must link to a Source Fragment. Every Fragment must link to a Source Object.

## 2. Source Lifecycle & Minimum Safe Sequence

To process any source safely, the following sequence MUST be strictly respected:

1. **Source Identification:** Identify the source and its channel.
2. **Access Verification:** Verify access without ingesting content.
3. **Metadata-Only Scan:** Extract titles, paths, timestamps, and IDs.
4. **Source Object Registration:** Assign canonical `SO-*` ID in `SOURCE-OBJECT-REGISTRY.md`.
5. **Content Pilot (Controlled):** Extract limited content boundaries.
6. **Source Fragment Registration:** Assign canonical `SF-*` ID in `SOURCE-FRAGMENT-REGISTRY.md`.
7. **Claim Extraction:** Extract atomic claims from Fragments.
8. **Thought Line Linking:** Group Claims into thematic Thought Lines.
9. **Decision Thread Reconstruction:** Trace rationale and options.
10. **Contradiction/Supersession Review:** Flag conflicts.
11. **Current Best Synthesis:** Generate active doctrine (future gate).

## 3. Current Blocked Actions

- **NO FULL CORPUS SCANNING:** Do not scan entire Obsidian vaults or Notion workspaces.
- **NO MASS CONTENT INGESTION:** Content must be piloted fragment by fragment.
- **NO PREMATURE SYNTHESIS:** Do not merge sources into "Current Best" until explicitly authorized by a Synthesis Gate.

## 4. Roles

- **ChatGPT Guardian Architect:** Validates architecture, policies, and gate transitions. Approves human-review escalations.
- **Manus Executor:** Executes gates, performs metadata scans, manages registries, strictly follows runbooks.
- **Git:** The only source of truth.
- **Human Reviewer:** Resolves impasses, approves sensitive content extraction, validates active decisions.

## 5. Explicit Warnings

- **LLM Internal Knowledge:** Is HEURISTIC CONTEXT ONLY. It is not source evidence.
- **Mem0:** Is SIGNAL ONLY. It is a routing aid, not a primary source.
- **Generated Sites/Apps:** Require a provenance census (code/URL mapping) before any content can be used.

## 6. Runbook Architecture

This protocol governs the execution of the following runbooks:
1. `SOURCE-INTAKE-RUNBOOK.md`
2. `METADATA-PILOT-RUNBOOK.md`
3. `CLAIM-EXTRACTION-RUNBOOK.md`
4. `THOUGHT-LINE-SEEDING-RUNBOOK.md`
5. `DECISION-THREAD-RECONSTRUCTION-RUNBOOK.md`
6. `CONTRADICTION-SUPERSESSION-RUNBOOK.md`
7. `HUMAN-REVIEW-PROTOCOL.md`
