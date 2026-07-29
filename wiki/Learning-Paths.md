# Wiki Index

<p class="gmd-lede">Choose a complete learning sequence or jump into the task
in front of you. Each guide ends with the most useful next readings.</p>

<div class="grid cards" markdown>

-   :material-school-outline:{ .lg .middle } **I am learning the system**

   ---

   Begin with [Home](index.md), then follow the recommended reading order
   below. This route builds vocabulary before governance and tooling.

-   :material-tools:{ .lg .middle } **I have a task to complete**

   ---

   Use the task table to enter at the owning concept, then follow its
   suggested reading links only as needed.

-   :material-book-search-outline:{ .lg .middle } **I need a quick reference**

   ---

   Open the [Glossary](Glossary.md) for terminology or the
   [Repository Map](Repository-Map.md) for paths and ownership.

</div>

## Recommended reading order

1. [Home](index.md) establishes the objective, scope, current status, and
   sources of truth.
2. [Architecture and Data Flow](Architecture.md) explains the three-schema
   workflow, the universal and country layers, and effective-canon resolution.
3. [Repository Map](Repository-Map.md) shows which folder owns each kind of
   input, validation behavior, and generated output.
4. [Artifact Model](Artifact-Model.md) describes variable, rule, parameter,
   and exception records and their IDs.
5. [Country Parameter Layer](Country-Parameter-Layer.md) explains country
   lookup tables, validity windows, precedence, and fallback behavior.
6. [Artifact Lifecycle](Artifact-Lifecycle.md) covers extraction, drafting,
   human review, approval, and promotion.
7. [Validation and Runtime Bundles](Validation-and-Builds.md) documents setup,
   structural checks, governance reports, and JSON compilation.
8. [Governance and Contributing](Governance-and-Contributing.md) defines write
   ownership, approval requirements, and review expectations.
9. [Glossary](Glossary.md) provides a quick reference for project terminology
   and artifact prefixes.

## Find documentation by task

| I need to... | Start with | Then read |
|---|---|---|
| Understand the project's purpose | [Home](index.md) | [Architecture](Architecture.md) |
| Understand how the folders connect | [Repository Map](Repository-Map.md) | [Artifact Lifecycle](Artifact-Lifecycle.md) |
| Understand the universal GMD schema | [Artifact Model](Artifact-Model.md) | [Architecture](Architecture.md) |
| Resolve country-specific lookup values | [Country Parameter Layer](Country-Parameter-Layer.md) | [Artifact Model](Artifact-Model.md) |
| Add or revise a canonical artifact | [Artifact Lifecycle](Artifact-Lifecycle.md) | [Governance and Contributing](Governance-and-Contributing.md) |
| Validate country files | [Validation and Runtime Bundles](Validation-and-Builds.md) | [Country Parameter Layer](Country-Parameter-Layer.md) |
| Compile a runtime JSON bundle | [Validation and Runtime Bundles](Validation-and-Builds.md) | [Architecture](Architecture.md) |
| Review an agent-generated draft | [Governance and Contributing](Governance-and-Contributing.md) | [Artifact Lifecycle](Artifact-Lifecycle.md) |
| Look up terminology or ID formats | [Glossary](Glossary.md) | [Artifact Model](Artifact-Model.md) |

## Document catalog

| Document | Main question answered |
|---|---|
| [Home](index.md) | What is this repository, what does it do, and how mature is it? |
| [Architecture and Data Flow](Architecture.md) | How do survey evidence, universal rules, country records, and downstream specifications interact? |
| [Repository Map](Repository-Map.md) | Which folder owns each concern and which scripts consume it? |
| [Artifact Model](Artifact-Model.md) | What does each canonical record contain and how do records reference one another? |
| [Artifact Lifecycle](Artifact-Lifecycle.md) | How does sourced guidance become reviewed canonical knowledge? |
| [Country Parameter Layer](Country-Parameter-Layer.md) | How are country values and exceptions selected for a survey year? |
| [Validation and Runtime Bundles](Validation-and-Builds.md) | What is checked, what is reported, and how is runtime JSON generated? |
| [Governance and Contributing](Governance-and-Contributing.md) | Who may change each area and what requires human approval? |
| [Glossary](Glossary.md) | What do the project's specialized terms and prefixes mean? |

## Suggested reading

- **For the shortest orientation:** start at [Home](index.md).
- **For path-based navigation:** use the
   [Repository Map](Repository-Map.md).
- **For terminology:** keep the [Glossary](Glossary.md) nearby.