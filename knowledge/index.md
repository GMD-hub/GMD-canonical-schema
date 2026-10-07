# CVS Artifact Index

This file is the master registry of all artifacts in the knowledge base.
Every artifact must be listed here. The index is the agent's entry point
to the knowledge base.

Last updated: 2026-10-07
Schema version: 0.2

## Variable specifications

| Variable ID | Canonical label | Module | File | Status | Version |
|---|---|---|---|---|---|
| VAR-male | Sex of household member | MOD-DEM | variables/dem/VAR-male.md | draft | 0.1 |
| VAR-educat4 | Highest education level completed, 4 categories | MOD-DEM | variables/dem/VAR-educat4.md | draft | 0.1 |
| VAR-educy | Years of education completed | MOD-DEM | variables/dem/VAR-educy.md | draft | 0.2 |
| VAR-subnatid1 | Subnational ID - highest level | MOD-GEO | variables/geo/VAR-subnatid1.md | draft | 0.1 |
| VAR-subnatid1prev | Subnational ID previous - highest level | MOD-GEO | variables/geo/VAR-subnatid1prev.md | draft | 0.2 |
| VAR-subnatid2 | Subnational ID - second highest level | MOD-GEO | variables/geo/VAR-subnatid2.md | draft | 0.1 |
| VAR-subnatid2prev | Subnational ID previous - second highest level | MOD-GEO | variables/geo/VAR-subnatid2prev.md | draft | 0.2 |
| VAR-subnatid3 | Subnational ID - third highest level | MOD-GEO | variables/geo/VAR-subnatid3.md | draft | 0.1 |
| VAR-subnatid3prev | Subnational ID previous - third highest level | MOD-GEO | variables/geo/VAR-subnatid3prev.md | draft | 0.2 |
| VAR-subnatid4 | Subnational ID - fourth highest level | MOD-GEO | variables/geo/VAR-subnatid4.md | draft | 0.1 |
| VAR-subnatid4prev | Subnational ID previous - lowest level | MOD-GEO | variables/geo/VAR-subnatid4prev.md | draft | 0.2 |
| VAR-subnatidsurvey | Lowest level of Subnational ID | MOD-GEO | variables/geo/VAR-subnatidsurvey.md | draft | 0.1 |
| VAR-geocode | Resolved geography crosswalk code | MOD-GEO | variables/geo/VAR-geocode.md | draft | 0.1 |
| VAR-gauladm1code | GAUL code - first administrative level | MOD-GEO | variables/geo/VAR-gauladm1code.md | draft | 0.2 |
| VAR-gauladm2code | GAUL code - second administrative level | MOD-GEO | variables/geo/VAR-gauladm2code.md | draft | 0.2 |
| VAR-psu | Primary sampling unit | MOD-GEO | variables/geo/VAR-psu.md | draft | 0.1 |
| VAR-strata | Strata | MOD-GEO | variables/geo/VAR-strata.md | draft | 0.1 |

## Decision rules

| Rule ID | Rule name | Scope | Module | File | Status | Version |
|---|---|---|---|---|---|---|
| RULE-SEX-001 | Binary sex mapping and exclusion of non-standard codes | module | MOD-DEM | rules/module/dem/RULE-SEX-001.md | draft | 0.1 |
| RULE-EDU-001 | Age restriction for categorical education variables | module | MOD-DEM | rules/module/dem/RULE-EDU-001.md | draft | 0.1 |
| RULE-EDU-002 | educat4 derivation order and recode | module | MOD-DEM | rules/module/dem/RULE-EDU-002.md | draft | 0.1 |
| RULE-EDU-003 | educy construction: individual-level path selection via grade arithmetic and country education-level crosswalk | module | MOD-DEM | rules/module/dem/RULE-EDU-003.md | draft | 0.2 |

## Parameter definitions

| Parameter ID | Parameter name | Module | File | Status | Version |
|---|---|---|---|---|---|
| PARAM-DEM-MIN-MARRIAGE-AGE | Minimum legal marriage age | MOD-DEM | parameters/PARAM-DEM-MIN-MARRIAGE-AGE.md | draft | 0.1 |
| PARAM-EDU-LEVEL-CROSSWALK | Country education crosswalk rows, with derived years-of-schooling | MOD-EDU | parameters/PARAM-EDU-LEVEL-CROSSWALK.md | draft | 0.3 |
| PARAM-WASH-WATER-CROSSWALK | Country water source crosswalk rows | MOD-DWL | parameters/PARAM-WASH-WATER-CROSSWALK.md | draft | 0.2 |
| PARAM-WASH-SANITATION-CROSSWALK | Country sanitation source crosswalk rows | MOD-DWL | parameters/PARAM-WASH-SANITATION-CROSSWALK.md | draft | 0.2 |
| PARAM-GEO-GMD-CROSSWALK | Country geography crosswalk rows | MOD-GEO | parameters/PARAM-GEO-GMD-CROSSWALK.md | draft | 0.4 |
| PARAM-LBR-MIN-WORKING-AGE | Minimum legal working age | MOD-LBR | parameters/PARAM-LBR-MIN-WORKING-AGE.md | draft | 0.1 |

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
