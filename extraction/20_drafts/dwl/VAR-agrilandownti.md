---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-agrilandownti
canonical_label: "Type of agricultural land ownership document"
variable_name: agrilandownti
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
    label: "Cooperative"
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
  - variable_id: VAR-docuagriland
    condition: "docuagriland = 1"

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
  source_section: "Assets and Dwellings (DWL), Mapping and Description of Variables, Land ownership, Agricultural, agrilandownti"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`agrilandownti` is a categorical variable specifying the type of document a household has to prove agricultural land ownership. Only if docuagriland=1.

## Conceptual intent

Describes the legal basis of agricultural land tenure; customary vs cooperative categories distinguish plot-level from group titles. See dwelownti for definitions.

## Construction notes

Only if docuagriland=1. If the household holds several plots under several types of ownership, collapse plots by area and pick the type covering the largest area. Map to codes 1-6.

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
