"""Agent 2: Source grounding checks for extraction drafts.

Checks provenance fields, derivation documentation, and rule references
in the Markdown body.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .helpers import load_draft, make_findings
from .models import AgentFindings, Finding

AGENT_NAME = "source_grounding"


def _check_provenance_source_document(data: dict[str, Any]) -> list[Finding]:
    """Check provenance.source_document is non-empty and references GMD guidelines."""
    findings: list[Finding] = []
    provenance = data.get("provenance", {})
    source_doc = provenance.get("source_document", "")
    if not source_doc or not source_doc.strip():
        findings.append(Finding(
            field="provenance.source_document",
            severity="error",
            message="provenance.source_document is empty",
        ))
    elif "GMD" not in source_doc and "gmd" not in source_doc.lower():
        findings.append(Finding(
            field="provenance.source_document",
            severity="warning",
            message=f"provenance.source_document does not reference GMD guidelines: {source_doc!r}",
        ))
    return findings


def _check_provenance_source_section(data: dict[str, Any]) -> list[Finding]:
    """Check provenance.source_section is non-empty."""
    findings: list[Finding] = []
    provenance = data.get("provenance", {})
    source_section = provenance.get("source_section", "")
    if not source_section or not source_section.strip():
        findings.append(Finding(
            field="provenance.source_section",
            severity="error",
            message="provenance.source_section is empty",
        ))
    return findings


def _check_derivation_in_construction_notes(data: dict[str, Any], body: str) -> list[Finding]:
    """Check that derived variable dependencies are documented in Construction notes."""
    findings: list[Finding] = []
    derived_from = data.get("derived_from", [])
    if not derived_from:
        return findings

    construction_match = re.search(
        r"^## Construction notes\s*$", body, re.MULTILINE
    )
    if not construction_match:
        return findings

    after = body[construction_match.end():]
    next_heading = re.search(r"^## ", after, re.MULTILINE)
    construction_text = after[: next_heading.start()] if next_heading else after

    for dep in derived_from:
        dep_name = dep.replace("VAR-", "")
        if dep_name.lower() not in construction_text.lower() and dep.lower() not in construction_text.lower():
            findings.append(Finding(
                field="construction_notes",
                severity="warning",
                message=f"Derivation dependency {dep} not mentioned in Construction notes",
            ))
    return findings


def _check_rules_referenced_in_body(data: dict[str, Any], body: str) -> list[Finding]:
    """Check that rules declared in frontmatter are referenced in the Markdown body."""
    findings: list[Finding] = []
    rules = data.get("rules", [])
    if not rules:
        return findings

    body_lower = body.lower()
    for rule_id in rules:
        if rule_id.lower() not in body_lower:
            findings.append(Finding(
                field="rules",
                severity="warning",
                message=f"Rule {rule_id} declared in frontmatter but not referenced in body",
            ))
    return findings


def check_draft(path: Path) -> AgentFindings:
    """Run all source grounding checks on a single draft."""
    data, body = load_draft(path)
    artifact_id = data.get("variable_id", path.stem)

    findings: list[Finding] = []
    findings.extend(_check_provenance_source_document(data))
    findings.extend(_check_provenance_source_section(data))
    findings.extend(_check_derivation_in_construction_notes(data, body))
    findings.extend(_check_rules_referenced_in_body(data, body))

    return make_findings(AGENT_NAME, artifact_id, findings)