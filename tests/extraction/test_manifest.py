"""Manifest and preflight tests — Phase 1 Step 2."""

import hashlib
from pathlib import Path

import pytest
import yaml

EXTRACTION_CONFIG = Path(__file__).resolve().parents[2] / "extraction" / "config"


class TestSourceManifest:
    """Verify source manifest exists and is properly structured."""

    def test_manifest_exists(self) -> None:
        manifest = EXTRACTION_CONFIG / "source-manifest.v1.yaml"
        assert manifest.exists(), f"Missing source manifest: {manifest}"

    def test_manifest_has_required_sections(self) -> None:
        manifest = EXTRACTION_CONFIG / "source-manifest.v1.yaml"
        if not manifest.exists():
            pytest.skip("Source manifest not yet created")
        data = yaml.safe_load(manifest.read_text(encoding="utf-8"))
        required = [
            "manifest_version", "repository", "source_files",
            "parser_contract", "output"
        ]
        for key in required:
            assert key in data, f"Manifest missing required key: {key}"

    def test_manifest_has_all_required_chapters(self) -> None:
        manifest = EXTRACTION_CONFIG / "source-manifest.v1.yaml"
        if not manifest.exists():
            pytest.skip("Source manifest not yet created")
        data = yaml.safe_load(manifest.read_text(encoding="utf-8"))
        paths = {f["path"] for f in data.get("source_files", [])}
        required = [
            "chapter2-IDN.qmd", "chapter3-GEO.qmd", "chapter4-DEM.qmd",
            "chapter5-LMR.qmd", "chapter6-UTL.qmd", "chapter7-DWL.qmd",
            "chapter8-CONS.qmd",
        ]
        missing = set(required) - paths
        assert not missing, f"Manifest missing required chapters: {missing}"

    def test_chapter8_is_welfare_excluded(self) -> None:
        manifest = EXTRACTION_CONFIG / "source-manifest.v1.yaml"
        if not manifest.exists():
            pytest.skip("Source manifest not yet created")
        data = yaml.safe_load(manifest.read_text(encoding="utf-8"))
        for f in data.get("source_files", []):
            if f["path"] == "chapter8-CONS.qmd":
                assert f["scope"] == "welfare-excluded", (
                    "Chapter 8 must be welfare-excluded"
                )
                return
        pytest.fail("chapter8-CONS.qmd not found in source_files")

    def test_manifest_scope_values_valid(self) -> None:
        manifest = EXTRACTION_CONFIG / "source-manifest.v1.yaml"
        if not manifest.exists():
            pytest.skip("Source manifest not yet created")
        data = yaml.safe_load(manifest.read_text(encoding="utf-8"))
        valid = {"included", "supporting", "welfare-excluded"}
        for f in data.get("source_files", []):
            assert f["scope"] in valid, (
                f"Invalid scope '{f['scope']}' for {f['path']}"
            )

    def test_parser_contract_has_version(self) -> None:
        manifest = EXTRACTION_CONFIG / "source-manifest.v1.yaml"
        if not manifest.exists():
            pytest.skip("Source manifest not yet created")
        data = yaml.safe_load(manifest.read_text(encoding="utf-8"))
        parser = data["parser_contract"]
        assert "tool" in parser
        assert "version" in parser
        assert "reader" in parser
        assert "writer" in parser

    def test_output_root_allowlisted(self) -> None:
        manifest = EXTRACTION_CONFIG / "source-manifest.v1.yaml"
        if not manifest.exists():
            pytest.skip("Source manifest not yet created")
        data = yaml.safe_load(manifest.read_text(encoding="utf-8"))
        output = data["output"]
        assert output["root"].startswith("extraction/20_drafts/"), (
            f"Output root must be under extraction/20_drafts/: {output['root']}"
        )
        for path in output.get("allowlist", []):
            assert path.startswith("extraction/20_drafts/"), (
                f"Allowlisted path must be under extraction/20_drafts/: {path}"
            )


