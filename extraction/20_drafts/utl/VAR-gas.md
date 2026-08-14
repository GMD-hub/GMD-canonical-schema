---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-gas
canonical_label: "Connection to gas/Usage of gas"
variable_name: gas
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
    label: "Yes, piped gas (LNG)"
  - value: 2
    label: "Yes, bottled gas (LPG)"
  - value: 3
    label: "Yes, but don't know"
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
  source_section: "Utilities (UTL), Access to Services, Access to Energy, gas"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`gas` is a categorical variable that identifies the type of gas usage in the household.

## Conceptual intent

It distinguishes piped (LNG) from bottled (LPG) gas use, and records an unknown type when the survey does not specify.

## Construction notes

Harmonize into 0 for no gas, 1 for piped gas (LNG), 2 for bottled gas (LPG), and 3 when the household uses gas but the type is unknown.

## Consistency checks

- Cross-check with `cooksource` and `lightsource` gas categories.
- Cross-check with `gasexp` components (`ngasexp`, `lpgexp`) where available.

## Escalation triggers

- The survey records gas use but not whether piped or bottled.

## Common mistakes

- Coding bottled gas (LPG) as piped natural gas.
- Treating unknown gas type as missing instead of 3.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
