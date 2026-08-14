"""Consistency and derivation graph agent.

Validates cross-variable consistency: derivation graph is acyclic,
derived_from/derives_to are symmetric, module consistency, and value code
consistency.

Usage:
    .venv/bin/python extraction/agents/consistency_derivation.py [draft_dir]

Output:
    YAML findings file per artifact in extraction/25_agent_review/
"""

import sys
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

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


def load_all_drafts(draft_dir: Path) -> dict[str, dict]:
    """Load all extraction drafts and return as dict keyed by variable_id."""
    variables = {}
    for md_file in sorted(draft_dir.rglob("*.md")):
        if md_file.name == ".gitkeep":
            continue
        content = md_file.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(content)
        if frontmatter and "variable_id" in frontmatter:
            variables[frontmatter["variable_id"]] = frontmatter
    return variables


def check_symmetry(variables: dict[str, dict]) -> list[dict]:
    """Check that derived_from and derives_to are symmetric."""
    findings = []

    for vid, var in variables.items():
        for dep in var.get("derived_from", []):
            if dep in variables:
                if vid not in variables[dep].get("derives_to", []):
                    findings.append({
                        "artifact_id": vid,
                        "field": "derived_from",
                        "severity": "error",
                        "message": f"{vid} derives_from {dep}, but {dep} does not derive_to {vid}",
                        "line": None,
                    })
            else:
                findings.append({
                    "artifact_id": vid,
                    "field": "derived_from",
                    "severity": "warning",
                    "message": f"{vid} derives_from {dep} which is not yet extracted",
                    "line": None,
                })

        for dep in var.get("derives_to", []):
            if dep in variables:
                if vid not in variables[dep].get("derived_from", []):
                    findings.append({
                        "artifact_id": vid,
                        "field": "derives_to",
                        "severity": "error",
                        "message": f"{vid} derives_to {dep}, but {dep} does not derive_from {vid}",
                        "line": None,
                    })

    return findings


def check_acyclic(variables: dict[str, dict]) -> list[dict]:
    """Check that the derivation graph is acyclic."""
    findings = []

    graph = {vid: set(var.get("derived_from", [])) for vid, var in variables.items()}
    visiting = set()
    visited = set()

    def visit(vid: str, path: list[str]) -> None:
        if vid in visiting:
            cycle_start = path.index(vid)
            cycle = path[cycle_start:] + [vid]
            findings.append({
                "artifact_id": vid,
                "field": "derived_from",
                "severity": "error",
                "message": f"Derivation graph contains a cycle: {' -> '.join(cycle)}",
                "line": None,
            })
            return
        if vid in visited:
            return
        visiting.add(vid)
        path.append(vid)
        for dep in graph.get(vid, set()):
            if dep in graph:
                visit(dep, path)
        path.pop()
        visiting.remove(vid)
        visited.add(vid)

    for vid in graph:
        visit(vid, [])

    return findings


def check_module_consistency(variables: dict[str, dict]) -> list[dict]:
    """Check that variables in a derivation chain are in the same module."""
    findings = []

    for vid, var in variables.items():
        module = var.get("module_id", "")
        for dep in var.get("derived_from", []):
            if dep in variables:
                dep_module = variables[dep].get("module_id", "")
                if module != dep_module:
                    findings.append({
                        "artifact_id": vid,
                        "field": "module_id",
                        "severity": "warning",
                        "message": f"{vid} ({module}) derives from {dep} ({dep_module}) - cross-module derivation",
                        "line": None,
                    })

    return findings


