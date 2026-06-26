---
# ================================================================
# DECISION RULE — GMD Canonical Variable Schema v0.1
# ================================================================

rule_id: RULE-EDU-001
rule_name: "Age restriction for categorical education variables"
scope: module
module_id: MOD-DEM
applies_to_variables:
  - VAR-educat7
  - VAR-educat5
  - VAR-educat4
  - VAR-primarycomp
priority: 95
version: "0.1"
status: draft
authority: "GPID Team"
effective_from: "2026-06-25"
effective_to: null
---

## Plain language rule

For all categorical education variables, set the value to `.c` for every
individual whose age is below the country-specific minimum education age
(`mineducatage`). Never guestimate or impute education for these individuals.

## Formal IF/THEN

```
IF   age < mineducatage
THEN set education variable = .c
     (applies to VAR-educat7, VAR-educat5, VAR-educat4, VAR-primarycomp)

ELSE IF   mineducatage is not defined for this survey
THEN      apply the education section to all individuals and document
          the absence of mineducatage in the do-file notes

ELSE IF   age >= mineducatage
THEN      proceed with harmonization according to the variable's own
          construction rules
```

## Prohibitions

- Do not guestimate or impute education for individuals below `mineducatage`
  using age, household relationship, or any other variable.
- Do not use standard Stata missing (`.`) for the age restriction. Use `.c`.
- Do not apply different age cutoffs to different education variables within
  the same survey. All categorical education variables must use the same
  `mineducatage` value.

## Rationale

The education section of many surveys is administered only to individuals
above a certain age. Applying education categories to younger individuals
would introduce spurious patterns. Using `.c` rather than standard missing
preserves the reason for the missing value in the harmonized data.

## Test examples

| Condition | Correct output for educat4 |
|---|---|
| age = 8, mineducatage = 10 | educat4 = .c |
| age = 15, mineducatage = 10 | proceed with harmonization |
| mineducatage not defined | harmonize all ages, document in notes |
| ECA survey, individual age 14 | check mineducatage; likely educat4 = .c |

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-06-25 | 0.1     | Initial draft | GPID Team  |
