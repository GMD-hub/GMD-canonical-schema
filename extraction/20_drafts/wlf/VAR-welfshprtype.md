---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.2
# ================================================================

# --- Identity ---
variable_id: VAR-welfshprtype
canonical_label: "Welfare aggregate type (shared prosperity)"
variable_name: welfshprtype
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
# String classifier; allowed values enumerated in prose: INC, CONS, EXP.
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
    - "shared prosperity welfare type"
    - "income"
    - "consumption"
    - "expenditure"
    - "welfare concept"
  typical_section_names:
    - "Welfare"
    - "Shared prosperity"
    - "Methodology"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Welfare aggregates, welfshprtype"
  extraction_method: manual
  extracted_on: "2026-09-21"
  human_reviewed: false
  reviewer: null
  notes: "String classifier for the concept underlying VAR-welfshprosperity.
          Allowed values enumerated in prose because value_codes accept integer
          values only. See VAR-welfaretype."
---

## Definition

`welfshprtype` is a three-letter string that specifies the type of welfare used
for the shared prosperity aggregate `welfshprosperity`. It follows the same
definition as `welfaretype`. Allowed values:

| Value  | Meaning     |
|--------|-------------|
| `INC`  | income      |
| `CONS` | consumption |
| `EXP`  | expenditure |

## Conceptual intent

`welfshprtype` records the welfare concept behind the shared prosperity measure
so that it can be interpreted and compared correctly, and so any difference from
the poverty concept (`welfaretype`) is explicit rather than assumed.

## Construction notes

Set `welfshprtype` from the documented concept underlying `welfshprosperity`,
using exactly one of `INC`, `CONS`, or `EXP` in upper case. When
`welfshprosperity` equals `welfare`, set `welfshprtype` equal to `welfaretype`.
The value is constant across households within a survey.

## Consistency checks

- `welfshprtype` must be exactly one of `INC`, `CONS`, `EXP` (upper case)
  wherever `welfshprosperity` is non-missing.
- It must equal `welfaretype` whenever `welfshprosperity` equals `welfare`.
- The value must be constant across all households in the survey.

## Escalation triggers

- The concept behind the shared-prosperity aggregate is not documented.
- Sources disagree on the shared-prosperity welfare concept.

## Common mistakes

- Assuming `welfshprtype` equals `welfaretype` without confirming the aggregates
  are the same.
- Using lower case or a non-standard abbreviation.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-09-21 | 0.2     | Initial draft | GPID Team  |
