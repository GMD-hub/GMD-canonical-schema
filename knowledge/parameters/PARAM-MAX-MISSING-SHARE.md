---
# ================================================================
# PARAMETER DEFINITION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
parameter_id: PARAM-MAX-MISSING-SHARE
parameter_name: "Maximum share of missing values in a harmonized variable"
module_id: MOD-DWL
schema_version: "0.1"
status: draft
authority: "GPID Team"

# --- Nature of the parameter ---
kind: validation
value_type: integer          # percent
value_schema: null

# --- Where it is used ---
# Symmetric with VAR.country_parameters: every variable listed here lists this
# parameter back in its own `country_parameters:` block.
applies_to_variables:
  - VAR-ac
  - VAR-acquihouse
  - VAR-acquiland
  - VAR-agriland
  - VAR-agrilandownti
  - VAR-areaagriland
  - VAR-areadocuagriland
  - VAR-areainheragriland
  - VAR-areaownagriland
  - VAR-areapurchagriland
  - VAR-arearentinagriland
  - VAR-arearentoutagriland
  - VAR-areaspace
  - VAR-bath
  - VAR-bcycle
  - VAR-boat
  - VAR-canoe
  - VAR-car
  - VAR-cellphone
  - VAR-computer
  - VAR-docuagriland
  - VAR-doculand
  - VAR-dwelownlti
  - VAR-dwelownti
  - VAR-dweltyp
  - VAR-etablet
  - VAR-ewpump
  - VAR-fan
  - VAR-femagrilandownti
  - VAR-femdoculand
  - VAR-femdwelownlti
  - VAR-floor
  - VAR-floorcs
  - VAR-fridge
  - VAR-inheragriland
  - VAR-internet
  - VAR-kitchen
  - VAR-landownti
  - VAR-landphone
  - VAR-male
  - VAR-mcycle
  - VAR-ownagriland
  - VAR-ownhouse
  - VAR-ownland
  - VAR-oxcart
  - VAR-phone
  - VAR-purchagriland
  - VAR-radio
  - VAR-rentinagriland
  - VAR-rentoutagriland
  - VAR-ricecook
  - VAR-roof
  - VAR-roofcs
  - VAR-rooms
  - VAR-sellagriland
  - VAR-selldwel
  - VAR-sellland
  - VAR-sewmach
  - VAR-stove
  - VAR-transagriland
  - VAR-transdwel
  - VAR-transland
  - VAR-tv
  - VAR-tvcable
  - VAR-typlivqrt
  - VAR-video
  - VAR-wall
  - VAR-wallcs
  - VAR-washmach
  - VAR-ybuilt

# --- Behavior when no country record exists ---
# A constant for now: the global default is the value. No country record carries it yet.
fallback_policy: use_global_default
global_default: 2

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: null
  extraction_method: manual
  extracted_on: "2026-11-17"
  human_reviewed: false
  reviewer: null
  notes: "Written on instruction of 2026-11-17 to hold in one place the 2 percent limit that 69
          dwelling variables each stated in their escalation triggers (more than 2 percent of
          records fall into .b or .c) and that VAR-male stated for its own codes. Each of the
          70 variables listed here now declares this parameter and names it in that trigger. The section of the source document that
          states the limit was not located in this repository, so source_section is null.
          Held as a constant for now: the global default is the value."
---

## Definition

The largest share of a harmonized variable's observations, in percent, that may
carry a missing value. It applies to the variables that declare it.

## What counts

- Counted: the observations inside the variable's universe that carry a
  cell-level missing value, all kinds combined.
- Compared with: the observations inside the variable's universe.
- Not counted: an observation outside the universe (`MISS-OUTSIDE-UNIVERSE`).
- Not measured: a variable that is not produced for a survey. It has no
  observations; its column-level missing value is reported with the survey.

## How the agent uses it

For each variable that declares this parameter, compute the share above and
compare it with the value. A variable above the value is escalated, with its
share and the count of each missing value. The check changes no harmonized
value.

## Fallback behavior

`fallback_policy: use_global_default`. No country record carries this parameter
yet, so the global default is the value for every country and year.

## Open questions

- Whether the same limit applies to more variables. It is attached to the 69 dwelling
  variables and to `male`, the ones that stated it; the record still carries the
  dwelling module in its `module_id`, which the model requires.
- Whether a variable above the value is only escalated or is also not released.

## Change log

| Date | Version | Change | Authority |
|---|---|---|---|
| 2026-11-17 | 0.1 | Initial draft | GPID Team (proposed) |
