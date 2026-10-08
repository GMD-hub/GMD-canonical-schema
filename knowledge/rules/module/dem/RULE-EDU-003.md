---
# ================================================================
# DECISION RULE - GMD Canonical Variable Schema v0.2
# ================================================================

rule_id: RULE-EDU-003
rule_name: "educy construction: individual-level path selection via grade
            arithmetic and country education-level crosswalk, and
            no-guestimation constraint"
scope: module
module_id: MOD-DEM
applies_to_variables:
  - VAR-educy
priority: 80
version: "0.2"
status: draft
authority: "GPID Team"
effective_from: "2026-06-25"
effective_to: null
---

## Plain language rule

Construct `educy` per individual, following whatever data point is actually
present for that record. Surveys route different individuals to different
questions via skip patterns, so the same survey can have grade-based,
level-based, and direct-years respondents side by side. Prefer the most
direct source. Use grade-based arithmetic for grade 1-12. For anything
beyond grade 12 (tertiary, vocational, or other post-secondary levels),
resolve years through the country's education-level crosswalk rather than a
fixed GMD-wide table. Never guestimate using age or other proxy variables.
Never count repeated grades as additional years. Never award years for
in-progress work beyond what is actually confirmed.

## Formal IF/THEN

```
/* --- Path selection (evaluated per individual; a single survey can route
       different individuals to different questions via skip patterns) --- */

IF   the individual has a reported value for total years of education or
     schooling (direct question)
THEN set educy = reported years
     cross-check for plausibility against age and educat7

ELSE IF   school = 1 (currently enrolled)
          AND the individual has a recorded current grade level (grade 1-12)
THEN      educy = current_grade - 1

ELSE IF   school = 1 (currently enrolled)
          AND the individual has a recorded current year within a
          post-grade-12 track (tertiary, vocational, or other
          post-secondary level)
THEN      educy = base_years + (current_track_year - 1)

ELSE IF   school = 1 (currently enrolled)
          AND the individual reports a named post-grade-12 level/program
          with no current-year or progress detail
THEN      educy = base_years
          flag the record: "enrolled in [level], in-progress duration
          unknown; educy reflects last completed level only"

ELSE IF   school = 0 (not currently enrolled)
          AND the individual has a recorded highest completed grade level
          (grade 1-12)
THEN      educy = highest_completed_grade

ELSE IF   school = 0 (not currently enrolled)
          AND the individual has a recorded ordinal year within a
          post-grade-12 track (e.g., "1st year", "2nd year") rather than a
          named qualification
THEN      educy = base_years + ordinal_year_number

ELSE IF   school = 0 (not currently enrolled)
          AND the individual has a recorded national education level or
          qualification label beyond simple grade numbering
THEN      match the reported level text to a country_entry_id in
          PARAM-EDU-LEVEL-CROSSWALK resolved from the country layer for the
          survey ISO3 code and survey ID year
          the matched record supplies isced_level, gmd_educat4_target,
          gmd_educat5_target, gmd_educat7_target, and cum_years_schooling
          set educy = cum_years_schooling for the matched country_entry_id
          document the matched country_entry_id in the do-file notes

ELSE      set educy = .b

/* --- Shared definition --- */

base_years = cum_years_schooling for the last completed level before the
             post-grade-12 track (typically upper secondary completion;
             12 years in most systems, resolved from the general-track
             ISCED-3 row in PARAM-EDU-LEVEL-CROSSWALK when the country's
             value differs)

/* --- Grade repetition (applied per individual, always) --- */

educy counts each grade level exactly once.
Repetition of a grade does not increase educy.
```

## Prohibitions

- Do not guestimate `educy` using age, household relationship, or any
  variable other than direct grade/year/level data.
- Do not count repeated grades as additional years of education.
- Do not set `educy = 0` for individuals with unknown or missing education.
  Use `.b` instead.
- Do not award years for an in-progress post-12 track beyond `base_years`
  when no current-year or progress detail is available for that
  individual.
- Do not use a `PARAM-EDU-LEVEL-CROSSWALK` record selected for the wrong
  ISO3 code or survey ID year.
- Do not continue when no valid country crosswalk record exists for a
  reported national level and the registry fallback policy blocks
  construction. Stop and escalate.

## Rationale

`educy` must be reproducible across harmonizations of the same survey.
Skip patterns mean individual records within one survey can carry different
kinds of source data (direct years, numeric grade, or a named national
level), so path selection is evaluated per individual rather than assumed
uniform across the survey. Grade 1-12 is handled by direct arithmetic
because grade numbering is cumulative and country-independent in practice.
Anything beyond grade 12 depends on country-specific program structures, so
those paths resolve through `PARAM-EDU-LEVEL-CROSSWALK`, which carries a
per-country, per-national-level `cum_years_schooling` value traceable to a
specific `country_entry_id`. This replaces the former fixed GMD-wide
tertiary-year table (BA/MA/PhD +N years), which could not reflect real
variation in program length across countries. The prohibition on
guestimation, including for in-progress post-12 work, prevents silent
variation across surveys where progress detail is absent.

## Test examples

| Situation | Correct output |
|---|---|
| Survey asks "years of schooling", reports 9 | educy = 9 |
| Enrolled, currently grade 7 | educy = 6 |
| Not enrolled, completed grade 12 | educy = 12 |
| Enrolled, currently 2nd year of a tertiary program | educy = base_years + 1 |
| Enrolled, "currently in Bachelor of Engineering," no year given | educy = base_years, flagged |
| Not enrolled, reports "2nd year" of tertiary (no qualification name) | educy = base_years + 2 |
| Not enrolled, reports "Bachelor of Engineering" (completed) | educy = cum_years_schooling matched via crosswalk |
| Individual repeated grade 3 twice | grade 3 counts as 1 year |
| No grade, level, or year information available | educy = .b |

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-06-25 | 0.1     | Initial draft | GPID Team  |
| 2026-09-30 | 0.2     | Replaced `PARAM-EDU-YEARS-BY-LEVEL` and the fixed tertiary-year table with `PARAM-EDU-LEVEL-CROSSWALK`-based resolution; reframed path selection to per-individual evaluation; added enrolled/not-enrolled post-grade-12 paths (ordinal year, named level, in-progress floor) | GPID Team |

