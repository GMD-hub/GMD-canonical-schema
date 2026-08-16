"""Agent 4: Consistency and derivation checks for extraction drafts.

Checks derived_from/derives_to symmetry, acyclic derivation graph,
module consistency, value code consistency, and prerequisite existence.
Requires loading all drafts to build the full derivation graph.
"""

from __future__ import annotations

from pathlib import Path

from .helpers import load_draft, make_findings
from .models import AgentFindings, Finding

AGENT_NAME = "consistency_derivation"


def _check_derivation_symmetry(
    all_variables: dict[str, dict],
) -> dict[str, list[Finding]]:
    """Check derived_from/derives_to symmetry across all variables.

    If A derives_from B, then B must derive_to A.
    Returns findings keyed by the variable that has the wrong derived_from.
    """
    findings_by_var: dict[str, list[Finding]] = {}
    for vid, data in all_variables.items():
        derived_from = set(data.get("derived_from", []))
        for source_id in derived_from:
            if source_id in all_variables:
                source_derives_to = set(all_variables[source_id].get("derives_to", []))
                if vid not in source_derives_to:
                    f = Finding(
                        field="derived_from",
                        severity="error",
                        message=(
                            f"Asymmetry: {vid} derives_from {source_id}, "
                            f"but {source_id} derives_to {list(source_derives_to)} "
                            f"(missing {vid})"
                        ),
                    )
                    findings_by_var.setdefault(vid, []).append(f)
    return findings_by_var


def _check_derivation_cycles(all_variables: dict[str, dict]) -> dict[str, list[Finding]]:
    """Check the derivation graph is acyclic via DFS. Returns findings per variable."""
    findings_by_var: dict[str, list[Finding]] = {}
    graph: dict[str, set[str]] = {
        vid: set(data.get("derived_from", []))
        for vid, data in all_variables.items()
    }
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> bool:
        if node in visiting:
            f = Finding(
                field="derived_from",
                severity="error",
                message=f"Derivation cycle detected at {node}",
            )
            findings_by_var.setdefault(node, []).append(f)
            return True
        if node in visited:
            return False
        visiting.add(node)
        for dep in graph.get(node, set()):
            if dep in graph:
                if visit(dep):
                    return True
        visiting.remove(node)
        visited.add(node)
        return False

    for vid in graph:
        visit(vid)
    return findings_by_var


def _check_module_consistency(
    artifact_id: str, data: dict, all_variables: dict[str, dict]
) -> list[Finding]:
    """Check cross-module derivations as warnings."""
    findings: list[Finding] = []
    this_module = data.get("module_id", "")
    for dep in data.get("derived_from", []):
        if dep in all_variables:
            dep_module = all_variables[dep].get("module_id", "")
            if dep_module and this_module and dep_module != this_module:
                findings.append(Finding(
                    field="derived_from",
                    severity="warning",
                    message=(
                        f"Cross-module derivation: {artifact_id} ({this_module}) "
                        f"derives_from {dep} ({dep_module})"
                    ),
                ))
    return findings


def _check_value_code_consistency(
    artifact_id: str, data: dict[str, dict], all_variables: dict[str, dict]
) -> list[Finding]:
    """Check derived variable's codes are subset of source codes.

    Handle value_codes: null gracefully (continuous variable, no codes to check).
    """
    findings: list[Finding] = []
    value_codes = data.get("value_codes")
    if value_codes is None:
        return findings

    derived_values = {vc["value"] for vc in value_codes}
    for dep in data.get("derived_from", []):
        if dep not in all_variables:
            continue
        dep_codes = all_variables[dep].get("value_codes")
        if dep_codes is None:
            continue
        source_values = {vc["value"] for vc in dep_codes}
        if not derived_values.issubset(source_values):
            extra = derived_values - source_values
            findings.append(Finding(
                field="value_codes",
                severity="warning",
                message=(
                    f"Value codes of {artifact_id} include {sorted(extra)} "
                    f"not present in source {dep}"
                ),
            ))
    return findings


def _check_prerequisites_exist(
    data: dict[str, dict], all_variables: dict[str, dict]
) -> list[Finding]:
    """Check that prerequisites reference existing or noted-as-unextracted variables."""
    findings: list[Finding] = []
    for prereq in data.get("prerequisites", []):
        prereq_id = prereq.get("variable_id", "")
        if prereq_id and prereq_id not in all_variables:
            findings.append(Finding(
                field="prerequisites",
                severity="warning",
                message=f"Prerequisite {prereq_id} not found in extracted drafts",
            ))
    return findings


def _check_unresolved_derivation_refs(
    data: dict[str, dict], all_variables: dict[str, dict]
) -> list[Finding]:
    """Check that derived_from references exist in the draft set."""
    findings: list[Finding] = []
    for dep in data.get("derived_from", []):
        if dep not in all_variables:
            findings.append(Finding(
                field="derived_from",
                severity="warning",
                message=f"Unresolved derivation reference: {dep} not found in extracted drafts",
            ))
    return findings


def check_drafts(draft_paths: list[Path]) -> list[AgentFindings]:
    """Run consistency/derivation checks across all drafts.

    Returns one AgentFindings per draft.
    """
    all_data: dict[str, dict] = {}
    all_bodies: dict[str, str] = {}

    for path in draft_paths:
        data, body = load_draft(path)
        vid = data.get("variable_id", path.stem)
        all_data[vid] = data
        all_bodies[vid] = body

    symmetry_findings = _check_derivation_symmetry(all_data)
    cycle_findings = _check_derivation_cycles(all_data)

    results: list[AgentFindings] = []
    for vid, data in all_data.items():
        findings: list[Finding] = []

        findings.extend(symmetry_findings.get(vid, []))
        findings.extend(cycle_findings.get(vid, []))

        findings.extend(_check_module_consistency(vid, data, all_data))
        findings.extend(_check_value_code_consistency(vid, data, all_data))
        findings.extend(_check_prerequisites_exist(data, all_data))
        findings.extend(_check_unresolved_derivation_refs(data, all_data))

        results.append(make_findings(AGENT_NAME, vid, findings))

    return results