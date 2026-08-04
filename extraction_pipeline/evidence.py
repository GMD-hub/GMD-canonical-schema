"""Evidence pipeline — Phase 5 Step 13 / Phase 6 Step 14.

Citation validation, evidence collection, and canonical Markdown emission.
"""

from pathlib import Path
from typing import Any

from extraction_pipeline.hashing import hash_bytes
from extraction_pipeline.pandoc_ast import recover_line_bounds
from schema.extraction.evidence import CitationValidation


class CanonicalizationError(ValueError):
    """A blocking canonicalization failure — required fields missing."""


class SourceCache:
    """Cache source file bytes to avoid re-reading on every citation (P3.7).

    When validating ~40-100 citations against the same 7 chapter files,
    the same file was read and decoded once per citation. This cache reads
    each file at most once per cache lifetime (typically one extraction run).
    """

    def __init__(self, source_dir: Path) -> None:
        self._source_dir = source_dir
        self._cache: dict[str, bytes] = {}

    def get_bytes(self, source_path: str) -> bytes | None:
        """Return cached bytes for a source file, reading if necessary.

        Returns None if the file does not exist.
        """
        if source_path not in self._cache:
            file_path = self._source_dir / source_path
            if not file_path.exists():
                return None
            self._cache[source_path] = file_path.read_bytes()
        return self._cache[source_path]


def validate_citation(
    source_dir: Path,
    source_path: str,
    excerpt: str,
    expected_excerpt_sha256: str | None = None,
) -> CitationValidation:
    """Validate a single citation against pinned source bytes.

    Returns a :class:`CitationValidation` with the result.
    """
    file_path = source_dir / source_path
    if not file_path.exists():
        return CitationValidation(
            valid=False, error=f"Source file not found: {source_path}"
        )

    source_bytes = file_path.read_bytes()

    # Verify excerpt hash if provided (before searching, to fail fast)
    if expected_excerpt_sha256:
        actual_sha256 = hash_bytes(excerpt.encode("utf-8"))
        if actual_sha256 != expected_excerpt_sha256:
            return CitationValidation(
                valid=False,
                error=(
                    f"Excerpt SHA-256 mismatch: "
                    f"expected {expected_excerpt_sha256[:12]}..., "
                    f"got {actual_sha256[:12]}..."
                ),
            )

    # Recover line bounds (single source of truth — P2.17 dedup)
    bounds = recover_line_bounds(excerpt, source_bytes)
    if bounds is None:
        return CitationValidation(
            valid=False,
            error=f"Excerpt not found in {source_path}",
        )

    start_line, end_line = bounds
    return CitationValidation(
        valid=True,
        line_start=start_line,
        line_end=end_line,
        source_path=source_path,
    )


def validate_citations_batch(
    source_dir: Path,
    citations: list[dict[str, Any]],
) -> list[CitationValidation]:
    """Validate multiple citations, caching source file reads (P3.7).

    Groups citations by ``source_path`` and reads each file at most once
    via :class:`SourceCache`, avoiding the per-citation re-read that
    :func:`validate_citation` performs when called in a loop.

    Args:
        source_dir: Root directory of the resolved source checkout.
        citations: List of citation dicts, each with ``source_path``,
            ``excerpt``, and optionally ``expected_excerpt_sha256``.

    Returns:
        List of :class:`CitationValidation` results, one per citation.
    """
    cache = SourceCache(source_dir)
    results: list[CitationValidation] = []

    for cit in citations:
        source_path = cit.get("source_path", "")
        excerpt = cit.get("excerpt", "")
        expected_hash = cit.get("expected_excerpt_sha256")

        source_bytes = cache.get_bytes(source_path)
        if source_bytes is None:
            results.append(CitationValidation(
                valid=False, error=f"Source file not found: {source_path}"
            ))
            continue

        # Verify excerpt hash if provided
        if expected_hash:
            actual_sha256 = hash_bytes(excerpt.encode("utf-8"))
            if actual_sha256 != expected_hash:
                results.append(CitationValidation(
                    valid=False,
                    error=(
                        f"Excerpt SHA-256 mismatch: "
                        f"expected {expected_hash[:12]}..., "
                        f"got {actual_sha256[:12]}..."
                    ),
                ))
                continue

        # Recover line bounds
        bounds = recover_line_bounds(excerpt, source_bytes)
        if bounds is None:
            results.append(CitationValidation(
                valid=False,
                error=f"Excerpt not found in {source_path}",
            ))
            continue

        start_line, end_line = bounds
        results.append(CitationValidation(
            valid=True,
            line_start=start_line,
            line_end=end_line,
            source_path=source_path,
        ))

    return results


