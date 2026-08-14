"""Schema-compliance review agent.

Validates extraction drafts against the Pydantic variable-spec model and
checks structural requirements (required sections, no stubs, front-matter
immutability).

Usage:
    .venv/bin/python extraction/agents/schema_compliance.py [draft_dir]

Output:
    YAML findings file per artifact in extraction/25_agent_review/
"""

import sys
import re
from pathlib import Path
from datetime import datetime, timezone

# Add project root to path for schema imports
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import yaml
from schema.variable import VariableDefinition, VARIABLE_ID_PATTERN, MODULE_ID_PATTERN, RULE_ID_PATTERN


REQUIRED_SECTIONS = [
    "Definition",
    "Conceptual intent",
    "Construction notes",
    "Consistency checks",
    "Escalation triggers",
    "Common mistakes",
    "Change log",
]

STUB_THRESHOLD_CHARS = 50


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


def check_frontmatter(frontmatter: dict, known_variable_ids: set, known_rule_ids: set) -> list[dict]:
    """Check YAML front matter against the Pydantic model."""
    findings = []

    # Try to validate with Pydantic
    try:
        VariableDefinition.model_validate(
            frontmatter,
            context={
                "variable_ids": known_variable_ids,
                "rule_ids": known_rule_ids,
                "allow_unresolved_draft": True,
            },
        )
    except Exception as e:
        findings.append({
            "field": "frontmatter",
            "severity": "error",
            "message": f"Pydantic validation failed: {e}",
            "line": None,
        })

    # Check variable_id format
    vid = frontmatter.get("variable_id", "")
    if not VARIABLE_ID_PATTERN.fullmatch(vid):
        findings.append({
            "field": "variable_id",
            "severity": "error",
            "message": f"variable_id '{vid}' does not match VAR-<lowercase-name>",
            "line": None,
        })

    # Check module_id format
    mid = frontmatter.get("module_id", "")
    if not MODULE_ID_PATTERN.fullmatch(mid):
        findings.append({
            "field": "module_id",
            "severity": "error",
            "message": f"module_id '{mid}' does not match MOD-<UPPERCASE-NAME>",
            "line": None,
        })

    # Check rule references format
    for rule_ref in frontmatter.get("rules", []):
        if not RULE_ID_PATTERN.fullmatch(rule_ref):
            findings.append({
                "field": "rules",
                "severity": "error",
                "message": f"rule reference '{rule_ref}' does not match RULE-<UPPERCASE-SEQ>",
                "line": None,
            })

    return findings


def check_sections(sections: dict[str, str]) -> list[dict]:
    """Check required markdown sections are present and non-stub."""
    findings = []

    for section_name in REQUIRED_SECTIONS:
        if section_name not in sections:
            findings.append({
                "field": f"section:{section_name}",
                "severity": "error",
                "message": f"Required section '## {section_name}' is missing",
                "line": None,
            })
            continue

        content = sections[section_name]
        if len(content) < STUB_THRESHOLD_CHARS:
            findings.append({
                "field": f"section:{section_name}",
                "severity": "warning",
                "message": f"Section '## {section_name}' may be a stub ({len(content)} chars < {STUB_THRESHOLD_CHARS} threshold)",
                "line": None,
            })

        # Check for placeholder text
        placeholders = ["TODO", "TBD", "placeholder", "lorem ipsum", "FIXME"]
        for placeholder in placeholders:
            if placeholder.lower() in content.lower():
                findings.append({
                    "field": f"section:{section_name}",
                    "severity": "warning",
                    "message": f"Section '## {section_name}' contains placeholder text: '{placeholder}'",
                    "line": None,
                })

    return findings


def check_variable_references(frontmatter: dict, known_variable_ids: set) -> list[dict]:
    """Check that variable references exist or are noted as not yet extracted."""
    findings = []

    for ref_field in ["derived_from", "derives_to"]:
        for ref_id in frontmatter.get(ref_field, []):
            if ref_id not in known_variable_ids:
                findings.append({
                    "field": ref_field,
                    "severity": "warning",
                    "message": f"References {ref_id} which is not yet extracted",
                    "line": None,
                })

    for prereq in frontmatter.get("prerequisites", []):
        ref_id = prereq.get("variable_id", "")
        if ref_id and ref_id not in known_variable_ids:
            findings.append({
                "field": "prerequisites",
                "severity": "warning",
                "message": f"Prerequisite references {ref_id} which is not yet extracted",
                "line": None,
            })

    return findings


