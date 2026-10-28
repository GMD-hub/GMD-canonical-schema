---
# ================================================================
# DECISION RULE — GMD Canonical Variable Schema v0.2
# ================================================================

rule_id: RULE-EDU-002
rule_name: "Education ladder: one level per source variable, placed through the
            national crosswalk, coarser levels derived by fixed recodes"
scope: module
module_id: MOD-DEM
applies_to_variables:
  - VAR-educat7
  - VAR-educat5
  - VAR-educat4
priority: 80
version: "0.2"
status: draft
authority: "GPID Team"
effective_from: "2026-06-25"
effective_to: null
---

## Plain language rule

Decide once, for the survey's source education variable, the most detailed
GMD level it supports: `educat7` if every substantive category of the source
can be placed in exactly one `educat7` category; otherwise `educat5` by the
same test; otherwise `educat4`. Build that level and derive every coarser
level from it with the fixed recodes. Do not build a level finer than the
source supports, and do not build a finer level partially by leaving out the
categories that do not fit it.

Place each source category through the country's education crosswalk
(`PARAM-EDU-LEVEL-CROSSWALK`): source category -> national level
(`country_entry_id`) -> its ISCED level -> the GMD code. Map a category
directly to a GMD code only when no national level matches it, and record
why.

Residual categories (other/specify, don't know, refused, not stated) carry no
education level. They are `.b`, and they do not count when deciding the level
the source supports. Never guestimate.

## Formal IF/THEN

```
/* --- Step 1: place each substantive source category (per category) --- */

FOR each substantive category of the source education variable
  IF   a PARAM-EDU-LEVEL-CROSSWALK row for the survey's ISO3 and year
       matches the category
  THEN place it through that row's isced_level
       (ISCED -> educat7 map in VAR-educat7 correspondence_output)
  ELSE place it directly at the most detailed GMD level that can be
       defended, and record the reason in the Harmonization Specification

residual categories (other/specify, don't know, refused, not stated)
  -> .b at every level; not placed, not counted in step 2

/* --- Step 2: the level the source supports (once per source variable) --- */

/* The recodes are not restated here: each lives in the derived variable's
   correspondence_output (VAR-educat5: from educat7; VAR-educat4: from
   educat7, else from educat5, in that preference order). */

IF   every substantive category is placed in exactly one educat7 category
THEN build educat7
     derive educat5 with the VAR-educat5 recode from educat7
     derive educat4 with the VAR-educat4 recode from educat7

ELSE IF   every substantive category is placed in exactly one educat5
          category
THEN      educat7 is not constructed for this survey (document why)
          build educat5
          derive educat4 with the VAR-educat4 recode from educat5
          document use of the educat5 path in the Harmonization Specification
          note: this recode is a derived convention, not stated verbatim
                in the GMD guidelines (see open question 1)

ELSE IF   every substantive category is placed in exactly one educat4
          category
THEN      educat7 and educat5 are not constructed for this survey
          build educat4 directly:
            1 = No education
            2 = Primary (complete or incomplete)
            3 = Secondary (complete or incomplete)
            4 = Tertiary (complete or incomplete)
          educat4 is behaving as an atomic variable for this survey
          document the direct mapping in the Harmonization Specification
          escalate to TTL before finalizing

ELSE IF   a substantive category cannot be placed even in one educat4
          category
THEN      that category = .b; escalate to TTL

ELSE IF   no education information available in this survey
THEN      set educat7, educat5, educat4 = .c for all individuals
```

## Prohibitions

- Do not skip the educat7 path without confirming it cannot be constructed.
- Do not build a level finer than the source supports. In particular, do not
  build `educat7` while leaving out (as missing) the categories that straddle
  `educat7` groups; the source then supports a coarser level only.
- Do not map a coarser level directly from the raw survey when a finer level
  was built. Always derive it with the recode in the derived variable's
  `correspondence_output`.
- Do not map a category directly to a GMD code when a crosswalk row matches
  it.
- Do not count residual categories (other/specify, don't know, refused, not
  stated) when deciding the level the source supports.
- Do not guestimate categories when the raw survey is ambiguous. Use `.b`
  and escalate to TTL.
- Do not combine categories differently from the recodes in the variable
  records. The groupings are fixed GMD standards and must not vary by survey.

## Rationale

Deriving coarser levels from the finest one built keeps all education
variables internally consistent: a dataset where `educat4` was built by a
different path than `educat7` would produce contradictory education profiles
for the same individuals. The fixed derivation order prevents this.

Deciding the level once per source variable follows the variable records:
`VAR-educat5` "must be derived from educat7 if educat7 was defined ... If
educat7 cannot be defined, educat5 is coded directly ... leave as missing if
all five groups cannot be created", and `VAR-educat7` lists "the raw survey
does not distinguish all seven education levels" as an escalation trigger. A
finer level built with some categories left out would publish a biased
distribution instead.

Routing each category through the national crosswalk makes the placement a
per-country decision, reviewed once (`country_entry_id`, ISCED anchor), rather
than a per-survey judgement. A direct mapping remains possible, but only as a
recorded exception.

Treating residual categories as `.b` follows `RULE-EDU-003` ("Do not set
`educy = 0` for individuals with unknown or missing education. Use `.b`
instead").

## Open questions (GPID Team decision required before promotion)

1. **The educat5 path to educat4 conflicts with the educat7 path.** educat5
   code 3 ("Primary complete but secondary incomplete") covers educat7 codes 3
   (primary complete) and 4 (incomplete secondary), which `educat4` separates
   (2 = primary, 3 = secondary). The educat5 recode puts the whole of code 3 in
   `educat4` 3, so a primary-complete individual is `educat4` 2 on the educat7
   path and 3 on the educat5 path. By this rule's own test, a source that only
   reaches educat5 does not determine `educat4` for code 3. Should code 3 be
   `.b` on the educat5 path (dropping it from the recode), or does the
   convention stand? The recode is transcribed as currently stated until
   decided.

## Test examples

| Situation | Action |
|---|---|
| Source distinguishes all seven levels; each matches a national level | Place via the crosswalk; build educat7; derive educat5, educat4 |
| Source has "secondary" with no complete/incomplete split | educat7 not constructed; build educat5 if every other category places; derive educat4 |
| One source category is "Other (specify)" | `.b`; does not affect the level the source supports |
| A source category matches no national level | Place it directly; reason recorded in the Harmonization Specification |
| educat7 defined but only 4 groups | Use path 1; missing groups become .b |
| Neither educat7 nor educat5 possible | Build educat4 directly; escalate to TTL |
| No education data in survey | educat7, educat5, educat4 = .c for all |

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-06-25 | 0.1     | Initial draft | GPID Team  |
| 2026-10-27 | 0.2     | Draft: extend from educat4 to the whole ladder (educat7/5/4); level decided once per source variable; categories placed through PARAM-EDU-LEVEL-CROSSWALK, direct mapping only as a recorded exception; residual categories `.b` and not counted; recodes referenced from the variable records instead of restated; open question on the educat5 path | GPID Team (proposed) |
