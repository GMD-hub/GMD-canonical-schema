---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-pidorig
canonical_label: "Personal unique identifier in the raw data"
variable_name: pid_orig
module_id: MOD-IDN
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

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
    label: "Cannot be harmonized because the original personal identifier is not available"

# --- Derivation graph ---
derived_from: []
derives_to: []

# --- Country parameter declarations ---
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
    - "personal id"
    - "pid"
    - "individual id"
    - "person number"
    - "member number"
    - "idcode"
  typical_section_names:
    - "Household roster"
    - "Individual roster"
    - "Household composition"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "ID Module (IDN), Mapping and Description of Variables, pid_orig"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "pid_orig is the individual identifier within the household available in the original data set, kept in the same format and type as the original variable. data_type is declared as string; where the original is numeric, keep the numeric type per the source."
---

## Definition

`pid_orig` is the individual identifier within the household available in the
original data set. It must be kept in the same format and type as in the
original data files.

## Conceptual intent

`pid_orig` preserves the original individual identifier so that users can merge
the harmonized data back to the original survey files. It complements
`hhid_orig` to uniquely trace each individual to its position in the raw data.

## Construction notes

Keep the original individual identifier exactly as it appears in the raw data,
including its format and type (numeric or string). Do not transform or
reconstruct the value here; `pid_orig` exists to preserve the original.

If the raw data does not contain an individual identifier and one must be
constructed from other raw variables, the harmonized `pid` is constructed from
them (see "variable names in raw data" in the source). `pid_orig` reproduces
the original identifier when one exists.

When `pid_orig` is missing it is constructed from the raw data variables that
identify the individual within the household.

## Consistency checks

- `pid_orig` must reproduce the individual identifier in the original data
  without loss of precision or type.
- Where `pid` was directly available in the original data, `pid` and `pid_orig`
  must be equal.

## Escalation triggers

- The original data has no usable personal identifier and the variables needed
  to reconstruct one are ambiguous.

## Common mistakes

- Renumbering `pid_orig` instead of preserving the original value.
- Changing the format or type of `pid_orig` relative to the original data,
  which breaks merging back to raw files.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
