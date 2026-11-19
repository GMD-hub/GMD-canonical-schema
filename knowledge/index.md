# CVS Artifact Index

This file is the master registry of all artifacts in the knowledge base.
Every artifact must be listed here. The index is the agent's entry point
to the knowledge base.

Last updated: 2026-11-18
Schema version: 0.2

## Variable specifications

| Variable ID | Canonical label | Module | File | Status | Version |
|---|---|---|---|---|---|
| VAR-male | Sex of household member | MOD-DEM | variables/dem/VAR-male.md | draft | 0.1 |
| VAR-educat4 | Highest education level completed, 4 categories | MOD-DEM | variables/dem/VAR-educat4.md | draft | 0.1 |
| VAR-educy | Years of education completed | MOD-DEM | variables/dem/VAR-educy.md | draft | 0.1 |
| VAR-subnatid1 | Subnational ID - highest level | MOD-GEO | variables/geo/VAR-subnatid1.md | draft | 0.1 |
| VAR-subnatid1prev | Subnational ID previous - highest level | MOD-GEO | variables/geo/VAR-subnatid1prev.md | draft | 0.1 |
| VAR-subnatid2 | Subnational ID - second highest level | MOD-GEO | variables/geo/VAR-subnatid2.md | draft | 0.1 |
| VAR-subnatid2prev | Subnational ID previous - second highest level | MOD-GEO | variables/geo/VAR-subnatid2prev.md | draft | 0.1 |
| VAR-subnatid3 | Subnational ID - third highest level | MOD-GEO | variables/geo/VAR-subnatid3.md | draft | 0.1 |
| VAR-subnatid3prev | Subnational ID previous - third highest level | MOD-GEO | variables/geo/VAR-subnatid3prev.md | draft | 0.1 |
| VAR-subnatid4 | Subnational ID - fourth highest level | MOD-GEO | variables/geo/VAR-subnatid4.md | draft | 0.1 |
| VAR-subnatid4prev | Subnational ID previous - lowest level | MOD-GEO | variables/geo/VAR-subnatid4prev.md | draft | 0.1 |
| VAR-subnatidsurvey | Lowest level of Subnational ID | MOD-GEO | variables/geo/VAR-subnatidsurvey.md | draft | 0.1 |
| VAR-geocode | Resolved geography crosswalk code | MOD-GEO | variables/geo/VAR-geocode.md | draft | 0.1 |
| VAR-gauladm1code | GAUL code - first administrative level | MOD-GEO | variables/geo/VAR-gauladm1code.md | draft | 0.1 |
| VAR-gauladm2code | GAUL code - second administrative level | MOD-GEO | variables/geo/VAR-gauladm2code.md | draft | 0.1 |
| VAR-psu | Primary sampling unit | MOD-GEO | variables/geo/VAR-psu.md | draft | 0.1 |
| VAR-strata | Strata | MOD-GEO | variables/geo/VAR-strata.md | draft | 0.1 |
| VAR-welfare | Welfare aggregate for poverty measurement | MOD-WLF | variables/wlf/VAR-welfare.md | draft | 0.1 |

## Decision rules

| Rule ID | Rule name | Scope | Module | File | Status | Version |
|---|---|---|---|---|---|---|
| RULE-SEX-001 | Binary sex mapping and exclusion of non-standard codes | module | MOD-DEM | rules/module/dem/RULE-SEX-001.md | draft | 0.1 |
| RULE-EDU-001 | Age restriction for categorical education variables | module | MOD-DEM | rules/module/dem/RULE-EDU-001.md | draft | 0.1 |
| RULE-EDU-002 | educat4 derivation order and recode | module | MOD-DEM | rules/module/dem/RULE-EDU-002.md | draft | 0.1 |
| RULE-EDU-003 | educy construction: individual-level path selection via grade arithmetic and country education-level crosswalk | module | MOD-DEM | rules/module/dem/RULE-EDU-003.md | draft | 0.1 |
| RULE-WASH-001 | WASH ladder: source categories placed through the national crosswalk; improved status derived from the fine code, or set directly for problematic categories | module | MOD-UTL | rules/module/utl/RULE-WASH-001.md | draft | 0.1 |

