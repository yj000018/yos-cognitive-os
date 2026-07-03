# SOURCE-CHANNEL-REGISTRY

> Y-OS / KAP — Level 1: Source Channels
> A **Channel** is a platform, system, or tool family that hosts one or more Source Instances.
> See `SOURCE-INSTANCE-REGISTRY.md` for Level 2 (individual instances).
> See `KAP-SOURCE-MATRIX.md` for status matrix.
> See `SOURCE-PIPELINE-REGISTRY.md` for pipeline status.
> Last Updated: 2026-07-03
> **Living document — add new channels immediately on discovery.**

---

## Architecture

```
CHANNEL (this file — Level 1)
  └── SOURCE INSTANCE (SOURCE-INSTANCE-REGISTRY.md — Level 2)
        └── FRAGMENT → CLAIM → THOUGHT LINE → DECISION THREAD
```

---

## Channel Status Vocabulary

| Status | Meaning |
|---|---|
| `ACTIVE` | Channel confirmed, connector operational, acquisition possible |
| `PARTIAL` | Channel accessible but incomplete (missing instances, partial auth) |
| `BLOCKED` | Channel identified, access not yet possible — requires user action |
| `DEFERRED` | Out of scope for current phase — catalogued for future activation |
| `DEPRECATED` | No longer used |

## Channel Scope Vocabulary

| Scope | Meaning |
|---|---|
| `yos` | yOS cognitive architecture knowledge only |
| `youniverse` | Personal data, life data, behavioral data |
| `both` | Contains both yOS and personal content |

## Channel Phase Vocabulary

| Phase | Meaning |
|---|---|
| `phase-1` | Active in KAP Phase 1 — yOS knowledge consolidation |
| `phase-2` | Activated in Phase 2 — YOUniverse personal data expansion |
| `future` | Not yet planned, connector TBD |

---

## Channel Registry

| ch_id | Channel Name | Platform / System | Scope | Phase | Status | Known Instances | Connector | Auth | Notes |
|---|---|---|---|---|---|---|---|---|---|
| CH-001 | Git / GitHub | github.com/yj000018 | `yos` | phase-1 | `ACTIVE` | 41 repos | GitHub REST API v3 | PAT (KAP .env) | Primary code + docs channel. PAT confirmed working. |
| CH-002 | ChatGPT | chat.openai.com | `both` | phase-1 | `PARTIAL` | 2 packs in Git, 6+ pending | Manual export + Git | Manual | KAP GPT sessions. Parallel sessions pending export. |
| CH-003 | Manus | manus.im | `yos` | phase-1 | `ACTIVE` | 194 sessions (in Git) | Git (already exported) | None (in Git) | All durable outputs in yos-cognitive-os. |
| CH-004 | Obsidian / Markdown | Local Mac + Git-backed | `yos` | phase-1 | `PARTIAL` | 2 confirmed (Git), 7 unknown | GitHub API + Mac filesystem | PAT (Git) / Mac FUSE (local) | User confirmed 9 vaults. 7 paths unknown. |
| CH-005 | Notion | notion.so | `yos` | phase-1 | `PARTIAL` | 3 workspaces (1 active) | Notion REST API v1 | Integration key (KAP .env) | Primary structured knowledge. Census incomplete. |
| CH-006 | Mem0 | api.mem0.ai | `yos` | phase-1 | `ACTIVE` | 1 store (316 entries) | Mem0 REST API | API key (KAP .env) | Signal/index only. Not primary corpus. |
| CH-007 | Internal LLM Knowledge | All LLMs (prompt-based) | `both` | phase-1 | `PARTIAL` | All active LLMs | Structured prompt batch | N/A | Heuristic only. Deferred until taxonomy complete. |
| CH-008 | Other LLM Sessions | claude.ai, gemini, grok, perplexity | `both` | phase-1 | `BLOCKED` | Unknown | Manual export / prompt | Manual | No bulk export API. Prompt extraction after taxonomy. |
| CH-009 | Generated Sites (Manus / Lovable) | manus.im, lovable.dev | `yos` | phase-1 | `PARTIAL` | 3 in Git, unknown deployed | GitHub API + HTTP | PAT (Git) | Deployed site URLs not inventoried. |
| CH-010 | Generated Apps (Manus / Replit / Lovable, no Git) | replit.com, lovable.dev | `yos` | phase-1 | `BLOCKED` | Unknown | TBD | Platform login | No inventory. Code not in Git. |
| CH-011 | General Web | Any public URL | `both` | phase-1 | `DEFERRED` | N/A | HTTP / scraper | None | Out of scope for Phase 1. No yOS-specific content. |
| CH-012 | Google Drive | drive.google.com | `youniverse` | phase-2 | `DEFERRED` | Unknown | Google Drive API | OAuth2 | Personal/admin docs. No yOS content. Phase 2 only. |
| CH-013 | Generic Uploaded Files | User uploads (Manus session) | `both` | phase-1 | `PARTIAL` | Session-by-session | Manus upload mechanism | N/A | Files uploaded during sessions. Transient — must be persisted to Git immediately. |
| CH-014 | Unknown / Unidentified Legacy | Unknown | `both` | phase-1 | `BLOCKED` | Unknown | TBD | TBD | Legacy sources not yet identified. Requires discovery audit. |

---

## Channel Summary

| Phase | Scope | Total | ACTIVE | PARTIAL | BLOCKED | DEFERRED |
|---|---|---|---|---|---|---|
| phase-1 | yos/both | 12 | 3 | 5 | 3 | 1 |
| phase-2 | youniverse | 1 | 0 | 0 | 0 | 1 |
| — | — | **13 + 1 legacy** | **3** | **5** | **3** | **2** |

### ACTIVE Channels (3)
- **CH-001 Git/GitHub** — 41 repos, PAT ✅
- **CH-003 Manus** — 194 sessions in Git ✅
- **CH-006 Mem0** — 316 entries, API ✅

### PARTIAL Channels (5)
- **CH-002 ChatGPT** — 2 packs in Git, 6+ sessions pending
- **CH-004 Obsidian** — 2/9 vaults confirmed, 7 unknown
- **CH-005 Notion** — 1 workspace active, census incomplete
- **CH-007 Internal LLM** — accessible via prompt, deferred until taxonomy
- **CH-009 Generated Sites** — 3 in Git, deployed URLs unknown

### BLOCKED Channels (3)
- **CH-008 Other LLM Sessions** — no export API, manual only
- **CH-010 Generated Apps (no Git)** — no inventory
- **CH-014 Unknown Legacy** — discovery audit required
