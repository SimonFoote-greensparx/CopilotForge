---
name: multi-step-work-design
description: Breaks a delegated Copilot Cowork task into ordered steps, each with a named intermediate output, its inputs, a completion test and a safe restart point, so long-running work can be followed, checked and resumed. Use when a Cowork task spans several sources or stages, when long runs go off course part-way, or when a team wants a repeatable structure for complex delegated work.
license: CC-BY-4.0
metadata:
  department: copilot-cowork
  lifecycle: Deliver, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3
  platforms: copilot-cowork, m365-copilot
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-cowork-customise, ms-copilot-overview
  status: draft
  authors: Simon Foote
---

# Multi-step work design

## Purpose

Complex work delegated in one instruction tends to fail quietly: Cowork makes an early assumption, builds on it for
twenty minutes and returns a polished output resting on the wrong foundation. This skill structures delegated work into
steps, each producing an intermediate output a person could look at, with clear inputs, a completion test and a point
from which the work can restart. The structure makes long runs visible, lets checkpoints sit where they matter and turns
a one-off success into something repeatable. It goes wrong when steps mirror how a person would click through
applications rather than the outputs the work actually needs.

## When to use

- A Cowork task draws on several sources or passes through several stages, such as gather, analyse, draft and assemble.
- Long runs go off course part-way and nobody can see where the error entered.
- A team wants a repeatable structure for a recurring piece of complex work.
- A task needs checkpoints and there is no clear step boundary to hang them on.

## When not to use

- Deciding what to delegate and what stays human - use `copilot-cowork:work-delegation-design`.
- Writing the goal, sources and constraints the task needs - use `copilot-cowork:task-context-design`.
- Designing the approvals between steps - use `copilot-cowork:human-checkpoint-design`.
- Designing a fixed, rule-based sequence that should run as a flow - use `automation:automation-process-design`.
- Designing autonomous agentic workflows in custom code - use `ai-foundry:agentic-workflow-design`.

## Questions to ask first

1. What are the natural stages of this work, described as things produced rather than actions taken?
2. Which steps depend on the output of an earlier one, and which could be done independently?
3. At which step is the most important judgement made, and what would go wrong downstream if it were wrong?
4. If the run stopped half-way, what would the person need in order to pick it up without starting again?
5. Which intermediate outputs would be useful in their own right, even if the run never finished?

## Required inputs

- The delegated parts and their levels from `copilot-cowork:work-delegation-design`.
- The goal and definition of done from `copilot-cowork:task-context-design`, or a draft of them.
- An example of the finished output, or a description of its structure.

Where the finished output's structure is unknown, design only the first two or three steps and add a direction check
before the rest. Never invent intermediate outputs that the work does not need just to make the plan look thorough.

## Decision framework

Each step must meet all five tests.

| Test | Passes when | Fails when |
|---|---|---|
| Named output | The step produces something a person can open and judge (a source list, a table, a draft section) | The step is an activity with no artefact |
| Clear inputs | Inputs are earlier outputs or named sources | The step "uses what it finds" |
| Completion test | A plain statement of what complete looks like | Complete means "when Cowork stops" |
| Right size | One main judgement or transformation | Several unrelated judgements bundled together |
| Restart point | The step can be re-run from its inputs without redoing earlier work | A failure means starting from the beginning |

Sequence by dependency: gather before analyse, analyse before draft, draft before assemble. Put the step carrying the
most important judgement early enough that a checkpoint after it saves real rework. Keep most tasks to between three and
seven steps; more usually means the task is two tasks.

## Practitioner approach

Start from the finished output and work backwards. Ask what the last step assembles, then what each part of that
assembly needs, until you reach the raw sources. A quarterly supplier review might resolve into: a confirmed source list,
a table of delivery metrics per supplier, a short list of at-risk suppliers with reasons, draft recommendations, and
the assembled briefing. Each of those is something a person could look at and say "yes" or "not quite".

Name every step by its output, not its action. "At-risk supplier table" is better than "analyse suppliers", because it
forces a decision about what the table contains and makes the completion test obvious. If you cannot name the output,
the step is probably a means to an end inside another step and should be merged.

