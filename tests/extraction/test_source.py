"""Tests for source resolution and hashing — Phase 2 Step 3."""

from pathlib import Path

import pytest

from extraction_pipeline.hashing import hash_bytes, hash_file, verify_file_hash
from extraction_pipeline.source import (
    SourceResolutionError,
    resolve_source,
    resolve_source_directory,
    verify_source_hashes,
)


class TestHashing:
    def test_hash_bytes_deterministic(self) -> None:
        data = b"hello extraction"
        assert hash_bytes(data) == hash_bytes(data)

    def test_hash_file_deterministic(self, tmp_path: Path) -> None:
        f = tmp_path / "test.txt"
        f.write_text("hello", encoding="utf-8")
        h1 = hash_file(f)
        h2 = hash_file(f)
        assert h1 == h2

    def test_different_content_different_hash(self, tmp_path: Path) -> None:
        f1 = tmp_path / "a.txt"
        f2 = tmp_path / "b.txt"
        f1.write_text("alpha", encoding="utf-8")
        f2.write_text("beta", encoding="utf-8")
        assert hash_file(f1) != hash_file(f2)

    def test_verify_file_hash_match(self, tmp_path: Path) -> None:
        f = tmp_path / "test.txt"
        f.write_text("verify me", encoding="utf-8")
        h = hash_file(f)
        assert verify_file_hash(f, h)

    def test_verify_file_hash_mismatch(self, tmp_path: Path) -> None:
        f = tmp_path / "test.txt"
        f.write_text("original", encoding="utf-8")
        assert not verify_file_hash(f, "a" * 64)

    def test_verify_file_hash_missing(self, tmp_path: Path) -> None:
        assert not verify_file_hash(tmp_path / "nonexistent.txt", "a" * 64)


class TestSourceResolution:
    @pytest.fixture
    def source_dir(self, tmp_path: Path) -> Path:
        d = tmp_path / "checkout"
        d.mkdir()
        for chapter in [
            "chapter2-IDN.qmd", "chapter3-GEO.qmd", "chapter4-DEM.qmd",
            "chapter5-LMR.qmd", "chapter6-UTL.qmd", "chapter7-DWL.qmd",
            "chapter8-CONS.qmd",
        ]:
            (d / chapter).write_text(f"Content of {chapter}", encoding="utf-8")
        return d

    @pytest.fixture
    def manifest(self) -> dict:
        return {
            "manifest_version": "1.0",
            "repository": {
                "url": "https://github.com/GMD-hub/GMD-guidelines",
                "commit_sha": "d46dc03d253764ad7bdef53f625d54fd2a0a9ea1",
            },
            "source_files": [
                {"path": "chapter2-IDN.qmd", "scope": "included"},
                {"path": "chapter3-GEO.qmd", "scope": "included"},
                {"path": "chapter4-DEM.qmd", "scope": "included"},
                {"path": "chapter5-LMR.qmd", "scope": "included"},
                {"path": "chapter6-UTL.qmd", "scope": "included"},
                {"path": "chapter7-DWL.qmd", "scope": "included"},
                {"path": "chapter8-CONS.qmd", "scope": "welfare-excluded"},
            ],
        }

    def test_resolve_directory(self, source_dir: Path, manifest: dict) -> None:
        result = resolve_source_directory(source_dir, manifest)
        assert result == source_dir.resolve()

    def test_missing_source_file(self, tmp_path: Path, manifest: dict) -> None:
        d = tmp_path / "partial"
        d.mkdir()
        (d / "chapter2-IDN.qmd").write_text("ok", encoding="utf-8")
        with pytest.raises(SourceResolutionError, match="not found"):
            resolve_source_directory(d, manifest)

    def test_source_path_is_directory_raises(self, tmp_path: Path, manifest: dict) -> None:
        """A manifest path pointing to a directory must raise, not silently pass."""
        d = tmp_path / "checkout"
        d.mkdir()
        for chapter in [
            "chapter3-GEO.qmd", "chapter4-DEM.qmd", "chapter5-LMR.qmd",
            "chapter6-UTL.qmd", "chapter7-DWL.qmd", "chapter8-CONS.qmd",
        ]:
            (d / chapter).write_text("ok", encoding="utf-8")
        # chapter2-IDN.qmd is a directory, not a file
        (d / "chapter2-IDN.qmd").mkdir()
        with pytest.raises(SourceResolutionError, match="not a file"):
            resolve_source_directory(d, manifest)

    def test_nonexistent_directory(self, manifest: dict) -> None:
        with pytest.raises(SourceResolutionError, match="does not exist"):
            resolve_source_directory(Path("/nonexistent/path"), manifest)

    def test_verify_hashes(self, source_dir: Path, manifest: dict) -> None:
        verified, all_verified = verify_source_hashes(source_dir, manifest)
        assert len(verified) == 7
        for entry in verified:
            assert entry.sha256 is not None
            assert len(entry.sha256) == 64
        # Manifest has null sha256 for all files → not verified against expected
        assert all_verified is False

    def test_verify_hashes_with_expected(self, source_dir: Path, manifest: dict) -> None:
        """When all expected hashes are set and match, all_verified is True."""
        for entry in manifest["source_files"]:
            entry["sha256"] = hash_file(source_dir / entry["path"])
        verified, all_verified = verify_source_hashes(source_dir, manifest)
        assert len(verified) == 7
        assert all_verified is True

    def test_hash_mismatch_raises(self, source_dir: Path, manifest: dict) -> None:
        # Set a wrong expected hash
        manifest["source_files"][0]["sha256"] = "a" * 64
        with pytest.raises(SourceResolutionError, match="SHA-256 mismatch"):
            verify_source_hashes(source_dir, manifest)

    def test_full_resolution_null_hashes(self, source_dir: Path, manifest: dict) -> None:
        """With null expected hashes, verified_sha256 must be False."""
        result = resolve_source(source_dir, manifest, "2026-08-03T00:00:00Z")
        assert not result.verified_sha256
        assert len(result.source_files) == 7
        assert result.repository.commit_sha == "d46dc03d253764ad7bdef53f625d54fd2a0a9ea1"

    def test_full_resolution_verified_hashes(self, source_dir: Path, manifest: dict) -> None:
        """When all expected hashes are set and match, verified_sha256 is True."""
        for entry in manifest["source_files"]:
            entry["sha256"] = hash_file(source_dir / entry["path"])
        result = resolve_source(source_dir, manifest, "2026-08-03T00:00:00Z")
        assert result.verified_sha256
        assert len(result.source_files) == 7
