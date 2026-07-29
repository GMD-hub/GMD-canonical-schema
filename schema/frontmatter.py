"""Read Markdown artifacts with YAML front matter."""

from pathlib import Path
from typing import Any

import yaml


def load_markdown(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path} does not start with YAML front matter")

    try:
        front_matter, body = text[4:].split("\n---\n", 1)
    except ValueError as exc:
        raise ValueError(f"{path} has unterminated YAML front matter") from exc

    data = yaml.safe_load(front_matter)
    if not isinstance(data, dict):
        raise ValueError(f"{path} front matter must be a mapping")
    return data, body.lstrip("\n")
