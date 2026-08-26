"""Focused fail-closed preflight tests."""

import copy
from pathlib import Path
import subprocess
from unittest.mock import Mock

import pytest
import yaml

import extraction_pipeline.preflight as pf


PATHS = [
    "chapters/chapter2-IDN.qmd", "chapters/chapter3-GEO.qmd", "chapters/chapter4-DEM.qmd",
    "chapters/chapter5-LMR.qmd", "chapters/chapter6-UTL.qmd", "chapters/chapter7-DWL.qmd",
    "chapters/chapter8-CONS.qmd",
]


def manifest_data() -> dict:
    return {
        "manifest_version": "1.0",
        "repository": {"url": "https://github.com/GMD-hub/GMD-guidelines", "commit_sha": "a" * 40},
        "source_files": [
            {"path": path, "scope": "welfare-excluded" if "chapter8" in path else "included", "sha256": str(index) * 64}
            for index, path in enumerate(PATHS, 1)
        ],
        "supporting_files": [{"path": "docs/GMD_household_survey_harmonization.md", "scope": "supporting", "sha256": "8" * 64}],
        "governance": {"module_registry_version": "v1", "field_classification_version": "v1", "schema_version": "0.1", "gmd_version": "3.0"},
        "parser_contract": {"tool": "pandoc", "version": "3.1.12", "installation_method": "action@commit", "reader": "markdown", "writer": "json", "normalization_version": "1.0"},
        "output": {"root": "extraction/20_drafts/", "allowlist": ["extraction/20_drafts/runs/"]},
    }


def governance_data() -> dict:
    return {"schema_version": "0.1", "gmd_version": "3.0", "modules": [{"source_chapter": path} for path in PATHS[:6]]}


def write_configs(tmp_path: Path, manifest: dict | None = None, governance: dict | None = None) -> tuple[Path, Path]:
    manifest_path = tmp_path / "manifest.yaml"
    governance_path = tmp_path / "governance.yaml"
    manifest_path.write_text(yaml.safe_dump(manifest or manifest_data()), encoding="utf-8")
    governance_path.write_text(yaml.safe_dump(governance or governance_data()), encoding="utf-8")
    return manifest_path, governance_path


def pandoc_result(output: str = "pandoc 3.1.12\n") -> subprocess.CompletedProcess[str]:
    return subprocess.CompletedProcess(["pandoc", "--version"], 0, output, "")


