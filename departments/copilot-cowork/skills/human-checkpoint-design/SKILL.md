---
name: human-checkpoint-design
description: Designs the human checkpoints inside delegated Copilot Cowork work - where the run pauses, who confirms, what evidence they see, what they may change and what happens on rejection - so approvals are real decisions rather than reflex clicks. Use when a Cowork task will send, file or change something, when a checkpoint is being skipped or rubber-stamped, or when a reviewer asks how people stay in control of delegated work.
license: CC-BY-4.0
metadata:
  department: copilot-cowork
  lifecycle: Deliver, Assure
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3
  platforms: copilot-cowork, m365-copilot
  edition-support: starter, scale, enterprise
  reviewers: responsible-ai
  sources: ms-copilot-cowork-customise, ms-responsible-ai, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Human checkpoint design

## Purpose

A checkpoint is the moment a person decides whether delegated work should continue or take effect. In Copilot Cowork it
is the main control that keeps people in charge of multi-step work, and it only works if the person has the right
evidence, the time and the authority to say no. This skill designs each checkpoint in a delegated task: where it sits,
who confirms, what they see, what they can change and what happens if they reject. Checkpoints usually fail by being
too many and too shallow, so people approve by habit, or by sitting after the point where an error has already had effect.

## When to use

- A Cowork task will send, publish, file, schedule or change something, and approvals need designing.
- A team reports that people approve checkpoints without reading them.
- A multi-step task makes a judgement mid-way that a person should confirm before later steps build on it.
- A reviewer asks how human control is maintained in a delegated workflow.

## When not to use

- Deciding which parts of the work are delegated and who is accountable - use `copilot-cowork:work-delegation-design`.
- Reviewing a finished output before it is used - use `copilot-cowork:delegated-work-review`.
- Designing approval steps inside a Power Automate flow - use `automation:human-in-the-loop`.
- Formal reviewer assessment of human oversight for a tier 2 or higher solution - use `responsible-ai:human-oversight`.

## Questions to ask first

1. At which points could an error made by Cowork become expensive, visible to others or hard to undo?
2. Who has the knowledge and the authority to approve at each point, and are they available when the run reaches it?
3. What does the approver need to see to make a real decision: the proposed action, the sources, the reasoning, the alternatives?
4. What can the approver do besides approve: edit, redirect, ask for more evidence, stop the run?
5. What happens to the work if nobody responds?

## Required inputs

- The delegation map, with delegation levels and take-back triggers, from `copilot-cowork:work-delegation-design`.
- The step outline from `copilot-cowork:multi-step-work-design`.
- The risk tier, where set.
- The organisation's position on which actions need approval, from `copilot-cowork:cowork-governance`.

If the approver for a checkpoint cannot be named, the step after it is not delegated until one is. Never design a
checkpoint that assumes an approver's availability without asking them.

## Decision framework

Place checkpoints by consequence, not by step count.

| Checkpoint type | Place it | Approver sees | Required when |
|---|---|---|---|
| Direction check | After Cowork has gathered sources and proposed an approach | Sources found, sources missing, proposed plan | The task is long or the sources are uncertain |
| Judgement check | After an interim conclusion that later steps depend on | The conclusion, the evidence and the alternatives considered | A wrong judgement would invalidate later work |
| Pre-effect approval | Immediately before anything is sent, filed, published or changed | The exact action, its recipients or targets, and what changes | Any delegation level D3 action |
| Exception stop | Whenever a take-back trigger fires | What triggered it and the state of the work | Always, for every task with defined triggers |

Rules: every pre-effect approval shows the exact action, not a summary of it; a checkpoint with no realistic way to
reject is removed or redesigned; no more than three routine checkpoints in a run unless the risk tier demands it, because
volume breeds rubber-stamping; silence never counts as approval.

## Practitioner approach

Walk the step outline and mark each point where a mistake would change what happens next or what other people see.
Those are the candidates. Most tasks need fewer checkpoints than teams first propose: a direction check early, one
judgement check if the work turns on an interim conclusion, and a pre-effect approval before anything leaves the
delegator's hands. Ten approvals in a twenty-minute run teach people to click through.

For each checkpoint, design what the approver sees. A pre-effect approval for sending supplier letters should show the
actual letters and the actual recipients, not "twelve letters ready to send". A judgement check should show the
evidence behind the conclusion and what else was considered, so the approver can disagree on the merits. If the approver
would need to reopen every source to decide, the checkpoint is too late or the output too opaque; restructure the step so
the evidence travels with the proposal.

