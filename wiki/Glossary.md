# Glossary

| Term | Meaning |
|---|---|
| Artifact | One governed Markdown record representing a variable, rule, parameter, module, rubric, or exception. |
| Canonical Variable Schema (CVS) | The governed representation of GMD harmonization rules maintained by this repository. |
| Country exception | Effective-dated country-specific conditional behavior that cannot be represented as a parameter value. |
| Country Parameter Layer | The `country-parameters/` hierarchy containing governed country values and exceptions. |
| Derivation graph | The directed relationships recorded by `derived_from` and `derives_to`. |
| Effective canon | The universal CVS combined with country records selected for one ISO3 code and survey ID year. |
| Fallback policy | Universal instruction controlling what happens when a required country parameter record is absent. |
| Front matter | YAML between `---` delimiters at the beginning of an artifact. |
| GPID Team | The human authority responsible for reviewing and approving GMD harmonization knowledge. |
| Harmonization Specification | A downstream proposal describing how one survey should map to the GMD standard. |
| Mapping role | Whether a canonical variable is mapped directly, derived, or preferably derived with an allowed fallback. |
| Parameter definition | Universal record defining a country-dependent value's meaning, type, shape, scope, and fallback. |
| Provenance | Evidence describing where a claim or value came from and whether a human reviewed it. |
| Runtime bundle | Generated JSON containing universal artifacts and one selected country layer. |
| Survey ID year | Calendar year in which survey fieldwork began; used to select country records. |
| Survey Profile | Upstream schema describing variables and evidence available in a raw survey. |
| Universal CVS | Country-neutral structure and rules stored under `knowledge/`. |
| Validity window | Inclusive `effective_from` and `effective_to` years; null means open ended. |

## Artifact prefixes

| Prefix | Artifact |
|---|---|
| `VAR-` | Variable specification |
| `RULE-` | Decision rule |
| `MOD-` | Module specification |
| `PARAM-` | Parameter definition |
| `CTY-` | Country layer identity |
| `EXC-` | Exception |

## Related documents

- [Wiki Index](Index.md) organizes all documentation by task.
- [Home](Home.md) introduces the project concepts summarized here.
- [Artifact Model](Artifact-Model.md) gives detailed field and ID definitions.

## All wiki pages

[Index](Index.md) | [Home](Home.md) | [Architecture](Architecture.md) | [Repository Map](Repository-Map.md) | [Artifact Model](Artifact-Model.md) | [Artifact Lifecycle](Artifact-Lifecycle.md) | [Country Parameter Layer](Country-Parameter-Layer.md) | [Validation and Builds](Validation-and-Builds.md) | [Governance and Contributing](Governance-and-Contributing.md) | [Glossary](Glossary.md)
