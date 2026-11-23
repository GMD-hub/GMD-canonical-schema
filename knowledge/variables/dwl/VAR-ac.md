---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-ac
canonical_label: "Ownership of an air conditioner"
variable_name: ac
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
missing_codes: []

# --- Derivation graph ---
derived_from: []
derives_to: []

# --- Country parameter declarations ---
# Not a routing instruction. The agent always loads the country layer.
country_parameters:
  - PARAM-MAX-MISSING-SHARE

# --- Universe / skip gate ---
gates: []

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
  source_section: "Assets and Dwellings (DWL), Mapping and Description of Variables, Assets, Appliances, ac"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`ac` is a binary dummy variable indicating whether the household owns a central or wall air conditioner, including air coolers.

## Conceptual intent

An asset strongly correlated with high welfare levels; useful in asset-based wealth indices.

## Construction notes

Map the raw air-conditioning question to 0/1. Both wall/central air conditioners and air coolers qualify.

## Consistency checks

- Values must be 0 or 1 (or explicitly missing); every household should have a non-missing code or a documented missing reason; verify the variable has variation (not all households share the same value).

## Escalation triggers

- The raw survey does not specify the required category clearly, so the harmonized assignment is ambiguous; the share of records with a missing value exceeds `PARAM-MAX-MISSING-SHARE`; coding patterns indicate imputation from expenditure rather than direct measurement.

## Common mistakes

- Retaining raw numeric placeholders (e.g. 98, 99, 9) as valid values instead of coding them as missing; guessing appliance/asset existence from expenditure or other variables; failing to code values that are not collected as `MISS-NOT-AVAILABLE`.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
