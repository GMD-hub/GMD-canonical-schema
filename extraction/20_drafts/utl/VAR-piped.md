---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-piped
canonical_label: "Access to piped water"
variable_name: piped
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
  []
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Access to Services, Water, Sanitation and Hygiene (WASH), piped"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`piped` is a binary variable that indicates whether the household has access to piped water, whether within or outside the premises.

## Conceptual intent

It distinguishes piped water service (household or yard connection and public tap/standpipe) from non-piped sources, capturing the fundamental water access dimension.

## Construction notes

Within premises includes a piped connection to an own tap (household or yard connection); outside premises includes a public water point shared among houses (public tap, standpipe, or fountain).

## Consistency checks

- `piped` equals 1 when `water_source` is 1, 2, or 3 (recode water_source 1/3=1, 4/14=0).
- Cross-check with `piped_to_prem` and `water_source`.

## Escalation triggers

- The access varies seasonally or the piped status of a source is ambiguous.

## Common mistakes

- Treating bottled or tanker water as piped water.
- Confusing a public standpipe within the compound with a private yard connection.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
