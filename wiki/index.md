# GMD CVS Wiki

> **Purpose:** `docs/` holds narrative background explaining why the design is
> what it is, written to be read once. `wiki/` holds operational reference
> documentation describing how the system currently behaves and is maintained
> continuously.

<p class="gmd-lede">Learn how governed harmonization guidance moves from
source evidence to canonical knowledge, country-specific inputs, and a
traceable runtime bundle.</p>

The GMD Canonical Variable Schema (CVS) is the policy layer for AI-assisted
household survey harmonization. This site explains what the CVS owns, how its
parts relate, and where human judgment remains mandatory.

!!! info "The central idea"
   A **Survey Profile** says what evidence a survey contains. The
   **effective canon** says which universal rules and governed country inputs
   apply. Together they support a draft **Harmonization Specification** that
   a human reviews before implementation.

## Start here

<div class="grid cards" markdown>

-   :material-map-outline:{ .lg .middle } **Understand the system**

    ---

    Follow evidence through the three-schema workflow and see how the
    effective canon is resolved.

    [Open architecture :material-arrow-right:](Architecture.md)

-   :material-file-tree-outline:{ .lg .middle } **Find the owning folder**

    ---

    Connect each repository path to its responsibility, input, and output.

    [Explore the repository map :material-arrow-right:](Repository-Map.md)

-   :material-shape-outline:{ .lg .middle } **Learn the artifacts**

    ---

    Compare variables, rules, parameters, and country exceptions before
    editing structured records.

    [Study the artifact model :material-arrow-right:](Artifact-Model.md)

-   :material-account-check-outline:{ .lg .middle } **Make a governed change**

    ---

    Move a sourced proposal through drafting, review, approval, validation,
    and promotion.

    [Follow the lifecycle :material-arrow-right:](Artifact-Lifecycle.md)

</div>

For a complete sequence or a task-specific route, use the
[learning paths](Learning-Paths.md).

Questions that require GPID Team authority are tracked in the independent
`governance/decisions/` record area. Project audits are kept in
`governance/audits/`; neither folder is part of the official wiki.

## A first worked example

!!! example "Hypothetical walkthrough: constructing years of education"
    This scenario is invented to explain the workflow. It is **not evidence
    about any real survey or country** and must not be used as a governed
    parameter or exception.

    1. A fictional Survey Profile reports a respondent's highest completed
       education category, but not explicit years of schooling.
    2. `VAR-educy` says categorical education may be used as a fallback path
       and declares `PARAM-EDU-YEARS-BY-LEVEL` as a dependency.
    3. The consumer loads the survey country's parameter and exception files
       and selects records using the fieldwork start year.
    4. If a valid, reviewed duration mapping exists, the universal rule uses
       it to translate the category into years. If none exists, the
       parameter's fallback policy decides whether to continue or escalate.
    5. The proposed mapping, selected record, validity window, source, and CVS
       commit are recorded in a Harmonization Specification for human review.

    The example connects the [architecture](Architecture.md),
    [artifact model](Artifact-Model.md), and
    [country resolution algorithm](Country-Parameter-Layer.md) without
    claiming that a particular value is correct.

The [glossary](Glossary.md) defines project-specific terms. The repository
[README](https://github.com/GMD-hub/GMD-canonical-schema/blob/main/README.md)
is the shorter entry point.

## Current implementation status

As of 2026-07-28, the repository uses schema version 0.1 and remains a draft
knowledge base. The authoritative inventory in `knowledge/index.md` contains:

| Artifact type | Current count | Notes |
|---|---:|---|
| Variable specifications | 3 | `male`, `educat4`, and `educy` |
| Decision rules | 4 | One sex rule and three education rules |
| Parameter definitions | 2 | Education duration and minimum marriage age |
| Module specifications | 0 | Folder structure exists; records have not been added |
| Universal exceptions | 0 | Country exceptions live in the country layer |

Twelve country folders exist. PER is an illustrative, unverified worked
example; the other country files are empty drafts. No placeholder or
`human_reviewed: false` value should be treated as production evidence.

## What this repository does and does not do

The CVS does:

- define canonical variables, values, missing codes, and derivation links;
- express reusable decision rules and explicit prohibitions;
- register country-dependent parameters and their fallback behavior;
- hold effective-dated country values and permitted country exceptions;
- validate country-layer structure and generate machine-readable JSON bundles;
- preserve provenance and the Git commit used for a runtime bundle.

The CVS does not:

- extract data or metadata from raw surveys;
- decide which raw survey variable matches a GMD variable by itself;
- execute Stata or generate production harmonization code;
- make unreviewed country values authoritative;
- replace GPID Team review and approval.

## Sources of truth

The hierarchy is:

1. `GMD_household_survey_harmonization.md` in `GMD-hub/GMD-guidelines` is the
   authority for harmonization rules.
2. Approved CVS artifacts represent those rules in this repository.
3. `knowledge/index.md` is the inventory and navigation entry point.
4. Generated JSON bundles are derived snapshots, never authoring sources.

When an artifact conflicts with the guidelines, the guidelines win. Record
the conflict in provenance notes and escalate it to the GPID Team.

## Related documents

- **New to the CVS?** Continue with
   [Architecture and Data Flow](Architecture.md).
- **Looking for a specific task?** Use the
   [Learning Paths](Learning-Paths.md).
- **Need a term quickly?** Open the [Glossary](Glossary.md).

## All wiki pages

[Home](index.md) | [Learning Paths](Learning-Paths.md) |
[Architecture](Architecture.md) | [Repository Map](Repository-Map.md) |
[Artifact Model](Artifact-Model.md) |
[Country Parameter Layer](Country-Parameter-Layer.md) |
[Artifact Lifecycle](Artifact-Lifecycle.md) |
[Validation and Builds](Validation-and-Builds.md) |
[Governance and Contributing](Governance-and-Contributing.md) |
[Glossary](Glossary.md)
