---
name: agent-opportunity-assessment
description: Tests whether a request that already points to an agent really warrants a dedicated, owned agent rather than a shared prompt, a scenario or an existing agent, and if so which kind - knowledge, task or autonomous - and which build path tier, recorded as a short assessment for intake. Use when a team asks for an agent, when several teams want similar agents, or when a prompt pattern is spreading and might become one.
license: CC-BY-4.0
metadata:
  department: m365-agents
  lifecycle: Discover, Envision
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, ai-foundry, sharepoint
  edition-support: starter, scale, enterprise
  reviewers: design-authority
  sources: ms-agents-extensibility, ms-agents-compare, ms-declarative-agents, ms-agent-builder, ms-copilot-studio-zoned-governance
  status: draft
  authors: Simon Foote
---

# Agent opportunity assessment

## Purpose

Requests for "an agent" arrive faster than an organisation can own them. This skill takes a request that already points
to an agent and asks two questions before any brief is written: does this need justify a dedicated agent with an owner,
knowledge and a lifecycle, and if so, what kind of agent and which build path tier fits? It works inside the agent
rung chosen by suitability, or as a fast check when a team arrives with an agent in mind. It goes wrong when every
repeated question becomes a new agent, so the organisation ends up with dozens of overlapping, unowned agents that each
answer a little differently.

## When to use

- A team asks for an agent and the request has not been tested against simpler options or existing agents.
- Several teams want similar agents and someone must decide whether one shared agent would serve them.
- A prompt pattern or scenario is spreading across a team and might be better as an agent.
- A maker has started building and the CoE wants a quick check that an agent is warranted.

## When not to use

- Deciding whether AI is the right answer at all, across every pattern from process change to Foundry - use `opportunity-management:ai-suitability`.
- Writing the agent brief once an agent is warranted - use `m365-agents:agent-use-case-design`.
- Confirming the risk tier - use `opportunity-management:risk-classification`.
- Detailed platform selection for a solution with complex integration needs - use `ai-architecture:platform-selection`.
- Whether a need justifies a custom Microsoft Foundry solution - use `ai-foundry:foundry-solution-assessment`.

## Questions to ask first

1. How many people need this, how often, and are they asking the same kind of question or doing the same task?
2. Does the knowledge or capability they need already exist in an agent, a shared prompt or a published scenario?
3. Is the knowledge it would rely on owned, current and accessible to the intended audience?
4. Does it only need to answer, or must it act in systems or run without a person directing it?
5. Who would own it after release, and have they agreed?

## Required inputs

- The request, with the requesting team, the intended audience and examples of real questions or tasks.
- The solution register or agent inventory, to check for existing agents.
- The suitability decision, if one exists, from `opportunity-management:ai-suitability`.
- The organisation's approved build paths and governance zones, from the CoE or platform team.

Where the solution register does not exist, record that duplication could not be checked and ask the CoE before
proceeding. Never assume a build path is approved or licensed.

## Decision framework

First, test whether a dedicated agent is warranted. All four must hold.

| Test | Warranted when | Otherwise |
|---|---|---|
| Shared, recurring need | Many people in a defined audience repeat the same kind of question or task | Individual Copilot use or a published scenario |
| Not already served | No existing agent, shared prompt or scenario meets most of the need | Extend or reuse the existing asset |
| Owned knowledge or capability | The knowledge or actions have an owner willing to keep them current | Fix ownership first; record as deferred |
| Owner for the agent | A business owner agrees to own outcomes, review and retirement | Not ready; no agent without an owner |

Then classify the kind of agent and the build path tier.

| Kind | Typical shape | Usual build path tier to test first |
|---|---|---|
| Knowledge agent | Answers questions from owned content for a defined audience | Maker self-service, such as Agent Builder, within the governed zone |
| Task agent | Answers and takes bounded actions in other systems with user confirmation | Copilot Studio with CoE support and automation doing the acting |
| Autonomous agent | Runs on triggers or schedules with limited human direction | Copilot Studio or pro-code with design review; higher tier by default |
| Custom engine agent | Needs its own orchestration, models or retrieval | Pro-code, often through Microsoft Foundry, after `ai-foundry:foundry-solution-assessment` |

The tier is a starting point for `m365-agents:agent-use-case-design`, which confirms the route in the brief.

## Practitioner approach

Begin by collecting ten real examples of what people would ask or ask the agent to do, in their own words, and who asks
them. This takes an hour and settles most questions. If the examples are varied and personal, the need is individual
Copilot use and the answer is a scenario through `m365-copilot:copilot-role-scenarios`. If they are the same questions
from many people about the same body of knowledge, an agent starts to make sense.

