---
# ================================================================
# MISSING VALUE DEFINITION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
missing_id: MISS-OUTSIDE-UNIVERSE
missing_name: outside_universe
canonical_label: "Outside of universe/not applicable"
schema_version: "0.1"
status: draft
authority: "GPID Team"

# --- Nature of the missing value ---
level: cell          # cell: describes one observation of a harmonized variable
scope: variable      # variable: applies only where a variable lists it in missing_codes

# --- Representations ---
# What an output format writes for this value. A format that is not listed writes `missing_name`.
representations:
  stata: ".u"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: null
  extraction_method: manual
  extracted_on: "2026-11-17"
  human_reviewed: false
  reviewer: null
  notes: "Scaffold of a new record kind (missing value definitions), written on instruction of 2026-11-17.
          This value and its Stata code `.u` are NEW: they are proposed in that instruction and
          are not in the source document, which is why `source_section` is null. The label is the
          wording given in the instruction. Not from the extraction pipeline."
---

## Definition

The observation is outside the variable's universe: the variable does not apply to it.

## When it applies

- The variable's universe condition is false for the observation. For example, an
  individual below the minimum age of the education variables.

## When it does not apply

- The observation is inside the universe and its input holds no value: use
  `MISS-MISSING-INPUT`.
- The whole variable is missing from the survey: that is a column missing.

## Open questions

- This value takes over the single-observation use of `.c`. The five education variable
  drafts are changed; RULE-EDU-001 and the minimum-age parameters under `knowledge/`
  are not yet.
- Whether an observation that is inside the variable's universe, but that the survey did
  not put the question to, takes this value or `MISS-MISSING-INPUT` is undecided.

## Change log

| Date       | Version | Change           | Authority            |
|------------|---------|------------------|----------------------|
| 2026-11-17 | 0.1     | Initial scaffold | GPID Team (proposed) |
