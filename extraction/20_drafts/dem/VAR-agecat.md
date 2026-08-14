---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-agecat
canonical_label: "Age of individual (categorical)"
variable_name: agecat
module_id: MOD-DEM
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: individual
mapping_role: atomic
data_type: string

# --- Allowed output values ---
value_codes: null
allowed_range: null

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"
  - code: ".c"
    label: "Age categories not collected in this survey"

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
    - "age group"
    - "age category"
    - "age band"
    - "age range"
  typical_section_names:
    - "Household roster"
    - "Demographics"
    - "Individual characteristics"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Demography (DEM), Mapping and Description of Variables, agecat"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "A string variable holding the raw age-group labels. Unlike age (continuous),
          agecat preserves the survey's own category boundaries and is used only when
          age is available in categories rather than in years."
---

## Definition

`agecat` is a string variable that captures the age group of an individual
using the age categories defined in the survey. It is used when information on
age is available only in age categories rather than in continuous years.

## Conceptual intent

`agecat` preserves the survey's original age-band classification (for example,
"15 years or younger", "15-24 years old", "25-54 years old", "55-64 years old",
"65 years or older"). It is the categorical counterpart to the continuous `age`
variable and is retained so downstream consumers can reproduce survey-specific
age groupings when continuous age is unavailable.

## Construction notes

Record the age category exactly as defined in the survey questionnaire. The
category labels are survey- and country-specific, so no standardized coding
scheme is imposed; the labels are carried as strings.

Where continuous `age` is available, prefer it over `agecat` for analysis. Use
`agecat` only when the survey did not collect age in years.

Document the exact category boundaries used by the survey in the do-file notes.

## Consistency checks

- If both `age` and `agecat` are available, verify that each individual's
  continuous age falls within the reported age category.
- Verify that age categories are mutually exclusive and exhaustive as defined by
  the survey.
- Confirm that the raw category labels are preserved verbatim and not
  recoded or truncated.

## Escalation triggers

- Age categories overlap or have ambiguous boundaries (e.g. unclear whether the
  lower bound is inclusive).
- The survey defines open-ended categories but the manual does not clarify upper
  or lower limits.
- `agecat` labels are missing or inconsistent with continuous `age`.

## Common mistakes

- Transcoding the string category labels into numeric codes, losing the original
  survey labels.
- Attempting to use `agecat` when continuous `age` is available and should be
  preferred.
- Truncating or normalizing category labels, making them uninterpretable.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
