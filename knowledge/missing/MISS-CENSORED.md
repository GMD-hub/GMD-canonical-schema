---
# ================================================================
# MISSING VALUE DEFINITION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
missing_id: MISS-CENSORED
missing_name: censored
canonical_label: "Censored values"
schema_version: "0.1"
status: draft
authority: "GPID Team"

# --- Nature of the missing value ---
level: cell          # cell: describes one observation of a harmonized variable
scope: global        # global: applies to every variable; no variable lists it

# --- Representations ---
# What an output format writes for this value. A format that is not listed writes `missing_name`.
representations:
  stata: ".t"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: null
  extraction_method: manual
  extracted_on: "2026-11-17"
  human_reviewed: false
  reviewer: null
  notes: "Scaffold of a new record kind (missing value definitions), written on instruction of 2026-11-17.
          This value and its Stata code `.t` are NEW: they are proposed in that instruction and
          are not in the source document, which is why `source_section` is null. The label is the
          wording given in the instruction. Not from the extraction pipeline."
---

## Definition

The survey holds a value for the observation, but the delivered data censors it, so the
harmonized value is not known.

## When it applies

- The data producer withheld the observation's value in the delivered data, for example
  for confidentiality.

## When it does not apply

- The survey holds no value for the observation: use `MISS-MISSING-INPUT`.
- The whole variable was withheld from the delivered data: that is a column missing
  (`MISS-NOT-AVAILABLE`).

## Open questions

- Whether a top-coded or bottom-coded value, where the delivered data gives a bound in
  place of the value, takes this missing value or keeps the bound as its value is
  undecided.

## Change log

| Date       | Version | Change           | Authority            |
|------------|---------|------------------|----------------------|
| 2026-11-17 | 0.1     | Initial scaffold | GPID Team (proposed) |
