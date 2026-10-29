---
name: topics-and-orchestration
description: Designs how a Copilot Studio agent decides what to do - which requests generative orchestration handles from the descriptions of knowledge, tools, topics and child agents, which need authored topics with fixed steps, and how triggers, variables, system topics and redirects fit together. Use when planning an agent's topics, when it picks the wrong topic or tool, or when authored topics keep multiplying.
license: CC-BY-4.0
metadata:
  department: copilot-studio
  lifecycle: Deliver, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: copilot-studio, power-platform
  edition-support: starter, scale, enterprise
  reviewers: design-authority, evaluation-quality
  sources: ms-copilot-studio-guidance, ms-agents-extensibility, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# Topics and orchestration

## Purpose

Every Copilot Studio agent has to decide, turn by turn, whether to answer from knowledge, call a tool, run an authored
topic or pass to another agent. This skill designs that decision layer: what is left to generative orchestration, what
is authored as a fixed topic, and how the descriptions, triggers and variables are written so the agent chooses well.
It usually goes wrong in one of two directions - hundreds of trigger-phrase topics that recreate a brittle decision tree,
or everything left to the model, including steps that must happen the same way every time.

## When to use

- A solution design exists and the agent's topics and orchestration need detailed design before build.
- The agent picks the wrong topic, tool or knowledge source, or asks for information it already has.
- Authored topics are multiplying and nobody can say which one fires for a given request.
- An existing classic, trigger-phrase agent is being moved to generative orchestration.

## When not to use

- The overall solution design across knowledge, tools, identity and channels - use `copilot-studio:studio-agent-design`.
- Wording, tone, clarifying questions, fallback messages and hand-off to people - use `copilot-studio:conversation-design`.
- Writing the agent's general instructions text - use `m365-agents:agent-instructions`.
- Designing the tools the orchestrator calls - use `copilot-studio:studio-actions-and-tools`.
- Splitting work across child or connected agents - use `copilot-studio:multi-agent-design`.

## Questions to ask first

1. Which requests must follow exactly the same steps or wording every time, for regulatory, safety or audit reasons?
2. Which requests need information collected and validated before anything happens, and what makes an input valid?
3. Is the agent using generative orchestration, classic trigger-phrase routing, or a mixture, and why?
4. Which knowledge sources, tools and child agents can the orchestrator choose between, and do their descriptions overlap?
5. What should happen when the agent cannot tell which path the user wants?

## Required inputs

- The solution design and its question-to-mechanism map from `copilot-studio:studio-agent-design`.
- The brief's representative questions and exclusions, in users' own words.
- The list of tools, knowledge sources and child agents with their current names and descriptions.
- Any mandated wording or sequence, with its owner (for example compliance or legal).

If mandated wording has no owner, record it as unconfirmed and do not author it from memory. If representative
questions are missing, orchestration cannot be tested; send the design back for them.

## Decision framework

Decide per request type, not per agent.

| Request type | Mechanism | Why |
|---|---|---|
| Open question answerable from owned knowledge | Generative answer from knowledge | Authoring cannot anticipate phrasing; knowledge descriptions guide selection |
| Single action with clear inputs | Tool chosen by the orchestrator, with input descriptions | The orchestrator fills inputs and asks for missing ones |
| Mandated wording, consent, disclosure or eligibility check | Authored topic with fixed messages and conditions | The path must be identical and auditable |
| Multi-turn data capture with validation rules | Authored topic with typed questions and validation | Validation must not depend on model judgement |
| Escalation, hand-off, sign-in, error and end of conversation | System topics, customised | Consistent platform behaviour; see `copilot-studio:conversation-design` |
| A distinct domain with its own owner | Child or connected agent | See `copilot-studio:multi-agent-design` |

A topic is warranted only when it removes a risk or a failure that generative orchestration demonstrably cannot handle.
If two candidate mechanisms have descriptions a colleague could confuse, the orchestrator will confuse them too; rewrite
or merge before adding more.

## Practitioner approach

Begin with an inventory of everything the orchestrator can choose: knowledge sources, tools, authored topics and child
agents. Write each one's name and description on a single page and read them as if you were the model. Overlap is the
most common cause of wrong choices. A description should say what the item does, when to use it, and when not to,
using the words users actually use rather than system names.

Map each representative question to its intended mechanism, then look for gaps and collisions. Questions with no
mechanism become knowledge gaps or exclusions; questions with two candidates need sharper descriptions. Keep the map,
because it is the basis of orchestration tests.

Author topics sparingly and for a reason you can state. A good authored topic is short, has a clear entry condition,
collects typed and validated inputs, calls the tool or flow it needs and ends deliberately. Give each topic a description
that orchestration can use, and avoid trigger phrases doing the work of descriptions where generative orchestration is
on. Use variables with clear scope: topic variables for one path, global variables only for context that every path
needs, such as the user's region. Uncontrolled globals are a frequent source of answers that leak context from one
part of the conversation into another.