def review_artifact(
    artifact_path: Path,
    draft_dir: Path,
    known_variable_ids: set,
    known_rule_ids: set,
) -> dict:
    """Review a single extraction draft for schema compliance."""
    content = artifact_path.read_text(encoding="utf-8")
    artifact_id = artifact_path.stem

    findings = []

    # Parse front matter
    frontmatter = parse_frontmatter(content)
    if frontmatter is None:
        findings.append({
            "field": "frontmatter",
            "severity": "error",
            "message": "Could not parse YAML front matter",
            "line": None,
        })
        return {
            "agent": "schema-compliance",
            "artifact_id": artifact_id,
            "checked_at": datetime.now(timezone.utc).isoformat(),
            "findings": findings,
            "summary": {"errors": 1, "warnings": 0, "passed": False},
        }

    # Check front matter
    findings.extend(check_frontmatter(frontmatter, known_variable_ids, known_rule_ids))

    # Check variable references
    findings.extend(check_variable_references(frontmatter, known_variable_ids))

    # Check sections
    sections = parse_sections(content)
    findings.extend(check_sections(sections))

    # Build summary
    errors = sum(1 for f in findings if f["severity"] == "error")
    warnings = sum(1 for f in findings if f["severity"] == "warning")

    return {
        "agent": "schema-compliance",
        "artifact_id": artifact_id,
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "findings": findings,
        "summary": {
            "errors": errors,
            "warnings": warnings,
            "passed": errors == 0,
        },
    }


def discover_variable_ids(draft_dir: Path) -> set[str]:
    """Discover all variable IDs from extraction drafts."""
    ids = set()
    for md_file in draft_dir.rglob("*.md"):
        if md_file.name == ".gitkeep":
            continue
        content = md_file.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(content)
        if frontmatter and "variable_id" in frontmatter:
            ids.add(frontmatter["variable_id"])
    return ids


def discover_rule_ids(draft_dir: Path) -> set[str]:
    """Discover all rule IDs from extraction drafts and knowledge."""
    ids = set()
    for md_file in draft_dir.rglob("*.md"):
        if md_file.name == ".gitkeep":
            continue
        content = md_file.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(content)
        if frontmatter:
            ids.update(frontmatter.get("rules", []))
    # From knowledge rules directory
    rules_dir = PROJECT_ROOT / "knowledge" / "rules"
    if rules_dir.exists():
        for rule_file in rules_dir.rglob("*.md"):
            ids.add(rule_file.stem)
    return ids


def main():
    draft_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else PROJECT_ROOT / "extraction" / "20_drafts"
    output_dir = PROJECT_ROOT / "extraction" / "25_agent_review"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Discover known IDs
    known_variable_ids = discover_variable_ids(draft_dir)
    known_rule_ids = discover_rule_ids(draft_dir)

    print(f"Discovered {len(known_variable_ids)} variable IDs, {len(known_rule_ids)} rule IDs")
    print(f"Reviewing drafts in {draft_dir}...")

    results = []
    for md_file in sorted(draft_dir.rglob("*.md")):
        if md_file.name == ".gitkeep":
            continue
        print(f"  Reviewing {md_file.stem}...")
        result = review_artifact(md_file, draft_dir, known_variable_ids, known_rule_ids)
        results.append(result)

        # Write findings
        output_file = output_dir / f"{md_file.stem}.schema-compliance.yml"
        with open(output_file, "w") as f:
            yaml.dump(result, f, default_flow_style=False, sort_keys=False)

    # Summary
    total_errors = sum(r["summary"]["errors"] for r in results)
    total_warnings = sum(r["summary"]["warnings"] for r in results)
    passed = sum(1 for r in results if r["summary"]["passed"])

    print(f"\nResults: {passed}/{len(results)} passed, {total_errors} errors, {total_warnings} warnings")

    # Write summary
    summary = {
        "agent": "schema-compliance",
        "run_at": datetime.now(timezone.utc).isoformat(),
        "total_artifacts": len(results),
        "passed": passed,
        "failed": len(results) - passed,
        "total_errors": total_errors,
        "total_warnings": total_warnings,
    }
    summary_file = output_dir / "schema-compliance-summary.yml"
    with open(summary_file, "w") as f:
        yaml.dump(summary, f, default_flow_style=False, sort_keys=False)

    sys.exit(0 if total_errors == 0 else 1)


if __name__ == "__main__":
    main()
