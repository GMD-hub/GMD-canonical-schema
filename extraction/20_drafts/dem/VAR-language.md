---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-language
canonical_label: "Language"
variable_name: language
module_id: MOD-DEM
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 2

# --- Nature of the variable ---
unit_of_analysis: individual
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
    label: "Language not collected in this survey"

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
    - "language"
    - "mother tongue"
    - "usual language"
    - "main language"
    - "language spoken"
  typical_section_names:
    - "Individual characteristics"
    - "Demographics"
    - "Language"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Demography (DEM), Mapping and Description of Variables, language"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "A string variable that refers either to the usual language spoken in the
          present home, the mother tongue, or the language the person commands
          best. Classification is country specific. Numeric entries are coded in
          string format using the naming convention '2 - language type'. Record the
          type of question used in the notes."
---

## Definition

`language` is a string variable recording an individual's language. It refers
either to the language normally spoken in the individual's present home (usual
language), the language spoken at home in early childhood (mother tongue), or
the language the person commands best (main language).

## Conceptual intent

`language` captures linguistic identity for demographic and social analysis. Its
classification is country specific, so no harmonized coding scheme is imposed.

## Construction notes

Information on language (including any sign language) should be harmonized for
all persons. Record the language as a string.

Numeric entries are coded in string format using the naming convention
"2 - language type" (where 2 is a placeholder for the numeric code).

In the tabulated results, the criterion for determining the language for children
not yet able to speak should be clearly indicated. Record in the notes the type
of question used for the harmonization (e.g. usual language or mother tongue).

## Consistency checks

- Verify the language string is recorded consistently and is not truncated.
- Confirm the type of language question (usual, mother tongue, main) is
  documented in the notes.
- Cross-check that the record for children who cannot yet speak is handled
  according to the documented criterion.

## Escalation triggers

- The survey does not clearly indicate which language type (usual, mother
  tongue, main) was collected.
- Numeric language codes cannot be mapped to string labels consistently.

## Common mistakes

- Failing to document which type of language question was used.
- Converting language to numeric codes without retaining the string labels.
- Leaving language missing for children who cannot yet speak instead of applying
  the documented criterion.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
