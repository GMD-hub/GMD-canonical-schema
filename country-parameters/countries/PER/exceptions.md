---
# ================================================================
# COUNTRY EXCEPTIONS - GMD Country Parameter Layer v0.1
# ================================================================

country_id: CTY-PER
iso3: PER
schema_version: "0.1"
status: draft

exceptions:

  - exception_id: EXC-PER-001
    applies_to_variables:
      - VAR-educy
    effective_from: 1980
    effective_to: 1999
    condition: "PLACEHOLDER. Natural language statement of when this
                exception applies."
    action: "PLACEHOLDER. Natural language statement of what to do."
    rationale: "PLACEHOLDER, ILLUSTRATIVE ONLY. This exception is a
                structural example and does not describe a real Peruvian
                situation."
    provenance:
      source: "PLACEHOLDER, NOT VERIFIED."
      approved_by: null
      approved_on: null
      human_reviewed: false
---

## Purpose

Country exceptions express conditional logic that cannot be reduced to a
parameter value. Each exception has a natural-language condition and action,
a variable scope, and an inclusive validity window.

## Exception notes

`EXC-PER-001` is a structural example only. Its condition, action, rationale,
and provenance all identify it as an unverified placeholder. It does not
represent a real situation in Peru and must not be used in production.

## What exceptions may not do

An exception may never redefine a variable's value codes, data type, missing
codes, or derivation graph. If a proposed change would do any of those things,
it belongs in the universal CVS and must follow the CVS approval path.

## Change log

| Date | Version | Change | Authority |
|---|---|---|---|
| 2026-07-28 | 0.1 | Initial illustrative draft | GPID Team |
