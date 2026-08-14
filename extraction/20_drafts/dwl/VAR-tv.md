---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-tv
canonical_label: "Ownership of a TV"
variable_name: tv
module_id: MOD-DWL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: binary

# --- Allowed output values ---
value_codes:
  - value: 0
    label: "No"
  - value: 1
    label: "Yes"
allowed_range: null

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"
  - code: ".c"
    label: "Information not available because the item was not collected in this survey"

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
    - 'owns'
    - 'have'
    - 'own a'
    - 'does ... have'
  typical_section_names:
    - 'Assets'
    - 'Household assets'
    - 'Appliances'
    - 'Durables'
    - 'Possessions'

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Assets and Dwellings (DWL), Mapping and Description of Variables, Assets, Appliances, tv"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`tv` is a binary dummy variable indicating whether the household owns a TV set, including both color and black-and-white TVs.

## Conceptual intent

A standard media/durable asset indicator widely used in asset-based welfare indices.

## Construction notes

Map the raw television-ownership question to 0/1. Both color and black-and-white sets qualify. `tv` is a prerequisite for `tv_cable`.

## Consistency checks

- Values must be 0 or 1 (or explicitly missing); every household should have a non-missing code or a documented missing reason; verify the variable has variation (not all households share the same value).

## Escalation triggers

- The raw survey does not specify the required category clearly, so the harmonized assignment is ambiguous; more than 2 percent of records fall into `.b` or `.c`; coding patterns indicate imputation from expenditure rather than direct measurement.

## Common mistakes

- Retaining raw numeric placeholders (e.g. 98, 99, 9) as valid values instead of coding them as missing; guessing appliance/asset existence from expenditure or other variables; failing to code values that are not collected as `.c`.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
