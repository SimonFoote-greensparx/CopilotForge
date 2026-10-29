---
name: adoption-to-value-metrics
description: Builds the measurement chain from adoption to benefit - usage, then scenario behaviour, then work outcome, then benefit - choosing leading indicators for their link to a named benefit and diagnosing where the chain breaks, so usage is never reported as value. Use when reports show active users but no outcomes, when a sponsor treats adoption as return, or when early warning is needed before benefits can be measured.
license: CC-BY-4.0
metadata:
  department: value-realisation
  lifecycle: Mobilise, Launch, Measure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-cowork, copilot-studio
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-adoption-hub, ms-copilot-privacy, ms-copilot-studio-guidance
  status: draft
  authors: Simon Foote
---

# Adoption to value metrics

## Purpose

Usage is necessary for value but is not value. This skill links each benefit to the adoption indicators that should
predict it, through the behaviour change and the work outcome in between, so the programme gets early warning while
benefits are still maturing and can see where the chain breaks. It goes wrong when active-user counts are presented as
return, when leading indicators are chosen because they are easy to count rather than because they predict anything,
and when usage data drifts towards monitoring individuals.

## When to use

- Adoption reports look healthy but nobody can show a change in the work.
- A sponsor or board treats active users or prompts as evidence of return.
- Benefits will take months to appear and the programme needs earlier signals that they are on track.
- Usage and outcomes disagree, and the team needs to find out why.
- An agent or Cowork task is live and its usage analytics need connecting to its benefits.

## When not to use

- Designing the overall Copilot adoption measures and reporting rules - use `copilot-adoption:adoption-measurement`.
- Measuring an individual agent's usage and value in detail - use `m365-agents:agent-value-measurement`.
- Measuring skills growth from learning - use `learning-and-skills:skills-measurement`.
- Measuring Champion programme health - use `champions:champion-metrics`.
- Defining the benefit statements the chain points at - use `value-realisation:benefit-hypothesis`.

## Questions to ask first

1. Which registered benefits depend on people adopting a Copilot capability, an agent or a Cowork task?
2. Which specific scenarios or behaviours, in which roles, are supposed to produce each benefit?
3. What usage data is available, at what aggregation, and what has the data protection officer agreed about its use?
4. How long after adoption should each benefit appear, and what is the earliest signal that it is coming?
5. Who will act when the chain breaks, and what can they change?

## Required inputs

- Registered benefit statements with the adoption level each assumes, from `value-realisation:benefit-hypothesis`.
- Priority scenarios by role from `copilot-adoption:scenario-discovery`.
- The adoption measures and minimum group size already agreed in `copilot-adoption:adoption-measurement`.
- An inventory of usage and analytics sources, confirmed by IT, and of outcome data from business systems.

If the minimum group size or the lawful basis for using usage data is not agreed, design the chain but publish nothing
until it is. Mark any link without a data source `[To confirm]` rather than substituting a proxy silently.

## Decision framework

Each benefit gets a chain of four links, each with at least one indicator, and only the last link counts as value.

| Link | What it shows | Example indicators | Counts as value? |
|---|---|---|---|
| Usage | People are using the capability | Active use by team as a share of enabled users; returning use after the first month | No |
| Scenario behaviour | Use is in the scenarios that matter | Share of target teams using the priority scenario routinely; agent sessions resolving the intended task | No |
| Work outcome | The work itself has changed | Cycle time, rework, backlog or first-time-right rate for the scenario | Not alone - it is evidence |
| Benefit | The organisation is better off | The registered benefit measure against its baseline | Yes |

Keep a leading indicator only if it passes all three tests: it is linked to a named benefit, the mechanism is written
down, and a forum will act when it moves. Use this table to diagnose a break in the chain.

| Pattern | Likely cause | Route |
|---|---|---|
| Usage high, behaviour low | Generic or shallow use; priority scenarios not landing | `copilot-adoption:scenario-discovery`, `change-and-communications:behaviour-reinforcement-plan` |
| Behaviour high, outcome flat | Scenario does not change the bottleneck, quality issues, or released time absorbed | `value-realisation:productivity-measurement`, `value-realisation:quality-measurement` |
| Outcome improved, benefit flat | Capacity not redeployed, or benefit wrongly specified | `value-realisation:benefit-owner` |
| Outcome improved, usage low | Another cause is driving the change | Recheck attribution before claiming the benefit |

## Practitioner approach

Start from the benefit and work backwards, never from the usage report forwards. For each benefit ask the owner which
people, in which roles, need to do what differently for it to appear. That gives the scenario behaviour. Then ask what
usage would have to look like for that behaviour to be possible. Indicators chosen this way are few and meaningful;
indicators chosen from whatever the dashboard shows are many and mostly noise.

