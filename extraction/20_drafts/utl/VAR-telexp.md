---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-telexp
canonical_label: "Total annual consumption of all phones"
variable_name: tel_exp
module_id: MOD-UTL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 2

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: derived
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
  - VAR-landphoneexp
  - VAR-cellphoneexp
derives_to: []
# --- Country parameter declarations ---
country_parameters: []

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards:
  - name: "COICOP 8.3.0"
    url: https://unstats.un.org/unsd/classifications/Econ
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Affordability, Additional variables, tel_exp"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`tel_exp` is a continuous aggregate variable of total annual household expenditures on landline phone and cell phone.

## Conceptual intent

It aggregates landline and cell phone expenditure into a telephone-expenditure indicator, following COICOP 8.3.0.

## Construction notes

Derived as the sum of `landphoneexp` and `cellphoneexp` (`egen tel_exp=rsum(landphone cellphone)`). Includes installation/subscription and call costs; excludes equipment. Surveys reporting only the aggregate may leave components missing.

## Consistency checks

- `telexp` should equal `landphoneexp` plus `cellphoneexp` when both are present.
- Cross-check that `commexp` and `tvintphexp` include `telexp`.

## Escalation triggers

- Directly reported aggregate differs from the sum of components.

## Common mistakes

- Including telephone equipment.
- Treating missing components as 0.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
