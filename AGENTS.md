# AGENTS.md - Operating Rules for AI Agents

Read this file completely before reading anything else in this repository.

## What this repository is

This is the Canonical Variable Schema (CVS) for the GMD AI-Assisted
Harmonization project. It contains the authoritative rules for how each GMD
variable must be harmonized. It is a knowledge base, not a workflow. Rules
here are stable and change slowly. Do not modify approved artifacts without
explicit human instruction from the GPID Team.

## Before doing anything

1. Read this file completely.
2. Read `knowledge/index.md` to understand what artifacts exist and where.
3. Read the relevant variable spec and any rules it references before drafting
   any harmonization output.
4. Read `country-parameters/README.md` before using country-specific content.

## Where agents are allowed to write

| Location | What goes here | Who writes |
|---|---|---|
| `extraction/20_drafts/` | Draft CVS artifacts generated from guidelines | Agent |
| `extraction/30_review/` | Human review notes and decisions | Human only |
| `extraction/40_approved/` | Artifacts approved for promotion | Human only |
| `knowledge/` | Approved, finalized CVS artifacts | Human only |
| `country-parameters/` | Country parameter values and exceptions | Human only |
| `schema/` | Pydantic validation models | Human or agent under supervision |

Agents write only to `extraction/20_drafts/`.
Never write directly to `knowledge/`.

## What always requires human approval

- Any new or modified file in `knowledge/`
- Any change to a rule's IF/THEN logic
- Any change to `derived_from` or `derives_to` in a variable spec
- Any addition to the `country-parameters/` folder
- Any change to this file (AGENTS.md)

## What agents must never do

- Write directly to `knowledge/`. Use `extraction/20_drafts/` instead.
- Invent harmonization rules not grounded in the GMD guidelines source document.
- Guestimate field values. If a field cannot be determined from the source,
  set it to `null` and explain what is missing in `provenance.notes`.
- Change the `status` field of any artifact from `active` to anything else.
- Skip the staging folders. Every draft must pass through `20_drafts/` and
  `30_review/` before being promoted to `knowledge/`.
- Include country-specific information in any file under `knowledge/`. The
  CVS is universal. Country content belongs in `country-parameters/`.
- Combine content from multiple variables into a single file.

## Source of truth

The authoritative source for all rules in this repository is:
GMD_household_survey_harmonization.md (GMD-hub/GMD-guidelines, main branch)

When a CVS artifact conflicts with the source document, the source document
wins. Document the conflict in `provenance.notes` and escalate to GPID Team.

## Naming conventions

| Artifact | ID format | Example |
|---|---|---|
| Variable | VAR- + lowercase Stata name | VAR-male, VAR-educat7 |
| Rule | RULE- + UPPERCASE-SEQ | RULE-SEX-001, RULE-EDU-002 |
| Module | MOD- + UPPERCASE | MOD-DEM, MOD-EDU |
| Exception | EXC- + descriptive | EXC-PILOT-VAR-URBAN-001 |
| Parameter | PARAM- + UPPERCASE module + descriptive | PARAM-EDU-YEARS-BY-LEVEL |
| Country layer | CTY- + ISO 3166-1 alpha-3 | CTY-PER |
| Country exception | EXC- + ISO3 + sequence | EXC-PER-001 |

Country codes use ISO 3166-1 alpha-3 in uppercase.

## The Country Parameter Layer

1. Before drafting any harmonization output, the agent must load
  `country-parameters/countries/<ISO3>/parameters.md` and
  `country-parameters/countries/<ISO3>/exceptions.md` for the survey's
  country, and select every record whose validity window contains the survey
  ID year. The survey ID year is the calendar year in which fieldwork began.
  This step is mandatory for every run and every variable.
2. The effective canon is the union of the universal CVS and the selected
  country records. Country records win over global defaults. The universal
  CVS always wins on structure.
3. If a variable declares a parameter in `country_parameters` and no valid
  country record exists, apply the parameter's `fallback_policy` from the
  registry. If the policy is `undecided`, stop and escalate. Never improvise
  a value.
4. Every parameter value used, its validity window, and its source (country
  record, global default, or fallback) must be recorded in the Harmonization
  Specification draft, together with the commit hash of the schema version
  used.
5. Country layers may contain only parameter records and exceptions. Agents
  must never write country-specific content into `knowledge/`, and never
  write structural overrides into a country layer.
