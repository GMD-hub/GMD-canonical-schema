# GMD CVS Wiki

This wiki explains how the GMD Canonical Variable Schema (CVS) works, how its
folders relate to one another, and how governed Markdown becomes a runtime
bundle for AI-assisted harmonization.

## Start here

1. Read [Architecture and data flow](Architecture.md) for the system model.
2. Use [Repository map](Repository-Map.md) to find the owning folder.
3. Read [Artifact model](Artifact-Model.md) before editing structured records.
4. Follow [Artifact lifecycle](Artifact-Lifecycle.md) for drafting and review.
5. Read [Country parameter layer](Country-Parameter-Layer.md) before using any
   country-specific content.
6. Use [Validation and runtime bundles](Validation-and-Builds.md) to check and
   compile the repository.
7. Follow [Governance and contributing](Governance-and-Contributing.md) for
   write permissions and approval requirements.

The [glossary](Glossary.md) defines project-specific terms. The root
[README](../README.md) is the shorter entry point.

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
