---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-marital
canonical_label: "Marital status"
variable_name: marital
module_id: MOD-DEM
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: individual
mapping_role: atomic
data_type: categorical

# --- Allowed output values ---
value_codes:
  - value: 1
    label: "Never married"
  - value: 2
    label: "Married"
  - value: 3
    label: "Divorced/separated"
  - value: 4
    label: "Widowed"
  - value: 5
    label: "unknown"
allowed_range: null

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"
  - code: ".c"
    label: "Not collected in this survey"

# --- Derivation graph ---
derived_from: []
derives_to: []

# --- Country parameter declarations ---
# Not a routing instruction. The agent always loads the country layer.
country_parameters:
  - PARAM-DEM-MIN-MARRIAGE-AGE

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards: []

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "marital status"
    - "marital"
    - "civil status"
  typical_section_names:
    - "Household roster"
    - "Demographics"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Demography (DEM), Mapping and Description of Variables, marital (calibration fixture)"
  extraction_method: manual
  extracted_on: "2026-08-07"
  human_reviewed: false
  reviewer: null
  notes: "Calibration fixture (not from the extraction pipeline). Carries seeded
          known defects for the calibration run; see known-answer-key.md."
---

## Definition

`marital` records the legal marital status of each individual within the
household as reported in the survey.

## Conceptual intent

`marital` supports household composition and demographic analyses. It is used
as a control in welfare analysis and to identify household heads and partners.

## Construction notes

Map the raw marital-status categories to the five GMD codes. Document the mapping of any survey-specific categories (e.g. "consensual union") in the do-file notes.

## Consistency checks

- An individual's `marital` value must be internally consistent with their age:
  no individual below the minimum legal marriage age should be coded married.
- Cross-check the marital-status distribution against the survey documentation
  and any published tabulations.
- No individual should have a standard missing value (`.`) for `marital`;
  every case must be a valid code or an explicit extended missing code.

## Escalation triggers

- The survey uses marital categories that do not map to the GMD codes (e.g.
  "consensual union" treated inconsistently).
- No valid `PARAM-DEM-MIN-MARRIAGE-AGE` record exists for the survey year and
  the parameter's fallback policy is undecided.
- A large share of the sample falls into the residual or missing categories.

## Common mistakes

- Coding "consensual union" as "Married" without documenting the mapping.
- Using a standard missing (`.`) instead of the appropriate extended missing
  code.
- Guestimating marital status when the raw category is ambiguous.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-07 | 0.1     | Initial fixture | Calibration |
