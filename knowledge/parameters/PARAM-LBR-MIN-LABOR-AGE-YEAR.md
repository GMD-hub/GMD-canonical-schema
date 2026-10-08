---
# ================================================================
# PARAMETER DEFINITION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
parameter_id: PARAM-LBR-MIN-LABOR-AGE-YEAR
parameter_name: "Minimum age for the labor module (12-month reference period)"
module_id: MOD-LBR
schema_version: "0.1"
status: draft
authority: "GPID Team"

# --- Nature of the parameter ---
kind: construction
value_type: integer
value_schema: null

# --- Derivation (ordered; TOTAL — always yields a value) ---
# PROPOSED facet (see harmonization/design/scalar-parameters).
derivation:
  - method: questionnaire_universe   # path a (authoritative): the 12-month labor section's cut-off,
    source: instrument_link          #   detected once per instrument version, reused across rounds
  - method: data_onset               # path b (empirical fallback): robust lower bound of the ages
    source: data                     #   at which the 12-month labor section is filled; per-run; review-flag

# --- Where it is used ---
# Symmetric with VAR.country_parameters: VAR-lstatusyear must list this parameter back.
# The 12-month labor family derived FROM lstatus_year inherits the universe by derivation.
applies_to_variables:
  - VAR-lstatusyear

# --- Behavior when no value could be produced ---
fallback_policy: block_and_escalate  # derivation is total; a missing value means it was not run.
global_default: null

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Labor (LBR), labor status (12-month reference period)"
  extraction_method: manual
  extracted_on: "2026-10-06"
  human_reviewed: false
  reviewer: null
  notes: "Registers the 12-month labor-module age threshold (variable_name
          `minlaborage_year`, drafted as VAR-minlaborageyear) as a scalar country
          parameter. VAR-lstatusyear now carries this parameter in its `country_parameters:`
          (symmetric edge); the emission carrier VAR-minlaborageyear also lists it but is not
          in applies_to_variables (it emits the value, is not gated). Kept DISTINCT from the
          7-day threshold PARAM-LBR-MIN-LABOR-AGE by decision:
          the two reference periods are modelled separately even where their values coincide.
          (Adding or merging parameters later is a content change; it does not affect the
          resolution/emission mechanism.)"
---

## Definition

The lowest age at which a survey administers its 12-month-reference-period labor module.
Labor status over the last 12 months (`lstatus_year`) is harmonized only for individuals
at or above this age; individuals below it receive `.c`. The 12-month labor variables
derived from `lstatus_year` inherit this universe through the derivation chain.

## Why this is country specific

As with the 7-day threshold, the working-age cut-off is a property of the instrument and
varies by country. A separate entry exists because the 12-month module may apply to a
different population than the 7-day module; the two are modelled distinctly even where their
values coincide.

## How the agent uses it

The agent resolves one scalar value for the survey and `lstatus_year` applies it as a
universe gate: `age >= minlaborage_year` keeps the row; below it sets `lstatus_year` to
`.c`. Downstream 12-month labor variables inherit the universe and need not re-apply it.

## Derivation (always produces a number)

An ordered, **total** strategy:

- **Path a — authoritative.** The lower age cut-off for the 12-month labor module, read from
  the questionnaire or interviewer manual. Detected once per instrument version and reused
  across rounds (`source: instrument_link`).
- **Path b — empirical fallback.** When the manual does not state a cut-off, the robust lower
  bound of the ages at which the 12-month labor section is actually filled in the data. A
  per-run computation (not a reusable instrument constant), recorded with a review flag.

The resolved value records which path produced it, the number, and its evidence.

## Fallback behavior

`fallback_policy: block_and_escalate`. Path b always yields a value, so the threshold is
never genuinely absent; a missing value means the derivation was not performed — escalate.
No `global_default`.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-10-06 | 0.1     | Initial draft | GPID Team  |
