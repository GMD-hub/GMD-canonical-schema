"""Evidence pipeline — Phase 5 Step 13 / Phase 6 Step 14.

Citation validation, evidence collection, and canonical Markdown emission.
"""

from typing import Any

from pydantic import ValidationError

from extraction_pipeline.hashing import hash_bytes
from extraction_pipeline.pandoc_ast import recover_line_bounds
from schema.extraction.evidence import (
    CitationInput,
    CitationValidation,
    CollectedEvidencePacket,
    VerifiedCitation,
)
from schema.extraction.manifest import ResolvedSource


class CanonicalizationError(ValueError):
    """A blocking canonicalization failure — required fields missing."""


class EvidenceValidationError(ValueError):
    """A citation or evidence packet failed proof-backed validation."""


class SourceCache:
    """Expose immutable source bytes from one verified proof."""

    def __init__(self, resolved_source: ResolvedSource) -> None:
        self._resolved_source = resolved_source

    def get_bytes(self, source_path: str) -> bytes | None:
        """Return verified bytes, or ``None`` for an unselected path."""
        try:
            return self._resolved_source.get_bytes(source_path)
        except KeyError:
            return None


def validate_citation(
    resolved_source: ResolvedSource,
    source_path: str,
    excerpt: str,
    expected_excerpt_sha256: str | None = None,
) -> CitationValidation:
    """Validate a single citation against pinned source bytes.

    Returns a :class:`CitationValidation` with the result.
    """
    if not isinstance(excerpt, str) or not excerpt.strip():
        return CitationValidation(valid=False, error="Citation excerpt must be nonblank")
    try:
        source_bytes = resolved_source.get_bytes(source_path)
    except KeyError:
        return CitationValidation(
            valid=False, error=f"Source file not found: {source_path}"
        )

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
    resolved_source: ResolvedSource,
    citations: list[dict[str, Any]],
) -> list[CitationValidation]:
    """Validate multiple citations, caching source file reads (P3.7).

    Groups citations by ``source_path`` and reads each file at most once
    via :class:`SourceCache`, avoiding the per-citation re-read that
    :func:`validate_citation` performs when called in a loop.

    Args:
        resolved_source: Verified source proof containing immutable bytes.
        citations: List of citation dicts, each with ``source_path``,
            ``excerpt``, and optionally ``expected_excerpt_sha256``.

    Returns:
        List of :class:`CitationValidation` results, one per citation.
    """
    cache = SourceCache(resolved_source)
    results: list[CitationValidation] = []

    for cit in citations:
        try:
            citation = CitationInput.model_validate(cit)
        except ValidationError:
            results.append(
                CitationValidation(valid=False, error="Invalid citation input")
            )
            continue
        source_path = citation.source_path
        excerpt = citation.excerpt
        expected_hash = citation.expected_excerpt_sha256

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
    resolved_source: ResolvedSource,
    inventory_item: dict,
) -> dict:
    """Collect evidence citations for a single inventory item.

    Validates that the item selects bytes in the exact source proof and records
    identities that orchestration can bind to that proof.
    """
    inventory_id = inventory_item.get("inventory_id")
    source_path = inventory_item.get("source_path")
    citations = inventory_item.get("citations", [])

    if not inventory_id:
        raise ValueError("inventory_item missing required 'inventory_id'")
    if not source_path:
        raise ValueError("inventory_item missing required 'source_path'")

    try:
        source_file = resolved_source.get_file(source_path)
    except KeyError as exc:
        raise FileNotFoundError(
            f"Source file not found for inventory item {inventory_id}: {source_path}"
        ) from exc

    if not isinstance(citations, list) or not citations:
        raise EvidenceValidationError(
            "inventory_item citations must be a non-empty list"
        )

    verified_citations: list[VerifiedCitation] = []
    for raw_citation in citations:
        try:
            citation = CitationInput.model_validate(raw_citation)
        except ValidationError as exc:
            raise EvidenceValidationError("Invalid citation input") from exc
        if citation.source_path != source_path:
            raise EvidenceValidationError(
                "Citation source_path must match the inventory source_path"
            )
        validation = validate_citation(
            resolved_source,
            citation.source_path,
            citation.excerpt,
            citation.expected_excerpt_sha256,
        )
        if not validation.valid:
            raise EvidenceValidationError(validation.error or "Citation is invalid")
        if validation.line_start is None or validation.line_end is None:
            raise EvidenceValidationError("Citation line bounds were not recovered")
        verified_citations.append(
            VerifiedCitation(
                citation_id=citation.citation_id,
                source_path=citation.source_path,
                excerpt=citation.excerpt,
                excerpt_sha256=citation.expected_excerpt_sha256,
                line_start=validation.line_start,
                line_end=validation.line_end,
            )
        )

    packet = CollectedEvidencePacket(
        inventory_id=inventory_id,
        source_path=source_path,
        source_sha256=source_file.sha256,
        source_blob_sha=source_file.blob_sha,
        source_commit_sha=resolved_source.repository.commit_sha,
        source_proof_sha256=resolved_source.proof_sha256(),
        citations=verified_citations,
    )
    return packet.model_dump(mode="json")


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
