---
name: strategic-outcomes
description: Turns an AI ambition into three to five measurable business outcomes, a short set of AI principles and an explicit statement of where AI will not be used, with clear expectations of the executive sponsor. Use when leaders say they want an AI strategy, when a programme has activity but no agreed outcomes, or when a sponsor needs to explain why the organisation is investing in AI.
license: CC-BY-4.0
metadata:
  department: ai-strategy
  lifecycle: Envision, Mobilise
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-responsible-ai, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Strategic outcomes

## Purpose

This skill converts a broad ambition ("we want to be AI-first") into a small number of business outcomes the
organisation can measure, the principles that govern how AI is used, and a clear statement of where it will not be
used. Those three things let every later decision, from scenario choice to agent approval, be tested against something
leaders actually agreed. Strategies usually fail here by listing products to deploy instead of results to achieve, by
setting so many outcomes that none gets resourced, or by treating principles as a poster rather than a decision rule.

## When to use

- The executive team asks for an AI strategy or vision and needs it to be more than a technology plan.
- A programme is busy (licences assigned, pilots running, agents appearing) but nobody can say what success looks like.
- A sponsor must justify AI investment to a board, trustees or a regulator.
- The maturity assessment is complete and the organisation is ready to set direction.

## When not to use

- Establishing the current baseline - use `ai-strategy:ai-maturity-assessment` first.
- Sequencing initiatives and capability work over time - use `ai-strategy:ai-roadmap`.
- Deciding whether a single idea should use AI - use `opportunity-management:ai-suitability`.
- Writing the acceptable-use policy and governance model - use `ai-centre-of-excellence:coe-governance-model`.
- Building the detailed benefits model and measurement plan for one initiative - use `value-realisation:benefit-realisation-plan`.

## Questions to ask first

1. Which business results matter most to the organisation over the next two to three years, regardless of AI?
2. Where does work currently cost too much, take too long, lose quality or frustrate customers or staff, and how is that measured today?
3. What would leaders refuse to let AI do, even if it worked, and why?
4. Who is the executive sponsor, and how much of their time and authority will they commit?
5. What does the maturity assessment say about the binding constraints, such as knowledge, governance or adoption?

## Required inputs

- The organisation's current business strategy or plan, and its existing performance measures.
- The maturity assessment from `ai-strategy:ai-maturity-assessment`, or a note that none exists.
- Access to the executive team for at least one working session, and to the named sponsor.
- Any existing AI principles, policies or regulatory commitments.

Where a baseline for an outcome measure does not exist, record the outcome with "baseline to confirm" and an owner and
date for establishing it. Never invent a figure to make the outcome look complete.

## Decision framework

Test every candidate outcome against these criteria. Keep three to five that pass; park the rest.

| Test | Passes when | Fails when |
|---|---|---|
| Business result | It describes a change in cost, time, quality, risk, revenue, experience or capability | It describes a technology deployed or a number of licences used |
| Measurable | A measure, a baseline (or a plan to get one) and a direction of travel are named | Success is a feeling or an activity count |
| Owned | A business executive, not the AI team, accepts accountability | Ownership sits only with IT or the CoE |
| AI makes a material difference | AI is a credible contributor alongside process and people change | The outcome would be met just as well without AI |
| Within reach | The maturity baseline makes it plausible within the horizon | It assumes capability two archetype stages ahead |

Principles pass when each one would change a real decision. The "not appropriate" list passes when it names concrete
uses, not abstractions.

## Practitioner approach

Start from the business strategy, not from AI. Ask the executive team which results they are already accountable
for and where those results are under pressure. Collect the pain in their words with whatever measures exist. Only
then ask where AI could plausibly contribute, and expect the honest answer to be "partly" for most outcomes: process,
data and people changes usually carry as much of the result as the technology.

Draft more candidates than you need, then apply the tests. Most first drafts fail on ownership or measurability.
"Improve productivity with Copilot" becomes "Reduce the time case handlers spend on case summaries, measured by
average handling time, owned by the operations director". Push each outcome to a single accountable executive. If no
executive will own it, it is not yet a strategic outcome.

Write principles as decision rules, not values statements. "Humans remain accountable for decisions about people" is
useful only if it is followed by what it means: no AI-generated output is used in recruitment or disciplinary decisions
without documented human review. Aim for five to eight principles covering accountability, transparency to staff and
customers, data handling, fairness, knowledge ownership and when AI is the wrong answer. Use the responsible AI source
records to check coverage, and summarise in your own words rather than adopting a published set wholesale.

