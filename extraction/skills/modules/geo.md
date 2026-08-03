# Module: GEO — Geography Variables v1

## Source Chapter

`chapter3-GEO.qmd`

## Module Code

`MOD-GEO` (Geography). Not ISO 3166-1 alpha-3 for Georgia.

## Variable Conventions

Geography variables capture spatial identifiers for household location:
urban/rural classification, subnational region, and administrative divisions.

## Expected Variables

- urban (urban/rural classification)
- subnatid1 (first subnational level)
- subnatid2 (second subnational level, where available)

## Common Edge Cases

- Urban/rural definitions differ by country; the harmonized variable uses
  a consistent binary classification
- Subnational identifiers must align with GMD region coding standards
- Some surveys use sample stratum instead of administrative geography

## Source Patterns

The chapter typically contains:
- A summary table of geography variables
- Value code specifications for urban/rural
- Notes on subnational coding conventions
