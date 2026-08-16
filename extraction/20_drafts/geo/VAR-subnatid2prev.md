---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-subnatid2prev
canonical_label: "Subnational ID previous - second highest level"
variable_name: subnatid2_prev
module_id: MOD-GEO
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 2

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: string

# --- Allowed output values ---
value_codes: null
allowed_range: null

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"
  - code: ".c"
    label: "Information not available because the subnational classification has not changed since the previous survey"

# --- Derivation graph ---
derived_from: []
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
    - "previous district"
    - "administrative change"
    - "split"
    - "boundary change"
    - "subnational"
  typical_section_names:
    - "Geography"
    - "Identification"
    - "Administrative boundaries"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Geography (GEO), Mapping and Description of Variables, subnatid2_prev"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`subnatid2_prev` is a country-specific categorical string variable that is coded
as missing unless the classification used for `subnatid2` has changed since the
previous survey. When the classification has changed, it records the `subnatid2`
code used in the previous survey.

## Conceptual intent

`subnatid2_prev` maintains temporal consistency in second-level subnational
identifiers, allowing analysts to track splits and administrative changes and to
make historical second-level comparisons across surveys.

## Construction notes

`subnatid2_prev` is coded as missing unless the second-level classification
changed since the previous survey. Where a change occurred (e.g., a district
split), the previous survey's code is recorded for all affected households.

`value_codes` is intentionally null because the previous values depend on the
country's administrative history and the country parameter layer. Load the
country parameters and exceptions valid for the survey's ID year and the
relevant previous survey. Values follow the same "code - name" string convention
as `subnatid2`.

## Consistency checks

- `subnatid2_prev` must be a string variable.
- When populated, its value must be a valid second-level code from the previous
  survey's classification.
- Affected households' previous codes must be consistent with the documented
  administrative change.
- No household may carry a standard missing (`.`) where a classification change
  occurred.

## Escalation triggers

- Administrative boundaries changed but the previous classification cannot be
  determined from documentation.
- The previous codes cannot be reconciled with the current `subnatid2` mapping
  for affected households.

## Common mistakes

- Populating `subnatid2_prev` even when the classification did not change.
- Using current codes instead of the previous survey's codes when recording a
  split.
- Fabricating previous codes instead of using the documented historical
  classification.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
