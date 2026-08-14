---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-school
canonical_label: "Currently enrolled in school"
variable_name: school
module_id: MOD-DEM
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: individual
mapping_role: atomic
data_type: binary

# --- Allowed output values ---
value_codes:
  - value: 1
    label: "Yes"
  - value: 0
    label: "No"
allowed_range: null

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"
  - code: ".c"
    label: "Schooling enrollment not collected in this survey"

# --- Derivation graph ---
derived_from: []
derives_to: []

# --- Country parameter declarations ---
# Not a routing instruction. The agent always loads the country layer.
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
    - "currently enrolled in school"
    - "attending school"
    - "enrolled in school"
    - "in school now"
  typical_section_names:
    - "Education"
    - "Schooling"
    - "Individual characteristics"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Demography (DEM), Mapping and Description of Variables, school"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "There is no age cut-off for school, but the country-specific age cut-off
          should be used and not guestimated. If the question was asked only for
          persons older than a certain age, do not guestimate enrolment for the
          younger population; leave as missing."
---

## Definition

`school` is a binary variable indicating whether an individual is currently
enrolled in school. It takes the value 1 if enrolled and 0 if not.

## Conceptual intent

`school` captures current schooling enrollment, in contrast to `everattend`
which captures any past attendance. It is used in education participation and
human capital analysis.

## Construction notes

Code `1 = Yes` for enrolled and `0 = No` for not enrolled. There is no universal
age cut-off for `school`; use the country-specific age cut-off rather than
guestimating.

If the survey asked about enrollment only for persons above a certain age, do
not guestimate enrollment for the younger population; leave it missing.

## Consistency checks

- An individual currently enrolled in school should also have `everattend = 1`.
- `school` enrollment should be consistent with the country's school-age
  structure and `mineducatage`.
- `school` should take only values 0, 1, or a documented missing code.

## Escalation triggers

- Survey enrollment status is ambiguous (e.g. does not distinguish current
  enrollment from recent attendance).
- Inconsistency between `school` and `everattend` beyond what the questionnaire
  would explain.

## Common mistakes

- Confusing `school` (current enrollment) with `everattend` (ever attended).
- Guestimating enrollment for age groups the survey did not ask about.
- Using a standard missing (`.`) instead of an explicit extended missing code.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
