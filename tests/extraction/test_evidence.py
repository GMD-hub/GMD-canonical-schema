"""Tests for evidence validation — Phase 5 Step 13 / Phase 6 Step 14."""

import hashlib

import pytest

from extraction_pipeline.evidence import (
    CanonicalizationError,
    SourceCache,
    canonicalize_to_markdown,
    collect_evidence,
    validate_citation,
    validate_citations_batch,
)
from schema.extraction.manifest import ResolvedSource


def _resolved_source(contents: dict[str, bytes]) -> ResolvedSource:
    entries = []
    for path, content in contents.items():
        git_blob = f"blob {len(content)}\0".encode("ascii") + content
        entries.append(
            {
                "path": path,
                "scope": "primary",
                "sha256": hashlib.sha256(content).hexdigest(),
                "blob_sha": hashlib.sha1(
                    git_blob,
                    usedforsecurity=False,
                ).hexdigest(),
                "content": content,
            }
        )
    return ResolvedSource(
        manifest_version="fixture-v1",
        manifest_sha256="a" * 64,
        repository={
            "url": "https://example.com/acme/source-repository",
            "commit_sha": "b" * 40,
        },
        parser_contract={
            "tool": "fixture-parser",
            "version": "1.2.3",
            "reader": "fixture-reader",
            "writer": "fixture-writer",
            "normalization_version": "normalization-v1",
        },
        governance={
            "module_registry_version": "registry-v1",
            "field_classification_version": "fields-v1",
            "schema_version": "schema-v1",
            "gmd_version": "guidelines-v1",
        },
        resolved_at="2026-08-30T12:00:00Z",
        source_files=entries,
        supporting_files=[],
        verified_sha256=True,
    )


def _citation(
    source_path: str,
    excerpt: str,
    citation_id: str = "CIT-001",
) -> dict[str, str]:
    return {
        "citation_id": citation_id,
        "source_path": source_path,
        "excerpt": excerpt,
        "expected_excerpt_sha256": hashlib.sha256(
            excerpt.encode("utf-8")
        ).hexdigest(),
    }


class TestValidateCitation:
    def test_valid_citation(self) -> None:
        proof = _resolved_source(
            {"docs/source.md": b"Age of household member in years."}
        )
        result = validate_citation(
            proof,
            "docs/source.md",
            "Age of household member",
        )
        assert result.valid
        assert result.line_start == 1

    def test_excerpt_not_found(self) -> None:
        proof = _resolved_source({"docs/source.md": b"Some content"})
        result = validate_citation(proof, "docs/source.md", "Missing text")
        assert not result.valid
        error: str = result.error or ""
        assert "not found" in error

    def test_file_not_found(self) -> None:
        proof = _resolved_source({"docs/source.md": b"Some content"})
        result = validate_citation(proof, "docs/missing.md", "text")
        assert not result.valid
        error: str = result.error or ""
        assert "not found" in error

    def test_hash_mismatch(self) -> None:
        proof = _resolved_source({"docs/source.md": b"real content"})
        result = validate_citation(
            proof,
            "docs/source.md",
            "real content",
            expected_excerpt_sha256="a" * 64,
        )
        assert not result.valid
        error: str = result.error or ""
        assert "mismatch" in error

    def test_hash_match(self) -> None:
        """A matching expected hash must return valid with line bounds."""
        from extraction_pipeline.hashing import hash_bytes

        excerpt = "real content"
        proof = _resolved_source({"docs/source.md": excerpt.encode("utf-8")})
        expected = hash_bytes(excerpt.encode("utf-8"))
        result = validate_citation(
            proof,
            "docs/source.md",
            excerpt,
            expected_excerpt_sha256=expected,
        )
        assert result.valid
        assert result.line_start == 1
        assert result.line_end == 1

    def test_multiline_excerpt_bounds(self) -> None:
        """A multi-line excerpt must yield line_start < line_end."""
        source = b"line 1\nline 2\nline 3\nline 4\n"
        proof = _resolved_source({"docs/source.md": source})
        excerpt = "line 2\nline 3"
        result = validate_citation(proof, "docs/source.md", excerpt)
        assert result.valid
        assert result.line_start == 2
        assert result.line_end == 3

    @pytest.mark.parametrize("excerpt", ["", " ", "\n"])
    def test_blank_excerpt_is_invalid(self, excerpt: str) -> None:
        proof = _resolved_source({"docs/source.md": b"content"})
        result = validate_citation(proof, "docs/source.md", excerpt)
        assert not result.valid
        assert "nonblank" in (result.error or "")


