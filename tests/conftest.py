import shutil
import subprocess
from pathlib import Path

import pytest
import yaml

from schema.frontmatter import load_markdown


ROOT = Path(__file__).resolve().parents[1]


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