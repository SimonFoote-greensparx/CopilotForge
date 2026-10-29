---
name: agent-lifecycle
description: Manages an individual Microsoft 365 agent after release through defined states - live, under change, under review, deprecated and retired - with change control, scheduled and triggered reviews, responses to platform changes, and a retirement path that tells users and disposes of the agent cleanly. Use when a live agent needs changing, when its review date arrives, when its owner or knowledge lapses, or when it should be retired.
license: CC-BY-4.0
metadata:
  department: m365-agents
  lifecycle: Launch, Improve, Scale
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, power-platform
  edition-support: starter, scale, enterprise
  reviewers: design-authority, evaluation-quality
  sources: ms-copilot-studio-guidance, ms-agent-builder, ms-coe-starter-kit, ms-managed-environments
  status: draft
  authors: Simon Foote
---

# Agent lifecycle

## Purpose

Releasing an agent is the start of its life, not the end of the project. This skill manages an individual agent from
release to retirement: it defines the states an agent moves through, controls changes, runs scheduled and triggered
reviews, responds to Microsoft platform changes, and retires agents cleanly when they are no longer needed. Agent estates
usually go wrong slowly: changes are made live without testing, reviews never happen, and agents that nobody uses keep
answering from knowledge that nobody maintains.

## When to use

- A live agent needs a change to its instructions, knowledge, actions or audience.
- An agent's scheduled review date has arrived.
- A trigger fires: the owner leaves, a source is retired, feedback shows repeated wrong answers, or usage collapses.
- Microsoft changes a capability the agent depends on.
- An agent should be retired, or someone asks whether it can be.

## When not to use

- The release gate before first sharing or widening the audience - use `m365-agents:agent-release-readiness`.
- Application lifecycle management, environments and pipelines for Copilot Studio solutions - use `copilot-studio:studio-alm` and `copilot-studio:studio-agent-lifecycle`.
- Running scheduled reviews across all live AI solutions in operations - use `ai-operations:ai-review-calendar`.
- The operational mechanics of retiring any AI solution, including data disposal - use `ai-operations:ai-solution-retirement`.
- Deciding to scale or stop on value evidence at portfolio level - use `opportunity-management:scale-or-stop`.

## Questions to ask first

1. What state is the agent in now, and who is its current business owner?
2. What has changed or is proposed: instructions, knowledge, actions, audience, or the platform beneath it?
3. Does the change alter the risk tier, the audience or the data the agent can reach?
4. What does the evidence say about use, value and answer quality since the last review?
5. If retired, what replaces it for users, and what happens to its configuration and interaction data?

## Required inputs

- The `agent-card` with owners, tier, sources and review date.
- The change log for instructions and knowledge, and the evaluation set.
- Usage, feedback and value evidence from `m365-agents:agent-value-measurement`.
- Relevant Microsoft change notices, checked against the source records.

Where the business owner is vacant, the agent enters "under review" automatically. Never change a live agent on the
promise that testing will follow.

## Decision framework

Agent states and what moves an agent between them.

| State | Meaning | Moves on when |
|---|---|---|
| Live | Released, owned, within review date | A change is proposed (under change), the review date arrives or a trigger fires (under review) |
| Under change | A change is being built and tested; the live version continues | Change passes tests and approval, then live; or is abandoned |
| Under review | Owner assesses continue, change or retire | Decision recorded: live, under change or deprecated |
| Deprecated | Users told of retirement date and alternative; no new audience | Retirement date reached |
| Retired | Unshared, disabled or deleted per policy; register updated | Final |

Changes are classified by impact. Minor (wording, conversation starters) needs a logged reason and regression run.
Significant (new source, new action, wider audience) needs the business owner's approval, a regression run and, if the
tier or exposure changes, re-classification and the release gate again. Retirement triggers include no meaningful use
for an agreed period, a vacant owner not filled in the agreed time, unmaintained knowledge, a better alternative, or a
failed review.

## Practitioner approach

Make the states visible. Record each agent's state on its agent card and in the register, so anyone can see which agents
are live, changing, under review or on their way out. That alone prevents most drift.

Control change by impact. Most changes after release are small: a clearer instruction, a new conversation starter, an
updated source. They still need a logged reason and a regression run through `m365-agents:agent-testing`, because small
edits can change behaviour. Significant changes, such as a new source, a new action or a wider audience, go to the
business owner for approval and back through classification if the tier or exposure changes. Widening the audience after
review is the change most often made without control.

