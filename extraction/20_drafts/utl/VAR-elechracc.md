---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-elechracc
canonical_label: "Electricity availability (hr/day)"
variable_name: elechr_acc
module_id: MOD-UTL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 2

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: numeric_continuous

# --- Allowed output values ---
value_codes:
  null
allowed_range:
  min: 0
  max: 24
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
  source_section: "Utilities (UTL), Access to Services, Access to Energy, elechr_acc"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`elechr_acc` is a numeric continuous variable that specifies access to electricity in hours per day.

## Conceptual intent

It measures the quality/reliability of electricity supply, complementing the binary access indicators.

## Construction notes

Report the number of electricity hours available per day. This typically reflects supply reliability where surveys record daily availability.

## Consistency checks

- Value should be within a plausible daily range (0-24 hours).
- Cross-check against `electricity` and `elec_acc` access status.

## Escalation triggers

- Unusually low hours per day (e.g. below 6) should be verified.
- The survey does not collect hours of availability.

## Common mistakes

- Reporting monthly totals instead of hours per day.
- Treating no electricity access as missing rather than 0 hours.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