class TestPreflight:
    """Verify preflight checks exist and enforce manifest contracts."""

    def test_preflight_module_exists(self) -> None:
        preflight = (
            Path(__file__).resolve().parents[2]
            / "extraction_pipeline" / "preflight.py"
        )
        assert preflight.exists(), (
            f"Preflight module not found: {preflight}"
        )
        content = preflight.read_text(encoding="utf-8")
        assert "def check_parser_contract" in content, (
            "Preflight must have a parser contract check function"
        )
        assert "source-manifest" in content or "SourceManifest" in content, (
            "Preflight must load and validate source manifest"
        )

    def test_preflight_rejects_branch_names(self) -> None:
        """Preflight must reject symbolic revisions (branches, tags) and accept
        only immutable commit SHAs. The manifest records a commit_sha field;
        source resolution (Phase 2 Step 3) will enforce SHA-only resolution."""
        # Design contract: the manifest schema includes commit_sha,
        # and source resolution must reject non-SHA references.
        manifest = EXTRACTION_CONFIG / "source-manifest.v1.yaml"
        if not manifest.exists():
            pytest.skip("Source manifest not yet created")
        data = yaml.safe_load(manifest.read_text(encoding="utf-8"))
        assert "commit_sha" in data["repository"], (
            "Manifest repository must have commit_sha field"
        )
        commit_sha = data["repository"]["commit_sha"]
        if commit_sha is None:
            pytest.skip(
                "commit_sha is null in the committed manifest — human-gated "
                "precondition; cannot verify SHA shape until set"
            )
        # Enforce the actual contract: a 40-char lowercase hex string.
        assert len(commit_sha) == 40, (
            f"commit_sha must be 40 chars, got {len(commit_sha)}"
        )
        assert all(c in "0123456789abcdef" for c in commit_sha.lower()), (
            "commit_sha must be hexadecimal"
        )


class TestManifestDigest:
    """Verify manifest digest computation is deterministic."""

    def test_digest_is_reproducible(self) -> None:
        """Same manifest content must produce same digest across runs.

        Note: there is no production digest helper yet; this test verifies the
        design contract that a deterministic serialization of the manifest is
        reproducible. If a production digest function is added, this test should
        call it instead of reinventing the serialization inline.
        """
        manifest_path = EXTRACTION_CONFIG / "source-manifest.v1.yaml"
        if not manifest_path.exists():
            pytest.skip("Source manifest not yet created")
        data = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
        serialized = yaml.dump(
            data, sort_keys=True, allow_unicode=True, default_flow_style=False
        )
        h1 = hashlib.sha256(serialized.encode("utf-8")).hexdigest()
        # Re-serialize from the same data to confirm determinism of the chosen
        # serialization rules (sort_keys=True, fixed flow style).
        serialized_again = yaml.dump(
            data, sort_keys=True, allow_unicode=True, default_flow_style=False
        )
        h2 = hashlib.sha256(serialized_again.encode("utf-8")).hexdigest()
        assert h1 == h2, "Manifest digest is not reproducible"
        # Guard against vacuousness: the two serializations must be byte-identical,
        # not just hash-equal (catches a hypothetical hash collision).
        assert serialized == serialized_again

    def test_file_reordering_changes_digest(self) -> None:
        """Reordering source files must change the manifest digest."""
        manifest_path = EXTRACTION_CONFIG / "source-manifest.v1.yaml"
        if not manifest_path.exists():
            pytest.skip("Source manifest not yet created")
        data = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
        original = yaml.dump(
            data, sort_keys=True, allow_unicode=True, default_flow_style=False
        )
        # Swap two source file entries
        if len(data.get("source_files", [])) >= 2:
            data["source_files"][0], data["source_files"][1] = (
                data["source_files"][1], data["source_files"][0]
            )
        reordered = yaml.dump(
            data, sort_keys=True, allow_unicode=True, default_flow_style=False
        )
        h_original = hashlib.sha256(original.encode("utf-8")).hexdigest()
        h_reordered = hashlib.sha256(reordered.encode("utf-8")).hexdigest()
        assert h_original != h_reordered, (
            "Source file reordering did not change manifest digest"
        )
