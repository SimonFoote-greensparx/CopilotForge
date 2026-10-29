---
name: generated-code-review
description: Sets and applies code review standards for changes produced by an AI coding agent - reviewable size, understanding before approval, tests checked against the work item, conventions and no unnecessary changes - so human review stays meaningful at agent speed. Use when a team starts accepting agent pull requests, when reviews have become rubber stamps, or when generated changes are merging that nobody on the team can explain.
license: CC-BY-4.0
metadata:
  department: copilot-code
  lifecycle: Deliver, Assure
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: copilot-code, github
  edition-support: starter, scale, enterprise
  reviewers: design-authority
  sources: nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Generated code review

## Purpose

Code review exists so that at least one person other than the author understands and agrees with every change. When the
author is an AI coding agent, that purpose matters more, because there is no author who understands the change at all
until a reviewer does. Agents also produce changes faster than people can read them, which pushes teams towards approving
on trust. This skill sets review standards for agent-produced changes and a way to apply them, so review remains a real
check on correctness, design and maintainability. It goes wrong when reviewers approve what they have skimmed because the
tests are green.

## When to use

- A team starts accepting pull requests produced by a coding agent.
- Reviews of agent changes have become quick approvals with few comments.
- Changes have merged that nobody on the team can explain.
- Engineering standards for review need updating to cover AI-generated code.

## When not to use

- Security-focused review of generated code - use `copilot-code:generated-code-security-review`.
- Validating the whole application against the solution brief - use `copilot-code:application-validation`.
- Reviewing the long-term maintainability and ownership of an AI-built application - use `copilot-code:maintainability-review`.
- Reviewing Copilot Cowork outputs before use - use `copilot-cowork:delegated-work-review`.

## Questions to ask first

1. Which work item does this change deliver, and what were its acceptance tests and boundaries?
2. Is the change small enough to understand fully in one sitting?
3. Do the tests assert what the work item required, including negative cases?
4. Does the change stay within its boundaries, or does it include refactoring, upgrades or files it did not need to touch?
5. Could the reviewer explain this change to a colleague and maintain it without the agent?

## Required inputs

- The work item with acceptance tests and boundaries from `copilot-code:requirements-to-build`.
- The repository conventions and protected areas from `copilot-code:repository-context`.
- Pipeline results for the change (build, tests, linting, scanning).

If the change has no linked work item, send it back. Never approve a change to a protected area without the named code
owner's review.

## Decision framework

A reviewer approves only when every standard is met.

| Standard | Met when | Send back when |
|---|---|---|
| Linked and bounded | The change links to a work item and stays within its boundaries | Unrelated files, refactors or upgrades are included |
| Reviewable size | The reviewer has read and understood all of it | Too large to read carefully in one sitting |
| Understood | The reviewer can explain what it does and why | "It looks plausible" is the honest assessment |
| Tests meaningful | Tests assert the work item's acceptance criteria, including negatives | Tests mirror the implementation or only cover the happy path |
| Conventions | Follows the repository's patterns and approved dependencies | Introduces new patterns or libraries without agreement |
| Error handling | Failures are handled deliberately and visibly | Errors swallowed, over-broad catches, or everything logged |
| No dead weight | No unused code, commented-out blocks or speculative features | Extra functionality "for later" |
| Provenance clear | The change is identified as agent-produced and the reviewer is named | Origin unclear |

From risk tier 2, changes to protected areas need a second reviewer. Reviewers are accountable for what they approve.

## Practitioner approach

Read the work item before the code. Knowing what the change was meant to do, and what it was not meant to touch, turns
review from "is this reasonable code?" into "does this do what was asked, and only that?". The second question is the one
that catches agent-generated problems.

Check size first and be willing to send changes back unread. If a change is too large to understand in one sitting, the
correct response is to ask for it to be split, not to skim it. Teams that hold this line find that agents and engineers
quickly adapt; teams that do not find that review quality quietly collapses.

