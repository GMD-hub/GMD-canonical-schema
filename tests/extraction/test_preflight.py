"""Preflight tests — Phase 1 Step 2."""

import copy
from pathlib import Path

import pytest
import yaml as _yaml

import extraction_pipeline.preflight as pf


MANIFEST_PATH = (
    Path(__file__).resolve().parents[2]
    / "extraction"
    / "config"
    / "source-manifest.v1.yaml"
)

ALL_SOURCE_FILES = [
    {"path": "chapter2-IDN.qmd", "scope": "included"},
    {"path": "chapter3-GEO.qmd", "scope": "included"},
    {"path": "chapter4-DEM.qmd", "scope": "included"},
    {"path": "chapter5-LMR.qmd", "scope": "included"},
    {"path": "chapter6-UTL.qmd", "scope": "included"},
    {"path": "chapter7-DWL.qmd", "scope": "included"},
    {"path": "chapter8-CONS.qmd", "scope": "welfare-excluded"},
]

BASE_MANIFEST = {
    "manifest_version": "1.0",
    "repository": {"url": "https://example.com/repo", "commit_sha": "a" * 40},
    "source_files": ALL_SOURCE_FILES,
    "parser_contract": {
        "tool": "pandoc", "version": "3.1.12",
        "reader": "markdown+pipe_tables+grid_tables+footnotes",
        "writer": "json",
        "normalization_version": "1.0",
    },
    "output": {
        "root": "extraction/20_drafts/runs/",
        "allowlist": ["extraction/20_drafts/runs/"],
    },
    "governance": {
        "module_registry_version": "v1",
        "schema_version": "0.1",
    },
}


def _base_manifest() -> dict:
    """Return a fresh deep copy of BASE_MANIFEST to prevent cross-test mutation."""
    return copy.deepcopy(BASE_MANIFEST)


class TestPreflightSuccess:
    def test_load_valid_manifest(self) -> None:
        if not MANIFEST_PATH.exists():
            pytest.skip("Source manifest not yet created")
        data = pf.load_manifest(MANIFEST_PATH)
        assert isinstance(data, dict)
        assert "manifest_version" in data

    def test_run_preflight_passes(self) -> None:
        if not MANIFEST_PATH.exists():
            pytest.skip("Source manifest not yet created")
        data = pf.load_manifest(MANIFEST_PATH)
        # If Pandoc version is null, the preflight is intentionally blocking.
        # This is expected until a human sets the approved version.
        if data["parser_contract"].get("version") is None:
            pytest.skip(
                "Pandoc version not yet set in manifest — human-gated precondition"
            )
        result = pf.run_preflight(MANIFEST_PATH)
        assert result is not None

    def test_run_preflight_passes_with_synthetic_manifest(self, tmp_path: Path) -> None:
        """Preflight must pass end-to-end with a complete synthetic manifest.

        This exercises the 'preflight passes' code path that is permanently
        skipped against the committed manifest (which has null version and
        commit_sha as human-gated preconditions).
        """
        manifest = tmp_path / "manifest.yaml"
        data = _base_manifest()
        manifest.write_text(_yaml.dump(data, sort_keys=True), encoding="utf-8")
        result = pf.run_preflight(manifest)
        assert result is not None
        assert result["manifest_version"] == "1.0"
        assert result["repository"]["commit_sha"] == "a" * 40


