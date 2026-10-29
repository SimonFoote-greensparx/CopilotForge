---
name: agent-value-measurement
description: Measures whether an individual agent delivers the value its hypothesis promised, combining audience-level usage, resolution and answer-quality signals, user feedback and the business outcome measure against the baseline, and produces a value report for the agent's review. Use when an agent has been live long enough to judge, when its review date approaches, or when someone claims an agent is or is not worth keeping.
license: CC-BY-4.0
metadata:
  department: m365-agents
  lifecycle: Measure, Improve, Scale
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3
  platforms: m365-agents, copilot-studio
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-studio-guidance, ms-agent-builder, ms-copilot-adoption-hub
  status: draft
  authors: Simon Foote
---

# Agent value measurement

## Purpose

An agent was built because someone expected it to make a measurable difference: fewer tickets, faster answers, less time
from experts on routine questions. This skill checks whether that is happening. It combines usage at audience level,
signals of whether questions were resolved and answered well, user feedback and the business outcome measure, and
compares them with the baseline recorded before build. It goes wrong when usage counts are presented as value, when no
baseline was taken, or when agent data is used to judge the people who use it.

## When to use

- An agent has been live long enough for its outcome measure to show an effect.
- The agent's review date is approaching and the owner needs evidence.
- Someone claims an agent is a great success, or a waste, without evidence.
- Several agents compete for support or investment and need comparable evidence.

## When not to use

- Stating the value hypothesis and baseline before build - use `opportunity-management:value-hypothesis`.
- Programme-level benefits, return on investment and financial benefits - use `value-realisation:roi-model` or `value-realisation:financial-benefits`.
- Improving a Copilot Studio agent from its analytics - use `copilot-studio:studio-analytics`.
- Measuring Copilot adoption across the workforce - use `copilot-adoption:adoption-measurement`.
- Deciding whether to scale or stop on the evidence - use `opportunity-management:scale-or-stop`.

## Questions to ask first

1. What value hypothesis and success measure did the brief record, and what was the baseline?
2. Who is the intended audience, how large is it, and what is the minimum group size for reporting?
3. Which usage, feedback and quality data does the build path provide, and who can access it?
4. Where does the outcome measure come from (ticketing, workload records, survey), and who owns that data?
5. What decision will the review make with this evidence?

## Required inputs

- The agent brief and `agent-card`, with value hypothesis, success measure, baseline, audience and review date.
- Usage and analytics data from the build path, at audience level.
- Feedback collected through the agent and the support route.
- The outcome data from its business source, owned by the function concerned.
- The latest evaluation results from `m365-agents:agent-testing`.

If no baseline was taken, say so plainly, take one now from comparable data or a comparison group if possible, and lower
the confidence of conclusions. Never reconstruct a baseline from memory and present it as measured.

## Decision framework

Read four layers together; no single layer proves value.

| Layer | Example measures | What it can show | What it cannot show |
|---|---|---|---|
| Reach and use | Share of the intended audience using the agent; repeat use; trend | Whether people find and return to it | Whether answers helped |
| Resolution and quality | Questions answered from knowledge, redirects, fallbacks, evaluation pass rate | Whether it answers in scope and well | Whether the business outcome moved |
| User feedback | Ratings, comments, reported wrong answers | Perceived usefulness and problems | Effects users do not notice |
| Business outcome | The brief's measure against baseline, such as tickets or time to answer | Whether value was delivered | Attribution, without a comparison or careful reasoning |

Verdicts: value demonstrated (outcome moved in line with the hypothesis and other layers support it), value emerging
(use and quality good, outcome not yet clear), value not demonstrated (outcome flat with adequate use), or not adopted
(low use; investigate before judging value).

## Practitioner approach

Start from the hypothesis in the brief, not from the dashboard. Write down what the agent was meant to change, for whom
and by how much, and what the baseline was. That defines the evidence you need; anything else is context.

Gather the four layers. Take usage and analytics from the build path at audience level, and read the definitions,
because terms such as "session", "engaged" or "resolved" mean different things in different tools. Check the source
records for what is currently available. Collect feedback from the agent and from the support route, and read the
comments, not just the ratings. Pull the latest evaluation results so quality is measured, not assumed. Get the outcome
data from its business owner, such as the service desk or the function's own records.

