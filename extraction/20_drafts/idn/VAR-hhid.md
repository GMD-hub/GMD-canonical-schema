---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-hhid
canonical_label: "Household unique identifier"
variable_name: hhid
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
    label: "Cannot be harmonized because the household identifier is not available"

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
  source_section: "ID Module (IDN), Mapping and Description of Variables, hhid"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "hhid must be unique in the database and identical across all harmonized modules. Original format (string or numeric) should be kept. If a Household ID exists in the original data, hhid and hhid_orig are the same. Do not construct hhid from the row index (_n); construct it from substantive identifying variables."
---

## Definition

`hhid` is the unique household identification number in the data file. The
original format, string or numeric, of the original data should be kept.

## Conceptual intent

`hhid` uniquely identifies each household and is the key used to merge across
all modules of the harmonized database. It must be unique within the database
and identical across modules so that households can be consistently linked.

## Construction notes

Keep the original format (string or numeric) of the original data. If a
household ID exists in the original data, `hhid` and `hhid_orig` should be the
same. If `hhid_orig` is missing, `hhid` is constructed from the raw data
variables that identify the household.

Do not use the sequential index of the observation as the ID
(`gen hhid = _n`), as row order may differ across files and vintages. Construct
`hhid` from substantive identifying variables instead. Where `hhid` is formed
by concatenation (`concat(varlist)`), sort the data first and use the same
variable order across all files so the identifier is consistent.

When identifiers are numeric but stored with low precision, format them with
sufficient precision (e.g. `format %15.0g hhid`) so they merge correctly.

## Consistency checks

- `hhid` must be unique in the dataset. Verify with `isid hhid pid` and
  `duplicates report hhid pid`.
- Check for missing `hhid` values.
- `hhid` must match perfectly with `hhid` across all harmonized modules.
- Observations whose information is missing in one module must still appear in
  the dataset so files merge correctly.
- If a household survey is repeated within a year and data is cross-sectional,
  new `hhid` values are constructed per household per quarter.

## Escalation triggers

- Duplicate `hhid` values are detected.
- `hhid` cannot be matched consistently across modules.
- The identifiers originate from variables whose order or sort differs across
  files, producing unstable IDs.

## Common mistakes

- Using the observation sequence number (`_n`) as the household ID.
- Reconstructing `hhid` without sorting first, or with inconsistent variable
  order, producing unstable identifiers across files.
- Storing numeric IDs at insufficient precision so values change or collide
  during merges.
- Dropping observations with missing data instead of keeping them with missing
  values, breaking the cross-module merge.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
