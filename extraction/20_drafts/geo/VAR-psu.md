---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-psu
canonical_label: "Primary sampling unit"
variable_name: psu
module_id: MOD-GEO
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: integer

# --- Allowed output values ---
value_codes: null
allowed_range: null

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"

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
    - "psu"
    - "cluster"
    - "primary sampling unit"
    - "sample cluster"
    - "enumeration area"
  typical_section_names:
    - "Sampling design"
    - "Survey methodology"
    - "Cluster identification"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Geography (GEO), Mapping and Description of Variables, psu"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`psu` is a country-specific, numeric variable that holds a unique identifier for
each primary sampling unit. A primary sampling unit (clusters) is selected in the
first (primary) stage of a multi-stage sample design and typically corresponds
to a well-defined geographic area, such as a municipality or a group of
contiguous municipalities.

## Conceptual intent

`psu` is required for the correct computation of standard errors under the
survey's complex sample design. In Stata it is declared through the `svyset`
command. It underpins the survey's sampling variance estimation.

## Construction notes

`psu` is a numeric (integer) country-specific variable. A unique identifier is
created for each primary sampling unit; the identifier is survey-specific and
based on the survey's cluster definitions. The value space depends on the country
parameter layer and the survey year/round; load the country parameters and
exceptions valid for the survey's ID year.

`value_codes` is intentionally null because primary sampling unit identifiers
cannot be enumerated in advance in a harmonized framework. Preserve the survey's
own PSU/cluster identifiers without renumbering across surveys.

## Consistency checks

- `psu` must be numeric (integer); verify no string or non-integer values.
- Every household must be assigned to exactly one primary sampling unit.
- A PSU must not span multiple strata; each PSU must nest within a single
  stratum (`strata`).
- Verify PSU identifiers are consistent within the survey year and not mixed
  across rounds.

## Escalation triggers

- The survey documentation does not identify the primary sampling units.
- A household cannot be assigned to a primary sampling unit.
- A PSU identifier maps to more than one stratum, indicating a design
  inconsistency.

## Common mistakes

- Renumbering PSUs across surveys instead of preserving the survey's own
  cluster identifiers.
- Storing PSU as a string rather than an integer.
- Assigning a household to multiple PSUs.
- Confusing `psu` with `strata` or with the design weight.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
