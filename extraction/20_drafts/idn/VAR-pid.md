---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-pid
canonical_label: "Personal unique identifier"
variable_name: pid
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
    label: "Cannot be harmonized because the personal identifier is not available"

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
    - "eglin"
  typical_section_names:
    - "Household roster"
    - "Individual roster"
    - "Household composition"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "ID Module (IDN), Mapping and Description of Variables, pid"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "pid allows identification of individuals within a household. It may be a concatenation of several raw variables; the length varies by country. Keep the format (string or numeric) of the original data. If a Personal ID exists in the original data, pid and pid_orig are the same. If pid_orig is missing, pid is constructed from raw variables. Must be unique in the database."
---

## Definition

`pid` allows identification of individuals within a household. The variable
varies in length depending on how the identification code was constructed in
each country, and may be a concatenation of several variables in the raw data
file.

## Conceptual intent

`pid` uniquely identifies each individual within a household and, together with
`hhid`, forms the individual-level key for the harmonized database. It must be
unique and identical across all harmonized modules.

## Construction notes

Keep the format (string or numeric) of the original data. If a personal ID
exists in the original data, `pid` and `pid_orig` should be the same. If
`pid_orig` is missing, `pid` is constructed from the raw data variables that
identify the individual.

When `pid` is constructed by concatenating several raw variables, create it
once and use the same variables and ordering across the data files so the
identifier points to the same individual in every file.

Ensure `pid` and `hhid` are stored at sufficient precision and in a consistent
format across all modules so they merge correctly.

## Consistency checks

- `pid` must be unique in the database. Verify with `isid hhid pid` and
  `duplicates report hhid pid`.
- `pid` must match perfectly with `pid` across all harmonized modules.
- Observations whose information is missing in one module must still appear in
  the dataset so files merge correctly.
- Check uniqueness at the individual level of the data.

## Escalation triggers

- Duplicate `pid` values are detected.
- `pid` cannot be matched consistently across modules.
- The concatenation order or sorting of component variables differs across
  files, producing inconsistent identifiers.

## Common mistakes

- Renumbering `pid` instead of preserving an available original identifier.
- Creating `pid` from a concatenation without a consistent variable order and
  sort, so identifiers differ across files.
- Dropping observations with missing data instead of keeping them, breaking the
  cross-module merge.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
