---
name: programme-risk-log
description: Runs the risks, assumptions, issues and decisions log for an AI programme, with AI-specific risk prompts, consistent scoring, owners by role, responses, review dates and escalation to the board, kept separate from solution risk tiers. Use when a programme is mobilising, when risks are known but owned by nobody, when assumptions about licences, knowledge or reviewers go unchecked, or when the board cannot see what threatens delivery.
license: CC-BY-4.0
metadata:
  department: programme-management
  lifecycle: Mobilise, Enable, Deliver, Assure, Launch, Measure
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: nist-ai-rmf, iso-iec-42001, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# Programme risk log

## Purpose

Every AI programme carries risks that are specific to it: licences assigned before people are ready, agents planned on
content nobody owns, reviewers who cannot keep up, Microsoft capabilities that change mid-flight, staff anxiety about
what AI means for their jobs. This skill runs the programme's risks, assumptions, issues and decisions log so that each
item has an owner, a response and a review date, and the board sees what threatens delivery in time to act. Logs fail
when they become a register filled in once for the charter, when every risk is scored amber, and when solution-level
AI risk is confused with programme delivery risk.

## When to use

- A programme is mobilising and needs its risk and issue log set up.
- Risks are known in conversation but owned by nobody, or the same risk appears in three workstream logs.
- The charter rests on assumptions (licences, capacity, knowledge readiness, supplier delivery) that nobody is checking.
- The board asks what could stop the programme, and the answer is a list with no responses.
- An issue has occurred and needs managing to resolution with a recorded decision.

## When not to use

- Assigning a risk tier to an individual AI solution and deriving its gates - use `opportunity-management:risk-classification`.
- Executive acceptance of residual risk in a specific AI solution - use `responsible-ai:ai-risk-acceptance`.
- Tracking a dependency between workstreams, suppliers or Microsoft releases - use `programme-management:dependency-management`.
- Overall programme health and corrective action - use `programme-management:programme-health`.
- Handling an incident in a live AI solution - use `ai-operations:ai-incident-management`.

## Questions to ask first

1. What could stop the programme reaching its next gate or its outcomes, and what has already gone wrong?
2. Which assumptions in the charter, plan or budget have not yet been confirmed by the person who can confirm them?
3. What scoring scale does the organisation already use for risk, and what level must be escalated to the board or sponsor?
4. Who owns each workstream, and therefore who can own the risks that arise in it?
5. Where will the log live, and who may see entries that touch on people, suppliers or security?

## Required inputs

- The programme charter and its assumptions from `programme-management:programme-charter`.
- The integrated plan and critical path from `programme-management:integrated-roadmap`.
- The organisation's risk scoring scale and escalation thresholds, if one exists; otherwise agree a simple one with the board.
- Workstream owners from `organisation-tailoring:ownership-map`.

Where the organisation has a corporate risk framework, use its scale and categories rather than inventing new ones, so
programme risks can be escalated without translation. If none exists, mark the scale as provisional until the board
agrees it.

## Decision framework

Classify each entry, then apply the rules for its type.

| Type | Definition | Must have | Closes when |
|---|---|---|---|
| Risk | Something that may happen and would affect objectives | Cause, event, effect, likelihood, impact, owner, response, review date | It can no longer happen or has become an issue |
| Assumption | Something treated as true for planning | Who can confirm it, by when, what happens if it is false | Confirmed (close) or disproved (raise a risk or issue) |
| Issue | Something that has happened and needs action | Effect, owner, action, target date | Resolved, with the decision recorded |
| Decision | A choice that resolves an issue or changes the plan | Options, decision, decider, date, forum | Recorded; it stays in the log |

Choose one response per risk: avoid (change the plan), reduce (act to lower likelihood or impact), transfer (to a
supplier or insurer where that genuinely moves the effect), or accept (with the decider recorded). Escalate to the board
when the score crosses the agreed threshold or the response needs resources beyond the workstream.

AI programme risk prompts to test at mobilisation and each gate:

| Area | Prompt |
|---|---|
| Adoption | Licences or access arrive before readiness, scenarios or support, and use stalls |
| Knowledge | Agents or Cowork tasks depend on content without owners, currency or correct permissions |
| Assurance | Reviewer capacity cannot keep pace with the release plan |
| Platform | A capability, licence term or limit the plan relies on changes or is not available as assumed |
| Cost | Consumption-based costs grow faster than forecast as agents scale |
| Suppliers | A partner's delivery, skills or knowledge transfer falls short |
| People | Staff concerns about job impact or monitoring reduce trust and use |
| Shadow AI | Unapproved tools continue because the approved route is slower |
| Value | Baselines are not captured, so benefits cannot be shown later |

## Practitioner approach

