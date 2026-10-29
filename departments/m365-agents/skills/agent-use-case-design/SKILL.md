---
name: agent-use-case-design
description: Turns an approved agent opportunity into an agent brief covering audience, purpose, scope and exclusions, instructions approach, knowledge sources, actions, the build-or-reuse decision, owner, support and success measures. Use when an idea has passed suitability as an agent, when a maker wants to start building, or when an existing agent needs its scope rewritten.
license: CC-BY-4.0
metadata:
  department: m365-agents
  lifecycle: Envision, Deliver
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, sharepoint
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, design-authority
  sources: ms-declarative-agents, ms-agent-builder, ms-agents-compare, ms-agents-extensibility, ms-copilot-studio-zoned-governance
  status: draft
  authors: Simon Foote
---

# Agent use-case design

## Purpose

An approved opportunity says an agent is the right answer; it does not yet say what the agent is for, who it serves or
what it must refuse. This skill turns the approved opportunity into an agent brief that a maker can build from, a
reviewer can judge and an owner can run. Agent work usually goes wrong here: the scope is "everything about HR", the
knowledge is "the SharePoint site", nobody is named to own the answers, and the build route is chosen because the maker
already knows one tool.

## When to use

- An opportunity has been through suitability and the agent rung was chosen.
- A maker or business team wants to start building and has no written scope.
- An existing agent has grown by accretion and needs its purpose and boundaries restated.
- Two teams want similar agents and someone must decide whether to build once or reuse.

## When not to use

- Deciding whether an agent is the right answer at all - use `opportunity-management:ai-suitability`.
- Confirming the risk tier that governs the build - use `opportunity-management:risk-classification`.
- Judging whether the knowledge the agent will ground on is fit to use - use `m365-agents:knowledge-source-readiness`.
- Writing the test plan and evaluation set - use `m365-agents:agent-testing`.
- Detailed topic, action, authentication and ALM design for a Copilot Studio build - use `copilot-studio:studio-agent-design`.

## Questions to ask first

1. Who exactly will use the agent, in which roles, and what question or task brings them to it on a normal working day?
2. What should the agent never do or answer, even if asked politely, and where should it send people instead?
3. Which knowledge will it ground on, who owns each source, and could every intended user already open that content?
4. Does it only answer, or must it also act in another system, and who would be accountable for those actions?
5. Does an existing agent, prompt or published Copilot pattern already meet most of the need?
6. Who will own the agent after release, and who will users contact when it gives a wrong answer?

## Required inputs

- The approved opportunity record and suitability decision, with business owner and problem statement, on the `opportunity-canvas`.
- The initial risk tier from `opportunity-management:risk-classification`.
- A list of candidate knowledge sources with their apparent owners.
- The organisation's approved agent-building routes and environments, from the CoE or platform team.

Where an input is missing, mark it "to confirm" in the brief and do not progress beyond a draft. In particular, never
assume a build route is approved or licensed, and never name an owner who has not agreed.

## Decision framework

Build the brief in this order; each row is a gate for the next.

| Decision | Ready when | Not ready if |
|---|---|---|
| Audience | Named roles, approximate population and where they work | "All staff" with no reason why everyone needs it |
| Purpose | One sentence naming the job and the measure it improves | The purpose lists several unrelated jobs |
| Scope and out-of-scope | In-scope questions listed, exclusions and redirects written | Exclusions are left for the instructions to "work out" |
| Knowledge | Each source has an owner and a readiness verdict | Any source is unowned or has no readiness verdict |
| Actions | Each action has a system, an accountable owner and a confirmation rule | Write actions with no human confirmation or owner |
| Build or reuse | Reuse options checked and the reason for building recorded | A new agent duplicates one already in the register |
| Route | Chosen from the source records against the agreed criteria | Chosen from habit or familiarity |
| Ownership | Business owner, knowledge owners and support route agreed | Owner is the maker by default |

For the build route, compare the options against criteria rather than products: whether the agent only answers or also
acts, how wide the audience is, whether it needs custom orchestration or its own model, and which governance zone the
organisation runs it in. Read the current capabilities and limits of Agent Builder, Copilot Studio and pro-code routes
in the source records (`ms-agents-compare`, `ms-agent-builder`, `ms-declarative-agents`) at the time of the decision,
and record what was checked.

## Practitioner approach

Start with the person, not the agent. Sit with two or three intended users and ask them to show you the last time they
needed the answer the agent is meant to give: where they looked, who they asked, how long it took and what went wrong.
Write the purpose from that evidence in one sentence with a measure, for example "Help line managers answer routine
absence-policy questions without raising a ticket, so HR advisers spend their time on complex cases." A purpose with
"and" in it usually hides two agents.

Write the scope as real questions, not topics. Ten to twenty representative questions in the users' own words become the
seed of the evaluation set later, so collect them now. Then write the out-of-scope list with equal care: the questions
the agent must decline, the ones it must redirect to a person, and the ones that touch decisions about individuals.
Every exclusion needs a destination, otherwise users experience a refusal as a dead end and stop using the agent.

Treat the instructions as a specification, not as clever prompting. The brief should state the role the agent plays,
the tone, how it handles uncertainty, when it must cite a source, what it does when knowledge is silent, and how it
behaves at the edges of scope. Leave the wording to the maker, but fix the behaviour here so testing has something to
test against.

