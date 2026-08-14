"""Source-grounding review agent.

Validates that every rule, value code, and derivation path in extraction
drafts traces back to the GMD guidelines document.

Usage:
    .venv/bin/python extraction/agents/source_grounding.py [draft_dir]

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


def check_source_citations(frontmatter: dict, sections: dict) -> list[dict]:
    """Check that value codes and rules have source citations."""
    findings = []

    # Check if provenance has source document
    provenance = frontmatter.get("provenance", {})
    source_doc = provenance.get("source_document", "")
    source_section = provenance.get("source_section", "")

    if not source_doc:
        findings.append({
            "field": "provenance.source_document",
            "severity": "error",
            "message": "No source document specified in provenance",
            "line": None,
        })
    elif "gmd" not in source_doc.lower() and "guidelines" not in source_doc.lower():
        findings.append({
            "field": "provenance.source_document",
            "severity": "warning",
            "message": f"Source document '{source_doc}' does not appear to be the GMD guidelines",
            "line": None,
        })

    if not source_section:
        findings.append({
            "field": "provenance.source_section",
            "severity": "warning",
            "message": "No source section specified in provenance",
            "line": None,
        })

    # Check if Definition section references the source
    definition = sections.get("Definition", "")
    if definition and source_doc:
        # Look for section references in the definition
        if source_section and source_section not in definition:
            findings.append({
                "field": "section:Definition",
                "severity": "warning",
                "message": f"Definition does not reference source section '{source_section}'",
                "line": None,
            })

    return findings


def check_derivation_grounding(frontmatter: dict, sections: dict) -> list[dict]:
    """Check that derivation paths are documented in Construction notes."""
    findings = []

    derived_from = frontmatter.get("derived_from", [])
    derives_to = frontmatter.get("derives_to", [])

    construction = sections.get("Construction notes", "")

    if derived_from and not construction:
        findings.append({
            "field": "section:Construction notes",
            "severity": "error",
            "message": f"Variable derives from {derived_from} but Construction notes section is empty",
            "line": None,
        })
    elif derived_from:
        # Check if each derivation path is mentioned
        for dep in derived_from:
            if dep not in construction:
                findings.append({
                    "field": "section:Construction notes",
                    "severity": "warning",
                    "message": f"Derivation dependency '{dep}' not mentioned in Construction notes",
                    "line": None,
                })

    if derives_to and not construction:
        findings.append({
            "field": "section:Construction notes",
            "severity": "error",
            "message": f"Variable derives {derives_to} but Construction notes section is empty",
            "line": None,
        })

    return findings


def check_rule_grounding(frontmatter: dict, sections: dict) -> list[dict]:
    """Check that rules are referenced in the Markdown body."""
    findings = []

    rules = frontmatter.get("rules", [])
    all_content = "\n".join(sections.values())

    for rule_id in rules:
        if rule_id not in all_content:
            findings.append({
                "field": "rules",
                "severity": "warning",
                "message": f"Rule '{rule_id}' is declared but not referenced in the Markdown body",
                "line": None,
            })

    return findings


def review_artifact(artifact_path: Path) -> dict:
    """Review a single extraction draft for source grounding."""
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
            "agent": "source-grounding",
            "artifact_id": artifact_id,
            "checked_at": datetime.now(timezone.utc).isoformat(),
            "findings": findings,
            "summary": {"errors": 1, "warnings": 0, "passed": False},
        }

    sections = parse_sections(content)

    findings.extend(check_source_citations(frontmatter, sections))
    findings.extend(check_derivation_grounding(frontmatter, sections))
    findings.extend(check_rule_grounding(frontmatter, sections))

    errors = sum(1 for f in findings if f["severity"] == "error")
    warnings = sum(1 for f in findings if f["severity"] == "warning")

    return {
        "agent": "source-grounding",
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

        output_file = output_dir / f"{md_file.stem}.source-grounding.yml"
        with open(output_file, "w") as f:
            yaml.dump(result, f, default_flow_style=False, sort_keys=False)

    total_errors = sum(r["summary"]["errors"] for r in results)
    total_warnings = sum(r["summary"]["warnings"] for r in results)
    passed = sum(1 for r in results if r["summary"]["passed"])

    print(f"\nResults: {passed}/{len(results)} passed, {total_errors} errors, {total_warnings} warnings")

    summary = {
        "agent": "source-grounding",
        "run_at": datetime.now(timezone.utc).isoformat(),
        "total_artifacts": len(results),
        "passed": passed,
        "failed": len(results) - passed,
        "total_errors": total_errors,
        "total_warnings": total_warnings,
    }
    summary_file = output_dir / "source-grounding-summary.yml"
    with open(summary_file, "w") as f:
        yaml.dump(summary, f, default_flow_style=False, sort_keys=False)

    sys.exit(0 if total_errors == 0 else 1)


if __name__ == "__main__":
    main()