Name the approver by role and confirm they have the authority to decide. The delegator is often the right person, but
not always: an external commitment may need a manager, and a message to a regulator may need someone with that remit.
Ask whether they will be available when the run reaches the checkpoint; a checkpoint that waits for a person on leave
becomes a reason to bypass the control.

Design the rejection path as carefully as the approval. The approver should be able to edit the proposal, send the step
back with a reason, ask for more evidence, or stop the run. Record what Cowork does with each response, and make
"stop" leave the work in a recoverable state. Decide what happens on silence: the run waits, it does not proceed.

Connect checkpoints to the take-back triggers from the delegation map. Each trigger should produce an exception stop
that tells the person why the run paused. Typical triggers are conflicting sources, a named individual appearing in a
draft, or a value outside an expected range.

Write the checkpoint design into the `cowork-task-design` template and test it in `copilot-cowork:workflow-validation`
by deliberately planting an error before each checkpoint and confirming the approver can see it. A checkpoint that does
not catch a planted error in testing will not catch a real one.

## Outputs

- A checkpoint schedule in the `cowork-task-design` template: each checkpoint's type, position, approver role, evidence shown, permitted responses and behaviour on silence.
- Exception stops linked to each take-back trigger.
- A planted-error test list for `copilot-cowork:workflow-validation`.

## Microsoft platform considerations

How Cowork pauses for confirmation and what it can show at that point depends on the current product and on the plugins
and skills in use. Confirm the current behaviour in the source records (`ms-copilot-cowork-customise`) and design to it.
Where an action runs through a plugin or connector into another system, check whether that system also needs its own
approval rather than relying on the Cowork checkpoint alone.

## Adoption considerations

Explain to approvers why each checkpoint exists and what they are expected to look for. A one-line "what to check" note
at each checkpoint improves attention more than any reminder. Fewer, better checkpoints build trust; many shallow ones
build fatigue.

## Knowledge considerations

Direction checks are the moment to catch wrong or stale sources. Make sure the approver sees which sources Cowork used and
which it could not find, so gaps reach `copilot-cowork:grounding-readiness`.

## Security and privacy considerations

Pre-effect approvals must show recipients and destinations explicitly, so an approver can spot information heading to the
wrong audience. From risk tier 2, any checkpoint guarding external sharing is reviewed with the `security-privacy` reviewer.

## Responsible AI considerations

Checkpoints are the evidence that people remain in control. They must give the approver real information and a real
choice. Where the work affects individuals, the approver must be someone with authority over that decision, and the
design goes to `responsible-ai:human-oversight` from risk tier 2.

## Evaluation requirements

Each checkpoint must catch a planted error in validation. Record the planted-error results as part of the evidence in
`copilot-cowork:workflow-validation`.

## Value measures

Measure, at team level, how often checkpoints lead to edits or rejections and how long runs wait at them. A checkpoint
that never changes anything may be unnecessary; one that always changes things suggests the context or steps need work.
Never report approval behaviour for named individuals.

## Scale notes

### Starter

One pre-effect approval before anything leaves the delegator's hands, plus exception stops for obvious triggers, is enough
for most early tasks.

### Scale

Use the four checkpoint types consistently across shared task designs, and review checkpoint statistics at team level to
remove useless checkpoints and strengthen weak ones.

### Enterprise

Set organisation-wide rules for which actions always need pre-effect approval and by which role, applied by business
units in their task designs and checked centrally at risk tier 2 and above.

## Hand-offs

- To `copilot-cowork:workflow-validation` with the planted-error test list.
- To `copilot-cowork:delegated-work-review` for the final review standard.
- To `responsible-ai:human-oversight` from risk tier 2.

## Reviewer gates

From risk tier 2, `responsible-ai` reviews whether checkpoints give approvers real evidence, real choice and appropriate
authority. Findings are blocking or advisory; a missing pre-effect approval on an external action is blocking.

## Failure modes

- Too many routine checkpoints, so approvers click through and miss the one that mattered.
- The approval shows a summary rather than the exact action, so the wrong recipient list is approved.
- The checkpoint sits after the effect, so it records an error rather than preventing it.
- Silence is treated as consent and the run proceeds while the approver is away.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Let a delegated task send, publish or change records without a pre-effect approval.
- Treat no response as approval.
- Design a checkpoint the approver has no realistic way to reject.
- Use checkpoint data to monitor or rank individual approvers.
