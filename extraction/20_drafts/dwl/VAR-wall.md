---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-wall
canonical_label: "Main material used for external walls"
variable_name: wall
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
    label: "Natural - No wall"
  - value: 12
    label: "Natural - Cane/palm/trunks"
  - value: 13
    label: "Natural - Dirt"
  - value: 14
    label: "Natural - Other"
  - value: 21
    label: "Rudimentary - Bamboo with mud"
  - value: 22
    label: "Rudimentary - Stone with mud"
  - value: 23
    label: "Rudimentary - Uncovered adobe"
  - value: 24
    label: "Rudimentary - Plywood"
  - value: 25
    label: "Rudimentary - Cardboard"
  - value: 26
    label: "Rudimentary - Reused wood"
  - value: 27
    label: "Rudimentary - Other"
  - value: 31
    label: "Finished - Woven Bamboo"
  - value: 32
    label: "Finished - Stone with lime/cement"
  - value: 33
    label: "Finished - Cement blocks"
  - value: 34
    label: "Finished - Covered adobe"
  - value: 35
    label: "Finished - Wood planks/shingles"
  - value: 36
    label: "Finished - Plaster wire"
  - value: 37
    label: "Finished - GRC/Gypsum/Asbestos"
  - value: 38
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
  source_section: "Assets and Dwellings (DWL), Mapping and Description of Variables, Main Dwelling, Materials, wall"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`wall` is a categorical variable indicating the type of material used for external walls, grouped into Natural, Rudimentary, and Finished categories.

## Conceptual intent

A core housing-quality indicator used in dwelling-material indices and shelter-condition analysis.

## Construction notes

Map the raw wall-material category to the harmonized codes. Where the match is imperfect, use the best-fit category or 96 (Other - Specific).

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
