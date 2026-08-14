---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-internet
canonical_label: "Internet connection"
variable_name: internet
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
    label: "Subscribed in the house"
  - value: 2
    label: "Accessible outside the house (includes internet cafes and smartphones with internet access)"
  - value: 3
    label: "Either (questionnaire does not specify in or outside the house)"
  - value: 4
    label: "No internet"
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
  source_section: "Assets and Dwellings (DWL), Mapping and Description of Variables, Assets, Appliances, internet"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`internet` is a categorical variable indicating whether anyone in the household can use an internet-connected device within the home or have access to the internet outside the house.

## Conceptual intent

Captures the household's access to the internet, wired or wireless, irrespective of who manages the connection.

## Construction notes

Map the raw internet-access question to codes 1-4. Code 4 when the household has no internet access. Use code 3 only when the questionnaire does not specify whether access is inside or outside the house.

## Consistency checks

- The value must be a valid category code (or explicitly missing); every household should have a non-missing code or a documented missing reason; verify the variable has variation.

## Escalation triggers

- The raw survey does not specify the required category clearly, so the harmonized assignment is ambiguous; more than 2 percent of records fall into `.b` or `.c`; coding patterns indicate imputation from expenditure rather than direct measurement.

## Common mistakes

- Retaining raw numeric placeholders (e.g. 98, 99, 9) as valid values instead of coding them as missing; guessing appliance/asset existence from expenditure or other variables; failing to code values that are not collected as `.c`.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
