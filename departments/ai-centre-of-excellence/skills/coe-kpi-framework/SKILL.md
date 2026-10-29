---
name: coe-kpi-framework
description: Builds a KPI framework and scorecard for an AI CoE across adoption, capability, portfolio flow, quality, governance and value, each measure with a baseline, target, source and owner, rolled up into a four-quadrant sponsor dashboard at team level. Use when a sponsor asks how they will know AI is working, when reporting relies on licence counts or hours saved, or when steering needs a scorecard before its first value review.
license: CC-BY-4.0
metadata:
  department: ai-centre-of-excellence
  lifecycle: Measure, Scale, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-copilot-studio-guidance, ms-coe-starter-kit, ms-copilot-privacy
  status: draft
  authors: Simon Foote
---

# CoE KPI framework

## Purpose

Most AI scorecards report what is easy to count: licences assigned, active users, hours "saved" from a survey. None of
those tells a sponsor whether work is better. This skill builds a balanced framework across six families - adoption,
capability, portfolio flow, quality, governance and value - with a baseline, a target, a data source and a business
owner for every measure. It goes wrong when measures have no baseline, when the CoE owns benefits the business should
own, or when usage data drifts into monitoring individuals.

## When to use

- A CoE or working group needs a scorecard before its first value review.
- The sponsor asks how they will know the investment is working.
- Current reporting relies on licence counts, active-user numbers or estimated hours saved alone.
- Business units report AI progress in incompatible ways and the hub needs one framework.
- Renewal or expansion decisions are approaching and evidence is thin.

## When not to use

- Measuring Copilot adoption for a specific launch or audience in detail - use `copilot-adoption:adoption-measurement`.
- Deciding whether a specific solution should scale or stop - use `opportunity-management:scale-or-stop`.
- Measuring Champion capability through evidence - use `champions:evidence-assessment`.
- Benefit realisation planning, financial benefits and ROI models in depth - the `value-realisation` department (planned).
- Setting the strategic outcomes that measures serve - use `ai-strategy:strategic-outcomes`.

## Questions to ask first

1. Which strategic outcomes has the sponsor agreed, and who in the business owns each?
2. What baselines exist today for those outcomes (cycle times, backlogs, error rates, satisfaction), and where do they come from?
3. What usage and adoption data can the organisation lawfully collect, at what aggregation, and above what minimum group size?
4. Who will collect, check and publish the scorecard, and how often?
5. Which decisions will the scorecard inform: renewal, expansion, scale-or-stop, investment?

## Required inputs

- Strategic outcomes with business owners, from `ai-strategy:strategic-outcomes`.
- The CoE charter's outcomes and the operating model's flow.
- An inventory of available data sources, including adoption reporting and the solution register.
- The organisation's position on workplace monitoring and data protection, from the data protection officer or HR.

Where a baseline is missing, record the measure with "baseline to be captured by" and a date; never back-fill a
baseline from memory or a vendor statistic. Mark any measure without an agreed owner `[To confirm]`.

## Decision framework

Select two to four measures per family, at least one leading and one lagging, and reject any measure that fails the tests.

| Family | What it shows | Example measures (choose and adapt) |
|---|---|---|
| Adoption | Whether AI is part of everyday work, by team or role | Share of licensed users active weekly by team; scenarios in regular use per role |
| Capability | Whether people can use AI well and safely | Champions with assessed evidence; staff completing role-based learning; confidence by team |
| Portfolio flow | Whether ideas move to decisions and delivery | Ideas received; median days from intake to decision; share routed to non-AI fixes |
| Quality | Whether solutions work well enough | Evaluation pass rate at release; answer accuracy on the test set over time; support tickets per solution |
| Governance | Whether controls work in proportion | Share of shared solutions with a named owner; tier 2+ released with reviews complete; register currency |
| Value | Whether outcomes improve against baselines | Business outcome measures with a baseline, owned by the business owner |

| Test | Reject the measure if |
|---|---|
| Baseline | No baseline exists and none can be captured |
| Owner | No business or CoE role will own it |
| Decision | No forum will act on it |
| Aggregation | It can only be reported for individuals or groups below the minimum size |
| Vanity | It rises without any change in outcomes (licence counts, prompts sent) |

Licence counts and hours saved may appear as context, never as the only measures of success.

For the sponsor, roll the six families up into a four-quadrant dashboard on one page. Each quadrant shows two or three
measures and their status; the detail stays in the framework.

| Quadrant | Draws on | Typical measures |
|---|---|---|
| Value | Value | Hours released, cost reduction or revenue impact, each with its method stated, shown beside an outcome measure from the work and never alone |
| Adoption | Adoption, capability | Active use by team or role; Champion participation as the share of teams with an active Champion |
| Capability | Portfolio flow, capability | Opportunities submitted and the share reaching a decision; agents and automations delivered with an owner and baseline |
| Governance | Governance, quality | Compliance with the tier controls; reviews completed on schedule; evaluation pass rate at release |

## Practitioner approach

Start at the value end. Take each strategic outcome and ask its business owner what would show it improving: proposal
turnaround time, time to close a service ticket, rework on contract summaries. These are the lagging measures, and the
business owner, not the CoE, is accountable for them. Capture the baseline now, before rollout changes it.

