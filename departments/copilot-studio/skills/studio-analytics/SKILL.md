---
name: studio-analytics
description: Uses Copilot Studio analytics and conversation records to improve a live agent - sessions, outcomes such as resolved, escalated and abandoned, unanswered questions, knowledge and tool use, satisfaction and recurring themes - through a regular improvement review at aggregate level that turns findings into prioritised fixes. Use when an agent is live and its owner asks how it is doing, when resolution falls, or when deciding what to fix next.
license: CC-BY-4.0
metadata:
  department: copilot-studio
  lifecycle: Measure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: copilot-studio, power-platform
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-studio-guidance, ms-copilot-studio-security-governance, ico-ai-data-protection, ms-coe-starter-kit
  status: draft
  authors: Simon Foote
---

# Studio analytics

## Purpose

A live agent tells you how it is doing through its conversations: which requests it resolves, where users give up, what
it cannot answer, which tools fail and how satisfied people are. This skill turns Copilot Studio analytics and
conversation records into a regular improvement review that decides what to fix next. Analytics usually goes wrong in
three ways: nobody looks after launch, the team reports session counts as if they were value, or transcripts are read
casually in ways that intrude on individual users.

## When to use

- An agent has been live long enough to have meaningful conversation volume.
- The business owner asks how the agent is performing, or resolution, satisfaction or usage falls.
- The team needs to decide which knowledge, topic, tool or conversation fixes to prioritise.
- A change has been released and its effect needs checking.

## When not to use

- Measuring the agent's value against its value hypothesis - use `m365-agents:agent-value-measurement`.
- Operational monitoring and alerting on failures - use `ai-operations:ai-solution-monitoring`.
- Collecting and acting on user feedback across AI solutions - use `ai-operations:ai-feedback-loop`.
- Retention and access rules for transcripts - use `security-privacy:ai-interaction-retention`.
- Organisation-wide Copilot usage reporting - use `m365-copilot:copilot-usage-reporting`.

## Questions to ask first

1. What does a good outcome look like for this agent - resolved without escalation, a completed action, a correct hand-off?
2. Which analytics are available and enabled in the agent's environment, and who has access to them?
3. Are conversation transcripts stored, who may read them, for what purpose, and for how long?
4. What baseline exists from the pilot or first weeks after launch?
5. Who attends the improvement review and who can approve fixes?

## Required inputs

- Access to the agent's analytics for the agent owner and maker, under the agreed access rules.
- The success measures from the brief and the baseline from early operation.
- The transcript access and retention rules from `security-privacy:ai-interaction-retention`.
- The current solution design, so findings can be traced to the layer that owns them.

If transcript access rules are not agreed, use aggregate analytics only until they are. Never read transcripts to
satisfy curiosity about what particular people asked.

## Decision framework

Read the signals in this order, because each points to a different owner.

| Signal | Likely cause | Owning skill for the fix |
|---|---|---|
| Many unanswered or low-confidence questions on a theme | Knowledge gap or poor source descriptions | `copilot-studio:studio-knowledge-architecture` |
| Requests routed to the wrong topic, tool or source | Overlapping descriptions or missing mechanism | `copilot-studio:topics-and-orchestration` |
| Tool or flow failures | Connection, permission or system issues | `copilot-studio:studio-actions-and-tools` |
| High abandonment early in conversations | Greeting, sign-in or clarification problems | `copilot-studio:conversation-design` |
| High escalation on one topic | Scope too wide, or a process that needs a person | Business owner decision |
| Low satisfaction with good resolution | Tone, length or speed | `copilot-studio:conversation-design` |

Prioritise fixes by volume multiplied by harm: a rare failure that exposes data outranks a common slow answer.

## Practitioner approach

Set the review rhythm before launch. Agree with the business owner how often to review - weekly in the first month, then
monthly is a common starting point - who attends and what decisions the review can take. Without a fixed review,
analytics are opened once and forgotten.

Start with outcomes, not volume. Session counts show reach; they do not show whether the agent helped. Look at the
proportions resolved, escalated and abandoned, then at completed actions and satisfaction where collected. Compare with
the baseline and with the previous review, and look for changes after releases.

