# Y-OS Repository Architecture Decision

> Decision ID: DEC-YOS-005
> Date: 2026-07-03 | Status: CONFIRMED

## Decision

**Use `yos-cognitive-os` as master control-plane repository. Use additional specialized repositories or submodules for heavy modules, code, memory vaults, source archives, and automation systems. Maintain a mandatory `REPO-REGISTRY.md` and machine-readable `repo_index.json` so agents can navigate all repos.**

---

## Options Evaluated

| Option | Description | Verdict |
|---|---|---|
| 1. Monorepo pur | Everything in one repo | REJECTED — too heavy long-term, poor separation |
| 2. Many small repos | Each module is a standalone repo | REJECTED — no master control plane, agents lost |
| 3. Master repo + Git submodules | Master references other repos as submodules | ACCEPTED (preferred) — clean separation, agent-navigable |
| 4. Master repo + Git subtree | External repo content integrated into master | ACCEPTABLE — simpler for agents, less clean for separation |
| 5. Master repo + external linked repos + registry | Master contains links, registry, paths, statuses | ACCEPTED (mandatory complement) — REPO-REGISTRY is required regardless |

## Recommended Architecture

```
yos-cognitive-os/          ← master control plane (this repo)
├── 00_Control_Plane/      ← doctrines, decisions, session captures
├── 01_Strategy/           ← strategic doctrine
├── 02_Architecture/       ← cognitive models, decisions
├── 03_Modules/KAP/        ← KAP module pointer (submodule or link to yj000018/KAP)
├── 05_Registries/         ← REPO-REGISTRY, MODULE-REGISTRY, etc.
├── 07_AI_Indexes/         ← repo_index.json, module_index.json
└── ...

yj000018/KAP               ← KAP module repo (standalone, linked from master)
yj000018/yos-memory-vault  ← future: durable memory / Obsidian-compatible
yj000018/yos-connectors    ← future: connector scripts and pipelines
yj000018/yos-automation    ← future: n8n / Playwright / workflows
```

## How Agents Navigate

1. Start at `07_AI_Indexes/repo_index.json` — machine-readable list of all repos with roles and URLs.
2. For doctrine: `00_Control_Plane/CANONICAL-DOCTRINE-REGISTRY.md`
3. For module location: `05_Registries/REPO-REGISTRY.md`
4. For KAP specifically: `03_Modules/KAP/` contains a pointer file linking to `yj000018/KAP`

## How KAP Fits as a YOS Module

KAP is referenced in `03_Modules/KAP/KAP-MODULE-POINTER.md` which contains:
- Link to `yj000018/KAP` repo
- Current KAP gate status
- KAP roadmap pointer
- KAP scope definition

KAP is not a submodule (to avoid submodule complexity for now) — it is a linked repo with a registry entry and a pointer file.

## Legacy Repos

All existing repos under `yj000018/` are inventoried in `05_Registries/REPO-REGISTRY.md` and `07_AI_Indexes/repo_index.json`. Legacy repos (Wild World, old KAP) are moved to `99_Legacy/` conceptually and marked in the registry.

## Tradeoffs

| Concern | Decision |
|---|---|
| Submodule complexity | Use pointer files + registry instead of Git submodules for now |
| Agent navigation | Mandatory repo_index.json + REPO-REGISTRY.md |
| Legacy repo inventory | All 36+ repos catalogued in registry |
| Monorepo vs split | Split, but master is the single entry point |
