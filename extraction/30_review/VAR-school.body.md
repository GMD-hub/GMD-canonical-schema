## Definition

`school` records whether an individual is currently enrolled in school.

`school` must be a numeric binary variable with the following valid nonmissing values:
1 = Yes, currently enrolled
0 = No, not currently enrolled

## Conceptual intent

`school` captures current enrollment status. It differs from `everattend`, which records whether the individual has attended school at any time in the past.
Use `school` to identify individuals currently participating in education. Do not use past attendance, completed education, literacy, or years of education as substitutes for current enrollment.
human capital analysis.

## Construction notes

Apply the following rules in order:
- Identify the source variables/question that records current school enrollment.
- If the source response means currently enrolled, assign school = 1.
- If the source response means not currently enrolled, assign school = 0.
- If the individual was not asked the question because the individual is outside the survey-defined eligible population, assign the applicable missing-value code.
- Otherwise, if current enrollment cannot be determined, assign the applicable missing-value code.
- If enrollment was asked only of persons above or below a specified age, do not assign enrollment status to persons outside that population.

Important. Do not guess, approximate, or impute school from other variables like age.

Investigate original survey codes such as -99, -999, and -88. Convert each code to the applicable missing-value code based on its documented meaning. Label and document any additional special missing values in the variable notes.

## Consistency checks

After constructing school, apply the following checks:
- Flag school when it is nonmissing and not equal to 0 or 1.
- Flag school when it is missing for an individual who is eligible for the question and has a valid source response.
- Flag school when it is nonmissing for an individual outside the population eligible for the enrollment question.
- Flag records where school = 1 and everattend = 0.
- Flag records where school = 1 and everattend is missing even though sufficient source information exists to construct everattend.
- Verify that original refusal, “do not know,” not-applicable, and other special categories were not recoded as 0.

## Escalation triggers

Escalate when:
- the source question does not clearly distinguish current enrollment from attendance;
- the enrollment reference period cannot be determined;
- the questionnaire, manual, skip pattern, and observed data imply different eligibility populations;
- the country-specific age cutoff for the enrollment question cannot be established;
- school and everattend are systematically inconsistent;
- multiple source variables provide conflicting current-enrollment information;
- the meaning of an original missing-value code cannot be established;
- enrollment values are systematically missing within the eligible population; or
- assigning a special missing-value code requires an interpretation not supported by the questionnaire or manual.

## Common mistakes

- Confusing `school` (current enrollment) with `everattend` (ever attended).
- Guestimating enrollment for age groups the survey did not ask about.
- Using a standard missing (`.`) instead of an explicit extended missing code.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
