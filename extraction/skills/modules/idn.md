# Module: IDN — Identification Variables v1

## Source Chapter

`chapter2-IDN.qmd`

## Module Code

`MOD-IDN` (Identification). Not ISO 3166-1 alpha-3 for Indonesia.

## Variable Conventions

Identification variables capture household member demographics essential for
harmonization: age, sex, relationship to head, marital status.

## Expected Variables

- age (member age in years)
- male (sex of household member — binary)
- marital_status
- relationship_to_head

## Common Edge Cases

- Age may be top-coded (e.g., 95+) or have minimum values
- Sex codes may include non-standard values requiring rule mapping
- Relationship codes vary widely across surveys
- Marital status categories differ by country

## Source Patterns

The chapter typically contains:
- A summary table of identification variables
- Individual subsections with value codes for each variable
- References to ISIC/ISCO standards for occupation codes