Run a short risk workshop at mobilisation with the workstream leads, the sponsor's delegate and a reviewer
representative. Use the prompts above to start the conversation, then ask each lead what keeps them awake about their
workstream. Write each risk as cause, event and effect: "Because HR policy pages have no named owner, the HR agent may
give outdated answers, which would delay its release and damage trust." Risks written this way point to their own
responses.

Pull the assumptions out of the charter and plan explicitly. AI programmes rest heavily on assumptions about licences,
platform capabilities, reviewer capacity and content quality. Give each one a person who can confirm it and a date by
which they will, and treat an unconfirmed assumption on the critical path as a risk in its own right.

Score consistently. Use the organisation's scale, apply it the same way across workstreams, and challenge entries where
everything is amber; a log where nothing is red or green is not being used to decide anything. Give each risk an owner
by role who can act on it, not the programme manager by default.

Keep programme risk separate from solution risk. A tier 3 agent is not automatically a high programme risk; the
programme risk is whether the responsible AI review will happen in time. Solution risk tiers live with
`opportunity-management:risk-classification` and the reviewers; the programme log tracks the delivery consequences.

Review the log weekly at the workstream leads meeting for movement, new entries and overdue actions, and take the top
risks and any threshold breaches to the board by exception. When an issue is resolved, record the decision with its
options and rationale and link it to the issue. When a risk materialises, convert it to an issue and keep the history.

Close the log properly at programme closure. Open risks that remain relevant to live solutions transfer to the CoE or
the owning business unit with a named owner, not into an archive.

## Outputs

- A risks, assumptions, issues and decisions log with type, description, cause and effect, scores, owner by role, response, actions, review date, status and links between related entries.
- A top risks summary for the board, prepared for inclusion in the `programme-health-report` template.
- A transfer list at closure, naming the role taking on each open item.

## Microsoft platform considerations

Where a risk depends on a Microsoft capability, licence term, limit or release date, record the source record checked and
the date, and review it when Microsoft announces change. Do not score platform risks from memory; check
`references/sources.md`. Licensing risks are resolved through the Microsoft licensing guide or a licensing partner, not in
the log.

## Adoption considerations

Log adoption risks with the same weight as technical ones; low use is the most common way an AI programme fails to
deliver its outcomes. Take adoption risk responses to the adoption lead rather than solving them in IT.

## Knowledge considerations

Content ownership and quality risks often sit on the critical path for agent releases. Give them owners from the
business units that own the knowledge, not from the build team.

## Security and privacy considerations

Some entries reveal security weaknesses or supplier issues; restrict access to the log accordingly. Data protection risks
are recorded and owned, but the judgement on them belongs to the DPO or legal adviser.

## Responsible AI considerations

Risks to people (job impact, fairness, over-reliance, monitoring concerns) belong in the log with a business owner and
a link to the `responsible-ai` review where a solution is involved. Never accept a responsible AI risk at programme level
that the charter reserves to the accountable executive.

## Evaluation requirements

Not applicable to the log itself; it should track the risk that evaluation evidence is late or incomplete for any
solution at tier 2 and above, since that blocks release at the `evaluation-quality` gate.

## Value measures

Report the number of risks above threshold, overdue actions, assumptions confirmed before their need-by date, and issue
age, at programme level. The AI Programme Manager owns these measures; they describe the log, never individuals.

## Scale notes

### Starter

A single list with ten to twenty entries, reviewed monthly at the working group, with the sponsor seeing anything red.

### Scale

A structured log with consistent scoring, weekly review by workstream leads, board escalation by threshold and links to
the decision log.

### Enterprise

Logs per tranche or business unit rolled up to a programme view, aligned to the corporate risk framework, with the top
risks visible to the portfolio board and risk function.

## Hand-offs

- To `programme-management:programme-board-cadence` for escalated risks and decisions.
- To `programme-management:dependency-management` where a risk is really a dependency.
- To `programme-management:programme-health` for the risk dimension of the health report.
- To `responsible-ai:ai-risk-acceptance` where residual solution risk needs executive acceptance.

## Reviewer gates

Not applicable, because the log releases no solution; risks raised by `security-privacy`, `responsible-ai`,
`evaluation-quality` or `design-authority` findings are recorded here with the reviewer's classification unchanged.

## Failure modes

- The log is completed for the charter and never reviewed again.
- Every risk is amber, so nothing is escalated until it becomes an issue.
- Assumptions about licences and capabilities are never confirmed, and the plan rests on them.
- Solution risk tiers are copied into the log as programme risks, and delivery threats are missed.
- The programme manager owns every risk, so nobody with the power to act does.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Downgrade or close a reviewer's blocking finding through the programme log.
- Accept a risk above the threshold the charter reserves to the sponsor or accountable executive.
- Record named individuals as the cause of a risk; describe roles, capacity and conditions instead.
- Treat an unconfirmed assumption as fact because the plan depends on it.
