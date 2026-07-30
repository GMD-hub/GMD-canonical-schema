---
date: 2026-07-30
title: "Complete CVS Roadmap"
trigger: "new-project"
outcome: "roadmap-updated"
---

# Strategy Session: Complete CVS Roadmap

## Context at Session Start

The roadmap contained one placeholder milestone that repeated the charter's broad framework-building focus. Three seed variable records existed, but the project did not yet have an actionable sequence for scaling the universal schema, human review, agent review, or the Country Parameter Layer.

The GPID Team approved the schema and templates on 2026-07-29. Documented team agreement is sufficient for project decisions and GPID Team approval is sufficient for human approval.

## Discussion Summary

The extraction target is every non-welfare variable covered by the GMD harmonization guidelines. Welfare variables are explicitly out of scope. The universal guideline content should be established before country parameters are populated.

The workflow should be highly agentic but as deterministic as possible. Python orchestration and validators will control inventories, state transitions, validation, and audit records. Specialized agents and skills will perform extraction, source-grounding review, schema review, completeness review, cross-variable consistency review, and Markdown-to-YAML reconciliation.

Human reviewers should edit only the readable Markdown content. A private Shiny app deployed under the project lead's Posit Connect account will provide a constrained review interface to authorized users. The app will preserve reviewer identity, review rounds, timestamps, and content hashes, while GitHub branches, pull requests, checks, and GPID Team approval remain the authoritative audit and approval path.

The app will be built in parallel with extraction and used for the first representative review sample. Country-specific content uses the terms Country Parameter Layer and `country-parameters/`; "lookup tables" is retired terminology.

## Proposed Changes

Replace the placeholder roadmap with seven milestones:

1. Extract the Universal Non-Welfare Schema.
2. Build the Human Review Application.
3. Establish Independent Agent Review.
4. Calibrate Human Review.
5. Reconcile and Complete Universal Records.
6. Populate the Country Parameter Layer.
7. Validate and Freeze Version 1.0.

The roadmap contains 43 features. The schema-approval feature is complete; all implementation features begin as ideas. The review application and bulk extraction are explicitly parallel workstreams.

## Decision

The user approved the proposed roadmap. The placeholder milestone and duplicate feature were retired, and `roadmap.json` was updated and verified with all seven milestones and 43 features.

Shiny in R was selected over Streamlit because the project lead can build and maintain the reviewer interface more efficiently in Shiny. The app remains a thin review client: Python continues to own schema validation and deterministic orchestration.

## Charter Updates

The previous Current Focus was archived in `.cg-docs/archive/charter-history.md`. The charter now focuses on extracting all non-welfare guideline content through the deterministic agent pipeline while building the private Posit Connect review app in parallel. `last-reviewed` was updated to 2026-07-30.