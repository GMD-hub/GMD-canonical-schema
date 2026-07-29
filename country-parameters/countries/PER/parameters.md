---
# ================================================================
# COUNTRY PARAMETERS - GMD Country Parameter Layer v0.1
# ================================================================

country_id: CTY-PER
country_name: "Peru"
iso3: PER
schema_version: "0.1"
status: draft

parameters:

  - parameter_id: PARAM-EDU-YEARS-BY-LEVEL
    effective_from: 1980
    effective_to: 1999
    value:
      primary: 6
      lower_secondary: 3
      upper_secondary: 2
    provenance:
      source: "PLACEHOLDER, NOT VERIFIED. Must be confirmed against the
               UNESCO ISCED mapping and national curriculum documentation
               before any use in production."
      verified_on: null
      human_reviewed: false
      reviewer: null

  - parameter_id: PARAM-EDU-YEARS-BY-LEVEL
    effective_from: 2000
    effective_to: null
    value:
      primary: 7
      lower_secondary: 3
      upper_secondary: 2
    provenance:
      source: "PLACEHOLDER, NOT VERIFIED."
      verified_on: null
      human_reviewed: false
      reviewer: null

  - parameter_id: PARAM-DEM-MIN-MARRIAGE-AGE
    effective_from: null
    effective_to: null
    value: 18
    provenance:
      source: "PLACEHOLDER, NOT VERIFIED. Must be confirmed against
               national legislation."
      verified_on: null
      human_reviewed: false
      reviewer: null
---

## Country notes

Every value in this file is an illustrative placeholder. None is a verified
fact about Peru, and none may be used in production before human review.

## Parameter notes

### PARAM-EDU-YEARS-BY-LEVEL

The two illustrative records demonstrate effective dating. The first closes
in 1999 and the second begins in 2000, so exactly one record is selected for
any covered survey ID year. The apparent change from 1999 to 2000 is a
structural example only and does not assert a real education reform.

### PARAM-DEM-MIN-MARRIAGE-AGE

The open-ended illustrative record demonstrates a validation parameter. The
value is not verified against Peruvian legislation.

## Verification status

All records have `human_reviewed: false`. Their provenance labels them as
placeholders, and production use is prohibited pending source verification and
GPID Team approval.

## Change log

| Date | Version | Change | Authority |
|---|---|---|---|
| 2026-07-28 | 0.1 | Initial illustrative draft | GPID Team |
