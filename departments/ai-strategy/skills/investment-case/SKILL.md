---
name: investment-case
description: Builds the funding case for the AI programme as a whole across the Adopt, Build and Scale journeys - investment options, full cost of ownership by category, benefit ranges tied to strategic outcomes, staged funding tranches released at evidence gates and the funding model. Use when leaders must decide how much to invest in AI overall, when a budget round needs a programme request, or when funding was approved for licences alone.
license: CC-BY-4.0
metadata:
  department: ai-strategy
  lifecycle: Envision, Mobilise, Scale
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-copilot-studio-guidance, ms-foundry-models, ms-coe-starter-kit
  status: draft
  authors: Simon Foote
---

# Investment case

## Purpose

This skill builds the case for funding the AI programme as a whole: what the organisation will spend across adoption,
building and scaling, what it can reasonably expect in return, and how money is released as evidence arrives. It puts
the full cost of ownership in front of decision-makers, including the people, knowledge and governance work that
licences alone never cover. Investment cases usually go wrong by presenting a licence count as the programme, by
promising precise savings nobody can later find, or by asking for everything up front so that there is no point at
which the organisation can stop.

## When to use

- Leaders must decide how much to invest in AI over the next one to three years.
- The annual budget round needs a programme-level request rather than a collection of project bids.
- Funding was approved for licences, and the adoption, knowledge and governance work behind them is unfunded.
- The programme is moving from adoption into building or scaling and needs a further tranche.
- Finance asks how the AI programme will be funded, charged and reviewed.

## When not to use

- Writing the case for one significant initiative, such as a single agent or engineered solution - use `opportunity-management:business-case`.
- Building the detailed return-on-investment model and its assumptions - use `value-realisation:roi-model`.
- Quantifying cashable and non-cashable benefits with finance - use `value-realisation:financial-benefits`.
- Tracking the approved budget and consumption during delivery - use `programme-management:budget-and-capacity`.
- Answering licensing and capacity questions - use `platform-governance:ai-licensing-and-capacity`, which routes to the licensing guide or a partner.

## Questions to ask first

1. Which strategic outcomes and ambition level is the investment meant to deliver, and over what horizon?
2. What is already funded (licences, platforms, people), and what has been assumed to be free?
3. How does finance prefer to see investment cases here: options, payback, net value ranges, or a fixed format?
4. At what points would leaders want the chance to stop, slow down or accelerate?
5. Will costs be held centrally, charged to business units, or a mix, and who owns consumption costs?

## Required inputs

- The vision, ambition level and strategic outcomes from `ai-strategy:ai-vision` and `ai-strategy:strategic-outcomes`.
- The roadmap from `ai-strategy:ai-roadmap`, or at least its first horizon.
- The maturity assessment, to judge how much foundation work is needed.
- Current costs and commitments from finance and IT, and any licensing position confirmed by the licensing guide or a partner.
- The organisation's investment appraisal rules and discount or hurdle conventions, if any.

Every price, licence cost and consumption estimate comes from the organisation's own quotes, agreements or a licensing
partner, and is marked "to confirm" until it does. Never insert a list price or a benefit figure from memory.

## Decision framework

Present three or four options, each a coherent programme rather than a cut-down budget line.

| Option | Typical shape | Choose it when |
|---|---|---|
| Do minimum | Safe everyday use of what is already licensed, basic governance, no build | Maturity is low or appetite is uncertain; it is also the honest comparator |
| Adopt-led | Structured adoption, Champions, knowledge readiness, a few owned agents | Outcomes depend mainly on everyday use and the organisation is an explorer or adopter |
| Adopt and build | Adoption plus a CoE delivering agents, automations and selected engineered solutions | Outcomes need owned solutions and the operating model can support them |
| Scale | Federated delivery, engineered solutions on Foundry, enterprise governance | Builder or scaler maturity with evidence from earlier tranches |

For each option, cost every category below, even where the answer is zero, so omissions are visible.

| Cost category | What it covers |
|---|---|
| Licences and subscriptions | Per-user and capacity commitments, confirmed with a licensing partner |
| Consumption | Metered usage of agents, models and platforms, with a range and an owner |
| People | Programme, CoE, adoption, Champions time, knowledge owners, makers and engineers |
| Partners | External delivery, assurance and specialist support |
| Knowledge and data | Clean-up, ownership, classification and readiness work |
| Governance and assurance | Reviewer capacity, monitoring, evaluation and tooling |
| Learning and change | Training, communications and manager enablement |
| Run and support | Owners, support model, review cycles and retirement of solutions |

Release funding in tranches tied to evidence gates. Each tranche names the evidence that unlocks the next: adoption at
team level, a benefit measured against baseline, a governance capability in place, or a scale-or-stop decision.

## Practitioner approach

Start from the outcomes and ambition, not from a licence quote. Ask what the programme must achieve and then cost what
it takes to achieve it. A case built bottom-up from licences answers the wrong question and leaves the work that
creates value unfunded.

Build the do-minimum option honestly. It is rarely zero: staff already have access to some AI capability, and doing
nothing about governance, knowledge or acceptable use carries cost and risk. The do-minimum option is the baseline every
other option is compared with, and it often reveals that some spending is unavoidable.

