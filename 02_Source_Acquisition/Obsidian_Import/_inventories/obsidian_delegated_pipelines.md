# Obsidian Delegated Pipeline Registry

**Gate:** OBSIDIAN-FINAL-SOURCE-SURFACE-MAP-GATE  
**Version:** v1.0  
**Date:** 2026-07-04  

---

## Delegated Pipeline Registry

| Surface | Delegated Pipeline | Reason | Next Gate |
|---|---|---|---|
| Y-World GitHub | GitHub Pipeline | GitHub repo — not an Obsidian vault. Current likely primary Y-World source, to be validated by GitHub gate. | GITHUB-SOURCE-METADATA-PILOT-GATE (in progress) |
| GDrive Y-OS Folders (01_Y_OS_CORE, Y-OS, yOS, YOS Vision) | GDrive Y-OS Pipeline | Fragmented GDrive folders — no confirmed `.obsidian` structure. Not Obsidian vaults. | GDRIVE-YOS-METADATA-COMPARISON-GATE |
| GDrive Obsidian Vault 1 & 2 | GDrive Backup Pipeline (future) | Possible LUDIVINE backups on GDrive. Excluded from Obsidian pipeline unless backup review authorized. | GDRIVE-OBSIDIAN-BACKUP-REVIEW-GATE (future, optional) |

---

## Clarification Notes

The GDrive Y-OS folders (`01_Y_OS_CORE`, `Y-OS`, `yOS`, `YOS Vision`) are delegated to the GDrive Y-OS pipeline because no `.obsidian` configuration folder was observed in any of them during metadata profiling. They may contain Markdown files, but they are not confirmed Obsidian vaults and must be handled under the GDrive fragmentation resolution pipeline.

The Y-World GitHub repository contains Markdown files and a `compile-graph.yml` workflow, but it is a Git repository, not an Obsidian vault. It must be handled under the GitHub pipeline and must not be merged with the iCloud Y-World Obsidian vault.
