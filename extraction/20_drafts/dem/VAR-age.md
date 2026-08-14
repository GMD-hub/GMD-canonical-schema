---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-age
canonical_label: "Age of individual (continuous)"
variable_name: age
module_id: MOD-DEM
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: individual
mapping_role: atomic
data_type: numeric

# --- Allowed output values ---
value_codes: null
allowed_range:
  min: 0
  max: 120

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"
  - code: ".c"
    label: "Age not collected in this survey"

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
    - "age"
    - "date of birth"
    - "age in completed years"
    - "how old"
    - "birth date"
  typical_section_names:
    - "Household roster"
    - "Demographics"
    - "Individual characteristics"
    - "Household composition"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Demography (DEM), Mapping and Description of Variables, age"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`age` records the age of each individual in completed years. It refers to the
interval of time between the date of birth and the date of the survey, and is
required for all persons in the household.

## Conceptual intent

`age` is one of the most fundamental demographic variables in the GMD. It is
used for age disaggregation across virtually all modules and is essential for
poverty, welfare, and demographic analysis. It is also a prerequisite for
constructing a wide range of derived variables and for applying age cut-offs
such as `mineducatage` and the under-five indicators.

## Construction notes

Record age in completed years for all persons. Every effort should be made to
determine the precise and accurate age of each person, particularly of children
aged under 5 and older persons.

Age may be secured either by obtaining the date of birth (year, month, and day)
or by asking directly for age at the person's last birthday. Derive completed
years from the date of birth relative to the survey date where the questionnaire
records birth dates.

If age information is not available, code it as missing according to the
instructions under the missing-value-codes section. Do not guestimate age.

## Consistency checks

- `age` must be an integer for persons aged 5 and over. Flag records where
  `age != int(age)`.
- `age` cannot be negative or greater than 120. Flag `(age < 0 | age > 120)`.
- `age` cannot be missing for members who should have a recorded value.
- Cross-check `age` against `childyr` and `childmth` for children under 5:
  age in completed years must be consistent with age in completed months.
- Cross-check `age` against education variables: a small child should not have
  secondary or tertiary completion.

## Escalation triggers

- A large share of records have missing age or implausible age values.
- Age and `childyr`/`childmth` are systematically inconsistent for children
  under 5.
- The survey records age only in broad categories and no continuous age can be
  derived; escalate if precise age is analytically required.

## Common mistakes

- Retaining negative or implausibly high age values (e.g. greater than 120).
- Leaving age missing when the date of birth was collected and could be used to
  compute completed years.
- Confusing age in completed years with age rounded to the nearest birthday.
- Recording age in categories instead of continuous years when the survey
  collected the precise value.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
