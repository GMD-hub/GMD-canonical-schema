---
# ================================================================
# DECISION RULE — GMD Canonical Variable Schema v0.1
# ================================================================

rule_id: RULE-EDU-002
rule_name: "educat4 derivation order and recode"
scope: module
module_id: MOD-DEM
applies_to_variables:
  - VAR-educat4
priority: 80
version: "0.1"
status: draft
authority: "GPID Team"
effective_from: "2026-06-25"
effective_to: null
---

## Plain language rule

Always attempt to derive `educat4` from `educat7` first. If `educat7` is
not available, derive from `educat5`. Only map directly from raw survey data
when neither `educat7` nor `educat5` can be defined. Never guestimate.

## Formal IF/THEN

```
IF   educat7 is defined for this survey
THEN derive educat4 using:
     recode educat7 (1=1) (2 3=2) (4 5=3) (6 7=4), gen(educat4)

ELSE IF   educat5 is defined for this survey
THEN      derive educat4 using:
          recode educat5 (1=1) (2=2) (3 4=3) (5=4), gen(educat4)
          document use of educat5 path in do-file notes
          note: this recode is a derived convention, not stated verbatim
                in the GMD guidelines

ELSE IF   neither educat7 nor educat5 is defined
THEN      map raw survey categories directly to the four groups:
            1 = No education
            2 = Primary (complete or incomplete)
            3 = Secondary (complete or incomplete)
            4 = Tertiary (complete or incomplete)
          educat4 is behaving as an atomic variable for this survey
          document direct mapping in do-file notes and Harmonization Spec
          escalate to TTL before finalizing

ELSE IF   no education information available in this survey
THEN      set educat4 = .c for all individuals
```

## Prohibitions

- Do not skip path 1 (educat7) without confirming it cannot be constructed.
- Do not guestimate categories when the raw survey is ambiguous. Use `.b`
  and escalate to TTL.
- Do not combine categories differently from the recode commands above. The
  groupings are fixed GMD standards and must not vary by survey.

## Rationale

Deriving `educat4` from `educat7` first ensures internal consistency across
all education variables. A dataset where `educat4` was built by a different
path than `educat7` would produce contradictory education profiles for the
same individuals. The fixed derivation order prevents this.

## Test examples

| Situation | Action |
|---|---|
| educat7 defined, all 7 groups present | Use path 1 recode exactly as stated |
| educat7 defined but only 4 groups | Use path 1; missing groups become .b |
| educat7 not possible, educat5 defined | Use path 2; document in do-file notes |
| Neither educat7 nor educat5 possible | Use path 3; escalate to TTL |
| No education data in survey | educat4 = .c for all |

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-06-25 | 0.1     | Initial draft | GPID Team  |
