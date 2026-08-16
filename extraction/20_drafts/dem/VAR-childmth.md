---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-childmth
canonical_label: "Child age in months for those under 5"
variable_name: childmth
module_id: MOD-DEM
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: individual
mapping_role: atomic
data_type: numeric

# --- Allowed output values ---
value_codes: null
allowed_range:
  min: 0
  max: 59

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"
  - code: ".c"
    label: "Not collected in this survey"

# --- Derivation graph ---
derived_from: []
derives_to: []

# --- Country parameter declarations ---
# Not a routing instruction. The agent always loads the country layer.
country_parameters: []

# --- Prerequisites ---
prerequisites:
  - variable_id: VAR-age
    condition: "Applied only to children aged under 5 years (less than 60 months)."

# --- Cross-references ---
rules: []
exceptions: []
external_standards: []

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "age in months"
    - "months of age"
    - "child age in months"
  typical_section_names:
    - "Child health"
    - "Anthropometrics"
    - "Child roster"
    - "Demographics"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Demography (DEM), Mapping and Description of Variables, childmth"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "childyr and childmth were included in the GMD harmonization for the first
          time in the December 2023 revision. If there is no information available,
          they must nonetheless be created."
---

## Definition

`childmth` records the age in complete months of children aged under 5 years
(less than 60 months). It is used to interpret Anthropometrics data.

## Conceptual intent

The age of children under 5 must be measured in months to correctly interpret
anthropometric indicators such as stunting, wasting, and underweight. `childmth`
provides the fine-grained age reference required for this analysis.

## Construction notes

For children under 5 years of age (aged less than 60 months), record the age in
complete months. Derive the value from the date of birth (or date of last
birthday) relative to the survey date where possible.

The variable must be constructed even if information is not directly available;
if a value cannot be derived, record the appropriate missing code and document
why.

## Consistency checks

- `childmth` must be consistent with `childyr` and `age`: the completed-month
  value must imply a completed-year value consistent with `childyr`.
- `childmth` should only be non-missing for individuals under 5 years of age and
  should be in the range [0, 59].
- Verify no value is 60 months or greater (which would indicate age 5 or above).

## Escalation triggers

- Systematic inconsistency between `childmth`, `childyr`, and `age`.
- No source information exists to construct `childmth` and no reasonable basis
  for derivation is documented.

## Common mistakes

- Recording `childmth` for children aged 5 years or older.
- Failing to create the variable at all when the survey lacks it, contrary to
  the December 2023 revision requirement.
- Recording months beyond 59 for children still under 5.
- Leaving `childmth` inconsistent with `childyr` or `age`.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
