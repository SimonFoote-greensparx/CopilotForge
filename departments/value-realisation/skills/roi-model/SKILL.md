---
name: roi-model
description: Builds a transparent return-on-investment model for an AI initiative or portfolio - full costs across licences, consumption, build, run, review effort, support and change, benefits by class and timing, low, central and high ranges, sensitivity to key assumptions and an assumptions log. Use when a case or renewal needs a return figure, when an ROI number cannot be traced to its inputs, or when estimated and actual return must be compared.
license: CC-BY-4.0
metadata:
  department: value-realisation
  lifecycle: Envision, Mobilise, Measure, Scale, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-foundry-models, ms-copilot-studio-guidance
  status: draft
  authors: Simon Foote
---

# ROI model

## Purpose

A return figure is only as good as the model behind it, and most AI return figures cannot be traced to anything. This
skill builds a model that anyone can follow: every cost and benefit line with its source, every assumption logged with
an owner, ranges instead of single points, and a sensitivity view showing which assumptions decide the answer. The same
model is reused after launch with actuals, so estimated and achieved return can be compared honestly. It goes wrong
when costs stop at licences, when benefits are gross and front-loaded, and when one optimistic number travels through
the organisation without its caveats.

## When to use

- A business case, investment case or renewal decision needs a return figure.
- An existing ROI number is being quoted and nobody can show how it was calculated.
- A sponsor wants to compare estimated return at approval with the return achieved.
- Several initiatives need comparable return figures for a portfolio decision.
- A scale decision depends on whether return holds at a larger size.

## When not to use

- Classifying and valuing financial benefits with finance - use `value-realisation:financial-benefits`.
- Writing the case document that the model supports - use `opportunity-management:business-case`.
- Building the programme-level funding case - use `ai-strategy:investment-case`.
- Tracking the programme budget and consumption spend - use `programme-management:budget-and-capacity`.
- Answering licensing and capacity questions - use `platform-governance:ai-licensing-and-capacity`.

## Questions to ask first

1. What decision will the model inform, who takes it, and what return would change their mind?
2. Over what period should return be assessed, and does the organisation use a standard appraisal method or discount rate?
3. Which costs are already committed or sunk, and which are incremental to this decision?
4. Which benefits are classified and valued with finance, and which are still estimates?
5. Which two or three assumptions does everyone privately doubt?

## Required inputs

- Classified and valued benefits from `value-realisation:financial-benefits`, with timing profiles.
- Non-financial benefits from `value-realisation:non-financial-benefits`, to be shown beside the return rather than inside it.
- Cost inputs from the organisation's own agreements, quotes and plans: licences, consumption, build effort, support, change and training.
- The organisation's appraisal conventions from finance.

Cost lines for licences and consumption come only from the organisation's own agreements or a licensing partner's
quote. Where a figure is not yet known, enter it as a range marked `[To confirm]` with its owner. Never use list prices
from memory or published averages.

## Decision framework

The model has five parts, and a return figure may be shown only when all five exist.

| Part | Contents |
|---|---|
| Costs | One-off: build, configuration, data and knowledge preparation, testing, change and training. Recurring: licences, consumption, support, monitoring, knowledge upkeep, human review effort, periodic evaluation. |
| Benefits | By class (cashable, non-cashable, cost avoidance, revenue) and by quarter, net of dis-benefits, with adoption ramp applied |
| Ranges | Low, central and high for every material line, with the basis for each |
| Sensitivity | The effect on return of each key assumption moving across its range; the break-even value of the most uncertain ones |
| Assumptions log | Every assumption with source, owner, confidence and the date it will be tested |

| Result | How to present it |
|---|---|
| Return positive across the low case | Robust; state the main risks |
| Positive in central, negative in low | Conditional; name the assumptions that must hold and how they will be tested early |
| Positive only in high | Not supportable on financial grounds; present non-financial case or redesign |
| Depends on cost avoidance or non-cashable value | Show separately from cashable return, and say so in the headline |

## Practitioner approach

Start from the decision. A model for a renewal compares continuing with stopping; a model for a new agent compares
building it with the next best option, which is often doing nothing or using Copilot Chat well. Getting the comparison
right matters more than any formula, and it decides which costs are incremental.

Build costs before benefits, and be thorough. AI costs are routinely understated because the visible line is the
licence. Add the effort to prepare and own knowledge, the time people spend reviewing outputs, the support load, the
cost of periodic evaluation and the change and training effort. Consumption-based services need a usage forecast with a
range, because costs grow with success. Take every rate and price from the organisation's own agreements or a
licensing partner, never from memory.

