"""Run all 4 review agents against extraction drafts.

Usage:
    .venv/bin/python extraction/agents/run_all_agents.py [draft_dir]

Output:
    Summary report in extraction/25_agent_review/SUMMARY.md
"""

import sys
import subprocess
from pathlib import Path
from datetime import datetime, timezone

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

AGENTS = [
    ("schema-compliance", "extraction/agents/schema_compliance.py"),
    ("source-grounding", "extraction/agents/source_grounding.py"),
    ("rules-caveats", "extraction/agents/rules_caveats.py"),
    ("consistency-derivation", "extraction/agents/consistency_derivation.py"),
]


def run_agent(agent_name: str, agent_script: str, draft_dir: str) -> dict:
    """Run a single agent and return its summary."""
    print(f"\n{'='*60}")
    print(f"Running {agent_name} agent...")
    print(f"{'='*60}")

    result = subprocess.run(
        [sys.executable, agent_script, draft_dir],
        cwd=str(PROJECT_ROOT),
        capture_output=True,
        text=True,
    )

    print(result.stdout)
    if result.stderr:
        print(f"STDERR:\n{result.stderr}")

    # Read the summary file
    summary_file = PROJECT_ROOT / "extraction" / "25_agent_review" / f"{agent_name}-summary.yml"
    if summary_file.exists():
        import yaml
        with open(summary_file) as f:
            return yaml.safe_load(f)
    else:
        return {
            "agent": agent_name,
            "status": "error",
            "return_code": result.returncode,
        }


def generate_summary(results: list[dict], output_dir: Path) -> str:
    """Generate a Markdown summary report."""
    lines = [
        "# Agent Review Summary",
        "",
        f"- **Run at**: {datetime.now(timezone.utc).isoformat()}",
        f"- **Agents**: {len(results)}",
        "",
        "## Results",
        "",
        "| Agent | Artifacts | Passed | Failed | Errors | Warnings |",
        "|-------|-----------|--------|--------|--------|----------|",
    ]

    total_errors = 0
    total_warnings = 0
    all_passed = True

    for r in results:
        agent = r.get("agent", "unknown")
        total = r.get("total_artifacts", 0)
        passed = r.get("passed", 0)
        failed = r.get("failed", 0)
        errors = r.get("total_errors", 0)
        warnings = r.get("total_warnings", 0)

        total_errors += errors
        total_warnings += warnings
        if errors > 0:
            all_passed = False

        status = "PASS" if errors == 0 else "FAIL"
        lines.append(f"| {agent} | {total} | {passed} | {failed} | {errors} | {warnings} |")

    lines.extend([
        "",
        f"**Overall**: {'ALL PASSED' if all_passed else 'FAILURES DETECTED'}",
        f"- Total errors: {total_errors}",
        f"- Total warnings: {total_warnings}",
        "",
        "## Per-Artifact Findings",
        "",
    ])

    # Read per-artifact findings
    import yaml
    for result in results:
        agent = result.get("agent", "unknown")
        summary_file = output_dir / f"{agent}-summary.yml"
        if not summary_file.exists():
            continue

        # Find all findings files for this agent
        for findings_file in sorted(output_dir.glob(f"*.{agent}.yml")):
            if findings_file.name.endswith("-summary.yml"):
                continue
            with open(findings_file) as f:
                findings = yaml.safe_load(f)
            artifact_id = findings.get("artifact_id", "unknown")
            errors = findings.get("summary", {}).get("errors", 0)
            warnings = findings.get("summary", {}).get("warnings", 0)
            status = "PASS" if errors == 0 else "FAIL"

            lines.append(f"### {artifact_id} ({agent}) - {status}")
            for finding in findings.get("findings", []):
                severity = finding.get("severity", "unknown")
                message = finding.get("message", "")
                lines.append(f"- [{severity}] {message}")
            lines.append("")

    return "\n".join(lines)


def main():
    draft_dir = sys.argv[1] if len(sys.argv) > 1 else str(PROJECT_ROOT / "extraction" / "20_drafts")
    output_dir = PROJECT_ROOT / "extraction" / "25_agent_review"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Running all 4 review agents against {draft_dir}...")
    print(f"Output directory: {output_dir}")

    results = []
    for agent_name, agent_script in AGENTS:
        result = run_agent(agent_name, agent_script, draft_dir)
        results.append(result)

    # Generate summary
    summary_md = generate_summary(results, output_dir)
    summary_file = output_dir / "SUMMARY.md"
    with open(summary_file, "w") as f:
        f.write(summary_md)

    print(f"\n{'='*60}")
    print(f"Summary written to {summary_file}")
    print(f"{'='*60}")

    # Check if any agent had errors
    total_errors = sum(r.get("total_errors", 0) for r in results)
    sys.exit(0 if total_errors == 0 else 1)


if __name__ == "__main__":
    main()
