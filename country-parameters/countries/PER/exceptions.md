---
# ================================================================
# COUNTRY EXCEPTIONS - GMD Country Parameter Layer v0.1
# ================================================================

country_id: CTY-PER
iso3: PER
schema_version: "0.2"
status: draft

exceptions:

  - exception_id: EXC-PER-001
    applies_to_variables:
      - VAR-welfare
    effective_from: 2010
    effective_to: 2016
    selectors:
      survey_type: income
      rural_only: true
    conflict_policy: higher_precedence_wins
    precedence: 20
    condition: If survey is income and household is rural
    condition_structured:
      all:
        - field: survey_type
          op: eq
          value: income
        - field: rural
          op: eq
          value: 1
    action: Multiply welfare by 1.15
    action_structured:
      operation: multiply
      target: welfare_value
      factor: 1.15
    rationale: Country-year adjustment rule
    provenance:
      source: approved memo
      approved_by: null
      approved_on: null
      human_reviewed: false
---

## Purpose

Country exceptions express conditional logic that cannot be reduced to a
parameter value. Each exception has a natural-language condition and action,
a variable scope, and an inclusive validity window.

## Exception notes

`EXC-PER-001` defines a welfare adjustment rule for income surveys in rural
households during 2010-2016.

## What exceptions may not do

An exception may never redefine a variable's value codes, data type, missing
codes, or derivation graph. If a proposed change would do any of those things,
it belongs in the universal CVS and must follow the CVS approval path.

## Change log

| Date | Version | Change | Authority |
|---|---|---|---|
| 2026-07-28 | 0.1 | Initial illustrative draft | GPID Team |
| 2026-09-06 | 0.2 | Add structured PER welfare adjustment exception | GPID Team |
