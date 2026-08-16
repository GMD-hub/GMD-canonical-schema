---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-literacy
canonical_label: "Can both read and write"
variable_name: literacy
module_id: MOD-DEM
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: individual
mapping_role: atomic
data_type: binary

# --- Allowed output values ---
value_codes:
  - value: 1
    label: "Yes"
  - value: 0
    label: "No"
allowed_range: null

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"
  - code: ".c"
    label: "Literacy not collected in this survey"

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
    - "read and write"
    - "literacy"
    - "can read"
    - "can write"
    - "literate"
  typical_section_names:
    - "Education"
    - "Literacy"
    - "Individual characteristics"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Demography (DEM), Mapping and Description of Variables, literacy"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "Literacy is the ability to both read and write with understanding a short
          simple statement about everyday life in any language. A person able to
          only read or only write is considered illiterate (literacy = 0)."
---

## Definition

`literacy` is a binary variable indicating whether an individual can both read
and write with understanding. It takes the value 1 if the individual is
literate and 0 if illiterate.

## Conceptual intent

Literacy measures basic human capital and is a key input for education and
welfare analysis. The GMD aligns literacy measurement with the international
standard definition: the ability to both read and write with understanding.

## Construction notes

Code `literacy = 1` only when the person can both read and write. If a person
can either read or write alone, they are considered illiterate (`literacy = 0`).

It can be assumed with some degree of accuracy that a respondent with secondary
education or above is literate.

Do not guestimate literacy; base it on the survey response (or a defensible
assumption documented in the do-file).

## Consistency checks

- Cross-check `literacy` against education: individuals with secondary education
  or above should generally be literate.
- Verify no individual has a standard missing value (`.`) where a valid code is
  expected.
- `literacy` should take only values 0, 1, or a documented missing code.

## Escalation triggers

- Ambiguity in how the survey distinguishes literacy from reading-only or
  writing-only abilities.
- A large share of the sample is missing literacy without a documented reason.

## Common mistakes

- Coding `literacy = 1` when the person can only read or only write.
- Guestimating literacy for individuals who were not asked.
- Using a standard missing (`.`) instead of an explicit extended missing code.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
