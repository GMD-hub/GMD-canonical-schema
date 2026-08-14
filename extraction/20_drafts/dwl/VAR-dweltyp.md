---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-dweltyp
canonical_label: "Type of dwelling"
variable_name: dweltyp
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
    label: "Detached house"
  - value: 2
    label: "Multi-family house"
  - value: 3
    label: "Separate apartment"
  - value: 4
    label: "Communal apartment"
  - value: 5
    label: "Room in a larger dwelling"
  - value: 6
    label: "Several buildings connected"
  - value: 7
    label: "Several separate buildings"
  - value: 8
    label: "Improvised housing unit"
  - value: 9
    label: "Other"
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
    - 'dwelling type'
    - 'kitchen'
    - 'bathroom'
    - 'rooms'
    - 'area'
    - 'year built'
  typical_section_names:
    - 'Dwelling'
    - 'Housing characteristics'
    - 'Facilities'

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Assets and Dwellings (DWL), Mapping and Description of Variables, Main Dwelling, Facilities characteristics, dweltyp"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`dweltyp` is a categorical variable specifying the type of dwelling unit the household lives in.

## Conceptual intent

Describes the structural form of the dwelling, a basic housing-conditions indicator.

## Construction notes

Map the raw dwelling-type category to codes 1-9. A separate apartment is a self-contained, non-shared apartment; a communal apartment is shared by two or more families.

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
