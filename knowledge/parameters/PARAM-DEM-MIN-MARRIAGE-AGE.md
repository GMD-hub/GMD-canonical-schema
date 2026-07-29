---
# ================================================================
# PARAMETER DEFINITION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
parameter_id: PARAM-DEM-MIN-MARRIAGE-AGE
parameter_name: "Minimum legal marriage age"
module_id: MOD-DEM
schema_version: "0.1"
status: draft
authority: "GPID Team"

# --- Nature of the parameter ---
kind: validation
value_type: integer
value_schema: null

# --- Where it is used ---
applies_to_variables: []

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
  notes: "The marital status variable spec does not yet exist in this
          repository. This parameter is included to demonstrate the
          validation kind of parameter."
---

## Definition

Defines an integer threshold that can be used to flag marital status records
for review when the reported age is below the applicable legal minimum.

## Why this is country specific

Marriage-age legislation differs across countries and periods. The parameter
is a validation input only and does not define or change harmonized value codes.

## How the agent uses it

Once a variable spec declares this parameter, the agent selects the record for
the survey ISO3 code and survey ID year and applies it as a validation check.
No current variable spec declares it.

## Fallback behavior

The fallback policy is undecided. The validator flags this parameter, and no
harmonization may rely on it until the GPID Team approves a policy.

## Data sources for populating values

Values require verified national legislation and an approved citation. No
illustrative value is a verified legal fact.

## Change log

| Date | Version | Change | Authority |
|---|---|---|---|
| 2026-07-28 | 0.1 | Initial draft | GPID Team |
