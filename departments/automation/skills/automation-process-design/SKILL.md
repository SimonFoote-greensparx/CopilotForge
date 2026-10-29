---
name: automation-process-design
description: Redesigns a business process before it is automated - removing waste, standardising inputs, writing down decision rules, defining exceptions and owners - and produces a future-state design that marks each step as human, flow, AI or desktop flow. Use when an assessment says a process is not ready to automate, when teams run the same process differently, or before build starts on any automation with AI steps.
license: CC-BY-4.0
metadata:
  department: automation
  lifecycle: Envision, Deliver
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: power-platform, copilot-studio, ai-foundry, platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: design-authority, responsible-ai
  sources: ms-copilot-studio-guidance, ms-responsible-ai, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Automation process design

## Purpose

Automating a process as it stands preserves every workaround, duplicate check and unclear rule, and makes them harder to
change. This skill redesigns the process first: it removes steps that add nothing, standardises inputs so fewer steps
need AI, writes down the decision rules, and names who owns the exceptions. The result is a future-state design that a
maker can build and a process owner can sign. Work here goes wrong when the design is drawn by the builder alone,
when exceptions are left for later, and when AI is used to cope with messy inputs that a form change would remove.

## When to use

- `automation:automation-assessment` judged the process not ready, or approved it for build.
- Different teams or sites run the same process in different ways and the automation must serve all of them.
- An automation will include AI steps and their inputs, outputs and review points need defining.
- An existing automation keeps breaking because the process around it has changed.
- A process owner needs a design they can understand and sign before build starts.

## When not to use

- Deciding which steps suit automation or AI in the first place - use `automation:automation-assessment`.
- Detailed flow construction, triggers, scopes and AI step configuration - use `automation:flow-design-patterns`.
- Designing the approval and review interactions in detail - use `automation:human-in-the-loop`.
- Designing delegated multi-step work done by a person with Copilot Cowork - use `copilot-cowork:multi-step-work-design`.
- Framing the original business problem and its owner - use `opportunity-management:problem-framing`.

## Questions to ask first

1. Who owns the process end to end, and who will own the automated version and its exceptions after go-live?
2. Which steps exist only to check, copy or chase something, and what would happen if they were removed?
3. Could the inputs be made structured at source (a form, a template, a supplier file) so that fewer steps need AI?
4. What are the decision rules at each branch, and can the process owner state them without saying "it depends"?
5. Which cases do not fit the standard path today, how often do they occur, and who handles them?

## Required inputs

- The automation assessment record, with the step list and step classification.
- The process owner and representatives of the people who do the work, available for at least one design session.
- Any policy, regulation or contract that constrains the process, named by the process owner.
- The current exception list, even if informal (emails, notes, a spreadsheet of "odd cases").
- The risk tier from `opportunity-management:risk-classification`.

If a decision rule cannot be stated, record it as "to confirm" against a named person and do not let the build guess it.
If no one will own exceptions, stop: the design cannot be approved.

## Decision framework

Apply these tests to every current step, in order. The first that applies decides what happens to the step.

| Test | If yes | Outcome |
|---|---|---|
| Does the step add nothing the customer, the business or a control needs? | Remove it | Record what was removed and who agreed |
| Is it a duplicate check or a copy between systems? | Consolidate | One check, one system of record |
| Is the input unstructured only because nobody asked for it structured? | Fix at source | Form, template or structured file replaces an AI step |
| Is it a fixed rule on structured data? | Flow step | Rule written down and owned |
| Is it unstructured input or language output? | AI step | Defined task, output shape, threshold and fallback |
| Does it carry judgement with material consequences? | Human step or approval | Named role, information shown, time limit |

Each future-state step records its type (human, flow, AI, desktop flow), input, output, owner, exception route and the
measure that shows it works. A design is ready for build when every branch has a written rule, every AI step has a
fallback, and every exception has an owner.

## Practitioner approach

Run the design with the process owner and people who do the work in the room, not with the maker alone. Start from the
assessment step list and walk it with real cases, including at least one that went wrong. Ask "why does this step
exist?" of each one. You will find steps that exist because a system once failed, checks nobody reads and reports
nobody uses. Remove them with the owner's agreement and record what was removed, so the decision survives audit.

Push hardest on inputs. Most AI steps in automation exist to cope with inputs that arrive in unpredictable shapes. Ask
whether a form, a mandatory field, a supplier template or a structured export could replace the free-text input. Each
input fixed at source removes an AI step, its testing, its review effort and its failure modes. Keep AI for the inputs
that are genuinely unstructured and cannot reasonably be changed.

