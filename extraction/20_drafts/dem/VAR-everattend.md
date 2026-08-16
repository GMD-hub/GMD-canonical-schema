---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-everattend
canonical_label: "Ever attended school"
variable_name: everattend
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
    label: "Ever-attended-school not collected in this survey"

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
    - "ever attended school"
    - "ever attended"
    - "ever been to school"
  typical_section_names:
    - "Education"
    - "Schooling"
    - "Individual characteristics"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Demography (DEM), Mapping and Description of Variables, everattend"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "everattend was included in the GMD harmonization for the first time in the
          December 2023 revision. If there is no information available, it must
          nonetheless be created. Length of attendance is not important; the
          indicator is whether the member ever attended school."
---

## Definition

`everattend` is a binary variable indicating whether a respondent has ever
attended school. It takes the value 1 if the individual has ever attended school
and 0 otherwise.

## Conceptual intent

`everattend` captures lifetime exposure to schooling regardless of current
enrollment or duration. The length of attendance is not important; what matters
is that at some point the member attended school.

## Construction notes

Ask respondents whether they have ever attended school and code `1 = Yes` or
`0 = No`. Do not condition on the length of attendance or on whether the person
is currently enrolled.

The variable must be created even if the survey does not provide direct
information; if no value can be determined, record the appropriate missing code
and document why.

## Consistency checks

- An individual recorded as currently enrolled in school should also have
  `everattend = 1`.
- Cross-check `everattend` against education attainment: anyone with a completed
  education level should have `everattend = 1`.
- `everattend` should take only values 0, 1, or a documented missing code.

## Escalation triggers

- Inconsistency between `everattend` and education attainment or enrollment.
- A large share of the sample missing `everattend` without a documented reason.

## Common mistakes

- Confusing `everattend` with current enrollment (`school`).
- Coding ever-attended as 0 for individuals who attended but are not currently
  enrolled.
- Failing to create the variable at all when the survey lacks it.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