Work backwards to leading measures. Value depends on solutions working (quality), solutions reaching people (portfolio
flow), people using them (adoption) and people being capable (capability), all within controls that hold (governance).
For each family pick the fewest measures that would warn the steering group early. A portfolio flow measure such as
days from intake to decision often predicts frustration months before adoption drops.

Be careful with productivity claims. Self-reported time saved is a perception measure, useful alongside others but
weak on its own. Prefer measures from the work itself, and where a time estimate is used, say how it was gathered.

Settle aggregation and privacy before any data is collected. Usage data is reported by team or role above an agreed
minimum group size; the scorecard never ranks individuals or names low users. Ask the data protection officer and HR to
confirm the position and record it on the scorecard.

Present the result to the sponsor as the four-quadrant dashboard: value, adoption, capability and governance. The
quadrants answer the questions a sponsor actually asks - is it worth it, are people using it, are we getting better at
delivering it, and is it safe - and keep any one number from dominating. Count delivery capability as outcomes, not
volume: opportunities submitted matter only alongside how many reach a decision, and agents delivered only alongside
how many have an owner, a baseline and measured value in the portfolio register. Report Champion participation as
coverage across teams, never as a league table of people.

Where the sponsor asks for return on investment, show the estimate made at intake beside the value achieved, with the
method and confidence of each. A return figure without its baseline and method should not appear on the dashboard.

For each measure write: definition, family, leading or lagging, baseline and date, target and date, data source,
collection frequency, owner and the forum that acts on it. Then build the scorecard: a one-page view grouped by family,
with status against target and a short commentary by the owner.

Agree how the scorecard is used. The value review in `ai-centre-of-excellence:coe-cadence` takes decisions from it;
exceptions go to steering. Review the measure set annually, retiring measures nobody acts on.

Finally, say what the scorecard cannot tell you. It will not prove causation, and early gains in adoption may not yet
show in outcomes. Write that caveat on the scorecard itself so it is not over-read.

## Outputs

- A KPI framework and scorecard on the `coe-kpi-scorecard` template: measures by family with definition, baseline, target, source, frequency, owner and acting forum.
- A one-page sponsor dashboard on the same template, grouping the measures into value, adoption, capability and governance quadrants.
- A baseline capture plan for measures that lack one.
- A recorded data protection and aggregation position for usage data.

## Microsoft platform considerations

Microsoft provides adoption and usage reporting for Copilot and agents, and Power Platform inventory through tools such
as the CoE Starter Kit. What each report contains, its aggregation and its availability change often; check the current
source records in `references/sources.md` and do not promise a report the tenant cannot produce.

## Adoption considerations

Adoption measures are reported by team and role to target support, not to judge people. Share the scorecard with
Champions and team leads so they can act on it.

## Knowledge considerations

Include at least one governance or quality measure on knowledge: the share of knowledge sources used by live agents that
have an owner and a review date within cycle. Until `knowledge-management` exists, the CoE lead tracks this from the register.

## Security and privacy considerations

Usage data is personal data in many cases. Collect only what the scorecard needs, aggregate above the minimum group
size, and keep raw data with its current owner. Confirm the lawful basis with the data protection officer.

## Responsible AI considerations

Avoid measures that create pressure to use AI where it is not appropriate, such as targets for prompts per person.
Include a measure of human review where tier 3 solutions inform decisions about people.

## Evaluation requirements

Quality measures depend on evaluation sets created at release through `m365-agents:agent-testing`. Re-run them on a
schedule so quality is tracked over time, not only at launch.

## Value measures

This skill defines the value measures for the CoE. Its own success is that the value review takes decisions from the
scorecard each cycle and that every value measure has a baseline and a business owner, checked by the CoE lead.

## Scale notes

### Starter

Five or six measures on one page, grouped loosely into the four quadrants and reviewed twice a year: weekly active use by team, two or three outcome measures from
target scenarios, and whether the acceptable-use starter is in place. The full KPI framework is omitted.

### Scale

Two to four measures per family, a quarterly value review, baselines captured before each launch, and team-level
adoption reporting.

### Enterprise

A hub framework with spoke scorecards and dashboards that roll up quadrant by quadrant, portfolio-level value tracking, and links to benefits realisation
through the `value-realisation` department (planned).

## Hand-offs

- To `ai-centre-of-excellence:coe-cadence` for the value review that uses the scorecard.
- To `copilot-adoption:adoption-measurement` for detailed adoption measures.
- To `opportunity-management:scale-or-stop` for solution-level decisions.

## Reviewer gates

Not applicable as a release gate, because the scorecard is a reporting instrument. Where usage data is collected, the
`security-privacy` department should confirm the aggregation and minimum group size before the first report.

## Failure modes

- Licence counts and active users are the only measures, so the scorecard looks green while work is unchanged.
- No baselines are captured before launch, and benefits can never be shown.
- Usage reporting slides into naming individuals, and trust in the programme collapses.
- The CoE reports benefits the business never agreed, and they are dismissed at renewal.
- The value quadrant shows only hours saved, so the dashboard is challenged the first time a finance lead asks how it was calculated.
- Opportunities submitted and agents delivered rise every month while value stays flat, and nobody notices because volume looks like progress.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Report adoption or usage for individuals, or rank people or teams below the minimum group size.
- Use licence counts or hours saved as the only measures of success.
- Invent a baseline or quote a vendor statistic as the organisation's own.
- Make the CoE accountable for business benefits.
