---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-heatsource
canonical_label: "Main source of heating"
variable_name: heatsource
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
  - value: 1
    label: "Firewood"
  - value: 2
    label: "Kerosene"
  - value: 3
    label: "Charcoal"
  - value: 4
    label: "Electricity"
  - value: 5
    label: "Gas"
  - value: 6
    label: "Central"
  - value: 9
    label: "Other"
  - value: 10
    label: "No heating"
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
  source_section: "Utilities (UTL), Access to Services, Access to Energy, heatsource"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`heatsource` is a categorical variable that indicates the main source of heating for the dwelling.

## Conceptual intent

It captures the predominant energy used for space heating, distinguishing central systems from individual heating bodies, and the main fuel used.

## Construction notes

Main source of heating refers to the system providing heat for most of the space, whether central heating or separate appliances (stove, fireplace). Code the predominant energy source; use 10 when there is no heating and 9 for other fuels.

## Consistency checks

- Cross-check with `central_acc` where central heating is the main source.
- Cross-check with `heating_exp` categories where available.

## Escalation triggers

- The survey does not ask about space heating at all.

## Common mistakes

- Coding a secondary heating source instead of the main one.
- Recording no heating (10) when the household heats with an individual stove.
- Confusing heating fuel with cooking fuel (`cooksource`).

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
