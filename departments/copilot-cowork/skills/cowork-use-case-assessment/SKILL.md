---
name: cowork-use-case-assessment
description: Assesses whether a specific piece of work suits delegation to Copilot Cowork, or is better served by Copilot Chat, an agent, an automation, a Copilot Code build or no AI, by testing outcome clarity, verifiability, context access and consequence. Use when a person or team proposes handing a task to Cowork, when Cowork results disappoint, or when a team cannot decide between Cowork and an agent.
license: CC-BY-4.0
metadata:
  department: copilot-cowork
  lifecycle: Envision, Deliver
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3
  platforms: copilot-cowork, copilot-chat, m365-copilot, m365-agents, power-platform
  edition-support: starter, scale, enterprise
  reviewers: design-authority
  sources: ms-copilot-cowork-customise, ms-copilot-overview, ms-agents-extensibility, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# Cowork use-case assessment

## Purpose

Copilot Cowork is attractive because it promises to take a whole piece of work off someone's desk. That promise makes it
easy to delegate the wrong things: tasks whose outcome nobody can describe, work whose result nobody can check, or
recurring processes that should be an automation or an agent. This skill tests one proposed task against a short set of
criteria and gives a clear verdict: suits Cowork, suits Cowork with conditions, or belongs elsewhere, with the reason
recorded. It goes wrong when the verdict is driven by enthusiasm for the tool rather than by the shape of the work.

## When to use

- A person or team proposes delegating a specific task to Cowork and wants a sense check first.
- A Champion or adoption lead is triaging candidate Cowork scenarios from a team.
- Cowork has been tried on a task and the results were poor, and someone asks whether the task was ever a good fit.
- A team cannot decide whether a need is a Cowork task, an agent or an automation.

## When not to use

- Deciding at intake whether a framed business opportunity needs AI at all, across every pattern - use `opportunity-management:ai-suitability`.
- Assessing whether a reusable agent is warranted for a defined audience - use `m365-agents:agent-opportunity-assessment`.
- Deciding whether an outcome needs software built with Copilot Code - use `copilot-code:code-use-case-assessment`.
- Splitting a task that already suits Cowork into delegated and human-held parts - use `copilot-cowork:work-delegation-design`.
- Assessing a fixed, rule-based process for automation - use `automation:automation-assessment`.

## Questions to ask first

1. What is the finished output, in one sentence, and how would the person who asked for it know it is right?
2. How often is the task done, by whom, and does it vary each time or follow the same steps?
3. Which files, mail, meetings or data does the work draw on, and can the person delegating already open all of them?
4. What happens if the output is wrong and nobody notices: an awkward draft, a wasted hour, or a decision, payment or message with real effect?
5. Is there already an agent, automation, published prompt or tested Cowork task design that does most of this?

## Required inputs

- A plain description of the task and its finished output, from the person who would delegate it.
- The frequency of the task and the roles who do it today.
- The sources of information the task uses, at the level of "the project site and the supplier mail folder".
- The organisation's current position on Cowork use, from `copilot-cowork:cowork-governance` where it exists.

If the person cannot describe the finished output, the assessment stops there and the task goes back for clarification.
Never assume Cowork is enabled, licensed or permitted for a team; mark it to confirm.

## Decision framework

Score the task against each criterion. A task suits Cowork when every row is at least "acceptable".

| Criterion | Good fit | Acceptable | Poor fit, route elsewhere |
|---|---|---|---|
| Outcome clarity | The finished output can be described and recognised | Output known in outline, refined at a checkpoint | Nobody can say what done looks like |
| Verifiability | The delegator can check the output in a fraction of the time it took to make | Checking needs a second reviewer | Errors would not be visible to the checker |
| Shape of work | Multi-step, mixes reading, judging and drafting | A few steps with one clear judgement | A single question (Chat) or a fixed rule-based sequence (automation) |
| Context access | Sources exist, are current and are open to the delegator | Sources need tidying first | The work needs data the delegator cannot or should not see |
| Consequence | Output is a draft or proposal a person acts on | Output has effect only after explicit approval | Output acts on people, money or rights without a person deciding |
| Reuse pattern | One person or a small team, occasional or varied | A team repeats it with variations | Many people need the same capability daily (agent) |

Route by the failing row: unclear outcome goes back to the requester; single questions go to Copilot Chat; fixed
sequences go to automation; daily shared needs go to an agent; outcomes that are working software go to Copilot Code;
consequential decisions about people go through risk classification before anything else.

## Practitioner approach

