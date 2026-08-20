"""Shared helpers for review agents."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from schema.frontmatter import load_markdown

from .models import AgentFindings, AgentSummary, Finding

REQUIRED_SECTIONS: list[str] = [
    "Definition",
    "Conceptual intent",
    "Construction notes",
    "Consistency checks",
    "Escalation triggers",
    "Common mistakes",
    "Change log",
]


def load_draft(path: Path) -> tuple[dict[str, Any], str]:
    """Load a draft YAML frontmatter + Markdown body via the shared parser."""
    return load_markdown(path)


def write_findings(findings: AgentFindings, output_dir: Path) -> Path:
    """Serialize AgentFindings to a YAML file in the output directory."""
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{findings.artifact_id}.{findings.agent}.yml"
    output_path = output_dir / filename
    data = findings.model_dump()
    output_path.write_text(
        yaml.safe_dump(data, default_flow_style=False, sort_keys=False),
        encoding="utf-8",
    )
    return output_path


def list_drafts(drafts_dir: Path) -> list[Path]:
    """Yield all .md files recursively from the drafts directory.

    Skips files inside the ``project-documentation/`` subdirectory
    (process docs, not variable definitions).
    """
    return sorted(
        p for p in drafts_dir.rglob("*.md")
        if "project-documentation" not in p.parts
    )


def list_parameter_ids(registry_dir: Path) -> tuple[set[str], list[str]]:
    """Load parameter IDs from knowledge/parameters/*.md.

    Returns (parameter_ids, skipped_files) where skipped_files lists
    filenames that failed to parse or lacked a parameter_id field.
    """
    parameter_ids: set[str] = set()
    skipped: list[str] = []
    if not registry_dir.is_dir():
        return parameter_ids, skipped
    for path in sorted(registry_dir.glob("*.md")):
        try:
            data, _ = load_markdown(path)
            pid = data.get("parameter_id", "")
            if pid:
                parameter_ids.add(pid)
            else:
                skipped.append(path.name)
        except Exception as exc:
            skipped.append(f"{path.name}: {exc}")
    return parameter_ids, skipped


def make_findings(
    agent: str,
    artifact_id: str,
    findings: list[Finding],
) -> AgentFindings:
    """Build an AgentFindings object with computed summary."""
    errors = sum(1 for f in findings if f.severity == "error")
    warnings = sum(1 for f in findings if f.severity == "warning")
    passed = 1 if errors == 0 and warnings == 0 else 0
    return AgentFindings(
        agent=agent,
        artifact_id=artifact_id,
        checked_at=datetime.now(timezone.utc).isoformat(),
        findings=findings,
        summary=AgentSummary(errors=errors, warnings=warnings, passed=passed),
    )