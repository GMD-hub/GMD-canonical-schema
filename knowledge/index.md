# CVS Artifact Index

This file is the master registry of all artifacts in the knowledge base.
Every artifact must be listed here. The index is the agent's entry point
to the knowledge base.

Last updated: 2026-07-28
Schema version: 0.1

## Variable specifications

| Variable ID | Canonical label | Module | File | Status | Version |
|---|---|---|---|---|---|
| VAR-male | Sex of household member | MOD-DEM | variables/dem/VAR-male.md | draft | 0.1 |
| VAR-educat4 | Highest education level completed, 4 categories | MOD-DEM | variables/dem/VAR-educat4.md | draft | 0.1 |
| VAR-educy | Years of education completed | MOD-DEM | variables/dem/VAR-educy.md | draft | 0.1 |

## Decision rules

| Rule ID | Rule name | Scope | Module | File | Status | Version |
|---|---|---|---|---|---|---|
| RULE-SEX-001 | Binary sex mapping and exclusion of non-standard codes | module | MOD-DEM | rules/module/dem/RULE-SEX-001.md | draft | 0.1 |
| RULE-EDU-001 | Age restriction for categorical education variables | module | MOD-DEM | rules/module/dem/RULE-EDU-001.md | draft | 0.1 |
| RULE-EDU-002 | educat4 derivation order and recode | module | MOD-DEM | rules/module/dem/RULE-EDU-002.md | draft | 0.1 |
| RULE-EDU-003 | educy construction: path selection, enrollment adjustment, tertiary assumptions | module | MOD-DEM | rules/module/dem/RULE-EDU-003.md | draft | 0.1 |

## Parameter definitions

| Parameter ID | Parameter name | Module | File | Status | Version |
|---|---|---|---|---|---|
| PARAM-EDU-YEARS-BY-LEVEL | Duration in years of each education level | MOD-DEM | parameters/PARAM-EDU-YEARS-BY-LEVEL.md | draft | 0.1 |
| PARAM-DEM-MIN-MARRIAGE-AGE | Minimum legal marriage age | MOD-DEM | parameters/PARAM-DEM-MIN-MARRIAGE-AGE.md | draft | 0.1 |

## Module specifications

None yet. To be added.

## Evaluation rubrics

None yet. To be added.

## Exceptions

No universal variable exceptions yet. Country exceptions are registered in
`country-parameters/countries/<ISO3>/exceptions.md` and are not stored under
`knowledge/`.

## Country layers

Country layer IDs use `CTY-<ISO3>`. The initial folders are PER, COL, ALB,
ROU, GHA, TZA, IDN, PHL, IND, BGD, EGY, and MAR. PER is an illustrative,
unverified worked example. All other country files are empty drafts.
