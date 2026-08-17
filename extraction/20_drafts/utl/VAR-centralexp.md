---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-centralexp
canonical_label: "Total annual consumption of central heating"
variable_name: central_exp
module_id: MOD-UTL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: numeric_continuous

# --- Allowed output values ---
value_codes:
  null
allowed_range: null
# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"
  - code: ".c"
    label: "Information not available because the item was not collected in this survey"
  - code: ".o"
    label: "Other value not covered by harmonized codes"
# --- Derivation graph ---
derived_from:
  []
derives_to:
  - VAR-heatingexp
  - VAR-utlexp
# --- Country parameter declarations ---
country_parameters: []

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards:
  - name: "COICOP 4.5.5 Heat energy"
    url: https://unstats.un.org/unsd/classifications/Econ
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Affordability, Essential variables - Energy, central_exp"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`central_exp` is a continuous variable that refers to total annual household expenditure on central heating.

## Conceptual intent

It captures central heating expenditure, a component of heating expenditure following COICOP 4.5.5.

## Construction notes

Record total annual household expenditure on central heating. Note expenditure for central heating is frequently combined with hot water or rent.

## Consistency checks

- Cross-check that `heatingexp` includes `centralexp`.
- Cross-check against `centralacc` access where available.

## Escalation triggers

- Central heating is combined with hot water or rent in the survey.

## Common mistakes

- Double counting when central heating is combined with hot water.
- Including rent in central heating expenditure.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
