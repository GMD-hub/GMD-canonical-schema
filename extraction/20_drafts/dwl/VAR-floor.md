---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-floor
canonical_label: "Main material used for floor"
variable_name: floor
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
  - value: 11
    label: "Natural - Earth/sand"
  - value: 12
    label: "Natural - Dung"
  - value: 13
    label: "Natural - Other"
  - value: 21
    label: "Rudimentary - Wood planks"
  - value: 22
    label: "Rudimentary - Palm/bamboo"
  - value: 23
    label: "Rudimentary - Other"
  - value: 31
    label: "Finished - Parquet or polished wood"
  - value: 32
    label: "Finished - Vinyl or asphalt strips"
  - value: 33
    label: "Finished - Ceramic/marble/granite"
  - value: 34
    label: "Finished - Floor tiles/terrazzo"
  - value: 35
    label: "Finished - Cement/red bricks"
  - value: 36
    label: "Finished - Carpet"
  - value: 37
    label: "Finished - Other"
  - value: 96
    label: "Other - Specific"
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
    - 'material'
    - 'roof'
    - 'wall'
    - 'floor'
    - 'construction material'
  typical_section_names:
    - 'Dwelling characteristics'
    - 'Housing'
    - 'Main material'

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Assets and Dwellings (DWL), Mapping and Description of Variables, Main Dwelling, Materials, floor"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`floor` is a categorical variable indicating the type of material used for floors, grouped into Natural, Rudimentary, and Finished categories.

## Conceptual intent

A core housing-quality indicator; floor material is strongly associated with household welfare.

## Construction notes

Map the raw floor-material category to the harmonized codes. Where the match is imperfect, use the best-fit category or 96 (Other - Specific).

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
