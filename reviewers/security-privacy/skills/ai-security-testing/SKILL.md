---
name: ai-security-testing
description: Reviews the security test plan and evidence for an AI solution - direct and indirect prompt injection, jailbreaks, instruction leakage, exfiltration through outputs and links, tool misuse and privilege escalation - and classifies each finding as blocking or advisory with a fix. Use when an agent with actions reaches its security gate, when it reads untrusted content, or when someone asks whether it can be talked into misbehaving.
license: CC-BY-4.0
metadata:
  department: security-privacy
  lifecycle: Deliver, Assure, Launch, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 2, 3, 4
  platforms: m365-agents, copilot-studio, ai-foundry, power-platform, azure
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, evaluation-quality
  sources: ms-copilot-studio-security-governance, ms-agents-extensibility, ms-foundry-models, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# AI security testing

## Purpose

Language models follow instructions, and they cannot reliably tell the organisation's instructions from instructions
hidden in an email, a web page or a document they were asked to read. That makes AI solutions attackable in ways
ordinary applications are not: through prompt injection, jailbreaks and the misuse of whatever tools the solution can
call. This reviewer skill sets out what security testing a solution needs for its risk tier, reviews the evidence, and
classifies each finding as blocking or advisory with a fix. Testing goes wrong when it stops at "the agent refused a
rude question", or when instructions in the system prompt are treated as the control rather than as something an
attacker will try to override.

## When to use

- An agent or AI solution with knowledge, actions or tools reaches its `security-privacy` gate at tier 2 or above.
- The solution reads untrusted content - inbound email, uploaded files, external websites, customer messages, third-party data.
- The solution can write, send, delete or call external services.
- A new tool, MCP server, action or knowledge source is added to a live solution.
- Someone shows that an agent can be talked out of its instructions.

## When not to use

- Testing for harmful, offensive or unsafe content in outputs - use `evaluation-quality:ai-safety-testing`.
- Planning a broad red-team exercise across harms, misuse and security - use `evaluation-quality:red-team-plan`.
- Security review of code the AI coding agent produced - use `copilot-code:generated-code-security-review`.
- Reviewing connector authentication and data policies - use `security-privacy:connector-review`.
- Functional testing of answers and permission trimming - use `m365-agents:agent-testing`.

## Questions to ask first

1. What untrusted content can reach the model - user input, documents, mail, web pages, tool results, other agents?
2. What can the solution do if it is manipulated - which tools, actions and data, under whose identity?
3. What would an attacker want - data from other users, the system prompt, an unauthorised action, a message sent externally, reputational damage?
4. Which mitigations exist outside the prompt - permissions, confirmation steps, content filters, output restrictions, tool allow-lists?
5. Who will run the tests, with what test identities, and where - never against production data or real customers?

## Required inputs

- The solution design with risk tier, identity map, knowledge sources, tools, actions and channels.
- Connector and identity findings from `security-privacy:connector-review` and `security-privacy:ai-identity-and-access-review`.
- A test environment and test identities that mirror production permissions without production data.
- Any existing test results from `m365-agents:agent-testing`, `copilot-studio:studio-testing-and-evaluation` or `ai-engineering:ai-solution-testing`.

Missing test evidence at tier 2 or above is a blocking finding for any solution with actions or untrusted input. Never
substitute a statement that the model provider handles prompt injection for the organisation's own tests.

## Decision framework

Scale the testing to the attack surface, then classify findings. From risk tier 2 a blocking finding stops release and
is not traded against dates.

| Attack surface | Minimum testing |
|---|---|
| Read-only, curated internal knowledge, internal users | Direct injection and instruction leakage attempts; permission trimming confirmed |
| Reads untrusted content (mail, uploads, web, customer messages) | Add indirect injection planted in that content, and exfiltration through links, images and summaries |
| Takes actions or calls tools | Add tool misuse, parameter tampering, action without confirmation and privilege escalation through chained steps |
| External audience or autonomous operation | Add sustained adversarial testing by people outside the build team, and abuse of cost and rate |

| Finding | Blocking when | Advisory when | Typical fix |
|---|---|---|---|
| Injection leads to action | Planted or typed instructions cause a write, send or external call | Injection changes tone or wording only | Require confirmation, restrict tools, separate reading from acting |
| Data exfiltration | Content from another user, source or system leaves through output, link or action | Model reveals non-sensitive configuration detail | Restrict output channels and link rendering; fix permissions at source |
| Instruction leakage | System prompt contains secrets, keys or sensitive logic | Prompt is revealed but holds nothing sensitive | Remove secrets from prompts; accept prompts may be seen |
| Tool misuse | Tool parameters can be steered beyond intended scope | Scope is enforced but error handling is noisy | Validate parameters server-side; least privilege on the tool |
| Missing evidence | No adversarial tests for a solution with actions or untrusted input | Tests exist but coverage gaps are minor | Run the minimum tests before review continues |

## Practitioner approach

