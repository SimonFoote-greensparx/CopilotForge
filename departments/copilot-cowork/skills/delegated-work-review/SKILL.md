---
name: delegated-work-review
description: Sets and applies the review a person carries out on a finished Copilot Cowork output before it is sent, filed, published or acted on, checking it against the definition of done, its sources, the audience and any actions taken, with a proportionate depth by consequence. Use when someone is about to use delegated output, when errors from Cowork reached others, or when a team needs a shared standard for checking delegated work.
license: CC-BY-4.0
metadata:
  department: copilot-cowork
  lifecycle: Deliver, Assure
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3
  platforms: copilot-cowork, m365-copilot
  edition-support: starter, scale, enterprise
  reviewers: responsible-ai
  sources: ms-copilot-cowork-customise, ms-responsible-ai, ms-copilot-overview
  status: draft
  authors: Simon Foote
---

# Delegated work review

## Purpose

The final review is where the person who delegated takes the output back and makes it their own. It is the last chance
to catch a wrong figure, a missing caveat, a sentence that should never reach that audience, or an action that should not
happen. This skill gives teams a proportionate review standard for Cowork outputs and a way to apply it, so review is
neither a skim of a confident-looking document nor a full redo that removes the point of delegating. It goes wrong when
fluent, well-formatted output is taken as evidence of accuracy.

## When to use

- A person is about to send, file, publish or act on an output produced by Cowork.
- An error from delegated work has reached a customer, colleague or decision and the team wants to prevent a repeat.
- A team needs a shared standard for what "checked" means for delegated outputs.
- A manager asks how the team assures work that Cowork helped to prepare.

## When not to use

- Designing the approvals that happen during the run - use `copilot-cowork:human-checkpoint-design`.
- Testing a task design before people rely on it - use `copilot-cowork:workflow-validation`.
- Reviewing code produced with an AI coding agent - use `copilot-code:generated-code-review`.
- Teaching general habits for verifying Copilot responses in everyday use - use `m365-copilot:prompting-practice`.
- Formal oversight review of a tier 2 or higher solution - use `responsible-ai:human-oversight`.

## Questions to ask first

1. Who will see or rely on this output, and what will they do because of it?
2. What was the definition of done, and does this output meet it?
3. Which claims, figures or statements in the output matter most, and can each be traced to a source?
4. Did the run take any action already, such as saving, sharing or scheduling, that needs checking or undoing?
5. Would you be comfortable putting your name to this output as if you had written it yourself?

## Required inputs

- The output and, where available, the intermediate outputs and sources Cowork used.
- The definition of done from the task design.
- The intended audience and use of the output.
- The risk tier or, if none, the consequence level from the review depth table below.

If the sources cannot be seen, the reviewer cannot verify the key claims, and the output is treated as a draft to be
checked by hand. Never review against an imagined standard; use the definition of done.

## Decision framework

Set review depth by what the output will do.

| Consequence | Example | Review depth |
|---|---|---|
| Low: internal draft for the delegator's own use | Notes to prepare for a meeting | Read for sense, check anything you will repeat |
| Moderate: shared internally or informs a team decision | Team briefing, project status summary | Check key claims and figures against sources, check audience fit |
| High: reaches external parties or informs decisions with real effect | Supplier letters, board paper, customer reply | Full check of every factual claim, tone and recipients; second reviewer where the risk tier requires |
| Affects individuals' rights, money or safety | Anything touching named people's cases | Delegated output is input only; a person with authority decides and records the decision |

Every review covers five checks: meets the definition of done; key claims trace to sources; nothing inappropriate for the
audience; caveats and gaps stated; any actions taken are correct. An output that fails any check at the required depth is
corrected or not used.

## Practitioner approach

Start by reading the output as its recipient would, not as its commissioner. Ask what they will take from it and what they
will do next. This shifts attention from "does this look finished" to "is this right and safe for them", and it often
reveals a missing caveat or a sentence pitched at the wrong audience.

Identify the claims that matter. Most outputs have a few statements that carry the weight: a figure in a summary, a
recommendation, a date, a commitment. Trace each to its source. If Cowork cited sources, open them and confirm the claim
is actually there and from the authoritative version. If it did not, the depth of review rises, because nothing in the
output can be taken on trust. Fluency is not evidence: a confident paragraph can rest on a misread table.

