"""Agent 1: Schema compliance checks for extraction drafts.

Validates Pydantic model, ID formats, structural section presence,
and placeholder detection. Does NOT check section content quality
—that is Agent 3 (rules_caveats).
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from schema.variable import (
    MODULE_ID_PATTERN,
    PARAMETER_ID_PATTERN,
    RULE_ID_PATTERN,
    VARIABLE_ID_PATTERN,
    VariableDefinition,
)

from .helpers import REQUIRED_SECTIONS, load_draft, make_findings
from .models import AgentFindings, Finding

AGENT_NAME = "schema_compliance"

PLACEHOLDER_PATTERNS: list[re.Pattern[str]] = [
    re.compile(r"\bTODO\b", re.IGNORECASE),
    re.compile(r"\bTBD\b", re.IGNORECASE),
    re.compile(r"\bFIXME\b", re.IGNORECASE),
    re.compile(r"lorem ipsum", re.IGNORECASE),
]

_ID_PATTERN_MAP: dict[str, re.Pattern[str]] = {
    "variable_id": VARIABLE_ID_PATTERN,
    "module_id": MODULE_ID_PATTERN,
}


def _find_section_headings(body: str) -> dict[str, int]:
    """Return heading text -> line number for H2 headings in body."""
    headings: dict[str, int] = {}
    for lineno, line in enumerate(body.splitlines(), start=1):
        if line.startswith("## "):
            heading_text = line[3:].strip()
            headings[heading_text] = lineno
    return headings


def _section_has_content(body: str, heading: str) -> bool:
    """Check if the section under `heading` has any non-empty lines after it."""
    pattern = re.compile(r"^## " + re.escape(heading) + r"\s*$", re.MULTILINE)
    match = pattern.search(body)
    if not match:
        return False
    after = body[match.end():]
    next_heading = re.search(r"^## ", after, re.MULTILINE)
    section_text = after[: next_heading.start()] if next_heading else after
    return any(line.strip() for line in section_text.splitlines())


def _check_frontmatter_validates(
    path: Path, data: dict[str, Any], variable_ids: set[str], parameter_ids: set[str], rule_ids: set[str]
) -> list[Finding]:
    """Validate frontmatter against VariableDefinition Pydantic model."""
    findings: list[Finding] = []
    try:
        VariableDefinition.model_validate(
            data,
            context={
                "variable_ids": variable_ids,
                "parameter_ids": parameter_ids,
                "rule_ids": rule_ids,
                "allow_unresolved_draft": True,
            },
        )
    except Exception as exc:
        findings.append(Finding(
            field="frontmatter",
            severity="error",
            message=f"Pydantic validation failed: {exc}",
        ))
    return findings


def _check_id_formats(data: dict[str, Any]) -> list[Finding]:
    """Validate ID format patterns for known fields."""
    findings: list[Finding] = []
    for field, pattern in _ID_PATTERN_MAP.items():
        value = data.get(field, "")
        if value and not pattern.fullmatch(str(value)):
            findings.append(Finding(
                field=field,
                severity="error",
                message=f"Invalid {field} format: {value!r} does not match {pattern.pattern}",
            ))
    for rule_id in data.get("rules", []):
        if not RULE_ID_PATTERN.fullmatch(rule_id):
            findings.append(Finding(
                field="rules",
                severity="error",
                message=f"Invalid rule ID format: {rule_id!r}",
            ))
    for param_id in data.get("country_parameters", []):
        if not PARAMETER_ID_PATTERN.fullmatch(param_id):
            findings.append(Finding(
                field="country_parameters",
                severity="error",
                message=f"Invalid parameter ID format: {param_id!r}",
            ))
    return findings


def _check_required_sections(body: str) -> list[Finding]:
    """Check that all 7 required sections are present and have content."""
    findings: list[Finding] = []
    headings = _find_section_headings(body)
    for section in REQUIRED_SECTIONS:
        if section not in headings:
            findings.append(Finding(
                field="body",
                severity="error",
                message=f"Required section missing: ## {section}",
            ))
        elif not _section_has_content(body, section):
            findings.append(Finding(
                field="body",
                severity="warning",
                message=f"Section ## {section} has no content after heading",
            ))
    return findings


def _check_placeholders(body: str) -> list[Finding]:
    """Detect placeholder text in the Markdown body."""
    findings: list[Finding] = []
    for lineno, line in enumerate(body.splitlines(), start=1):
        for pattern in PLACEHOLDER_PATTERNS:
            if pattern.search(line):
                findings.append(Finding(
                    field="body",
                    severity="warning",
                    message=f"Placeholder text detected: {pattern.pattern} on line {lineno}",
                    line=lineno,
                ))
    return findings


def _check_unresolved_parameter_refs(data: dict[str, Any], parameter_ids: set[str]) -> list[Finding]:
    """Check that country_parameters references exist in the registry."""
    findings: list[Finding] = []
    for param_id in data.get("country_parameters", []):
        if param_id not in parameter_ids:
            findings.append(Finding(
                field="country_parameters",
                severity="error",
                message=f"Parameter reference not in registry: {param_id}",
            ))
    return findings


def check_draft(
    path: Path,
    variable_ids: set[str],
    parameter_ids: set[str] | None = None,
    rule_ids: set[str] | None = None,
) -> AgentFindings:
    """Run all schema compliance checks on a single draft."""
    if parameter_ids is None:
        parameter_ids = set()
    if rule_ids is None:
        rule_ids = set()

    data, body = load_draft(path)
    artifact_id = data.get("variable_id", path.stem)

    findings: list[Finding] = []
    findings.extend(_check_frontmatter_validates(path, data, variable_ids, parameter_ids, rule_ids))
    findings.extend(_check_id_formats(data))
    findings.extend(_check_required_sections(body))
    findings.extend(_check_placeholders(body))
    findings.extend(_check_unresolved_parameter_refs(data, parameter_ids))

    return make_findings(AGENT_NAME, artifact_id, findings)