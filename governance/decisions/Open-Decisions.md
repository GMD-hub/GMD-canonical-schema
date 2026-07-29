# Open Decisions, July 2026

| Field | Value |
|---|---|
| Record type | Decision request register |
| Record ID | DEC-2026-07 |
| Created | 2026-07-29 |
| Status | open |
| Authority | GPID Team |
| Source audit | [Gap Audit, July 2026](../audits/Gap-Audit-2026-07.md) |
| Implementation status | No decision-dependent canonical change made |

This record presents governance questions that require GPID Team authority. It
records options and recommendations, but it does not make either decision.
Current `fallback_policy: undecided` values remain unchanged, and country
exceptions do not receive a priority field.

## C1. Fallback policy

Both definitions under `knowledge/parameters/` currently use
`fallback_policy: undecided`. By design, a missing valid country record stops
the affected harmonization path and requires escalation.

### Decision request 1: who sets fallback policy?

| Option | Consequence |
|---|---|
| GPID Team sets one central policy per parameter | The same missing-coverage behavior applies across countries. Review is concentrated in the universal parameter definition, and country economists provide evidence without changing fallback semantics. |
| Country economists set policy per country | Behavior can reflect local evidence and operational context, but reviewers must inspect a larger decision surface. The country model and validator would need a governed way to represent and validate country-specific policy. |

**Recommendation, not a decision:** Set fallback policy centrally per parameter
through GPID Team review. Country economists should supply and review country
records and evidence, while the universal parameter definition should control
what absence means.

### Decision request 2: may construction parameters use a global default?

| Option | Consequence |
|---|---|
| Permit a reviewed global default | Harmonization can continue when country coverage is missing, but one value may conceal material differences in national education systems. Reviewers must establish evidence that the default is valid for the parameter's full scope. |
| Prohibit a global default for construction parameters such as education duration | Missing coverage continues to block the affected construction path. This is operationally slower but avoids converting a proxy or assumption into completed years of education. |
| Decide global-default eligibility separately for each construction parameter | Review can account for the parameter's meaning, but each parameter needs an explicit GPID Team decision and rationale before `use_global_default` is allowed. |

The GMD guidelines prohibit estimating years of education from proxies. A
global education-duration default could create the same practical risk if it
is used without country evidence.

**Recommendation, not a decision:** Do not allow a global default for
`PARAM-EDU-YEARS-BY-LEVEL`. Decide eligibility separately for any future
construction parameter and require explicit source evidence.

## C2. Exception precedence

Universal rules carry priorities from 0 through 100. Country exceptions have
no equivalent field. When a selected country exception and a universal rule
both apply to the same variable and year, the current documentation does not
define their order.

| Option | Reviewability consequence | Validator consequence |
|---|---|---|
| Give exceptions a priority on the same scale as rules | A reviewer can compare all applicable logic in one explicit order, but each exception requires a justified priority and tie handling. | Add a required priority field after migration, validate its range, and define duplicate-priority behavior. Overlap may remain informational when ordering is unambiguous. |
| Apply exceptions after all universal rules | Ordering is simple and country logic acts as a final adjustment, but an exception can obscure which universal result it replaced unless provenance is explicit. | Overlap between exceptions still needs an order or prohibition. Rule-to-exception overlap can be accepted by definition. |
| Apply exceptions before all universal rules | Ordering is simple and universal rules remain the final authority, but later rules may erase the intended country-specific action. | Overlap between exceptions still needs an order or prohibition. Rule-to-exception overlap can be accepted by definition. |
| Prohibit overlapping exceptions entirely | Review is simpler because exception-to-exception ordering never arises, but legitimate layered country conditions must be merged into larger records or split into non-overlapping windows. | Change the B3 overlapping exception report from informational to a structural failure. Rule-to-exception ordering still needs a separate statement. |

**Recommendation, not a decision:** Use an explicit priority on the same scale
as universal rules, with documented tie behavior and provenance showing the
final ordered set. Until the GPID Team decides, keep exception overlap
informational and do not add a priority field to the exception model.

## Decision record template

When GPID Team decides a question, add a dated outcome below the relevant
request. Do not replace the original options or recommendation.

| Field | Value |
|---|---|
| Decision status | `decided`, `closed`, or `superseded` |
| Decision | Pending GPID Team decision |
| Decided on | Pending |
| Decision authority | Pending |
| Source reference | Pending meeting, issue, or approval reference |
| Rationale | Pending |
| Implementation references | Pending |
| Validation references | Pending |

## Related records and implementation evidence

- [Governance Records](../README.md)
- [Gap Audit, July 2026](../audits/Gap-Audit-2026-07.md)
- `wiki/Governance-and-Contributing.md`
- `wiki/Country-Parameter-Layer.md`
- `wiki/Validation-and-Builds.md`