List each knowledge source with its owner, location, audience and the readiness verdict from
`m365-agents:knowledge-source-readiness`. Because an agent answers with the permissions of the person asking, a source
that is overshared today becomes easy to discover tomorrow; flag any doubt to the `security-privacy` reviewer early
rather than at the gate.

If the agent must act, name each action, the system it touches, whether it reads or writes, whose identity it runs
under, and whether the user must confirm before anything changes. Where the action is a fixed sequence, prefer an
automation the agent calls over asking the model to improvise steps.

Before choosing a route, check the solution register and ask the CoE whether a similar agent exists. Extending an owned
agent is cheaper than running two that drift apart. When building is justified, compare routes against the decision
criteria and today's source records, not memory, and write down why the simpler route was not enough.

Close by agreeing ownership in writing: the business owner who answers for outcomes, the knowledge owners, the maker,
and the support route. Add success measures with baselines, the review date, and the risk tier. Walk the business owner
through the brief before any build starts; a brief they cannot explain back is not finished.

## Outputs

- An agent brief on the `agent-brief` template: audience, purpose, scope and out-of-scope with redirects, instructions approach, knowledge sources with owners and readiness, actions, build-or-reuse decision and route rationale, ownership, support route, success measures and risk tier.
- A seed list of representative user questions, handed to `m365-agents:agent-testing`.
- A list of open questions and preconditions, each with an owner and a date.

## Microsoft platform considerations

Declarative agents, agents built in Agent Builder, agents built in Copilot Studio and pro-code custom engine agents
differ in how they are built, shared, governed and extended. The brief should record the criteria that led to the
route, then confirm current capability, sharing options, limits and licensing from the source records, because these
change frequently. Copilot Studio agents live in Power Platform environments, so the environment, data policy and
governance zone are part of the route decision, not an afterthought.

## Adoption considerations

An agent nobody knows about delivers nothing. Name the intended users' existing channels (team sites, manager briefings,
Champion networks) in the brief so `m365-agents:agent-release-readiness` can plan communications. Involve a few users in
writing the scope; they become the first advocates and the first honest testers.

## Knowledge considerations

The agent's quality is capped by its knowledge. Every source needs an owner and a readiness verdict before build;
unowned or stale sources are preconditions to fix, routed through `m365-agents:knowledge-source-readiness` and
`knowledge-management:knowledge-lifecycle`. Prefer a small, curated source over a whole site.

## Security and privacy considerations

Record the sensitivity of each knowledge source, the intended sharing scope, any personal data the agent might surface,
and any action that changes data or reaches outside the tenant. From risk tier 2 these go to the `security-privacy`
reviewer through `security-privacy:data-exposure-review` and `security-privacy:connector-review`.

## Responsible AI considerations

If the agent's answers could inform decisions about people, money, safety or rights, write explicit human oversight
into the scope and mark the case for `responsible-ai:ai-impact-assessment` via risk classification. Users must be
able to tell they are dealing with an agent and where its answers come from.

## Evaluation requirements

The brief must contain enough to test against: representative questions, expected behaviour at the edges, and refusal
rules. The acceptance threshold itself is agreed by the business owner in `m365-agents:agent-testing`.

## Value measures

Record the baseline from the problem statement (for example tickets raised, time to answer, rework) and the measure the
business owner will use, with its source and review date. Measure at team or role level; never use agent data to
judge individual staff.

## Scale notes

### Starter

One page is enough: audience, purpose, ten real questions, exclusions, two or three sources with owners, and the named
owner. A partner may help choose the route. Most first agents should only answer, not act.

### Scale

Use the full brief for every agent through the CoE intake, check the solution register for reuse as a standard step, and
apply the governance zone the organisation has defined for each route.

### Enterprise

Federate brief writing to business-unit agent product owners using the shared template, with the hub reviewing anything
at risk tier 2 or above. Track briefs in the portfolio so overlapping agents are visible before they are built.

## Hand-offs

- To `m365-agents:knowledge-source-readiness` for each knowledge source named in the brief.
- To `m365-agents:agent-testing` with the seed questions and behaviour rules.
- To `security-privacy:data-exposure-review` and `security-privacy:connector-review` from risk tier 2.
- To `copilot-studio:studio-agent-design` for detailed design of Copilot Studio builds.

## Reviewer gates

From risk tier 2, the brief is reviewed by `security-privacy` for knowledge exposure, sharing scope and actions, and by
`design-authority:platform-fit-review` for route choice and duplication, with the route challenge and response recorded
on the brief.

## Failure modes

- Scope is written as topics, so the agent answers confidently far outside what its knowledge supports.
- The maker becomes the owner by default, leaves the team, and the agent decays unnoticed.
- The route is chosen from familiarity, and the agent is rebuilt later when its limits are reached.
- A whole site is added as knowledge, surfacing overshared and outdated content to a wide audience.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Start a build without a named business owner who has agreed the brief.
- Leave exclusions for the instructions to infer, or decline a question without saying where to go instead.
- Choose a build route, or assert its capabilities, from memory rather than the current source records.
- Add knowledge sources that have no owner or readiness verdict.
