---
name: foundry-agent-architecture
description: Architects a single agent, or a small set of cooperating agents, on Foundry Agent Service - its responsibilities, instructions, model, tools, knowledge, state, identity and the surfaces it is published to - so it can be built, secured and operated. Use when a Foundry agent has been approved, when an agent prototype needs a production design, or when a Copilot Studio agent is being rebuilt in Foundry.
license: CC-BY-4.0
metadata:
  department: ai-foundry
  lifecycle: Mobilise, Deliver
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure, entra, m365-agents
  edition-support: starter, scale, enterprise
  reviewers: design-authority, security-privacy, responsible-ai
  sources: ms-foundry-models, ms-agents-extensibility, ms-agents-compare, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# Foundry agent architecture

## Purpose

An agent on Foundry Agent Service combines a model, instructions, tools, knowledge and conversation state behind an
identity, and every one of those is a design decision with security, cost and quality consequences. This skill produces
the agent's architecture: what it is responsible for, what it may do, how it holds state, which identity it acts with
and where it is surfaced. Agent designs go wrong when one agent is given every tool "in case", when its identity has
far more access than its users, and when the prototype's shortcuts become production by default.

## When to use

- A Foundry agent has been approved by `ai-foundry:foundry-solution-assessment` and needs a design before build.
- A prototype agent works in a notebook or playground and needs a production architecture.
- An agent built in Copilot Studio or Agent Builder is being rebuilt, wholly or partly, on Foundry.
- An agent is being split into several cooperating agents, or several agents are being consolidated.

## When not to use

- Designing a multi-step workflow where the autonomy, checkpoints and stop conditions are the main question - use `ai-foundry:agentic-workflow-design`.
- Designing the contract of an individual tool or function - use `ai-foundry:foundry-tool-design`.
- Connecting external MCP servers to the agent - use `ai-foundry:mcp-integration`.
- Designing an agent in Copilot Studio - use `copilot-studio:studio-agent-design`.
- Designing a declarative Microsoft 365 agent - use `m365-agents:agent-use-case-design`.

## Questions to ask first

1. What is the agent responsible for, in one sentence, and what must it refuse or hand over?
2. Who are its users, and does it act with their identity, its own identity or both?
3. Which actions can it take that change something outside the conversation, and which need a person to approve them?
4. What must it remember within a conversation and across conversations, and for how long may that be kept?
5. Where will people reach it: inside an application, through an API, in Microsoft 365 or Teams, or as a step in another agent?

## Required inputs

- The approved solution design on the `foundry-solution-design` template, with risk tier.
- The model selection record from `ai-foundry:model-selection`, or at least a shortlist.
- A list of candidate actions and knowledge sources with their owners.
- The organisation's Azure identity and network standards.

Where actions, owners or identity standards are missing, mark them `[To confirm: ...]` in the architecture and do not
design around assumptions. An action with no owner is removed from scope until it has one.

## Decision framework

| Decision | Default | Move away from the default when |
|---|---|---|
| Number of agents | One agent with a narrow responsibility | Responsibilities need different permissions, models or owners, or one set of instructions becomes contradictory |
| Identity for actions | The user's delegated identity, so permissions are trimmed | The action has no user context (batch, scheduled) or must use a service capability the user lacks; then a managed identity with least privilege |
| Tools | Only those the responsibility needs, each with an owner | Never add tools speculatively |
| State | Conversation state held by the service for the session only | Cross-session memory is a stated requirement with a retention rule agreed with the DPO |
| Write actions | Proposed by the agent, confirmed by a person | Tier 0 or 1, reversible, low impact, and confirmed by `responsible-ai:human-oversight` for higher tiers |
| Surfaces | One surface at launch | Each further surface is a change with its own identity and audience review |

## Practitioner approach

Write the responsibility statement first and keep it narrow: who the agent serves, what outcome it helps with, and the
boundary where it refuses or hands over. Every later decision is tested against this statement. If the team cannot
agree it, the agent is really several agents or no agent.

Decide the shape. A single agent is simpler to evaluate, secure and support, so it is the default. Split into several
agents only when parts genuinely need different permissions, models, owners or instructions that would conflict. When
agents cooperate, name the coordinating agent, what each specialist may do, and how results and failures pass between
them. If the cooperation is really a defined sequence with checkpoints, hand the flow to
`ai-foundry:agentic-workflow-design` and keep this design to the agents themselves.

Design identity before tools. For each action, decide whether it runs as the signed-in user, so the user's permissions
apply, or as a managed identity for the agent. User-delegated access is the safer default because it prevents the agent
becoming a route around permissions. Where a managed identity is unavoidable, scope it to the minimum resources and
operations, and record why. Bring `ai-architecture:ai-identity-design` in for anything non-trivial.

