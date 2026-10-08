# Runtime JSON bundles

Markdown with YAML front matter is the authoring and governance format for the
universal CVS and Country Parameter Layer. Humans author, review, and approve
Markdown files. JSON is generated for machine consumption only and is never
hand edited.

Run the compiler with an uppercase ISO3 code and an optional survey ID year:

```sh
python build/compile_bundle.py PER 2019
```

Optional selectors can be supplied to disambiguate country records when
multiple records are valid for the same year but scoped to different survey
contexts:

```sh
python build/compile_bundle.py PER 2019 --selector survey_type=income --selector rural_only=true
```

When a year is supplied, only country records whose inclusive validity window
contains that year are included. When omitted, all records and their windows
are included and the output filename uses `all`.

When selectors are supplied, records are included only if all selector
key-value pairs declared in the record match the active selector context.

Bundles are written under `build/output/`, which is ignored by git. Each
bundle contains the complete universal modules, variables, rules, and parameter
definitions plus the selected country parameter and exception records. The
Markdown body of every included artifact is carried in a `body` field.

Each bundle records `country_code` and also includes the country content under
the `country` object. This avoids the duplicate `country` key that would result
from representing both concepts at the same JSON object level.

The active selector context is stored in the top-level `selectors` object for
traceability.

The `commit_hash` in every bundle links a harmonized survey to the exact schema
version used to produce it. Regenerate a bundle whenever source Markdown or the
selected commit changes.
