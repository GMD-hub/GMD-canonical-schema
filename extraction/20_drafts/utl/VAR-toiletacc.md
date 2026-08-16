---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-toiletacc
canonical_label: "Access to a flush toilet"
variable_name: toilet_acc
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
    label: "Yes, in premise"
  - value: 2
    label: "Yes, but not in premise including public toilet"
  - value: 3
    label: "Yes, unstated whether in or outside premise"
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
  source_section: "Utilities (UTL), Access to Services, Water, Sanitation and Hygiene (WASH), toilet_acc"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`toilet_acc` is a categorical variable that indicates the type of access to a flush toilet, including whether it is within the premise.

## Conceptual intent

It captures not only flush-toilet access but also the location of the facility, an important service-level dimension.

## Construction notes

Code 0 for no access to a flush toilet, 1 for access within the premise, 2 for access not within the premise (including public toilets), and 3 when the survey does not state whether it is inside or outside the premise.

## Consistency checks

- Cross-check with `sanitation_source` (flush toilet categories).
- Use the unstated category (3) only when the survey genuinely does not record location.

## Escalation triggers

- The survey records access but not whether the facility is within the premise.

## Common mistakes

- Assigning 1 (in premise) when the survey does not state the location.
- Treating no flush toilet access as missing rather than 0.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