Bring benefits in as finance agreed them, net of dis-benefits, and apply an adoption ramp. Benefits seldom arrive at
full level on launch day; a realistic curve over several quarters, tied to the adoption assumptions in the benefit
statements, changes the answer more than most people expect. Keep cashable, non-cashable, cost avoidance and revenue on
separate lines so the headline can say what kind of return it is.

Use ranges for every material line, and then run the sensitivity. Move each key assumption across its range and see
which ones flip the answer. Calculate break-even values for the most doubtful ones: "the case holds as long as at least
this share of the target teams use the scenario weekly". Break-even framing helps sponsors judge risk better than a
single percentage return.

Keep an assumptions log as the spine of the model. Each assumption has a source, an owner, a confidence level and a
date when it will be tested against reality, which then becomes a measurement point in the realisation plan.

Present simply. Lead with the decision, the central return, the low case and the two assumptions that matter most.
Show non-financial benefits beside the return, in their own units. Never let a return figure travel without its range,
its class and its date.

After launch, keep the same structure and replace estimates with actuals at each review. The comparison of estimated
and actual return, line by line, is the most valuable output of the whole exercise, because it teaches the
organisation how to estimate the next case.

## Outputs

- An ROI model with costs, benefits, ranges, sensitivity and assumptions log, in the organisation's spreadsheet or modelling tool.
- A one-page return summary: decision, central and low return, break-even values, key assumptions and non-financial benefits beside it.
- Assumption test dates handed to the `benefits-register` as measurement points.
- An estimated-versus-actual comparison at each post-implementation review, recorded in the `post-implementation-review-report`.

## Microsoft platform considerations

Licensing models and consumption-based charges for Copilot, agents, Copilot Studio and Microsoft Foundry differ and
change. Model them as separate cost lines with the charging basis the organisation's agreement actually uses, take
figures from the organisation's agreements or a licensing partner, and check `references/sources.md` before describing
how any product is charged. Never state prices or licensing conclusions.

## Adoption considerations

The adoption ramp is usually the most sensitive assumption in an AI return model. Make it explicit, tie it to the
adoption plan, and test it early using `value-realisation:adoption-to-value-metrics`.

## Knowledge considerations

Knowledge preparation and upkeep are real recurring costs for any grounded solution. Include the owner time needed to
keep sources current; leaving it out makes agents look cheaper than they are and starves their knowledge later.

## Security and privacy considerations

Include the cost of required security and privacy controls and reviews in the model. Commercial terms in the model may
be confidential; share the summary widely and the full model only with those who need it.

## Responsible AI considerations

Include the cost of human oversight for solutions that inform decisions about people, and never improve a return by
assuming oversight will be reduced. Return figures must not create pressure to deploy AI where review has said it is
not appropriate.

## Evaluation requirements

Include the recurring cost of evaluation and regression testing. Where benefits depend on output quality, link the
assumption to the quality threshold agreed at release so the model and the evaluation are consistent.

## Value measures

Success is the share of return figures in circulation that can be traced to a model with all five parts, and the gap
between estimated and actual return narrowing over successive cases, tracked by the Benefits Realisation Lead.

## Scale notes

### Starter

A simple spreadsheet with incremental costs, benefits as finance agreed them, low and central cases and five or six
logged assumptions. Use a partner's support for anything involving consumption-based services at volume.

### Scale

A standard model structure for every case above a threshold finance sets, sensitivity and break-even analysis, and
estimated-versus-actual comparison at every review.

### Enterprise

A portfolio model that aggregates initiatives without double counting, shared cost rates and adoption curves, and
calibration of future estimates from the history of past cases.

## Hand-offs

- To `opportunity-management:business-case` or `ai-strategy:investment-case` with the return summary.
- To `value-realisation:benefit-realisation-plan` with assumption test dates.
- To `value-realisation:post-implementation-review` for estimated-versus-actual comparison.
- To `platform-governance:ai-licensing-and-capacity` for any licensing or capacity question raised by the model.

## Reviewer gates

Not applicable, because the model informs a funding or scale decision rather than releasing a solution. The finance
contact agrees conventions and figures. Where a model assumes reduced human oversight, `responsible-ai` must be consulted
before the figure is used.

## Failure modes

- Costs stop at licences, and the run cost of review, knowledge and support appears after approval.
- Benefits start at full level on launch day, and the return is overstated in the first year.
- A single return percentage travels without its range or class, and becomes a commitment nobody made.
- Consumption costs are forecast at pilot volume and grow sharply with adoption.
- Nobody compares estimated with actual return, so the next case repeats the same errors.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Show a return figure without its range, its class of benefit and its assumptions.
- Enter licence prices or consumption rates from memory or published lists.
- Mix cashable return with cost avoidance or non-cashable value in one headline figure.
- Improve the return by assuming human oversight or evaluation will be cut.
