---
name: financial-benefits
description: Quantifies the financial benefits of AI work with the finance function, classifying each as cashable, non-cashable, cost avoidance or revenue, agreeing the valuation method, evidence and budget line, and keeping released time apart from cash until a decision redeploys or removes cost. Use when a case or CFO needs money figures, when hours saved are being multiplied into savings, or when benefits must be banked in budgets.
license: CC-BY-4.0
metadata:
  department: value-realisation
  lifecycle: Envision, Mobilise, Measure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# Financial benefits

## Purpose

Finance teams are rightly sceptical of AI savings that never show up in a budget. This skill quantifies financial
benefits with finance rather than for it: it classifies each benefit by how it reaches the accounts, agrees a valuation
method and evidence standard for each class, and identifies the budget line where a cashable benefit will land. It
goes wrong when released hours are multiplied by salary and called savings, when cost avoidance is counted as cash,
and when benefits are banked before the decisions that would release them have been taken.

## When to use

- A business case, investment case or renewal needs financial benefit figures.
- Someone has converted hours saved into a savings figure and finance has challenged it.
- Benefits need to be reflected in budgets, headcount plans or supplier contracts.
- A portfolio needs consistent financial treatment of benefits across business units.
- The finance function asks how AI benefits will be evidenced at year end.

## When not to use

- Building the return-on-investment model that combines costs and benefits - use `value-realisation:roi-model`.
- Writing the funding case for the whole programme - use `ai-strategy:investment-case`.
- Measuring the time released in the first place - use `value-realisation:productivity-measurement`.
- Evidencing benefits that should not be forced into money - use `value-realisation:non-financial-benefits`.
- Planning and tracking the programme's own budget and consumption costs - use `programme-management:budget-and-capacity`.

## Questions to ask first

1. Which finance role will agree the classification and valuation, and what are the organisation's existing rules for benefits?
2. For each benefit, what specific cost will fall, what cost will be avoided, or what revenue will rise, and in which budget?
3. What decision is needed to turn released time into cash (vacancies not filled, contracts reduced, overtime cut), and who takes it?
4. What evidence will finance accept at year end for each class of benefit?
5. Over what period, and from what date, will the benefit be counted?

## Required inputs

- Registered benefit statements with measured or expected effects, from `value-realisation:benefit-hypothesis`.
- Measured productivity or quality results, where available, from `value-realisation:productivity-measurement` and `value-realisation:quality-measurement`.
- The organisation's finance rules for benefits, standard cost rates and planning cycle, from the finance function.
- Relevant budget lines and their holders.

Where the organisation has no standard cost rates or benefit rules, agree provisional ones with finance and record them
as `[To confirm]`. Never use published salary averages or vendor value calculators as the organisation's rates.

## Decision framework

Classify every financial benefit before valuing it. The class decides the evidence and whether it may be banked.

| Class | Meaning | Evidence finance usually needs | Can be banked in budget? |
|---|---|---|---|
| Cashable | A cost line falls (agency spend, overtime, external services, licences retired) | Budget reduction or contract change actually made | Yes, once the decision is taken |
| Non-cashable efficiency | Effort released and redeployed to other valued work | Redeployment record and outcome of the redeployed work | No - report as value, not saving |
| Cost avoidance | A future cost is not incurred (growth absorbed without recruitment, penalty avoided) | Documented counterfactual agreed in advance | No - report separately with method |
| Revenue | Income rises or is protected (faster quotes, better conversion, retained customers) | Attributable change in revenue measure, with confounders named | Sometimes, by agreement |

Rules that apply to all classes:

| Rule | Requirement |
|---|---|
| Net | Benefits are stated net of dis-benefits such as review effort and run cost |
| Range | Figures are ranges with the method and confidence stated |
| Owner | Each financial benefit has a business owner and a finance contact (roles) |
| No double count | Released time is valued once, in one class, against one initiative |

## Practitioner approach

Meet finance early, before any figure is written. Ask how the organisation already treats benefits from change
programmes, what standard rates it uses, and what it will accept as evidence. Working within existing rules is faster
and more credible than inventing an AI-specific method, and it makes finance a co-owner of the figures instead of their
auditor.

Classify before valuing. Take each benefit and ask where it would appear in the accounts. Most AI productivity benefits
are non-cashable: people do more or better work in the same hours. That is genuine value, but it is not a saving, and
calling it one is the fastest way to lose finance's trust. A benefit becomes cashable only when a decision changes a
cost line: a vacancy is not refilled, agency use stops, a contract is reduced, a tool is retired. Name that decision,
its owner and its date.

