# CVS Artifact Index

This file is the master registry of all artifacts in the knowledge base.
Every artifact must be listed here. The index is the agent's entry point
to the knowledge base.

Last updated: 2026-09-01
Schema version: 0.0.1

## Variable specifications

| Variable ID | Canonical label | Module | File | Status | Version |
|---|---|---|---|---|---|
| VAR-male | Sex of household member | MOD-DEM | variables/dem/VAR-male.md | draft | 0.1 |
| VAR-educat4 | Highest education level completed, 4 categories | MOD-DEM | variables/dem/VAR-educat4.md | draft | 0.1 |
| VAR-educy | Years of education completed | MOD-DEM | variables/dem/VAR-educy.md | draft | 0.1 |
| VAR-welfare | Household welfare aggregate (consumption) | MOD-WLF | variables/wlf/VAR-welfare.md | draft | 0.1 |
| VAR-consfood | Household food consumption component | MOD-WLF | variables/wlf/VAR-consfood.md | draft | 0.1 |
| VAR-consalcoholtobacco | Household alcohol and tobacco consumption component | MOD-WLF | variables/wlf/VAR-consalcoholtobacco.md | draft | 0.1 |
| VAR-consclothing | Household clothing and footwear consumption component | MOD-WLF | variables/wlf/VAR-consclothing.md | draft | 0.1 |
| VAR-conshousing | Household housing services consumption component | MOD-WLF | variables/wlf/VAR-conshousing.md | draft | 0.1 |
| VAR-consfurnishings | Household furnishings and household-equipment consumption component | MOD-WLF | variables/wlf/VAR-consfurnishings.md | draft | 0.1 |
| VAR-conshealth | Household health expenditure component | MOD-WLF | variables/wlf/VAR-conshealth.md | draft | 0.1 |
| VAR-constransport | Household transport consumption component | MOD-WLF | variables/wlf/VAR-constransport.md | draft | 0.1 |
| VAR-conscommunications | Household communications and information services consumption component | MOD-WLF | variables/wlf/VAR-conscommunications.md | draft | 0.1 |
| VAR-consrecreation | Household recreation and culture consumption component | MOD-WLF | variables/wlf/VAR-consrecreation.md | draft | 0.1 |
| VAR-conseducation | Household education expenditure component | MOD-WLF | variables/wlf/VAR-conseducation.md | draft | 0.1 |
| VAR-conshotelsrestaurants | Household hotels and restaurants consumption component | MOD-WLF | variables/wlf/VAR-conshotelsrestaurants.md | draft | 0.1 |
| VAR-consmiscellaneous | Household miscellaneous goods and services consumption component | MOD-WLF | variables/wlf/VAR-consmiscellaneous.md | draft | 0.1 |
| VAR-consdurables | Household durables consumption component | MOD-WLF | variables/wlf/VAR-consdurables.md | draft | 0.1 |

## Decision rules

| Rule ID | Rule name | Scope | Module | File | Status | Version |
|---|---|---|---|---|---|---|
| RULE-SEX-001 | Binary sex mapping and exclusion of non-standard codes | module | MOD-DEM | rules/module/dem/RULE-SEX-001.md | draft | 0.1 |
| RULE-EDU-001 | Age restriction for categorical education variables | module | MOD-DEM | rules/module/dem/RULE-EDU-001.md | draft | 0.1 |
| RULE-EDU-002 | educat4 derivation order and recode | module | MOD-DEM | rules/module/dem/RULE-EDU-002.md | draft | 0.1 |
| RULE-EDU-003 | educy construction: path selection, enrollment adjustment, tertiary assumptions | module | MOD-DEM | rules/module/dem/RULE-EDU-003.md | draft | 0.1 |
| RULE-WLF-001 | Methodological switch resolution and escalation gate | module | MOD-WLF | rules/module/wlf/RULE-WLF-001.md | draft | 0.1 |
| RULE-WLF-002 | Unit-value hierarchical cascade for pricing own-produced and in-kind food | module | MOD-WLF | rules/module/wlf/RULE-WLF-002.md | draft | 0.1 |
| RULE-WLF-003 | Food-ration re-pricing: preference ladder and official-price prohibition | module | MOD-WLF | rules/module/wlf/RULE-WLF-003.md | draft | 0.1 |
| RULE-WLF-004 | Reference period: short-recall preference and usual-month deprecation | module | MOD-WLF | rules/module/wlf/RULE-WLF-004.md | draft | 0.1 |
| RULE-WLF-005 | Zero-vs-missing distinction and item-nonresponse procedure | module | MOD-WLF | rules/module/wlf/RULE-WLF-005.md | draft | 0.1 |
| RULE-WLF-006 | Acquisition-as-proxy acceptance and bulk-purchase scrutiny | module | MOD-WLF | rules/module/wlf/RULE-WLF-006.md | draft | 0.1 |
| RULE-WLF-007 | Outlier detection, treatment, and mandatory sensitivity analysis | module | MOD-WLF | rules/module/wlf/RULE-WLF-007.md | draft | 0.1 |

## Parameter definitions

| Parameter ID | Parameter name | Module | File | Status | Version |
|---|---|---|---|---|---|
| PARAM-EDU-YEARS-BY-LEVEL | Duration in years of each education level | MOD-DEM | parameters/PARAM-EDU-YEARS-BY-LEVEL.md | draft | 0.1 |
| PARAM-DEM-MIN-MARRIAGE-AGE | Minimum legal marriage age | MOD-DEM | parameters/PARAM-DEM-MIN-MARRIAGE-AGE.md | draft | 0.1 |
| PARAM-WLF-EQUIVALENCE-SCALE | Adult-equivalence scale constants (alpha, theta) | MOD-WLF | parameters/PARAM-WLF-EQUIVALENCE-SCALE.md | draft | 0.1 |

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
