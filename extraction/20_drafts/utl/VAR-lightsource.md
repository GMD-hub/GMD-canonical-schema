---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-lightsource
canonical_label: "Main source of lighting"
variable_name: lightsource
module_id: MOD-UTL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: categorical

# --- Allowed output values ---
value_codes:
  - value: 1
    label: "Electricity"
  - value: 2
    label: "Kerosene"
  - value: 3
    label: "Candles"
  - value: 4
    label: "Gas"
  - value: 9
    label: "Other"
  - value: 10
    label: "No light source"
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
  source_section: "Utilities (UTL), Access to Services, Access to Energy, lightsource"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`lightsource` is a categorical variable that identifies the main source of lighting for the household.

## Conceptual intent

It captures the primary source used for lighting, a basic energy access indicator.

## Construction notes

Harmonize into the categories for electricity, kerosene, candles, gas, other, or no light source.

## Consistency checks

- Cross-check against `electyp` where created from cooking/lighting sources.
- Cross-check against `electricity` and `elecacc` where electricity is the main light source.

## Escalation triggers

- The survey does not ask about lighting separately.

## Common mistakes

- Recording the main energy source instead of the specific lighting source.
- Coding candles as a kerosene source.
- Conflating lighting source with electricity connection type.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
