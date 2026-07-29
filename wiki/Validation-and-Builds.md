# Validation and Runtime Bundles

## Environment

Create an isolated Python environment from the repository root:

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

The project currently depends on Pydantic 2 and PyYAML 6.

## Validate the country layer

```sh
python3 validation/validate_country_layer.py
```

The command loads the universal parameter registry, variable IDs, and every
country folder. It checks:

- parameter definition schemas and duplicate parameter IDs;
- variable references to known parameters;
- country file identity and strict field schemas;
- country values against registered integer or mapping shapes;
- country exceptions against known variable IDs and ID naming rules;
- invalid or overlapping parameter validity windows;
- country ISO3 values leaked into universal YAML front matter.

It also prints three governance reports:

| Report | Meaning |
|---|---|
| Undecided fallback | Parameter definitions that do not yet define behavior when coverage is absent |
| Coverage gap | Countries with no record for each registered parameter |
| Unverified values | Country records whose provenance is not human reviewed |

These reports can contain rows while validation exits successfully. The
script exits with status 1 when the `Structural failures` section is nonempty.

!!! example "Structural failure versus governance report"
  A country record whose mapping omits the required `primary` key is a
  structural failure: software cannot trust its shape, so validation exits
  unsuccessfully. A well-shaped record with `human_reviewed: false` appears
  in the unverified-values report: the structure is usable for review, but
  the value is not approved evidence. A zero exit code never upgrades its
  governance status.

## Compile a runtime bundle

```sh
python3 build/compile_bundle.py PER 2019
```

Arguments are an uppercase three-letter ISO3 code and an optional integer
survey ID year. With a year, the compiler includes only records valid for that
year. Without a year, it includes all country records and retains their
windows:

```sh
python3 build/compile_bundle.py PER
```

Output names follow:

```text
build/output/bundle_<ISO3>_<year-or-all>.json
```

!!! example "Hypothetical boundary-year selection"
  Assume one parameter record ends in 1999 and its non-overlapping successor
  begins in 2000. Compiling for survey year 1999 selects the first; compiling
  for 2000 selects the second. Compiling without a year retains both records
  and their windows so a downstream consumer can see the complete layer.

## Bundle contents

Each bundle contains:

```text
bundle_version
generated_on
commit_hash
country_code
survey_id_year
universal
  modules
  variables
  rules
  parameters
country
  iso3
  parameters
  exceptions
```

Every artifact includes its structured front matter plus a `body` field with
the Markdown content. `commit_hash` is the current `HEAD`, allowing downstream
outputs to identify the exact repository snapshot used.

Generated JSON is a runtime derivative. Do not hand edit it or treat it as the
source for future canonical changes.

For example, correcting a typo directly in
`build/output/bundle_PER_2019.json` would be lost on the next compilation and
would break traceability. Correct the governed Markdown through its required
review path, then regenerate the bundle.

## What is validated today

Parameter definitions and country files have dedicated strict Pydantic models.
The compiler also verifies variable-to-parameter references and country
exception variable references. Other universal variables, rules, and modules
are currently loaded as generic YAML mappings rather than validated against
dedicated artifact models. A successful bundle therefore proves that the
implemented structural checks pass; it does not prove semantic correctness or
human approval of every artifact.

## Interpreting failures

Common failures include lowercase or unknown ISO3 folders, malformed front
matter, unknown parameter or variable IDs, mapping values with missing or
extra keys, reversed or overlapping validity windows, and mismatched country
identity fields. Fix source Markdown and regenerate; never patch the JSON.

After any canonical change, run the repository validator and compile at least
one representative bundle for each affected country and boundary year.

## Suggested reading

- **To locate every input and output:** revisit the
  [Repository Map](Repository-Map.md).
- **To understand the selection algorithm being tested:** read the
  [Country Parameter Layer](Country-Parameter-Layer.md).
- **To interpret technical success within the approval process:** continue to
  [Governance and Contributing](Governance-and-Contributing.md).
