# What we are building and why

## The problem

The GMD harmonization guidelines are written for human consultants. Every
new harmonizer reads the same long document, interprets it in their own
way, and produces code that works but is never quite identical to what
someone else would have written. The AI system we are building has the same
problem: if we feed it the full guidelines document, it will interpret them
differently each time.

## The solution: Canonical Variable Schema (CVS)

The CVS is a structured reference card for each GMD variable. It contains
the same rules that are in the guidelines, reorganized into a format that
is unambiguous for both the AI agent and human reviewers. One file per
variable. One file per decision rule. Nothing left to interpretation.

## Where the CVS fits in the pipeline

The system works in three steps:

1. **Read the survey.** The system extracts variable information from a raw
   household survey questionnaire (PDF) and produces a structured survey profile.

2. **Apply the GMD rules (this is the CVS).** The system reads the CVS to
   understand what each GMD variable requires and how to construct it.

3. **Draft a harmonization decision.** The system combines steps 1 and 2 to
   propose how to map the raw survey variable to the GMD standard. A GPID
   economist reviews and approves this proposal before any code runs.

The CVS is the fixed anchor. If the rules it contains are correct, the AI
drafts will be correct. This is why we need your review before building
anything further.

## Building on Laura's work

Laura explored a similar approach earlier this year in a pilot repository
that examined how to structure GMD variable knowledge for AI consumption.
Her pilot introduced several ideas that are now core to this design:
separating decision rules from variable definitions, using structured
metadata alongside plain-language guidance, and treating exceptions as
first-class records. The CVS extends her work by connecting the knowledge
base to the full harmonization pipeline and adding the fields the AI agent
needs to operate reliably.
