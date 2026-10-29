---
name: requirements-to-build
description: Turns an agreed solution brief into small, ordered, testable work items an AI coding agent and its human reviewers can deliver - each with a clear outcome, acceptance tests, boundaries and dependencies - so generated changes stay reviewable. Use when a Copilot Code build is about to start, when agent-generated pull requests are too large to review, or when work items keep coming back because acceptance was unclear.
license: CC-BY-4.0
metadata:
  department: copilot-code
  lifecycle: Deliver
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: copilot-code, github
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Requirements to build

## Purpose

An AI coding agent works best on a well-specified, bounded piece of work, and humans review best when each change is small
enough to understand. A solution brief is neither: it describes the whole outcome. This skill breaks the brief into
ordered work items, each with a clear outcome, acceptance tests, boundaries on what it may touch, and dependencies, sized
so that the resulting change can be reviewed properly. It goes wrong when work items are copied straight from feature
lists, so the agent produces enormous changes that reviewers approve because they cannot face reading them.

## When to use

- A build is about to start from an agreed `code-solution-brief`.
- Pull requests produced by the coding agent are too large or too mixed to review properly.
- Work items come back repeatedly because acceptance was unclear or the agent interpreted them differently.
- A team is planning which items to give the coding agent and which to keep for engineers.

## When not to use

- Writing the solution brief itself - use `copilot-code:code-solution-brief`.
- Setting repository-wide instructions, conventions and constraints for the agent - use `copilot-code:repository-context`.
- Validating the finished application against the brief - use `copilot-code:application-validation`.
- Setting the testing strategy for pro-code AI solutions - use `ai-engineering:ai-solution-testing`.

## Questions to ask first

1. Which acceptance criteria in the brief describe user-visible behaviour, and which describe constraints that apply everywhere?
2. What is the thinnest working slice that delivers something a user could try end to end?
3. Which items touch security-sensitive areas (identity, data access, external calls, secrets) and should be kept small and reviewed closely?
4. Which items are well suited to the coding agent, and which need an engineer's design judgement first?
5. What must be true before each item can start?

## Required inputs

- The agreed solution brief with acceptance criteria, including negative criteria.
- The repository context and engineering standards from `copilot-code:repository-context`.
- The team's working method (backlog tool, branching, review practice).

If acceptance criteria are missing or untestable, return to the brief rather than inventing them. Never create items that
reach beyond the brief's scope without the business owner agreeing a scope change.

## Decision framework

Each work item must meet these tests before it goes to the coding agent.

| Test | Passes when | Fails when |
|---|---|---|
| Single outcome | One behaviour or one technical change | "Build the inspection module" |
| Testable acceptance | Given, when, then statements or equivalent, including at least one negative case where relevant | "Should work properly" |
| Boundaries | Names the parts of the codebase it may change and those it must not | Open-ended |
| Reviewable size | The resulting change can be read and understood in one sitting | Touches many unrelated files |
| Dependencies stated | Prerequisites and order are explicit | Hidden assumptions about earlier work |
| Suitability for the agent | Well specified, low design ambiguity, existing patterns to follow | Needs architectural or security design decisions |

| Item type | Agent suitability | Notes |
|---|---|---|
| Follows an established pattern (a new form like an existing one) | High | Point to the pattern |
| Tests for agreed behaviour | High | Review tests as carefully as code |
| New architectural element or integration | Low until designed | An engineer designs, the agent implements |
| Identity, authorisation, secrets, data access | Agent may implement, engineer must design and review | Keep items very small |

## Practitioner approach

Start by separating behaviour from constraints. Acceptance criteria that describe what a user can do become work items;
criteria that apply everywhere (accessibility, logging, no personal data in logs, approved libraries only) belong in the
repository context so every item inherits them. Mixing them produces items that repeat constraints inconsistently.

Find the thinnest end-to-end slice. A first item that lets one user complete one journey, however plainly, exposes
integration problems early and gives the business owner something real to react to. Build outwards from that slice in
small increments, each adding one behaviour.

