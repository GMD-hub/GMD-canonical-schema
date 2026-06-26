---
# ================================================================
# DECISION RULE — GMD Canonical Variable Schema v0.1
# ================================================================

rule_id: RULE-EDU-003
rule_name: "educy construction — path selection, enrollment adjustment,
            tertiary assumptions, and no-guestimation constraint"
scope: module
module_id: MOD-DEM
applies_to_variables:
  - VAR-educy
priority: 80
version: "0.1"
status: draft
authority: "GPID Team"
effective_from: "2026-06-25"
effective_to: null
---

## Plain language rule

Construct `educy` from the most direct source of grade or year information
available in the survey. Adjust for enrollment status. Apply fixed-year
assumptions for tertiary when grade data is absent. Never guestimate using
age or other proxy variables. Never count repeated grades as additional years.

## Formal IF/THEN

```
/* --- Path selection --- */

IF   survey contains a direct question on years of education or schooling
THEN set educy = reported years
     cross-check for plausibility against age and educat7

ELSE IF   survey contains current or highest grade level
          AND individual is currently enrolled (school = 1)
THEN      educy = years_for(current_grade - 1)
          using education_years_by_country_v1

ELSE IF   survey contains current or highest grade level
          AND individual is not currently enrolled (school = 0)
THEN      educy = years_for(highest_completed_grade)
          using education_years_by_country_v1

ELSE IF   survey contains only categorical education levels
THEN      use highest available categorical variable as source:
            IF   educat7 is defined  -> use educat7 categories
            ELSE IF educat5 defined  -> use educat5 categories
            ELSE IF educat4 defined  -> use educat4 categories
          convert categories to years using education_years_by_country_v1
          document source variable in do-file notes

ELSE      set educy = .b

/* --- Tertiary adjustment (applied within any path above
       when tertiary education is identified) --- */

IF   individual has completed specified tertiary degree
THEN add to years of completed secondary:
       BA/BSc: +4  |  MA/MSc: +6  |  PhD: +8

ELSE IF   individual has not completed tertiary
          OR completion status cannot be ascertained
THEN      add to years of completed secondary:
            BA/BSc: +2  |  MA/MSc: +5  |  PhD: +7

/* --- Grade repetition (applied always) --- */

educy counts each grade level exactly once.
Repetition of a grade does not increase educy.
```

## Prohibitions

- Do not guestimate `educy` using age, household relationship, or any
  variable other than direct grade/year data and categorical education vars.
- Do not count repeated grades as additional years of education.
- Do not set `educy = 0` for individuals with unknown or missing education.
  Use `.b` instead.
- Do not apply tertiary year assumptions without confirming the degree type.
  If degree type is unknown, use the "not completed" assumptions.
- Do not use a lookup table from the wrong country. Verify the country code.

## Rationale

`educy` must be reproducible across harmonizations of the same survey. The
three-path hierarchy ensures every harmonizer follows the same decision
sequence. The prohibition on guestimation prevents silent variation across
surveys where grade data is absent. The fixed tertiary-year assumptions are
a GMD-wide convention ensuring consistency when surveys do not record
tertiary grade levels explicitly.

## Test examples

| Situation | Correct output |
|---|---|
| Survey asks "years of schooling", reports 9 | educy = 9 |
| Enrolled, currently grade 7, 6-year primary country | educy = 6 |
| Not enrolled, completed grade 12, 6+6 system | educy = 12 |
| Only educat7 available, code 3 (primary complete), 6-year primary | educy = 6 |
| Completed BA, secondary = 12 years, tertiary years not recorded | educy = 16 |
| No grade or category information available | educy = .b |
| Individual repeated grade 3 twice | grade 3 counts as 1 year |

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-06-25 | 0.1     | Initial draft | GPID Team  |
