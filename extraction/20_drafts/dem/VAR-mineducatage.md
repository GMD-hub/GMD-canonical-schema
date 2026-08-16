---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-mineducatage
canonical_label: "Education module application age (country specific)"
variable_name: mineducatage
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
allowed_range: null

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"
  - code: ".c"
    label: "Not specified by survey questionnaire or manual"

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
    - "minimum age for education"
    - "education application age"
    - "school entry age"
    - "education section age"
  typical_section_names:
    - "Education"
    - "Questionnaire manual"
    - "Survey metadata"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Demography (DEM), Mapping and Description of Variables, mineducatage"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "mineducatage is currently an unregistered prerequisite/parameter. This
          draft classifies it as a country-specific variable (numeric age
          threshold). It is a blocking issue for PARAM registration: the value is
          country-specific and should eventually be registered as a country
          parameter (e.g. PARAM-EDU-MIN-EDUCATION-AGE) with per-country records.
          The questionnaire and/or manual specifies the lower age cut-off; if
          unknown, leave missing or ask the Supervisor / Country Poverty
          Economist."
---

## Definition

`mineducatage` is the minimum age for which the education section is applied in
a country. Education variables (such as `educat7`, `educat5`, `educat4`, and
`primarycomp`) are harmonized only for individuals at or above this age.

## Conceptual intent

The lower age cut-off at which education information is collected varies from
country to country. `mineducatage` records this threshold so that education
variables are coded correctly and consistently, and so that individuals below
the cut-off are not guestimated.

## Construction notes

Obtain `mineducatage` from the survey questionnaire and/or manual, which specify
the lower age cut-off at which education information is collected. The value is
country-specific.

If `mineducatage` is unknown, leave it as missing or ask the Supervisor or the
Country Poverty Economist; do not invent a value.

This is a country-specific value. Because it varies by country and survey, it
should ultimately be registered as a country parameter with per-country records;
until such a parameter record exists, this draft treats it as a variable carrying
the country-specific threshold.

## Consistency checks

- `mineducatage` should be consistent with the age below which education is not
  collected in the survey documentation.
- Verify no individual below `mineducatage` receives a non-missing education
  value (`.c` is applied below the threshold).
- Confirm the threshold is non-negative and plausible as a schooling entry age.

## Escalation triggers

- The questionnaire or manual does not specify the lower age cut-off and it
  cannot be confirmed with the Supervisor or Country Poverty Economist.
- Disagreement between the documented cut-off and the point at which education
  values actually begin in the data.

## Common mistakes

- Treating `mineducatage` as a universal (non-country-specific) value.
- Guestimating the threshold when it is unspecified.
- Failing to register the country-specific value as a parameter, which blocks
  downstream PARAM resolution.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
