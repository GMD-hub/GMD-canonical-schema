# Cross-Variable Country Exceptions — Design Plan

## Goal
Let reviewers author country exceptions whose condition can reference other GMD
variables' harmonized values (not just survey-context `selectors`), in a form
that is structurally validated at authoring time, safe against circular
evaluation order, and directly consumable by a downstream harmonization agent.

## 1. Current state
- Schema: `schema/country_exceptions.py` — `condition_structured` /
  `action_structured` are `dict[str, Any]`, unvalidated.
- Validator: `validation/validate_country_layer.py` — validates
  `applies_to_variables` against known IDs; no validation of condition content.
- Reviewer UI: `country-review-app` — raw YAML editor per draft; `R/models.R`
  only classifies artifact type and checks ID patterns.
- Agent consumption: `build/compile_bundle.py` — bundles universal + country
  layer; no exception dependency graph today.

Precedent already exists at the universal level: `Prerequisite(variable_id,
condition)` in `schema/variable.py`, and `validate_acyclic_derivation_graph`
for `derived_from`.

## 2. Schema changes (Phase A)
- Add `depends_on_variables: list[str] = []` to `CountryExceptionRecord`,
  validated the same way as `applies_to_variables`.
- Replace `condition_structured: dict[str, Any]` with a typed model:
  `ConditionClause(field, op, value)` / `ConditionGroup(all, any)`. Same
  treatment for `action_structured` (`operation`, `target`, params).
- Naming convention: `field` starting with `VAR-` = reference to another GMD
  variable's resolved value; bare snake_case = survey-context selector.
- Consistency validator: every `VAR-` field in `condition_structured` must
  appear in `depends_on_variables` and vice versa.
- Optional: validate literal values against the referenced variable's
  `value_codes`/`allowed_range`.

## 3. Validator changes (Phase A)
- Build a per-country graph: `applies_to_variables -> depends_on_variables`.
- Extend acyclic check across exceptions + the universal `derived_from` graph
  combined.
- Reject self-reference unless explicitly modeled (see open question).
- Add an "Exception dependency graph report" section.

## 4. Agent consumption (Phase B)
- Add a compiled `exception_dependency_graph` section to
  `build/compile_bundle.py` output, topologically ordered.
- Document the runtime contract: resolve all `depends_on_variables` before
  evaluating `condition_structured`.

## 5. Reviewer app changes (Phase D)
- Condition builder widget: variable picker -> operator picker (constrained by
  data_type) -> value picker (value_codes labels when available).
- Auto-sync `depends_on_variables` from clauses referencing `VAR-x`.
- Inline validation before submit via a new `validation/validate_exception_draft.py`
  entrypoint, called from R.
- Auto-generate natural-language `condition`/`action` drafts from structured
  form, editable by reviewer.

## 6. Impact / migration
- Backward compatible by default (`depends_on_variables` defaults to `[]`).
- Existing `PER/exceptions.md` structured record needs reshaping to the new
  clause/group type.
- Bump `schema_version` (0.2 -> 0.3) with change-log entry.
- Update `country-parameters/README.md` and `wiki/Country-Parameter-Layer.md`.
- Extend `tests/test_exception_validation.py` with new negative/positive cases.

## 7. Open question
Should a variable be allowed to reference its own raw (pre-exception) value
in its condition (self-correction pattern)? Needs explicit modeling (e.g. a
`self` sentinel or `raw:` prefix) so it isn't flagged as circular.

## Phasing
A (schema/validator) -> B (bundle/agent contract) -> C (docs) -> D (reviewer app) -> E (migrate PER, add examples)