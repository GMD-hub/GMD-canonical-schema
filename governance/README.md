# Governance Records

This folder contains project-level review records that are intentionally
separate from the canonical wiki and from the governed CVS artifacts.

## What belongs here

| Folder | Purpose | Examples |
|---|---|---|
| `audits/` | Findings about repository gaps, controls, documentation, tests, or operational risk | Gap audits and follow-up verification reports |
| `decisions/` | Questions requiring authority, options considered, decisions taken, and their implementation trace | Open decision requests and closed decision records |

The `wiki/` folder is the maintained operational reference for how the system
currently behaves. The `knowledge/` and `country-parameters/` folders contain
governed canonical content. Governance records do not redefine rules, variable
contracts, derivation relationships, fallback policies, or country values.

`extraction/30_review/` remains the location for human review notes attached to
candidate CVS artifacts. This folder records project-level audits and decisions
that may span multiple artifacts or repository controls.

## Record lifecycle

1. An audit records evidence, the gap determination, and the affected paths.
2. An audit may create one or more decision requests in `decisions/`.
3. A decision record remains `open` until the responsible authority records an
   outcome, date, rationale, and source or meeting reference.
4. Implementation references identify the files and tests changed because of
   the decision.
5. A follow-up audit verifies the result and links back to the decision record.

A recommendation is not a decision. An unresolved question remains open until
an authorized human records the outcome.

## Required provenance

Each record should state, at minimum:

- record type and stable record ID;
- creation date and current status;
- responsible authority or decision owner;
- source branch, commit, issue, meeting, or other evidence reference;
- related audit, decision, artifact, implementation, and validation paths;
- for a decision: outcome, decided date, decision authority, and rationale;
- for an audit: scope, method, evidence, finding, and disposition.

Use explicit relative paths so a reviewer can trace a question from its audit,
to its decision, to the implementation and validation evidence.

## Status vocabulary

- `draft`: record is being prepared or has not completed review;
- `open`: question or action remains unresolved;
- `decided`: an authorized decision and rationale are recorded;
- `closed`: implementation and follow-up verification are complete;
- `superseded`: a later record replaces this one.

## Current records

- [Gap Audit, July 2026](audits/Gap-Audit-2026-07.md)
- [Open Decisions, July 2026](decisions/Open-Decisions.md)
