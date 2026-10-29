---
name: agent-testing
description: Builds a proportionate test plan and a small evaluation set of real user questions with expected answers, covering groundedness, refusal and out-of-scope behaviour, permission trimming across different users and regression after change, against a threshold the business owner agrees. Use when an agent is ready for testing, before widening its audience, or after its instructions or knowledge change.
license: CC-BY-4.0
metadata:
  department: m365-agents
  lifecycle: Deliver, Assure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio
  edition-support: starter, scale, enterprise
  reviewers: evaluation-quality, security-privacy
  sources: ms-copilot-studio-guidance, ms-agent-builder, ms-copilot-privacy, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Agent testing

## Purpose

Agents are probabilistic: the same question can produce different wording, and a small change to instructions or
knowledge can quietly break answers that used to be right. This skill gives an agent a proportionate test plan and a
small, durable evaluation set of real questions with expected answers, run before release and after every change. Agent
testing usually goes wrong in one of two ways: the maker tries a few friendly questions and calls it done, or the team
attempts an exhaustive test that never finishes and is never repeated.

## When to use

- An agent built from an approved brief is ready for testing before release.
- An agent is about to be shared with a wider audience or a higher risk tier.
- Instructions, knowledge sources, actions or the underlying configuration have changed.
- Users report wrong, ungrounded or surprising answers and the team needs evidence.

## When not to use

- Writing the agent's scope, behaviour rules and seed questions - use `m365-agents:agent-use-case-design`.
- Checking whether knowledge sources are owned, current and correctly shared - use `m365-agents:knowledge-source-readiness`.
- Deciding whether the agent can be released and who supports it - use `m365-agents:agent-release-readiness`.
- Formal evaluation strategy, golden datasets, red teaming and release evidence for tier 3 and above - the `evaluation-quality` department (planned).

## Questions to ask first

1. What does a good answer look like for this agent, and who can judge it with authority?
2. What must the agent refuse or redirect, and what should it say when its knowledge is silent?
3. Which user groups will use it, and do they have different access to the underlying content?
4. What pass rate would the business owner accept for release, and which failures are never acceptable?
5. What changes are likely after release, and who will re-run the tests when they happen?

## Required inputs

- The agent brief with purpose, scope, exclusions, behaviour rules and seed questions.
- Knowledge readiness verdicts, including known contradictions and coverage gaps.
- Test accounts or willing testers representing each audience group and at least one user outside the audience.
- The risk tier, which sets the depth of testing.

Where test users with different permissions are not available, permission-trimming tests cannot be run; record that as
a gap, and from risk tier 2 treat it as a blocker to release rather than assuming trimming works.

## Decision framework

Depth rises with risk tier. Each tier includes everything above it.

| Tier | Minimum evaluation set | Tests required | Who signs |
|---|---|---|---|
| 1 | 15-25 questions | In-scope answers, three refusal cases, one change re-run | Agent owner |
| 2 | 30-60 questions | Adds groundedness checks, out-of-scope probes, permission tests with two or more user profiles, regression set | Business owner, with `security-privacy` evidence |
| 3 | 60 or more, with variants | Adds adversarial prompts, action confirmation tests, failure handling, monitoring baseline | Business owner, `evaluation-quality` (planned) |
| 4 | Agreed with `evaluation-quality` | Adds independent testing and human oversight tests | Accountable executive |

Score each answer on four dimensions: correct (matches the expected answer in substance), grounded (supported by a cited
or identifiable source), appropriate (tone, scope and refusal behaviour as specified) and safe (no content the user
should not see). The release threshold is a pass rate per dimension agreed in advance by the business owner, plus a
list of zero-tolerance failures, such as exposing restricted content or acting without confirmation, where a single
occurrence fails the test.

## Practitioner approach

Build the evaluation set from the users, not the maker. Start with the seed questions from the brief and add questions
from the people who will use the agent, in their own words, including the clumsy and incomplete ones. For each, write
the expected answer in substance and the source it should come from. Ask the knowledge owner to confirm the expected
answers; a test set with wrong expectations is worse than none.

Add the edges deliberately. Include questions just outside scope, questions the brief says must be redirected, questions
where knowledge is silent, questions that invite the agent to speculate about a named person, and requests to ignore its
instructions. Include the contradictions found during knowledge readiness, because they show which version the agent
prefers.

Test permission trimming with real differences in access. Run the same questions as a user in the audience, a user with
narrower access and a user outside the audience. The agent should only use content each person can open. If a user
outside the audience can reach the agent and get substantive answers from sensitive content, that is a zero-tolerance
failure and a finding for `security-privacy:data-exposure-review`.

