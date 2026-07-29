---
# ================================================================
# PARAMETER DEFINITION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
parameter_id: PARAM-EDU-YEARS-BY-LEVEL
parameter_name: "Duration in years of each education level"
module_id: MOD-DEM
schema_version: "0.1"
status: draft
authority: "GPID Team"

# --- Nature of the parameter ---
kind: construction
value_type: mapping
value_schema:
  primary: integer
  lower_secondary: integer
  upper_secondary: integer

# --- Where it is used ---
applies_to_variables:
  - VAR-educy
  - VAR-educat4

# --- Behavior when no country record exists ---
fallback_policy: undecided
global_default: null

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  extraction_method: manual
  extracted_on: "2026-07-28"
  human_reviewed: false
  reviewer: null
  notes: "fallback_policy is UNDECIDED and awaiting GPID Team decision.
          Replaces the former education years country lookup table."
---

## Definition

Defines the number of years assigned to primary, lower secondary, and upper
secondary education when constructing harmonized education variables.

## Why this is country specific

Education cycles differ across countries and can change over time. The
universal definition and value shape remain stable, while each governed
country record supplies the applicable durations for a validity window.

## How the agent uses it

The agent always loads the folder matching the survey ISO3 code. It selects
the one record whose inclusive validity window contains the survey ID year,
defined as the calendar year in which fieldwork began. The selected mapping
is then used by the construction rules that reference this parameter.

## Fallback behavior

The fallback policy is not yet decided. Until the GPID Team selects a policy,
the validator flags this parameter and harmonization must stop when a valid
country record is missing.

Candidate policies and consequences:

- `use_global_default`: apply a non-null global value and flag the output as
  default based. This permits construction but can hide country variation.
- `block_and_escalate`: do not construct the variable and escalate the missing
  coverage. This corresponds to Situation C in the Harmonization Specification.
- A parameter-specific redesign or approved coverage requirement: add a
  governed country value before harmonization. This preserves specificity but
  requires consultation and review before work can proceed.

`skip_check` is not a candidate because this is a construction parameter.

## Data sources for populating values

The primary seed source is the UNESCO ISCED country mappings at
http://uis.unesco.org/en/isced-mappings. Legacy Stata do-files are a secondary
source and every value taken from them requires human verification before use.

## Change log

| Date | Version | Change | Authority |
|---|---|---|---|
| 2026-07-28 | 0.1 | Initial draft | GPID Team |
