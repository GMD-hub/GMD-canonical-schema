"""Committed gates over the actual hand-drafted CVS variable corpus.

These gates exercise the real artifacts under extraction/20_drafts/, not
synthetic fixtures. They implement the plan's V5 (frontmatter validation),
V5b (7 body sections), C4 (no duplicate variable_id), derivation-graph
acyclicity, and the grep-based welfare-leakage content scan (V6 substitute).
"""

from pathlib import Path

import pytest

from schema.frontmatter import load_markdown
from schema.variable import (
    VariableDefinition,
    validate_acyclic_derivation_graph,
)

ROOT = Path(__file__).resolve().parents[2]  # worktree root
DRAFTS = ROOT / "extraction" / "20_drafts"

# Registered reference sets (derived from the knowledge/ registry).
RULE_IDS = {"RULE-EDU-001", "RULE-EDU-002", "RULE-EDU-003", "RULE-SEX-001"}
PARAM_IDS = {
    "PARAM-DEM-MIN-MARRIAGE-AGE",
    "PARAM-EDU-YEARS-BY-LEVEL",
}
REQUIRED_SECTIONS = [
    "## Definition",
    "## Conceptual intent",
    "## Construction notes",
    "## Consistency checks",
    "## Escalation triggers",
    "## Common mistakes",
    "## Change log",
]


def iter_drafts():
    return sorted(DRAFTS.glob("*/VAR-*.md"))


def test_drafts_exist():
    drafts = list(iter_drafts())
    assert drafts, "no drafts found under extraction/20_drafts/"
    modules = sorted({p.parent.name for p in drafts})
    assert modules, "no draft modules found under extraction/20_drafts/"
    assert {"idn", "geo", "dem", "lbr", "utl", "dwl"} <= set(modules)


def test_all_drafts_validate_frontmatter():
    all_ids = {p.stem for p in iter_drafts()}
    failures = []
    for f in iter_drafts():
        try:
            data, _ = load_markdown(f)
            VariableDefinition.model_validate(
                data,
                context={
                    "allow_unresolved_draft": True,
                    "variable_ids": all_ids,
                    "parameter_ids": PARAM_IDS,
                    "rule_ids": RULE_IDS,
                },
            )
        except Exception as exc:  # noqa: BLE001
            failures.append(f"{f}: {exc}")
    assert not failures, "\n".join(failures)


def test_all_drafts_have_required_body_sections():
    missing = []
    for f in iter_drafts():
        text = f.read_text(encoding="utf-8")
        for section in REQUIRED_SECTIONS:
            if section not in text:
                missing.append(f"{f}: missing {section}")
    assert not missing, "\n".join(missing)


def test_no_duplicate_variable_id():
    ids = [p.stem for p in iter_drafts()]
    dupes = {i for i in ids if ids.count(i) > 1}
    assert not dupes, f"duplicate variable ids: {sorted(dupes)}"


def test_derivation_graph_acyclic():
    all_ids = {p.stem for p in iter_drafts()}
    variables = []
    for f in iter_drafts():
        data, _ = load_markdown(f)
        variables.append(
            VariableDefinition.model_validate(
                data,
                context={
                    "allow_unresolved_draft": True,
                    "variable_ids": all_ids,
                    "parameter_ids": PARAM_IDS,
                    "rule_ids": RULE_IDS,
                },
            )
        )
    validate_acyclic_derivation_graph(variables)  # raises on cycle


def test_no_welfare_leakage_in_drafts():
    """Grep-based welfare-leakage content scan (V6 substitute).

    The pipeline's check_welfare_leakage_content requires structured
    citation objects not present in Markdown drafts, so this grep-based scan
    is the concrete substitute. It requires human sign-off (weaker than the
    content-based detector).
    """
    hits = []
    for f in iter_drafts():
        text = f.read_text(encoding="utf-8").lower()
        for needle in ("chapter8-cons", "chapter-8", "cons.qmd"):
            if needle in text:
                hits.append(f"{f}: {needle}")
    assert not hits, "potential welfare leakage:\n" + "\n".join(hits)
