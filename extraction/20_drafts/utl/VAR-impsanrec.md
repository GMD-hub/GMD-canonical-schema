---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-impsanrec
canonical_label: "Improved sanitation facility"
variable_name: imp_san_rec
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
  source_section: "Utilities (UTL), Access to Services, Water, Sanitation and Hygiene (WASH), imp_san_rec"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`imp_san_rec` is a binary variable that estimates the recommended categorization of access to improved sanitation facilities in each country.

## Conceptual intent

It flags whether a household's sanitation facility is improved according to recommended access, minimizing expected misclassification and aligning with JMP/SDG monitoring.

## Construction notes

If the survey is on file in the SDG computations, set 1 if most of the problematic category was estimated improved at the rural level, otherwise 0. Otherwise base recommendations on standard international classifications and country insights; use 0 where there is no evidence.

## Consistency checks

- `imp_san_rec` equals 1 for improved facilities: flush/pour-flush to sewer, septic tank, or pit latrine; VIP; pit latrine with slab; composting toilet.
- Note: facilities shared with other households or open to the public are not considered improved.

## Escalation triggers

- A problematic facility category's improved status is disputed.
- No evidence exists for a problematic category and 0 is applied without documentation.

## Common mistakes

- Counting shared facilities as improved.
- Counting bucket, hanging toilet, flush to elsewhere, or no facility as improved.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
