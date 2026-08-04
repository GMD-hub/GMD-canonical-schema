"""Transactional writes — Phase 4 Step 9.

Deterministic, contained, lineage-aware writer for extraction output.
"""

import json
from pathlib import Path

from loguru import logger


class WriterError(Exception):
    """A blocking write error."""


def validate_path_containment(path: Path, root: Path) -> None:
    """Ensure path is within the allowed root."""
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError as exc:
        raise WriterError(f"Path {path} is outside allowed root {root}") from exc


def atomic_write_json(data: object, path: Path, root: Path) -> None:
    """Write JSON data atomically within the allowed root.

    Uses ``sort_keys=True`` for deterministic key ordering (byte-identical
    reproducibility per G10). Does not use ``default=str`` — non-serializable
    types raise ``TypeError`` to enforce fail-loudly (P2.18).
    """
    validate_path_containment(path, root)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.parent / (path.name + ".tmp")
    tmp.write_text(
        json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )
    # On macOS, rename is atomic for files on the same filesystem
    tmp.rename(path)
    logger.info("JSON written atomically", path=str(path))


def atomic_write_markdown(content: str, path: Path, root: Path) -> None:
    """Write Markdown content atomically within the allowed root."""
    validate_path_containment(path, root)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.parent / (path.name + ".tmp")
    tmp.write_text(content, encoding="utf-8")
    tmp.rename(path)
    logger.info("Markdown written atomically", path=str(path))


def resolve_output_path(
    output_root: Path,
    execution_id: str,
    category: str,
    filename: str,
) -> Path:
    """Resolve a deterministic output path for the given category."""
    parts = [output_root, "runs", execution_id, category]
    if filename:
        parts.append(filename)
    path = Path(*parts)
    return path.resolve()