def collect_evidence(
    source_dir: Path,
    inventory_item: dict,
) -> dict:
    """Collect evidence citations for a single inventory item.

    Validates that the inventory item has the required keys and that the
    source file exists. Does not silently return unverified input —
    raises ``FileNotFoundError`` if the source file is missing.
    """
    inventory_id = inventory_item.get("inventory_id")
    source_path = inventory_item.get("source_path")
    citations = inventory_item.get("citations", [])

    if not inventory_id:
        raise ValueError("inventory_item missing required 'inventory_id'")
    if not source_path:
        raise ValueError("inventory_item missing required 'source_path'")

    # Verify the source file exists — fail loudly, not silently
    source_file = source_dir / source_path
    if not source_file.exists():
        raise FileNotFoundError(
            f"Source file not found for inventory item {inventory_id}: {source_path}"
        )

    return {
        "inventory_id": inventory_id,
        "source_path": source_path,
        "citations": citations,
    }


# Required frontmatter fields for canonical Markdown emission.
# Missing any of these is silent data corruption at the output boundary.
_REQUIRED_FRONTMATTER_FIELDS = (
    "variable_id",
    "canonical_label",
    "variable_name",
    "module_id",
    "gmd_version",
    "schema_version",
    "tier",
)


def canonicalize_to_markdown(candidate: dict, body_sections: list[str]) -> str:
    """Emit a canonical-shaped Markdown draft from a validated candidate.

    Raises :class:`CanonicalizationError` if any required frontmatter field
    is missing or empty — never silently emits empty values into a canonical
    draft.

    Note: ``extracted_on`` is volatile metadata per Decision 7 and is NOT
    written into the canonical Markdown body. It belongs in the run ledger
    only, so that canonical content is byte-identical across runs.
    """
    # Validate required fields — fail loudly (P2.8)
    missing = [
        field
        for field in _REQUIRED_FRONTMATTER_FIELDS
        if not candidate.get(field)
    ]
    if missing:
        raise CanonicalizationError(
            f"Cannot canonicalize: required frontmatter fields are missing "
            f"or empty: {', '.join(missing)}"
        )

    lines = [
        "---",
        f"variable_id: {candidate['variable_id']}",
        f"canonical_label: {candidate['canonical_label']}",
        f"variable_name: {candidate['variable_name']}",
        f"module_id: {candidate['module_id']}",
        f"gmd_version: {candidate['gmd_version']}",
        f"schema_version: {candidate['schema_version']}",
        f"status: {candidate.get('status', 'draft')}",
        f"tier: {candidate['tier']}",
        "---",
        "",
    ]

    for section in body_sections:
        heading = section.strip().lstrip("#").strip()
        lines.append(f"## {heading}")
        lines.append("")
        if heading == "Provenance":
            lines.append(f"- **Source**: {candidate.get('source_document', '')}")
            lines.append(f"- **Section**: {candidate.get('source_section', '')}")
            lines.append(f"- **Method**: {candidate.get('extraction_method', '')}")
            # NOTE: extracted_on is volatile metadata (Decision 7) — not in
            # canonical content. It goes in the run ledger only.
        lines.append("")

    return "\n".join(lines)