def check_value_code_consistency(variables: dict[str, dict]) -> list[dict]:
    """Check that derived variables have consistent value codes with their sources."""
    findings = []

    for vid, var in variables.items():
        derived_from = var.get("derived_from", [])
        if not derived_from:
            continue

        # Get the variable's value codes
        var_values = {vc["value"] for vc in var.get("value_codes", []) or []}
        if not var_values:
            continue

        # Check against each source
        for dep_id in derived_from:
            if dep_id not in variables:
                continue
            dep = variables[dep_id]
            dep_values = {vc["value"] for vc in dep.get("value_codes", []) or []}

            if dep_values and not var_values.issubset(dep_values):
                # Allow if there's a mapping (derived variables may have different codes)
                # This is a warning, not an error, because mapping is valid
                findings.append({
                    "artifact_id": vid,
                    "field": "value_codes",
                    "severity": "warning",
                    "message": f"{vid} value codes {sorted(var_values)} not a subset of {dep_id} value codes {sorted(dep_values)}",
                    "line": None,
                })

    return findings


def check_prerequisites(variables: dict[str, dict]) -> list[dict]:
    """Check that prerequisite variables exist."""
    findings = []

    for vid, var in variables.items():
        for prereq in var.get("prerequisites", []):
            prereq_id = prereq.get("variable_id", "")
            if prereq_id and prereq_id not in variables:
                findings.append({
                    "artifact_id": vid,
                    "field": "prerequisites",
                    "severity": "warning",
                    "message": f"Prerequisite {prereq_id} is not yet extracted",
                    "line": None,
                })

    return findings


def review_all(draft_dir: Path) -> list[dict]:
    """Review all extraction drafts for consistency and derivation."""
    variables = load_all_drafts(draft_dir)

    findings = []
    findings.extend(check_symmetry(variables))
    findings.extend(check_acyclic(variables))
    findings.extend(check_module_consistency(variables))
    findings.extend(check_value_code_consistency(variables))
    findings.extend(check_prerequisites(variables))

    # Group findings by artifact
    artifact_findings = defaultdict(list)
    for f in findings:
        artifact_findings[f["artifact_id"]].append(f)

    results = []
    for vid in sorted(variables.keys()):
        artifact_findings_list = artifact_findings.get(vid, [])
        errors = sum(1 for f in artifact_findings_list if f["severity"] == "error")
        warnings = sum(1 for f in artifact_findings_list if f["severity"] == "warning")

        results.append({
            "agent": "consistency-derivation",
            "artifact_id": vid,
            "checked_at": datetime.now(timezone.utc).isoformat(),
            "findings": artifact_findings_list,
            "summary": {
                "errors": errors,
                "warnings": warnings,
                "passed": errors == 0,
            },
        })

    return results


def main():
    draft_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else PROJECT_ROOT / "extraction" / "20_drafts"
    output_dir = PROJECT_ROOT / "extraction" / "25_agent_review"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Reviewing all drafts in {draft_dir} for consistency...")

    results = review_all(draft_dir)

    for result in results:
        output_file = output_dir / f"{result['artifact_id']}.consistency-derivation.yml"
        with open(output_file, "w") as f:
            yaml.dump(result, f, default_flow_style=False, sort_keys=False)
        status = "PASS" if result["summary"]["passed"] else "FAIL"
        print(f"  {result['artifact_id']}: {status} ({result['summary']['errors']} errors, {result['summary']['warnings']} warnings)")

    total_errors = sum(r["summary"]["errors"] for r in results)
    total_warnings = sum(r["summary"]["warnings"] for r in results)
    passed = sum(1 for r in results if r["summary"]["passed"])

    print(f"\nResults: {passed}/{len(results)} passed, {total_errors} errors, {total_warnings} warnings")

    summary = {
        "agent": "consistency-derivation",
        "run_at": datetime.now(timezone.utc).isoformat(),
        "total_artifacts": len(results),
        "passed": passed,
        "failed": len(results) - passed,
        "total_errors": total_errors,
        "total_warnings": total_warnings,
    }
    summary_file = output_dir / "consistency-derivation-summary.yml"
    with open(summary_file, "w") as f:
        yaml.dump(summary, f, default_flow_style=False, sort_keys=False)

    sys.exit(0 if total_errors == 0 else 1)


if __name__ == "__main__":
    main()
