# 🧠 Project Brain — Chronological Log

_Generated 2026-09-03 · 37 artifacts (newest first) + 56 roadmap features_

## undated

- **[2026-08-14-agent-review-lessons](.cg-docs/brainstorms/2026-08-14-agent-review-lessons.md)** · `brainstorm` · _—_ · `—`
  > A prototype of all 4 review agents was built and run against the 6 calibration drafts. The prototype was reverted bec…

## 2026-09-03

- **[Direct GitHub App Review Queue Cutover](.cg-docs/solutions/git-workflows/2026-09-03-direct-review-queue-cutover.md)** · `solution` · _—_ · `2026-09-03`
  > The production queue needed one format-only migration from production-v2 controls to descriptor schema 1.1. A separat…

## 2026-08-30

- **[2026-08-25-canonical-non-welfare-inventory-ledger-review](.cg-docs/reviews/2026-08-25-canonical-non-welfare-inventory-ledger-review.md)** · `review` · _—_ · `2026-08-30`
  > This report verifies the repaired Task C implementation on PR #18 after merging `origin/main` commit `90eddb33425a051…

## 2026-08-26

- **[2026-08-25-complete-release-a-production-queue-cutover-review](.cg-docs/reviews/2026-08-25-complete-release-a-production-queue-cutover-review.md)** · `review` · _—_ · `2026-08-26`
  > **Review mode**: full (`review:auto`, release/security risk) **Findings**: 12 (P0: 3, P1: 5, P2: 4)
- **[2026-08-25-complete-release-a-production-queue-cutover-review-2](.cg-docs/reviews/2026-08-25-complete-release-a-production-queue-cutover-review-2.md)** · `review` · _—_ · `2026-08-26`
  > `mode:verify` found no prior fixed finding and therefore fell back to a normal full review.
- **[2026-08-25-complete-release-a-production-queue-cutover-verify-review](.cg-docs/reviews/2026-08-25-complete-release-a-production-queue-cutover-verify-review.md)** · `review` · _—_ · `2026-08-26`
  > **Review mode**: light verification **Findings**: 1 (P0: 1)
- **[Fail-Closed Deterministic Promotion from Immutable Evidence](.cg-docs/solutions/data-quality/2026-08-26-fail-closed-deterministic-promotion.md)** · `solution` · _—_ · `2026-08-26`
  > A promotion command could accept a hand-authored candidate that passed schema and fixed-total checks but was never re…
- **[Testing release queues with distinct commits and exact regeneration](.cg-docs/solutions/testing-patterns/2026-08-26-release-queue-validator-bindings.md)** · `solution` · _—_ · `2026-08-26`
  > A production queue validator initially treated checkout `HEAD` as the pinned source commit. That fails after bootstra…

## 2026-08-25

- **[Canonical Non-Welfare Inventory Ledger](.cg-docs/plans/2026-08-25-canonical-non-welfare-inventory-ledger.md)** · `plan` · _completed_ · `2026-08-25`
  > Replace the contradictory prose inventory with one deterministic, row-level, machine-readable ledger that proves the …
- **[Enable and Complete Release A Production Queue Cutover](.cg-docs/plans/2026-08-25-complete-release-a-production-queue-cutover.md)** · `plan` · _completed_ · `2026-08-25`
  > This plan closed on 2026-09-03 with an approved simplification. The separate staging repository, staging Connect item…

## 2026-08-20

- **[2026-08-13-complete-non-welfare-extraction-verify-review-2](.cg-docs/reviews/2026-08-13-complete-non-welfare-extraction-verify-review-2.md)** · `review` · _—_ · `2026-08-20`
  > **Review mode**: verify (light) **Files reviewed**: extraction_pipeline/review_agents/helpers.py, tests/review_agents…
- **[Exclude non-variable dirs from the review runner to eliminate false-positive errors](.cg-docs/solutions/testing-patterns/2026-08-20-exclude-runs-from-review-runner.md)** · `solution` · _—_ · `2026-08-20`
  > The agent review runner reported **40 errors / 497 warnings** across 271 drafts (`extraction/25_agent_review/`). All …
