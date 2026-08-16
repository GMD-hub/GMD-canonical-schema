---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-waste
canonical_label: "Main types of solid waste disposal"
variable_name: waste
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
    label: "Solid waste collected on a regular basis by authorized collectors"
  - value: 2
    label: "Solid waste collected on an irregular basis by authorized collectors"
  - value: 3
    label: "Solid waste collected by self-appointed collectors"
  - value: 4
    label: "Occupants dispose of solid waste in a local dump supervised by authorities"
  - value: 5
    label: "Occupants dispose of solid waste in a local dump not supervised by authorities"
  - value: 6
    label: "Occupants burn solid waste"
  - value: 7
    label: "Occupants bury solid waste"
  - value: 8
    label: "Occupants dispose solid waste into river, sea, creek, pond"
  - value: 9
    label: "Occupants compost solid waste"
  - value: 10
    label: "Other arrangement"
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
  source_section: "Utilities (UTL), Access to Services, Water, Sanitation and Hygiene (WASH), waste"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`waste` is a categorical variable that indicates the type of solid waste disposal used by the household.

## Conceptual intent

It captures the usual manner of collection and disposal of solid waste or garbage, categorized by disposal method and by the administrator of waste disposal.

## Construction notes

Code by the usual manner of collection/disposal (collection, disposal, burial, compost) and by who administers it (authorized collectors, self-appointed collectors, authority-supervised dumps).

## Consistency checks

- Cross-check that the disposal category is consistent with reported garbage collection services.
- Cross-check against `garbage_exp` where available.

## Escalation triggers

- The survey uses a disposal arrangement not represented in the ten categories.

## Common mistakes

- Confusing authorized and self-appointed collectors.
- Treating burning as collection rather than disposal.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
