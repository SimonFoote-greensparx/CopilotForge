---
name: escalation-and-appeal
description: Reviews the routes people have when an AI solution gets something wrong for them - reaching a person during an interaction, questioning or appealing an AI-influenced outcome, correcting information and reporting harm - including timescales, independent review and learning, classifying gaps as blocking or advisory. Use when outputs affect people, when an agent serves customers, or when complaints about an AI outcome have nowhere to go.
license: CC-BY-4.0
metadata:
  department: responsible-ai
  lifecycle: Deliver, Assure, Launch, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 2, 3, 4
  platforms: m365-agents, copilot-studio, ai-foundry, power-platform, platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: responsible-ai
  sources: ms-responsible-ai, ico-ai-data-protection, nist-ai-rmf, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# Escalation and appeal

## Purpose

When AI gets something wrong for a person, what matters most is whether they can get it put right. That needs a way to
reach a person while the problem is happening, a way to question an outcome afterwards, someone with the authority and
information to review it, and a feedback route so the same mistake is not repeated. This reviewer skill checks those
routes for a specific solution and classifies gaps as blocking or advisory. It goes wrong when appeals are sent back to
the same AI that made the error, or when the route exists but nobody affected knows about it.

## When to use

- Outputs influence decisions about employees, candidates, customers or members of the public.
- An agent serves customers or the public, or staff on matters affecting their employment.
- The impact assessment or human oversight plan relies on people being able to challenge outcomes.
- Complaints about an AI-influenced outcome have arrived and there is no clear route.
- A solution's audience or autonomy is about to grow.

## When not to use

- Collecting general user feedback to improve an agent - use `ai-operations:ai-feedback-loop`.
- Handling operational incidents and harms in live service - use `ai-operations:ai-incident-management`.
- Designing the in-conversation hand-off mechanics of an agent - use `copilot-studio:conversation-design`.
- Responding to data protection rights requests - use `security-privacy:privacy-assessment` with the DPO.
- Designing review before an output takes effect - use `responsible-ai:human-oversight`.

## Questions to ask first

1. Who could be harmed or disadvantaged by an error, and how would they notice?
2. How can a person reach a human during an interaction, and how quickly?
3. How can someone question an outcome afterwards, who reviews it, and can that reviewer overturn it?
4. What information will the reviewer have about how the AI contributed?
5. How do appeal outcomes feed back into the solution, and who checks the themes?

## Required inputs

- The AI impact assessment record and human oversight plan.
- The solution design, channels and the decisions or outputs it influences.
- The organisation's existing complaints, grievance and case review processes.
- The record map from `security-privacy:ai-interaction-retention`, so reviewers can see what happened.

Where no existing process covers the outcome, record the gap and the process owner who must decide. Never invent a
service level on the organisation's behalf; mark it to be confirmed by the process owner.

## Decision framework

From risk tier 2 every gap is classified; the gate is mandatory and blocking from tier 3, and from tier 2 when outputs
inform decisions about people.

| Route | Blocking when | Advisory when | Typical fix |
|---|---|---|---|
| Reach a person in the moment | Customer-facing or high-impact interactions have no route to a person | Route exists but is slow or hard to find | Visible hand-off, contact details, or live transfer |
| Question an outcome | People affected cannot challenge an AI-influenced outcome | Route exists but is not explained to them | Connect to complaints or case review; tell people at the decision point |
| Independent review | Appeals go back to the same AI or to someone without authority to overturn | Reviewer has authority but limited information | Named reviewing role with authority and access to the AI's contribution |
| Correction | Wrong information about a person persists in sources or outputs after an appeal succeeds | Correction is manual and slow | Correct at source and re-check outputs |
| Learning | Appeal outcomes never reach the solution owner | Themes reviewed irregularly | Aggregate appeal themes into the review calendar |
| Timescales | No expectation set for response on matters affecting rights or livelihood | Timescales set but not monitored | Process owner sets and monitors timescales |

## Practitioner approach

Start by imagining the error from the affected person's side. A customer receives a refusal drafted by AI. A member of
staff is told their leave request does not meet policy by an HR agent. A candidate is not shortlisted after an AI
summary. For each, ask how they would know something went wrong, who they would contact, and what would happen next.
Write the journey down; gaps become obvious.

