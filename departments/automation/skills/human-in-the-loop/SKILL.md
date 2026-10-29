---
name: human-in-the-loop
description: Designs the human approval and review steps inside an automation - where a person checks AI output before it takes effect, what they see, how long they have, who covers absence, and how to stop reviews becoming rubber stamps. Use when an automated flow acts on AI output, when approvals sit unanswered or are approved without reading, or when a reviewer asks what checks an automation needs.
license: CC-BY-4.0
metadata:
  department: automation
  lifecycle: Deliver, Assure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: power-platform, copilot-studio, m365-copilot
  edition-support: starter, scale, enterprise
  reviewers: responsible-ai, design-authority
  sources: ms-responsible-ai, nist-ai-rmf, ico-ai-data-protection, ms-copilot-studio-guidance
  status: draft
  authors: Simon Foote
---

# Human in the loop

## Purpose

An automation that acts on AI output needs a person in the right place, seeing the right information, with time to make
a real decision. This skill designs those review and approval steps: where they sit in the flow, what the reviewer is
shown, how quickly they must act, who covers when they are away and how the organisation knows the reviews are real.
It goes wrong in two directions: reviews placed after the effect has already happened, and reviews so frequent and
thin that people approve without reading, which gives the appearance of oversight without the substance.

## When to use

- An automation design includes AI steps whose output will update records, send messages or trigger decisions.
- Approvals in a live flow sit unanswered for days, or are approved in seconds without evidence of reading.
- A reviewer or process owner asks what human checks an automation needs before it goes live.
- The volume of items needing review is growing and the team cannot keep up.
- The organisation wants to reduce review from every item to sampled review and needs a safe basis for doing so.

## When not to use

- Designing checkpoints in delegated work run through Copilot Cowork - use `copilot-cowork:human-checkpoint-design`.
- The formal reviewer assessment of oversight for tier 3 and above - use `responsible-ai:human-oversight`.
- Retry, fallback and exception queue mechanics - use `automation:exception-handling`.
- Redesigning the process and deciding which steps stay human - use `automation:automation-process-design`.
- Reviewing outputs of delegated Cowork tasks before they have effect - use `copilot-cowork:delegated-work-review`.

## Questions to ask first

1. What is the worst thing that happens if an AI result is wrong and nobody checks it, and how quickly would anyone notice?
2. Who has the authority and knowledge to approve, and is that the same person who requested the work?
3. How many items a day will need review, and how much time does each genuinely need?
4. What does the reviewer need to see to decide well: the AI result, the source, the confidence, the reason, the alternatives?
5. What should happen if nobody responds within the time the process can tolerate?

## Required inputs

- The automation design, including AI step definitions, thresholds and the points where results take effect.
- The risk tier and any regulatory or policy requirement for human decision-making, from the process owner.
- Expected volumes, and the roles available to review, with their declared capacity.
- The exception routes defined in `automation:automation-process-design`.

If volumes or reviewer capacity are unknown, mark them "to confirm" and design for full review until evidence supports
sampling. Never assume reviewers have spare capacity.

## Decision framework

Choose the review mode for each point where AI output takes effect. Higher modes are the default for higher tiers.

| Review mode | Use when | Minimum design |
|---|---|---|
| None, automatic | Effect is internal, reversible, low impact and validated by rules | Validation, logging and periodic sample check by the owner |
| Sampled review after effect | Effect is reversible, volume is high and accuracy is proven over time | Agreed sample rate, fast reversal route, trend review |
| Review on exception | Most items are routine; only low-confidence or rule-failing items need a person | Threshold from evaluation, clear reason shown to reviewer |
| Approval before effect | Effect is external, hard to reverse, financial or affects a person | Approve, reject or amend; evidence shown; time limit and escalation |
| Two-person approval | High value, high harm or separation of duties required | Different requester and approver; recorded reasons |

From tier 3, any AI output that informs a decision about an individual needs approval before effect at minimum. Moving a
step to a lighter mode requires evidence from monitoring and the process owner's written agreement.

## Practitioner approach

Start from the effects, not the AI steps. List every point where the automation changes something outside itself: a
record updated, a message sent, money moved, a case closed, a person told something. For each, ask what happens if the
AI result behind it is wrong. That answer, not the AI step, decides the review mode.

Place reviews before effects. A review that happens after the email has gone is a complaint-handling process, not
oversight. Where a step must happen quickly, consider holding only the risky part (for example, drafting the reply
automatically but sending only after approval) rather than reviewing everything after the fact.

