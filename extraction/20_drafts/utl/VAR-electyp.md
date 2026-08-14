---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-electyp
canonical_label: "Lighting and/or electricity type"
variable_name: electyp
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
    label: "Gas"
  - value: 3
    label: "Lamp"
  - value: 4
    label: "Others"
  - value: 10
    label: "No cook and light source"
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
  source_section: "Utilities (UTL), Access to Services, Access to Energy, electyp"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`electyp` is a categorical variable that specifies the source of energy used for cooking and/or lighting.

## Conceptual intent

It is used when separate cooking and lighting source questions are unavailable, and prioritized by electricity, then gas, then lamp when both are available.

## Construction notes

When `cooksource` and `lightsource` are available, prioritize electricity (cooksource=4 or lightsource=1), then gas (cooksource=5 or lightsource=4), then lamp (cooksource=2 or lightsource in 2,3), otherwise other.

## Consistency checks

- When `cooksource` or `lightsource` indicate electricity, `electyp` should be 1.
- When both indicate gas, `electyp` should be 2.

## Escalation triggers

- The survey has only a single combined energy-source question.

## Common mistakes

- Prioritizing a secondary source over electricity when both are present.
- Coding multiple sources instead of the single prioritized type.
- Using this variable when separate cooking and lighting sources exist.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
