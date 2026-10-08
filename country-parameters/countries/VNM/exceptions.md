---
country_id: CTY-VNM
iso3: VNM
schema_version: '0.2'
status: draft
exceptions: []
---

## Purpose

Country exceptions capture conditional logic that cannot be represented as a
parameter value.

## Example condition (welfare, illustrative)

The following is an illustrative condition example requested for continuity
with prior work. It is provided as documentation only and is not activated in
`exceptions` until the corresponding welfare variable artifact is registered in
`knowledge/variables/`.

```yaml
exception_id: EXC-VNM-900
applies_to_variables:
  - VAR-welfare
condition: "If household area is urban"
action: "Apply welfare deflator factor 0.85"
rationale: "Illustrative policy example for urban adjustment"
```

## Active exceptions

No active VNM exceptions are registered in front matter yet.

## Change log

| Date | Version | Change | Authority |
|---|---|---|---|
| 2026-09-06 | 0.2 | Add VNM exceptions shell and illustrative welfare condition example | GPID Team |