Reason about attribution honestly. If tickets fell after the agent launched, ask what else changed: a policy update, a
seasonal pattern, a new portal. Where possible compare with a period, team or region without the agent, or look for
direct evidence, such as tickets on the agent's topics falling while others did not. State the confidence of the
conclusion and what would raise it.

Be careful with time savings. Self-reported minutes saved are weak evidence on their own; combine them with operational
measures where you can, and use the methods in `value-realisation:productivity-measurement` for anything that will feed a
financial case.

Diagnose before judging. Low use may mean people do not know the agent exists, the agent sits in the wrong channel, or
its answers disappoint. Each needs a different fix, and only the last is a value problem. Look at the questions people
asked that the agent could not answer; they often reveal knowledge gaps worth fixing, through
`knowledge-management:knowledge-gap-analysis`.

Write a short value report for the review: hypothesis, baseline, the four layers, the verdict, the confidence, what
would improve value, and the recommendation to continue, change or retire. Keep all data at audience or team level,
above the minimum group size. Never report which individuals used the agent or what they asked.

## Outputs

- An agent value report: hypothesis, baseline, reach and use, resolution and quality, feedback, outcome, verdict, confidence and recommendation.
- A list of improvement actions (knowledge gaps, instruction changes, communications) with owners.
- The value evidence recorded against the agent on the `agent-card` and in the solution register.

## Microsoft platform considerations

Agent Builder, declarative agents and Copilot Studio provide different usage, analytics and feedback data with their own
definitions and retention. See `ms-copilot-studio-guidance` and `ms-agent-builder` for what is available now; these
change frequently, so confirm metric definitions before reporting them. Business outcome data usually comes from systems
outside Microsoft 365 and must be obtained from its owner.

## Adoption considerations

Low reach is often an adoption problem rather than a value problem. Route it to communications and Champions before
concluding the agent has failed, and share credible value evidence through `change-and-communications:success-stories`.

## Knowledge considerations

Unanswered questions and wrong answers are the best evidence of knowledge gaps. Pass them to knowledge owners with
counts at topic level so the knowledge improves, not just the agent.

## Security and privacy considerations

Analytics and transcripts may contain personal data. Access is limited to people with a documented need, reporting stays
above the minimum group size, and transcripts are reviewed only under the organisation's agreed policy, checked with the
data protection lead.

## Responsible AI considerations

Agent data must not be used to assess, rank or monitor individual users. Where the agent supports decisions about
people, the value report also records whether human oversight operated as designed.

## Evaluation requirements

The value report includes the latest evaluation pass rate against the threshold agreed at release. A value verdict
without current quality evidence is incomplete.

## Value measures

This skill produces the agent's value measures: the outcome measure against baseline, owned by the agent's business
owner, with reach, quality and feedback as supporting layers. Estate-level summaries are owned by the CoE lead and
reported at audience or team level only.

## Scale notes

### Starter

A one-page report for each agent at its review, with a simple before-and-after comparison and the owner's judgement.

### Scale

A standard value report for every agent, comparable across agents, feeding CoE portfolio reviews and scale-or-stop
decisions.

### Enterprise

Value reporting integrated with the value dashboard and portfolio, with comparison groups designed in for significant
agents and finance involvement for anything feeding a financial case.

## Hand-offs

- To `opportunity-management:scale-or-stop` with the value report.
- To `m365-agents:agent-lifecycle` for the continue, change or retire decision.
- To `value-realisation:adoption-to-value-metrics` and `value-realisation:value-dashboard` for programme reporting.
- To `knowledge-management:knowledge-gap-analysis` with unanswered-question themes.

## Reviewer gates

Not applicable as a formal gate, because the report informs the owner's review rather than releasing anything; reports
that feed a financial business case are checked with finance through `value-realisation:financial-benefits`.

## Failure modes

- Usage counts are presented as value, and an agent that answers poorly is kept because it is busy.
- No baseline was taken, and the review relies on anecdotes.
- A coincident change is credited to the agent, and a scale decision rests on false attribution.
- Analytics are used to see who asked what, and users stop trusting the agent.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Present usage as proof of value.
- Report or inspect which individuals used the agent or what they asked, outside an agreed policy.
- Invent or reconstruct a baseline and present it as measured.
- Give a value verdict without current answer-quality evidence.
