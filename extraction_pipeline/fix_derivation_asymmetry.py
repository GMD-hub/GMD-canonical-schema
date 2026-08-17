#!/usr/bin/env python3
"""Fix derivation graph asymmetries in extraction drafts.

For every pair where variable A declares derived_from [B], ensures that
variable B's derives_to list includes A.  Operates on .md files with YAML
frontmatter under extraction/20_drafts/ (excluding project-documentation/).

Round-trip preservation: uses regex surgery on the raw text so YAML comments,
ordering, and formatting are preserved.  Only the derives_to field is touched.

Usage:
    .venv/bin/python extraction_pipeline/fix_derivation_asymmetry.py          # dry-run
    .venv/bin/python extraction_pipeline/fix_derivation_asymmetry.py --apply  # write changes
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

DRAFTS_DIR = Path("extraction/20_drafts")
EXCLUDE_DIRS = {"project-documentation", "runs"}


def _load_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path} does not start with YAML front matter")
    front_matter, body = text[4:].split("\n---\n", 1)
    data = yaml.safe_load(front_matter)
    if not isinstance(data, dict):
        raise ValueError(f"{path} front matter must be a mapping")
    return data, text


def _collect_drafts(drafts_dir: Path) -> list[Path]:
    paths: list[Path] = []
    for p in sorted(drafts_dir.rglob("*.md")):
        rel = p.relative_to(drafts_dir)
        if rel.parts[0] in EXCLUDE_DIRS:
            continue
        paths.append(p)
    return paths


def _build_graph(
    drafts: list[Path],
) -> tuple[dict[str, dict], dict[str, Path], dict[str, str]]:
    """Parse all drafts and return (data_by_id, path_by_id, raw_text_by_id)."""
    data_by_id: dict[str, dict] = {}
    path_by_id: dict[str, Path] = {}
    raw_by_id: dict[str, str] = {}

    for path in drafts:
        try:
            data, raw = _load_frontmatter(path)
        except Exception as exc:
            print(f"  SKIP {path}: {exc}", file=sys.stderr)
            continue
        vid = data.get("variable_id", "")
        if not vid:
            continue
        data_by_id[vid] = data
        path_by_id[vid] = path
        raw_by_id[vid] = raw

    return data_by_id, path_by_id, raw_by_id


def _find_missing_edges(
    data_by_id: dict[str, dict],
) -> dict[str, list[str]]:
    """Return {target_id: [source_ids that should be in target's derives_to]}."""
    missing: dict[str, list[str]] = {}
    for vid, data in data_by_id.items():
        derived_from = data.get("derived_from") or []
        for source_id in derived_from:
            if source_id not in data_by_id:
                continue
            source_dt = set(data_by_id[source_id].get("derives_to") or [])
            if vid not in source_dt:
                missing.setdefault(source_id, []).append(vid)
    return missing


def _inject_derives_to_entries(raw: str, new_entries: list[str]) -> str:
    """Add entries to the derives_to field in raw frontmatter text.

    Handles three patterns:
      1. Inline empty:  derives_to: []
      2. Multiline list:
           derives_to:
             - VAR-aaa
             - VAR-bbb
      3. Null:          derives_to: null
    """
    NULL_TOKENS = {"null", "~", "Null", "NULL"}
    lines = raw.split("\n")
    result: list[str] = []
    i = 0
    injected = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("derives_to:") and not injected:
            after_colon = stripped[len("derives_to:"):].strip()
            indent = line[: len(line) - len(line.lstrip())]

            if after_colon == "[]" or after_colon in NULL_TOKENS:
                # Pattern 1 / 3: inline empty or null -> multiline
                result.append(f"{indent}derives_to:")
                for entry in new_entries:
                    result.append(f"{indent}  - {entry}")
                injected = True
                i += 1
                continue

            elif after_colon == "" or after_colon.startswith("["):
                # Pattern 2: multiline list (or inline non-empty)
                # Check if it's an inline non-empty list like [VAR-a, VAR-b]
                if after_colon.startswith("[") and after_colon != "[]":
                    # Inline list with entries — parse and rewrite, preserving
                    # existing order and appending only missing entries
                    entries_str = after_colon.strip("[]")
                    existing = [
                        e.strip().strip("'\"")
                        for e in entries_str.split(",")
                        if e.strip()
                    ]
                    combined = list(dict.fromkeys(existing + new_entries))
                    result.append(f"{indent}derives_to:")
                    for entry in combined:
                        result.append(f"{indent}  - {entry}")
                    injected = True
                    i += 1
                    continue

                # Multiline: collect existing entries, find end of list
                result.append(line)  # the "derives_to:" line
                i += 1
                existing_entries: list[str] = []
                item_indent: str | None = None  # detected from first existing item

                # Consume only list item lines (stop at blank or non-list)
                while i < len(lines):
                    next_line = lines[i]
                    next_stripped = next_line.strip()
                    if next_stripped.startswith("- "):
                        existing_entries.append(next_stripped[2:].strip())
                        if item_indent is None:
                            item_indent = next_line[: len(next_line) - len(next_line.lstrip())]
                        result.append(next_line)
                        i += 1
                    else:
                        break

                # Determine indent for new entries: match existing items, or
                # default to key indent + "  "
                if item_indent is not None:
                    new_indent = item_indent
                else:
                    new_indent = indent + "  "

                # Append new entries immediately after existing items
                existing_set = set(existing_entries)
                for entry in new_entries:
                    if entry not in existing_set:
                        result.append(f"{new_indent}- {entry}")

                injected = True
                continue

        result.append(line)
        i += 1

    return "\n".join(result)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fix derivation graph asymmetries in extraction drafts"
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write changes to files (default: dry-run, print only)",
    )
    parser.add_argument(
        "--drafts-dir",
        type=Path,
        default=DRAFTS_DIR,
        help="Drafts directory (default: extraction/20_drafts)",
    )
    args = parser.parse_args()

    drafts = _collect_drafts(args.drafts_dir)
    print(f"Loaded {len(drafts)} draft files")

    data_by_id, path_by_id, raw_by_id = _build_graph(drafts)
    print(f"Parsed {len(data_by_id)} variable specs")

    missing = _find_missing_edges(data_by_id)
    total_edges = sum(len(v) for v in missing.values())
    print(f"Found {total_edges} missing derivation edges across {len(missing)} variables")

    if not missing:
        print("No asymmetries found. Nothing to do.")
        return

    files_fixed = 0
    for target_id, source_ids in sorted(missing.items()):
        path = path_by_id[target_id]
        print(f"  {target_id} ({path.name}): needs +{len(source_ids)} in derives_to: {source_ids}")

        if args.apply:
            new_raw = _inject_derives_to_entries(raw_by_id[target_id], source_ids)
            if new_raw != raw_by_id[target_id]:
                path.write_text(new_raw, encoding="utf-8")
                files_fixed += 1
                print(f"    -> WRITTEN")
            else:
                print(f"    -> NO CHANGE (already present?)")

    if args.apply:
        print(f"\nDone: {files_fixed} files modified, {total_edges} missing edges added")
    else:
        print(f"\nDry-run complete. Use --apply to write {total_edges} edges to {len(missing)} files.")


if __name__ == "__main__":
    main()