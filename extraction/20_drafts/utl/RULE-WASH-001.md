---
# ================================================================
# DECISION RULE — GMD Canonical Variable Schema v0.2
# ================================================================

rule_id: RULE-WASH-001
rule_name: "WASH ladder: source categories placed through the national
            crosswalk; improved status derived from the fine code, or set
            directly for problematic categories"
scope: module
module_id: MOD-UTL
applies_to_variables:
  - VAR-watersource
  - VAR-impwatrec
  - VAR-sanitationsource
  - VAR-impsanrec
priority: 80
version: "0.2"
status: draft
authority: "GPID Team"
effective_from: "2026-10-27"
effective_to: null
---

## Plain language rule

Place each category of the survey's main drinking-water source question (or
sanitation-facility question) through the country's WASH crosswalk
(`PARAM-WASH-WATER-CROSSWALK` / `PARAM-WASH-SANITATION-CROSSWALK`): source
category -> national category (`country_entry_id`) -> its JMP node (`jmp_id`)
-> the `water_source` / `sanitation_source` code that node takes in the
`VAR-watersource` / `VAR-sanitationsource` JMP anchor. Map a category directly
only when no national category matches it, and record why.

When a category is placed at one fine code that determines improved status,
derive the improved indicator from that code with the fixed recode (water:
codes 1-8 improved, 9-14 not improved; sanitation: codes 2, 3, 5, 6, 7
improved, 9-14 not improved). Override the recode for a code only on
documented country evidence.

When a category cannot be placed at such a code (a problematic category: it
spans fine codes with different improved status, has no fine code, or lands on
a code that does not determine improved status), set the improved indicator
directly: 1 if the survey is on file in the SDG calculations and most of the
category was estimated improved at the rural level, otherwise 0; for surveys
not on file, base it on standard international classifications and country
insights, and use 0 where there is no evidence. Document every direct
decision.

Don't know, refused and not stated carry no source or improved status. Never
guestimate.

## Formal IF/THEN

```
/* --- Step 1: place each source category (per category) --- */

FOR each category of the source question
  IF   a national crosswalk row for the survey's ISO3 and year matches it
  THEN take the code(s) the row's jmp_id has in the VAR-watersource /
       VAR-sanitationsource JMP anchor: one fine code, a list (the codes a
       coarse node spans), or none (a node with no fine code)
  ELSE place it directly at the best-matching fine code, or mark it
       problematic; record the reason in the Harmonization Specification

don't know / refused / not stated -> missing; not placed

/* --- Step 2: the fine variable (water_source / sanitation_source) --- */

IF   the category is placed at one fine code
THEN fine variable = that code
ELSE (problematic category)
     OPEN QUESTION 1 below: escalate to TTL; do not guess a fine code

/* --- Step 3: the improved indicator (imp_wat_rec / imp_san_rec) --- */

IF   the category is placed at one fine code that determines improved
     status (present in the VAR-impwatrec / VAR-impsanrec recode map)
THEN improved = recode of that code
     unless documented country evidence supports an override for that code

ELSE IF   the category spans fine codes that all take the same improved
          value in the recode map
THEN      improved = that value

ELSE IF   the row's jmp_id is in the direct path of VAR-impwatrec /
          VAR-impsanrec (a JMP node with no fine code)
THEN      improved = its value there

ELSE IF   the survey is on file in the SDG calculations
THEN      improved = 1 if most of the category was estimated improved at
          the rural level, else 0

ELSE      improved from standard international classifications and country
          insights; 0 where there is no evidence; document the decision
```

## Prohibitions

- Do not map a category directly when a national crosswalk row matches it.
- Do not set the improved indicator independently of the fine code when the
  category was placed at one fine code that determines it, unless documented
  country evidence supports the override.
- Do not apply 0 to a problematic category without documenting that no
  evidence exists.
- Do not guess a fine code for a problematic category.
- Do not code bottled water (`water_source` 7) as unimproved.

## Rationale

