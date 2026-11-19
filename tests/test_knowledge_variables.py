"""Committed gates over the variable records under knowledge/variables/.

These gates exercise the real records, not synthetic fixtures. The gates
themselves are in tests/variable_gates.py; the drafts under
extraction/20_drafts/ pass the same gates in tests/extraction/test_drafts.py.
"""

import pytest

from schema.frontmatter import load_markdown
from schema.variable import VariableDefinition, validate_acyclic_derivation_graph

import variable_gates as gates

VARIABLES = gates.knowledge_variables()
CONTEXT = gates.reference_context(with_drafts=False)
SAMPLE = gates.KNOWLEDGE / "variables" / "dem" / "VAR-male.md"


def test_variables_exist():
    assert VARIABLES, "no variables found under knowledge/variables/"
    modules = {path.parent.name for path in VARIABLES}
    assert {"idn", "geo", "dem", "lbr", "utl", "dwl"} <= modules


def test_all_variables_validate_frontmatter():
    failures = gates.frontmatter_failures(VARIABLES, CONTEXT)
    assert not failures, "\n".join(failures)


def test_unregistered_parameter_is_rejected():
    data, _ = load_markdown(SAMPLE)
    data["country_parameters"] = ["PARAM-EDU-NOT-REGISTERED"]

    with pytest.raises(ValueError, match="unknown parameter IDs"):
        VariableDefinition.model_validate(data, context=CONTEXT)


def test_unregistered_missing_id_is_rejected():
    data, _ = load_markdown(SAMPLE)
    data["missing_codes"] = ["MISS-NOT-REGISTERED"]

    with pytest.raises(ValueError, match="unknown missing IDs"):
        VariableDefinition.model_validate(data, context=CONTEXT)


def test_global_missing_id_is_not_listed_by_a_variable():
    assert "MISS-MISSING-INPUT" in CONTEXT["global_missing_ids"]
    data, _ = load_markdown(SAMPLE)
    data["missing_codes"] = ["MISS-MISSING-INPUT"]

    with pytest.raises(ValueError, match="global scope"):
        VariableDefinition.model_validate(data, context=CONTEXT)


def test_all_variables_have_required_body_sections():
    missing = gates.missing_sections(VARIABLES)
    assert not missing, "\n".join(missing)


def test_no_duplicate_variable_id():
    dupes = gates.duplicate_ids(VARIABLES)
    assert not dupes, f"duplicate variable ids: {dupes}"


def test_derivation_graph_acyclic():
    variables = [gates.validate(path, CONTEXT) for path in VARIABLES]
    validate_acyclic_derivation_graph(variables)  # raises on cycle


def test_no_welfare_leakage():
    hits = gates.welfare_leakage(VARIABLES)
    assert not hits, "potential welfare leakage:\n" + "\n".join(hits)
