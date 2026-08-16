---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-ownhouse
canonical_label: "Ownership of house"
variable_name: ownhouse
module_id: MOD-DWL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: categorical

# --- Allowed output values ---
value_codes:
  - value: 1
    label: "Ownership/secure rights"
  - value: 2
    label: "Renting"
  - value: 3
    label: "Provided for free"
  - value: 4
    label: "Without permission"
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
    - 'own'
    - 'rent'
    - 'tenure'
    - 'ownership'
    - 'title'
    - 'deed'
  typical_section_names:
    - 'Dwelling ownership'
    - 'Tenure'
    - 'Housing tenure'

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Assets and Dwellings (DWL), Mapping and Description of Variables, Main Dwelling, Ownership, ownhouse"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`ownhouse` is a categorical variable specifying whether a household owns, rents, is provided for free, or squats in their house.

## Conceptual intent

A fundamental tenure-status variable feeding ownership, gender, and welfare analyses. It is a prerequisite for several ownership sub-variables.

## Construction notes

Map the raw tenure question to codes 1-4. Ownership includes secure tenure whether or not full payment has been made. Rental denotes regular payment to the owner with or without a formal agreement. `ownhouse` is a prerequisite for `acqui_house`.

## Consistency checks

- The value must be a valid category code (or explicitly missing); every household should have a non-missing code or a documented missing reason; verify the variable has variation.

## Escalation triggers

## Escalation triggers

- The raw survey does not specify the category/measure clearly, so the harmonized assignment is ambiguous; more than 2 percent of records fall into `.b` or `.c`; the source documentation contradicts the harmonized definition.

## Common mistakes

## Common mistakes

- Using raw numeric placeholders (e.g. 98, 99) as valid values instead of coding them as missing; recording a value whose units or category mapping are not sourced from the survey documentation; failing to code values not collected as `.c`.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
