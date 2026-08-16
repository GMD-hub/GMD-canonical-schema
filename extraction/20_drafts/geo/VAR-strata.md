---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-strata
canonical_label: "Strata"
variable_name: strata
module_id: MOD-GEO
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
    - "strata"
    - "stratum"
    - "sampling strata"
    - "design weight"
    - "sample design"
  typical_section_names:
    - "Sampling design"
    - "Survey methodology"
    - "Sample weights"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Geography (GEO), Mapping and Description of Variables, strata"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`strata` is a country-specific variable that holds a unique identifier for each
sampling stratum. A stratum is a subpopulation of the target population formed
from the census sampling frame based on auxiliary information, and sampling is
conducted separately within each stratum. Strata are mutually exclusive and
collectively exhaustive.

## Conceptual intent

`strata` is required for the correct computation of the variance (or confidence
intervals) of population estimates under the survey's sample design. In Stata it
is declared through the `svyset` command. `strata` must match the sampling design
of the survey for the given year or round.

## Construction notes

The chapter states `strata` is numeric and country specific, but specifies that
the variable is recorded in string format using the naming convention
"code of stratum - stratum name", for example "1 - Dar-es-salaam". This draft
records `data_type` as string in line with the stated format convention. The
value space is country-specific and depends on the country parameter layer: load
the country parameters and exceptions valid for the survey's ID year.

`value_codes` is intentionally null because the strata identifiers are
survey-year specific and cannot be enumerated in advance. Use the sampling
documentation for the given year/round. Do not reuse strata from other
rounds or versions of the same survey.

## Consistency checks

- `strata` values must be mutually exclusive and collectively exhaustive; every
  household must be assigned to exactly one stratum.
- Verify each value follows the "code - stratum name" string convention.
- Cross-check that the strata used match the sampling design for the survey
  year/round.
- Strata structure should be consistent with the design weight construction.

## Escalation triggers

- The survey documentation does not specify how strata were defined for the
  given year.
- Households cannot be uniquely assigned to a stratum.
- The strata in the data conflict with the documented sampling design for the
  survey year/round.

## Common mistakes

- Using strata from a different year or version of the survey.
- Leaving `strata` numeric without the "code - name" string convention.
- Assigning a household to more than one stratum (violating mutual
  exclusivity).
- Confusing `strata` with the design weight or with `psu`.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
