---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-heatingexp
canonical_label: "Total annual consumption of heating"
variable_name: heating_exp
module_id: MOD-UTL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

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
  - VAR-centralexp
  - VAR-hwaterexp
derives_to: []
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
  source_section: "Utilities (UTL), Affordability, Essential variables - Energy, heating_exp"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`heating_exp` is a continuous aggregate variable of total annual household expenditures on heating.

## Conceptual intent

It aggregates central heating and hot water into a heating-expenditure indicator, following COICOP 4.5.5 (GMD includes all heat energy from building or other sources).

## Construction notes

Derived as the sum of `centralexp` and `hwaterexp`. Be careful to avoid double counting, as hot water is often combined with cold water or central heating.

## Consistency checks

- `heatingexp` should equal `centralexp` plus `hwaterexp` when both are present.
- Verify no double counting where hot water is combined with central heating.

## Escalation triggers

- Double counting when central heating and hot water are combined in raw data.

## Common mistakes

- Including cold water supply in heating expenditure.
- Treating missing components as 0.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
