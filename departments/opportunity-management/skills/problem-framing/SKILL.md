---
name: problem-framing
description: Turns a raw idea or tool request into a framed business problem with a named business owner, affected roles, current cost, expected outcome and baseline, and politely sends solution-first requests back to the problem. Use when an idea arrives at intake, when someone asks for an agent or Copilot feature before saying what is wrong, or when a pilot cannot say what it was meant to improve.
license: CC-BY-4.0
metadata:
  department: opportunity-management
  lifecycle: Envision
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Problem framing

## Purpose

This skill is the front door of the opportunity lifecycle. It takes an idea, a complaint or a request for a specific
tool and turns it into a problem statement that someone owns, that can be measured, and that later skills can judge.
Nothing enters assessment without it. Intake usually goes wrong by accepting "we need an agent for X" as a requirement,
by framing problems on behalf of a business that has not agreed it has one, or by skipping the baseline so that nobody
can later say whether anything improved.

## When to use

- A new idea arrives through intake, a Champion, a manager or a hackathon.
- Someone requests a specific tool or feature ("an agent for onboarding", "Copilot in our case system") without stating the problem.
- A pilot is under way but cannot say what it was meant to improve or for whom.
- Several teams describe what may be the same problem in different words and need one shared framing.

## When not to use

- Deciding whether AI is the right answer once the problem is framed - use `opportunity-management:ai-suitability`.
- Assigning a risk tier - use `opportunity-management:risk-classification`.
- Comparing framed opportunities against each other - use `opportunity-management:opportunity-prioritisation`.
- Finding everyday Copilot scenarios for a role during adoption - use `copilot-adoption:scenario-discovery`.
- Setting organisation-wide outcomes - use `ai-strategy:strategic-outcomes`.

## Questions to ask first

1. What goes wrong today, for whom, how often, and what happens as a result?
2. Who in the business is accountable for this work and would decide that the problem is solved?
3. How is the problem measured now, or what could be counted within a few weeks to establish a baseline?
4. What would be different, and by how much, if the problem were solved?
5. Which strategic outcome, if any, does this contribute to?

## Required inputs

- The original request in the requester's own words, kept verbatim on the record.
- Access to the business owner, or to someone who can name them.
- Any existing data about the work: volumes, cycle times, error or rework rates, complaints, staff time.

If no business owner can be named, the opportunity is held at "awaiting owner" and does not proceed; a request
without an owner is a suggestion, not an opportunity. If no baseline exists, record how and by when it will be
established. Never estimate a baseline and present it as measured.

## Decision framework

An opportunity is framed when every row is satisfied. Anything less returns to the requester with the specific gap.

| Element | Framed when | Not framed when |
|---|---|---|
| Problem statement | One or two sentences describing the failure, in business terms, without naming a technology | It describes a tool, feature or product |
| Business owner | A named role-holder accepts accountability for the outcome | Ownership sits with IT, the CoE or "the business" in general |
| Affected roles | Roles and approximate numbers are listed | "Everyone" or a single enthusiast |
| Current cost | Time, delay, quality, risk or experience impact is described, with a measure | Impact is asserted without any measure |
| Expected outcome | The change sought and its direction are stated | Success is "using AI" or "going live" |
| Baseline | A measured value, or a dated plan to measure it | Absent with no plan |
| Strategic fit | The outcome it supports is named, or "none" is recorded honestly | Left blank |
| Backlog entry | Captured in the backlog with owner, status and an estimated value range | Discussed in a meeting or a chat thread but not recorded |

Record an early view of the problem type as a signal for suitability, not a decision. It shapes the conversation and
stops "AI" being assumed.

| Problem type | What it looks like | Signal for `opportunity-management:ai-suitability` |
|---|---|---|
| Process issue | Steps, hand-offs or ownership are broken | Likely process change, no AI |
| Education gap | People do not know how to use what they have | Likely training or an adoption scenario |
| Repetitive task | Fixed steps on structured inputs | Likely ordinary automation |
| Knowledge issue | People cannot find or trust answers held in owned content | Possibly an agent grounded in that content |
| Business data workflow | Judgement over business data across systems, with actions | Possibly an agent with connectors, often paired with automation |

## Practitioner approach

Keep the request verbatim, then set it aside. Ask the requester to describe the last time the problem happened: who was
involved, what they were trying to do, what went wrong and what it cost. Stories surface the real failure far better
than abstract questions, and they often reveal that the requested tool addresses a symptom.

When a request arrives solution-first, acknowledge the idea and redirect to the problem rather than refusing it. "An
agent might well help; before we design one, can you walk me through what happens today when a new starter asks about
their benefits?" Most people are happy to explain their work. The requested solution is recorded as one candidate for
`opportunity-management:ai-suitability` to test, not as the requirement.

