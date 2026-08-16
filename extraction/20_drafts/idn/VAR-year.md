---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-year
canonical_label: "Survey start year"
variable_name: year
module_id: MOD-IDN
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: survey
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
    label: "Cannot be harmonized because survey start year is not available"

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
external_standards:
  - name: "World Bank survey catalogue metadata guidance"
    url: "https://microdata.worldbank.org/index.php/home"

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "survey year"
    - "year"
    - "year of survey"
    - "survey start year"
  typical_section_names:
    - "Survey metadata"
    - "Identification"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "ID Module (IDN), Mapping and Description of Variables, year"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "The Lessons Learned section recommends the year be a four-digit number in the range of 1980 to the current year (assumed 2020 in the source). The lower bound (1980) is adopted; the upper bound is the current year and is left as an open quality check rather than a fixed allowed_range."
---

## Definition

`year` is a numeric variable that denotes the year in which implementation of
the household survey began. For example, if a survey was implemented during
October 2018 to September 2019, `year` would be 2018.

## Conceptual intent

`year` identifies the survey reference year based on the World Bank survey
catalogue metadata guidance. It is the survey-level temporal key used together
with `countrycode` to attribute results to a specific country-year and to
merge metadata across the harmonized database.

## Construction notes

`year` is the calendar year in which fieldwork began, per World Bank survey
catalogue metadata guidance. It is typically sourced directly from survey
metadata or the survey identification file rather than from a household-level
question.

The year must be a four-digit integer. Verify it falls in a plausible range:
below 1980 or beyond the current year warrants investigation. Use a check such
as `(year<1980 | year>current) & mod(year,1)==0` to flag out-of-range or
non-integer values.

## Consistency checks

- `year` should be a four-digit integer value.
- `year` should not be earlier than 1980 nor later than the current year.
- For surveys spanning multiple calendar years, `year` must equal the year
  fieldwork began, which may differ from `int_year`.

## Escalation triggers

- `year` falls outside the plausible range (before 1980 or in the future)
  without a documented explanation.
- The survey catalogue metadata does not clearly indicate when fieldwork began.

## Common mistakes

- Using the year the data was released or processed rather than the year
  fieldwork began.
- Using the year in which the majority of interviews took place (that is
  `int_year`) instead of the survey start year.
- Recording `year` as a string or with a decimal component.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