Then write the "where AI is not appropriate" statement. Name uses the organisation will not pursue in this horizon, for
example fully automated decisions about individuals, or customer-facing advice in a regulated area before assurance
capability exists. Distinguish "never" from "not yet, until a stated precondition is met". This list protects the
programme from enthusiasm as much as from risk, and it is the strongest signal to staff that leadership has thought
about consequences.

Agree the sponsor's role explicitly: chairing the quarterly review, removing blockers across functions, accepting risk
where the governance model requires it, and visibly using AI themselves within the principles. Record the time
commitment. A sponsor who only signs the strategy is a figurehead, and programmes with figurehead sponsors stall at
the first cross-functional conflict.

Play the outcomes, principles and exclusions back on one page. If the executive team cannot recall them a month later,
there are too many or they are too abstract. Hand the result to `ai-strategy:ai-roadmap` for sequencing.

## Outputs

- The strategic outcomes section of the `ai-roadmap` template: three to five outcomes, each with measure, baseline or baseline plan, target direction, horizon and accountable executive.
- A set of AI principles written as decision rules.
- A "where AI is not appropriate" statement, separating "never" from "not yet" with preconditions.
- A sponsor commitment statement covering role, decisions reserved to the sponsor and time committed.

## Microsoft platform considerations

Not applicable at this stage, because outcomes and principles must hold whatever the platform choice. Product names and
capabilities change often; keep them out of the outcomes and let `ai-strategy:ai-roadmap` and the delivery skills
choose platforms against the current source records.

## Adoption considerations

Staff hear the strategy through its principles and exclusions far more than through its outcomes. Publish both in
plain language, with the reasoning, so people understand what AI is for in this organisation and what it will not be
used for. Route the communication through the adoption programme rather than a single announcement.

## Knowledge considerations

Where an outcome depends on AI grounded in organisational knowledge, name the knowledge domain and its owner as a
precondition. An outcome that relies on unowned knowledge is recorded with that dependency so the roadmap can address
it first.

## Security and privacy considerations

The principles should state how personal and confidential data may be used with AI, and who decides exceptions. Check
the wording with the data protection officer and the security lead; legal interpretation belongs with them, not with
this skill.

## Responsible AI considerations

The principles and the exclusions are the organisation's first responsible AI commitments. Test them against the
responsible AI and risk management source records for coverage of accountability, fairness, transparency, privacy,
reliability and human oversight. Where a principle would bind high-impact uses, connect it to the risk tiers so it is
enforced through `opportunity-management:risk-classification`.

## Evaluation requirements

Not applicable to solution testing. The outputs are checked by asking the executive team to apply the outcomes and
principles to two or three real pending decisions; if they do not change or clarify any decision, rewrite them.

## Value measures

Each outcome carries its own measure, baseline and accountable executive. The strategy's overall success is the
movement of those measures at the agreed review points, reported at organisation, unit or team level, never by
individual.

## Scale notes

### Starter

One working session with the leadership team and a one-page result: two or three outcomes, a handful of principles
and a short exclusions list. The sponsor is usually the chief executive or a director.

### Scale

Run separate sessions with each major function, then consolidate into three to five organisation outcomes. Publish the
principles with worked examples, and review outcomes quarterly at steering.

### Enterprise

Set enterprise outcomes and principles centrally, then let business units derive their own outcomes beneath them, with
the hub checking alignment. Principles become part of the federated governance model and are reviewed annually by the
executive board.

## Hand-offs

- To `ai-strategy:ai-roadmap` to sequence the initiatives and capability work that deliver the outcomes.
- To `ai-strategy:ai-operating-model` to decide who owns, builds and supports AI against these outcomes.
- To `ai-centre-of-excellence:coe-governance-model` to turn the principles into policy and controls.
- To `opportunity-management:problem-framing` so new ideas are framed against the agreed outcomes.

## Reviewer gates

Not applicable. Outcomes and principles are executive decisions, not releases.
`responsible-ai:prohibited-use-review` may be asked for advice on the principles, particularly where AI is not
appropriate.

## Failure modes

- Outcomes describe products deployed ("roll out Copilot to all staff") rather than results achieved.
- Ten outcomes are agreed, none is resourced, and the programme reverts to activity reporting.
- Principles are generic values that never change a decision, so staff ignore them.
- No exclusions are stated, and the first contentious use case becomes a public argument.
- The sponsor signs the strategy and disengages, leaving the AI team to resolve cross-functional conflicts it has no authority over.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Write an outcome that names a product instead of a business result.
- Invent baselines, targets or benefit figures to make an outcome look complete.
- Assign ownership of a business outcome to the AI or IT team alone.
- Omit the statement of where AI is not appropriate.
