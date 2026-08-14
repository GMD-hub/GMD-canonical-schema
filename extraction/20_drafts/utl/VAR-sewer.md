---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-sewer
canonical_label: "Access to sewer"
variable_name: sewer
module_id: MOD-UTL
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
  - value: 0
    label: "No"
  - value: 1
    label: "Flush/pour flush to piped sewer system"
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
  source_section: "Utilities (UTL), Access to Services, Water, Sanitation and Hygiene (WASH), sewer"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`sewer` is a categorical variable that specifies whether the household has access to a toilet connected to a piped sewer system.

## Conceptual intent

It identifies households with the highest level of sanitation service, connected to a piped sewer network.

## Construction notes

Code 1 only when the household's toilet is a flush/pour flush discharging to a piped sewer system; otherwise 0.

## Consistency checks

- `sewer` equals 1 when `sanitation_source` is 2 (piped sewer system) or an equivalent flush to sewer.
- Cross-check with `sanitation_source` and `imp_san_rec`.

## Escalation triggers

- The disposal destination of the flush toilet is unstated.

## Common mistakes

- Coding a septic tank as a sewer connection.
- Coding flush to elsewhere (e.g. river) as sewer access.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
