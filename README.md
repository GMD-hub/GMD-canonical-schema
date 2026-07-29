# GMD Canonical Variable Schema

The GMD Canonical Variable Schema (CVS) is the governed knowledge base for
AI-assisted household survey harmonization. It translates the GMD
harmonization guidelines into versioned records that are readable by people,
validated by software, and consumable by harmonization agents.

The CVS answers one question consistently: **given the evidence available in
a survey, what rules must be followed to construct a specific GMD variable?**
It does not inspect raw surveys, generate final harmonization code, or replace
human approval.

## How the system fits together

The wider harmonization workflow uses three schemas:

| Stage | Schema | Responsibility |
|---|---|---|
| 1 | Survey Profile | Describes variables and evidence found in a raw survey. |
| 2 | Canonical Variable Schema (this repository) | Defines the universal GMD rules and governed country-specific inputs. |
| 3 | Harmonization Specification | Records the proposed mapping for one survey and variable. |

For each harmonization run, this repository supplies an **effective canon**:

```text
effective canon = universal CVS + applicable country records
```

The universal layer defines structure, value codes, derivation relationships,
and decision rules. The country layer supplies parameter values and permitted
exceptions for an ISO3 country code and survey ID year. Country records may be
more specific, but they never override universal structure.

## Repository map

| Path | Purpose |
|---|---|
| `knowledge/` | Universal variable, rule, parameter, module, rubric, and exception artifacts. `knowledge/index.md` is the registry. |
| `country-parameters/` | Country parameter values and exceptions, organized by uppercase ISO3 code. |
| `schema/` | Pydantic models and Markdown front-matter loader used for validation. |
| `validation/` | Cross-repository structural and governance checks. |
| `build/` | Compiler that produces one runtime JSON bundle for a country and optional survey year. |
| `extraction/` | Staging workflow for turning source guidelines into reviewed CVS artifacts. |
| `governance/` | Project audits, open questions, decision records, and implementation traceability. |
| `docs/` | Existing explanatory examples and schema notes. |
| `wiki/` | Detailed project documentation and operating guidance. |
| `AGENTS.md` | Mandatory operating and write-access rules for AI agents. |

Markdown with YAML front matter is the governed source format. Files under
`build/output/` are generated runtime artifacts and must not be hand edited.

## Quick start

Requirements: Python 3.10 or later, Git, and a checkout with an available
`HEAD` commit.

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 validation/validate_country_layer.py
python3 build/compile_bundle.py PER 2019
```

The validator prints reports for undecided fallbacks, country coverage gaps,
unverified values, and structural failures. It exits with status 1 only when
structural failures are found; governance reports can contain open items while
the command still succeeds.

The compiler writes `build/output/bundle_PER_2019.json`. It validates the
universal parameter registry, country records, references, and ISO3 identity;
selects records whose inclusive validity window contains 2019; and embeds the
current Git commit hash. Omit the year to include every country record and its
validity window:

```sh
python3 build/compile_bundle.py PER
```

## Authoring and governance

The authoritative source for CVS rules is
`GMD_household_survey_harmonization.md` in the
`GMD-hub/GMD-guidelines` repository. When a CVS artifact conflicts with that
source, the source wins and the conflict must be escalated to the GPID Team.

New artifacts follow this lifecycle:

```text
source/context -> agent draft -> human review -> approved staging -> knowledge
```

AI agents write drafts to `extraction/20_drafts/`. Humans own review,
approval, and promotion into `knowledge/` and `country-parameters/`. Never
invent a rule or parameter value; use `null` where the source is insufficient
and document the missing evidence in provenance.

Project-level audits and decision records live under `governance/`. They are
review records, not canonical CVS artifacts and not official wiki pages.

Read `AGENTS.md` before making any change. Before a harmonization run, read
`knowledge/index.md`, the relevant variable and rule files, and
`country-parameters/README.md` plus both files for the survey country.

## Documentation

The wiki provides the detailed operating guide:

- [Complete wiki index](wiki/Learning-Paths.md)
- [System overview](wiki/index.md)
- [Architecture and data flow](wiki/Architecture.md)
- [Repository map](wiki/Repository-Map.md)
- [Artifact model](wiki/Artifact-Model.md)
- [Artifact lifecycle](wiki/Artifact-Lifecycle.md)
- [Country parameter layer](wiki/Country-Parameter-Layer.md)
- [Validation and runtime bundles](wiki/Validation-and-Builds.md)
- [Governance and contribution workflow](wiki/Governance-and-Contributing.md)
- [Glossary](wiki/Glossary.md)
- [Governance records](governance/README.md)

The authoritative artifact inventory remains `knowledge/index.md`.
