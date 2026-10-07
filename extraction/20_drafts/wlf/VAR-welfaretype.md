---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.2
# ================================================================

# --- Identity ---
variable_id: VAR-welfaretype
canonical_label: "Welfare aggregate type (poverty)"
variable_name: welfaretype
module_id: MOD-WLF
gmd_version: "3.0"
schema_version: "0.2"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: string

# --- Allowed output values ---
# String classifier. The schema's value_codes carry integer values only, so the
# allowed values are enumerated in prose (see Definition): INC, CONS, EXP.
value_codes: null
allowed_range: null

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because the welfare concept is not documented"

# --- Derivation graph ---
derived_from: []
derives_to: []

# --- Country parameter declarations ---
country_parameters: []

# --- Universe / skip gate ---
gates: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards: []

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "welfare type"
    - "income"
    - "consumption"
    - "expenditure"
    - "welfare concept"
  typical_section_names:
    - "Welfare"
    - "Welfare aggregate"
    - "Methodology"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Welfare aggregates, welfaretype"
  extraction_method: manual
  extracted_on: "2026-09-21"
  human_reviewed: false
  reviewer: null
  notes: "String classifier for the welfare concept underlying welfare /
          welfarenom / welfaredef. Allowed values enumerated in prose because
          value_codes accept integer values only."
---

## Definition

`welfaretype` is a three-letter string that specifies the type of welfare the
country uses for its poverty measurement. It labels the concept carried in
`welfare`, `welfarenom`, and `welfaredef`. Allowed values:

| Value  | Meaning     |
|--------|-------------|
| `INC`  | income      |
| `CONS` | consumption |
| `EXP`  | expenditure |

## Conceptual intent

`welfaretype` records which welfare concept underlies the poverty aggregate so
that downstream users can interpret and compare `welfare` correctly. Income-,
consumption-, and expenditure-based aggregates are not directly comparable, and
this label is what makes the choice explicit rather than implicit.

## Construction notes

Set `welfaretype` from the country's documented welfare concept for
`welfare` / `welfarenom` / `welfaredef`, using exactly one of `INC`, `CONS`, or
`EXP`. Record the value in upper case. Do not infer the concept from the
variable's magnitude; take it from the survey or country methodology.

`welfaretype` is constant across households within a survey. When the poverty
aggregate is delivered as a passthrough, the type follows directly from the
source documentation.

## Consistency checks

- `welfaretype` must be exactly one of `INC`, `CONS`, `EXP` (upper case)
  wherever `welfare` is non-missing.
- The value must be constant across all households in the survey.
- It must agree with the concept described in the survey/country documentation.

## Escalation triggers

- The survey documentation does not state whether welfare is income-,
  consumption-, or expenditure-based.
- Different sources disagree on the welfare concept.
- The aggregate appears to mix concepts (e.g. income for some households,
  consumption for others).

## Common mistakes

- Using lower case or a non-standard abbreviation instead of `INC`/`CONS`/`EXP`.
- Inferring the type from magnitudes rather than documentation.
- Letting `welfaretype` vary across households within one survey.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-09-21 | 0.2     | Initial draft | GPID Team  |