- **[Exclude runs/ from the review runner to eliminate 40 false-positive errors](.cg-docs/plans/2026-08-20-exclude-runs-from-review-runner.md)** · `plan` · _completed_ · `2026-08-20`
  > Drive the agent review error count from **40 -> 0** by aligning `extraction_pipeline/review_agents/helpers.py::list_d…

## 2026-08-17

- **[Fix parameter-registry loading in the schema-compliance review runner](.cg-docs/plans/2026-08-17-fix-parameter-registry-loading-review-runner.md)** · `plan` · _done_ · `2026-08-17`
  > Make `extraction_pipeline.review_agents.run_all_agents` load the universal parameter registry from `knowledge/paramet…
- **[Parameter registry loading pattern for review agents](.cg-docs/solutions/testing-patterns/2026-08-17-parameter-registry-loading.md)** · `solution` · _—_ · `2026-08-17`
  > Review agents that validate `country_parameters` references need access to the parameter ID registry (`knowledge/para…

## 2026-08-15

- **[Build Independent Agent Review System](.cg-docs/plans/2026-08-14-build-agent-review.md)** · `plan` · _active_ · `2026-08-15`
  > Build four deterministic Python review agents and a runner that validate every extraction draft in `extraction/20_dra…
- **[Derivation asymmetry check requires both variables in draft set](.cg-docs/solutions/testing-patterns/2026-08-15-unresolved-derivation-ref.md)** · `solution` · _—_ · `2026-08-15`
  > VAR-urban declares `derived_from: [VAR-rurality]` but VAR-rurality is not in the draft set. The expected test for an …
- **[Pydantic allow_unresolved_draft does not bypass rule_ids/parameter_ids validation](.cg-docs/solutions/testing-patterns/2026-08-15-pydantic-rule-ids-context.md)** · `solution` · _—_ · `2026-08-15`
  > When validating extraction drafts against `VariableDefinition` with `allow_unresolved_draft=True`, Pydantic raised `u…

## 2026-08-14

- **[2026-08-13-complete-non-welfare-extraction-review](.cg-docs/reviews/2026-08-13-complete-non-welfare-extraction-review.md)** · `review` · _—_ · `2026-08-14`
  > **Review mode**: data-risk (auto-routed from /cg-work review:auto) **Files reviewed**: 267 variable drafts + 3 run re…
- **[2026-08-13-complete-non-welfare-extraction-verify-review](.cg-docs/reviews/2026-08-13-complete-non-welfare-extraction-verify-review.md)** · `review` · _—_ · `2026-08-14`
  > **Note**: Verify mode was invoked as `/cg-review mode:verify`, but the prior review (`2026-08-13-complete-non-welfare…
- **[Hand-drafting GMD CVS variable specs at scale and validating them](.cg-docs/solutions/data-quality/2026-08-14-hand-draft-cvs-variable-specs.md)** · `solution` · _—_ · `2026-08-14`
  > The GMD Canonical Variable Schema (CVS) needed `VariableDefinition`-valid draft specs for every non-welfare variable …

## 2026-08-13

- **[Complete Non-Welfare Variable Extraction Across All Modules](.cg-docs/plans/2026-08-13-complete-non-welfare-extraction.md)** · `plan` · _completed_ · `2026-08-13`
  > Produce schema-valid, source-grounded draft specifications for **every** non-welfare variable defined in the GMD harm…

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
- **[Add deterministic routing, failure states, and audit records](roadmap.json#add-review-routing-audit)** · `feature` · _planned_ · `—`
  > Add deterministic routing, failure states, and audit records
- **[Create review branches and pull requests through a narrowly scoped GitHub App](roadmap.json#automate-review-pull-requests)** · `feature` · _idea_ · `—`
  > Create review branches and pull requests through a narrowly scoped GitHub App
- **[Build a cross-variable consistency and derivation review agent](roadmap.json#build-consistency-derivation-review)** · `feature` · _planned_ · `—`
  > Build a cross-variable consistency and derivation review agent
- **[Build extraction agents, skills, and Python orchestration](roadmap.json#build-extraction-system)** · `feature` · _done_ · `—`
  > Build extraction agents, skills, and Python orchestration
- **[Build the Markdown-to-YAML reconciliation agent and skill](roadmap.json#build-markdown-yaml-reconciliation)** · `feature` · _idea_ · `—`
  > Build the Markdown-to-YAML reconciliation agent and skill
- **[Build a rules and caveats completeness agent and skill](roadmap.json#build-rules-caveats-review)** · `feature` · _planned_ · `—`
  > Build a rules and caveats completeness agent and skill
- **[Build a schema-compliance review agent and skill](roadmap.json#build-schema-compliance-review)** · `feature` · _planned_ · `—`
  > Build a schema-compliance review agent and skill
- **[Build a private Shiny app for Posit Connect](roadmap.json#build-shiny-review-app)** · `feature` · _done_ · `—`
  > Build a private Shiny app for Posit Connect
- **[Build a source-grounding review agent and skill](roadmap.json#build-source-grounding-review)** · `feature` · _planned_ · `—`
  > Build a source-grounding review agent and skill
- **[Create the canonical non-welfare inventory ledger](roadmap.json#canonical-non-welfare-inventory-ledger)** · `feature` · _planned_ · `—`
  > Create the canonical non-welfare inventory ledger
- **[Classify mineducatage as a variable to draft or a country parameter to register \(currently an unregistered prerequisite reference in VAR-educat7\)](roadmap.json#classify-mineducatage)** · `feature` · _idea_ · `—`
  > Classify mineducatage as a variable to draft or a country parameter to register (currently an unregistered prerequisi…
- **[Complete global rules and module specifications](roadmap.json#complete-global-rules-modules)** · `feature` · _idea_ · `—`
  > Complete global rules and module specifications
- **[Complete Release A production queue cutover](roadmap.json#complete-release-a-production-queue-cutover)** · `feature` · _done_ · `—`
  > Complete Release A production queue cutover
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
- **[Use approved variable status for Foundry eligibility](roadmap.json#enforce-approved-variable-status)** · `feature` · _done_ · `—`
  > Use approved variable status for Foundry eligibility
- **[Extract all non-welfare variables into extraction/20_drafts/](roadmap.json#extract-non-welfare-variables)** · `feature` · _done_ · `—`
  > Extract all non-welfare variables into extraction/20_drafts/
- **[Finalize the review rubric and acceptance criteria](roadmap.json#finalize-review-rubric)** · `feature` · _done_ · `—`
  > Finalize the review rubric and acceptance criteria
- **[Exclude runs/ from the review runner to eliminate 40 false-positive errors](roadmap.json#fix-review-runner-runs-exclusion)** · `feature` · _done_ · `—`
  > Exclude runs/ from the review runner to eliminate 40 false-positive errors
- **[Fix parameter-registry loading in the schema-compliance review runner](roadmap.json#fix-schema-compliance-parameter-loading)** · `feature` · _done_ · `—`
  > Fix parameter-registry loading in the schema-compliance review runner
- **[Freeze schema and country bundles as Version 1.0](roadmap.json#freeze-version-1)** · `feature` · _idea_ · `—`
  > Freeze schema and country bundles as Version 1.0
- **[Establish recurring regional exception gathering](roadmap.json#gather-regional-exceptions)** · `feature` · _idea_ · `—`
  > Establish recurring regional exception gathering
- **[Inventory all non-welfare variables and classify structural fields](roadmap.json#inventory-non-welfare-variables)** · `feature` · _done_ · `—`
  > Inventory all non-welfare variables and classify structural fields
- **[Launch production content review and approval](roadmap.json#launch-production-content-review)** · `feature` · _planned_ · `—`
  > Launch production content review and approval
- **[Measure extraction and agent-review errors](roadmap.json#measure-review-errors)** · `feature` · _done_ · `—`
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
- **[Refresh review-agent test conventions and stale solution note after the parameter-registry fix](roadmap.json#refresh-review-agent-test-and-doc-conventions)** · `feature` · _idea_ · `—`
  > Refresh review-agent test conventions and stale solution note after the parameter-registry fix
- **[Register the Non-Null Weight Invariant as a RULE-WGT-* rule artifact so IDN weight variables can reference it without breaking strict validation](roadmap.json#register-weight-invariant-rule)** · `feature` · _idea_ · `—`
  > Register the Non-Null Weight Invariant as a RULE-WGT-* rule artifact so IDN weight variables can reference it without…
- **[Resolve the 7-vs-8 body-section contract at the governance level: reconcile the existing 7-section draft format \(Definition, Conceptual intent, Construction notes, Consistency checks, Escalation triggers, Common mistakes, Change log\) against the authoritative 8-section contract in universal-extraction.md and extraction-governance.v1.yaml](roadmap.json#resolve-body-section-contract)** · `feature` · _idea_ · `—`
  > Resolve the 7-vs-8 body-section contract at the governance level: reconcile the existing 7-section draft format (Defi…
- **[Resolve fallback authority and escalation behavior](roadmap.json#resolve-fallback-authority)** · `feature` · _idea_ · `—`
  > Resolve fallback authority and escalation behavior
- **[Resolve guideline-versus-practice differences through reviewed exceptions](roadmap.json#resolve-reviewed-exceptions)** · `feature` · _idea_ · `—`
  > Resolve guideline-versus-practice differences through reviewed exceptions
- **[Review and enrich their Markdown through the Shiny app](roadmap.json#review-calibration-sample)** · `feature` · _done_ · `—`
  > Review and enrich their Markdown through the Shiny app
- **[Human-review all remaining variables through the calibrated workflow](roadmap.json#review-remaining-variables)** · `feature` · _idea_ · `—`
  > Human-review all remaining variables through the calibrated workflow
- **[Add save-draft and submit-for-GPID-review actions](roadmap.json#save-submit-review)** · `feature` · _done_ · `—`
  > Add save-draft and submit-for-GPID-review actions
- **[Select five to ten variables across complexity levels](roadmap.json#select-calibration-sample)** · `feature` · _done_ · `—`
  > Select five to ten variables across complexity levels
- **[Show extracted YAML and guideline evidence as read-only context](roadmap.json#show-yaml-guideline-evidence)** · `feature` · _done_ · `—`
  > Show extracted YAML and guideline evidence as read-only context
- **[Simplify the interface based on reviewer experience](roadmap.json#simplify-review-interface)** · `feature` · _done_ · `—`
  > Simplify the interface based on reviewer experience
- **[Standardize the variable naming convention: document the mapping from GMD snake_case names to CVS variable_id \(no underscores, per ^VAR-\[a-z\]\[a-z0-9\]*$\) and record each mapping in the inventory before drafting](roadmap.json#standardize-variable-naming-convention)** · `feature` · _idea_ · `—`
  > Standardize the variable naming convention: document the mapping from GMD snake_case names to CVS variable_id (no und…
- **[Stress-test against legacy do-files and historical decisions](roadmap.json#stress-test-legacy-decisions)** · `feature` · _idea_ · `—`
  > Stress-test against legacy do-files and historical decisions
- **[Tune the rules_caveats vague-text regex and escalation IF/WHEN heuristic to drop ~150 false-positive warnings](roadmap.json#tune-vague-text-escalation-heuristic)** · `feature` · _idea_ · `—`
  > Tune the rules_caveats vague-text regex and escalation IF/WHEN heuristic to drop ~150 false-positive warnings
- **[Unify EXCLUDE_DIRS across helpers.py and fix_derivation_asymmetry.py to prevent future drift](roadmap.json#unify-exclude-dirs)** · `feature` · _idea_ · `—`
  > Unify EXCLUDE_DIRS across helpers.py and fix_derivation_asymmetry.py to prevent future drift
- **[Run structural validation after every extraction](roadmap.json#validate-every-extraction)** · `feature` · _done_ · `—`
  > Run structural validation after every extraction
- **[Validate references, provenance, and derivation graphs](roadmap.json#validate-provenance-derivations)** · `feature` · _idea_ · `—`
  > Validate references, provenance, and derivation graphs
- **[Run registry and derivation-graph validation](roadmap.json#validate-registry-derivations)** · `feature` · _idea_ · `—`
  > Run registry and derivation-graph validation
