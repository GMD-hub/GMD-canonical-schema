---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-intmonth
canonical_label: "Month of household survey interview"
variable_name: int_month
module_id: MOD-IDN
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: numeric

# --- Allowed output values ---
value_codes:
  - value: 1
    label: "January"
  - value: 2
    label: "February"
  - value: 3
    label: "March"
  - value: 4
    label: "April"
  - value: 5
    label: "May"
  - value: 6
    label: "June"
  - value: 7
    label: "July"
  - value: 8
    label: "August"
  - value: 9
    label: "September"
  - value: 10
    label: "October"
  - value: 11
    label: "November"
  - value: 12
    label: "December"
allowed_range:
  min: 1
  max: 12

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because the interview month is not available"
  - code: ".c"
    label: "Information not available because the interview date was not collected in this survey"

# --- Derivation graph ---
derived_from: []
derives_to: []

# --- Country parameter declarations ---
country_parameters: []

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards: []

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "interview date"
    - "interview month"
    - "month of interview"
    - "date of interview"
    - "survey date"
  typical_section_names:
    - "Household identification"
    - "Interview information"
    - "Household questionnaire cover"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "ID Module (IDN), Mapping and Description of Variables, int_month"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "The Gregorian calendar month is used, or the closest approximation available in the raw data. Value codes 1-12 map directly to the source listing."
---

## Definition

`int_month` is a numeric variable that specifies the month in which the survey
questionnaire was administered to the household, in the Gregorian calendar or
the closest approximation. Values range from 1 (January) to 12 (December).

## Conceptual intent

`int_month` captures the month of the household interview, complementing
`int_year` to give the timing of data collection. It is essential for
seasonality analysis and for checking the internal consistency of interview
dates.

## Construction notes

Map the raw interview month directly to the GMD numeric code, where
1 = January, 2 = February, ..., 12 = December. Months are expressed in the
Gregorian calendar or the closest approximation available in the raw data.

Cross-tabulate `int_month` against `int_year` to confirm internal consistency.

## Consistency checks

- `int_month` must be an integer between 1 and 12 for every non-missing
  observation.
- `int_month` combined with `int_year` must form a valid interview date.

## Escalation triggers

- `int_month` falls outside the range 1-12.
- The recorded interview month is inconsistent with the survey field period or
  with `int_year`.

## Common mistakes

- Using the reference/recall month rather than the actual interview month.
- Mapping month names incorrectly when the raw survey uses a non-Gregorian
  calendar or a different month numbering.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
