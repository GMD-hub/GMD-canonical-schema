---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-intyear
canonical_label: "Year of household survey interview"
variable_name: int_year
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
value_codes: null
allowed_range: null

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because the interview year is not available"
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
    - "interview year"
    - "date of interview"
    - "month of interview"
    - "survey date"
  typical_section_names:
    - "Household identification"
    - "Interview information"
    - "Household questionnaire cover"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "ID Module (IDN), Mapping and Description of Variables, int_year"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "The variable name in the schema is int_year and it is validated against the 4-digit year rules from the source. The canonical variable_id VAR-intyear uses the no-underscore convention required by the schema."
---

## Definition

`int_year` is a numeric variable recording the 4-digit year of the household
survey interview.

## Conceptual intent

`int_year` captures the year in which the household was interviewed, which may
differ from the survey start year `year`. It supports the `int_month x
int_year` cross-tabulation and is used for analyses that require the actual
timing of data collection rather than the survey reference year.

## Construction notes

When most of the survey data collection was conducted, use the following rules
to assign the reference year:

1. If the period of reference for the survey covers multiple years, use the
   year with most of the survey respondents.
2. If the period of reference is half in one year and half in the other, the
   first year is used.
3. The year is expressed in the Gregorian calendar.

When a precise interview date is recorded, `int_year` is derived from the month
and year of the actual interview for that household.

## Consistency checks

- `int_year` should be a four-digit integer value.
- Cross-tabulate `int_month` against `int_year` to confirm the combination is
  internally consistent.

## Escalation triggers

- `int_year` is outside the plausible range for the survey period without a
  documented explanation.
- The interview date is not recorded, so it cannot be determined whether the
  survey spanned multiple years.

## Common mistakes

- Confusing `int_year` with the survey start year `year`.
- Assigning the year incorrectly when the reference period spans two calendar
  years (should use the year with most respondents, or the first year when
  split evenly).

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