## Parameter definitions

| Parameter ID | Parameter name | Module | File | Status | Version |
|---|---|---|---|---|---|
| PARAM-DEM-MIN-MARRIAGE-AGE | Minimum legal marriage age | MOD-DEM | parameters/PARAM-DEM-MIN-MARRIAGE-AGE.md | draft | 0.1 |
| PARAM-EDU-LEVEL-CROSSWALK | Country education crosswalk rows, with derived years-of-schooling | MOD-EDU | parameters/PARAM-EDU-LEVEL-CROSSWALK.md | draft | 0.1 |
| PARAM-WASH-WATER-CROSSWALK | Country water source crosswalk rows | MOD-DWL | parameters/PARAM-WASH-WATER-CROSSWALK.md | draft | 0.1 |
| PARAM-WASH-SANITATION-CROSSWALK | Country sanitation source crosswalk rows | MOD-DWL | parameters/PARAM-WASH-SANITATION-CROSSWALK.md | draft | 0.1 |
| PARAM-GEO-GMD-CROSSWALK | Country geography crosswalk rows | MOD-GEO | parameters/PARAM-GEO-GMD-CROSSWALK.md | draft | 0.1 |
| PARAM-LBR-MIN-WORKING-AGE | Minimum legal working age | MOD-LBR | parameters/PARAM-LBR-MIN-WORKING-AGE.md | draft | 0.1 |
| PARAM-LBR-MIN-LABOR-AGE | Minimum age for the labor module (7-day reference period) | MOD-LBR | parameters/PARAM-LBR-MIN-LABOR-AGE.md | draft | 0.1 |
| PARAM-LBR-MIN-LABOR-AGE-YEAR | Minimum age for the labor module (12-month reference period) | MOD-LBR | parameters/PARAM-LBR-MIN-LABOR-AGE-YEAR.md | draft | 0.1 |
| PARAM-EDU-MIN-EDUCATION-AGE | Minimum age for the education module | MOD-DEM | parameters/PARAM-EDU-MIN-EDUCATION-AGE.md | draft | 0.1 |
| PARAM-MAX-MISSING-SHARE | Maximum share of missing values in a harmonized variable | MOD-DWL | parameters/PARAM-MAX-MISSING-SHARE.md | draft | 0.1 |

## Missing value definitions

| Missing ID | Canonical label | Level | Scope | File | Status | Version |
|---|---|---|---|---|---|---|
| MISS-NOT-HARMONIZED | Variable had not been harmonized | column | global | missing/MISS-NOT-HARMONIZED.md | draft | 0.1 |
| MISS-CANNOT-HARMONIZE | Variable cannot be harmonized because data does not meet harmonization definition | column | global | missing/MISS-CANNOT-HARMONIZE.md | draft | 0.1 |
| MISS-NOT-AVAILABLE | Variable was not harmonized because information is not available | column | global | missing/MISS-NOT-AVAILABLE.md | draft | 0.1 |
| MISS-MISSING-INPUT | Input variable was missing | cell | global | missing/MISS-MISSING-INPUT.md | draft | 0.1 |
| MISS-OUTSIDE-UNIVERSE | Outside of universe/not applicable | cell | global | missing/MISS-OUTSIDE-UNIVERSE.md | draft | 0.1 |
| MISS-DECLINED-TO-ANSWER | Decline to answer | cell | global | missing/MISS-DECLINED-TO-ANSWER.md | draft | 0.1 |
| MISS-DO-NOT-KNOW | Do not know | cell | global | missing/MISS-DO-NOT-KNOW.md | draft | 0.1 |
| MISS-CENSORED | Censored values | cell | global | missing/MISS-CENSORED.md | draft | 0.1 |
| MISS-OTHER-CATEGORY | Other category not covered in the harmonized categories | cell | variable | missing/MISS-OTHER-CATEGORY.md | draft | 0.1 |

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
