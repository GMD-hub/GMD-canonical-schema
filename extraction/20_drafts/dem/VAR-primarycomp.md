---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-primarycomp
canonical_label: "Primary school completion"
variable_name: primarycomp
module_id: MOD-DEM
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: individual
mapping_role: derived
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
  - code: ".c"
    label: "Education section not applied because the individual is below mineducatage"
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"

# --- Derivation graph ---
derived_from:
  - VAR-educat7
  - VAR-educat5
derives_to: []

# --- Country parameter declarations ---
# Not a routing instruction. The agent always loads the country layer.
country_parameters: []

# --- Prerequisites ---
prerequisites:
  - variable_id: VAR-mineducatage
    condition: "Set primarycomp to .c for individuals below mineducatage."
  - variable_id: VAR-educat7
    condition: "Preferred source. Derive primarycomp from educat7 when available."
  - variable_id: VAR-educat5
    condition: "Fallback source when educat7 is not defined."

# --- Cross-references ---
rules: []
exceptions: []
external_standards: []

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "primary completion"
    - "completed primary"
    - "finished primary school"
  typical_section_names:
    - "Education"
    - "Schooling"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Demography (DEM), Mapping and Description of Variables, primarycomp"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "Record at least primary completion for every individual in the household,
          derived from educat7 or educat5. Recode educat7 (1/2=0)(3/7=1). One can
          assume with a degree of certainty that certain conditions qualify
          primary-school completion (educat7 in 3-7, or educat5 in 3-5)."
---

## Definition

`primarycomp` is a binary variable indicating whether an individual has
completed at least primary education. It takes the value 1 if primary has been
completed and 0 otherwise.

## Conceptual intent

`primarycomp` records at least primary completion for every individual in the
household. It provides a simple, internationally comparable indicator of basic
education completion used in welfare and human capital analysis.

## Construction notes

Derive `primarycomp` from `educat7` or `educat5`:

```stata
recode educat7 (1/2=0) (3/7=1), gen(primarycomp)
```

Alternatively:

```stata
gen primarycomp = inrange(educat7,3,7) if !mi(educat7)
gen primarycomp = inrange(educat5,3,5) if !mi(educat5)
```

Prefer `educat7` as the source; use `educat5` when `educat7` is not defined.
Apply the age restriction, setting `primarycomp` to `.c` below `mineducatage`.

## Consistency checks

- `primarycomp` must be consistent with `educat7`/`educat5`: an individual with
  a completed-primary level or above must have `primarycomp = 1`.
- No individual below `mineducatage` should have a non-missing `primarycomp`.
- `primarycomp` should take only values 0, 1, or a documented missing code.

## Escalation triggers

- Inconsistency between `primarycomp` and the education variables used to derive
  it.
- A large share of individuals at or above `mineducatage` missing `primarycomp`.

## Common mistakes

- Deriving `primarycomp` inconsistently across surveys (different cut-offs).
- Failing to apply the `mineducatage` age restriction.
- Using standard missing (`.`) instead of `.c` for the age restriction.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
