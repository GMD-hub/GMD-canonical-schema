"""Committed gates over the actual hand-drafted CVS variable corpus.

These gates exercise the real artifacts under extraction/20_drafts/, not
synthetic fixtures. They implement the plan's V5 (frontmatter validation),
V5b (7 body sections), C4 (no duplicate variable_id), derivation-graph
acyclicity, and the grep-based welfare-leakage content scan (V6 substitute).
"""

from pathlib import Path

import pytest

from schema.frontmatter import load_markdown
from schema.missing import MissingDefinition, global_missing_ids, validate_missing_set
from schema.parameter import ParameterDefinition
from schema.variable import (
    VariableDefinition,
    validate_acyclic_derivation_graph,
)

ROOT = Path(__file__).resolve().parents[2]  # worktree root
DRAFTS = ROOT / "extraction" / "20_drafts"

# Registered rule references: the knowledge/ registry plus the rules drafted beside the variables
# (a draft rule is cited by draft variables before it is promoted, e.g. RULE-WASH-001).
RULE_IDS = {
    path.stem
    for path in [*(ROOT / "knowledge" / "rules").rglob("RULE-*.md"), *DRAFTS.rglob("RULE-*.md")]
    if "runs" not in path.relative_to(ROOT).parts
}


def missing_definitions(folder: Path) -> dict[str, MissingDefinition]:
    return {
        path.stem: MissingDefinition.model_validate(load_markdown(path)[0])
        for path in sorted(folder.rglob("MISS-*.md"))
        if "runs" not in path.relative_to(ROOT).parts
    }


# Registered missing value references: the knowledge/ registry, where a definition drafted beside
# the variables takes the place of its registered version (a draft definition is cited by draft
# variables before it is promoted). The registry is only read here; its own records are tested
# in tests/test_missing_definitions.py.
DRAFT_MISSING = missing_definitions(DRAFTS)
MISSING = {**missing_definitions(ROOT / "knowledge"), **DRAFT_MISSING}
MISSING_IDS = set(MISSING)
# The definitions of global scope apply to every variable: a variable must not list them.
GLOBAL_MISSING_IDS = global_missing_ids(list(MISSING.values()))
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


@pytest.fixture(scope="module")
def parameter_ids() -> set[str]:
    # the knowledge/ registry plus the parameters drafted beside the variables (a draft parameter is
    # cited by draft variables before it is promoted, as a draft rule is)
    paths = sorted(
        [*(ROOT / "knowledge" / "parameters").glob("*.md"), *DRAFTS.glob("parameters/PARAM-*.md")]
    )
    assert paths, "no canonical parameter definitions found"
    return {
        ParameterDefinition.model_validate(load_markdown(path)[0]).parameter_id
        for path in paths
    }


def test_drafts_exist():
    drafts = list(iter_drafts())
    assert drafts, "no drafts found under extraction/20_drafts/"
    modules = sorted({p.parent.name for p in drafts})
    assert modules, "no draft modules found under extraction/20_drafts/"
    assert {"idn", "geo", "dem", "lbr", "utl", "dwl"} <= set(modules)


def test_all_drafts_validate_frontmatter(parameter_ids: set[str]):
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
                    "parameter_ids": parameter_ids,
                    "rule_ids": RULE_IDS,
                    "missing_ids": MISSING_IDS,
                    "global_missing_ids": GLOBAL_MISSING_IDS,
                },
            )
        except Exception as exc:  # noqa: BLE001
            failures.append(f"{f}: {exc}")
    assert not failures, "\n".join(failures)


def test_unregistered_parameter_is_rejected(parameter_ids: set[str]):
    data, _ = load_markdown(DRAFTS / "dem" / "VAR-male.md")
    data["country_parameters"] = ["PARAM-EDU-NOT-REGISTERED"]

    with pytest.raises(ValueError, match="unknown parameter IDs"):
        VariableDefinition.model_validate(
            data,
            context={
                "allow_unresolved_draft": True,
                "variable_ids": {p.stem for p in iter_drafts()},
                "parameter_ids": parameter_ids,
                "rule_ids": RULE_IDS,
                "missing_ids": MISSING_IDS,
                "global_missing_ids": GLOBAL_MISSING_IDS,
            },
        )


def test_unregistered_missing_id_is_rejected(parameter_ids: set[str]):
    data, _ = load_markdown(DRAFTS / "dem" / "VAR-male.md")
    data["missing_codes"] = ["MISS-NOT-REGISTERED"]

    with pytest.raises(ValueError, match="unknown missing IDs"):
        VariableDefinition.model_validate(
            data,
            context={
                "allow_unresolved_draft": True,
                "variable_ids": {p.stem for p in iter_drafts()},
                "parameter_ids": parameter_ids,
                "rule_ids": RULE_IDS,
                "missing_ids": MISSING_IDS,
                "global_missing_ids": GLOBAL_MISSING_IDS,
            },
        )


def test_global_missing_id_is_not_listed_by_a_variable(parameter_ids: set[str]):
    assert "MISS-MISSING-INPUT" in GLOBAL_MISSING_IDS
    data, _ = load_markdown(DRAFTS / "dem" / "VAR-male.md")
    data["missing_codes"] = ["MISS-MISSING-INPUT"]

    with pytest.raises(ValueError, match="global scope"):
        VariableDefinition.model_validate(
            data,
            context={
                "allow_unresolved_draft": True,
                "variable_ids": {p.stem for p in iter_drafts()},
                "parameter_ids": parameter_ids,
                "rule_ids": RULE_IDS,
                "missing_ids": MISSING_IDS,
                "global_missing_ids": GLOBAL_MISSING_IDS,
            },
        )


def test_missing_value_drafts_validate():
    """A drafted definition is named after its file and fits the registered set it joins."""
    if not DRAFT_MISSING:
        pytest.skip("no missing value definitions are drafted")
    for stem, definition in DRAFT_MISSING.items():
        assert definition.missing_id == stem
    validate_missing_set(list(MISSING.values()))


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


def test_derivation_graph_acyclic(parameter_ids: set[str]):
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
                    "parameter_ids": parameter_ids,
                    "rule_ids": RULE_IDS,
                    "missing_ids": MISSING_IDS,
                    "global_missing_ids": GLOBAL_MISSING_IDS,
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
