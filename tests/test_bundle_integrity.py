import json
import subprocess
import sys
from pathlib import Path

from schema.frontmatter import load_markdown

from conftest import write_markdown


def test_compiled_bundle_has_commit_and_bodies(temp_repository: Path) -> None:
    result = subprocess.run(
        [sys.executable, "build/compile_bundle.py", "PER", "1995"],
        cwd=temp_repository,
        check=True,
        capture_output=True,
        text=True,
    )
    bundle_path = temp_repository / result.stdout.strip()
    bundle = json.loads(bundle_path.read_text(encoding="utf-8"))

    assert bundle["commit_hash"]
    artifacts = []
    for values in bundle["universal"].values():
        artifacts.extend(values)
    artifacts.extend(bundle["country"]["parameters"])
    artifacts.extend(bundle["country"]["exceptions"])
    assert artifacts
    assert all("body" in artifact for artifact in artifacts)


def test_compiled_bundle_applies_selectors(temp_repository: Path) -> None:
    path = (
        temp_repository
        / "country-parameters"
        / "countries"
        / "PER"
        / "parameters.md"
    )
    data, body = load_markdown(path)
    target = data["parameters"][0]
    target["selectors"] = {"survey_type": "income"}
    write_markdown(path, data, body)

    result = subprocess.run(
        [
            sys.executable,
            "build/compile_bundle.py",
            "PER",
            "1995",
            "--selector",
            "survey_type=consumption",
        ],
        cwd=temp_repository,
        check=True,
        capture_output=True,
        text=True,
    )
    bundle_path = temp_repository / result.stdout.strip()
    bundle = json.loads(bundle_path.read_text(encoding="utf-8"))

    assert bundle["selectors"] == {"survey_type": "consumption"}
    parameter_ids = [item["parameter_id"] for item in bundle["country"]["parameters"]]
    assert "PARAM-EDU-YEARS-BY-LEVEL" not in parameter_ids