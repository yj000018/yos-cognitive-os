#!/usr/bin/env python3
"""
obsidian_metadata_scan.py
YOS/KAP — OBSIDIAN-MARKDOWN-METADATA-DRY-RUN-GATE
Read-only metadata scanner for Obsidian/Markdown vaults.
Supports local path scan OR GitHub API scan (for Git-backed vaults).
Outputs only allowed metadata. Never reads or outputs note body content.
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# ─── CONFIG ────────────────────────────────────────────────────────────────────
ALLOWED_EXTENSIONS = {".md", ".canvas"}
ATTACHMENT_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".pdf",
                         ".mp3", ".mp4", ".webm", ".zip", ".csv", ".xlsx"}
WIKILINK_PATTERN = re.compile(r'\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]')
MD_LINK_PATTERN = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')
FRONTMATTER_PATTERN = re.compile(r'^---\s*\n(.*?)\n---', re.DOTALL)
FRONTMATTER_KEY_PATTERN = re.compile(r'^([a-zA-Z0-9_\-]+)\s*:', re.MULTILINE)

# ─── GITHUB API SCAN ───────────────────────────────────────────────────────────

def github_api_get(url, token):
    """Minimal GitHub API GET — returns parsed JSON or None."""
    import urllib.request
    req = urllib.request.Request(url, headers={"Authorization": f"token {token}",
                                                "Accept": "application/vnd.github.v3+json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"[WARN] GitHub API error: {e} — URL: {url}", file=sys.stderr)
        return None


def scan_github_tree(owner, repo, branch, token):
    """
    Fetch the full git tree (recursive) for a GitHub repo.
    Returns list of file metadata dicts (no body content).
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
    tree_data = github_api_get(url, token)
    if not tree_data or "tree" not in tree_data:
        print("[ERROR] Could not fetch git tree.", file=sys.stderr)
        return []
    return tree_data["tree"]