Look for what is missing as well as what is wrong. Did the output state where sources disagreed or were silent, as the
task design asked? Were the known awkward cases handled? An output that is complete only because gaps were quietly
filled with plausible content fails review, however polished it looks.

Check audience fit. Delegated work draws on everything the delegator can reach, so sensitive details from one context can
appear in an output for another: a personal circumstance in a team update, an internal margin in a customer letter.
Read specifically for names, figures and internal references that should not travel.

Check what already happened. If the run saved, shared or scheduled anything, confirm it went to the right place and the
right people, and undo anything that should not stand.

Then decide and own it. The person who uses the output is accountable for it, in the same way as for work drafted by a
colleague. If the review found errors, note the pattern: an error that recurs across outputs points to a fix in the task
design, the sources or the checkpoints, and should go back through `copilot-cowork:workflow-validation` rather than being
corrected by hand every time.

## Outputs

- A review standard for the team, with depth by consequence and the five checks, recorded in the `cowork-task-design` template for shared designs.
- For each high-consequence output, a brief review note: who reviewed, what was checked, corrections made and any second reviewer.
- A log of recurring error patterns at team level, referred back to the task design owner.

## Microsoft platform considerations

How Cowork shows its sources, intermediate outputs and actions taken may change with product updates. Confirm current
behaviour in the source records (`ms-copilot-cowork-customise`, `ms-copilot-overview`) and adapt the review routine to what
is visible. Where an output cannot show its sources, plan for a deeper manual check.

## Adoption considerations

People adopt review habits when the standard is short and proportionate. Teach the five checks and the depth table, and
share real examples of errors that review caught. Avoid messages that imply Cowork outputs need no checking; they erode
trust when the first error appears.

## Knowledge considerations

Errors traced to stale or conflicting sources should reach the source owner through `copilot-cowork:grounding-readiness`
rather than being corrected silently in each output.

## Security and privacy considerations

Read high-consequence outputs specifically for personal data, confidential figures and internal references that should not
reach the audience. Where something sensitive appears, find out which source supplied it and whether that source is
overshared, and report it.

## Responsible AI considerations

The reviewer remains accountable for what is used. Where outputs inform decisions about individuals, the output is input
to a human decision, never the decision itself. Consider whether recipients should be told AI helped prepare the output,
in line with the organisation's transparency position.

## Evaluation requirements

Not applicable as a separate evaluation; recurring review findings feed `copilot-cowork:workflow-validation`, which
re-tests the design.

## Value measures

Track, at team level, how many outputs pass review with light edits, how many need substantial correction and how many
errors reach recipients, against the pre-Cowork baseline for the work. Never report review results for individuals.

## Scale notes

### Starter

Teach the five checks and the depth table to everyone using Cowork, and ask teams to note errors that reached others.

### Scale

Build the review standard into every shared task design, collect recurring error patterns at team level and route them to
design owners.

### Enterprise

Set the depth table centrally, with business units adding domain-specific checks (for example regulated communications),
and require second reviewers for high-consequence outputs at risk tier 2 and above.

## Hand-offs

- To `copilot-cowork:workflow-validation` with recurring error patterns.
- To `copilot-cowork:grounding-readiness` with source-related errors.
- To `responsible-ai:human-oversight` from risk tier 2 for outputs that affect individuals.

## Reviewer gates

From risk tier 2, `responsible-ai` reviews the review standard to confirm high-consequence outputs receive a real human
decision with appropriate authority. Findings are blocking or advisory; absence of review for outputs that affect
individuals is blocking.

## Failure modes

- Polished formatting is taken as evidence of accuracy, and a misread figure goes to the board.
- Gaps filled with plausible content pass review because nobody checked what was missing.
- Sensitive details from one context appear in an output for another audience.
- The same error is corrected by hand every week instead of being fixed in the task design.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Send, publish or act on a high-consequence output without checking its key claims against sources.
- Treat delegated output as the decision on a matter affecting an individual.
- Attribute accountability for a used output to the AI rather than the person who used it.
- Use review records to rank or monitor individual staff.