Write the mechanism in one sentence per link: "If claims handlers use the summarisation agent on incoming files, they
skip the manual read-through, so time to first decision falls." The sentence is the hypothesis the indicators test. If
it cannot be written, the link is a guess and should be labelled as one.

Set expected lags. Usage moves in weeks, behaviour in one or two months, and outcomes and benefits often take a quarter
or more. Put the expected timing on each link so a sponsor does not read a flat benefit in month one as failure, or a
usage spike as success.

Choose behaviour indicators carefully, because they do most of the predictive work. Generic activity says little;
routine use of the specific scenario in the target teams says a lot. Where analytics cannot show scenario use, a short
pulse survey of teams or a structured sample from managers can, reported at team level. For agents and Cowork tasks,
use the analytics that show sessions completing the intended task rather than sessions started.

Report the chain together, never one link alone. A one-page view per benefit shows each link's status and the expected
lag. When a link breaks, use the diagnosis table and route the problem to the skill that can fix it. The value of this
work is in those routings: they turn measurement into programme decisions.

Hold the line on privacy. Usage data is reported by team or role above the agreed minimum group size, never by person,
and never used for performance management. Do not let a diagnosis of "low behaviour" become a list of named low users.

Revisit the chain at each benefit review. Indicators that turned out not to predict the benefit are retired; links that
proved strong become standard for similar scenarios elsewhere in the portfolio.

## Outputs

- An adoption-to-value chain for each benefit, recorded against it in the `benefits-register`: indicators per link, mechanism sentence, expected lag, source and acting forum.
- A one-page chain view per benefit for the value review, suitable for the `coe-kpi-scorecard`.
- A diagnosis log of breaks in the chain, the cause found and the routing taken.
- A list of retired indicators and the reason.

## Microsoft platform considerations

Microsoft provides usage reporting for Copilot and analytics for agents built in Copilot Studio, and these differ in
what they can show about scenario use. What each report contains, its aggregation level and its retention change over
time; check `references/sources.md` and confirm with IT before promising an indicator the tenant cannot produce.

## Adoption considerations

This skill depends on the adoption programme and feeds it. Share chain breaks with the adoption lead and Champions as
programme signals at team level, so they can target support rather than chase usage numbers.

## Knowledge considerations

For agents grounded in organisational content, a break between behaviour and outcome often traces back to knowledge
quality. Check the agent's knowledge sources with their owner before concluding that the scenario does not work.

## Security and privacy considerations

Usage data is frequently personal data. Use only aggregated reports, apply the minimum group size, keep raw data with
its current owner and confirm the lawful basis with the data protection officer before linking usage to business
outcomes, because linking can make individuals identifiable in small teams.

## Responsible AI considerations

Avoid indicators that pressure people to use AI where it does not suit the task, such as usage targets per person.
Where a scenario's outcome depends on human review, include an indicator that review is happening.

## Evaluation requirements

A break between behaviour and outcome can be a quality problem. Check the solution's current evaluation results before
attributing the break to adoption, and request a re-run through the solution's evaluation owner if they are stale.

## Value measures

Success is the share of adoption-dependent benefits with a complete chain, and the number of programme changes made
because a chain break was diagnosed, tracked by the Benefits Realisation Lead each value review cycle.

## Scale notes

### Starter

One chain for each of the two or three priority scenarios, using standard usage reporting, a short pulse survey and
one outcome measure, reviewed twice a year.

### Scale

Chains for every adoption-dependent benefit in the register, a quarterly diagnosis in the value review, and indicators
standardised for common scenarios.

### Enterprise

A library of proven chains by scenario and role that business units reuse, with spoke results rolled up to a portfolio
view of where adoption is and is not converting to value.

## Hand-offs

- To `copilot-adoption:adoption-measurement` and `copilot-adoption:scenario-discovery` when the break is in usage or behaviour.
- To `value-realisation:productivity-measurement` and `value-realisation:quality-measurement` when the break is in outcome.
- To `value-realisation:benefit-owner` when outcomes improve but benefits are not released.
- To `value-realisation:value-dashboard` for the sponsor view.

## Reviewer gates

Not applicable as a release gate, because the chain is a reporting instrument. Before usage data is first linked to
outcome data, `security-privacy` confirms aggregation, minimum group size and lawful basis.

## Failure modes

- Active users are reported to the board as return on investment, and the claim collapses under the first challenge.
- Leading indicators are chosen from whatever the report shows and predict nothing about the benefit.
- A flat benefit in month two is read as failure because nobody set the expected lag.
- Linking usage to outcomes in a small team makes individuals identifiable, and trust in the programme is lost.
- Diagnosis stops at "low adoption" when the real break is a quality or capacity problem further down the chain.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Present usage, licences assigned or prompts sent as value.
- Report or diagnose adoption by named individual, or below the minimum group size.
- Set usage targets for individuals.
- Keep an indicator nobody acts on.