Begin with a threat sketch, not a test list. On one page, draw what flows into the model, what the model can do, and
whose identity it does it with. Mark every point where content the organisation does not control enters: a user's
message, an inbound email being summarised, a document uploaded by a customer, a web page, the output of a tool or
another agent. Those entry points decide what to test.

Assume instructions will be overridden. The question is not whether an attacker can get the model to ignore its system
prompt, because sometimes they will, but what happens next. A manipulated agent that can only read curated content the
user could already open is a nuisance. One that can send email, update records or call an external API is an incident.
Most serious findings are therefore fixed outside the model: by removing a tool, requiring a person to confirm an
action, narrowing an identity, or stopping the solution from rendering links and images that can carry data out.

Test direct injection first, then indirect. For indirect injection, plant instructions in the content the solution
reads, such as hidden text in a document, a line in an email or a field in a record, and see whether the solution acts
on them. For solutions with tools, try to steer parameters, chain actions to reach something the user could not do
directly, and trigger actions without confirmation. Try to extract the system prompt and check whether it contains
anything that would matter if seen; secrets never belong there.

Use test identities with realistic permissions in a non-production environment, and keep a record of every prompt and
result so findings can be reproduced and fixes re-tested. Where Microsoft provides built-in protections, such as content
filtering or prompt shields, record which were enabled and test around them rather than assuming coverage; their scope
changes, so confirm it in the source records.

Write findings in plain terms: what was attempted, what happened, why it matters, and the fix. Re-test every blocking
fix. Security testing is never finished, so agree with the owner which tests become regression tests, run after every
change to instructions, knowledge, tools or model.

## Outputs

- A security test plan scaled to the attack surface, with entry points, scenarios, identities and environment.
- Test evidence: prompts, planted content, results and reproducibility notes.
- The security testing findings in the `ai-risk-assessment`, each classified blocking or advisory with fix, owner and re-test result, and the verdict.
- A short list of security regression tests handed to the solution owner.

## Microsoft platform considerations

Copilot Studio, agents built for Microsoft 365 Copilot and Foundry solutions offer different protections against
injection and harmful content, and these are configured differently on each route. Content filters, prompt shields,
tool approval settings and evaluation tooling change often; confirm current capability in
`ms-copilot-studio-security-governance`, `ms-agents-extensibility` and `ms-foundry-models` before relying on them.

## Adoption considerations

Not applicable as a primary concern, because users rarely see security testing. Where a fix adds a confirmation step,
explain to the business owner why it protects users rather than slowing them down.

## Knowledge considerations

Knowledge sources that anyone can edit are an injection route. Note editable or externally sourced knowledge in the
threat sketch and ask the knowledge owner to restrict who can publish into it.

## Security and privacy considerations

This skill is the security testing review. Findings that reveal overshared content go to
`security-privacy:data-exposure-review`; findings about connector or identity design go to
`security-privacy:connector-review` and `security-privacy:ai-identity-and-access-review`.

## Responsible AI considerations

A manipulated solution can mislead or harm the people it serves. Where testing shows outputs can be steered to give
unsafe or deceptive advice, involve `evaluation-quality:ai-safety-testing` and the `responsible-ai` reviewers.

## Evaluation requirements

Every blocking finding needs a reproducible test and a passing re-test after the fix. Security regression tests are
run after each change to instructions, knowledge, tools or model, and results are kept with the release evidence.

## Value measures

Track at portfolio level the share of tier 2+ solutions with security test evidence, blocking findings found before
versus after release, and time to fix. The security and privacy lead owns these, with a baseline from the first cycle.

## Scale notes

### Starter

Use a short standard set of injection and leakage prompts for every agent with untrusted input or actions, run by
someone other than the maker. Keep first agents read-only to keep the surface small.

### Scale

Maintain a shared library of attack prompts and planted-content files, and make security regression tests part of the
release route for every change.

### Enterprise

Add independent adversarial testing for tier 3 and 4 solutions, coordinate with `evaluation-quality:red-team-plan`, and
feed new attack patterns from incidents back into the shared library.

## Hand-offs

- To the solution's build team with each finding and fix.
- To `evaluation-quality:red-team-plan` for broader adversarial exercises at tier 3 and 4.
- To `security-privacy:ai-incident-readiness` with the attack patterns responders should recognise.
- To `m365-agents:agent-release-readiness` with the verdict.

## Reviewer gates

This skill is the `security-privacy` gate for AI security testing, blocking from risk tier 2 for any solution with
actions or untrusted input. `evaluation-quality` relies on its evidence for the release pack. Disagreement escalates to
the accountable executive for written risk acceptance.

## Failure modes

- Testing covers only typed attacks and misses instructions planted in documents or email the agent summarises.
- The system prompt is treated as the control, so a successful jailbreak becomes an unauthorised action.
- Tests run once before launch and never again, while tools and knowledge keep changing.
- Testing uses an administrator's identity, so permission and escalation findings are invisible.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Accept system prompt instructions as a security control.
- Run adversarial tests against production data, real customers or live external systems.
- Pass a tier 2 or higher solution with actions or untrusted input without adversarial test evidence.
- Keep secrets, keys or credentials in prompts or instructions.