The guidelines tie the improved indicators to the fine variables:
`water_source` is "feeding the `piped`, `piped_to_prem`, and `imp_wat_rec`
variables", and `imp_wat_rec` "should equal 1 when `water_source` is 1 through
8 and 0 when it is 9 through 14, unless country evidence supports an
override"; `imp_san_rec` "equals 1 for improved facilities: flush/pour-flush
to sewer, septic tank, or pit latrine; VIP; pit latrine with slab; composting
toilet". Deriving improved status from the fine code keeps the two variables
consistent wherever the fine code is known.

The direct path for problematic categories is the guidelines' construction
note for both improved indicators ("If the survey is on file in the SDG
calculations, set 1 if most of the problematic category was estimated
improved at the rural level, otherwise 0. Otherwise base recommendations on
standard international classifications and relevant country insights; use 0
where there is no evidence").

Routing each category through the national crosswalk makes the placement a
per-country decision, reviewed once (`country_entry_id`, JMP classification),
rather than a per-survey judgement, as for education (`RULE-EDU-002`).

## Open questions (GPID Team decision required before promotion)

1. **Problematic categories and the fine variable.** For education, a source
   category that does not fit the finer level makes the whole source step
   down (`RULE-EDU-002`). Should the same hold here, so that one problematic
   category means `water_source` / `sanitation_source` is not constructed for
   the survey and only the improved indicator is? Or is the fine variable
   constructed for the categories that place, with the problematic ones
   missing? The guidelines say only "referring to the survey questionnaire for
   the best match". In a sample of 15 draft survey links (ECA), the strict
   reading would leave 7 of 8 surveys without `water_source` and 4 of 9 without
   `sanitation_source`.
2. **Coarse codes inside `sanitation_source`.** Codes 1 (a flush toilet) and
   4 (pit latrine) are themselves coarse: their improved status depends on
   detail the code does not carry (where it flushes to; slab or not). Code 8
   (special case) has no improved status in the guidelines. All three are
   therefore absent from the `VAR-impsanrec` recode map, so a category placed
   at them takes `imp_san_rec` directly. Does placing a category at code 1 or 4
   count as reaching the fine level (with improved set directly for it), and
   what does code 8 cover?
3. **"Other (specify)".** Both fine variables have an explicit code 14
   (Other), and the water recode makes 14 not improved (the sanitation map
   follows by analogy). Should a survey's "other" category go to 14 with
   improved 0, or be missing, as residual categories are for education?
4. **Shared facilities.** The guidelines treat sanitation facilities shared
   with other households, or open to the public, as not improved. A recode
   from `sanitation_source` cannot see sharing; the national categories carry
   `shared_flag`. How should sharing enter `imp_san_rec`?

## Test examples

| Situation | Action |
|---|---|
| "Piped into dwelling" matches a national category with jmp_id `tap_water.piped_on_premises.piped_water_into_dwelling` | water_source = 1; imp_wat_rec = 1 (derived) |
| "Bottled water" matches a national category with jmp_id `packaged_water.bottled_water` | water_source = 7; imp_wat_rec = 1 (derived) |
| "Protected well or spring" (jmp_id `ground_water.protected_wells_or_springs`, codes 5 and 6) | water_source: open question 1; imp_wat_rec = 1 (both codes improved) |
| "Spring water, well" (jmp_id `ground_water`) spans protected and unprotected sources | Problematic: imp_wat_rec set directly (SDG estimate, else evidence, else 0, documented); water_source: open question 1 |
| "Flush to pit latrine" (jmp_id `flush_toilets.to_pit`, no sanitation_source code) | imp_san_rec = 1 (VAR-impsanrec direct path); sanitation_source: open questions 1, 2 |
| A category matches no national category | Place it directly; reason recorded in the Harmonization Specification |
| Don't know | Missing in all four variables |

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-10-27 | 0.1     | Initial draft | GPID Team (proposed) |
| 2026-10-28 | 0.2     | Place categories by jmp_id through the VAR JMP anchors; spans with one improved value, and the VAR-impwatrec / VAR-impsanrec direct path, decide improved | GPID Team (proposed) |
