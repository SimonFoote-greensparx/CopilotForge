---
name: studio-agent-design
description: Turns an agreed agent brief into a Copilot Studio solution design - orchestration approach, topics, knowledge, tools and flows, authentication, channels, environment and solution packaging, and the run model - recording each design decision with the alternatives rejected. Use when a brief has chosen Copilot Studio, when a maker is about to build without a design, or when a growing agent needs its architecture reset.
license: CC-BY-4.0
metadata:
  department: copilot-studio
  lifecycle: Envision, Deliver
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: copilot-studio, power-platform, m365-agents
  edition-support: starter, scale, enterprise
  reviewers: design-authority, security-privacy
  sources: ms-copilot-studio-guidance, ms-agents-extensibility, ms-agents-compare, ms-copilot-studio-security-governance, ms-copilot-studio-zoned-governance
  status: draft
  authors: Simon Foote
---

# Studio agent design

## Purpose

An agent brief says what an agent is for; it does not say how a Copilot Studio agent should be put together. This skill
turns the brief into a solution design that makes each structural choice explicitly - how the agent decides what to do,
what it knows, what it can do, whose identity it uses, where it lives and how it reaches people - and records why. Studio
agents usually go wrong when a maker starts in the canvas, adds knowledge and tools as ideas occur, and discovers at
release that the agent runs under the maker's credentials in a personal environment with no way to promote it.

## When to use

- A brief from `m365-agents:agent-use-case-design` has chosen Copilot Studio as the build route.
- A maker is about to start building an agent that will take actions, serve a wide audience or sit at risk tier 2 or above.
- An existing Studio agent has grown by accretion and needs its structure reset before more is added.
- A design authority or partner asks for the design of an agent before agreeing to support it.

## When not to use

- Deciding whether AI or an agent is warranted at all - use `opportunity-management:ai-suitability`.
- Writing the brief, audience, scope and success measures - use `m365-agents:agent-use-case-design`.
- Choosing between Copilot Studio, Agent Builder, Foundry or pro-code for a solution - use `ai-architecture:platform-selection`.
- Detailed design of one layer - use `copilot-studio:topics-and-orchestration`, `copilot-studio:studio-knowledge-architecture`, `copilot-studio:studio-actions-and-tools` or `copilot-studio:multi-agent-design`.
- The formal design review of the finished design - use `design-authority:ai-design-review`.

## Questions to ask first

1. Is there an agreed brief with an owner, audience, scope, exclusions and a risk tier? If not, stop and send it back.
2. Does the agent only answer, or does it also act in other systems, and if it acts, whose identity should the action carry?
3. Which parts of the conversation must follow a fixed, auditable path, and which can be left to generative orchestration?
4. Where will users meet the agent - Teams and Microsoft 365 Copilot, a website, a custom app - and are they signed in there?
5. Which environment and governance zone will it be built and run in, and who will support it once the maker moves on?

## Required inputs

- The agreed agent brief, including representative questions and exclusions, and the risk tier from `opportunity-management:risk-classification`.
- Knowledge readiness verdicts from `m365-agents:knowledge-source-readiness`.
- The organisation's environment strategy and data policies (from `platform-governance:ai-environment-strategy` and `platform-governance:connector-policy`).
- The systems the agent must read or change, and their owners.

Where an input is missing, mark it "to confirm" in the design and do not design around a guess. A missing environment
strategy is not a reason to build in the default environment; record it as a precondition.

## Decision framework

Design each dimension against a default and move away from the default only for a recorded reason.

| Dimension | Default | Move away when | Detailed by |
|---|---|---|---|
| Orchestration | Generative orchestration with a small number of authored topics | Regulated wording, mandatory sequence or validated data capture is required | `copilot-studio:topics-and-orchestration` |
| Knowledge | The smallest set of ready, owned sources the questions need | Questions span many owners or need structured records | `copilot-studio:studio-knowledge-architecture` |
| Tools | Read-only tools first; write tools with confirmation | The outcome cannot be reached without changing records | `copilot-studio:studio-actions-and-tools` |
| Identity | The end user's identity for knowledge and tools | A service identity is justified, scoped and approved | `copilot-studio:studio-authentication` |
| Structure | One agent | Distinct domains, owners or release cycles make one agent unmanageable | `copilot-studio:multi-agent-design` |
| Packaging | In a named solution in a non-default development environment from day one | Never | `copilot-studio:studio-alm` |
| Channel | Where the audience already works | The audience is external or unauthenticated | `copilot-studio:studio-deployment` |

If the design needs more than three move-aways at tier 2 or above, check with `ai-architecture:platform-selection`
whether Copilot Studio is still the right route.

## Practitioner approach

Start from the brief's representative questions, not from the Studio canvas. Sort them into three piles: questions
answered from knowledge, requests that need an action in another system, and interactions that must follow a fixed path
(a regulated disclosure, an eligibility check, a structured request form). The piles shape the design. An agent that is
almost all knowledge is a light design; an agent with several write actions is an integration project with a
conversational front end, and should be resourced as one.