Find the business owner early. The requester is often not the owner; a Champion or analyst may have spotted the problem
in someone else's process. Contact the owner, confirm they recognise the problem and accept accountability for the
outcome, and record their role on the canvas. If the owner disagrees that there is a problem, the opportunity stops
here, and that is a useful result.

Quantify current cost with whatever is available: system volumes, queue times, complaint counts, rework, or a short
time sample by the team. Precision matters less than having a reference point that can be measured again later. Where
nothing can be counted now, agree a light measurement over two to four weeks and hold the opportunity until it is in.

Write the problem statement in one or two sentences using the owner's words and a measure, and keep technology out of
it. "Contract managers spend most of Monday compiling site reports from emails, and a third of reports arrive late" is
framed. "We need an agent to write site reports" is not. Then write the expected outcome as a change in that measure.

Capture the opportunity in the backlog as soon as it has an owner, even before it is fully framed. The operating rule
is that work with no backlog entry is not a project and gets no resources, which is what turns intake from a
suggestion box into a pipeline. At capture the entry carries the business owner, a status, and a first estimated value
as a range; the return estimate and priority are added at assessment and prioritisation, never guessed now.

Note the problem type you think you are looking at, and say it out loud to the owner. Hearing "this sounds like a
hand-off problem rather than a knowledge problem" often changes the conversation more than any canvas.

Look for duplicates. If another unit has framed the same problem, merge the records and involve both owners; shared
problems are often better candidates for reuse. Finally, link the opportunity to a strategic outcome where one fits,
note early signs of data sensitivity or external reach for risk classification, and pass the framed opportunity on.

## Outputs

- A framed opportunity on the `opportunity-canvas` template: verbatim request, problem statement, business owner, affected roles, current cost, expected outcome, baseline or baseline plan, strategic fit, early problem type and early risk signals.
- A backlog entry at the capture stage, with owner, status and an estimated value range, on the `prioritisation-matrix` template's backlog register.
- A short reply to the requester explaining what happens next, or which gap must be closed first.
- Where the opportunity stops, a recorded reason (no owner, no agreed problem, duplicate) and any referral.

## Microsoft platform considerations

Not applicable, because a framed problem names no platform. Requested products are recorded only as candidate
solutions for `opportunity-management:ai-suitability`, which checks them against the current source records.

## Adoption considerations

How intake treats people decides whether they bring ideas again. Respond quickly, explain gaps in plain language, and
credit the person who raised the idea, including Champions who route opportunities. Make stopping a framed opportunity
feel like a result rather than a rejection.

## Knowledge considerations

Ask where the information involved in the work lives and who keeps it current. Unowned or scattered knowledge is
recorded as an early signal for suitability and for `knowledge-management:knowledge-inventory`; it is often the
real problem.

## Security and privacy considerations

Note at framing whether the work involves personal, confidential or regulated data, and whether outputs would reach
customers or the public. These are signals for `opportunity-management:risk-classification`, not decisions; framing
does not clear any data for use.

## Responsible AI considerations

Note whether the work involves decisions about people, money, safety or rights. If it does, flag it on the canvas so
risk classification and responsible AI review consider it from the start.

## Evaluation requirements

Not applicable to solution testing. The framing is checked by whether the business owner agrees with the problem
statement and baseline in writing, and whether a second reader could restate the problem without mentioning a tool.

## Value measures

The baseline and expected outcome recorded here are the reference points for every later value claim. The business
owner owns them. Measures are of the work and its outcomes, at team or process level, never of individual staff.

## Scale notes

### Starter

A short conversation and a one-page canvas, completed by the person leading AI with the business owner. Keep the
baseline simple; a two-week tally is often enough.

### Scale

A standard intake form feeding the canvas, a weekly triage that returns incomplete requests with specific gaps, and a
register where duplicates can be spotted.

### Enterprise

Business-unit spokes frame their own opportunities on the shared canvas; the hub checks quality and looks for problems
framed in several units that suggest an enterprise solution.

## Hand-offs

- To `opportunity-management:ai-suitability` to decide whether AI is the right answer.
- To `opportunity-management:risk-classification` once a candidate pattern is chosen.
- To `copilot-adoption:scenario-discovery` when the problem is clearly about individuals using tools they already have.

## Reviewer gates

Not applicable. Framing is an intake step and releases nothing; reviewer gates apply after risk classification.

## Failure modes

- A tool request is accepted as the requirement, and the solution is built for a problem nobody defined.
- The requester is recorded as owner, leaves or loses interest, and the solution is orphaned.
- No baseline is taken, so the benefit can never be demonstrated and the initiative cannot be judged at scale-or-stop.
- Framing becomes a bureaucratic hurdle, and people route ideas around intake.
- Ideas agreed in meetings never reach the backlog, so work starts with no owner, no baseline and no record.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Accept a technology or product as the problem statement.
- Advance an opportunity without a named business owner who agrees the problem exists.
- Invent or estimate a baseline and record it as measured.
- Dismiss a solution-first request without helping the requester describe the problem.