Run reviews as decisions, not status meetings. At each review, the business owner looks at usage, value, answer quality,
feedback, knowledge currency and ownership, and decides: continue, change or retire. Record the decision and set the next
review date. Triggered reviews follow the same pattern but happen when something breaks the agent's assumptions, such as
a source being retired or the owner leaving.

Watch the platform. Microsoft changes agent capabilities, settings and limits frequently. Assign someone, usually the
technical owner or the CoE, to check change notices against the source records and assess whether each agent is
affected. Test affected agents before the change reaches users where possible.

Retire deliberately. Agree retirement criteria at release, so retirement is routine rather than contentious. When an
agent is to be retired, mark it deprecated, tell its users when and why, and point them to the alternative. On the
retirement date, stop sharing it, disable or delete it in line with the organisation's retention policy, decide with
records management what happens to its interaction data, and update the register. Hand the operational mechanics to
`ai-operations:ai-solution-retirement` where that service exists.

Learn from each retirement. Record why the agent was retired and what that teaches about future opportunity assessment,
knowledge ownership or scope.

## Outputs

- The agent's state and lifecycle history on the `agent-card` and in the solution register.
- Change records classified by impact, with approvals and regression results.
- Review decisions (continue, change, retire) with evidence and the next review date.
- Deprecation notices and a retirement record covering users, configuration and data.

## Microsoft platform considerations

How agents are versioned, unshared, disabled and deleted differs between Agent Builder, declarative agents and Copilot
Studio, and between governance zones. Inventory and governance tooling such as the CoE Starter Kit and Managed
Environments features can support reviews and retirement; see `ms-copilot-studio-guidance`, `ms-agent-builder`,
`ms-coe-starter-kit` and `ms-managed-environments`. These change often; check the current records before relying on a
specific control.

## Adoption considerations

Users need notice before an agent changes significantly or retires, and a clear alternative. Silent retirements and
unannounced behaviour changes erode trust in every agent, not just the one affected.

## Knowledge considerations

Knowledge currency is the most common reason an agent fails review. Link review dates to knowledge owners' review cycles,
and treat a retired or unmaintained source as a trigger for review.

## Security and privacy considerations

Significant changes can widen exposure; re-run `security-privacy:data-exposure-review` when sources, connectors or
audience change at tier 2 and above. At retirement, remove access, connectors and credentials, and agree the handling of
interaction data with records management and the data protection lead.

## Responsible AI considerations

From tier 3, reviews confirm that human oversight arrangements still operate as designed. A change that moves the agent
closer to decisions about people triggers re-classification and the `responsible-ai` gate.

## Evaluation requirements

Every change is followed by a regression run of the evaluation set, and each review checks current answer quality against
the threshold agreed at release. From tier 3, `evaluation-quality` checks regression evidence for significant changes.

## Value measures

Track at estate level the share of agents within review date, changes made with logged regression runs, and agents
retired against criteria rather than abandoned. The CoE lead owns estate measures; business owners own each agent's
value measures.

## Scale notes

### Starter

A state column and review date on a simple register, a change log per agent, and a review conversation with the owner
every few months.

### Scale

Lifecycle states in the solution register, change classes with approvals, a review calendar run through the CoE, and
platform change checks as a standing task.

### Enterprise

Lifecycle management federated to business-unit agent product owners under common states and change classes, with
estate reporting, automated reminders and links to operations and the portfolio.

## Hand-offs

- To `m365-agents:agent-testing` for regression after each change.
- To `m365-agents:agent-release-readiness` when a change widens audience or raises the tier.
- To `ai-operations:ai-solution-retirement` for retirement mechanics.
- To `opportunity-management:scale-or-stop` when a review raises scaling or stopping at portfolio level.

## Reviewer gates

From risk tier 2, significant changes are assessed by `design-authority` through `design-authority:ai-change-impact-review`,
and from tier 3 regression evidence by `evaluation-quality`; each finding is blocking or advisory, and blocking findings
stop the change.

## Failure modes

- Live edits are made without regression, and behaviour drifts unnoticed.
- Review dates pass with no decision, and unused agents accumulate.
- A Microsoft platform change alters behaviour, and nobody checks the agents that depend on it.
- An agent is deleted without notice, and users lose a tool they relied on without an alternative.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Change a live agent without a logged reason and a regression run.
- Widen an agent's audience without passing the release gate again.
- Let a review date pass without a recorded decision.
- Retire an agent without telling its users and handling its data under policy.
