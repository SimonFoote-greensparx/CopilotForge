---
name: multi-agent-design
description: Designs Copilot Studio solutions in which agents work together - child agents, connected agents reused across teams and calls to agents on other Microsoft platforms - deciding when to split, how the parent routes and passes context, which identity each uses, who owns each and how failures are contained. Use when one agent has grown too broad, when teams want to reuse each other's agents, or when an agent must hand work to another.
license: CC-BY-4.0
metadata:
  department: copilot-studio
  lifecycle: Envision, Deliver, Scale
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 2, 3, 4
  platforms: copilot-studio, ai-foundry, m365-agents, power-platform
  edition-support: scale, enterprise
  reviewers: design-authority, security-privacy, responsible-ai
  sources: ms-copilot-studio-guidance, ms-agents-extensibility, ms-agents-compare, ms-copilot-studio-security-governance, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Multi-agent design

## Purpose

As agents mature, a single agent often tries to do too much, or several teams build agents that would be more useful
together. This skill designs Copilot Studio solutions in which agents cooperate: when to split work into child or
connected agents, how a parent decides which agent to call and what context it passes, whose identity each agent uses,
who owns each part, and how failures, loops and accountability are handled. Multi-agent designs usually go wrong when
splitting is done for elegance rather than need, when context and permissions leak across agents, and when nobody owns
the behaviour of the whole.

## When to use

- One agent's scope, knowledge and tools have grown so broad that orchestration and testing are suffering.
- Several teams own agents in related domains and want users to reach them through one front door.
- An agent needs to call an agent built by another team, or on another Microsoft platform such as Foundry.
- A design proposes several agents and the split needs testing before build.

## When not to use

- Designing a single agent's overall solution - use `copilot-studio:studio-agent-design`.
- Routing between topics, tools and knowledge within one agent - use `copilot-studio:topics-and-orchestration`.
- Agentic workflows with bounded autonomy built on Foundry - use `ai-foundry:agentic-workflow-design`.
- Hand-off from an agent to a person or contact centre - use `copilot-studio:conversation-design`.
- Formal review of the architecture - use `design-authority:ai-design-review`.

## Questions to ask first

1. What problem does splitting solve - scope too broad, different owners, different release cycles, reuse - and could better descriptions or topics solve it instead?
2. Which agent does the user talk to, and does the user need to know other agents are involved?
3. What context passes between agents, and is any of it sensitive or beyond the receiving agent's purpose?
4. Whose identity does each agent use for knowledge and tools when called by another agent?
5. Who owns the end-to-end behaviour, and who owns each agent?

## Required inputs

- The solution design for each agent involved, with knowledge maps and action registers.
- Ownership for each agent and agreement from owners of agents being reused.
- The authentication design for each agent.
- The risk tier of the combined solution, which is at least the highest tier of any component.

If the owner of a reused agent has not agreed to it being called, the design cannot depend on it. Record the dependency
as unconfirmed.

## Decision framework

| Pattern | Use when | Watch for |
|---|---|---|
| One agent with better descriptions or topics | Problems are misrouting or clutter within one owner's domain | Splitting would add cost without solving the cause |
| Child agents within one agent | One owner, distinct sub-domains with their own instructions, knowledge or tools | Released together; ownership stays with the parent owner |
| Connected agents | Separate owners or release cycles, reuse across several parents | Versioning, contracts and availability between teams |
| Calls to agents on other platforms | Specialist capability built in Foundry or elsewhere in the Microsoft estate | Identity, data leaving the environment, latency and support boundaries |

Split only when at least one of these holds: different owners, different release cycles, a sub-domain whose instructions
conflict with the rest, or genuine reuse by more than one parent. The combined solution takes the highest risk tier of
its parts, and reviewers assess it as a whole.

## Practitioner approach

Test the need before designing the split. Many "we need multiple agents" proposals are really one agent with overlapping
descriptions or an unstructured knowledge layer. Try fixing the single agent first and record why that was not enough.

Design from the user's point of view. Usually one agent is the front door and others work behind it. Decide whether
users should be told when another agent is involved; where a connected agent has a different owner or acts on different
systems, telling users improves transparency and helps support.

Write a contract for each agent-to-agent call. Describe what the called agent does, when the parent should call it, the
inputs it accepts, the outputs it returns, and what it does not do. Treat these descriptions as carefully as tool
descriptions, because the parent's orchestrator chooses agents the same way it chooses tools.

