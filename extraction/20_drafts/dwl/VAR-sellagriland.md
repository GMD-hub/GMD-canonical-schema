---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-sellagriland
canonical_label: "Right to sell agricultural land"
variable_name: sellagriland
module_id: MOD-DWL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 2

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
prerequisites:
  - variable_id: VAR-ownagriland
    condition: "ownagriland = 1"

# --- Cross-references ---
rules: []
exceptions: []
external_standards:
  - name: 'FAO World Programme for the Census of Agriculture 2020'
    url: 'http://www.fao.org/3/a-i4913e.pdf'

# --- Discovery hints ---
source_hints:
  question_keywords:
    - 'agricultural land'
    - 'farm land'
    - 'plot'
    - 'hectares'
    - 'cultivated land'
  typical_section_names:
    - 'Agricultural land'
    - 'Land'
    - 'Farm holdings'

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Assets and Dwellings (DWL), Mapping and Description of Variables, Land ownership, Agricultural, sellagriland"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`sellagriland` is a binary dummy variable specifying whether the respondent has alienation rights (the right to sell) for their agricultural land. Only if ownagriland=1.

## Conceptual intent

A tenure-rights indicator capturing the ability to alienate agricultural land.

## Construction notes

Only if ownagriland=1. Map the alienation-rights question to 0/1.

## Consistency checks

- Values must be 0 or 1 (or explicitly missing); every household should have a non-missing code or a documented missing reason; verify the variable has variation (not all households share the same value).

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