Check the in-the-moment route. Customer-facing and high-impact agents should make it easy to reach a person, and should
hand over context so the person does not start again. Where a live hand-off is not possible, give a clear contact route
and set expectations.

Then check the after-the-fact route. Most organisations already have complaints, grievance or case review processes.
The usual fix is to connect the AI solution to them, not to build a new one. Make sure the process owner knows AI is
involved, that reviewers can see what the AI contributed (its output, the sources it used and who acted on it), and
that the reviewer has authority to overturn. An appeal that is reprocessed by the same agent is not an appeal.

Check correction. If an appeal succeeds because source data was wrong, the data must be corrected at source, or the
same error will recur. Coordinate with the data and knowledge owners.

Tell people. Routes nobody knows about do not exist in practice. The decision point is where people need to learn that
AI was involved and how to question the outcome; coordinate wording with `responsible-ai:ai-transparency`.

Close the loop. Agree how appeal outcomes are aggregated, by theme and outcome rather than by individual, and reviewed
with the solution owner. A rising rate of successful appeals is an early warning that the solution or its data has
drifted.

Keep it proportionate. An internal policy agent may need only a clear "contact HR" route and a feedback link. A
customer-facing triage agent needs a full route with independent review and monitored timescales.

## Outputs

- An escalation and appeal map for the solution: in-the-moment route, after-the-fact route, reviewing role and authority, information available, correction steps, timescales to confirm and learning loop.
- Gaps classified blocking or advisory with fix and owner, recorded in the `ai-impact-assessment-record`.
- Wording requirements passed to `responsible-ai:ai-transparency`.

## Microsoft platform considerations

Hand-off to a person, escalation topics, ticket creation and case management integration are implemented differently
across agents, Copilot Studio and custom solutions, and options change. Design the route first, then confirm the
mechanism in the platform's current source records.

## Adoption considerations

People accept AI in services more readily when they know they can reach a person. Make the route visible in launch
communications, and make sure frontline teams who receive escalations are prepared for them.

## Knowledge considerations

Successful appeals often expose wrong or outdated knowledge. Send those themes to the knowledge owner so sources are
fixed, not just the individual case.

## Security and privacy considerations

Reviewers need access to interaction records for the case, but only for the case. Check access with
`security-privacy:ai-interaction-retention`, and route data protection rights requests to the DPO rather than handling
them as appeals.

## Responsible AI considerations

This skill is the responsible AI review of redress. It completes the controls identified in
`responsible-ai:ai-impact-assessment` and works with `responsible-ai:human-oversight`, which catches errors before they
take effect.

## Evaluation requirements

Test the route before release: walk two or three realistic cases end to end, including a hand-off and an appeal, and
confirm the reviewer can see what the AI contributed and can overturn it.

## Value measures

Track appeal volumes, outcomes, time to resolution and recurring themes at aggregate level, and the share of tier 2+
solutions with a tested route. The business owner owns these measures, with the process owner for timescales.

## Scale notes

### Starter

Connect each solution to an existing contact or complaints route and make it visible. Avoid external or high-impact
uses until a reviewed appeal route exists.

### Scale

Standardise appeal routes per pattern, brief complaints and case teams on AI involvement, and review themes in the
operations cadence.

### Enterprise

Integrate AI involvement into enterprise complaints and case management, report appeal themes across the portfolio to
the responsible AI function, and test routes periodically.

## Hand-offs

- To `ai-operations:ai-feedback-loop` and `ai-operations:ai-incident-management` with themes and serious cases.
- To `responsible-ai:ai-transparency` for wording at the decision point.
- To the process owner of complaints or case review to confirm timescales.
- To `responsible-ai:ai-risk-acceptance` for disputed gaps.

## Reviewer gates

This skill is part of the `responsible-ai` gate, mandatory and blocking from risk tier 3, and from tier 2 when outputs
inform decisions about people. Disagreement escalates to the accountable executive for written risk acceptance.

## Failure modes

- Appeals are routed back to the same agent, which repeats its answer.
- The route exists in a policy document but nobody affected is told about it.
- A successful appeal fixes one case while the wrong source data keeps producing the same error.
- Appeal themes are never reviewed, so drift goes unnoticed for months.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Accept an appeal route that sends the case back to the same AI.
- Invent service levels or timescales on behalf of the process owner.
- Report appeal data in a way that identifies or ranks individual staff.
- Trade a blocking gap against a launch date.
