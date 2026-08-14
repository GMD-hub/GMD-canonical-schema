"""Rules and caveats completeness agent.

Validates that extraction drafts have complete, actionable IF/THEN logic,
edge cases covered, and no vague statements in required sections.

Usage:
    .venv/bin/python extraction/agents/rules_caveats.py [draft_dir]

Output:
    YAML findings file per artifact in extraction/25_agent_review/
"""

import sys
import re
from pathlib import Path
from datetime import datetime, timezone

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import yaml


REQUIRED_SECTIONS = [
    "Definition",
    "Conceptual intent",
    "Construction notes",
    "Consistency checks",
    "Escalation triggers",
    "Common mistakes",
    "Change log",
]

VAGUE_PATTERNS = [
    (r"\bverify\b", "vague 'verify' - specify what to check"),
    (r"\bcheck\b.*\bthat\b", "vague 'check that' - specify the check"),
    (r"\bensure\b", "vague 'ensure' - specify the condition"),
    (r"\bappropriate\b", "vague 'appropriate' - specify what is appropriate"),
    (r"\bvalid\b(?!ation)", "vague 'valid' - specify validity criteria"),
    (r"\bcorrect\b", "vague 'correct' - specify correctness criteria"),
    (r"\breasonable\b", "vague 'reasonable' - specify reasonableness criteria"),
]

PLACEHOLDER_PATTERNS = [
    r"\bTODO\b",
    r"\bTBD\b",
    r"\bFIXME\b",
    r"\bplaceholder\b",
    r"\blorem ipsum\b",
    r"\bN/A\b",
    r"\bnone\b",
    r"\bsee above\b",
    r"\bsee below\b",
]


def parse_frontmatter(content: str) -> dict | None:
    """Extract YAML front matter from a markdown file."""
    lines = content.split("\n")
    markers = [i for i, line in enumerate(lines) if line.strip() == "---"]
    if len(markers) < 2:
        return None
    yaml_content = "\n".join(lines[markers[0] + 1 : markers[1]])
    try:
        return yaml.safe_load(yaml_content)
    except yaml.YAMLError:
        return None


def parse_sections(content: str) -> dict[str, str]:
    """Extract markdown sections by heading."""
    sections = {}
    current_section = None
    current_content = []

    for line in content.split("\n"):
        match = re.match(r"^## (.+)$", line)
        if match:
            if current_section:
                sections[current_section] = "\n".join(current_content).strip()
            current_section = match.group(1)
            current_content = []
        elif current_section:
            current_content.append(line)

    if current_section:
        sections[current_section] = "\n".join(current_content).strip()

    return sections


def check_construction_notes(frontmatter: dict, sections: dict) -> list[dict]:
    """Check Construction notes section for completeness."""
    findings = []

    construction = sections.get("Construction notes", "")
    derived_from = frontmatter.get("derived_from", [])
    mapping_role = frontmatter.get("mapping_role", "")

    if not construction:
        findings.append({
            "field": "section:Construction notes",
            "severity": "error",
            "message": "Construction notes section is empty",
            "line": None,
        })
        return findings

    # Check if derivation paths are documented
    if derived_from:
        for dep in derived_from:
            if dep not in construction:
                findings.append({
                    "field": "section:Construction notes",
                    "severity": "warning",
                    "message": f"Derivation dependency '{dep}' not documented in Construction notes",
                    "line": None,
                })

    # Check for IF/THEN logic if the variable is derived
    if mapping_role in ["derived", "derived_preferred"]:
        if "if" not in construction.lower() and "then" not in construction.lower():
            findings.append({
                "field": "section:Construction notes",
                "severity": "warning",
                "message": "Derived variable should have IF/THEN logic in Construction notes",
                "line": None,
            })

    # Check for ordering/priority if multiple derivation paths
    if len(derived_from) > 1:
        if "order" not in construction.lower() and "priority" not in construction.lower() and "first" not in construction.lower():
            findings.append({
                "field": "section:Construction notes",
                "severity": "warning",
                "message": "Multiple derivation paths but no ordering/priority documented",
                "line": None,
            })

    return findings


def check_consistency_checks(sections: dict) -> list[dict]:
    """Check Consistency checks section for actionability."""
    findings = []

    checks = sections.get("Consistency checks", "")

    if not checks:
        findings.append({
            "field": "section:Consistency checks",
            "severity": "error",
            "message": "Consistency checks section is empty",
            "line": None,
        })
        return findings

    # Check for vague patterns
    for pattern, message in VAGUE_PATTERNS:
        if re.search(pattern, checks, re.IGNORECASE):
            findings.append({
                "field": "section:Consistency checks",
                "severity": "warning",
                "message": f"Consistency checks: {message}",
                "line": None,
            })

    # Check for specific check items (bullet points or numbered lists)
    has_list = bool(re.search(r"^[\s]*[-*]\s", checks, re.MULTILINE))
    has_numbered = bool(re.search(r"^[\s]*\d+\.\s", checks, re.MULTILINE))
    if not has_list and not has_numbered:
        findings.append({
            "field": "section:Consistency checks",
            "severity": "warning",
            "message": "Consistency checks should be a list of specific checks",
            "line": None,
        })

    return findings


