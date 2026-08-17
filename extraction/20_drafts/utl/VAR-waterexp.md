---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-waterexp
canonical_label: "Total annual consumption of water supply and hot water"
variable_name: water_exp
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
  - VAR-pwaterexp
  - VAR-hwaterexp
derives_to:
  - VAR-utlexp
# --- Country parameter declarations ---
country_parameters: []

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards:
  - name: "COICOP 4.4.1 Water supply"
    url: https://unstats.un.org/unsd/classifications/Econ
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Affordability, Essential variables - Water, Sanitation and Hygiene (WASH), water_exp"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`water_exp` is a continuous aggregate variable of total annual household expenditure on water supply and hot water supply.

## Conceptual intent

It aggregates water supply and hot water into a single water-expenditure indicator, following COICOP 4.4.1.

## Construction notes

Derived as the sum of `pwater_exp` and `hwater_exp` (`egen water_exp=rsum(pwater_exp hwater_exp)`). Surveys reporting only the aggregate may leave the components missing.

## Consistency checks

- `water_exp` should equal `pwater_exp` plus `hwater_exp` when both are present.
- Cross-check that aggregate does not double count hot water.

## Escalation triggers

- Directly reported aggregate differs from the sum of components.

## Common mistakes

- Double counting when hot water is combined with heating.
- Treating missing components (aggregate-only survey) as 0.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
