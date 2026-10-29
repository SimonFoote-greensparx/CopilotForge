---
name: task-context-design
description: Designs the context pack a Copilot Cowork task needs - the goal, the definition of done, the named inputs and sources, constraints, examples and the custom instructions or skills to apply - and records it as a reusable task design. Use when a delegated task gives vague or inconsistent results, when a team wants to share a task design others can reuse, or before running a Cowork task that draws on several sources.
license: CC-BY-4.0
metadata:
  department: copilot-cowork
  lifecycle: Deliver, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3
  platforms: copilot-cowork, m365-copilot, sharepoint
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-cowork-customise, ms-copilot-overview, ms-copilot-privacy
  status: draft
  authors: Simon Foote
---

# Task context design

## Purpose

Copilot Cowork does what its context lets it do. A task described in one line ("pull together the quarterly supplier
review") leaves Cowork to guess the audience, the sources, the format and the standard, and it will guess differently
each time. This skill designs the context pack for a delegated task: the goal and definition of done, the specific inputs
and sources, the constraints, a worked example where one helps, and which organisational skills or custom instructions
apply. It goes wrong when context is treated as clever prompting rather than as a specification someone else could pick
up and reuse.

## When to use

- A delegated task produces vague, inconsistent or off-target results and the context is the likely cause.
- A team wants to write down a task design that colleagues can reuse with the same results.
- A task draws on several sources and Cowork needs to know which ones count and which to ignore.
- An organisational skill or custom instruction is being considered to carry standing context for a type of work.

## When not to use

- Deciding which parts of the work are delegated at all - use `copilot-cowork:work-delegation-design`.
- Breaking the task into steps with intermediate outputs - use `copilot-cowork:multi-step-work-design`.
- Checking whether the named sources are current, owned and appropriately shared - use `copilot-cowork:grounding-readiness`.
- Teaching everyday prompting habits for Copilot Chat and the apps - use `m365-copilot:prompting-practice`.
- Writing instructions for a reusable agent - use `m365-agents:agent-instructions`.

## Questions to ask first

1. Who is the output for, and what will they do with it?
2. What does "done" look like: format, length, structure, level of detail and the standard it must meet?
3. Which specific files, folders, mail threads, meetings or data should Cowork use, and which should it ignore even if it finds them?
4. What constraints apply: house style, terminology, confidentiality, things it must not say or assume?
5. Is there a past example of good output that could show the standard, and is it safe to use?
6. Does an organisational skill, plugin or custom instruction already carry some of this context?

## Required inputs

- The delegation map from `copilot-cowork:work-delegation-design`, so context covers only the delegated parts.
- The step outline from `copilot-cowork:multi-step-work-design` where the task has several steps.
- The list of candidate sources with their location and apparent owner.
- Any house style, templates or standards the output must follow.

If the audience or the definition of done is unknown, mark it to confirm and do not run the task beyond a trial. Never
invent a source location or a standard; ask the person who owns the work.

## Decision framework

A context pack is complete when every element below is present or deliberately marked as not needed.

| Element | Complete when | Warning sign |
|---|---|---|
| Goal | One sentence naming the output and its audience | Describes activity rather than output |
| Definition of done | Format, structure, length and quality standard stated | "Make it good" or "the usual" |
| Inputs | Named sources with locations, plus anything the delegator supplies at run time | "Everything about the project" |
| Exclusions | Sources, periods or topics to ignore | Silence, so archives and drafts are mixed in |
| Constraints | Style, terminology, confidentiality and must-not rules | Constraints only in the delegator's head |
| Example | A short, safe example of good output, or a note why none is used | A real example containing personal data |
| Standing context | Which organisational skills or custom instructions apply | The same standing rules retyped in every task |
| Uncertainty rule | What Cowork does when sources conflict or are silent | Cowork fills gaps with plausible content |

Put context in the right place: standing rules that apply to many tasks belong in an organisational skill or custom
instruction governed by `copilot-cowork:cowork-governance`; task-specific facts belong in the task design.

## Practitioner approach

Write the goal and the definition of done first, in the words of the person who will receive the output. "A two-page
briefing for the operations director on supplier delivery performance last quarter, with the three suppliers most at
risk and a recommended action for each" gives Cowork a target it can hit and the delegator a standard to check against.
If you cannot write that sentence, the work is not ready to delegate.

Name the inputs precisely. Point to the specific library, folder, mail folder, meeting series or file, and say which
time period matters. Then name what to ignore: superseded drafts, archive folders, a previous supplier list. Cowork works
with whatever the delegator can reach, and a broad search across a messy estate will find the wrong version as readily as
the right one. Precision here prevents most of the errors people later blame on the model.

Write constraints as plain rules. House style, approved terminology, the audience's reading level, what must not be
included (named individuals' personal circumstances, unreleased figures) and what must be cited. Add an uncertainty
rule: when sources disagree or say nothing, Cowork should flag it at a checkpoint rather than choose or invent.

Use an example when the standard is hard to describe. A short, fictional or cleaned example of good output often
communicates format and tone better than a paragraph of rules. Never use a real document containing personal or
confidential data as an example unless its audience matches the task's audience.

Separate standing context from task context. If every finance team task repeats the same style rules and glossary, that
is a candidate for an organisational skill or custom instruction, owned and reviewed through governance. Task designs
then refer to it rather than copying it, so a change to the standard reaches every task at once.

Record the pack on the `cowork-task-design` template, try it on one real instance, and compare the output with the
definition of done. Adjust the context, not just the wording: most poor results trace back to a missing exclusion, an
undefined audience or an unstated standard. Once it works, hand it to `copilot-cowork:workflow-validation` before
others rely on it, and give it an owner and a review date so it does not drift out of date with its sources.

## Outputs

- A task design on the `cowork-task-design` template: goal, definition of done, inputs and exclusions, constraints, example, standing context, uncertainty rule, owner and review date.
- A list of sources for `copilot-cowork:grounding-readiness`.
- Candidate standing context (style rules, glossaries) proposed as organisational skills or custom instructions.

## Microsoft platform considerations

Cowork can be customised with plugins, skills and custom instructions, and the balance between them shapes where context
should live. Confirm what the organisation has enabled and how each is scoped and shared in the source records
(`ms-copilot-cowork-customise`). Cowork grounds on Microsoft 365 work context within the user's permissions
(`ms-copilot-privacy`), so precise source naming matters more than prompt wording.

## Adoption considerations

Good task designs spread when they are easy to find and copy. Publish validated designs in a shared library with the
owner named, and let `copilot-cowork:cowork-adoption` use them as starting points for teams.

## Knowledge considerations

The pack depends on sources being findable and current. Prefer a small set of curated, owned sources over broad searches,
and record the owner of each so stale content can be fixed at source rather than worked around in the task.

## Security and privacy considerations

Check that examples and named sources match the audience of the output. Do not paste confidential content into standing
context that will be shared widely. From risk tier 2, sources with sensitive content go to `security-privacy:data-exposure-review`.

## Responsible AI considerations

The uncertainty rule is a responsible AI control: it stops Cowork from filling gaps with plausible but unsupported
content. Where the output describes or affects people, require sources to be cited so a reviewer can check them.

## Evaluation requirements

The definition of done is the acceptance standard for `copilot-cowork:workflow-validation` and
`copilot-cowork:delegated-work-review`. Write it so that two reviewers would agree whether an output meets it.

## Value measures

Track first-time acceptance of outputs (used with light edits) and rework at team level, against the baseline from the
use-case assessment. A rising rework rate usually signals a context pack that has drifted from its sources.

## Scale notes

### Starter

A half-page design per task, kept with the team's files, is enough. Focus on goal, definition of done, named sources and
exclusions.

### Scale

Keep a shared library of task designs with owners and review dates, and move repeated standing context into governed
organisational skills or custom instructions.

### Enterprise

Business units maintain their own task libraries on the shared template; standing context with organisation-wide reach
is approved centrally and versioned.

## Hand-offs

- To `copilot-cowork:grounding-readiness` with the named sources.
- To `copilot-cowork:human-checkpoint-design` with the uncertainty rule and points where sources may conflict.
- To `copilot-cowork:workflow-validation` before others reuse the design.
- To `copilot-cowork:cowork-governance` for proposed organisational skills or custom instructions.

## Reviewer gates

From risk tier 2, `security-privacy` checks that named sources, examples and standing context do not draw sensitive
content into outputs for a wider audience. Findings are blocking or advisory; a blocking finding stops the design being
shared until fixed.

## Failure modes

- Inputs are described as "everything on the project", so Cowork mixes current and superseded material.
- The definition of done lives in the delegator's head, so outputs cannot be judged consistently.
- A real document with personal data is used as an example and leaks into outputs for another audience.
- Standing rules are copied into dozens of task designs and drift apart when the standard changes.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Run a shared task design that has no definition of done.
- Use real personal or confidential content as an example for an audience that should not see it.
- Leave Cowork to resolve conflicting sources silently.
- Copy standing organisational rules into individual task designs instead of governing them once.
