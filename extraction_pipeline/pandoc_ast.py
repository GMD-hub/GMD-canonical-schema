"""Pandoc AST models — Phase 2 Step 4.

Models for Pandoc JSON AST nodes used in extraction. Provides deterministic
node IDs, line-bound recovery, and inventory-bearing region detection.
"""

import hashlib
import json
from pathlib import Path
from typing import Any


class PandocASTError(Exception):
    """A blocking Pandoc AST processing failure."""


def normalize_ast_node(node: dict[str, Any]) -> dict[str, Any]:
    """Normalize a Pandoc AST node for deterministic processing.

    Removes platform-dependent formatting and attribute ordering.
    """
    if not isinstance(node, dict):
        return node
    normalized: dict[str, Any] = {}
    for key in sorted(node.keys()):
        value = node[key]
        if isinstance(value, list):
            normalized[key] = [
                normalize_ast_node(item) if isinstance(item, dict) else item
                for item in value
            ]
        elif isinstance(value, dict):
            normalized[key] = normalize_ast_node(value)
        else:
            normalized[key] = value
    return normalized


def normalize_ast(ast: dict[str, Any]) -> dict[str, Any]:
    """Normalize the entire Pandoc AST for deterministic output."""
    return normalize_ast_node(ast)


def generate_node_id(source_path: str, ast_position: str, anchor: str) -> str:
    """Generate a deterministic node ID from source path, position, and anchor.

    The ID is stable across repeated parsing of the same source.
    """
    key = f"{source_path}::{ast_position}::{anchor}"
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


def parse_pandoc_json(json_path: Path) -> dict[str, Any]:
    """Load and validate a Pandoc JSON AST file."""
    if not json_path.exists():
        raise PandocASTError(f"Pandoc JSON file not found: {json_path}")
    try:
        ast = json.loads(json_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise PandocASTError(f"Invalid JSON in Pandoc output: {exc}") from exc
    if not isinstance(ast, dict) or "blocks" not in ast:
        raise PandocASTError("Pandoc JSON must be a dict with a 'blocks' key")
    return ast


def find_headings(ast: dict[str, Any]) -> list[dict[str, Any]]:
    """Extract all heading nodes from a Pandoc AST."""
    headings: list[dict[str, Any]] = []
    for i, block in enumerate(ast.get("blocks", [])):
        if isinstance(block, dict) and block.get("t") == "Header":
            headings.append({"index": i, "level": block["c"][0], "content": block["c"][2]})
    return headings


def find_tables(ast: dict[str, Any]) -> list[dict[str, Any]]:
    """Extract all table nodes from a Pandoc AST."""
    tables: list[dict[str, Any]] = []
    for i, block in enumerate(ast.get("blocks", [])):
        if isinstance(block, dict) and block.get("t") == "Table":
            tables.append({"index": i, "caption": block.get("c", [])})
    return tables


def is_inventory_bearing(ast: dict[str, Any]) -> bool:
    """Check if the AST contains inventory-bearing constructs.

    Returns True if headings or tables are found.
    """
    headings = find_headings(ast)
    tables = find_tables(ast)
    return len(headings) > 0 or len(tables) > 0


def recover_line_bounds(
    excerpt: str, source_bytes: bytes
) -> tuple[int, int] | None:
    """Recover one-based line bounds for an excerpt within source bytes.

    Returns (start_line, end_line) or None if the excerpt cannot be located.
    """
    source_str = source_bytes.decode("utf-8", errors="replace")
    idx = source_str.find(excerpt)
    if idx < 0:
        return None
    start_line = source_str[:idx].count("\n") + 1
    end_idx = idx + len(excerpt)
    end_line = source_str[:end_idx].count("\n") + 1
    return (start_line, end_line)