def test_complete_synthetic_preflight_passes(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    paths = write_configs(tmp_path)
    run = Mock(return_value=pandoc_result())
    monkeypatch.setattr(pf.subprocess, "run", run)
    result = pf.run_preflight(*paths)
    assert result["supporting_files"][0]["scope"] == "supporting"
    run.assert_called_once_with(["pandoc", "--version"], shell=False, capture_output=True, text=True, timeout=10, check=False)


def test_preapproval_manifest_fails_schema_validation(tmp_path: Path) -> None:
    data = manifest_data()
    data["repository"]["commit_sha"] = None
    manifest = tmp_path / "preapproval-manifest.yaml"
    manifest.write_text(yaml.safe_dump(data), encoding="utf-8")
    with pytest.raises(pf.PreflightError, match="schema validation"):
        pf.load_manifest(manifest)


@pytest.mark.parametrize("label", ["manifest", "governance"])
def test_missing_and_directory_inputs_fail(tmp_path: Path, label: str) -> None:
    missing = tmp_path / "missing.yaml"
    directory = tmp_path / "directory"
    directory.mkdir()
    valid = write_configs(tmp_path)
    args = (missing, valid[1]) if label == "manifest" else (valid[0], missing)
    with pytest.raises(pf.PreflightError, match="not found"):
        pf.run_preflight(*args)
    args = (directory, valid[1]) if label == "manifest" else (valid[0], directory)
    with pytest.raises(pf.PreflightError, match="not a file"):
        pf.run_preflight(*args)


@pytest.mark.parametrize("content,message", [("- item\n", "YAML mapping"), ("x: [\n", "Invalid YAML")])
def test_bad_yaml_fails_with_stable_error(tmp_path: Path, content: str, message: str) -> None:
    manifest, governance = write_configs(tmp_path)
    manifest.write_text(content, encoding="utf-8")
    with pytest.raises(pf.PreflightError, match=message) as caught:
        pf.run_preflight(manifest, governance)
    if message == "Invalid YAML":
        assert caught.value.__cause__ is not None


@pytest.mark.parametrize("label", ["manifest", "governance"])
@pytest.mark.parametrize(
    "failure",
    [OSError("read failed"), UnicodeDecodeError("utf-8", b"x", 0, 1, "bad")],
)
def test_read_and_decode_errors_are_chained(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    label: str,
    failure: Exception,
) -> None:
    manifest, governance = write_configs(tmp_path)
    original_read = Path.read_text

    def fail_target(path: Path, *args: object, **kwargs: object) -> str:
        target = manifest if label == "manifest" else governance
        if path == target:
            raise failure
        return original_read(path, *args, **kwargs)

    monkeypatch.setattr(Path, "read_text", fail_target)
    with pytest.raises(pf.PreflightError, match="Unable to read") as caught:
        pf.run_preflight(manifest, governance)
    assert caught.value.__cause__ is failure


@pytest.mark.parametrize("mutation,message", [
    (lambda data: data["source_files"].reverse(), "exact governed order"),
    (lambda data: data["source_files"].append(copy.deepcopy(data["source_files"][0])), "Duplicate governed path"),
    (lambda data: data["source_files"][0].update(path="chapter2-IDN.qmd"), "exact governed order"),
    (lambda data: data["source_files"][0].update(scope="supporting"), "exact governed order"),
    (lambda data: data.update(supporting_files=[]), "canonical Markdown"),
])
def test_exact_source_contract_is_enforced(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, mutation: object, message: str) -> None:
    data = manifest_data()
    mutation(data)
    paths = write_configs(tmp_path, data)
    monkeypatch.setattr(pf.subprocess, "run", Mock(return_value=pandoc_result()))
    with pytest.raises(pf.PreflightError, match=message):
        pf.run_preflight(*paths)


def test_duplicate_across_collections_is_rejected() -> None:
    data = manifest_data()
    data["supporting_files"][0] = copy.deepcopy(data["source_files"][0])
    with pytest.raises(pf.PreflightError, match="Duplicate governed path"):
        pf.check_source_files(data)


@pytest.mark.parametrize("unsafe", ["/chapters/chapter2-IDN.qmd", "chapters/../chapter2-IDN.qmd"])
def test_unsafe_paths_are_rejected_before_contract_comparison(unsafe: str) -> None:
    data = manifest_data()
    data["source_files"][0]["path"] = unsafe
    with pytest.raises(pf.PreflightError, match="Unsafe governed path"):
        pf.check_source_files(data)


@pytest.mark.parametrize(
    "path",
    [
        "/extraction/20_drafts/runs",
        "extraction/20_drafts/../knowledge",
        "extraction/20_drafts-escape/runs",
        "extraction//20_drafts/runs",
        "extraction/20_drafts/./runs",
    ],
)
@pytest.mark.parametrize("field", ["root", "allowlist"])
def test_output_paths_reject_structural_escape(path: str, field: str) -> None:
    data = manifest_data()
    if field == "root":
        data["output"]["root"] = path
    else:
        data["output"]["allowlist"] = [path]
    with pytest.raises(pf.PreflightError, match="extraction/20_drafts or a descendant"):
        pf.check_output_allowlist(data)


@pytest.mark.parametrize(
    "path",
    ["extraction/20_drafts", "extraction/20_drafts/", "extraction/20_drafts/runs/INV-001"],
)
def test_output_paths_accept_exact_draft_root_and_descendants(path: str) -> None:
    data = manifest_data()
    data["output"] = {"root": path, "allowlist": [path]}
    pf.check_output_allowlist(data)


@pytest.mark.parametrize("key", ["schema_version", "gmd_version"])
def test_governance_blank_and_drift_fail(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, key: str) -> None:
    governance = governance_data()
    governance[key] = " "
    paths = write_configs(tmp_path, governance=governance)
    monkeypatch.setattr(pf.subprocess, "run", Mock(return_value=pandoc_result()))
    with pytest.raises(pf.PreflightError, match=f"Governance {key} must be nonblank"):
        pf.run_preflight(*paths)
    governance[key] = "9.9"
    paths = write_configs(tmp_path, governance=governance)
    with pytest.raises(pf.PreflightError, match=f"{key} mismatch"):
        pf.run_preflight(*paths)


def test_governance_module_order_drift_fails(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    governance = governance_data()
    governance["modules"].reverse()
    paths = write_configs(tmp_path, governance=governance)
    monkeypatch.setattr(pf.subprocess, "run", Mock(return_value=pandoc_result()))
    with pytest.raises(pf.PreflightError, match="module source paths"):
        pf.run_preflight(*paths)


@pytest.mark.parametrize("result,message", [
    (subprocess.CompletedProcess([], 1, "", "bad"), "command failed"),
    (pandoc_result(""), "Malformed"),
    (pandoc_result("pandoc 3.1.12.1.2\n"), "Malformed"),
    (pandoc_result("pandoc 3.1.13\n"), "version mismatch"),
    (pandoc_result("pandoc 3.1.12 suffix\n"), "Malformed"),
])
def test_parser_runtime_failures(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, result: subprocess.CompletedProcess[str], message: str) -> None:
    paths = write_configs(tmp_path)
    monkeypatch.setattr(pf.subprocess, "run", Mock(return_value=result))
    with pytest.raises(pf.PreflightError, match=message):
        pf.run_preflight(*paths)


@pytest.mark.parametrize("failure", [FileNotFoundError("pandoc"), subprocess.TimeoutExpired("pandoc", 10)])
def test_parser_process_failures_are_chained(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, failure: Exception) -> None:
    paths = write_configs(tmp_path)
    monkeypatch.setattr(pf.subprocess, "run", Mock(side_effect=failure))
    with pytest.raises(pf.PreflightError, match="Unable to execute") as caught:
        pf.run_preflight(*paths)
    assert caught.value.__cause__ is failure
