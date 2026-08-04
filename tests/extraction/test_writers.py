"""Tests for transactional writers — Phase 4 Step 9."""

from pathlib import Path

import pytest

from extraction_pipeline.writers import (
    WriterError,
    atomic_write_json,
    atomic_write_markdown,
    resolve_output_path,
    validate_path_containment,
)


class TestPathContainment:
    def test_valid_containment(self) -> None:
        validate_path_containment(
            Path("/a/b/c/file.json"), Path("/a/b")
        )

    def test_path_outside_root(self) -> None:
        with pytest.raises(WriterError, match="outside allowed root"):
            validate_path_containment(
                Path("/etc/passwd"), Path("/a/b")
            )

    def test_symlink_escape(self, tmp_path: Path) -> None:
        root = tmp_path / "safe"
        root.mkdir()
        outside = tmp_path / "outside"
        outside.mkdir()
        link = root / "link"
        link.symlink_to(outside)
        with pytest.raises(WriterError, match="outside allowed root"):
            validate_path_containment(link / "file.json", root)


class TestAtomicWrites:
    def test_atomic_write_json(self, tmp_path: Path) -> None:
        root = tmp_path / "output"
        root.mkdir()
        path = root / "test.json"
        atomic_write_json({"key": "value"}, path, root)
        assert path.exists()
        content = path.read_text(encoding="utf-8")
        assert '"key": "value"' in content

    def test_atomic_write_markdown(self, tmp_path: Path) -> None:
        root = tmp_path / "output"
        root.mkdir()
        path = root / "test.md"
        atomic_write_markdown("# Title\n\nContent", path, root)
        assert path.exists()

    def test_no_partial_write_on_error(self, tmp_path: Path) -> None:
        """A write outside the allowed root must raise and leave no target or .tmp file."""
        root = tmp_path / "safe"
        root.mkdir()
        outside = tmp_path / "outside.json"
        with pytest.raises(WriterError):
            atomic_write_json({"x": 1}, outside, root)
        assert not outside.exists()
        assert not (tmp_path / "outside.json.tmp").exists()

    def test_resolve_output_path(self) -> None:
        path = resolve_output_path(
            Path("/workspace/extraction/20_drafts"),
            "exec-abc123",
            "inventory",
            "inventory.json",
        )
        expected = Path(
            "/workspace/extraction/20_drafts/runs/exec-abc123/inventory/inventory.json"
        )
        assert path == expected

    def test_resolve_output_path_empty_filename(self) -> None:
        """An empty filename must yield a directory path with no trailing file component."""
        path = resolve_output_path(
            Path("/workspace/extraction/20_drafts"),
            "exec-abc123",
            "inventory",
            "",
        )
        expected = Path(
            "/workspace/extraction/20_drafts/runs/exec-abc123/inventory"
        )
        assert path == expected