Check the register before anything else. Ask the CoE whether an agent, shared prompt or published scenario already covers
the area. Extending an owned agent to a new audience is almost always cheaper than building a second one that will drift
apart. Where two teams want similar agents, convene them; one agent with a broader audience and clear exclusions often
serves both.

Test ownership honestly. An agent is a small product: it needs someone to own its answers, its knowledge and its review
cycle. If the requesting team cannot name that person, or the knowledge has no owner, record the opportunity as deferred
with the precondition, and offer a published scenario in the meantime.

Classify the kind of agent by what it must do, not by which tool the team likes. Answer-only agents grounded in owned
content are the most common and the easiest to run. Agents that act need accountable owners for each action and usually
an automation doing the deterministic steps. Agents that run without a person directing them carry more risk and usually
a higher tier. Check the current capability and limits of each build path in the source records at the time of the
assessment, because they change often, and note what you checked.

Write a short assessment: the need, the examples, the reuse check, the ownership position, the warranted verdict, the
kind of agent, the build path tier to test first and the initial risk tier to confirm. Share it with the requester in
plain language. A clear "not an agent, here is what will help instead" keeps trust; a silent rejection does not.

## Outputs

- An agent opportunity assessment, recorded on the `opportunity-canvas`: need, examples, reuse check, ownership position, verdict, kind of agent, build path tier and initial risk tier.
- Where not warranted, a referral to a scenario, a shared prompt or an existing agent.
- Where warranted, a hand-off to agent brief writing with the collected examples.

## Microsoft platform considerations

Declarative agents built in Agent Builder, agents built in Copilot Studio and custom engine agents differ in how they are
built, extended, governed and shared, and in which governance zone they belong. The comparison and extensibility options
are described in `ms-agents-compare`, `ms-agents-extensibility`, `ms-declarative-agents` and `ms-agent-builder`; zoning
in `ms-copilot-studio-zoned-governance`. All of these change often, so check them at the time of the decision.

## Adoption considerations

A request turned down without an alternative discourages future ideas. Route individual needs to scenarios and
prompting support through `m365-copilot:copilot-role-scenarios`, and tell requesters when a deferred agent becomes
possible.

## Knowledge considerations

Most agents are knowledge agents, so the condition and ownership of the knowledge decide whether the agent is warranted.
Record the candidate sources and owners; their detailed readiness is assessed later through
`m365-agents:knowledge-source-readiness`.

## Security and privacy considerations

Note the sensitivity of the knowledge and the breadth of the intended audience. An agent that would make sensitive
content easier to reach for a wide audience raises the risk tier and brings the `security-privacy` review forward.

## Responsible AI considerations

If the agent would inform decisions about people, money, safety or rights, or act without a person directing it, record
that it needs explicit human oversight and route it through risk classification to `responsible-ai`.

## Evaluation requirements

The ten collected examples become the seed of the evaluation set; record them with the assessment so
`m365-agents:agent-testing` can build on them.

## Value measures

Record the baseline the need implies (time to find answers, tickets raised, repeated questions to experts) and the
measure the owner would use, so `m365-agents:agent-value-measurement` can compare later.

## Scale notes

### Starter

A short conversation and a one-page assessment with the CoE lead or a partner. Most first agents are knowledge agents
built by makers within a governed zone.

### Scale

Run the assessment as a standard step in CoE intake, with a register check and consistent kinds and tiers, and reuse
earlier assessments as precedents.

### Enterprise

Federate first-pass assessment to business-unit agent product owners using shared criteria, with the hub reviewing task,
autonomous and custom engine agents and any duplicate across units.

## Hand-offs

- To `m365-agents:agent-use-case-design` when an agent is warranted.
- To `opportunity-management:risk-classification` to confirm the tier.
- To `m365-copilot:copilot-role-scenarios` when individual Copilot use fits better.
- To `ai-foundry:foundry-solution-assessment` for custom engine candidates.

## Reviewer gates

From risk tier 2, the kind and build path tier are open to challenge by `design-authority` for unnecessary agents,
duplication and platform fit, classified as blocking or advisory. The CoE lead records the challenge and response on the
assessment.

## Failure modes

- Every recurring question becomes a new agent, and overlapping agents give inconsistent answers.
- The register is not checked, and a second agent is built beside an owned one.
- An agent is approved with no owner for its knowledge, and its answers decay.
- The kind of agent is chosen from the team's favourite tool rather than what the agent must do.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Approve an agent that has no agreed business owner.
- Skip the check for an existing agent, shared prompt or scenario.
- Choose a kind of agent or build path from habit, or assert its capabilities from memory.
- Reject a request without routing the requester to something that helps.
