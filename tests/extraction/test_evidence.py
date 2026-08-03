"""Tests for evidence validation — Phase 5 Step 13 / Phase 6 Step 14."""

from pathlib import Path

import pytest

from extraction_pipeline.evidence import (
    CanonicalizationError,
    SourceCache,
    canonicalize_to_markdown,
    collect_evidence,
    validate_citation,
    validate_citations_batch,
)


class TestValidateCitation:
    def test_valid_citation(self, tmp_path: Path) -> None:
        (tmp_path / "chapter2-IDN.qmd").write_text(
            "Age of household member in years.", encoding="utf-8"
        )
        result = validate_citation(tmp_path, "chapter2-IDN.qmd", "Age of household member")
        assert result.valid
        assert result.line_start == 1

    def test_excerpt_not_found(self, tmp_path: Path) -> None:
        (tmp_path / "chapter2-IDN.qmd").write_text("Some content", encoding="utf-8")
        result = validate_citation(tmp_path, "chapter2-IDN.qmd", "Missing text")
        assert not result.valid
        error: str = result.error or ""
        assert "not found" in error

    def test_file_not_found(self, tmp_path: Path) -> None:
        result = validate_citation(tmp_path, "missing.qmd", "text")
        assert not result.valid
        error: str = result.error or ""
        assert "not found" in error

    def test_hash_mismatch(self, tmp_path: Path) -> None:
        (tmp_path / "ch.qmd").write_text("real content", encoding="utf-8")
        result = validate_citation(
            tmp_path, "ch.qmd", "real content", expected_excerpt_sha256="a" * 64,
        )
        assert not result.valid
        error: str = result.error or ""
        assert "mismatch" in error

    def test_hash_match(self, tmp_path: Path) -> None:
        """A matching expected hash must return valid with line bounds."""
        from extraction_pipeline.hashing import hash_bytes

        excerpt = "real content"
        (tmp_path / "ch.qmd").write_text(excerpt, encoding="utf-8")
        expected = hash_bytes(excerpt.encode("utf-8"))
        result = validate_citation(
            tmp_path, "ch.qmd", excerpt, expected_excerpt_sha256=expected,
        )
        assert result.valid
        assert result.line_start == 1
        assert result.line_end == 1

    def test_multiline_excerpt_bounds(self, tmp_path: Path) -> None:
        """A multi-line excerpt must yield line_start < line_end."""
        source = "line 1\nline 2\nline 3\nline 4\n"
        (tmp_path / "ch.qmd").write_text(source, encoding="utf-8")
        excerpt = "line 2\nline 3"
        result = validate_citation(tmp_path, "ch.qmd", excerpt)
        assert result.valid
        assert result.line_start == 2
        assert result.line_end == 3


class TestSourceCache:
    """Tests for the source file cache (P3.7)."""

    def test_caches_file_content(self, tmp_path: Path) -> None:
        """The cache reads each file at most once."""
        (tmp_path / "ch.qmd").write_text("content here", encoding="utf-8")
        cache = SourceCache(tmp_path)
        # First read — loads from disk
        bytes1 = cache.get_bytes("ch.qmd")
        assert bytes1 is not None
        assert b"content here" in bytes1
        # Second read — returns from cache (no disk I/O)
        bytes2 = cache.get_bytes("ch.qmd")
        assert bytes2 is bytes1  # same object, not re-read

    def test_missing_file_returns_none(self, tmp_path: Path) -> None:
        cache = SourceCache(tmp_path)
        assert cache.get_bytes("nonexistent.qmd") is None

    def test_multiple_files_cached(self, tmp_path: Path) -> None:
        """Multiple source files are cached independently."""
        (tmp_path / "ch2.qmd").write_text("alpha", encoding="utf-8")
        (tmp_path / "ch3.qmd").write_text("beta", encoding="utf-8")
        cache = SourceCache(tmp_path)
        assert cache.get_bytes("ch2.qmd") == b"alpha"
        assert cache.get_bytes("ch3.qmd") == b"beta"
        assert cache.get_bytes("ch2.qmd") == b"alpha"


