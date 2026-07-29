# CVS Knowledge Base Change Log

## v0.1 - 2026-07-29

Repository governance and structural validation strengthened without changing
canonical rule logic, derivation relationships, fallback policies, or country
values.

**Added:**
- Pull request and push validation workflow with governance report artifacts
- CODEOWNERS placeholder for GPID Team review of governed paths
- Strict Pydantic models for variable and rule front matter
- Exception identity, window, and informational overlap checks
- Effective-dating, scope, overlap, exception, and bundle integrity tests
- `governance/audits/Gap-Audit-2026-07.md` and
  `governance/decisions/Open-Decisions.md`

**Changed:**
- Coverage reports now show the optional country focal point
- Operational documentation now distinguishes narrative background from the
  continuously maintained wiki
- The wiki now points to the independent governance record area by repository
  path rather than treating audits and decisions as official wiki pages

Authority: GPID Team
Status: draft

## v0.1 - 2026-07-28

Country Parameter Layer added as a draft governed extension to the universal
CVS.

**Added:**
- Universal parameter registry with construction and validation examples
- Country folders for 12 ISO3 codes, with an illustrative unverified PER example
- Strict Pydantic models, structural validation, and coverage reports
- Runtime JSON bundle compiler with source Markdown bodies and commit hash

**Changed:**
- Replaced variable lookup routing fields with `country_parameters`
- Moved country exceptions out of `knowledge/` into the country layer
- Defined survey ID year as the calendar year in which fieldwork began

Authority: GPID Team
Status: draft

## v0.1 - 2026-06-25

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
- Country parameter coverage and fallback policies remain incomplete
- Pydantic validation models not yet written (schema/ folder)
- Extraction pipeline agents not yet written (extraction/agents/ folder)
