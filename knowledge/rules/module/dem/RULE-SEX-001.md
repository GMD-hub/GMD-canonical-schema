---
# ================================================================
# DECISION RULE — GMD Canonical Variable Schema v0.1
# ================================================================

rule_id: RULE-SEX-001
rule_name: "Binary sex mapping and exclusion of non-standard codes"
scope: module
module_id: MOD-DEM
applies_to_variables:
  - VAR-male
priority: 90
version: "0.1"
status: draft
authority: "GPID Team"
effective_from: "2026-06-25"
effective_to: null
---

## Plain language rule

Map the raw sex variable to 1 (male) or 0 (female). Exclude all numeric
placeholder codes. Preserve non-binary or ambiguous categories as `.o`
rather than forcing them into a binary value. Never impute sex from any
other variable.

## Formal IF/THEN

```
IF   raw sex variable clearly indicates "male" (or local language equivalent)
THEN set male = 1

ELSE IF   raw sex variable clearly indicates "female" (or local equivalent)
THEN      set male = 0

ELSE IF   raw sex variable is a numeric placeholder (e.g., 98, 99, 9)
THEN      set male = .a

ELSE IF   raw sex variable contains a non-binary or ambiguous category
          (e.g., "other", "unspecified", "non-binary", "prefer not to say")
THEN      set male = .o
          document raw code, label, and frequency in do-file notes

ELSE IF   sex was not collected in this survey
THEN      set male = .c

ELSE IF   raw variable is present but cannot be mapped to male or female
          under any reasonable interpretation
THEN      set male = .b
          escalate to TTL before proceeding
```

## Prohibitions

- Do not impute sex from any other variable (name, relationship, age, etc.).
- Do not assign 1 or 0 to non-binary or ambiguous categories.
- Do not drop individuals because sex is missing. Retain with missing code.
- Do not use standard Stata missing (`.`) in place of an extended code.

## Rationale

The binary structure of `male` reflects the GMD standard for global
comparability. Non-binary responses are preserved as `.o` rather than forced
into 1 or 0, so that the do-file notes capture any departure from the binary
assumption. This protects future harmonizers from inheriting a silent coding
decision they cannot audit.

## Test examples

| Raw value | Label in raw data       | Correct output                       |
|-----------|-------------------------|--------------------------------------|
| 1         | Male                    | male = 1                             |
| 2         | Female                  | male = 0                             |
| 98        | Not applicable          | male = .a                            |
| 3         | Other                   | male = .o, document in do-file notes |
| —         | Variable not in survey  | male = .c                            |
| —         | Present but unresolvable| male = .b, escalate to TTL           |

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-06-25 | 0.1     | Initial draft | GPID Team  |
