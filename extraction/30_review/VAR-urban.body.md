## Definition

`urban` records whether the household is located in an urban or rural area according to the survey's sampling frame. 

urban must be a numeric binary variable with the following valid nonmissing values:
1 = Urban
0 = Rural

## Conceptual intent

`urban` is a core variable used to disaggregate indicators and to perform data-quality and consistency checks.

## Construction notes

Apply the following rules in order:

1. If a source variable directly classifies the household’s location as urban or rural, recode the source categories as follows:
Urban → 1
Rural → 0
2. Otherwise, if the source variable includes semi-urban, mixed, or an equivalent intermediate category, classify that category base con the specific country classification.
3. Otherwise, if another set of variables explicitly identifies the household’s location as urban or rural, use that information to construct urban.
4. Otherwise, assign the applicable missing-value code to urban.

Important. Do not infer urban from population size, administrative level, settlement name, household characteristics, infrastructure, geographic coordinates, or other indirect information unless the survey documentation explicitly defines how that information maps to the country’s official urban-rural classification.

Do not assign all households to urban or rural when the country or survey does not use an urban-rural classification.

Investigate original survey codes such as -99, -999, and -88. Convert each code to the corresponding missing-value code based on its documented meaning. Label and document any additional special missing values in the variable notes. The missing-value guidance distinguishes unavailable, unharmonized, incompatible, refusal, “do not know,” and other-category values.

## Consistency checks

After constructing urban, apply the following checks:
- Flag urban when it is nonmissing and not equal to 0 or 1.
- Compare the distribution of urban with the original source categories to confirm that no categories were omitted or incorrectly recoded.


## Escalation triggers

Escalate when:
- the source documentation does not identify which categories are urban or rural;
- a source category is neither urban, rural, semi-urban, nor mixed;
conflicting source variables assign different urban-rural classifications to the same household;
- the country or survey does not use an urban-rural classification;
the source classification changes between survey rounds and the correct mapping cannot be determined;
- the meaning of an original missing-value code cannot be established;
- urban is missing for a substantial share of households even though source information appears to be available;
- nonbinary or inconsistent values occur systematically;


## Common mistakes

- Using the statistical office's broad regional variable instead of the actual locality-type variable for `urban`.
- Coding a missing locality as rural (0) instead of an explicit missing code.


## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-07 | 0.1     | Initial fixture | Calibration |
