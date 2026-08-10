# 🧠 Project Brain — Chronological Log

_Generated 2026-08-10 · 15 artifacts (newest first) + 43 roadmap features_

## 2026-08-10

- **[2026-08-07-calibrate-human-review-review](.cg-docs/reviews/2026-08-07-calibrate-human-review-review.md)** · `review` · _—_ · `2026-08-10`
  > **Review mode**: standard (explicit user request; publishing/deployment config kept in focus as a high-risk signal) *…
- **[2026-08-07-calibrate-human-review-verify-review](.cg-docs/reviews/2026-08-07-calibrate-human-review-verify-review.md)** · `review` · _—_ · `2026-08-10`
  > **Review mode**: light (mode:verify) **Prior review**: `.cg-docs/reviews/2026-08-07-calibrate-human-review-review.md`…
- **[Golem module tests: capture moduleServer returns, drive namespaced inputs, keep fixtures R CMD check-safe](.cg-docs/solutions/testing-patterns/2026-08-10-golem-module-testserver-capture.md)** · `solution` · _—_ · `2026-08-10`
  > When the review-app was restructured into the `{golem}` layout (`R/mod_dashboard.R`, `R/mod_detail.R`, `app_ui.R` → `…

## 2026-08-07

- **[Calibrate Human Review](.cg-docs/brainstorms/2026-08-07-calibrate-human-review.md)** · `brainstorm` · _decided_ · `2026-08-07`
  > <!-- Valid status values: decided, in-progress, abandoned -->
- **[Calibrate Human Review](.cg-docs/plans/2026-08-07-calibrate-human-review.md)** · `plan` · _active_ · `2026-08-07`
  > Make the Shiny review app live-capable, materialize a 6-variable calibration sample with full front matter (3 real + …

## 2026-08-06

- **[2026-08-03-extract-universal-non-welfare-schema-verify-review](.cg-docs/reviews/2026-08-03-extract-universal-non-welfare-schema-verify-review.md)** · `review` · _—_ · `2026-08-06`
  > **Review mode**: light (verify pass) **Prior review**: `.cg-docs/reviews/2026-08-03-extract-universal-non-welfare-sch…
- **[Windows Platform Test Failures: Line Endings, Symlinks, and Path Resolution](.cg-docs/solutions/testing-patterns/2026-08-06-windows-platform-test-fixes.md)** · `solution` · _—_ · `2026-08-06`
  > Three test failures occurred on Windows that passed on Linux/macOS: 1. `test_multiline_excerpt_bounds` — Excerpt "lin…

## 2026-08-04

- **[Build the Human Review Application](.cg-docs/brainstorms/2026-08-04-build-human-review-application.md)** · `brainstorm` · _decided_ · `2026-08-04`
  > <!-- Valid status values: decided, in-progress, abandoned -->
- **[Build the Human Review Application](.cg-docs/plans/2026-08-04-build-human-review-application.md)** · `plan` · _completed_ · `2026-08-04`
  > Deliver a private, Git-backed **Shiny for R** application, deployed to Posit Connect, that lets GPID reviewers browse…

## 2026-08-03

- **[2026-08-03-extract-universal-non-welfare-schema-review](.cg-docs/reviews/2026-08-03-extract-universal-non-welfare-schema-review.md)** · `review` · _—_ · `2026-08-03`
  > **Review mode**: standard (data-risk signals noted: extraction pipeline, reproducibility-sensitive, survey harmonizat…
- **[Extract the Universal Non-Welfare Schema](.cg-docs/brainstorms/2026-08-03-extract-universal-non-welfare-schema.md)** · `brainstorm` · _decided_ · `2026-08-03`
  > <!-- Valid status values: decided, in-progress, abandoned -->
- **[Extract the Universal Non-Welfare Schema](.cg-docs/plans/2026-08-03-extract-universal-non-welfare-schema.md)** · `plan` · _completed_ · `2026-08-03`
  > Build an evidence-first corpus compiler that locks the authoritative GMD guideline revision, inventories every non-we…
- **[Orchestrator cross-file attribute mismatch — untested code passes review](.cg-docs/solutions/bugs/2026-08-03-orchestrator-cross-file-attribute-mismatch.md)** · `solution` · _—_ · `2026-08-03`
  > The extraction orchestrator (`extraction_pipeline/orchestrator.py`) was added as a fix for P2.23 ("Missing orchestrat…
- **[Welfare boundary enforcement — content-based detection vs ID-substring heuristic](.cg-docs/solutions/testing-patterns/2026-08-03-welfare-boundary-content-based-detection.md)** · `solution` · _—_ · `2026-08-03`
  > The extraction pipeline's welfare leakage detector (`check_no_welfare_leakage` in `extraction_pipeline/reports.py`) u…

## 2026-07-30

- **[Complete CVS Roadmap](.cg-docs/strategy/2026-07-30-complete-cvs-roadmap.md)** · `strategy` · _—_ · `2026-07-30`
  > The roadmap contained one placeholder milestone that repeated the charter's broad framework-building focus. Three see…

## Roadmap Features

- **[Add labor parameters where confirmed by universal extraction](roadmap.json#add-labor-parameters)** · `feature` · _idea_ · `—`
  > Add labor parameters where confirmed by universal extraction
- **[Add deterministic routing, failure states, and audit records](roadmap.json#add-review-routing-audit)** · `feature` · _idea_ · `—`
  > Add deterministic routing, failure states, and audit records
- **[Create review branches and pull requests through a narrowly scoped GitHub App](roadmap.json#automate-review-pull-requests)** · `feature` · _idea_ · `—`
  > Create review branches and pull requests through a narrowly scoped GitHub App
- **[Build a cross-variable consistency and derivation review agent](roadmap.json#build-consistency-derivation-review)** · `feature` · _idea_ · `—`
  > Build a cross-variable consistency and derivation review agent
- **[Build extraction agents, skills, and Python orchestration](roadmap.json#build-extraction-system)** · `feature` · _done_ · `—`
  > Build extraction agents, skills, and Python orchestration
- **[Build the Markdown-to-YAML reconciliation agent and skill](roadmap.json#build-markdown-yaml-reconciliation)** · `feature` · _idea_ · `—`
  > Build the Markdown-to-YAML reconciliation agent and skill
- **[Build a rules and caveats completeness agent and skill](roadmap.json#build-rules-caveats-review)** · `feature` · _idea_ · `—`
  > Build a rules and caveats completeness agent and skill
- **[Build a schema-compliance review agent and skill](roadmap.json#build-schema-compliance-review)** · `feature` · _idea_ · `—`
  > Build a schema-compliance review agent and skill
- **[Build a private Shiny app for Posit Connect](roadmap.json#build-shiny-review-app)** · `feature` · _done_ · `—`
  > Build a private Shiny app for Posit Connect
- **[Build a source-grounding review agent and skill](roadmap.json#build-source-grounding-review)** · `feature` · _idea_ · `—`
  > Build a source-grounding review agent and skill
- **[Complete global rules and module specifications](roadmap.json#complete-global-rules-modules)** · `feature` · _idea_ · `—`
  > Complete global rules and module specifications
- **[Configure the real GPID CODEOWNERS team and branch protection](roadmap.json#configure-codeowners-protection)** · `feature` · _idea_ · `—`
  > Configure the real GPID CODEOWNERS team and branch protection
- **[Confirm completion criteria for all non-welfare variables](roadmap.json#confirm-non-welfare-completion)** · `feature` · _idea_ · `—`
  > Confirm completion criteria for all non-welfare variables
- **[Cross-check against legacy harmonization code](roadmap.json#cross-check-legacy-code)** · `feature` · _idea_ · `—`
  > Cross-check against legacy harmonization code
- **[Keep urban/rural parameters deferred unless evidence makes them necessary](roadmap.json#defer-urban-rural-parameters)** · `feature` · _idea_ · `—`
  > Keep urban/rural parameters deferred unless evidence makes them necessary
- **[Define the deterministic extraction contract and source-citation requirements](roadmap.json#define-extraction-contract)** · `feature` · _done_ · `—`
  > Define the deterministic extraction contract and source-citation requirements
- **[Define the versioned review states and manifest](roadmap.json#define-review-state-manifest)** · `feature` · _done_ · `—`
  > Define the versioned review states and manifest
- **[Document the schema approval from the 2026-07-29 GPID meeting](roadmap.json#document-schema-approval)** · `feature` · _done_ · `—`
  > Document the schema approval from the 2026-07-29 GPID meeting
- **[Allow editing only of the human Markdown section](roadmap.json#edit-human-markdown-only)** · `feature` · _done_ · `—`
  > Allow editing only of the human Markdown section
- **[Extract all non-welfare variables into extraction/20_drafts/](roadmap.json#extract-non-welfare-variables)** · `feature` · _done_ · `—`
  > Extract all non-welfare variables into extraction/20_drafts/
- **[Finalize the review rubric and acceptance criteria](roadmap.json#finalize-review-rubric)** · `feature` · _idea_ · `—`
  > Finalize the review rubric and acceptance criteria
- **[Freeze schema and country bundles as Version 1.0](roadmap.json#freeze-version-1)** · `feature` · _idea_ · `—`
  > Freeze schema and country bundles as Version 1.0
- **[Establish recurring regional exception gathering](roadmap.json#gather-regional-exceptions)** · `feature` · _idea_ · `—`
  > Establish recurring regional exception gathering
- **[Inventory all non-welfare variables and classify structural fields](roadmap.json#inventory-non-welfare-variables)** · `feature` · _done_ · `—`
  > Inventory all non-welfare variables and classify structural fields
- **[Measure extraction and agent-review errors](roadmap.json#measure-review-errors)** · `feature` · _idea_ · `—`
  > Measure extraction and agent-review errors
- **[Populate education parameters from authoritative sources](roadmap.json#populate-education-parameters)** · `feature` · _idea_ · `—`
  > Populate education parameters from authoritative sources
- **[Present the completed artifact and revisit institutional infrastructure needs](roadmap.json#present-version-1)** · `feature` · _idea_ · `—`
  > Present the completed artifact and revisit institutional infrastructure needs
- **[Process only approved Markdown revisions](roadmap.json#process-approved-markdown)** · `feature` · _idea_ · `—`
  > Process only approved Markdown revisions
- **[Promote approved universal records through the governed lifecycle](roadmap.json#promote-universal-records)** · `feature` · _idea_ · `—`
  > Promote approved universal records through the governed lifecycle
- **[Generate proposed YAML changes on review branches](roadmap.json#propose-yaml-review-changes)** · `feature` · _idea_ · `—`
  > Generate proposed YAML changes on review branches
- **[Record reviewer identity, review round, timestamps, and content hashes](roadmap.json#record-review-metadata)** · `feature` · _done_ · `—`
  > Record reviewer identity, review round, timestamps, and content hashes
- **[Resolve fallback authority and escalation behavior](roadmap.json#resolve-fallback-authority)** · `feature` · _idea_ · `—`
  > Resolve fallback authority and escalation behavior
- **[Resolve guideline-versus-practice differences through reviewed exceptions](roadmap.json#resolve-reviewed-exceptions)** · `feature` · _idea_ · `—`
  > Resolve guideline-versus-practice differences through reviewed exceptions
- **[Review and enrich their Markdown through the Shiny app](roadmap.json#review-calibration-sample)** · `feature` · _idea_ · `—`
  > Review and enrich their Markdown through the Shiny app
- **[Human-review all remaining variables through the calibrated workflow](roadmap.json#review-remaining-variables)** · `feature` · _idea_ · `—`
  > Human-review all remaining variables through the calibrated workflow
- **[Add save-draft and submit-for-GPID-review actions](roadmap.json#save-submit-review)** · `feature` · _done_ · `—`
  > Add save-draft and submit-for-GPID-review actions
- **[Select five to ten variables across complexity levels](roadmap.json#select-calibration-sample)** · `feature` · _done_ · `—`
  > Select five to ten variables across complexity levels
- **[Show extracted YAML and guideline evidence as read-only context](roadmap.json#show-yaml-guideline-evidence)** · `feature` · _done_ · `—`
  > Show extracted YAML and guideline evidence as read-only context
- **[Simplify the interface based on reviewer experience](roadmap.json#simplify-review-interface)** · `feature` · _idea_ · `—`
  > Simplify the interface based on reviewer experience
- **[Stress-test against legacy do-files and historical decisions](roadmap.json#stress-test-legacy-decisions)** · `feature` · _idea_ · `—`
  > Stress-test against legacy do-files and historical decisions
- **[Run structural validation after every extraction](roadmap.json#validate-every-extraction)** · `feature` · _done_ · `—`
  > Run structural validation after every extraction
- **[Validate references, provenance, and derivation graphs](roadmap.json#validate-provenance-derivations)** · `feature` · _idea_ · `—`
  > Validate references, provenance, and derivation graphs
- **[Run registry and derivation-graph validation](roadmap.json#validate-registry-derivations)** · `feature` · _idea_ · `—`
  > Run registry and derivation-graph validation
