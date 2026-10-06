## Definition

`age` records each household member's age in completed years on the interview date. It is the number of full years elapsed between the person's date of birth and the interview date. 
 Create `age` for every household member when the required source information is available. 

 `age` must be numeric, nonnegative, and integer-valued. Valid nonmissing values are integers from 0 through 120. 

 If the survey provides age only in categories and a continuous age cannot be derived, do not assign an approximate age. Code `age` using the applicable missing-value code and store the original age categories in the string variable `agecat`. The GMD guidelines define `agecat` as the survey-specific age groups used when age is available only in categories. age groups and not a continuous age variable, record the original categories in `agecat`. Do not try to assigning an approximate age.

## Conceptual intent

`age` is a core demographic variable used to construct age-dependent variables and perform data-quality and consistency checks..

## Construction notes

Apply the following rules in order: 
1. If a source variable records the household member's age in completed years at the time of the interview, use that variable to construct `age`. 
2. Otherwise, if the person's date of birth and the interview date are available, calculate `age` as the number of full years between the two dates. Do not round to the nearest year. 
3. Otherwise, if only age categories are available, store those categories in `agecat` and assign the applicable missing-value code to `age`. 
4. Otherwise, assign the applicable missing-value code to `age`. 

Important. Do not guess, approximate, or impute `age` from household relationships, education, marital status, or other indirect information. 

Investigate original survey codes such as `-99`, `-999`, and `-88`. Convert each code to the corresponding missing-value code based on its documented meaning. Label and document any additional special missing values in the variable notes.

## Consistency checks

After constructing `age`, apply the following checks: 
- Flag `age` when it is nonmissing and `age < 0`. 
- Flag `age` when it is nonmissing and `age > 120`. 
- Flag `age` when it is nonmissing and not an integer. 
- Flag `age` when it is missing for a household member and the source data contain sufficient information to construct it. 

## Escalation triggers 
- the source information does not determine which value should be used to construct `age`; 
- the meaning of an original missing-value code cannot be established; 
- only age categories are available but continuous age is not; 
- missing, invalid, or inconsistent age values occur systematically.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