Value each class with the method finance agrees. For non-cashable efficiency, the value of redeployed time is usually
the cost of the time, but only once the redeployment is evidenced. For cost avoidance, write the counterfactual in
advance ("without this, the team would have needed two more people to absorb forecast growth") and get finance and the
owner to agree it before the period starts; counterfactuals written afterwards are not credible. For revenue, use the
business's existing revenue measures and name the other things that move them.

State figures net and as ranges. Subtract review effort, support and the solution's run cost where they fall in the
same budget, or hand them to `value-realisation:roi-model` if costs are modelled there. Give a low, central and high
figure with the method beside it.

Time the benefits. Financial benefits rarely start on launch day. Profile them by quarter, starting when adoption and
the enabling decisions make them possible, and agree with finance when a benefit is banked: in the next budget round,
on contract change, or at year end on evidence.

Keep the human consequences in view. Where a cashable benefit depends on reducing roles, the decision belongs to the
organisation's leadership and HR, with its own consultation and legal obligations. This skill records the dependency;
it never assumes or recommends job reductions.

Finally, reconcile at portfolio level so that the same released hours or avoided cost are not claimed by several
initiatives, and report cashable, non-cashable, cost avoidance and revenue as separate totals, never as one number.

## Outputs

- A financial benefits schedule per initiative, recorded in the `benefits-register`: class, valuation method, range, timing profile, evidence standard, owner and finance contact.
- A decision log of the cost-changing decisions that cashable benefits depend on, with owners and dates.
- Agreed counterfactuals for cost avoidance benefits, signed off before the measurement period.
- A portfolio summary reporting each class as a separate total.

## Microsoft platform considerations

Licence and consumption costs belong in the cost side of the return model, not here, and licence retirements count as
cashable only where the organisation's agreements allow them. Do not state licence prices, terms or entitlements; route
those questions to `platform-governance:ai-licensing-and-capacity`, the Microsoft licensing guide or a licensing partner.

## Adoption considerations

Financial benefits from AI usually depend on broad, sustained adoption of specific scenarios. Record the adoption level
each figure assumes so the realisation plan can warn when adoption falls short.

## Knowledge considerations

Not applicable as a valuation input, because financial classification depends on cost lines rather than content.
Knowledge dependencies sit with the benefit statement and its realisation plan.

## Security and privacy considerations

Cost and staffing data used to value benefits can be sensitive. Use standard rates rather than individual salaries,
share figures at team or function level, and keep supporting finance data with the finance function.

## Responsible AI considerations

Where cashable benefits depend on workforce change, ensure leadership has considered the impact on people through
`change-and-communications:people-change-impact`, and that communications do not frame AI adoption as a reduction
programme without that decision having been taken openly.

## Evaluation requirements

Financial value from quality improvements depends on the quality being real. Before valuing fewer errors or less rework,
check that the result is evidenced by `value-realisation:quality-measurement`, not inferred from release testing.

## Value measures

Success is the share of financial benefit figures that finance has agreed by class and method, and the proportion of
cashable benefits that are actually banked on schedule, tracked by the Benefits Realisation Lead with the finance
contact.

## Scale notes

### Starter

Classify the two or three main benefits with the finance lead in one meeting, use the organisation's standard rates,
and report non-cashable value and any cashable saving separately.

### Scale

A financial benefits schedule for every initiative above a size threshold finance sets, counterfactuals agreed in
advance, and quarterly reconciliation with budget holders.

### Enterprise

A finance-owned benefits policy for AI, portfolio-level reconciliation across business units, and benefits reflected in
planning and budget cycles.

## Hand-offs

- To `value-realisation:roi-model` with the classified and valued benefits.
- To `value-realisation:benefit-owner` for the cost-changing decisions the owner must take.
- To `value-realisation:value-dashboard` for reporting by class.
- To `opportunity-management:business-case` or `ai-strategy:investment-case` where figures support a funding decision.

## Reviewer gates

Not applicable, because financial classification is agreed with the finance function rather than passed through a
reviewer-class gate. The finance contact's agreement, recorded in the register, is the control. Where benefits depend
on workforce change, `responsible-ai` may be consulted through the impact assessment for the solution.

## Failure modes

- Survey hours are multiplied by salary and presented as savings, and every later figure is distrusted.
- Cost avoidance is reported as cash, and budget holders are asked to give up money that was never in their budget.
- A cashable benefit depends on a decision nobody takes, so it is banked in the plan and missed in the accounts.
- The same released time is valued by three initiatives, and the portfolio total is impossible.
- Benefits are framed as job cuts before leadership has decided anything, and adoption stalls through fear.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Present non-cashable efficiency or cost avoidance as cash savings.
- Use vendor value calculators or published averages as the organisation's rates.
- Assume, recommend or announce role reductions as a benefit.
- State licence prices, entitlements or terms.
- Report financial benefits as a single combined number without their classes.
