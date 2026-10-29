---
name: foundry-cost-management
description: Estimates, budgets and controls the running cost of a Microsoft Foundry solution - model consumption, reserved capacity, search, storage, compute and monitoring - with cost per outcome, tagging, budgets, alerts and named owners. Use when a Foundry build needs a cost estimate, when consumption spend is rising or unexplained, or when a team is choosing between pay-per-use and reserved capacity.
license: CC-BY-4.0
metadata:
  department: ai-foundry
  lifecycle: Mobilise, Deliver, Measure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: ai-foundry, azure
  edition-support: starter, scale, enterprise
  reviewers: design-authority
  sources: ms-foundry-models
  status: draft
  authors: Simon Foote
---

# Foundry cost management

## Purpose

A Foundry solution is paid for every time it runs, and its cost moves with usage, prompt length, model choice and
design decisions nobody priced. This skill brings financial operations discipline to custom AI: an estimate built from
the solution's own behaviour, a cost per business outcome the owner can judge, tagging so all spend is attributable,
budgets and alerts that reach someone who can act, and a routine of optimisation. Cost management goes wrong when the
estimate is a guess at token counts made before the prompts exist, when shared resources make spend unattributable, and
when the first anyone hears of an overspend is the monthly invoice.

## When to use

- A Foundry solution has been approved and needs a running-cost estimate and budget before build continues.
- Consumption spend is rising, spiking or cannot be explained by usage.
- A team is choosing between pay-per-use deployments, reserved throughput and batch processing.
- A sponsor asks what a solution costs per case, per answer or per user, and whether it still pays back.
- Several Foundry solutions share resources and finance wants spend split by owner.

## When not to use

- Deciding whether the solution is worth building at all - use `ai-foundry:foundry-solution-assessment`.
- Licensing, seat and capacity entitlement questions across Microsoft AI - use `platform-governance:ai-licensing-and-capacity`.
- Programme-level budget and people capacity - use `programme-management:budget-and-capacity`.
- Choosing deployment type, region and capacity for reasons other than cost - use `ai-foundry:foundry-deployment-architecture`.
- Building the return-on-investment model for the benefits case - use `value-realisation:roi-model`.

## Questions to ask first

1. What is the unit of business outcome (a case resolved, a document processed, a question answered), and how many are expected per day at launch and at full use?
2. Which cost-bearing components does the design use: models, reserved capacity, search indexes, storage, compute for tools, monitoring and evaluation runs?
3. Who owns the budget, who receives alerts, and what may they do when a threshold is crossed?
4. Is demand steady, spiky or batch, and does any part of the work tolerate delay?
5. What cost per outcome would make the solution no longer worth running?

## Required inputs

- The solution design on the `foundry-solution-design` template, with the model selection record and deployment choices.
- Measured token use per task from prototype or evaluation runs, not estimates from the specification.
- Volume forecasts from the business owner, with a low, expected and high case.
- The organisation's Azure tagging standard, cost allocation model and budget approval route.

Where measured token use is not yet available, mark the estimate `[To confirm: measured during evaluation]` and give a
range rather than a figure. Never quote unit prices from memory; read them from the current Azure pricing source on the
day and record the date.

## Decision framework

| Decision | Default | Change when |
|---|---|---|
| Consumption model | Pay-per-use while volume is uncertain | Steady, predictable volume makes reserved capacity cheaper at measured utilisation, and someone owns the commitment |
| Real-time or batch | Real-time only where a person or system is waiting | Work tolerates delay; route it to batch processing where the source records show it is offered for the model |
| Model per step | The smallest model that met the evaluation threshold | Evaluation shows a step needs a larger model; never upsize for comfort |
| Context size | Send only what the step needs | Evidence shows quality drops when context is trimmed |
| Caching | Reuse results for repeated identical or near-identical requests where freshness allows | Answers must reflect live data or differ by user permissions |
| Resource sharing | Separate resources or tags per solution | Shared capacity is deliberate and has an agreed allocation key |

| Alert | Threshold to agree | Who acts |
|---|---|---|
| Budget forecast | Forecast exceeds monthly budget | Solution owner |
| Anomaly | Daily spend far above its normal pattern | Engineering on call |
| Cost per outcome | Rises above the agreed ceiling | Business owner and solution owner |

## Practitioner approach

Build the estimate from the design, not from a calculator. List every component that bills, then for each model call
in the solution record its inputs, typical prompt and context size, output size and how many times it runs per business
outcome. Agentic designs multiply calls: a single answer may involve planning, several tool calls and a final
response, each carrying the conversation so far. Measure these on the prototype or evaluation runs and multiply by the
volume range. Add search, storage, compute for hosted tools, monitoring data ingestion and the evaluation runs you will
repeat after every change, which teams routinely forget.

Express the result as cost per outcome as well as cost per month. A monthly figure invites a yes or no; a cost per
resolved case can be set against the value hypothesis and watched as usage grows. Agree with the business owner the
ceiling above which the solution should be redesigned or paused, and record it.

