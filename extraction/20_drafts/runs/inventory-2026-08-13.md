---
date: 2026-08-14
plan: 2026-08-13-complete-non-welfare-extraction
module: all (IDN, GEO, DEM, LBR, UTL, DWL)
source-commit: d46dc03d253764ad7bdef53f625d54fd2a0a9ea1
---

# Authoritative Non-Welfare Variable Inventory (from chapter summary tables)

Source: GMD-guidelines, chapters 2-7 (chapter 8 CONS excluded - welfare).
Naming rule: GMD snake_case -> CVS `VAR-<underscore-drop>` (one grandfathered exception: `VAR-marital`).

## IDN (chapter2-IDN) - module ID MOD-IDN

| GMD name | variable_id | Label | Type | UOA | Tier | Section | Status |
|----------|-------------|-------|------|-----|------|---------|--------|
| countrycode | VAR-countrycode | Country code | string | survey | 1 | countrycode | missing |
| year | VAR-year | Survey start year | numeric | survey | 1 | year | missing |
| int_year | VAR-intyear | Interview year | numeric | hhold/ind | 1 | int_year | missing |
| int_month | VAR-intmonth | Interview month | numeric 1-12 | household | 1 | int_month | missing |
| hhid_orig | VAR-hhidorig | Household ID in raw data | num/str | household | 1 | hhid_orig | missing |
| hhid | VAR-hhid | Household unique ID | str/num | household | 1 | hhid | missing |
| pid_orig | VAR-pidorig | Personal ID in raw data | num/str | individual | 1 | pid_orig | missing |
| pid | VAR-pid | Personal unique ID | str/num | individual | 1 | pid | missing |
| weight | VAR-weight | Household weights | numeric | household | 1 | Lessons Learned | missing |

mineducatage classification: variable to draft in DEM (country-specific threshold parameter), not a registered PARAM today. Blocking issue recorded.

## GEO (chapter3-GEO) - module MOD-GEO (GEO-module rows only)

| GMD name | variable_id | Label | Type | UOA | Tier | Section | Status |
|----------|-------------|-------|------|-----|------|---------|--------|
| subnatid1 | VAR-subnatid1 | Subnational ID level 1 | string | household | 1 | subnatid1 | missing |
| subnatid2 | VAR-subnatid2 | Subnational ID level 2 | string | household | 1 | subnatid2 | missing |
| subnatid3 | VAR-subnatid3 | Subnational ID level 3 | string | household | 2 | subnatid3 | missing |
| subnatid4 | VAR-subnatid4 | Subnational ID level 4 | string | household | 2 | subnatid4 | missing |
| subnatidsurvey | VAR-subnatidsurvey | Lowest representative level | string | household | 1 | subnatidsurvey | missing |
| strata | VAR-strata | Stratum identifier | string | household | 1 | strata | missing |
| psu | VAR-psu | Primary sampling unit | numeric | household | 1 | psu | missing |
| subnatid1_prev | VAR-subnatid1prev | SUBNATID1 previous | string | household | 2 | subnatid1_prev | missing |
| subnatid2_prev | VAR-subnatid2prev | SUBNATID2 previous | string | household | 2 | subnatid2_prev | missing |
| subnatid3_prev | VAR-subnatid3prev | SUBNATID3 previous | string | household | 2 | subnatid3_prev | missing |
| subnatid4_prev | VAR-subnatid4prev | SUBNATID4 previous | string | household | 2 | subnatid4_prev | missing |
| gaul_adm1_code | VAR-gauladm1code | GAUL admin level 1 | numeric | household | 1 | gaul_adm1_code | missing |
| gaul_adm2_code | VAR-gauladm2code | GAUL admin level 2 | numeric | household | 1 | gaul_adm2_code | missing |
| urban | VAR-urban | Urban/rural (EXISTS - verify module_id MOD-GEO) | binary | household | 1 | urban | done (verify) |

## DEM (chapter4-DEM) - module MOD-DEM

Already drafted/approved: VAR-male (approved), VAR-educat4 (approved), VAR-educy (approved), VAR-educat7 (draft, needs fix), VAR-marital (draft, keep canonical).

