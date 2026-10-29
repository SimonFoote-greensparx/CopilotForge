---
name: studio-testing-and-evaluation
description: Plans layered testing of a Copilot Studio agent - topic paths, orchestration choices, knowledge answers, tool and flow calls, authentication per channel, failure handling and regression after change - using the authoring test tools, repeatable evaluation sets and owner-agreed thresholds in a test environment. Use when a Studio agent with tools, topics or several sources needs testing, or when a change must be regression-tested.
license: CC-BY-4.0
metadata:
  department: copilot-studio
  lifecycle: Deliver, Assure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: copilot-studio, power-platform
  edition-support: starter, scale, enterprise
  reviewers: evaluation-quality, security-privacy
  sources: ms-copilot-studio-guidance, ms-copilot-studio-security-governance, nist-ai-rmf, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# Studio testing and evaluation

## Purpose

A Copilot Studio agent can give a right answer for the wrong reason: the orchestrator chose the wrong source but the
content happened to match, or a flow failed but the agent still said "done". This skill tests the agent layer by layer -
orchestration, topics, knowledge, tools, identity and channels - as well as end to end, and turns the results into a
regression pack that runs before every import to production. Studio testing usually goes wrong when makers test only in
the authoring test pane as themselves, when tests cover answers but not actions, and when nobody re-runs anything after
a change.

## When to use

- A Studio agent with topics, tools, flows or several knowledge sources is ready for testing.
- A change to instructions, descriptions, knowledge, tools or connectors is about to be imported to test or production.
- Users report misrouting, failed actions or answers that ignore their permissions.
- The release gate needs evidence that the agent behaves correctly in its real channels.

## When not to use

- The answer-quality evaluation set and owner threshold common to all agents - use `m365-agents:agent-testing`, which this skill builds on.
- The organisation's evaluation strategy and golden datasets for higher tiers - use `evaluation-quality:ai-evaluation-strategy` and `evaluation-quality:golden-dataset`.
- Prompt injection and adversarial security testing - use `security-privacy:ai-security-testing`.
- Deciding whether the tested agent can be released - use `m365-agents:agent-release-readiness`.

## Questions to ask first

1. Which layers does this agent have - authored topics, generative orchestration, knowledge sources, tools, flows, child agents - and which changed?
2. What does the business owner accept as a pass, and which failures are never acceptable?
3. Which test users exist with different permissions, and is there a test environment with test data and test connections?
4. Which channels will the agent be published to, and can each be tested before release?
5. Who will re-run the regression pack after each change, and where are the results kept?

## Required inputs

- The solution design, request-to-mechanism map, question-to-source map and tool specifications.
- The evaluation set and threshold from `m365-agents:agent-testing`.
- A test environment with its own connections and safe test data, from `copilot-studio:studio-alm`.
- Test accounts representing each audience and at least one user outside it.

If there is no test environment, tools that write cannot be tested safely; record that as a blocker for write tools,
not a reason to test against production systems.

## Decision framework

Test every layer the agent has, at a depth set by risk tier.

| Layer | What to test | Tier 1 | Tier 2 | Tier 3 and 4 |
|---|---|---|---|---|
| Orchestration | Correct mechanism chosen for each request | Sample | Full map | Full map with paraphrases |
| Authored topics | Every branch, validation and exit | Main paths | All branches | All branches plus invalid input |
| Knowledge | Groundedness, citation, silent knowledge, freshness | Evaluation set | Plus trimming with two profiles | Plus adversarial and conflicting sources |
| Tools and flows | Selection, inputs, confirmation, failure, repeat | Each tool once | All failure paths | Plus load and unavailable systems |
| Identity and channels | Sign-in, trimming, run-as per channel | Primary channel | Every channel | Every channel and device type |
| Regression | Re-run after change | Changed layer | Regression pack | Full pack, independently reviewed |

Zero-tolerance failures at any tier: writing without confirmation, exposing content the user cannot open, reporting
success when an action failed, and bypassing a mandated topic.

## Practitioner approach

Start from the design artefacts. The request-to-mechanism map gives orchestration cases, the question-to-source map gives
knowledge cases, tool specifications give action cases, and the conversation samples give tone and escalation cases. If
these artefacts do not exist, testing will drift towards whatever the maker thinks of; send the gap back to design.

Test orchestration explicitly. For each case, record which topic, tool, source or child agent was chosen, using the test
pane's activity and tracing views where available, not only the final message. A correct answer by an unintended route
is a failure, because it will break as content changes.

