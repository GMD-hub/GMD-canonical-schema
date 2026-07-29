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

!!! example "Example: finding the source of a bundle value"
	Suppose a generated bundle contains a selected education-duration mapping.
	Start with the bundle metadata in `build/output/`, then follow its country
	code and survey year to `country-parameters/countries/<ISO3>/parameters.md`.
	The record's `parameter_id` leads to its universal contract under
	`knowledge/parameters/`, and the bundle's commit hash identifies the exact
	repository snapshot. The JSON is the end of the trail, not the place to
	edit the value.

## `country-parameters/`

Every `countries/<ISO3>/` folder contains exactly two governed Markdown files:

| File | Contents |
|---|---|
| `parameters.md` | Values for registered parameter IDs, each with validity and provenance |
| `exceptions.md` | Conditional country logic scoped to registered variable IDs |

The folder name, file `iso3`, and `country_id` must agree. ISO3 codes use
three uppercase letters and `country_id` is `CTY-<ISO3>`.

For example, a `COL/` folder must declare `iso3: COL` and
`country_id: CTY-COL` in both files. A mismatch such as `iso3: PER` is a
structural error even if the contained record values happen to validate.

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

!!! example "Hypothetical path: a proposed parameter"
	An agent drafts one parameter definition in `20_drafts/`. A human records
	review findings in `30_review/`; if approved, a human places the candidate
	in `40_approved/` and later promotes it to `knowledge/parameters/` while
	updating `knowledge/index.md`. The compiler ignores all three staging
	folders, so a draft cannot leak into a runtime bundle.

## Suggested reading

- **To understand how these paths exchange information:** read
	[Architecture and Data Flow](Architecture.md).
- **To follow content through the staging folders:** continue to the
	[Artifact Lifecycle](Artifact-Lifecycle.md).
- **To run the scripts described here:** use
	[Validation and Runtime Bundles](Validation-and-Builds.md).
