---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-cooksource
canonical_label: "Main source of cooking fuel"
variable_name: cooksource
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
    label: "Firewood"
  - value: 2
    label: "Kerosene"
  - value: 3
    label: "Charcoal"
  - value: 4
    label: "Electricity"
  - value: 5
    label: "Gas"
  - value: 9
    label: "Other"
  - value: 10
    label: "No cook source"
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
  source_section: "Utilities (UTL), Access to Services, Access to Energy, cooksource"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`cooksource` is a categorical variable that identifies the main source of cooking fuel for the household.

## Conceptual intent

It captures the primary fuel used for cooking, a fundamental clean-cooking access indicator.

## Construction notes

If several fuels are asked in the survey, record only the main source. Firewood includes both purchased and collected; electricity includes mains, generator, and solar; other includes fuels like coffee waste, sawdust, crop residue, and cow dung.

## Consistency checks

- Cross-check against `electyp` where it is created from cooking/lighting sources.
- Cross-check with cooking-fuel expenditures where available.

## Escalation triggers

- The survey records multiple fuels and the main source is ambiguous.

## Common mistakes

- Recording all fuels instead of the main cooking fuel.
- Treating collected firewood as not a cooking source.
- Coding electricity from generator/solar as a non-electric source.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