Control context deliberately. Pass only what the called agent needs to do its job; do not forward the whole
conversation by default. Sensitive data passed to an agent with a broader audience, different logging or a different
environment is a data exposure. Record what passes in each direction.

Keep identity honest. Each agent should act with the end user's identity where possible, so that the combined solution
cannot do more than the user could. Where a called agent uses a service identity, the parent's users inherit its reach;
review that explicitly.

Contain failure. Decide what the parent does when a called agent is unavailable, slow or returns nothing useful, and
prevent loops where agents call each other repeatedly. Set clear limits and fallbacks, and tell the user plainly when
part of their request could not be completed.

Assign ownership at two levels: each agent's owner, and an owner for the end-to-end behaviour who coordinates releases,
testing and incidents across agents. Version connected agents and agree change notice between teams, so a change to a
shared agent does not silently break its callers.

Test end to end as well as per agent: routing between agents, context passed, identity at each step, failures of each
dependency and the user's experience across the whole conversation.

## Outputs

- A multi-agent design: agents, pattern for each, the reason for the split, and a diagram of calls and context flows.
- An agent contract for each agent-to-agent call: purpose, when called, inputs, outputs, exclusions and version.
- An identity and context map showing what passes between agents and under which identity each acts.
- Ownership at agent and end-to-end level, recorded in the `studio-solution-design`.
- End-to-end test cases including dependency failures and loop prevention.

## Microsoft platform considerations

Child agents, connected agents, agent-to-agent protocols and calls to agents on other Microsoft platforms are developing
quickly and several capabilities may be in preview. Check `ms-copilot-studio-guidance`, `ms-agents-extensibility` and
`ms-agents-compare` for what is currently supported, and `ms-copilot-studio-security-governance` for admin controls over
which agents may be connected. Do not commit to a pattern without confirming it in the source records.

## Adoption considerations

Users want one place to ask. A well-designed front door with specialist agents behind it can simplify adoption, but only
if the experience feels coherent; test with users, not only with the teams who own each agent.

## Knowledge considerations

Each agent keeps its own knowledge with its own owners. Avoid connecting the same source to several agents with different
descriptions, which produces conflicting answers across the solution.

## Security and privacy considerations

Context passed between agents, service identities in called agents and data crossing environments or platforms are the
main exposures. Map them, minimise them and send the map to `security-privacy:data-exposure-review` and
`security-privacy:connector-review`.

## Responsible AI considerations

Accountability blurs when several agents contribute to an outcome. Make one owner accountable for the end-to-end
behaviour, keep a human decision point for outcomes affecting people, and make it possible to trace which agent produced
which part of an answer or action.

## Evaluation requirements

Evaluate each agent on its own and the solution end to end, including routing between agents, context minimisation,
identity at each step, dependency failures and loops. From tier 3, the `evaluation-quality` reviewers agree the end-to-end evaluation.

## Value measures

Track end-to-end resolution, failures caused by dependencies and reuse of connected agents across parents, owned by the
end-to-end owner and reported at solution level.

## Scale notes

### Starter

Not usually needed; keep to single agents and fix scope and descriptions first. Child agents within one owner's agent
are the most a starter organisation should attempt.

### Scale

Child agents for distinct sub-domains, and a small number of connected agents with contracts, owners and versioning.

### Enterprise

A catalogue of reusable connected agents with contracts and owners, end-to-end owners for composite solutions, and
design authority review for every new cross-team or cross-platform call.

## Hand-offs

- To `copilot-studio:studio-agent-design` for each agent's design.
- To `ai-foundry:agentic-workflow-design` where Foundry agents take part.
- To `security-privacy:data-exposure-review` with the identity and context map.
- To `copilot-studio:studio-testing-and-evaluation` with end-to-end test cases.

## Reviewer gates

`design-authority` reviews every multi-agent design for necessity and supportability, `security-privacy` reviews context
and identity flows, and `responsible-ai` reviews accountability where outcomes affect people. The solution is reviewed at
the highest tier of its parts; unreviewed context flows to an agent with broader access are a blocking finding.

## Failure modes

- Agents are split for neatness, doubling ownership and testing effort without solving a real problem.
- The whole conversation is forwarded to a connected agent with a wider audience and different logging.
- A connected agent changes without notice and its callers start failing.
- Two agents call each other in a loop, and nobody owns the end-to-end behaviour.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Split an agent without recording the problem the split solves.
- Pass more context between agents than the called agent needs.
- Depend on another team's agent without its owner's agreement and a versioned contract.
- Leave a composite solution without an owner for its end-to-end behaviour.
