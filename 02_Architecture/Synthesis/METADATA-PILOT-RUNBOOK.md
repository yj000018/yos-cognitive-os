# METADATA-PILOT-RUNBOOK

> Y-OS / KAP Cognitive Architecture
> Gate: PROCESS-DOCS-RUNBOOK-GATE
> Last Updated: 2026-07-03

## 1. Definition of a Metadata-Only Pilot

A metadata-only pilot is a non-invasive scan of a Source Instance designed to catalog available Source Objects without ingesting their internal content. It maps the terrain before extraction begins.

## 2. Strict Boundaries

**Allowed Actions:**
- List files, directories, databases, or tables.
- Read file names, titles, paths, and URLs.
- Read timestamps (created, modified).
- Read object types (markdown, json, pdf, page).
- Read structural relations (parent-child folders).

**Forbidden Actions:**
- Reading file bodies.
- Extracting text snippets.
- Summarizing content.
- Creating Source Fragments.
- Extracting Claims.

## 3. Execution by Source Channel

### A. Git Repositories
- Use `git ls-tree` or GitHub API `GET /repos/{owner}/{repo}/git/trees/{sha}?recursive=1`.
- Capture paths, blobs, and commit timestamps.

### B. Obsidian / Markdown
- Use filesystem `find` or `ls -R`.
- Capture `.md` file names, folder structure, and file creation dates.
- Do NOT `cat` or `read` the files.

### C. Notion
- Use Notion API `POST /v1/search` with `filter: { property: "object", value: "page" }`.
- Extract `id`, `title`, `url`, `created_time`, `last_edited_time`.
- Do NOT call `GET /v1/blocks/{block_id}/children`.

### D. ChatGPT Capture Packs / Manus Outputs
- If already in Git, read markdown headers (`#`, `##`) and frontmatter.
- Do NOT parse paragraphs.

### E. Generated Sites / Apps
- Perform Provenance Census: map URLs/routes to GitHub repos or Replit project IDs.
- Do NOT scrape site text.

## 4. Output Artifacts

The output of a Metadata Pilot must be a list of candidate Source Objects, which are then registered in `SOURCE-OBJECT-REGISTRY.md` with canonical `SO-*` IDs.

## 5. Blockers & Readiness

**Log a Blocker IF:**
- API rate limits are hit during listing.
- File count exceeds 10,000 (requires chunking strategy).
- Folder structure is cyclical/recursive.

**Ready for Content Pilot WHEN:**
- All objects are registered in `SOURCE-OBJECT-REGISTRY.md`.
- Guardian Architect approves the transition to Content Pilot for specific `SO-*` IDs.