class TestSourceCache:
    """Tests for the source file cache (P3.7)."""

    def test_caches_file_content(self) -> None:
        """The cache returns the same immutable proof bytes."""
        proof = _resolved_source({"docs/source.md": b"content here"})
        cache = SourceCache(proof)
        bytes1 = cache.get_bytes("docs/source.md")
        assert bytes1 is not None
        assert b"content here" in bytes1
        bytes2 = cache.get_bytes("docs/source.md")
        assert bytes2 is bytes1

    def test_missing_file_returns_none(self) -> None:
        cache = SourceCache(_resolved_source({"docs/source.md": b"content"}))
        assert cache.get_bytes("docs/missing.md") is None

    def test_multiple_files_cached(self) -> None:
        """Multiple proof files remain independently addressable."""
        proof = _resolved_source(
            {"docs/source-a.md": b"alpha", "docs/source-b.md": b"beta"}
        )
        cache = SourceCache(proof)
        assert cache.get_bytes("docs/source-a.md") == b"alpha"
        assert cache.get_bytes("docs/source-b.md") == b"beta"
        assert cache.get_bytes("docs/source-a.md") == b"alpha"


class TestValidateCitationsBatch:
    """Tests for batch citation validation with caching (P3.7)."""

    def test_batch_valid_citations(self) -> None:
        """Multiple citations against the same file are validated with one read."""
        source = "line 1: age\nline 2: sex\nline 3: education\n"
        proof = _resolved_source({"docs/source.md": source.encode("utf-8")})
        citations = [
            _citation("docs/source.md", "line 1: age", "CIT-001"),
            _citation("docs/source.md", "line 2: sex", "CIT-002"),
            _citation("docs/source.md", "line 3: education", "CIT-003"),
        ]
        results = validate_citations_batch(proof, citations)
        assert len(results) == 3
        assert all(r.valid for r in results)
        assert results[0].line_start == 1
        assert results[1].line_start == 2
        assert results[2].line_start == 3

    def test_batch_missing_file(self) -> None:
        """A citation referencing a missing file returns invalid."""
        proof = _resolved_source({"docs/source.md": b"content"})
        citations = [_citation("docs/missing.md", "text")]
        results = validate_citations_batch(proof, citations)
        assert len(results) == 1
        assert not results[0].valid
        assert "not found" in results[0].error

    def test_batch_excerpt_not_found(self) -> None:
        """An excerpt not in the source returns invalid."""
        proof = _resolved_source({"docs/source.md": b"real content"})
        citations = [_citation("docs/source.md", "missing excerpt")]
        results = validate_citations_batch(proof, citations)
        assert len(results) == 1
        assert not results[0].valid
        assert "not found" in results[0].error

    def test_batch_multiple_files(self) -> None:
        """Citations across multiple files are validated correctly."""
        proof = _resolved_source(
            {
                "docs/source-a.md": b"alpha content",
                "docs/source-b.md": b"beta content",
            }
        )
        citations = [
            _citation("docs/source-a.md", "alpha content", "CIT-001"),
            _citation("docs/source-b.md", "beta content", "CIT-002"),
        ]
        results = validate_citations_batch(proof, citations)
        assert len(results) == 2
        assert results[0].valid
        assert results[0].source_path == "docs/source-a.md"
        assert results[1].valid
        assert results[1].source_path == "docs/source-b.md"