List the tools and knowledge the responsibility needs, and only those. For each tool record its owner, whether it
reads or writes, and whether a person confirms before it runs. Detailed contracts go to `ai-foundry:foundry-tool-design`;
external MCP servers to `ai-foundry:mcp-integration`; grounding choices to `ai-foundry:foundry-grounding-strategy`.

Decide state and memory deliberately. Conversation threads and any cross-session memory are personal data in many
cases; set what is stored, where and for how long, and agree retention with the data owner and DPO.

Choose one launch surface. Each surface brings its own authentication, audience and transcript handling, so adding
surfaces later is a change, not a configuration tweak. Finally, record the architecture in the agent section of the
`foundry-solution-design` template with a simple diagram, and list what remains unknown until evaluation, such as
whether the chosen model calls tools reliably enough.

## Outputs

- The agent architecture section of the `foundry-solution-design` template: responsibility, agent shape, identity per action, tool and knowledge list with owners, state and retention, surfaces and diagram.
- A tool inventory handed to `ai-foundry:foundry-tool-design`.
- Open questions to resolve through evaluation.

## Microsoft platform considerations

Foundry Agent Service manages agents, threads, tool calls and runs on the organisation's Azure resources, and its
capabilities, tool types and connected surfaces are changing quickly. Check the current source records for which tools,
knowledge connections and publishing channels are available before designing around them, and whether a capability is
in preview. Where the agent is surfaced in Microsoft 365, the extensibility guidance governs how it appears and which
identity flows apply.

## Adoption considerations

Agents surfaced to people need a clear statement of what they do and do not do, visible in the surface itself. Plan
launch communications with the business owner, and keep the first audience small enough to learn from.

## Knowledge considerations

Each knowledge source needs an owner, a refresh route and an audience consistent with the agent's users. Grounding
approach and retrieval design are separate decisions handled by `ai-foundry:foundry-grounding-strategy`.

## Security and privacy considerations

The agent's identity, tool permissions, network exposure and stored threads are the main attack and leakage surfaces.
Design for least privilege, user-delegated access where possible and prompt-injection resistance in tools that read
untrusted content. `security-privacy:ai-identity-and-access-review` reviews the result from tier 2.

## Responsible AI considerations

Any action that affects people, money, safety or rights needs a defined human checkpoint, designed with
`responsible-ai:human-oversight`. Users must be able to tell they are dealing with AI and how to reach a person.

## Evaluation requirements

Plan evaluation for task quality, tool-call correctness, refusal of out-of-scope requests and behaviour under
prompt-injection attempts, with thresholds agreed before testing. Agent-level evaluation design goes to
`ai-foundry:model-evaluation` and safety testing to `ai-foundry:foundry-safety-evaluation`.

## Value measures

Carry the solution's value measure into the agent design: the task outcome it should improve, its baseline and the
business owner. Report usage and outcomes for the agent at audience level, never by individual user.

## Scale notes

### Starter

Build one narrow agent with read-only tools first, user-delegated access and one surface. Add write actions only after
it has run well.

### Scale

Reuse agreed patterns for identity, state retention and tool registration across agents, so each new agent starts from
a reviewed baseline.

### Enterprise

Maintain an agent catalogue with owners, identities and tool permissions, and require architecture review for any agent
that coordinates others or acts across business areas.

## Hand-offs

- To `ai-foundry:foundry-tool-design` for each tool's contract.
- To `ai-foundry:foundry-grounding-strategy` for knowledge.
- To `ai-foundry:foundry-prompt-engineering` for instructions.
- To `ai-foundry:foundry-deployment-architecture` for environments and topology.
- To `ai-foundry:foundry-observability` so tracing is designed in from the start.

## Reviewer gates

From risk tier 2, `security-privacy` reviews identity, tool permissions and state retention, `responsible-ai` reviews
human checkpoints on consequential actions, and `design-authority` checks conformance to the reference architecture.

## Failure modes

- The agent is given every available tool, and a prompt-injection in a document triggers an action nobody intended.
- A managed identity with broad access serves all users, so the agent returns content users could not open themselves.
- Conversation threads are kept indefinitely because nobody set retention, and become an unplanned store of personal data.
- The prototype's single shared key and open endpoint go into production unchanged.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Give an agent a tool without a named owner and a stated reason linked to its responsibility.
- Let an agent identity hold broader access than the users it serves without a recorded justification.
- Allow consequential write actions without a designed human checkpoint.
- Design around a preview capability without recording it as a risk and checking the current source.