Missing (per ownership rule, DEM owns core person demographics; IDN owns identifiers/weights):

| GMD name | variable_id | Label | Type | UOA | Tier | Section | Status |
|----------|-------------|-------|------|-----|------|---------|--------|
| age | VAR-age | Age continuous | numeric | individual | 1 | age | missing |
| agecat | VAR-agecat | Age categorical bands | string | individual | 1 | agecat | missing |
| childyr | VAR-childyr | Child age under 5 (years) | numeric | individual | 1 | childyr | missing |
| childmth | VAR-childmth | Child age under 5 (months) | numeric | individual | 1 | childmth | missing |
| relationcs | VAR-relationcs | Relationship to head country-specific | string | individual | 1 | relationcs | missing |
| relationharm | VAR-relationharm | Relationship to head harmonized | categorical 1-6 | individual | 1 | relationharm | missing |
| literacy | VAR-literacy | Literacy binary | binary | individual | 1 | literacy | missing |
| everattend | VAR-everattend | Ever attended school | binary | individual | 1 | everattend | missing |
| mineducatage | VAR-mineducatage | Education application age | numeric | module/param | 1 | mineducatage | missing |
| primarycomp | VAR-primarycomp | Primary completion | binary | individual | 1 | primarycomp | missing |
| school | VAR-school | Currently enrolled | binary | individual | 1 | school | missing |
| language | VAR-language | Language | string | individual | 2 | language | missing |
| eye_dsablty | VAR-eyedisability | Eye disability | categorical 1-4 | individual | 1 | eye_dsablty | missing |
| hear_dsablty | VAR-heardisability | Hearing disability | categorical 1-4 | individual | 1 | hear_dsablty | missing |
| walk_dsablty | VAR-walkdisability | Walking disability | categorical 1-4 | individual | 1 | walk_dsablty | missing |
| conc_dsord | VAR-concentrationdisorder | Concentration disorder | categorical 1-4 | individual | 1 | conc_dsord | missing |
| slfcre_dsablty | VAR-selfcaredisability | Self-care disability | categorical 1-4 | individual | 1 | slfcre_dsablty | missing |
| comm_dsablty | VAR-communicationdisability | Communication disability | categorical 1-4 | individual | 1 | comm_dsablty | missing |
| educat5 | VAR-educat5 | Education 5 categories | categorical | individual | 1 | educat5 | missing |

NOTE: `relationship_to_head` from skill maps to `relationcs`/`relationharm` in source. `disability_status` maps to 6 domain variables. `marital_status` = `VAR-marital` (grandfathered).

## LBR (chapter5-LMR) - module MOD-LBR (alias resolved)

95 variables (7-day, 12-month, primary/secondary, earnings). Signature list:
lstatus, lstatus_year, nlfreason, nlfreason_year, unempldur_l, unempldur_u, minlaborage, minlaborage_year,
empstat, empstat_2, empstat_year, empstat_2_year, ocusec*, industry_orig*, industrycat10*, industrycat4*,
occup_orig*, occup*, wage_nc*, unitwage*, whours*, wmonths*, wage_total*, contract*, healthins*, socialsec*,
union*, firmsize_l*, firmsize_u* (each with _2, _year, _2_year variants), t_hours_others*, t_wage_nc_others*,
t_wage_others*, t_hours_total*, t_wage_nc_total*, t_wage_total*, njobs, t_hours_annual, linc_nc, laborincome.
All underscore names normalize to VAR-<underscore-drop>.

## UTL (chapter6-UTL) - module MOD-UTL

66 variables (4 ID + 15 WASH access + 9 energy access + 20 WASH/energy expenditure + 12 additional expenditure).
All household. Normalize via underscore-drop.

## DWL (chapter7-DWL) - module MOD-DWL

69 module variables (18 appliances + 6 transport + 6 materials + 7 facilities + 7 ownership + 7 residential land + 18 agri land).
All household. Normalize via underscore-drop.

## Exclusion ledger (chapter 8 CONS - welfare)

chapter8-CONS.qmd excluded entirely. Any chapter-8 reference in drafts is a welfare-leakage finding.