Customise the system topics rather than ignoring them. Escalation, fallback, sign-in, errors and conversation end are
where trust is won or lost, and their defaults rarely fit the organisation's support routes. Agree their behaviour with
`copilot-studio:conversation-design`.

Write the agent's instructions to set policy for the orchestrator - priorities, what to refuse, when to ask a clarifying
question, when to cite - rather than to script individual answers. Instructions that list special cases for specific
questions are a sign that knowledge or descriptions need fixing instead.

Test orchestration explicitly. Run the representative questions and inspect which mechanism the agent chose, using the
test pane and activity views where available, not only whether the final answer looked right. A right answer reached by
the wrong path will break when content changes. Record choices and failures, fix the description or topic that caused
them, and re-run.

As the agent grows, review the inventory every release. Retire topics nobody triggers, merge near-duplicates and watch
for a creeping return to decision-tree authoring.

## Outputs

- An orchestration inventory: every knowledge source, tool, topic and child agent with its name, description and intended use.
- A request-to-mechanism map with the reason each authored topic exists.
- Topic specifications for each authored topic: entry condition, inputs and validation, steps, variables, exit.
- System topic behaviour agreed with conversation design, recorded in the `studio-solution-design`.

## Microsoft platform considerations

Copilot Studio supports generative orchestration and classic routing, and how descriptions, trigger phrases, system
topics and variables behave differs between them and changes between releases. Check `ms-copilot-studio-guidance` for
current behaviour and any preview status before designing around a capability. `ms-agents-extensibility` helps explain
how topics, tools and agents relate when the same capability is exposed through Microsoft 365 Copilot.

## Adoption considerations

Users do not know topic names; they type what they need. Design from their phrasing, and use analytics after launch to
find requests the orchestrator mishandles, feeding them back through `copilot-studio:studio-analytics`.

## Knowledge considerations

When the orchestrator picks the wrong knowledge source, the cause is usually overlapping or vague source descriptions,
or two sources that disagree. Fix descriptions here and route content conflicts to `copilot-studio:studio-knowledge-architecture`.

## Security and privacy considerations

Global variables and topic outputs can carry personal or sensitive data into later turns, tools and transcripts. Scope
variables narrowly, clear them when a path ends, and never place secrets in topic logic.

## Responsible AI considerations

Paths that affect people's entitlements, safety or rights should be authored, deterministic and explainable rather than
left to model choice. Record which those paths are so `responsible-ai` reviewers can see where judgement is and is not
delegated to the model.

## Evaluation requirements

Orchestration tests check the mechanism chosen as well as the answer. The request-to-mechanism map provides the cases,
with an agreed rate of correct routing and zero tolerance for mandated paths being bypassed. Detailed planning sits with
`copilot-studio:studio-testing-and-evaluation`.

## Value measures

Track the share of sessions that reach the intended mechanism, escalations caused by misrouting and the number of
authored topics over time, measured by the agent owner at agent level. A falling topic count with stable routing quality
is a sign of a healthier design.

## Scale notes

### Starter

Keep to generative orchestration with a handful of authored topics for mandatory paths, and one page of descriptions the
maker and business owner have both read.

### Scale

Publish description-writing standards and reusable topic patterns (sign-in, escalation, consent) so agents behave
consistently, and review orchestration inventories at each release.

### Enterprise

Hold shared system-topic patterns and description standards centrally, and require orchestration test evidence from tier
2 before release. Track routing quality across the portfolio to find common weaknesses.

## Hand-offs

- To `copilot-studio:conversation-design` for message wording, clarifying questions and system topic behaviour.
- To `copilot-studio:studio-actions-and-tools` for tool descriptions and inputs.
- To `copilot-studio:studio-testing-and-evaluation` with the request-to-mechanism map.
- To `copilot-studio:multi-agent-design` when a domain should become its own agent.

## Reviewer gates

From risk tier 2, `evaluation-quality` checks that orchestration tests cover every mandated path, and `design-authority`
checks that authored topics are justified and the inventory is maintainable. Mandated paths that can be bypassed are a
blocking finding.

## Failure modes

- Descriptions overlap, so the orchestrator alternates between two tools or sources for the same request.
- A mandated disclosure is left to generative answers and is paraphrased differently each time.
- Global variables carry one user's earlier context into an unrelated action.
- The team tests final answers only, and misrouting goes unnoticed until content changes.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Author a topic for every question users might ask.
- Leave mandated wording, consent or eligibility steps to model judgement.
- Patch misrouting by adding question-specific instructions instead of fixing descriptions.
- Store secrets or credentials in topic logic or variables.