Begin with the output, not the task. Ask the person to describe what will be on their screen when the work is finished:
a briefing pack, a comparison table, a set of draft replies, a reconciled tracker. If they describe activity ("go through
the supplier emails") rather than an output, keep asking until there is a thing that can be judged. Delegation without a
defined output produces long, plausible work that nobody can accept or reject.

Then test verifiability honestly. The value of delegating comes from the gap between the effort to produce and the
effort to check. If checking a supplier comparison means re-reading every contract, the gap has closed and Cowork adds
risk without saving time. Ask the delegator how they would spot an error, and whether they would be the right person to
spot it.

Look at the shape of the work. Cowork earns its place on multi-step work that mixes finding, reading, judging and
drafting across several sources. A one-off question is better asked in Copilot Chat. A process that runs the same way
every time on structured inputs is better as an automation, because it will behave identically on each run and can be
monitored. A capability that a whole department needs every day is better as an owned agent with tested knowledge.

Check context early. Cowork works with what the delegating person can reach, so stale folders, overshared sites and
mail threads with conflicting versions become stale, overshared or conflicting outputs. If the sources are clearly in poor
shape, the verdict is "suits Cowork with conditions" and the condition is `copilot-cowork:grounding-readiness`.

Weigh consequence last, because it changes the controls rather than the fit. Draft outputs a person reads and edits
suit Cowork well. Outputs that send, publish, file or change something need explicit approval steps, designed with
`copilot-cowork:human-checkpoint-design`. Work that would inform decisions about individuals, money or rights needs a
risk tier from `opportunity-management:risk-classification` before anyone delegates it.

Finally, look for reuse. Ask the Champion network or CoE whether a tested task design, agent or flow already exists.
Record the verdict, the criterion that decided it, any conditions and the route for work that does not fit. Keep the
record short: a few lines per task is enough, and similar tasks can share a precedent.

Product capability changes often. Before ruling a task in or out on a specific Cowork feature, plugin or limit, check the
current source records rather than relying on memory.

## Outputs

- A Cowork fit verdict per task: suits Cowork, suits Cowork with conditions, or route elsewhere, with the deciding criterion.
- For tasks that fit, the conditions to meet first and the hand-off to delegation and context design.
- For tasks that do not fit, a referral to the right route with a one-line reason the requester can understand.

## Microsoft platform considerations

Copilot Chat, Copilot in the Microsoft 365 apps, Copilot Cowork, agents and Power Automate overlap at the edges. Use the
shape of the work to choose, then confirm current Cowork capability, customisation through plugins, skills and custom
instructions, and availability in the source records (`ms-copilot-cowork-customise`, `ms-agents-extensibility`). Do not
promise a feature to a team until the source record and the organisation's governance position both confirm it.

## Adoption considerations

A "route elsewhere" verdict is still help: tell the requester where to go and why. Teams who hear only "no" stop
experimenting. Collect good-fit tasks as candidate scenarios for `copilot-cowork:cowork-adoption`.

## Knowledge considerations

Fit depends on the condition of the sources the task draws on. Name them in the verdict and flag obvious problems
(duplicates, out-of-date material, unclear owners) for `copilot-cowork:grounding-readiness`.

## Security and privacy considerations

Cowork acts with the delegating person's access. If the task would surface content that person should not see, or move
information to an audience who should not see it, the task does not fit until access is fixed. Route doubts to
`security-privacy:data-exposure-review`.

## Responsible AI considerations

Tasks that inform decisions about people, money, safety or rights are not ruled out automatically, but they need a risk
tier and explicit human decision points before delegation. Some tasks should not be delegated at all; say so plainly.

## Evaluation requirements

Not applicable at assessment stage beyond the verifiability criterion; evidence that a task works reliably is gathered
later in `copilot-cowork:workflow-validation`.

## Value measures

Record the current effort and delay for the task (from the team's own estimate or records) as the baseline, and the
measure the team will use, such as turnaround or rework. Measure at team or role level, never for individuals.

## Scale notes

### Starter

A short conversation and a few lines per task, held by whoever leads AI adoption. Most early tasks are drafting and
summarising work that fits well with a final human review.

### Scale

Champions run the assessment with teams using the shared criteria, and the CoE keeps a library of precedents so similar
tasks get the same verdict across business units.

### Enterprise

Business-unit spokes assess locally against the shared criteria; anything at risk tier 2 or above, or any task that
sends, files or changes records, is confirmed by the hub before delegation.

## Hand-offs

- To `copilot-cowork:work-delegation-design` when the task suits Cowork.
- To `copilot-cowork:grounding-readiness` when sources are a condition.
- To `opportunity-management:risk-classification` when the output could affect people, money or rights.
- To `m365-agents:agent-opportunity-assessment`, `automation:automation-assessment` or `copilot-code:code-use-case-assessment` when the work belongs elsewhere.

## Reviewer gates

From risk tier 2, the verdict is open to challenge by `design-authority` through `design-authority:platform-fit-review`
for choosing Cowork where an owned agent or automation would be safer or more reliable. Below tier 2, the CoE lead or
adoption lead records the verdict.

## Failure modes

- A task is delegated because the tool is new, not because the output can be defined and checked.
- A recurring process is run through Cowork by many people with different instructions, producing inconsistent results that an automation would have avoided.
- The delegator cannot verify the output, so errors pass straight through into decisions.
- Cowork is promised for a team before the organisation has decided its governance position or confirmed availability.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Approve a task for Cowork when nobody can describe its finished output.
- Treat Cowork as the answer for a recurring, rule-based process that an automation would run more reliably.
- Delegate work that decides something about a person without a risk tier and an explicit human decision.
- Assert Cowork availability, licensing or limits from memory.
