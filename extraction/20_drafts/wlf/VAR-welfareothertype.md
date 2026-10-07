---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.2
# ================================================================

# --- Identity ---
variable_id: VAR-welfareothertype
canonical_label: "Alternative welfare aggregate type"
variable_name: welfareothertype
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
    - "alternative welfare type"
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
  source_section: "Welfare aggregates, welfareothertype"
  extraction_method: manual
  extracted_on: "2026-09-21"
  human_reviewed: false
  reviewer: null
  notes: "String classifier for the concept underlying VAR-welfareother.
          Allowed values enumerated in prose because value_codes accept integer
          values only. See VAR-welfaretype."
---

## Definition

`welfareothertype` is a three-letter string that specifies the type of welfare
carried in `welfareother`. It follows the same definition as `welfaretype`.
Allowed values:

| Value  | Meaning     |
|--------|-------------|
| `INC`  | income      |
| `CONS` | consumption |
| `EXP`  | expenditure |

## Conceptual intent

`welfareothertype` records the welfare concept behind the secondary aggregate so
that `welfareother` can be interpreted correctly and distinguished from the
primary welfare series.

## Construction notes

Set `welfareothertype` from the documented concept underlying `welfareother`,
using exactly one of `INC`, `CONS`, or `EXP` in upper case. It is present only
when `welfareother` is present, and is constant across households within a
survey. Leave it missing (`.a`) when `welfareother` is missing.

## Consistency checks

- `welfareothertype` must be exactly one of `INC`, `CONS`, `EXP` (upper case)
  wherever `welfareother` is non-missing.
- It is missing wherever `welfareother` is missing.
- The value must be constant across all households in the survey.

## Escalation triggers

- `welfareother` is present but its concept is not documented.
- Sources disagree on the secondary aggregate's welfare concept.

## Common mistakes

- Setting `welfareothertype` while leaving `welfareother` empty (or vice versa).
- Using lower case or a non-standard abbreviation.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-09-21 | 0.2     | Initial draft | GPID Team  |