Next, decide orchestration. Generative orchestration lets the agent choose knowledge, tools, topics and child agents
from their names and descriptions, which reduces authoring but moves the design effort into writing precise
descriptions and instructions. Keep authored topics for the paths the third pile identified. Write down which requests
are generative and which are authored; this list is what testers will later use.

For every action, name the system, the operation, whether it reads or writes, the identity it runs under and what the
user confirms. Prefer the end user's identity so the agent can do nothing the user could not do themselves. Where a
service identity is proposed, record why, what it can reach and who approved it, because this is the decision the
security reviewer will examine first.

Place the agent before building it. Agree the development, test and production environments, the solution and
publisher it will live in, and the connection references and environment variables it will need. Retrofitting a
solution onto an agent built in a personal environment is slow and error-prone, and it is the most common reason
promising pilots never reach production.

Decide the channels and check that authentication works in each. An agent designed for Teams and Microsoft 365 Copilot
behaves differently on a public website, where users may be anonymous and every tool must be safe for anyone.

Finally, write the run model: who owns the agent, who maintains knowledge, who watches analytics, who supports users
and what triggers a review. Record the design on the `studio-solution-design` template with the alternatives considered
for each dimension. Product capability changes often, so cite the source record behind any feature the design depends
on rather than relying on memory.

## Outputs

- A solution design on the `studio-solution-design` template covering every dimension in the decision framework, with decisions, alternatives rejected and open questions.
- A question-to-mechanism map: each representative question mapped to knowledge, a tool, an authored topic or a child agent.
- An action register naming system, operation, read or write, identity and confirmation for each tool.
- Preconditions and owners, carried into the `alm-and-environment-plan` and the `agent-release-checklist`.

## Microsoft platform considerations

Copilot Studio agents live in Power Platform environments and are governed by environment settings, data policies and
Managed Environment controls. Orchestration modes, knowledge types, tool types, channels and authentication options
evolve quickly and some features are in preview; check `ms-copilot-studio-guidance` and
`ms-copilot-studio-security-governance` for the current position before a design depends on them. Where the brief
could be met by a declarative agent, `ms-agents-compare` and `ms-agents-extensibility` help confirm the choice.

## Adoption considerations

Design for the channel users already open every day; an agent that needs a new destination needs an adoption plan.
Agree with the business owner how users will learn what the agent can and cannot do, and hand that to
`copilot-adoption:launch-plan`.

## Knowledge considerations

The design names every knowledge source with its owner and readiness verdict. A source that is not ready is a
precondition, not a design decision; do not compensate for poor content with more instructions.

## Security and privacy considerations

Record every identity the agent uses, every system it can reach and every place its outputs go, including transcripts.
Designs that use maker or service credentials, anonymous channels or write actions bring the `security-privacy` gate
forward. Personal data in knowledge or tools needs `security-privacy:privacy-assessment`.

## Responsible AI considerations

If the agent informs decisions about people, money, safety or rights, the design must show where a person reviews the
outcome and how users are told they are dealing with an AI agent. Escalate such designs through
`opportunity-management:risk-classification` to the `responsible-ai` reviewers.

## Evaluation requirements

The question-to-mechanism map becomes the skeleton of the test plan. Each mechanism needs at least one test, and the
release threshold is agreed with the business owner before build ends, through `copilot-studio:studio-testing-and-evaluation`.

## Value measures

Carry the brief's success measures into the design and name where each will be read, for example Studio analytics
outcomes or a business system report. The business owner owns them; measures are reported by agent and audience, never
by individual user.

## Scale notes

### Starter

A two-page design on the template, agreed between the maker and the business owner, is enough for a tier 1 knowledge
agent. Still build in a solution in a non-default environment.

### Scale

Use the template for every Studio agent at tier 2 and above, reuse approved patterns for common designs, and have the
Copilot Studio Architect review designs with write actions or service identities before build.

### Enterprise

Maintain reference designs per pattern, require `design-authority` review from tier 2, and link each design to the
solution inventory so dependencies between agents, flows and connectors are visible across the estate.

## Hand-offs

- To `copilot-studio:topics-and-orchestration`, `copilot-studio:studio-knowledge-architecture` and `copilot-studio:studio-actions-and-tools` for detailed design.
- To `copilot-studio:studio-alm` and `copilot-studio:studio-environments` to place the agent.
- To `copilot-studio:studio-testing-and-evaluation` with the question-to-mechanism map.
- To `design-authority:ai-design-review` from tier 2.

## Reviewer gates

From risk tier 2, `design-authority` reviews the design for platform fit, conformance and supportability, and
`security-privacy` reviews identities, connectors and data flows. Designs with write actions or anonymous channels are
reviewed by `security-privacy` at tier 1 as well.

## Failure modes

- The agent is built first and the design written afterwards to describe what exists, so no alternatives were considered.
- Every request is left to generative orchestration, including a regulated disclosure that must be worded exactly.
- Tools are configured with the maker's own connection, and the agent acts with the maker's rights for everyone.
- The agent is built in a personal or default environment and cannot be promoted without a rebuild.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Start building a tier 2 or higher agent without a recorded design and an agreed brief.
- Let an agent act under the maker's personal credentials for other users.
- Build a production-bound agent outside a solution or in the default environment.
- Depend on a feature's availability, limits or licensing without checking the current source record.