Write acceptance tests before the code. For each item, state the behaviour as testable examples, including what must not
happen. Ask the coding agent to write or extend tests for those examples as part of the item, and review the tests first:
a test that asserts the wrong thing makes wrong code look correct. Negative cases matter most for access rules: "a site
manager cannot open another site's inspection" should be a test, not an assumption.

Set boundaries. Tell the agent which parts of the codebase the item may touch, and which it must leave alone. Agents
tend to tidy, refactor and upgrade things they pass; useful sometimes, but it makes changes larger and hides the real
change among incidental ones. If refactoring is needed, make it its own item.

Size for review, not for the agent. The agent can produce a large change in minutes; a reviewer cannot understand it in
minutes. If an item would produce a change a reviewer could not read carefully in one sitting, split it. This single
rule does more for quality than any other.

Keep design decisions with people. New integrations, data models, authentication and authorisation approaches, and
anything security-sensitive should be designed by an engineer first, then implemented in small items, with the agent
following the design rather than inventing one.

Order the items by dependency and risk, record them in the team's backlog with links to the brief, and review the list
with the engineering owner and business owner before the agent starts.

## Outputs

- An ordered backlog of work items, each with outcome, acceptance tests (including negative cases), boundaries, dependencies and agent suitability.
- A list of repository-wide constraints moved into `copilot-code:repository-context`.
- Design items reserved for engineers before implementation.

## Microsoft platform considerations

Work items typically live as issues in the repository's tracking system and are assigned to the coding agent or engineers
there. How Copilot Code and coding agents accept, plan and report on work items changes over time; confirm current
behaviour in the relevant source records and the organisation's engineering guidance before designing the workflow around
a specific feature.

## Adoption considerations

Engineers new to working with a coding agent often write items too large. Pair them with someone experienced for the first
few builds and review item size together; small items quickly prove their value in faster, better reviews.

## Knowledge considerations

Not applicable as a primary concern, because work items specify software behaviour; link each item to the brief so the
reasoning behind it is retained for future maintainers.

## Security and privacy considerations

Keep identity, authorisation, data access and external calls in separate, small items with explicit negative tests, so the
security reviewer can see each change clearly. Never include real personal data or secrets in work item text or examples.

## Responsible AI considerations

Where the software supports decisions about people, include acceptance tests that prove the human decision step exists and
cannot be bypassed, and keep those items with engineers rather than delegating their design.

## Evaluation requirements

Acceptance tests written here are the unit of evidence for `copilot-code:application-validation`. Every acceptance
criterion in the brief must map to at least one work item and test.

## Value measures

Track at team level the share of items accepted at first review, average change size and rework, as indicators that items
are well specified. Never use these measures to compare individual engineers.

## Scale notes

### Starter

A short list of small items with acceptance tests is enough for a first build. Keep the agent on pattern-following and test
items until the team is confident.

### Scale

Adopt a standard item template with acceptance tests and boundaries, and review item size as part of planning.

### Enterprise

Build item standards into the engineering standards for AI-assisted work, with traceability from brief to items to tests to
release evidence for builds at risk tier 2 and above.

## Hand-offs

- To `copilot-code:repository-context` with repository-wide constraints.
- To `copilot-code:generated-code-review` with the item acceptance tests reviewers will check against.
- To `copilot-code:application-validation` with the traceability from criteria to tests.

## Reviewer gates

Not applicable as a separate gate, because work items are planning artefacts; their adequacy is tested when changes pass
`copilot-code:generated-code-review` and, from risk tier 2, when `design-authority` reviews the design items reserved for
engineers.

## Failure modes

- Items are copied from a feature list, so the agent produces changes too large to review and reviewers approve them unread.
- Tests are generated alongside the code and assert what the code does rather than what was required.
- The agent is given security-sensitive design decisions and invents an authorisation model.
- Incidental refactoring hides the real change in a large diff.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Give the coding agent a work item without testable acceptance criteria.
- Size items for the agent's speed rather than the reviewer's capacity.
- Leave identity, authorisation or data access design to the agent.
- Put secrets or real personal data in work items or examples.