Then find themes. Group unanswered questions, escalations and abandoned sessions by topic or theme using the platform's
groupings where available, and read a small, purposeful sample of conversations for the largest themes under the agreed
access rules. The aim is to understand failure patterns, not to inspect what individuals asked. Note what users wanted,
what the agent did, and which layer caused the failure.

Trace each pattern to its owner using the decision framework, and write it as a fix with an expected effect: "connect
the updated travel policy library and describe it; expect unanswered travel questions to fall". Prioritise by volume and
harm, agree the fixes at the review, and send them through ALM and regression testing like any other change.

Check the effect. At the next review, look at the measure the fix was meant to move. If it did not move, the cause was
misdiagnosed; revisit it rather than adding more changes on top.

Report upwards in plain language: what users are trying to do, how well the agent serves them, what changed since the last
review, and the decisions taken. Keep reporting at agent and audience level and above the agreed minimum group size.
Never use analytics or transcripts to judge individual users or staff who receive escalations.

Finally, feed recurring knowledge gaps to `knowledge-management:knowledge-gap-analysis`, and value questions to
`m365-agents:agent-value-measurement`.

## Outputs

- An improvement review pack: outcomes against baseline, top themes, failure patterns traced to layers, and prioritised fixes with expected effects.
- A decision log of fixes agreed, owners and the measure each should move.
- A short sponsor summary at agent level.

## Microsoft platform considerations

Copilot Studio analytics, outcome definitions, theme grouping, satisfaction collection, transcript storage and export
options change over time and depend on environment settings. Check `ms-copilot-studio-guidance` for current analytics
and `ms-copilot-studio-security-governance` for transcript controls. The `ms-coe-starter-kit` record can help with
estate-level usage views.

## Adoption considerations

Low reach in part of the audience is an adoption signal, not an agent defect. Share it with `copilot-adoption:adoption-measurement`
and the launch owner, and show users what changed because of their questions.

## Knowledge considerations

Unanswered and wrongly answered questions are the best evidence of knowledge gaps. Route them to knowledge owners with
the volume and examples, and confirm the gap closes after content is fixed.

## Security and privacy considerations

Transcripts can contain personal and sensitive data. Read them only under agreed access rules and for improvement
purposes, keep samples small, never export them to uncontrolled locations, and follow retention rules. Purpose and
transparency follow the privacy assessment and `ico-ai-data-protection` guidance.

## Responsible AI considerations

Look for patterns of harm in aggregate: users from one group escalated more often, sensitive subjects handled poorly, or
overconfident answers. Report them to the `responsible-ai` reviewers for agents at tier 2 and above.

## Evaluation requirements

Add real failing questions found in review, with corrected expected answers, to the regression pack through
`copilot-studio:studio-testing-and-evaluation`, so each fix stays fixed.

## Value measures

Resolution rate, escalation rate and reason, abandonment, completed actions and satisfaction, each against baseline,
owned by the business owner and reported at agent and audience level. Never report individual usage.

## Scale notes

### Starter

A monthly thirty-minute review of the agent's analytics by the maker and business owner, with three fixes agreed and checked next time.

### Scale

A standard review pack across agents, shared theme categories, and a CoE view of common failure patterns across the portfolio.

### Enterprise

Analytics exported to a governed reporting platform where supported, trend reporting across the estate, and improvement
reviews linked to the release calendar and the solution inventory.

## Hand-offs

- To the owning design skills for each fix, through `copilot-studio:studio-alm`.
- To `m365-agents:agent-value-measurement` for value against the hypothesis.
- To `knowledge-management:knowledge-gap-analysis` for recurring knowledge gaps.
- To `copilot-studio:studio-agent-lifecycle` when usage suggests an agent should be merged or retired.

## Reviewer gates

From risk tier 2, `security-privacy` confirms transcript access, purpose and retention are agreed before transcripts are
read for improvement. Reading transcripts without agreed access rules is a blocking finding.

## Failure modes

- Nobody reviews analytics after launch and the agent decays unnoticed.
- Session counts are reported to sponsors as success while resolution falls.
- Transcripts are browsed casually and individual users' questions are discussed by name.
- Fixes are made without checking whether they moved the measure they targeted.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Use analytics or transcripts to monitor, judge or rank individual users or staff.
- Read transcripts without agreed access rules and a stated improvement purpose.
- Report session or message counts as evidence of value.
- Assert which analytics features exist without checking the current source record.
