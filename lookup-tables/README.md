# Lookup Tables

This folder contains country-specific parameter tables referenced by CVS
variable records. These tables are NOT part of the Canonical Variable Schema
itself. The CVS records reference them by ID only. The tables live here.

Country-specific content must never appear inside `knowledge/`. If a variable
requires a lookup table, the CVS record states `requires_country_lookup: true`
and names the table in `country_lookup_table`. The actual table is here.

## Tables and their status

### education_years_by_country_v1

Referenced by: VAR-educy (via RULE-EDU-003)
Status: DOES NOT EXIST YET
Responsible workstream: GPID Team (separate from CVS schema work)

This table must contain, for each country:
- Country code (ISO 3166-1 alpha-3)
- Duration of primary education in years
- Duration of lower secondary education in years
- Duration of upper secondary education in years
- Source (UNESCO ISCED mapping, national curriculum document, or other)
- Year the data was verified

Until this table exists, educy cannot be reliably harmonized via the derived
path (path 3 in RULE-EDU-003). Path 1 (direct years from survey) and path 2
(grade level from survey) are not affected.

The UNESCO ISCED country mappings are available at:
http://uis.unesco.org/en/isced-mappings

### urban-rural/

Reserved for future country-specific urban/rural classification tables.
No table exists yet.