Cost people first. Programme and CoE roles, Champions' time, business owners and knowledge owners are the largest and
most often omitted costs. Express them as time from named roles or capacity, agreed with the managers who must release
it. Then add licences, consumption, partners and run costs. For consumption, give a range with the assumptions behind
it and name who watches it; metered costs surprise organisations that treat them as fixed.

Express benefits as ranges linked to outcomes. Draw them from value hypotheses for known initiatives and from
comparable internal evidence, not from vendor or analyst headlines. Separate cashable from non-cashable benefits and
agree the treatment with finance through `value-realisation:financial-benefits`. Say plainly which benefits are
assumptions until pilots produce evidence.

Design the tranches. The first tranche funds foundations and early evidence; later tranches are released when the
named evidence appears. This gives leaders genuine decision points and protects the programme from all-or-nothing
judgements at the first difficult quarter. Agree who decides each release, normally the executive sponsor at steering.

Agree the funding model with finance: central funding for foundations and governance, business-unit funding for
solutions they own, and a clear owner for consumption. Hidden cross-subsidy creates resentment later.

Write the case on the `investment-case` template. Lead with the recommendation and the decision requested, then
options, costs, benefits, risks, tranches and funding model. Test it with finance before it reaches the sponsor, and
let the sponsor present it.

## Outputs

- An investment case on the `investment-case` template: decision requested, options compared, full cost of ownership by category, benefit ranges by outcome, risks, tranches with release evidence, funding model and owners.
- A list of assumptions marked "to confirm", each with an owner and date.
- A one-page summary for the sponsor to present.

## Microsoft platform considerations

Platform choice drives cost shape. Per-user licences, capacity commitments and metered consumption behave very
differently as use grows, and engineered solutions on Foundry carry model and hosting costs that scale with demand.
Licensing terms, prices and entitlements change often and depend on agreements; never state them, and route every
licensing question to the Microsoft licensing guide or a licensing partner. Check platform capability assumptions
against `references/sources.md`.

## Adoption considerations

Investment in licences without investment in adoption is the commonest reason AI programmes disappoint. Make the
adoption and change costs explicit in every option, sized with the adoption lead, and show what happens to expected
benefits if they are cut.

## Knowledge considerations

Knowledge readiness is a real cost: owners' time, clean-up and ongoing review. Include it in every option that builds
agents, and size it with the knowledge manager rather than assuming existing content is ready.

## Security and privacy considerations

Include the cost of the security and privacy controls the roadmap needs, such as reviewer capacity, labelling and
monitoring. The security lead and data protection officer confirm the scope; this skill does not decide which controls
are required.

## Responsible AI considerations

Fund responsible AI review and evaluation capacity in proportion to the higher-tier work in each option. An option that
includes tier 3 or tier 4 solutions without funded review capacity is not a viable option and should be presented as
such.

## Evaluation requirements

Fund evaluation capacity (test sets, evaluation effort, tooling) for every option that builds agents or engineered
solutions. The case itself is checked by finance for internal consistency and by the sponsor against the outcomes.

## Value measures

The case states, per outcome, the measure, baseline or baseline plan, expected range and benefit owner, and when each
will be reported. The benefits realisation lead owns tracking against the case. Measures are at organisation, unit or
team level, never individual.

## Scale notes

### Starter

A short case, often two options (do minimum and adopt-led), one tranche with a six-month review, and costs dominated by
people time. Finance may accept a two-page paper.

### Scale

Three or four options, two or three tranches, and a funding model that separates central foundations from
business-unit solutions. Reviewed at each roadmap horizon.

### Enterprise

A portfolio-level case with business-unit sub-cases on the same template, consumption owners per unit, and tranches
aligned with the enterprise planning cycle. The board approves the envelope; the sponsor forum releases tranches.

## Hand-offs

- To `value-realisation:roi-model` to build the detailed return model behind the benefit ranges.
- To `programme-management:budget-and-capacity` to track the approved budget and consumption.
- To `opportunity-management:business-case` for initiatives large enough to need their own case inside the envelope.
- To `ai-strategy:strategy-refresh` to revisit the case against evidence at each tranche gate.

## Reviewer gates

Not applicable. The investment case is a funding decision, not a release. Finance reviews it for consistency, and
reviewer departments are consulted only to confirm the assurance capacity each option needs.

## Failure modes

- The case is a licence quote with a productivity multiplier, and the people and knowledge work is never funded.
- Benefits are stated as precise savings, finance cannot find them a year later, and credibility is lost for the next round.
- Everything is requested up front, so the first poor quarter becomes a vote on the whole programme.
- Consumption costs are treated as fixed and exceed expectations once agents are widely used.
- Licensing assumptions are taken from memory and turn out to be wrong after approval.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- State a licence price, entitlement or licensing conclusion; route it to the Microsoft licensing guide or a licensing partner.
- Present benefit assumptions as measured results, or use vendor or analyst headline figures as the organisation's benefits.
- Omit people, knowledge, governance or run costs because they are hard to estimate.
- Ask for the whole investment without staged release points where leaders can stop or change course.
