---
date: 2026-08-07
title: "Calibrate Human Review"
status: decided
scope: "Deep"
artifact-schema-version: 1
chosen-approach: "Instrument-first, run-once, finalize"
tags: [human-review, calibration, shiny, review-rubric, measurement, interface, governance]
---
<!-- Valid status values: decided, in-progress, abandoned -->

# Calibrate Human Review

## Context

The Shiny review app (`review-app/`) is built and all unit/integration tests
pass against an in-memory GitHub double (`test-integration.R`). The
calibration sample is defined in
`.cg-docs/calibration/2026-08-06-calibration-sample.md` (6 variables: real
`VAR-male`, `VAR-educat4`, `VAR-educy` from `knowledge/`; fixtures
`VAR-educat7`, `VAR-urban`, `VAR-marital`). `extraction/20_drafts/` is empty
and needs the sample materialized. Roadmap milestone `calibrate-human-review`
is `in-progress` with `select-calibration-sample` done; remaining features
are `review-calibration-sample`, `measure-review-errors`,
`simplify-review-interface`, `finalize-review-rubric`. The
`independent-agent-review` milestone is planned, not started; this
calibration focuses on the human-review-only workflow, treating agent review
as a future layer.

The predecessor plan's R21/V9 requires validating the MVP against a
calibration sample before scaling. Its own Phase 5 review (execution report,
Run 5, Step 3.9, full mode) found unresolved P0/P1 defects that block a real
live operator run: a leaked RSA private key in `tests/testthat/pubkey`; C1
front-matter immutability is a no-op; audit/content-hash binding broken;
production write transport cannot send payloads (`gh_adapter_http` has no
`body`); the adapter is never wired into the server; `app.R` calls a
non-exported entry point (won't boot on Connect); preview XSS;
`authorize()` fails open; and more. The review's recommendation: do not
commit until `/cg-fix-triage` resolves the P0 set.

Two further findings shape the plan: (1) a draft front-matter discrepancy —
the real `knowledge/` artifacts carry full front matter, while the
integration test materializes minimal `artifact_id` + `module` stubs; (2) a
module inconsistency — `educat4`/`educy` carry `module_id: MOD-DEM` and live
under `knowledge/variables/dem/` (guidelines source section "Demography
(DEM)"), yet the calibration sample assigns them `edu`, the
`knowledge/variables/edu/` directory is empty, and the dashboard filter is
hard-coded to `dem`/`edu`/`welfare` (no `geo`).

## Requirements

Decisions from clarification (one per question area, plus the
seeded-defects decision from the devil's-advocate exchange):

1. **Live-run vs fixes (Q1): live-capable subset first.** Phase 0 fixes only
   the defects that block a safe, evidence-trustworthy live run; the live
   calibration runs against a disposable repo + Posit Connect staging; the
   remaining P0/P1 set is deferred to a tracked separate fix effort.
2. **Draft front matter (Q2): full front matter, mirror `knowledge/`.** All 6
   drafts carry the full variable-spec front matter and Markdown body. The 3
   real members copy from `knowledge/variables/`; the 3 fixtures are authored
   to match that structure. The C1 front-matter-immutability fix joins
   Phase 0.
3. **Module convention (Q3): `module_id` authoritative.** Drafts land under the
   directory matching their front-matter `module_id` (male/educat4/educy/
   educat7/marital -> `dem`; urban -> `geo`; `educat7` authored `MOD-DEM` to
   match `educat4`). The dashboard module filter is derived from indexed
   `module_id`s (`geo` appears; dead `edu`/`welfare` drop). The empty
   `knowledge/variables/edu/` and the sample's `edu` assignment are recorded
   as a governance/consistency finding for the measurement framework.
4. **Error taxonomy (Q4): unified content taxonomy + separate defect log.**
   Define the full content-error taxonomy now, aligned to the 4 future
   agent-review dimensions (source-grounding, schema-compliance,
   rules-caveats, consistency-derivation) plus human-review content
   categories, with a `stage` field (extraction / human-review /
   agent-review), severity, and a structured log format. The calibration
   populates extraction + human-review errors; agent-review categories are
   reserved, tagged-but-not-populated. App/tooling defects go in a separate
   defect log so they do not dilute content error rates.
5. **Rubric (Q5): two-layer, gating 30 -> 40.** Layer 1 (automated, blocks
   submission): YAML schema-valid + front matter byte-unchanged + all
   required Markdown sections present and non-stub. Layer 2 (human, blocks
   approval): per-section content quality (Definition accuracy,
   Construction-notes path coverage, Consistency-check actionability,
   Escalation-triggers presence, Common-mistakes relevance) judged against
   the read-only guideline-evidence panel. Promotion from
   `extraction/30_review/` to `extraction/40_approved/` requires both layers
   plus no open block/major extraction errors. Agent-review dimensions are
   reserved as future gates.
6. **Interface simplification (Q6): friction-driven + fix known issues in
   Phase 0.** Phase 0 derives the dashboard filter from `module_id`s and
   drops dead `edu`/`welfare`. The live-operator protocol captures structured
   friction (per-task time-on-task, error count, 1-5 friction rating per
   step, free-text) in a friction log with severity (block/slow/cosmetic).
   Decision rule: a friction item that blocks a required path, or is rated
   >=4 by >=2 reviewers, triggers a simplification change before scaling;
   cosmetic items batch for later. Criteria: reduce steps per path, remove
   dead/ambiguous controls, clarify labels, surface guideline evidence
   beside the editor.
7. **Reviewer panel (Q7): 2 reviewers (reviewer + approver).** The
   administrator reopen path is covered by `test-integration.R` against the
   double only; admin friction goes unmeasured in the live run (acknowledged
   trade-off). The >=2-reviewer friction threshold is satisfied for
   reviewer + approver.
8. **Seeded defects (devil's advocate): known-answer calibration.** The 3
   fixture drafts deliberately contain planted known defects (e.g. a
   hallucinated rule, a `module_id`/directory mismatch, a missing escalation
   trigger, a derivation-graph break). The known-answer key is kept separate
   and used only for scoring. Reviewer and rubric detection are measured
   (catch rate, false negatives). The 3 real members are pre-approved and
   treated as the (likely clean) baseline.

## Approaches Considered

All three share **Phase 0 (live-capable subset)**: wire the adapter into the
server; fix the production-write transport (`req_body_json`); fix the Connect
entry point; remove the leaked private key + gitignore + tempfile PEM; fix
preview XSS; fix C1 front-matter immutability; derive the dashboard module
filter from `module_id`s. The precise P0/P1 boundary (e.g. `authorize()`
fail-closed, audit/content-hash binding) is set at plan time via
`/cg-fix-triage`, with the principle that anything making the live run unsafe
or its audit evidence untrustworthy is in Phase 0; pure cleanliness/hardening
(exhaustive `validate_review_record`, NAMESPACE/roxygen, `renv.lock`, `DT`
declaration) is deferred.

### Approach 1: Instrument-first, run-once, finalize

Define the shared instrumentation (measurement taxonomy + log/defect format,
two-layer rubric + section template, live-operator protocol, friction log) up
front as one coherent spec; materialize the 6 drafts conforming to the
template; execute one live run that populates all logs and exercises the
rubric; then measure, simplify, and finalize the rubric from run evidence.

**Pros:** most coherent single source of truth; drafts conform to the rubric
from the start; errors log in the right schema with no retrofit; single live
run; the rubric is *finalized* (not merely defined) from real evidence;
matches the "coherent sequence, each step feeds the next" requirement.
**Cons:** heavier upfront design; if the run reveals the instrumentation is
wrong, specs are refactored.
**Effort:** Large. **Recommended:** Yes.

### Approach 2: Materialize-first, instrument-as-you-go

Materialize the 6 drafts and complete Phase 0 fixes first; derive the
measurement/rubric/protocol from the drafts and a dry-run; back-fill ad-hoc
errors into the taxonomy; run live; simplify/finalize.

**Pros:** specs grounded in real drafts; lower risk of designing the wrong
section template.
**Cons:** materialization errors are logged ad-hoc then retrofitted (rework);
the rubric template is derived from 3 real + 3 synthetic drafts which may not
be canonical; less coherent.
**Effort:** Large. **Recommended:** No — retrofit and template-canonicity
risks undercut the coherent-sequence requirement.

### Approach 3: Two-run calibration (pilot then formal)

Instrumentation spec + Phase 0; a pilot run on 2 drafts (1 simple, 1 complex)
to shake out the protocol/instrumentation and app fixes; a formal run on all
6 with finalized instrumentation; measure/simplify/finalize.

**Pros:** catches instrumentation/protocol/app-fix flaws before the full run;
highest-quality measurement.
**Cons:** two live runs = more reviewer time and scheduling; slower; arguably
over-engineered for a 6-artifact sample.
**Effort:** Large. **Recommended:** No (for a 6-artifact sample); becomes
attractive if the sample grows or Phase 0 proves unusually shaky.

## Decision

**Approach 1: Instrument-first, run-once, finalize.**

It is the most coherent: the instrumentation (measurement taxonomy, two-layer
rubric, protocol, friction log) is defined once up front so the materialized
drafts conform to the rubric's section template and extraction errors log in
the right schema from the first write. A single live run populates all logs
and exercises both rubric layers, and the rubric is *finalized* from real run
evidence rather than asserted. This best satisfies the requirement that the
five deliverables form a coherent sequence where each step's output feeds the
next. Seeded known defects in the 3 fixtures make extraction-error detection
measurable on the small sample.

## Next Steps

Handoff to `/cg-plan`, which will detail a phased implementation:

- **Phase 0 — Live-capable subset (app fixes):** run `/cg-fix-triage` to set
  the exact P0/P1 boundary; wire the adapter into the server; fix the
  production-write transport; fix the Connect entry point; remove the leaked
  private key; fix preview XSS; fix C1 front-matter immutability; derive the
  dashboard module filter from `module_id`s. Defer the remaining P0/P1 set to
  a tracked separate effort (add a roadmap idea or a `/cg-fix-triage`
  follow-up).
- **Phase 1 — Instrumentation spec:** content-error taxonomy (aligned to the
  4 future agent-review dimensions + human-review content), `stage` +
  severity + structured log; separate app-defect log; two-layer rubric (Layer
  1 structural template = the variable-spec Markdown section set + YAML
  schema gate; Layer 2 per-section content criteria); live-operator protocol
  (paths, time-on-task, error count, 1-5 friction rating, free-text) and
  friction-log format.
- **Phase 2 — Materialize the 6 drafts:** full front matter mirroring
  `knowledge/`, `module_id`-authoritative directories; copy the 3 real members
  from `knowledge/variables/`; author the 3 fixtures to match the structure
  *with seeded known defects*; keep the known-answer key separate; log
  materialization/extraction errors (e.g. the `edu`/`MOD-DEM` discrepancy)
  into the content-error log.
- **Phase 3 — Live operator run:** reviewer + approver against a disposable
  repo + Connect staging; execute the protocol; populate friction, content
  error, and defect logs; exercise both rubric layers and the 30 -> 40
  promotion gate.
- **Phase 4 — Measure, simplify, finalize:** aggregate logs (error/defect
  rates, catch rate vs. the known-answer key, friction-by-step); apply the
  friction decision rule to simplify; finalize the rubric acceptance criteria
  from run evidence.

Governance escalations (do not block the plan; raise in parallel):

- **Roadmap inconsistency:** `roadmap.json` marks `extract-non-welfare-variables`
  ("Extract all non-welfare variables into `extraction/20_drafts/`") as `done`,
  but `extraction/20_drafts/` is empty and the calibration doc says the
  extraction milestone has not produced drafts. Reconcile the status and
  determine where extracted drafts went.
- **Module question (`/cg-strategy`):** is there a `MOD-EDU`, or do education
  variables belong to `MOD-DEM` per the guidelines' Demography section? The
  empty `knowledge/variables/edu/` and the dashboard's `edu` filter suggest
  an intended `MOD-EDU` that the approved artifacts (all `MOD-DEM`)
  contradict. Resolve before scaling; until then `module_id` is authoritative.
- **Milestone boundary:** Phase 0 app fixes arguably belong to the
  `human-review-application` milestone (marked `done` but not live-capable),
  not `calibrate-human-review`. Record that calibration is paying down the
  predecessor's unfinished debt. The `human-review-application` milestone
  objective wording (asserts PRs are already authoritative) was already
  flagged by the predecessor for `/cg-strategy`.
- **Lifecycle note:** copying approved `knowledge/` content back into
  `extraction/20_drafts/` as calibration "drafts" is a pragmatic workaround,
  not the normal `source -> draft -> review -> approved -> knowledge` flow;
  document it as such so it is not mistaken for real agent extraction output.