class TestCollectEvidence:
    def test_collect_basic(self) -> None:
        proof = _resolved_source({"docs/source.md": b"content"})
        item = {
            "inventory_id": "INV-001",
            "source_path": "docs/source.md",
            "citations": [_citation("docs/source.md", "content")],
        }
        result = collect_evidence(proof, item)
        assert result["inventory_id"] == "INV-001"
        assert result["source_path"] == "docs/source.md"
        assert result["source_sha256"] == hashlib.sha256(b"content").hexdigest()
        assert result["source_commit_sha"] == proof.repository.commit_sha
        assert result["source_proof_sha256"] == proof.proof_sha256()
        assert result["citations"][0]["citation_id"] == "CIT-001"
        assert result["citations"][0]["line_start"] == 1

    def test_collect_missing_inventory_id_raises(self) -> None:
        """Missing inventory_id must raise, not silently default to empty."""
        proof = _resolved_source({"docs/source.md": b"content"})
        with pytest.raises(ValueError, match="inventory_id"):
            collect_evidence(proof, {"source_path": "docs/source.md"})

    def test_collect_missing_source_path_raises(self) -> None:
        """Missing source_path must raise, not silently default to empty."""
        proof = _resolved_source({"docs/source.md": b"content"})
        with pytest.raises(ValueError, match="source_path"):
            collect_evidence(proof, {"inventory_id": "INV-001"})

    def test_collect_missing_source_file_raises(self) -> None:
        """A missing source file must raise FileNotFoundError, not silently pass."""
        proof = _resolved_source({"docs/source.md": b"content"})
        with pytest.raises(FileNotFoundError, match="not found"):
            collect_evidence(
                proof,
                {"inventory_id": "INV-001", "source_path": "docs/missing.md"},
            )

    def test_collect_rejects_invalid_or_empty_citations(self) -> None:
        proof = _resolved_source({"docs/source.md": b"committed content"})
        with pytest.raises(ValueError, match="non-empty"):
            collect_evidence(
                proof,
                {
                    "inventory_id": "INV-001",
                    "source_path": "docs/source.md",
                    "citations": [],
                },
            )
        with pytest.raises(ValueError, match="not found"):
            collect_evidence(
                proof,
                {
                    "inventory_id": "INV-001",
                    "source_path": "docs/source.md",
                    "citations": [
                        _citation("docs/source.md", "uncommitted claim")
                    ],
                },
            )

    def test_batch_rejects_missing_excerpt(self) -> None:
        proof = _resolved_source({"docs/source.md": b"content"})
        result = validate_citations_batch(
            proof,
            [{"citation_id": "CIT-001", "source_path": "docs/source.md"}],
        )
        assert not result[0].valid
        assert result[0].error == "Invalid citation input"


class TestCanonicalize:
    def test_basic_markdown(self) -> None:
        candidate = {
            "variable_id": "VAR-age",
            "canonical_label": "Age",
            "variable_name": "age",
            "module_id": "MOD-IDN",
            "gmd_version": "1.0",
            "schema_version": "0.1",
            "status": "draft",
            "tier": "1",
            "source_document": "GMD guidelines",
            "source_section": "chapter2-IDN.qmd",
            "extraction_method": "deterministic",
        }
        sections = [
            "## Summary", "## Value codes", "## Derivation",
            "## Source note", "## Prerequisites", "## Country parameters",
            "## External standards", "## Provenance",
        ]
        md = canonicalize_to_markdown(candidate, sections)
        assert md.startswith("---")
        assert "variable_id: VAR-age" in md
        assert "## Provenance" in md

    def test_missing_required_field_raises(self) -> None:
        """Missing required frontmatter fields must raise CanonicalizationError."""
        candidate = {
            "variable_id": "VAR-age",
            "canonical_label": "",  # empty — should raise
            "variable_name": "age",
            "module_id": "MOD-IDN",
            "gmd_version": "1.0",
            "schema_version": "0.1",
            "tier": "1",
        }
        with pytest.raises(CanonicalizationError, match="canonical_label"):
            canonicalize_to_markdown(candidate, ["## Summary"])

    def test_all_required_fields_missing_raises(self) -> None:
        """All required fields missing must raise with all field names."""
        with pytest.raises(CanonicalizationError, match="variable_id"):
            canonicalize_to_markdown({}, ["## Summary"])

    def test_no_extracted_on_in_output(self) -> None:
        """extracted_on must NOT appear in canonical Markdown (Decision 7, P2.20)."""
        candidate = {
            "variable_id": "VAR-age",
            "canonical_label": "Age",
            "variable_name": "age",
            "module_id": "MOD-IDN",
            "gmd_version": "1.0",
            "schema_version": "0.1",
            "tier": "1",
            "extracted_on": "2026-08-03T12:00:00Z",
        }
        md = canonicalize_to_markdown(candidate, ["## Provenance"])
        assert "Extracted on" not in md
        assert "extracted_on" not in md
