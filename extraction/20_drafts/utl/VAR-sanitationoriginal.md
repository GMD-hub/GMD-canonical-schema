---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-sanitationoriginal
canonical_label: "Main toilet facility (country specific)"
variable_name: sanitation_original
module_id: MOD-UTL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: string

# --- Allowed output values ---
value_codes:
  null
allowed_range: null
# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"
  - code: ".c"
    label: "Information not available because the item was not collected in this survey"
  - code: ".o"
    label: "Other value not covered by harmonized codes"
# --- Derivation graph ---
derived_from:
  []
derives_to: []
# --- Country parameter declarations ---
country_parameters: []

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards:
  []
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Access to Services, Water, Sanitation and Hygiene (WASH), sanitation_original"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`sanitation_original` is a string variable that records the original survey response for the main toilet facility, kept verbatim for country-specific reference.

## Conceptual intent

It preserves the raw survey wording so the harmonized `sanitation_source` code can be audited and country-specific categories are not lost.

## Construction notes

Record the original survey response as a string following the naming convention "1 - Flush toilet". This is a country-specific variable.

## Consistency checks

- The string should match the questionnaire wording for the main toilet facility.
- Cross-check that `sanitation_source` can be traced back to a value in `sanitation_original`.

## Escalation triggers

- The survey response cannot be matched to any standardized `sanitation_source` category.

## Common mistakes

- Harmonizing from raw data without preserving this original string.
- Recording a secondary toilet instead of the main facility used by the household.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