Make spend attributable from the first deployment. Apply the organisation's tags for solution, owner, environment and
cost centre to every resource, keep production and non-production apart, and where capacity is shared, agree the
allocation key in writing before the first invoice. Unattributed AI spend is the commonest reason finance loses
confidence in a programme.

Set budgets and alerts that reach a person with authority to act, and write down what they will do: throttle, switch
to a smaller model, pause a workflow or accept the spend. Pair budget alerts with consumption-rate alerts in
monitoring, because invoices and cost reports lag behind usage. Guard against runaway cost in the design itself with
per-run budgets in agentic workflows, rate limits per caller and quotas per environment.

Review cost monthly with usage and quality side by side. Look first at prompt and context bloat, steps that use a
larger model than they need, repeated identical calls that could be cached, and work that could move to batch. Change
one thing at a time and rerun evaluation, because a cheaper configuration that quietly lowers quality is not a saving.

Reserved capacity is a financial commitment, not a performance setting. Recommend it only when measured, steady usage
shows a saving at realistic utilisation, and when someone owns the commitment and its renewal. Capacity terms, prices
and discounts are volatile; take them from the current source and route commercial questions to the Microsoft
licensing guide, a licensing partner or procurement.

State what the estimate cannot determine: real user behaviour after launch, especially conversation length and retry
patterns, which only production data reveals.

## Outputs

- A cost model in the `foundry-solution-design` template: components, measured units per outcome, volume range, cost per outcome, monthly range, assumptions with dates and sources.
- A budget, alert and response plan naming the owner and action for each threshold.
- A tagging and allocation statement for every resource the solution uses.
- A monthly cost review record with the optimisations tried and their effect on quality.

## Microsoft platform considerations

Foundry costs combine model consumption, which differs by model, provider and deployment type, with the Azure services
around it. Partner and third-party models may be billed differently from models sold by Microsoft, and reserved,
pay-per-use and batch options are not available for every model or region. All of this changes often, so take current
facts from the source records and the Azure pricing pages, and use Azure cost management tooling for budgets, alerts
and allocation. Licensing and commercial terms route to the Microsoft licensing guide or a licensing partner.

## Adoption considerations

Not applicable to most cost work, because users do not see it directly. Where cost controls change what users
experience, such as shorter answers or queued requests, tell them through the solution's release communications.

## Knowledge considerations

Not applicable to cost directly, but grounding design drives context size; large, poorly targeted retrieval results
are a common hidden cost, so share findings with `ai-foundry:retrieval-design`.

## Security and privacy considerations

Cost and usage reports can reveal who used the solution and how much. Report at solution, team or role level only, and
restrict access to any per-caller usage data used for throttling. Denial-of-wallet attacks, where an attacker drives
up consumption, are a security concern; rate limits and authenticated access are the controls.

## Responsible AI considerations

Not applicable in most cases, because cost decisions rarely affect people directly. Where a cost saving reduces
safety filtering, human review or evaluation coverage, it becomes a responsible AI decision and goes to the
`responsible-ai` department before it is made.

## Evaluation requirements

Every cost optimisation that changes a model, prompt, context size or cache is evaluated against the existing
threshold before release, using `ai-foundry:model-evaluation`. Record the quality result next to the saving.

## Value measures

Track cost per outcome against the agreed ceiling and against the value per outcome in the benefits case, owned by the
solution owner with finance. Track the share of spend that is tagged and attributable, aiming for all of it.

## Scale notes

### Starter

Keep one budget per solution with a forecast alert to the owner, use pay-per-use, and review cost monthly alongside
usage. A simple spreadsheet cost model is enough if its assumptions are dated.

### Scale

Standardise tags, budgets and cost-per-outcome reporting across Foundry solutions, and run a shared monthly review
where solution owners compare patterns and reuse optimisations.

### Enterprise

Run AI cost as part of the organisation's financial operations practice, with chargeback or showback by owner,
governed decisions on reserved capacity across solutions, and anomaly detection on consumption.

## Hand-offs

- To `ai-foundry:foundry-deployment-architecture` when cost points to a different deployment type or capacity model.
- To `ai-foundry:model-selection` when a smaller model might do a step.
- To `platform-governance:ai-licensing-and-capacity` for entitlement and commercial questions.
- To `value-realisation:roi-model` with cost per outcome for the benefits case.
- To `ai-operations:ai-solution-monitoring` for consumption-rate alerts.

## Reviewer gates

From risk tier 2, `design-authority` checks that the cost model is complete, that resources are tagged to the
standard and that reserved capacity commitments have an owner. Cost changes that alter safety or review controls also
pass the `responsible-ai` gate.

## Failure modes

- The estimate counts one model call per answer, but the agent makes several with growing context, and spend runs far above budget.
- Resources are shared and untagged, so nobody can say which solution caused a spike.
- Budget alerts go to a shared mailbox nobody reads, and the overspend is found on the invoice.
- Reserved capacity is bought on forecast volume that never arrives.
- A cheaper model is swapped in to save money without re-evaluation, and quality falls unnoticed.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Quote prices, discounts or capacity terms from memory.
- Approve a running cost without a named budget owner and an alert that reaches them.
- Make a cost optimisation that changes model behaviour without re-running evaluation.
- Report usage or cost by named individual.