class TestValidateCitationsBatch:
    """Tests for batch citation validation with caching (P3.7)."""

    def test_batch_valid_citations(self, tmp_path: Path) -> None:
        """Multiple citations against the same file are validated with one read."""
        source = "line 1: age\nline 2: sex\nline 3: education\n"
        (tmp_path / "ch.qmd").write_text(source, encoding="utf-8")
        citations = [
            {"source_path": "ch.qmd", "excerpt": "line 1: age"},
            {"source_path": "ch.qmd", "excerpt": "line 2: sex"},
            {"source_path": "ch.qmd", "excerpt": "line 3: education"},
        ]
        results = validate_citations_batch(tmp_path, citations)
        assert len(results) == 3
        assert all(r.valid for r in results)
        assert results[0].line_start == 1
        assert results[1].line_start == 2
        assert results[2].line_start == 3

    def test_batch_missing_file(self, tmp_path: Path) -> None:
        """A citation referencing a missing file returns invalid."""
        citations = [{"source_path": "nonexistent.qmd", "excerpt": "text"}]
        results = validate_citations_batch(tmp_path, citations)
        assert len(results) == 1
        assert not results[0].valid
        assert "not found" in results[0].error

    def test_batch_excerpt_not_found(self, tmp_path: Path) -> None:
        """An excerpt not in the source returns invalid."""
        (tmp_path / "ch.qmd").write_text("real content", encoding="utf-8")
        citations = [{"source_path": "ch.qmd", "excerpt": "missing excerpt"}]
        results = validate_citations_batch(tmp_path, citations)
        assert len(results) == 1
        assert not results[0].valid
        assert "not found" in results[0].error

    def test_batch_multiple_files(self, tmp_path: Path) -> None:
        """Citations across multiple files are validated correctly."""
        (tmp_path / "ch2.qmd").write_text("alpha content", encoding="utf-8")
        (tmp_path / "ch3.qmd").write_text("beta content", encoding="utf-8")
        citations = [
            {"source_path": "ch2.qmd", "excerpt": "alpha content"},
            {"source_path": "ch3.qmd", "excerpt": "beta content"},
        ]
        results = validate_citations_batch(tmp_path, citations)
        assert len(results) == 2
        assert results[0].valid
        assert results[0].source_path == "ch2.qmd"
        assert results[1].valid
        assert results[1].source_path == "ch3.qmd"


class TestCollectEvidence:
    def test_collect_basic(self, tmp_path: Path) -> None:
        (tmp_path / "ch2.qmd").write_text("content", encoding="utf-8")
        item = {"inventory_id": "INV-IDN-001", "source_path": "ch2.qmd", "citations": ["CIT-001"]}
        result = collect_evidence(tmp_path, item)
        assert result == {
            "inventory_id": "INV-IDN-001",
            "source_path": "ch2.qmd",
            "citations": ["CIT-001"],
        }

    def test_collect_missing_inventory_id_raises(self, tmp_path: Path) -> None:
        """Missing inventory_id must raise, not silently default to empty."""
        (tmp_path / "ch2.qmd").write_text("content", encoding="utf-8")
        with pytest.raises(ValueError, match="inventory_id"):
            collect_evidence(tmp_path, {"source_path": "ch2.qmd"})

    def test_collect_missing_source_path_raises(self, tmp_path: Path) -> None:
        """Missing source_path must raise, not silently default to empty."""
        with pytest.raises(ValueError, match="source_path"):
            collect_evidence(tmp_path, {"inventory_id": "INV-001"})

    def test_collect_missing_source_file_raises(self, tmp_path: Path) -> None:
        """A missing source file must raise FileNotFoundError, not silently pass."""
        with pytest.raises(FileNotFoundError, match="not found"):
            collect_evidence(
                tmp_path,
                {"inventory_id": "INV-001", "source_path": "nonexistent.qmd"},
            )


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
