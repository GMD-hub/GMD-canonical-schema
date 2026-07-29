import json
import subprocess
import sys
from pathlib import Path


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