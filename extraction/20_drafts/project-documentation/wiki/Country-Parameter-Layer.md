# Country Parameter Layer

## Why it exists

Some harmonization rules are universal while their inputs vary by country or
over time. Education-cycle duration is one example. The universal CVS defines
what the value means and the shape it must have; a country record supplies the
applicable value for a period.

This separation keeps `knowledge/` universal and makes country evidence
explicit, effective dated, reviewable, and replaceable without changing a
variable's structural contract.

## Mandatory loading algorithm

For every run and every variable:

1. Derive the survey ID year from the calendar year in which fieldwork began.
2. Load `country-parameters/countries/<ISO3>/parameters.md`.
3. Load `country-parameters/countries/<ISO3>/exceptions.md`.
4. Select each record for which the year is within the inclusive validity
   window. Null lower or upper bounds are open ended.
5. Confirm that declared parameter requirements are satisfied.
6. Apply fallback policy where no valid country record exists.
7. Record each parameter value, its window, its source or fallback, and the CVS
   Git commit hash in the Harmonization Specification draft.

The survey ID year is not the welfare year and is not necessarily the year in
which fieldwork ended.

## Resolution example

Suppose a survey began fieldwork in 1999 and the country file contains:

| Record | Effective from | Effective to |
|---|---:|---:|
| A | 1980 | 1999 |
| B | 2000 | null |

Record A applies because both bounds are inclusive. A survey beginning in
2000 selects record B. Overlapping records for the same parameter are a
structural failure.

## Parameters versus exceptions

Use a parameter when the country variation is a value with a stable universal
meaning, such as a legal age or a mapping of education levels to years.

Use an exception when the variation is conditional logic that cannot be
reduced to a parameter. An exception states when it applies, what action to
take, why, which variables it affects, and its validity window.

Neither mechanism may redefine value codes, missing codes, data types, or
derivation relationships. Such a proposal belongs in the universal CVS review
path.

## Fallback behavior

When no selected record exists, read the parameter definition under
`knowledge/parameters/`:

- `use_global_default`: use the non-null registered default and identify it as
  a fallback in downstream provenance;
- `skip_check`: omit only the affected validation check;
- `block_and_escalate`: stop the affected operation;
- `undecided`: stop and request a GPID Team decision.

Never infer a country value from nearby countries, an outdated record, or
general knowledge.

## Current coverage warning

The present country layer is not production ready. PER contains explicitly
unverified placeholders demonstrating validity windows and record shape. The
remaining country folders are empty drafts. The validator's coverage and
unverified-value reports are therefore operational review inputs, not noise to
be suppressed.

## Adding country content

Country files are human-owned governed artifacts. Before adding a value or
exception, establish an authoritative source, use the correct ISO3 folder,
match an existing parameter or variable ID, define non-overlapping validity,
record provenance, obtain human review, and run repository validation.