def check_escalation_triggers(sections: dict) -> list[dict]:
    """Check Escalation triggers section for specificity."""
    findings = []

    triggers = sections.get("Escalation triggers", "")

    if not triggers:
        findings.append({
            "field": "section:Escalation triggers",
            "severity": "error",
            "message": "Escalation triggers section is empty",
            "line": None,
        })
        return findings

    # Check for concrete conditions
    if "if" not in triggers.lower():
        findings.append({
            "field": "section:Escalation triggers",
            "severity": "warning",
            "message": "Escalation triggers should have concrete IF conditions",
            "line": None,
        })

    # Check for vague patterns
    for pattern, message in VAGUE_PATTERNS:
        if re.search(pattern, triggers, re.IGNORECASE):
            findings.append({
                "field": "section:Escalation triggers",
                "severity": "warning",
                "message": f"Escalation triggers: {message}",
                "line": None,
            })

    return findings


def check_common_mistakes(sections: dict) -> list[dict]:
    """Check Common mistakes section for real pitfalls."""
    findings = []

    mistakes = sections.get("Common mistakes", "")

    if not mistakes:
        findings.append({
            "field": "section:Common mistakes",
            "severity": "error",
            "message": "Common mistakes section is empty",
            "line": None,
        })
        return findings

    # Check for placeholder text
    for pattern in PLACEHOLDER_PATTERNS:
        if re.search(pattern, mistakes, re.IGNORECASE):
            findings.append({
                "field": "section:Common mistakes",
                "severity": "warning",
                "message": f"Common mistakes contains placeholder text: '{pattern}'",
                "line": None,
            })

    # Check for specific mistake items
    has_list = bool(re.search(r"^[\s]*[-*]\s", mistakes, re.MULTILINE))
    has_numbered = bool(re.search(r"^[\s]*\d+\.\s", mistakes, re.MULTILINE))
    if not has_list and not has_numbered:
        findings.append({
            "field": "section:Common mistakes",
            "severity": "warning",
            "message": "Common mistakes should be a list of specific pitfalls",
            "line": None,
        })

    return findings


def check_all_sections(sections: dict) -> list[dict]:
    """Check all required sections for completeness."""
    findings = []

    for section_name in REQUIRED_SECTIONS:
        if section_name not in sections:
            findings.append({
                "field": f"section:{section_name}",
                "severity": "error",
                "message": f"Required section '## {section_name}' is missing",
                "line": None,
            })
        elif not sections[section_name]:
            findings.append({
                "field": f"section:{section_name}",
                "severity": "error",
                "message": f"Required section '## {section_name}' is empty",
                "line": None,
            })

    return findings


def review_artifact(artifact_path: Path) -> dict:
    """Review a single extraction draft for rules and caveats completeness."""
    content = artifact_path.read_text(encoding="utf-8")
    artifact_id = artifact_path.stem

    findings = []

    frontmatter = parse_frontmatter(content)
    if frontmatter is None:
        findings.append({
            "field": "frontmatter",
            "severity": "error",
            "message": "Could not parse YAML front matter",
            "line": None,
        })
        return {
            "agent": "rules-caveats",
            "artifact_id": artifact_id,
            "checked_at": datetime.now(timezone.utc).isoformat(),
            "findings": findings,
            "summary": {"errors": 1, "warnings": 0, "passed": False},
        }

    sections = parse_sections(content)

    findings.extend(check_all_sections(sections))
    findings.extend(check_construction_notes(frontmatter, sections))
    findings.extend(check_consistency_checks(sections))
    findings.extend(check_escalation_triggers(sections))
    findings.extend(check_common_mistakes(sections))

    errors = sum(1 for f in findings if f["severity"] == "error")
    warnings = sum(1 for f in findings if f["severity"] == "warning")

    return {
        "agent": "rules-caveats",
        "artifact_id": artifact_id,
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "findings": findings,
        "summary": {
            "errors": errors,
            "warnings": warnings,
            "passed": errors == 0,
        },
    }


def main():
    draft_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else PROJECT_ROOT / "extraction" / "20_drafts"
    output_dir = PROJECT_ROOT / "extraction" / "25_agent_review"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Reviewing drafts in {draft_dir}...")

    results = []
    for md_file in sorted(draft_dir.rglob("*.md")):
        if md_file.name == ".gitkeep":
            continue
        print(f"  Reviewing {md_file.stem}...")
        result = review_artifact(md_file)
        results.append(result)

        output_file = output_dir / f"{md_file.stem}.rules-caveats.yml"
        with open(output_file, "w") as f:
            yaml.dump(result, f, default_flow_style=False, sort_keys=False)

    total_errors = sum(r["summary"]["errors"] for r in results)
    total_warnings = sum(r["summary"]["warnings"] for r in results)
    passed = sum(1 for r in results if r["summary"]["passed"])

    print(f"\nResults: {passed}/{len(results)} passed, {total_errors} errors, {total_warnings} warnings")

    summary = {
        "agent": "rules-caveats",
        "run_at": datetime.now(timezone.utc).isoformat(),
        "total_artifacts": len(results),
        "passed": passed,
        "failed": len(results) - passed,
        "total_errors": total_errors,
        "total_warnings": total_warnings,
    }
    summary_file = output_dir / "rules-caveats-summary.yml"
    with open(summary_file, "w") as f:
        yaml.dump(summary, f, default_flow_style=False, sort_keys=False)

    sys.exit(0 if total_errors == 0 else 1)


if __name__ == "__main__":
    main()