Write the decision rules down in plain language. If the process owner says "it depends", ask on what, and keep asking
until the rule can be written. Rules that cannot be written are judgement, and judgement belongs with a person or with
an AI step whose output a person reviews. Do not let a maker infer rules from past cases without the owner's sign-off.

Design exceptions as part of the process, not an afterthought. List the known exception types, their frequency and who
resolves them. Give each a route: a queue, a named role, a time limit and what happens when the limit passes. An
automation without designed exceptions creates an unowned inbox within weeks.

Define each AI step precisely: the task, the input, the output shape (fields and allowed values), the threshold below
which the result is not trusted, the fallback and where a person reviews. Mark every point where a result takes effect
outside the team, such as a message to a customer or a payment, and design a review or approval before it.

Complete the `automation-design` template with the future-state steps, AI step definitions, review points, exceptions,
connectors, monitoring needs and value baseline. Walk the process owner through it and get a signature. Revisit the
design when the process, policy or systems change, not only when the flow breaks.

## Outputs

- A future-state automation design on the `automation-design` template: owner, removed steps, future-state step table (type, input, output, owner, exception route), AI step definitions, review and approval points, exception catalogue, systems and connectors, monitoring needs, value baseline and sign-off.
- A short record of steps removed or consolidated and who agreed.
- A list of input changes requested at source (forms, templates, supplier files) with owners.

## Microsoft platform considerations

Keep the design platform-neutral until steps are classified, then note the intended route for each: a cloud flow, a
desktop flow, an AI model in Power Platform or a model deployed through Microsoft Foundry, an approval, or an agent action.
Where an agent is part of the solution, Power Automate flows often do the acting while the agent interprets. Check
current capabilities and limits in `references/sources.md` before committing the design to a feature.

## Adoption considerations

The people who run the process today will run the exceptions tomorrow. Their involvement in design is the best predictor
that they will trust and support the automation. Explain what changes for them, what they will review and how they
raise problems. Route significant role changes to the `change-and-communications` department.

## Knowledge considerations

Written decision rules, category definitions and exception guides are knowledge assets in their own right. Store them
where the process owner maintains them, and point AI steps at that maintained version rather than a copy embedded in a
prompt.

## Security and privacy considerations

Record the data each step handles and where it goes. Removing steps often removes copies of personal data, which is a
privacy gain worth recording. Steps that move personal data to new systems or outside the tenant go to
`security-privacy:privacy-assessment`.

## Responsible AI considerations

Where an AI step informs a decision about a person, the design must show who reviews the result before effect, what they
see and how an affected person can challenge the outcome. From tier 3, the design goes to `responsible-ai` for review of
oversight and escalation.

## Evaluation requirements

Each AI step names its acceptance threshold, agreed by the process owner before testing, and the sample of real inputs it
will be tested against. The end-to-end design is tested with real cases, including known exceptions, before go-live.

## Value measures

Record baselines for the redesigned process separately from the automation: some value comes from removed steps and
fixed inputs alone. The process owner owns the baselines; `automation:automation-value` measures the outcome.

## Scale notes

### Starter

One design session with the owner and a practitioner, a one-page future state and a short exception list. Prefer fixing
inputs at source over adding AI steps.

### Scale

Use the `automation-design` template for every automation with AI steps or tier 2 risk, and keep a library of designed
exception patterns and AI step definitions for reuse.

### Enterprise

Harmonise processes across business units before automating them once, rather than automating each variant. Design
shared components (classification, extraction, approval) centrally and let business units configure them.

## Hand-offs

- To `automation:flow-design-patterns` to build the design.
- To `automation:human-in-the-loop` for detailed review and approval design.
- To `automation:exception-handling` for retry, fallback and exception queue design.
- To `automation:automation-value` with the baseline.

## Reviewer gates

From risk tier 2, `design-authority` reviews the design for unnecessary AI steps and unsupported patterns. From tier 3,
`responsible-ai` reviews human oversight where AI steps inform decisions about people. Findings are recorded on the design.

## Failure modes

- The maker designs alone, the owner signs without reading, and undocumented rules surface as production defects.
- Messy inputs are accepted as given, so AI steps are added to clean up problems a form would remove.
- Exceptions are left "for phase two" and pile up in an inbox nobody owns.
- The process changes after go-live and nobody updates the design or the automation.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Approve a design with a branch whose rule nobody can state.
- Add an AI step where fixing the input at source would remove the need.
- Leave exceptions without a named owner, route and time limit.
- Let a maker infer business rules from past cases without the process owner's sign-off.
