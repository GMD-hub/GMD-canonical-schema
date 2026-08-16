---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-eyedisability
canonical_label: "Eye disability"
variable_name: eye_dsablty
module_id: MOD-DEM
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: individual
mapping_role: atomic
data_type: categorical_ordered

# --- Allowed output values ---
value_codes:
  - value: 1
    label: "No - no difficulty"
  - value: 2
    label: "Yes - some difficulty"
  - value: 3
    label: "Yes - a lot of difficulty"
  - value: 4
    label: "Cannot do at all"
allowed_range: null

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
prerequisites: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards: []

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "difficulty seeing"
    - "vision"
    - "seeing even with glasses"
    - "eye"
  typical_section_names:
    - "Disability"
    - "Functioning"
    - "Health"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Demography (DEM), Mapping and Description of Variables, eye_dsablty"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "Indicates whether an individual has any difficulty seeing, even when
          wearing glasses. Part of the Washington Group short set of disability
          questions; domain is atomic (not derived from other variables)."
---

## Definition

`eye_dsablty` is a numerical/categorical variable indicating whether an
individual has any difficulty seeing, even when wearing glasses. It takes four
ordered values: 1 = No difficulty, 2 = Some difficulty, 3 = A lot of difficulty,
4 = Cannot do at all.

## Conceptual intent

`eye_dsablty` is a disability-domain indicator measuring the extent of vision
difficulty. It forms part of a set of comparable disability indicators (alongside
hearing, walking, concentration, self-care, and communication) used for
disability prevalence analysis.

## Construction notes

Map the survey question on difficulty seeing (even when wearing glasses)
directly to the four harmonized categories. This is an atomic variable: no
derivation from other variables is performed.

Record 1 when the individual reports no difficulty, 2 for some difficulty, 3 for
a lot of difficulty, and 4 when the individual cannot do it at all.

## Consistency checks

- `eye_dsablty` should take only integer values in [1, 4] or a documented
  missing code.
- Cross-check against other disability domains for internal consistency (e.g.
  severe difficulty in one domain should be reviewed for plausibility).
- No standard missing (`.`) should remain where a valid code was expected.

## Escalation triggers

- The survey's disability scale does not map to the four difficulty categories.
- A very large share of the sample is missing or reports extreme difficulty
  without a plausible explanation.

## Common mistakes

- Confusing the four-point scale (difficulty) with a binary disabled/not
  disabled indicator.
- Transcribing "some difficulty" and "a lot of difficulty" into the same code.
- Using a standard missing (`.`) instead of an explicit extended missing code.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
