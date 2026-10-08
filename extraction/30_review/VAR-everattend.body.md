## Definition

`everattend` records whether an individual has attended school at any time in the past or is currently attending school.
`everattend` must be a numeric binary variable with the following valid nonmissing values:
1 = Yes, has attended school
0 = No, has never attended school
The duration of attendance is not relevant. Assign everattend = 1 if the individual attended school at any point, even for a short period.

## Conceptual intent

`everattend` captures lifetime school attendance. It differs from school, which records whether the individual is currently enrolled.

## Construction notes

Apply the following rules in order:
1. Identify the source variable or question that records whether the individual has ever attended school.
2. If the source response means that the individual has attended school at any time, assign everattend = 1.
3. If the source response explicitly means that the individual has never attended school, assign everattend = 0.
4. Otherwise, if school = 1, assign everattend = 1.
5. Otherwise, if current or completed education information explicitly establishes past attendance, assign everattend = 1.
6. Otherwise, assign the applicable missing-value code to everattend.

Important. Assign everattend = 0 only when the source information explicitly establishes that the individual has never attended school. Do not infer everattend = 0 from school = 0 or other indirect information.
- If the ever-attendance question was asked only of a survey-defined population, do not assign attendance status to individuals outside that population unless another source variable explicitly establishes that they attended school.
- Investigate original survey codes such as -99, -999, and -88. Convert each code to the applicable missing-value code based on its documented meaning. Label and document any additional special missing values in the variable notes.

## Consistency checks

After constructing everattend, apply the following checks:
- Flag everattend when it is nonmissing and not equal to 0 or 1.
- Flag records where school = 1 and everattend != 1.
- Flag records where everattend = 0 and an education variable contains valid information indicating school attendance.
- Flag everattend when it is missing and the source data contain sufficient information to establish past or current school attendance.
- Flag everattend when it is nonmissing for an individual outside the population eligible for the source question, unless another source variable explicitly supports the value.
- Verify that original refusal, “do not know,” not-applicable, and other special categories were not recoded as 0.
- Compare the distribution of everattend with school and the available education variables to identify systematic inconsistencies

## Escalation triggers

Escalate when:
- the source question does not clearly distinguish ever attending school from currently attending school;
- multiple source variables provide conflicting information about past school attendance;
- school and everattend are systematically inconsistent;
- the meaning of an original missing-value code cannot be established;
- assigning a special missing-value code requires an interpretation not supported by the questionnaire or manual.

## Common mistakes

- Confusing everattend with current enrollment.
- Assigning everattend = 0 when school = 0.
- Assigning everattend = 0 when education information is missing.
- Treating zero completed years or no completed education as evidence that the individual never attended school.
Requiring a minimum duration of attendance before assigning everattend = 1.
- Guessing attendance status for individuals outside the population covered by the source question.
- Recoding refusal, “do not know,” not-applicable, or undocumented source values as 0.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
