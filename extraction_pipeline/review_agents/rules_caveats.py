"""Agent 3: Rules and caveats quality checks for extraction drafts.

Checks content quality of required sections: substantive content,
actionable consistency checks, concrete escalation triggers,
real pitfalls in common mistakes, and vague text detection.
Does NOT check section heading existence — that is Agent 1.
"""

from __future__ import annotations

import re
from pathlib import Path

from .helpers import REQUIRED_SECTIONS, load_draft, make_findings
from .models import AgentFindings, Finding

AGENT_NAME = "rules_caveats"

MIN_SECTION_LENGTH = 50

VAGUE_PATTERNS: list[re.Pattern[str]] = [
    re.compile(r"\bverify\b", re.IGNORECASE),
    re.compile(r"\bcheck that\b", re.IGNORECASE),
    re.compile(r"\bensure\b", re.IGNORECASE),
    re.compile(r"\bappropriate\b", re.IGNORECASE),
    re.compile(r"\bvalid\b", re.IGNORECASE),
    re.compile(r"\bcorrect\b", re.IGNORECASE),
    re.compile(r"\breasonable\b", re.IGNORECASE),
]


def _extract_section(body: str, heading: str) -> tuple[str, int | None]:
    """Extract the text content under a heading. Returns (text, start_line)."""
    pattern = re.compile(r"^## " + re.escape(heading) + r"\s*$", re.MULTILINE)
    match = pattern.search(body)
    if not match:
        return "", None
    after = body[match.end():]
    next_heading = re.search(r"^## ", after, re.MULTILINE)
    section_text = after[: next_heading.start()] if next_heading else after
    start_line = body[: match.end()].count("\n") + 1
    return section_text.strip(), start_line


def _check_substantive_content(body: str) -> list[Finding]:
    """Check each required section has >= 50 chars of body text after heading."""
    findings: list[Finding] = []
    for section in REQUIRED_SECTIONS:
        text, _ = _extract_section(body, section)
        if text and len(text) < MIN_SECTION_LENGTH:
            findings.append(Finding(
                field=section.lower().replace(" ", "_"),
                severity="error",
                message=f"Section ## {section} is a stub ({len(text)} chars < {MIN_SECTION_LENGTH} minimum)",
            ))
    return findings


def _check_construction_notes(body: str) -> list[Finding]:
    """Check construction notes for derivation paths and ordering."""
    findings: list[Finding] = []
    text, _ = _extract_section(body, "Construction notes")
    if not text or len(text) < MIN_SECTION_LENGTH:
        return findings

    if "TODO" in text.upper():
        findings.append(Finding(
            field="construction_notes",
            severity="warning",
            message="Construction notes contain TODO marker",
        ))
    return findings


def _check_consistency_checks(body: str) -> list[Finding]:
    """Check consistency checks are specific and in list format."""
    findings: list[Finding] = []
    text, _ = _extract_section(body, "Consistency checks")
    if not text:
        return findings

    has_list_items = bool(re.search(r"^[-*]\s|^\d+[.)]\s", text, re.MULTILINE))
    if not has_list_items:
        findings.append(Finding(
            field="consistency_checks",
            severity="warning",
            message="Consistency checks section lacks list format (bullet points or numbered)",
        ))

    for pattern in VAGUE_PATTERNS:
        for lineno_offset, line in enumerate(text.splitlines()):
            if pattern.search(line) and line.strip().startswith(("-", "*")):
                findings.append(Finding(
                    field="consistency_checks",
                    severity="warning",
                    message=f"Vague text in Consistency checks: '{pattern.pattern}' in '{line.strip()[:60]}'",
                ))
                break
    return findings


def _check_escalation_triggers(body: str) -> list[Finding]:
    """Check escalation triggers have concrete IF conditions."""
    findings: list[Finding] = []
    text, _ = _extract_section(body, "Escalation triggers")
    if not text:
        return findings

    if "TODO" in text.upper():
        findings.append(Finding(
            field="escalation_triggers",
            severity="warning",
            message="Escalation triggers contain TODO placeholder",
        ))

    has_concrete_conditions = bool(
        re.search(r"\bif\b|\bwhen\b|\bno\b|\bcannot\b|\bmore than\b|\bdiffers\b", text, re.IGNORECASE)
    )
    if not has_concrete_conditions:
        findings.append(Finding(
            field="escalation_triggers",
            severity="warning",
            message="Escalation triggers lack concrete IF/WHEN conditions",
        ))
    return findings


def _check_common_mistakes(body: str) -> list[Finding]:
    """Check common mistakes are real pitfalls, not placeholders."""
    findings: list[Finding] = []
    text, _ = _extract_section(body, "Common mistakes")
    if not text:
        return findings

    has_list_items = bool(re.search(r"^[-*]\s|^\d+[.)]\s", text, re.MULTILINE))
    if not has_list_items:
        findings.append(Finding(
            field="common_mistakes",
            severity="warning",
            message="Common mistakes section lacks list format (bullet points or numbered)",
        ))

    if "TODO" in text.upper() or "TBD" in text.upper():
        findings.append(Finding(
            field="common_mistakes",
            severity="warning",
            message="Common mistakes contain placeholder text (TODO/TBD)",
        ))
    return findings


def check_draft(path: Path) -> AgentFindings:
    """Run all rules/caveats quality checks on a single draft."""
    data, body = load_draft(path)
    artifact_id = data.get("variable_id", path.stem)

    findings: list[Finding] = []
    findings.extend(_check_substantive_content(body))
    findings.extend(_check_construction_notes(body))
    findings.extend(_check_consistency_checks(body))
    findings.extend(_check_escalation_triggers(body))
    findings.extend(_check_common_mistakes(body))

    return make_findings(AGENT_NAME, artifact_id, findings)