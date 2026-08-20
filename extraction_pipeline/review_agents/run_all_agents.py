"""Runner script: execute all review agents and produce SUMMARY.md.

Usage:
    .venv/bin/python -m extraction_pipeline.review_agents.run_all_agents
    .venv/bin/python -m extraction_pipeline.review_agents.run_all_agents --drafts-dir extraction/20_drafts/ --output-dir extraction/25_agent_review/
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

from .consistency_derivation import check_drafts as consistency_check
from .helpers import list_drafts, list_parameter_ids, load_draft, write_findings
from .models import AgentFindings
from .rules_caveats import check_draft as rules_check
from .schema_compliance import check_draft as schema_check
from .source_grounding import check_draft as source_check


def _purge_stale_findings(
    all_findings: list[AgentFindings], output_dir: Path
) -> None:
    """Delete output_dir/*.yml findings whose artifact_id is no longer in the
    current corpus.

    The runner only ever writes findings via write_findings; without this,
    entries for drafts that were removed or excluded from the corpus would
    persist as stale yml files and drift from SUMMARY.md.
    """
    if not output_dir.is_dir():
        return
    expected = {f.artifact_id for f in all_findings}
    for path in output_dir.glob("*.yml"):
        if path.name.endswith(".yml") and path.stem.split(".")[0] not in expected:
            path.unlink()


def _write_summary(all_findings: list[AgentFindings], output_dir: Path) -> Path:
    """Generate SUMMARY.md with aggregated results table."""
    output_dir.mkdir(parents=True, exist_ok=True)
    summary_path = output_dir / "SUMMARY.md"

    total_errors = sum(f.summary.errors for f in all_findings)
    total_warnings = sum(f.summary.warnings for f in all_findings)

    lines: list[str] = [
        "# Agent Review Summary",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        "",
        f"**Total errors:** {total_errors} | **Total warnings:** {total_warnings}",
        "",
        "## Results Table",
        "",
        "| Artifact | Agent | Errors | Warnings | Passed |",
        "|----------|-------|--------|----------|--------|",
    ]

    for f in all_findings:
        passed = "yes" if f.summary.passed else "no"
        lines.append(
            f"| {f.artifact_id} | {f.agent} | {f.summary.errors} | {f.summary.warnings} | {passed} |"
        )

    lines.append("")
    lines.append("## Per-Artifact Findings")
    lines.append("")

    for f in all_findings:
        if not f.findings:
            continue
        lines.append(f"### {f.artifact_id} ({f.agent})")
        lines.append("")
        for finding in f.findings:
            line_info = f" (line {finding.line})" if finding.line else ""
            lines.append(f"- **{finding.severity}** [{finding.field}]{line_info}: {finding.message}")
        lines.append("")

    summary_path.write_text("\n".join(lines), encoding="utf-8")
    return summary_path


def run(
    drafts_dir: Path,
    output_dir: Path,
) -> tuple[list[AgentFindings], int]:
    """Execute all agents against drafts. Returns (findings, exit_code)."""
    draft_paths = list_drafts(drafts_dir)
    if not draft_paths:
        print(f"No drafts found in {drafts_dir}", file=sys.stderr)
        return [], 0

    variable_ids = set()
    rule_ids = set()
    has_any_country_params = False
    for path in draft_paths:
        data, _ = load_draft(path)
        vid = data.get("variable_id", "")
        if vid:
            variable_ids.add(vid)
        for rule_id in data.get("rules", []):
            rule_ids.add(rule_id)
        if data.get("country_parameters"):
            has_any_country_params = True

    registry_dir = Path(__file__).resolve().parents[2] / "knowledge" / "parameters"
    parameter_ids, skipped_params = list_parameter_ids(registry_dir)

    if skipped_params:
        print(f"Skipped parameter files: {skipped_params}", file=sys.stderr)

    if not parameter_ids and has_any_country_params:
        print(
            "ERROR: parameter registry is empty or missing, but drafts declare "
            "country_parameters references. Aborting to prevent false positives.",
            file=sys.stderr,
        )
        return [], 1

    all_findings: list[AgentFindings] = []

    for path in draft_paths:
        all_findings.append(schema_check(path, variable_ids, parameter_ids=parameter_ids, rule_ids=rule_ids))
        all_findings.append(source_check(path))
        all_findings.append(rules_check(path))

    all_findings.extend(consistency_check(draft_paths))

    _purge_stale_findings(all_findings, output_dir)

    for findings in all_findings:
        write_findings(findings, output_dir)

    _write_summary(all_findings, output_dir)

    has_errors = any(f.summary.errors > 0 for f in all_findings)

    print(f"Checked {len(draft_paths)} drafts with 4 agents")
    print(f"Total findings: {sum(len(f.findings) for f in all_findings)}")
    print(f"Errors: {sum(f.summary.errors for f in all_findings)}")
    print(f"Warnings: {sum(f.summary.warnings for f in all_findings)}")

    return all_findings, 1 if has_errors else 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Run all review agents")
    parser.add_argument(
        "drafts_dir",
        nargs="?",
        default="extraction/20_drafts",
        help="Directory containing extraction drafts (default: extraction/20_drafts)",
    )
    parser.add_argument(
        "--output-dir",
        default="extraction/25_agent_review",
        help="Output directory for findings (default: extraction/25_agent_review)",
    )
    args = parser.parse_args()

    drafts_dir = Path(args.drafts_dir)
    output_dir = Path(args.output_dir)

    if not drafts_dir.is_dir():
        print(f"Error: {drafts_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    _, exit_code = run(drafts_dir, output_dir)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()