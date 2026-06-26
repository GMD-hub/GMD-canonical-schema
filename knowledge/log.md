# CVS Knowledge Base Change Log

## v0.1 — 2026-06-25

Initial schema design and three example records seeded.

**Added:**
- Schema templates: variable spec and rule (YAML front matter + Markdown body)
- VAR-male + RULE-SEX-001: atomic binary variable, baseline format
- VAR-educat4 + RULE-EDU-001 + RULE-EDU-002: derived_preferred variable with
  shared age restriction rule and three-path derivation rule
- VAR-educy + RULE-EDU-003: continuous variable with country lookup table
  dependency and multi-path construction rule

**Design decisions recorded in:** session_summary_CVS_schema_design.md
(add to project sources for context in future sessions)

**Open items:**
- Tier vs basic flag distinction for education categorical variables
- Country lookup table education_years_by_country_v1 does not yet exist
- Pydantic validation models not yet written (schema/ folder)
- Extraction pipeline agents not yet written (extraction/agents/ folder)
