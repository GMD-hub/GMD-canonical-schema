---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-urban
canonical_label: "Urban / rural residence"
variable_name: urban
module_id: MOD-GEO
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
  - value: 1
    label: "Urban"
  - value: 0
    label: "Rural"
allowed_range: null

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"

# --- Derivation graph ---
derived_from:
  - VAR-rurality
derives_to: []

# --- Country parameter declarations ---
# Not a routing instruction. The agent always loads the country layer.
country_parameters: []

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards: []

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "urban"
    - "rural"
    - "locality type"
    - "area"
  typical_section_names:
    - "Housing"
    - "Geography"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Geography (GEO) [Chapter 3], Mapping and Description of Variables, urban"
  extraction_method: manual
  extracted_on: "2026-08-07"
  human_reviewed: false
  reviewer: null
  notes: "Calibration fixture (not from the extraction pipeline). Carries seeded
          known defects for the calibration run; see known-answer-key.md."
---

## Definition

`urban` is a binary dummy variable that records whether the household resides
in an urban or rural locality according to the survey's sampling frame. It
takes the value 1 for urban and 0 for rural.

## Conceptual intent

`urban` is the standard residence classification used across the GMD for
rural-urban disaggregation of welfare, poverty, and demographic indicators. It
must follow the national statistics office definition recorded in the source
survey documentation.

## Construction notes

Map the survey's reported locality type directly to the GMD binary code using
the urban/rural definition stated in the survey's sampling documentation. When
the survey provides multiple locality classes, classify them into urban and
rural according to the national definition; document the grouping in the
do-file notes.

## Consistency checks

- No household should have a standard missing value (`.`) for `urban`; every
  case must be either 1 or 0 or carry an explicit extended missing code.
- Cross-check the urban share against the survey's sampling design; large
  departures from the published sampling rate may signal a coding error.
- Verify the `module_id` matches the directory the artifact lives under
  (`geo/` implies `MOD-GEO`).

## Escalation triggers

- The survey documentation does not state how localities were classified, so
  urban/rural cannot be determined reliably.
- The reported urban share differs sharply from the national statistics office
  publication with no sampling explanation.

## Common mistakes

- Using the statistical office's broad regional variable instead of the actual
  locality-type variable for `urban`.
- Coding a missing locality as rural (0) instead of an explicit missing code.
- Ignoring the survey's definition when it differs from the assumed national
  one.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-07 | 0.1     | Initial fixture | Calibration |
