---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-landownti
canonical_label: "Residential land ownership type of document"
variable_name: landownti
module_id: MOD-DWL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 2

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: categorical

# --- Allowed output values ---
value_codes:
  - value: 1
    label: "Title; deed"
  - value: 2
    label: "Leasehold (govt issued)"
  - value: 3
    label: "Customary land certificate/plot level"
  - value: 4
    label: "Customary based / group right"
  - value: 5
    label: "Cooperative group right"
  - value: 6
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
prerequisites:
  - variable_id: VAR-ownland
    condition: "ownland = 1"

# --- Cross-references ---
rules: []
exceptions: []
external_standards: []

# --- Discovery hints ---
source_hints:
  question_keywords:
    - 'land ownership'
    - 'residential land'
    - 'title'
    - 'deed'
    - 'sell land'
    - 'transfer land'
  typical_section_names:
    - 'Land ownership'
    - 'Residential land'

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Assets and Dwellings (DWL), Mapping and Description of Variables, Land ownership, Residential, landownti"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`landownti` is a categorical variable specifying the type of document a household has to prove residential land ownership. Only for landowners (ownland=1).

## Conceptual intent

Describes the legal basis of residential land tenure; customary vs cooperative categories distinguish plot-level from group titles.

## Construction notes

Only for landowners (ownland=1). If the household holds plots under several types of ownership, collapse plots by area and pick the type covering the largest area. Map to codes 1-6.

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
