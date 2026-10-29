---
name: agent-instructions
description: Writes and maintains the instructions that govern a Microsoft 365 agent - role, audience, scope, how to use and cite knowledge, uncertainty and refusal behaviour, redirects, tone, response format and conversation starters - under version control with a change log and a regression run after every edit. Use when a brief is ready to build, when an agent misbehaves, or when someone wants to edit a live agent's instructions.
license: CC-BY-4.0
metadata:
  department: m365-agents
  lifecycle: Deliver, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3
  platforms: m365-agents, copilot-studio
  edition-support: starter, scale, enterprise
  reviewers: evaluation-quality
  sources: ms-declarative-agents, ms-agent-builder, ms-copilot-studio-guidance, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# Agent instructions

## Purpose

An agent's instructions are its specification: they decide what it answers, how it uses its knowledge, when it declines
and where it sends people. This skill turns the behaviour fixed in the agent brief into clear instructions, keeps them
under version control, and makes sure every change is tested before it reaches users. Instructions usually go wrong in
one of two ways: they are written as clever prompting with vague aspirations ("be helpful and accurate"), or they are
edited live by whoever has access, so behaviour shifts without anyone noticing until users complain.

## When to use

- An agent brief is agreed and the maker is ready to write the instructions.
- A live agent answers outside its scope, ignores its knowledge, or declines things it should answer.
- Someone wants to change a live agent's instructions and the change needs controlling.
- Several agents need consistent tone, citation and refusal behaviour.

## When not to use

- Deciding the agent's purpose, audience, scope and exclusions in the first place - use `m365-agents:agent-use-case-design`.
- Choosing and configuring the knowledge the agent grounds on - use `m365-agents:agent-grounding`.
- Designing Copilot Studio topics and generative orchestration - use `copilot-studio:topics-and-orchestration`.
- Engineering and versioning system prompts for a production Foundry solution - use `ai-foundry:foundry-prompt-engineering`.
- Teaching users to write good prompts - use `m365-copilot:prompting-practice`.

## Questions to ask first

1. What does the brief say about purpose, audience, in-scope questions, exclusions and redirects?
2. How should the agent behave when its knowledge is silent, contradictory or out of date?
3. When must it cite a source, and in what format should answers appear for this audience?
4. Who may change the instructions, and how is a change approved and tested?
5. Which test set exists to check behaviour after each change?

## Required inputs

- The agreed agent brief on the `agent-brief` template, with scope, exclusions and redirects.
- The knowledge configuration from `m365-agents:agent-grounding`.
- The evaluation set from `m365-agents:agent-testing`, or at least the seed questions.
- The organisation's standard wording for AI disclosure, escalation routes and tone, if one exists.

If the brief has no exclusions or redirects, stop and return to `m365-agents:agent-use-case-design`; instructions cannot
safely invent them. Never write a capability into instructions that the build path does not support; check the source
records.

## Decision framework

Instructions should cover each element below, in plain, specific language.

| Element | Good instruction | Weak instruction |
|---|---|---|
| Role and purpose | States the job and the audience in one or two sentences | "You are a helpful assistant" |
| Scope | Lists the kinds of questions in scope | Leaves scope to the model |
| Knowledge use | Says to answer from named knowledge and cite it | "Use your knowledge" |
| Uncertainty | Says what to do when knowledge is silent or conflicting | Silent, so the agent guesses |
| Exclusions and redirects | Names what to decline and where to send people | "Do not answer inappropriate questions" |
| Format and tone | Specifies length, structure and tone for the audience | Unstated |
| Conversation starters | Show real in-scope questions | Generic or out-of-scope examples |

Change control scales with risk tier: from tier 1, every change is logged with a reason and a regression run; from tier
2, the business owner approves changes before publication; from tier 3, the `evaluation-quality` reviewer confirms the
regression evidence.

## Practitioner approach

Write from the brief, not from a blank page. Take the purpose, audience, in-scope questions, exclusions and redirects and
turn each into a short instruction. Use direct, specific language: "Answer only questions about the travel and expenses
policy for employees. If a question is about another policy, say you cannot help with that and point the user to the HR
service portal." Specific instructions are easier to test and harder for the model to misread.

Spend most of the effort on the edges. Tell the agent what to do when its knowledge does not contain the answer: say so
plainly and offer the redirect, rather than filling the gap. Tell it what to do when two sources conflict: prefer the
named authoritative source, or say there is a conflict and redirect. Tell it when to cite and how. These behaviours
decide whether users trust the agent.

