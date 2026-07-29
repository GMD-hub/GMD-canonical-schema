# Repository Map

## Top-level ownership

| Path | Owns | Reads from | Produces or supports |
|---|---|---|---|
| `AGENTS.md` | Agent operating rules and write boundaries | Project governance | Safe agent behavior |
| `README.md` | Project entry point | All major subsystems | Onboarding and navigation |
| `knowledge/` | Universal CVS artifacts | Approved extraction outputs | Universal half of the effective canon |
| `country-parameters/` | Effective-dated country values and exceptions | Universal parameter and variable IDs | Country half of the effective canon |
| `schema/` | Pydantic models and front-matter parsing | Artifact field contracts | Validation used by scripts |
| `validation/` | Repository-wide country-layer checks and reports | `knowledge/`, `country-parameters/`, `schema/` | Structural failures and governance reports |
| `build/` | Runtime bundle compiler | Universal and country layers plus `schema/` | `build/output/bundle_<ISO3>_<year>.json` |
| `extraction/` | Governed staging workflow | Guidelines and contextual sources | Candidate CVS artifacts for human approval |
| `docs/` | Explanatory guides and worked examples | Current CVS design | Human-readable background |
| `wiki/` | Complete project operating documentation | Current repository behavior | Architecture, workflows, and navigation |
| `requirements.txt` | Python dependencies | None | Pydantic 2 and PyYAML environment |

## `knowledge/`

| Path | Contents |
|---|---|
| `knowledge/index.md` | Master registry of all canonical artifacts and the first navigation stop |
| `knowledge/variables/<module>/` | One variable specification per file |
| `knowledge/rules/global/` | Rules that apply across modules |
| `knowledge/rules/module/<module>/` | Reusable module-scoped decision rules |
| `knowledge/parameters/` | Universal parameter definitions, value schemas, and fallback policies |
| `knowledge/modules/` | Module specifications; currently empty |
| `knowledge/rubrics/` | Evaluation rubrics; currently empty |
| `knowledge/exceptions/variable/` | Universal variable exceptions; currently empty |
| `knowledge/log.md` | Knowledge-base log |

The directory tree can contain placeholders for future artifact types. The
index, not directory existence, determines the current registered inventory.

## `country-parameters/`

Every `countries/<ISO3>/` folder contains exactly two governed Markdown files:

| File | Contents |
|---|---|
| `parameters.md` | Values for registered parameter IDs, each with validity and provenance |
| `exceptions.md` | Conditional country logic scoped to registered variable IDs |

The folder name, file `iso3`, and `country_id` must agree. ISO3 codes use
three uppercase letters and `country_id` is `CTY-<ISO3>`.

## `schema/`, `validation/`, and `build/`

`schema/frontmatter.py` splits each artifact into a YAML mapping and Markdown
body. Parameter and country files have strict Pydantic models with unknown
fields forbidden. The current compiler treats non-parameter universal
artifacts as generic mappings; their full field contracts are documented in
the artifacts but are not yet represented by dedicated Pydantic models.

`validation/validate_country_layer.py` validates all registered parameter
definitions and country files, checks references and overlapping parameter
windows, detects ISO3 values leaked into universal front matter, and prints
governance reports.

`build/compile_bundle.py` validates the same modeled inputs for one requested
country, filters records by year when supplied, and combines them with every
universal Markdown artifact in the recognized folders.

## `extraction/`

| Stage | Role | Writer |
|---|---|---|
| `00_context/` | Supporting context needed to interpret the source | Governed project process |
| `10_source/` | Source material or scoped source extracts | Governed project process |
| `20_drafts/` | Agent-generated candidate artifacts | AI agents |
| `30_review/` | Human review notes and decisions | Humans only |
| `40_approved/` | Artifacts approved for promotion | Humans only |
| `agents/` | Extraction workflow support | Governed project process |

Approval staging does not itself make an artifact canonical. Human promotion
into `knowledge/` or `country-parameters/`, plus index maintenance where
applicable, completes the lifecycle.

## Related documents

- [Architecture and Data Flow](Architecture.md) explains how these folders interact.
- [Artifact Lifecycle](Artifact-Lifecycle.md) follows content across the folders.
- [Validation and Runtime Bundles](Validation-and-Builds.md) documents the scripts.

## All wiki pages

[Index](Index.md) | [Home](Home.md) | [Architecture](Architecture.md) | [Repository Map](Repository-Map.md) | [Artifact Model](Artifact-Model.md) | [Artifact Lifecycle](Artifact-Lifecycle.md) | [Country Parameter Layer](Country-Parameter-Layer.md) | [Validation and Builds](Validation-and-Builds.md) | [Governance and Contributing](Governance-and-Contributing.md) | [Glossary](Glossary.md)
