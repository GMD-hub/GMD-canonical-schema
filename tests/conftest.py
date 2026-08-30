import shutil
import subprocess
from pathlib import Path

import pytest
import yaml

from extraction_pipeline.hashing import hash_bytes
from schema.frontmatter import load_markdown


ROOT = Path(__file__).resolve().parents[1]
SOURCE_REPOSITORY_URL = "https://example.com/acme/source-fixture"


def write_markdown(path: Path, data: dict, body: str) -> None:
    front_matter = yaml.safe_dump(data, sort_keys=False, allow_unicode=False).rstrip()
    path.write_text(f"---\n{front_matter}\n---\n\n{body}", encoding="utf-8")


@pytest.fixture
def temp_repository(tmp_path: Path) -> Path:
    repository = tmp_path / "repository"
    repository.mkdir()
    for relative_path in ["build", "country-parameters", "knowledge", "schema"]:
        shutil.copytree(
            ROOT / relative_path,
            repository / relative_path,
            ignore=shutil.ignore_patterns("__pycache__", "output"),
        )

    # The production repository has unresolved variable references. Remove them
    # only in the disposable fixture so focused country-layer tests start valid.
    for filename in ["VAR-educat4.md", "VAR-educy.md"]:
        path = repository / "knowledge" / "variables" / "dem" / filename
        data, body = load_markdown(path)
        data["derived_from"] = []
        data["derives_to"] = []
        data["prerequisites"] = []
        write_markdown(path, data, body)

    subprocess.run(["git", "init", "--quiet"], cwd=repository, check=True)
    subprocess.run(
        ["git", "config", "user.email", "tests@example.invalid"],
        cwd=repository,
        check=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "CVS Tests"], cwd=repository, check=True
    )
    subprocess.run(["git", "add", "."], cwd=repository, check=True)
    subprocess.run(
        ["git", "commit", "--quiet", "-m", "test fixture"],
        cwd=repository,
        check=True,
    )
    return repository


@pytest.fixture
def source_repository(tmp_path: Path) -> dict[str, object]:
    """Create a generic Git source repository and complete source policy."""
    repository = tmp_path / "source-repository"
    repository.mkdir()
    contents = {
        "docs/source.md": b"immutable source bytes\n",
        "references/context.txt": b"supporting context\n",
    }
    for relative_path, content in contents.items():
        target = repository / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)

    subprocess.run(["git", "init", "--quiet"], cwd=repository, check=True)
    subprocess.run(
        ["git", "config", "user.email", "tests@example.invalid"],
        cwd=repository,
        check=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "Source Proof Tests"],
        cwd=repository,
        check=True,
    )
    subprocess.run(
        ["git", "remote", "add", "origin", SOURCE_REPOSITORY_URL],
        cwd=repository,
        check=True,
    )
    subprocess.run(["git", "add", "."], cwd=repository, check=True)
    subprocess.run(
        ["git", "commit", "--quiet", "-m", "source fixture"],
        cwd=repository,
        check=True,
    )
    commit = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repository,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    manifest = {
        "manifest_version": "fixture-v1",
        "repository": {"url": SOURCE_REPOSITORY_URL, "commit_sha": commit},
        "source_files": [
            {
                "path": "docs/source.md",
                "scope": "primary",
                "sha256": hash_bytes(contents["docs/source.md"]),
            }
        ],
        "supporting_files": [
            {
                "path": "references/context.txt",
                "scope": "supporting",
                "sha256": hash_bytes(contents["references/context.txt"]),
            }
        ],
        "governance": {
            "module_registry_version": "registry-fixture-v1",
            "field_classification_version": "fields-fixture-v1",
            "schema_version": "schema-fixture-v1",
            "gmd_version": "guidelines-fixture-v1",
        },
        "parser_contract": {
            "tool": "fixture-parser",
            "version": "1.2.3",
            "reader": "fixture-reader",
            "writer": "fixture-writer",
            "normalization_version": "normalization-fixture-v1",
        },
        "output": {
            "root": "extraction/20_drafts/",
            "run_root": "extraction/20_drafts/runs/",
            "allowlist": ["extraction/20_drafts/runs/"],
        },
    }
    return {
        "root": repository,
        "commit": commit,
        "contents": contents,
        "manifest": manifest,
    }
