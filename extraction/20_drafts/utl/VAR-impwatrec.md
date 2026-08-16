---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-impwatrec
canonical_label: "Improved water source"
variable_name: imp_wat_rec
module_id: MOD-UTL
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
  - name: "WHO/UNICEF JMP"
    url: https://washdata.org
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Access to Services, Water, Sanitation and Hygiene (WASH), imp_wat_rec"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`imp_wat_rec` is a binary variable that estimates the recommended categorization of access to improved water sources in each country.

## Conceptual intent

It flags whether a household's main water source is improved, following the recommended access that minimizes expected misclassification error and aligns with JMP and SDG monitoring.

## Construction notes

If the survey is on file in the SDG calculations, set 1 if most of the problematic category was estimated improved at the rural level, otherwise 0. Otherwise base recommendations on standard international classifications and relevant country insights; use 0 where there is no evidence.

## Consistency checks

- `imp_wat_rec` should equal 1 when `water_source` is 1 through 8 and 0 when it is 9 through 14, unless country evidence supports an override.
- Cross-validate against external JMP data while recognizing source differences.

## Escalation triggers

- The classification of a problematic source category is disputed between the poverty and WASH teams.
- No evidence exists for a problematic category and a 0 is applied without documentation.

## Common mistakes

- Coding bottled water (7) as unimproved when JMP treats it as improved.
- Overriding the standardized mapping without documenting the country evidence.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