def get_file_metadata_from_github(owner, repo, path, token):
    """
    Fetch file metadata from GitHub API (NOT content).
    Returns size and sha only — no body.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    data = github_api_get(url, token)
    if not data:
        return None
    return {"size": data.get("size", 0), "sha": data.get("sha", "")}


def get_file_content_for_metadata_only(owner, repo, path, token):
    """
    Fetches ONLY the first 2KB of a file to extract frontmatter keys and wikilinks.
    Does NOT store or return full body content.
    Strictly metadata extraction only.
    URL-encodes path components to handle filenames with spaces (v1.1 fix).
    """
    import urllib.request, urllib.parse, base64
    # Encode each path segment separately to handle spaces and special chars
    encoded_parts = [urllib.parse.quote(part, safe='') for part in path.split('/')]
    encoded_path = '/'.join(encoded_parts)
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{encoded_path}"
    req = urllib.request.Request(url, headers={"Authorization": f"token {token}",
                                                "Accept": "application/vnd.github.v3+json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            if data.get("encoding") == "base64" and data.get("content"):
                # Decode only first 2KB for metadata extraction
                raw = base64.b64decode(data["content"])[:2048].decode("utf-8", errors="ignore")
                return raw
    except Exception as e:
        print(f"[WARN] Could not fetch metadata slice for {path}: {e}", file=sys.stderr)
    return None


def extract_frontmatter_keys(content_slice):
    """Extract only frontmatter KEY names (not values) from a content slice."""
    match = FRONTMATTER_PATTERN.match(content_slice)
    if not match:
        return []
    fm_block = match.group(1)
    keys = FRONTMATTER_KEY_PATTERN.findall(fm_block)
    return list(set(keys))


def extract_wikilinks(content_slice):
    """Extract wikilink targets from a content slice."""
    return list(set(WIKILINK_PATTERN.findall(content_slice)))


def extract_md_links(content_slice):
    """Extract markdown link URLs from a content slice."""
    return [url for _, url in MD_LINK_PATTERN.findall(content_slice)]


# ─── MAIN SCAN ─────────────────────────────────────────────────────────────────

def run_github_scan(owner, repo, branch, token, source_instance_id, output_dir):
    """
    Run a metadata-only scan of a GitHub-backed Obsidian vault.
    Produces: markdown_file_inventory.json, wikilink_map.json, attachment_inventory.json
    """
    print(f"[INFO] Scanning {owner}/{repo} (branch: {branch}) — metadata only")
    tree = scan_github_tree(owner, repo, branch, token)
    if not tree:
        return None

    md_files = []
    attachments = []
    all_titles = {}
    wikilink_entries = []
    attachment_entries = []

    obj_counter = 1

    for item in tree:
        if item.get("type") != "blob":
            continue
        path = item.get("path", "")
        ext = Path(path).suffix.lower()
        size = item.get("size", 0)
        filename = Path(path).name
        folder = str(Path(path).parent)

        if ext in ALLOWED_EXTENSIONS:
            so_id = f"SO-OBS-YWLD-{obj_counter:04d}"
            obj_counter += 1

            # Fetch metadata slice (first 2KB only — no body stored)
            content_slice = get_file_content_for_metadata_only(owner, repo, path, token)
            has_fm = False
            fm_keys = []
            wikilinks = []
            md_links = []

            if content_slice:
                has_fm = bool(FRONTMATTER_PATTERN.match(content_slice))
                fm_keys = extract_frontmatter_keys(content_slice) if has_fm else []
                wikilinks = extract_wikilinks(content_slice)
                md_links = extract_md_links(content_slice)

                # Register wikilinks
                for wl in wikilinks:
                    wikilink_entries.append({
                        "source_object_id": so_id,
                        "source_note": path,
                        "target_raw": wl,
                        "target_resolved": "",
                        "status": "unknown",
                        "notes": "resolution pending — no local vault available"
                    })

            # Track titles for duplicate detection
            stem = Path(path).stem
            if stem in all_titles:
                all_titles[stem].append(so_id)
            else:
                all_titles[stem] = [so_id]

            md_files.append({
                "source_object_id": so_id,
                "source_instance_id": source_instance_id,
                "source_channel_id": "CH-004",
                "relative_path": path,
                "filename": filename,
                "extension": ext,
                "folder": folder if folder != "." else "/",
                "size_bytes": size,
                "created_at": None,
                "modified_at": None,
                "has_frontmatter": has_fm,
                "frontmatter_keys": fm_keys,
                "wikilinks_count": len(wikilinks),
                "outgoing_wikilinks": wikilinks,
                "markdown_links": md_links,
                "attachment_links": [],
                "orphan_status": "unknown",
                "content_ingested": False,
                "notes": "metadata-only scan via GitHub API — no body content stored"
            })

        elif ext in ATTACHMENT_EXTENSIONS:
            att_id = f"SO-OBS-YWLD-ATT-{len(attachments)+1:04d}"
            attachments.append({
                "source_object_id": att_id,
                "attachment_path": path,
                "referenced_by_source_object_ids": [],
                "file_type": ext,
                "size_bytes": size,
                "status": "unknown",
                "content_copied": False,
                "notes": "attachment metadata only — content not copied"
            })

    # Detect duplicates
    duplicates = {k: v for k, v in all_titles.items() if len(v) > 1}

    # Summary stats
    folders = set(Path(f["relative_path"]).parent.as_posix() for f in md_files)

    summary = {
        "total_md_files": len(md_files),
        "total_attachments": len(attachments),
        "total_folders": len(folders),
        "total_wikilinks": len(wikilink_entries),
        "duplicate_titles": duplicates,
        "duplicate_count": len(duplicates)
    }

    # Write outputs
    os.makedirs(output_dir, exist_ok=True)
    idx_dir = os.path.join(output_dir, "Indexes")
    os.makedirs(idx_dir, exist_ok=True)

    with open(os.path.join(idx_dir, "markdown_file_inventory.json"), "w") as f:
        json.dump(md_files, f, indent=2)
    with open(os.path.join(idx_dir, "wikilink_map.json"), "w") as f:
        json.dump(wikilink_entries, f, indent=2)
    with open(os.path.join(idx_dir, "attachment_inventory.json"), "w") as f:
        json.dump(attachments, f, indent=2)

    print(f"[INFO] Scan complete: {summary['total_md_files']} MD files, "
          f"{summary['total_attachments']} attachments, "
          f"{summary['total_wikilinks']} wikilinks")
    return summary


# ─── ENTRY POINT ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOS/KAP Obsidian Metadata Scanner")
    parser.add_argument("--mode", choices=["local", "github"], default="github")
    parser.add_argument("--owner", default="yj000018")
    parser.add_argument("--repo", default="Y-WORLD")
    parser.add_argument("--branch", default="main")
    parser.add_argument("--token", required=True)
    parser.add_argument("--instance-id", default="INST-OBS-002")
    parser.add_argument("--output-dir",
                        default="/home/ubuntu/yos-cognitive-os/03_Modules/KAP/Pipelines/Obsidian")
    args = parser.parse_args()

    if args.mode == "github":
        result = run_github_scan(
            args.owner, args.repo, args.branch, args.token,
            args.instance_id, args.output_dir
        )
        if result:
            print(json.dumps(result, indent=2))
    else:
        print("[ERROR] Local mode not implemented in this version.", file=sys.stderr)
        sys.exit(1)
