# Module: DEM — Demographics Variables v1

## Source Chapter

`chapter4-DEM.qmd`

## Module Code

`MOD-DEM` (Demographics)

## Variable Conventions

Demographics variables include sex (male), education levels (educat4, educat5, educat7),
years of education (educy), literacy, disability status, and minimum education age.

## Expected Variables

- male (sex of household member — binary)
- age (member age in years)
- relationship_to_head
- marital_status
- educat4 (4-level education — ages 5+)
- educat5 (5-level education)
- educat7 (7-level education)
- educy (years of education, derived from educat7)
- literacy
- disability_status

## Sub-Domains

- **Core demographics**: male, age, relationship
- **Education**: educat4, educat5, educat7, educy, literacy
  - Education variables use age restrictions (e.g., educat4 for ages 5+)
  - educy is constructed from educat7 with enrollment adjustments
  - See PARAM-EDU-YEARS-BY-LEVEL for country-specific education duration
- **Disability**: disability status indicators (embedded in DEM)

## Common Edge Cases

- Education variables have prerequisite age filters
- educy construction varies by survey year and education system
- Years of education requires country-specific education duration parameters
- Disability questions vary significantly across surveys

## Source Patterns

The chapter typically contains:
- A summary table of demographic variables
- Education level value codes (4-level, 5-level, 7-level)
- Construction rules for derived variables
- References to country-specific education parameters
