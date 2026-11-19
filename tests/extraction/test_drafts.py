"""Committed gates over the drafts under extraction/20_drafts/.

A draft is a record being written or revised before it is promoted to
knowledge/. These gates exercise the real drafts, not synthetic fixtures,
and are skipped while nothing is drafted. The gates themselves are in
tests/variable_gates.py; the promoted records pass the same gates in
tests/test_knowledge_variables.py. knowledge/ is only read here, as the
registry the drafts' references resolve against.
"""

import pytest

from schema.missing import validate_missing_set
from schema.variable import validate_acyclic_derivation_graph

import variable_gates as gates

DRAFTS = gates.draft_variables()
DRAFT_MISSING = gates.drafted_missing()
CONTEXT = gates.reference_context(with_drafts=True)

no_variable_drafts = pytest.mark.skipif(
    not DRAFTS, reason="no variables are drafted under extraction/20_drafts/"
)


@no_variable_drafts
def test_all_drafts_validate_frontmatter():
    failures = gates.frontmatter_failures(DRAFTS, CONTEXT)
    assert not failures, "\n".join(failures)


@no_variable_drafts
def test_all_drafts_have_required_body_sections():
    missing = gates.missing_sections(DRAFTS)
    assert not missing, "\n".join(missing)


@no_variable_drafts
def test_no_duplicate_variable_id():
    dupes = gates.duplicate_ids(DRAFTS)
    assert not dupes, f"duplicate variable ids: {dupes}"


@no_variable_drafts
def test_derivation_graph_acyclic():
    """The graph as it would be once the drafts are promoted."""
    records = {path.stem: path for path in gates.knowledge_variables()}
    records.update({path.stem: path for path in DRAFTS})
    variables = [gates.validate(path, CONTEXT) for path in records.values()]
    validate_acyclic_derivation_graph(variables)  # raises on cycle


@no_variable_drafts
def test_no_welfare_leakage_in_drafts():
    hits = gates.welfare_leakage(DRAFTS)
    assert not hits, "potential welfare leakage:\n" + "\n".join(hits)


@no_variable_drafts
def test_every_draft_label_fits_a_stata_variable_label():
    assert gates.long_labels(DRAFTS) == {}


def test_missing_value_drafts_validate():
    """A drafted definition is named after its file and fits the registered set it joins."""
    if not DRAFT_MISSING:
        pytest.skip("no missing value definitions are drafted")
    for stem, definition in DRAFT_MISSING.items():
        assert definition.missing_id == stem
    merged = {**gates.registered_missing(), **DRAFT_MISSING}
    validate_missing_set(list(merged.values()))