Keep instructions short enough to read. Long, repetitive instructions tend to produce inconsistent behaviour, and nobody
can maintain them. If the instructions keep growing to handle special cases, the scope is probably too wide or the
knowledge too poor; return to the brief or to grounding rather than patching with more words.

Write conversation starters from the seed questions in the users' own words. They show users what the agent is for, and
they are the first thing testers will try.

Test before publishing. Run the evaluation set from `m365-agents:agent-testing`, including refusal and out-of-scope
cases, and compare with the expected behaviour. Adjust one thing at a time so you know what made the difference.

Put the instructions under version control. Store each version with its date, author, reason for change and test
result, wherever the organisation keeps agent configuration. Agree who may edit and who approves, in line with the
agent's tier. A one-word change can alter behaviour, so every edit triggers a regression run.

Review the instructions at each scheduled agent review and whenever feedback shows a pattern of wrong or unhelpful
answers. Capability in the build path changes, so check the source records for new instruction options or limits
before redesigning.

## Outputs

- Agent instructions, versioned, with a change log recording date, author, reason, approver and test result.
- Conversation starters drawn from real user questions.
- A short note in the agent brief or `agent-card` recording who may edit and approve instructions.

## Microsoft platform considerations

Agent Builder, declarative agents and Copilot Studio each provide instruction fields with their own capabilities, length
limits and behaviours, described in `ms-agent-builder`, `ms-declarative-agents` and `ms-copilot-studio-guidance`. These
change frequently; check them before writing and do not rely on a limit or behaviour from memory. Where instructions are
part of a packaged solution, keep them under the same source control as the rest of the agent.

## Adoption considerations

Clear conversation starters and honest "I cannot help with that, try here" responses make an agent easy to adopt.
Agents that guess or refuse without a redirect are abandoned quickly.

## Knowledge considerations

Instructions cannot fix poor knowledge. If answers are wrong because sources are wrong, out of date or missing, the fix is
in the knowledge through `m365-agents:knowledge-source-readiness` and `m365-agents:agent-grounding`, not in more
instructions.

## Security and privacy considerations

Instructions are not a security control: they do not stop a user reaching content their permissions allow. Never rely on
an instruction to hide sensitive content; restrict the content instead. Consider prompt injection through knowledge
content and user input, and include tests for it where the tier warrants, with `security-privacy:ai-security-testing`.

## Responsible AI considerations

Instructions must make the agent identify itself as AI where users might not realise, cite sources for factual answers,
and redirect questions that touch decisions about people, money, safety or rights to the appropriate human route.

## Evaluation requirements

Every instruction change is followed by a regression run of the evaluation set, including refusal and out-of-scope
cases, with results recorded in the change log. From tier 3, the `evaluation-quality` reviewer checks the evidence.

## Value measures

Track the share of evaluation cases passed after each change and, in operation, the rate of feedback flagging wrong or
unhelpful answers, at audience level. The agent's business owner owns these measures.

## Scale notes

### Starter

A short set of instructions written from a one-page brief, a simple version history and a handful of tests rerun after
each edit.

### Scale

A shared instruction pattern for tone, citation and refusal across agents, with versioned instructions and regression
runs as standard.

### Enterprise

Instruction standards maintained centrally, instructions held in source control with packaged solutions, and approvals
tied to tier and change policy.

## Hand-offs

- To `m365-agents:agent-testing` for regression after each change.
- To `m365-agents:agent-grounding` when behaviour problems trace back to knowledge configuration.
- To `m365-agents:agent-lifecycle` for change control in operation.
- To `copilot-studio:conversation-design` for Copilot Studio agents that need designed conversations.

## Reviewer gates

From risk tier 3, instruction changes require `evaluation-quality` to confirm regression evidence before publication,
classifying findings as blocking or advisory. A blocking finding stops the change from going live.

## Failure modes

- Instructions are vague aspirations, so the agent guesses when its knowledge is silent.
- Instructions grow with every complaint until they contradict themselves.
- A live edit by someone with access changes behaviour without a test, and nobody can say what changed.
- Instructions are used to hide content that permissions should have restricted.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Publish an instruction change without a regression run and a logged reason.
- Rely on instructions to keep sensitive content from users who can access it.
- Invent scope, exclusions or redirects that the brief did not agree.
- Assert instruction limits or behaviours from memory rather than the current source records.