Read the tests before the implementation. Ask whether each test expresses the acceptance criterion or merely restates what
the code does. Look for missing negative cases, mocks that remove the behaviour under test, and assertions so loose they
cannot fail. Good tests make the rest of the review faster; weak tests make green pipelines meaningless.

Then read the implementation for understanding. Could you explain it to a colleague? Does it follow the repository's
patterns, or has the agent introduced a new approach? Is error handling deliberate? Are there unnecessary abstractions,
duplicated logic or dead code? Coding agents are prone to verbosity and to solving problems the work item did not have.

Look at the edges of the change. Has the agent modified files outside the boundaries, upgraded a dependency, reformatted a
module or changed configuration? Incidental changes hide real ones and should be split out or removed.

Ask the agent to explain, but verify. Asking the agent why it made a choice can speed understanding, but its explanation is
not evidence; check the code says what the explanation claims.

Comment specifically and feed patterns back. Where the agent repeatedly makes the same kind of mistake, improve the
repository instructions or work item template rather than correcting it in every review. Record the reviewer on each
change so accountability is clear.

## Outputs

- Code review standards for agent-produced changes, added to the team's engineering standards.
- Review records on each change: linked work item, reviewer, comments and decision.
- A list of recurring issues fed back to `copilot-code:repository-context` and `copilot-code:requirements-to-build`.

## Microsoft platform considerations

Pull request workflows, required reviews, code owners and labels identifying agent-produced changes are provided by the
development platform and evolve. Configure them to enforce the standards, and confirm current capabilities in the relevant
source records and with the platform team.

## Adoption considerations

Reviewing agent output is a skill that takes practice. Pair reviewers for the first few weeks, share examples of good send-backs,
and make it clear that sending a change back for size or clarity is good practice, not obstruction.

## Knowledge considerations

Review comments capture design reasoning that would otherwise be lost. Encourage reviewers to record the "why" of
non-obvious choices in the code or pull request so future maintainers have it.

## Security and privacy considerations

General review is not a security review, but reviewers should flag obvious concerns (secrets, unchecked input, broad
permissions) and route them to `copilot-code:generated-code-security-review`. Never approve changes to protected security
areas without the code owner.

## Responsible AI considerations

Not applicable as a primary concern, because this skill governs review of code changes; the key accountability point is that
a named person, not the agent, approves every change.

## Evaluation requirements

Periodically sample merged agent changes and re-review them against the standards. A rising rate of issues found after
merge indicates reviews have become shallow.

## Value measures

Track at team level the share of agent changes accepted at first review, sent back for size, and defects traced to merged
agent changes. Never use review metrics to rank individual reviewers or engineers.

## Scale notes

### Starter

Adopt the standards table as a checklist in pull request templates and require one reviewer who has read the whole change.

### Scale

Enforce linked work items, labels for agent-produced changes and code owner reviews through the platform, and sample merged
changes monthly.

### Enterprise

Embed the standards in organisation-wide engineering standards, require second reviewers for protected areas from risk tier
2, and use sampling results across repositories to improve shared instructions.

## Hand-offs

- To `copilot-code:generated-code-security-review` with security concerns.
- To `copilot-code:repository-context` with recurring issues to correct at source.
- To `copilot-code:application-validation` once the build is feature-complete.

## Reviewer gates

From risk tier 2, `design-authority` may sample review records through `design-authority:architecture-conformance` to check
that agent changes follow the reference architecture and standards. Findings are blocking or advisory.

## Failure modes

- Reviewers approve skimmed changes because the pipeline is green.
- Tests generated with the code assert its behaviour rather than the requirement, so wrong behaviour passes review.
- Incidental refactoring and upgrades hide the meaningful change in a large diff.
- Nobody on the team can explain merged code, so the agent becomes the only "maintainer".

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Approve a change you have not read and understood.
- Treat a passing pipeline as a substitute for review.
- Merge agent changes to protected areas without the code owner's review.
- Use review data to rank or monitor individual engineers.
