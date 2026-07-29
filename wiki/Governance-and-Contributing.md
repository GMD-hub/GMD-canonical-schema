# Governance and Contributing

## Read before changing anything

`AGENTS.md` is the binding repository instruction for AI agents. Every agent
must read it completely, then read `knowledge/index.md`. Work involving a
variable requires its specification and referenced rules. Work involving
country content also requires `country-parameters/README.md` and both files in
the relevant country folder.

## Write ownership

| Location | Writer |
|---|---|
| `extraction/20_drafts/` | AI agents |
| `extraction/30_review/` | Humans only |
| `extraction/40_approved/` | Humans only |
| `knowledge/` | Humans only after approval |
| `country-parameters/` | Humans only |
| `schema/` | Humans, or agents under supervision |

Agent-generated canonical artifacts remain in `20_drafts/` until reviewed.
Documentation changes do not authorize changes to governed canonical
artifacts or rule logic.

!!! example "Example: route the change before editing"
	A wording correction in this wiki follows the documentation workflow. A
	proposed new universal fallback policy starts as sourced draft work in
	`extraction/20_drafts/` and requires human approval before promotion. A
	country-specific value belongs in `country-parameters/` and is human-owned.
	The subject may be similar, but ownership follows the destination and the
	semantic effect of the change.

## Changes requiring human approval

- every new or modified file under `knowledge/`;
- every change to rule IF/THEN logic;
- every change to `derived_from` or `derives_to`;
- every addition or modification under `country-parameters/`;
- every change to `AGENTS.md`.

Approval is semantic, not merely technical. Passing Pydantic validation does
not authorize a rule or establish that a country value is true.

| Hypothetical request | Correct route | Why |
|---|---|---|
| Clarify an explanatory paragraph without changing policy | Documentation review | Presentation changes, canon does not |
| Change a rule's IF condition | Draft, human review, approval, promotion | Decision behavior changes |
| Add a sourced country value | Human-owned country layer process | The value is country-specific canon |
| Correct generated JSON | Correct governed source, then rebuild | Runtime output is derivative |

## Drafting principles

1. Use the GMD guidelines as the rule authority.
2. Keep one variable per file and use stable artifact IDs.
3. Separate universal structure from country values and exceptions.
4. Express decision behavior as explicit IF/THEN logic and prohibitions.
5. Preserve source provenance, extraction method, date, and review state.
6. Set unknown values to null and state what evidence is missing.
7. Never guess, silently broaden a rule, or infer a country value.
8. Keep status and review fields truthful.

## Review checklist

- The artifact is in the correct layer and module.
- Every claim is grounded in the authoritative source.
- IDs, references, and derivation links resolve correctly.
- Rule conditions and outcomes are deterministic enough to review.
- Missing values, edge cases, prohibitions, and escalation triggers are clear.
- Country windows use the fieldwork start year and do not overlap.
- Parameter values match the universal value shape.
- Provenance distinguishes verified evidence from placeholders.
- `knowledge/index.md` will remain synchronized after promotion.
- Structural validation and representative compilation succeed.

## Handling conflicts

If the CVS and source guidelines disagree, do not repair the discrepancy by
inventing a compromise. Document the conflict in provenance notes, preserve
the guideline's authority, and escalate to the GPID Team.

If a requested country change would alter universal structure, route it to the
universal CVS approval process. If a universal proposal contains a country
fact, move that fact to the Country Parameter Layer instead.

!!! example "Hypothetical conflict"
	Suppose a draft artifact says to infer a missing education duration, while
	the authoritative guideline prohibits estimation. The reviewer should not
	soften both statements into a compromise. The guideline remains
	authoritative, the discrepancy is documented in provenance, and the issue
	is escalated for a human decision.

## Generated files

`build/output/` contains compiler output. Regenerate bundles after source or
commit changes. Reviews and commits should focus on governed Markdown and
Python validation behavior, not manual edits to generated JSON.

## Suggested reading

- **To see ownership applied stage by stage:** revisit the
	[Artifact Lifecycle](Artifact-Lifecycle.md).
- **To identify sensitive fields and references:** use the
	[Artifact Model](Artifact-Model.md).
- **To separate technical checks from approval:** read
	[Validation and Runtime Bundles](Validation-and-Builds.md).