Design what the reviewer sees. Show the AI result alongside the input it came from, so the reviewer can compare rather
than trust. Show the confidence or validation outcome and why the item was routed to them. Offer approve, reject and
amend, and make reject as easy as approve. Ask for a short reason on rejection or amendment; those reasons are the best
evidence for improving the AI step.

Size the work. Multiply volume by realistic review time and compare it with declared capacity. If the numbers do not
fit, reviews will become rubber stamps. Reduce volume by fixing inputs, tightening validation or routing only
low-confidence items, rather than asking people to review faster. Watch for automation bias: a reviewer who approves
everything in seconds is a design problem, not a performance problem.

Set time limits and escalation. Every approval needs a deadline matched to the process, a reminder, a delegate for
absence and a defined outcome when the deadline passes. The default outcome on timeout should be the safe one (hold or
escalate), never automatic approval.

Separate duties where it matters. The person who requested a payment or submitted a claim should not approve the AI
decision about it. Record who approved what and when, with the evidence they saw.

Plan the path to lighter review. Agree with the process owner what evidence would justify moving from full approval to
review on exception or sampling: a period of stable accuracy, low rejection rates and no serious errors. Write the
evidence threshold down now, so the change later is a decision rather than drift.

## Outputs

- A review and approval design per effect point: review mode, reviewer role, information shown, decision options, time limit, escalation, delegate, timeout outcome and record kept. It forms the review section of the `automation-design` template.
- Reviewer capacity calculation, with the assumptions behind it.
- Criteria for moving any step to a lighter review mode, agreed with the process owner.

## Microsoft platform considerations

Power Automate approvals, adaptive cards in Microsoft Teams and actionable messages in Outlook are common ways to put a
decision in front of a reviewer, and Copilot Studio agents can collect confirmation in conversation. Their options for
timeouts, delegation, reassignment and audit records change; check current behaviour in `references/sources.md` and test
the timeout and absence paths explicitly.

## Adoption considerations

Reviewers need to know why they are reviewing, what good review looks like and that rejecting AI output is welcome.
Brief them before go-live and share what their rejections led to. Treat review load as a design measure at team level,
never as a measure of individual reviewers.

## Knowledge considerations

Reviewers need the rules they are checking against: policy, thresholds, category definitions. Link to the maintained
source from the review card rather than relying on memory.

## Security and privacy considerations

Review cards and approval emails can carry personal or confidential data to devices and inboxes. Show only what the
decision needs, link to the record rather than copying it where possible, and send approvals only to the authorised
role.

## Responsible AI considerations

This skill designs the human oversight that `responsible-ai:human-oversight` reviews from tier 3. Where AI informs a
decision about a person, the reviewer must be able to understand and override it, and the affected person must have a
route to challenge the outcome through the `responsible-ai` department's escalation and appeal design.

## Evaluation requirements

Test the review paths end to end: approve, reject, amend, timeout, absence and escalation. Before go-live, confirm the
reviewer can detect seeded errors in a sample of AI results. After go-live, track rejection and amendment rates by step.

## Value measures

Track review volume, time to decision, rejection and amendment rates and timeouts, at step and team level. These show
whether oversight is real and where AI steps need improvement. The process owner owns them; never report them per
reviewer.

## Scale notes

### Starter

Use approval before effect for anything external or affecting a person, with one reviewer role and a named delegate.
Keep the review card simple and test the timeout path.

### Scale

Standardise review card patterns and timeout rules across automations, and review the evidence for moving steps to
lighter modes at the CoE cadence.

### Enterprise

Define organisation-wide rules for which effects always need approval, and two-person approval for the highest-harm
decisions. Monitor review load across automations so oversight does not quietly erode as volumes grow.

## Hand-offs

- To `automation:flow-design-patterns` to build the review steps into the flow.
- To `automation:exception-handling` for timeout and escalation routes.
- To `responsible-ai:human-oversight` for review from tier 3.
- To `automation:automation-monitoring` to track review measures after go-live.

## Reviewer gates

From risk tier 3, `responsible-ai` reviews the oversight design, and a review placed after an effect on a person is a
blocking finding. From tier 2, `design-authority` checks that review placement and timeout behaviour are sound.

## Failure modes

- Reviews happen after the effect, so the organisation finds errors only through complaints.
- Review volume exceeds capacity and reviewers approve without reading.
- Approvals time out to automatic approval, quietly removing oversight during holidays.
- The requester approves their own AI-assisted decision, defeating separation of duties.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Place a review after an effect that cannot easily be reversed.
- Let an approval default to approved when nobody responds.
- Use review data to rank or monitor individual reviewers.
- Move a step to lighter review without evidence and the process owner's written agreement.
