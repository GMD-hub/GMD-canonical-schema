---
# ================================================================
# PARAMETER DEFINITION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
parameter_id: PARAM-LBR-MIN-LABOR-AGE
parameter_name: "Minimum age for the labor module (7-day reference period)"
module_id: MOD-LBR
schema_version: "0.1"
status: draft
authority: "GPID Team"

# --- Nature of the parameter ---
kind: construction           # gate: determines the universe, so it changes harmonized output
value_type: integer          # a scalar age threshold
value_schema: null

# --- Derivation (ordered; TOTAL — always yields a value) ---
# PROPOSED facet (see harmonization/design/scalar-parameters).
derivation:
  - method: questionnaire_universe   # path a (authoritative): the labor section's lower age cut-off,
    source: instrument_link          #   detected once per instrument version, reused across rounds
  - method: data_onset               # path b (empirical fallback): robust lower bound of the ages
    source: data                     #   at which the labor section is filled; per-run; review-flag

# --- Where it is used ---
# Symmetric with VAR.country_parameters: VAR-lstatus must list this parameter back.
# The 7-day labor family derived FROM lstatus (empstat, industrycat*, occup*, wage*,
# whours, ...) inherits the universe through derivation and need not re-declare the gate.
applies_to_variables:
  - VAR-lstatus

# --- Behavior when no value could be produced ---
fallback_policy: block_and_escalate  # derivation is total; a missing value means it was not run.
global_default: null                 # no universal minimum working age may be assumed

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Labor (LBR), labor status (7-day reference period)"
  extraction_method: manual
  extracted_on: "2026-10-06"
  human_reviewed: false
  reviewer: null
  notes: "Registers the labor-module age threshold (variable_name `minlaborage`, currently
          drafted as VAR-minlaborage) as a scalar country parameter, parallel to
          PARAM-EDU-MIN-EDUCATION-AGE. The VAR identity may remain for output emission.
          VAR-lstatus now carries PARAM-LBR-MIN-LABOR-AGE in its `country_parameters:`
          (symmetric edge); the emission carrier VAR-minlaborage also lists it but is not in
          applies_to_variables (it emits the value, is not gated). Kept distinct from the 12-month threshold
          PARAM-LBR-MIN-LABOR-AGE-YEAR by decision; the two reference periods are modelled
          separately even where their values coincide."
---

## Definition

The lowest age at which a survey administers its 7-day-reference-period labor module.
Labor status (`lstatus`) is harmonized only for individuals at or above this age;
individuals below it receive `.c` (labor section not applied). The labor variables derived
from `lstatus` inherit this universe through the derivation chain.

## Why this is country specific

The working-age cut-off for the labor module differs across countries and can change when
an instrument is revised. The value shape (a single age) is universal; the applicable
threshold is a property of each survey's instrument.

## How the agent uses it

The agent resolves one scalar value for the survey and `lstatus` applies it as a universe
gate: `age >= minlaborage` keeps the row; `age < minlaborage` sets `lstatus` to `.c`. The
downstream 7-day labor variables need not re-apply the gate — they are `.c` wherever
`lstatus` is.

## Derivation (always produces a number)

An ordered, **total** strategy:

- **Path a — authoritative.** The lower age cut-off for the labor module, read from the
  questionnaire or interviewer manual. Detected once per instrument version and reused
  across rounds (`source: instrument_link`).
- **Path b — empirical fallback.** When the manual does not state a cut-off, the robust lower
  bound of the ages at which the labor section is actually filled in the data. A per-run
  computation (not a reusable instrument constant), recorded with a review flag. Use a robust
  bound, not the single youngest record.

The resolved value records which path produced it, the number, and its evidence.

## Fallback behavior

`fallback_policy: block_and_escalate`. Path b always yields a value, so the threshold is
never genuinely absent; a missing value means the derivation was not performed — escalate
rather than harmonize below-cutoff individuals. No `global_default` — a working-age minimum
cannot be assumed universally.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-10-06 | 0.1     | Initial draft | GPID Team  |
