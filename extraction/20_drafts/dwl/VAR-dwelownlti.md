---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-dwelownlti
canonical_label: "Legal title for ownership of dwelling"
variable_name: dwelownlti
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
  source_section: "Assets and Dwellings (DWL), Mapping and Description of Variables, Main Dwelling, Ownership, dwelownlti"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`dwelownlti` is a binary dummy variable specifying whether a household has legal evidence for ownership of the dwelling.

## Conceptual intent

A tenure-security indicator (secure tenure rights), relevant to SDG 1.4.

## Construction notes

Map the presence of legal evidence of ownership to 0/1. See the chapter's legal-documentation table for what counts as evidence.

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