Find the step that carries the key judgement. In the supplier example it is choosing which suppliers count as at risk;
everything after builds on that choice. Put a judgement checkpoint immediately after it and make sure the step's output
carries its evidence, so the person approving can disagree on the merits. This one placement prevents most of the
"polished but wrong" failures teams experience.

Make each step restartable. Intermediate outputs should be saved where the delegator can find them, named consistently,
so that if the run stops or a checkpoint sends work back, it resumes from the last good output. Restartable steps also
let a person take over part of the work by hand without losing what Cowork has done.

Look for independent steps. Where two analyses do not depend on each other, they can be produced and reviewed
separately, which keeps each smaller and easier to check. Resist the temptation to split work so finely that the
delegator spends more time reviewing steps than they would have spent doing the task.

Record the step outline on the `cowork-task-design` template, with each step's output, inputs, completion test and
restart point, then try it on one real instance. Watch where the run drifts or where you had to intervene, and adjust
the step boundaries. Once stable, hand it to `copilot-cowork:workflow-validation`.

## Outputs

- A step outline in the `cowork-task-design` template: for each step, the named output, inputs, completion test, restart point and any checkpoint after it.
- A note of where intermediate outputs are stored and how they are named.
- The step carrying the key judgement, flagged for `copilot-cowork:human-checkpoint-design`.

## Microsoft platform considerations

Cowork plans and carries out multi-step work within Microsoft 365, and its planning behaviour, visibility of progress and
handling of pauses evolve. Check current behaviour in the source records (`ms-copilot-cowork-customise`,
`ms-copilot-overview`) and treat the step outline as the specification of what you expect, so changes in product behaviour
show up as deviations you can see.

## Adoption considerations

A clear step outline makes delegated work less mysterious and easier to trust. Share example outlines for common work
types so teams learn to think in outputs rather than clicks, and so new users can follow a run and step in when needed.

## Knowledge considerations

The first step of most outlines is gathering sources. Make its output a confirmed source list, so stale or missing
content is visible before analysis starts and can be routed to `copilot-cowork:grounding-readiness`.

## Security and privacy considerations

Intermediate outputs can concentrate sensitive information drawn from several places. Store them where only the intended
audience can reach them, and delete or archive them according to the organisation's retention rules once the work is done.

## Responsible AI considerations

Where a step makes a judgement about people, such as prioritising cases or summarising complaints about individuals, keep
that step at a delegation level where a person decides, and make the evidence visible in its output.

## Evaluation requirements

Each step's completion test becomes a check in `copilot-cowork:workflow-validation`. Validation should confirm that
intermediate outputs, not only the final output, meet their tests.

## Value measures

Track at team level how often runs complete without restarting from the beginning, and how much rework the final output
needs, against the baseline for the task. Never use run data to compare individuals.

## Scale notes

### Starter

Three to five steps written as outputs, with one checkpoint after the key judgement, is enough for most tasks.

### Scale

Publish step outlines for common work types in the shared task library so teams start from a tested structure.

### Enterprise

Business units maintain outlines for their recurring complex work; outlines for tasks at risk tier 2 or above are
reviewed centrally alongside their checkpoint design.

## Hand-offs

- To `copilot-cowork:human-checkpoint-design` with the step carrying the key judgement and any pre-effect steps.
- To `copilot-cowork:task-context-design` with the inputs each step needs.
- To `copilot-cowork:workflow-validation` once the outline is stable.

## Reviewer gates

Not applicable as a separate gate; the step outline is reviewed as part of the task design through
`copilot-cowork:human-checkpoint-design` and, from risk tier 2, by `responsible-ai` through
`responsible-ai:human-oversight`.

## Failure modes

- Steps describe clicks and actions rather than outputs, so nobody can tell whether a step succeeded.
- The key judgement sits late in the run, so errors are found only in the polished final output.
- Intermediate outputs are not saved, so any failure means starting again.
- Work is split so finely that reviewing the steps takes longer than doing the task.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Define a step without a named output and a completion test.
- Place the key judgement where no checkpoint can catch it before later steps build on it.
- Leave intermediate outputs containing sensitive content where a wider audience can reach them.
- Design more steps than the delegator can realistically review.