class TestPreflightSourceRejection:
    def test_missing_manifest_raises(self) -> None:
        nonexistent = MANIFEST_PATH.parent / "nonexistent-manifest.yaml"
        with pytest.raises(pf.PreflightError, match="not found"):
            pf.load_manifest(nonexistent)

    def test_invalid_scope_raises(self, tmp_path: Path) -> None:
        manifest = tmp_path / "manifest.yaml"
        data = _base_manifest()
        data["source_files"] = [{"path": "chapter2-IDN.qmd", "scope": "invalid-scope"}]
        manifest.write_text(_yaml.dump(data, sort_keys=True), encoding="utf-8")
        with pytest.raises(pf.PreflightError, match="Invalid scope"):
            pf.run_preflight(manifest)

    def test_missing_source_chapter_raises(self, tmp_path: Path) -> None:
        manifest = tmp_path / "manifest.yaml"
        data = _base_manifest()
        data["source_files"] = [{"path": "chapter2-IDN.qmd", "scope": "included"}]
        manifest.write_text(_yaml.dump(data, sort_keys=True), encoding="utf-8")
        with pytest.raises(pf.PreflightError, match="Required source chapters"):
            pf.run_preflight(manifest)

    def test_output_outside_allowlist_raises(self, tmp_path: Path) -> None:
        manifest = tmp_path / "manifest.yaml"
        data = _base_manifest()
        data["output"] = {
            "root": "knowledge/rules/",
            "allowlist": ["knowledge/rules/"],
        }
        manifest.write_text(_yaml.dump(data, sort_keys=True), encoding="utf-8")
        with pytest.raises(pf.PreflightError, match="under extraction/20_drafts"):
            pf.run_preflight(manifest)

    def test_duplicate_source_path_raises(self, tmp_path: Path) -> None:
        manifest = tmp_path / "manifest.yaml"
        data = _base_manifest()
        data["source_files"] = [
            {"path": "chapter2-IDN.qmd", "scope": "included"},
            {"path": "chapter2-IDN.qmd", "scope": "included"},
        ]
        manifest.write_text(_yaml.dump(data, sort_keys=True), encoding="utf-8")
        with pytest.raises(pf.PreflightError, match="Duplicate source file"):
            pf.run_preflight(manifest)

    def test_missing_parser_version_raises(self, tmp_path: Path) -> None:
        manifest = tmp_path / "manifest.yaml"
        data = _base_manifest()
        data["parser_contract"] = {
            "tool": "pandoc",
            "reader": "markdown", "writer": "json",
        }
        manifest.write_text(_yaml.dump(data, sort_keys=True), encoding="utf-8")
        with pytest.raises(pf.PreflightError, match="Parser contract missing"):
            pf.run_preflight(manifest)

    def test_missing_governance_raises(self, tmp_path: Path) -> None:
        manifest = tmp_path / "manifest.yaml"
        data = _base_manifest()
        data.pop("governance")
        manifest.write_text(_yaml.dump(data, sort_keys=True), encoding="utf-8")
        with pytest.raises(pf.PreflightError, match="governance"):
            pf.run_preflight(manifest)

    def test_empty_governance_raises(self, tmp_path: Path) -> None:
        manifest = tmp_path / "manifest.yaml"
        data = _base_manifest()
        data["governance"] = {}
        manifest.write_text(_yaml.dump(data, sort_keys=True), encoding="utf-8")
        with pytest.raises(pf.PreflightError, match="governance"):
            pf.run_preflight(manifest)

    def test_non_mapping_yaml_raises(self, tmp_path: Path) -> None:
        manifest = tmp_path / "manifest.yaml"
        manifest.write_text("- list\n- items\n", encoding="utf-8")
        with pytest.raises(pf.PreflightError, match="YAML mapping"):
            pf.run_preflight(manifest)

    @pytest.mark.parametrize(
        "missing_key",
        ["manifest_version", "repository", "source_files", "parser_contract", "output"],
    )
    def test_missing_each_required_key_raises(
        self, tmp_path: Path, missing_key: str
    ) -> None:
        manifest = tmp_path / "manifest.yaml"
        data = _base_manifest()
        data.pop(missing_key)
        manifest.write_text(_yaml.dump(data, sort_keys=True), encoding="utf-8")
        with pytest.raises(pf.PreflightError, match="missing required key"):
            pf.run_preflight(manifest)

    def test_null_commit_sha_raises(self, tmp_path: Path) -> None:
        """A null commit_sha must fail preflight — pipeline is not deterministic."""
        manifest = tmp_path / "manifest.yaml"
        data = _base_manifest()
        data["repository"]["commit_sha"] = None
        manifest.write_text(_yaml.dump(data, sort_keys=True), encoding="utf-8")
        with pytest.raises(pf.PreflightError, match="commit_sha is null"):
            pf.run_preflight(manifest)

    def test_short_commit_sha_raises(self, tmp_path: Path) -> None:
        """A non-40-hex commit_sha must fail preflight."""
        manifest = tmp_path / "manifest.yaml"
        data = _base_manifest()
        data["repository"]["commit_sha"] = "abc123"
        manifest.write_text(_yaml.dump(data, sort_keys=True), encoding="utf-8")
        with pytest.raises(pf.PreflightError, match="40-character hex"):
            pf.run_preflight(manifest)

    def test_branch_name_commit_sha_raises(self, tmp_path: Path) -> None:
        """A branch name in commit_sha must fail preflight — only SHAs accepted."""
        manifest = tmp_path / "manifest.yaml"
        data = _base_manifest()
        data["repository"]["commit_sha"] = "main"
        manifest.write_text(_yaml.dump(data, sort_keys=True), encoding="utf-8")
        with pytest.raises(pf.PreflightError, match="40-character hex"):
            pf.run_preflight(manifest)
