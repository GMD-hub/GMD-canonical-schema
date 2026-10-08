## Definition

`agecat` records each household member's age group as defined in the original survey.
Create `agecat` when the survey provides age in categories rather than in completed years and a continuous age variable cannot be constructed.
`agecat` must be a string, country-specific categorical variable. Preserve the age-group boundaries and category meanings provided by the survey. Examples include "15 years or younger", "15-24 years old", "25-54 years old", "55-64 years old", and "65 years or older".
Do not assign an approximate continuous age, category midpoint

## Conceptual intent

`agecat` preserves the age information collected by the survey when exact age in completed years is unavailable. It supports age-group disaggregation while retaining the survey-specific category definitions.

## Construction notes

Apply the following rules in order:
1. If a source variable records age in completed years, use it to construct age. Do not construct agecat unless the survey also contains an independently collected age-category variable.
2. Otherwise, if date of birth and interview date are available, construct age from those dates. Do not derive agecat unless the original survey explicitly collected or defined age groups.
3. Otherwise, if the survey records age only in categories, create agecat from the original age-category variable and assign the applicable missing-value code to age.

Preserve the original survey categories. Do not combine, split, reorder, standardize, or redefine the age groups.

Convert numeric source codes and their value labels into strings that retain both the code and category meaning. Use the format "code - category label", for example:
"1 - 15 years or younger"
"2 - 15-24 years old"
"3 - 25-54 years old"
"4 - 55-64 years old"
"5 - 65 years or older"

Investigate original survey codes such as -99, -999, and -88. Convert each code to the applicable missing representation based on its documented meaning. Label and document any additional special missing values in the variable notes. The missing-value guidance requires harmonizers to investigate survey-specific codes and document additional missing-value definitions.

## Consistency checks
After constructing agecat, apply the following checks:
- Flag agecat when it is not stored as a string variable.
- Flag agecat when a source age-category code has no corresponding category label.
- Flag agecat when categories were replaced by midpoints, boundaries, or approximate ages.
- Flag agecat when category labels omit information required to interpret the age interval, such as the lower boundary, upper boundary, or open-ended limit.
- Flag agecat when it is missing even though the source data contain a valid age-category value.
- If both age and agecat are available from the source survey, flag records where the value of age falls outside the interval represented by agecat.
- Verify that age categories are mutually exclusive and exhaustive as defined by the survey.
- Confirm that the raw category labels are preserved verbatim and not
  recoded or truncated.

## Escalation triggers

- The source documentation does not define the meaning or boundaries of one or more age categories.
- A source category combines values that cannot be represented unambiguously as an age interval.
The source category labels conflict with their documented numeric boundaries.
- The source information does not determine whether age or agecat should be constructed.
- The meaning of an original missing-value code cannot be established.
- Missing, unlabeled, overlapping, or inconsistent age categories occur systematically.
- age and agecat are systematically inconsistent when both are available.

## Common mistakes

- Transcoding the string category labels into numeric codes, losing the original survey labels.


## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