If the agent takes actions, test that each write action asks for confirmation, uses the expected identity, and fails
safely when the target system is unavailable or the user lacks rights.

Run each question more than once, because answers vary. Score against the four dimensions, record the actual answer,
and note whether failures trace to instructions, knowledge or configuration. Fix the cause, not the symptom: adding a
special-case instruction for every failed question makes the agent brittle.

Agree the threshold before you look at results. Present results to the business owner as pass rates per dimension, the
list of failures with causes, and any zero-tolerance breaches. The owner decides whether the agent meets the threshold;
the maker does not grade their own work.

Keep the set as the regression pack. After any change to instructions, knowledge or actions, re-run at least the
regression subset and compare with the last baseline. Store the set, results and decisions with the agent's release
record so the next owner can repeat them.

## Outputs

- A test plan and evaluation set: questions, expected answers, expected sources, edge and refusal cases, permission profiles and action tests.
- A results record scored on correctness, groundedness, appropriateness and safety, with causes and fixes.
- The test evidence section of the `agent-release-checklist`, with the agreed threshold and the business owner's decision.
- A regression subset and the trigger list of changes that require it to be re-run.

## Microsoft platform considerations

Agent-building routes offer different testing, analytics and evaluation features, and these are changing quickly.
Use what the chosen route provides and check current capabilities in the source records (`ms-copilot-studio-guidance`,
`ms-agent-builder`) rather than assuming a feature exists. Permission trimming depends on how each knowledge source is
connected; confirm the current behaviour in `ms-copilot-privacy`.

## Adoption considerations

Involve real users as testers; they find the questions makers never think of, and they become early advocates. Share
the known limits from testing with users at launch, so expectations match what the agent can do.

## Knowledge considerations

Most answer failures trace to knowledge, not instructions. Route knowledge-caused failures back to the knowledge owner
through `m365-agents:knowledge-source-readiness` and re-test after the fix rather than patching instructions.

## Security and privacy considerations

Never place real personal or confidential data in test questions or expected answers beyond what the testers may see.
Permission-trimming and action tests provide evidence for the `security-privacy` reviewer from risk tier 2.

## Responsible AI considerations

Include questions that probe for unfair, speculative or overconfident answers about people, and check that the agent
signals uncertainty and cites sources. For agents touching decisions about people, the `responsible-ai` department
(planned) sets additional tests from tier 3.

## Evaluation requirements

This skill is the agent's evaluation. The minimum is an owner-agreed threshold per dimension, zero-tolerance failures
named, results recorded, and a regression subset re-run after every material change.

## Value measures

Track pass rate over time, the number of regressions caught before users saw them, and the time to re-test after a
change. The agent owner owns these measures; report by agent, never by individual maker or tester.

## Scale notes

### Starter

A spreadsheet of 15-25 real questions, expected answers and three refusal cases, run by the maker and two users, with
the owner deciding. Re-run it whenever the agent changes.

### Scale

Use a shared test set format across agents, require permission tests with at least two profiles from tier 2, and keep
regression packs with the agent's record so testing survives a change of owner.

### Enterprise

Hand tier 3 and 4 agents to the `evaluation-quality` department (planned) for formal evaluation and red teaming, and
automate regression runs where the route supports it. Report pass-rate trends across the portfolio.

## Hand-offs

- To `m365-agents:agent-release-readiness` with the test evidence and the owner's decision.
- To `security-privacy:data-exposure-review` with permission-trimming results from tier 2.
- Back to `m365-agents:knowledge-source-readiness` for knowledge-caused failures.
- To the `evaluation-quality` department (planned) for tier 3 and above.

## Reviewer gates

From risk tier 2, `evaluation-quality` (planned) reviews the evaluation set and threshold, and `security-privacy` reviews
permission-trimming and action test evidence. Until `evaluation-quality` exists, the CoE lead checks that the threshold
was agreed before results were seen.

## Failure modes

- The maker writes the questions and expected answers alone, so the test confirms the maker's assumptions.
- The threshold is set after results are known and drifts to whatever the agent achieved.
- Permission tests use only the maker's account, so oversharing is never exercised.
- No regression run after a knowledge update, and a previously correct answer silently changes.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Let the maker approve their own agent against a threshold they set after testing.
- Skip permission-trimming tests with different users from risk tier 2.
- Patch failures with question-specific instructions instead of fixing the cause.
- Use real personal data in test cases beyond what the testers are entitled to see.
