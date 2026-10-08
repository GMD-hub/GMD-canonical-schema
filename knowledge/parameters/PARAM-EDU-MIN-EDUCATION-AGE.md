---
# ================================================================
# PARAMETER DEFINITION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
parameter_id: PARAM-EDU-MIN-EDUCATION-AGE
parameter_name: "Minimum age for the education module"
module_id: MOD-DEM
schema_version: "0.1"
status: draft
authority: "GPID Team"

# --- Nature of the parameter ---
kind: construction           # gate: determines the universe, so it changes harmonized output
value_type: integer          # a scalar age threshold
value_schema: null

# --- Derivation (ordered; TOTAL — always yields a value) ---
# PROPOSED facet (see harmonization/design/scalar-parameters). Tried in order; because
# path b always produces a number, the parameter is never genuinely absent at resolution.
derivation:
  - method: questionnaire_universe   # path a (authoritative): the section's lower age cut-off,
    source: instrument_link          #   detected once per instrument version, reused across rounds
  - method: data_onset               # path b (empirical fallback): robust lower bound of the ages
    source: data                     #   at which the education section is filled; per-run; review-flag

# --- Where it is used ---
# Symmetric with VAR.country_parameters: every variable listed here must list this
# parameter back in its own `country_parameters:` block.
applies_to_variables:
  - VAR-educat7
  - VAR-educat5
  - VAR-educat4
  - VAR-educy
  - VAR-primarycomp

# --- Behavior when no value could be produced ---
fallback_policy: block_and_escalate  # the derivation is total, so a missing value means the
                                     # derivation step was not run — an anomaly to stop on, not
                                     # a licence to skip the gate.
global_default: null                 # no universal minimum age may be assumed

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Demography (DEM), education variables; RULE-EDU-001"
  extraction_method: manual
  extracted_on: "2026-10-06"
  human_reviewed: false
  reviewer: null
  notes: "Registers the education-module age threshold (variable_name `mineducatage`,
          currently drafted as VAR-mineducatage) as a scalar country parameter, per
          VAR-mineducatage's own escalation note. The VAR identity may remain for output
          emission; this PARAM is the parameter identity used by the education gates.
          The listed gate consumers now carry PARAM-EDU-MIN-EDUCATION-AGE in their
          `country_parameters:` (symmetric edge). The emission carrier VAR-mineducatage also
          lists it in country_parameters but is deliberately NOT in applies_to_variables (it
          emits the value, it is not gated by it) — that asymmetry marks the carrier."
---

## Definition

The lowest age at which a survey administers its education section. The categorical
education variables (`educat7`, `educat5`, `educat4`, `primarycomp`) and the years-of-
education variable (`educy`) are harmonized only for individuals at or above this age;
individuals below it receive `.c` (education section not applied), never a guessed value.

## Why this is country specific

The age at which education information begins to be collected varies by country and can
change when an instrument is revised. The concept and value shape (a single age) are
universal; the applicable threshold is a property of each survey's instrument.

## How the agent uses it

The agent resolves one scalar value for the survey, then each listed education variable
applies it as a universe gate: `age >= mineducatage` keeps the row for harmonization, and
`age < mineducatage` sets the variable to `.c`. The same value must be used for every
education variable in a survey (RULE-EDU-001 forbids different cutoffs across them).

## Derivation (always produces a number)

An ordered, **total** strategy:

- **Path a — authoritative.** The lower age cut-off for the education section, read from the
  questionnaire or interviewer manual. Questionnaires are stable across data-collection
  rounds, so this is detected once per instrument version and reused for every round
  (`source: instrument_link`).
- **Path b — empirical fallback.** When the manual does not state a cut-off, the robust lower
  bound of the ages at which the education section is actually filled in the data. This is a
  per-run computation — a property of the round's microdata, not a reusable instrument
  constant — and is recorded with a review flag. Use a robust bound, not the single youngest
  record: one mis-keyed child would corrupt it.

The resolved value records which path produced it, the number, and its evidence, so the
threshold and its provenance are both visible — preferred over an invisible "gate skipped".

## Fallback behavior

`fallback_policy: block_and_escalate`. Because path b always yields a value, the threshold is
never genuinely absent; a missing value means the derivation step was not performed, which is
an error to escalate rather than silently harmonizing below-cutoff individuals. RULE-EDU-001
branch 2 ("if `mineducatage` is not defined, apply the section to all ages") is left unchanged
but becomes **moot** — the parameter is always defined, so that branch is never reached. No
`global_default`: a minimum schooling age cannot be assumed universally.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-10-06 | 0.1     | Initial draft | GPID Team  |
