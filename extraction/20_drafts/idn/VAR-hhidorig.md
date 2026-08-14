---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-hhidorig
canonical_label: "Household unique identifier in the raw data"
variable_name: hhid_orig
module_id: MOD-IDN
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

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
    label: "Cannot be harmonized because the original household identifier is not available"

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
    - "household id"
    - "hhid"
    - "household number"
    - "household identifier"
    - "folio"
    - "hh"
  typical_section_names:
    - "Household identification"
    - "Household roster"
    - "Cover page"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "ID Module (IDN), Mapping and Description of Variables, hhid_orig"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "hhid_orig is the household identifier as it appears in the original data, kept in the same format and type as the original variable. data_type is declared as string; where the original is numeric, keep the numeric type per the source."
---

## Definition

`hhid_orig` is the household identifier available in the original data. It must
be kept in the same format and type as in the original data files.

## Conceptual intent

`hhid_orig` preserves the original household identifier so that users can merge
the harmonized data back to the original survey files. Keeping the original
identifier (as opposed to only the reconstructed `hhid`) is essential for
traceability and for merging with raw data.

## Construction notes

Keep the original household identifier exactly as it appears in the raw data,
including its format and type (numeric or string). Do not transform or
reconstruct the value here; `hhid_orig` exists to preserve the original.

If the raw data does not contain a household identifier and one must be
constructed from other raw variables, the original variables used for the
construction are retained (see "variable names in raw data" in the source), and
the harmonized `hhid` is constructed from them.

When `hhid_orig` is missing it is constructed from the raw data variables that
identify the household.

## Consistency checks

- `hhid_orig` must reproduce the household identifier in the original data
  without loss of precision or type.
- Where `hhid` was directly available in the original data, `hhid` and
  `hhid_orig` must be equal.

## Escalation triggers

- The original data has no usable household identifier and the variables
  needed to reconstruct one are ambiguous.
- `hhid_orig` cannot be reproduced exactly from the raw data.

## Common mistakes

- Reconstructing or renumbering `hhid_orig` instead of preserving the original
  value.
- Changing the format or type of `hhid_orig` relative to the original data,
  which breaks merging back to raw files.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