Test tools and flows in a test environment with test connections and test data. Check that the orchestrator selects the
right tool, asks for inputs it must not guess, confirms before writing, returns a reference, and handles permission denial,
validation failure, duplicates and an unavailable system. Then check the target system to confirm what actually happened.

Test identity outside the authoring canvas. The maker usually has broad access and sees more than users will. Publish to
the test environment's channels and test as ordinary users with different access, including someone outside the audience.
Test sign-in in each channel the agent will use.

Run each case more than once, because generated answers vary. Score against the agreed dimensions and record actual
responses, the mechanism chosen and the cause of each failure: description, instruction, knowledge, tool or
configuration. Fix causes rather than adding special-case instructions, then re-run the affected cases.

Use automated or batch evaluation features where the platform provides them, and check the source records for what is
currently available. Automation helps with volume and repeatability; it does not replace a business owner reviewing a
sample of answers.

Turn the cases into a regression pack stored with the agent's solution. Before every import to production, run the pack
in the test environment, compare with the last baseline and record the result in the release record. Agree the threshold
with the business owner before results are seen.

## Outputs

- A layered test plan covering each layer the agent has, with depth by risk tier.
- Test cases and results recording the mechanism chosen, actual response, score and cause of failures.
- A regression pack stored with the solution, and a baseline result.
- Test evidence for the `agent-release-checklist`, including zero-tolerance checks and the owner's decision.

## Microsoft platform considerations

Copilot Studio provides an authoring test pane, activity and tracing views, and evaluation features that are evolving,
with some in preview. Check `ms-copilot-studio-guidance` for what is currently available and how it behaves, and
`ms-copilot-studio-security-governance` for test environment controls. Do not design a test approach that depends on a
feature without confirming it exists in the organisation's environments.

## Adoption considerations

Involve real users in channel testing; they find phrasing and sign-in problems makers miss. Share known limits from
testing in launch materials so expectations are realistic.

## Knowledge considerations

Knowledge failures dominate answer tests. Route them to the knowledge owner through
`copilot-studio:studio-knowledge-architecture` and re-test after content is fixed, rather than adjusting instructions.

## Security and privacy considerations

Test in a test environment with test data and test connections, never against production records. Do not use real
personal data in test cases. Identity, trimming and action results are evidence for `security-privacy` from tier 2, and
adversarial testing is handed to `security-privacy:ai-security-testing`.

## Responsible AI considerations

Include cases that probe for speculative or unfair answers about people, overconfident responses and failure to offer a
person on sensitive subjects. From tier 3, agree additional cases with the `responsible-ai` reviewers.

## Evaluation requirements

This skill is the agent's technical evaluation. The minimum is every layer tested at its tier depth, zero-tolerance checks
passed, an owner-agreed threshold met, and a regression pack re-run before every production import.

## Value measures

Track regression failures caught before production, defects found by users after release and time to complete a
regression run, owned by the agent owner and reported by agent, never by individual maker or tester.

## Scale notes

### Starter

A spreadsheet of cases per layer, run in a test environment by the maker and two users, with the business owner deciding.

### Scale

A shared test plan format, regression packs stored in solutions, mandatory channel testing as ordinary users and a check
at import that the regression pack was run.

### Enterprise

Automate regression runs in deployment pipelines where supported, hand tier 3 and 4 agents to `evaluation-quality` for
independent evaluation, and report regression trends across the portfolio.

## Hand-offs

- To `m365-agents:agent-release-readiness` with the test evidence.
- To `security-privacy:ai-security-testing` for adversarial testing from tier 2.
- To `evaluation-quality:regression-evaluation` for independent regression review at tier 3 and above.
- Back to the owning design skill for each failure cause.

## Reviewer gates

From risk tier 2, `evaluation-quality` reviews coverage of layers, the threshold and zero-tolerance checks, and
`security-privacy` reviews identity, trimming and action evidence. Any zero-tolerance failure is blocking.

## Failure modes

- Tests run only in the authoring pane as the maker, so trimming and sign-in problems reach users.
- Answers are tested but actions are not, and a failing flow reports success in production.
- Tool tests run against production systems and create real records.
- The regression pack exists but nobody runs it before importing a change.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Test write tools against production systems or with real personal data.
- Accept a right answer reached through the wrong mechanism as a pass.
- Let the maker set the threshold after seeing the results.
- Import a change to production without re-running the regression pack.
