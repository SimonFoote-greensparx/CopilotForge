---
name: ai-solution-testing
description: Sets the testing strategy for pro-code AI solutions - unit tests around non-model code, contract tests for tools, recorded or stubbed model responses, integration, adversarial and failure-path tests - and how each layer fits alongside evaluation. Use when planning tests for a Foundry or Azure AI solution, when tests are flaky because they call live models, or when testing stops at a few manual prompts.
license: CC-BY-4.0
metadata:
  department: ai-engineering
  lifecycle: Deliver, Assure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure, github, copilot-code
  edition-support: starter, scale, enterprise
  reviewers: evaluation-quality, security-privacy
  sources: ms-foundry-models, ms-responsible-ai, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# AI solution testing

## Purpose

Custom AI solutions mix deterministic code (parsing, routing, tool implementations, authorisation) with probabilistic
model behaviour. Teams tend to test one and forget the other: either unit tests that never touch the model, or a few
manual prompts that never exercise the code paths around it. This skill sets a layered testing strategy so that each
part is tested by the method that suits it, tests are fast and stable where they can be, and the probabilistic parts
are covered by evaluation rather than by brittle exact-match assertions. It goes wrong when tests call live models for
everything and become slow and flaky, and when failure paths are never tested at all.

## When to use

- A team is planning tests for a pro-code AI solution on Microsoft Foundry or Azure.
- Tests call live models, are slow, cost money and fail intermittently.
- Testing consists of trying a few prompts by hand before release.
- Failure paths (timeouts, filtered content, tool errors, malformed model output) have never been exercised.
- A solution is moving to a higher risk tier and testing needs to be strengthened.

## When not to use

- Building the automated quality evaluation of model outputs - use `ai-engineering:evaluation-harness`.
- Validating an AI-built application against its requirements - use `copilot-code:application-validation`.
- Security testing including prompt injection as a reviewer activity - use `security-privacy:ai-security-testing`.
- Setting evaluation strategy and acceptance thresholds - use `evaluation-quality:ai-evaluation-strategy`.
- Performance and load testing in depth - use `ai-engineering:ai-performance-engineering`.

## Questions to ask first

1. Which parts of the solution are deterministic code, and which depend on model output?
2. What does the solution do with model output (parse it, route on it, call tools, show it to users), and what breaks if it is malformed?
3. Which external dependencies (models, indexes, tools, business systems) can be stubbed, and which must be tested for real?
4. What failure behaviours are specified, and have any been tested?
5. How long can the test suite take on a pull request, and what is the budget for live model calls?

## Required inputs

- The solution architecture and the code repository.
- Specified behaviour for failures and edge cases, from the design or non-functional requirements.
- Tool and API contracts from `ai-engineering:ai-api-and-tooling`.
- The evaluation strategy, so testing and evaluation do not duplicate or leave gaps.

If failure behaviour is not specified, write the tests that reveal current behaviour, record it and ask the solution
owner to confirm it is acceptable. Never assume a failure path works because the happy path does.

## Decision framework

Each layer tests something different. Use the cheapest layer that can catch the defect.

| Layer | Tests | Model calls | Runs |
|---|---|---|---|
| Unit | Parsing, validation, routing logic, prompt assembly, authorisation checks, tool implementations | None; model responses stubbed | Every commit |
| Contract | Tool and API specifications, model output schemas, interfaces between components | None | Every commit |
| Recorded interaction | Orchestration behaviour on recorded real model responses, including awkward ones | Replayed | Every pull request |
| Failure path | Timeouts, throttling, content filter blocks, refusals, malformed output, tool errors | Stubbed or injected | Every pull request |
| Integration | End-to-end through real deployments in a test environment | Live | Before promotion |
| Adversarial | Prompt injection through inputs, documents and tool results; attempts to reach other users' data | Live | Before promotion and after material change |
| Evaluation | Quality against the golden dataset and thresholds | Live | Per the evaluation harness |
| Performance | Latency and throughput under load | Live | Before production for tier 3 and above |

Exact-match assertions on free-text model output belong nowhere except deliberate snapshot tests of prompts.

## Practitioner approach

Separate what is deterministic from what is not. Draw the request path and mark each step. Prompt assembly, input
validation, parsing of model output, routing decisions, tool implementations and authorisation are code, and deserve
ordinary, thorough unit tests with model responses stubbed. Most defects in AI solutions are here, not in the model.

Test prompt assembly as code. Check that the right instructions, context and retrieved content end up in the prompt,
that user input is clearly separated from instructions, that token budgets are respected and that nothing sensitive is
included that should not be. Snapshot tests of assembled prompts catch accidental changes.

Treat model output as untrusted input to the rest of the system. Write tests that feed malformed, partial, overlong,
empty and unexpected outputs into the parsing and routing code, and assert that the solution handles each safely. Record
real model responses, including odd ones found in development, and replay them so orchestration tests are fast and
deterministic.

Test the failure paths deliberately. Inject timeouts, throttling responses, content filter blocks, refusals, tool errors
and unavailable indexes, and check that the behaviour matches `ai-engineering:ai-resilience` and the design. These are
the paths users meet on bad days, and they are usually untested.

Run integration tests against real deployments in a test environment before promotion, with representative data and
identities. Include permission tests: the same request as users with different access must return different results.
Keep these few and focused on wiring, leaving quality judgements to the evaluation harness.

Test adversarially. Put injection attempts in user input, in documents the solution retrieves and in tool results. Check
that the solution does not follow injected instructions, reveal its system prompt where that matters, call tools it
should not or return other users' data. Share the results with `security-privacy:ai-security-testing`.

Keep the suite healthy. Unit, contract, recorded and failure-path tests should run in minutes without live calls. Quarantine
and fix flaky tests promptly. Add a test for every production defect, at the cheapest layer that would have caught it.

## Outputs

- A test strategy for the solution: layers, what each covers, triggers, environments and budgets.
- Unit, contract, recorded interaction and failure-path test suites in the repository.
- Integration and adversarial test suites run before promotion, with results stored as release evidence.
- A defect-to-test log showing each production defect and the test added.

## Microsoft platform considerations

Microsoft Foundry and Azure services can be called from test code through SDKs, and test environments can mirror
production deployments; content filtering behaviour, error responses and throttling signals vary by service and change.
Check current behaviour in `references/sources.md` when building stubs, and refresh recorded responses when models or
services change.

## Adoption considerations

Engineers new to AI often believe model-based code cannot be tested. Show them how much of the solution is ordinary code,
provide stubbing and recording helpers in the template repository, and make the fast suite the default local check.

## Knowledge considerations

Integration tests that depend on retrieval need a stable test corpus. Version a small, representative set of documents
for the test environment, including documents with restricted access for permission tests.

## Security and privacy considerations

Adversarial and permission tests are core, not optional, from tier 2. Recorded model responses and test data must not
contain real personal data unless the test environment has production-equivalent protection.

## Responsible AI considerations

Include test cases for refusals, escalation to a person and behaviour when the solution is unsure, and check that failure
messages to users are honest and helpful. Quality and fairness across user groups are measured in evaluation, not here.

## Evaluation requirements

Testing and evaluation complement each other: tests prove the code behaves correctly around the model; evaluation proves
the outputs are good enough. Both are release evidence. Avoid duplicating quality judgements in tests.

## Value measures

Track defects caught per layer, production defects that a test should have caught, suite run time and flaky test rate.
The AI engineering lead owns these at team level.

## Scale notes

### Starter

Unit tests with stubbed model responses, a handful of failure-path tests and a short integration check before release.
Add an injection test for every input route.

### Scale

All layers in place, recorded interaction libraries shared across solutions, adversarial tests in the pre-promotion
pipeline and a defect-to-test practice.

### Enterprise

Shared test tooling, injection and permission test packs maintained centrally, and test coverage by layer reported to the
design authority across the estate.

## Hand-offs

- To `ai-engineering:evaluation-harness` for quality evaluation of outputs.
- To `security-privacy:ai-security-testing` with adversarial test results.
- To `ai-engineering:ai-ci-cd` to wire test layers into pipeline stages.
- To `ai-engineering:ai-resilience` where failure-path tests reveal missing behaviour.

## Reviewer gates

From risk tier 2, `evaluation-quality` checks that tests and evaluation together cover the solution, and
`security-privacy` checks adversarial and permission tests. Missing permission tests for user-scoped data are a blocking
finding.

## Failure modes

- Every test calls a live model, the suite is slow and flaky, and engineers stop running it.
- Exact-match assertions on model text break on every model update and are deleted rather than fixed.
- Malformed model output is never tested, and a parsing failure takes the solution down in production.
- Injection through retrieved documents is never tested, and a planted instruction makes the solution call a tool.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Rely on a few manual prompts as the test strategy for a solution at tier 1 or above.
- Assert exact free-text model output as a pass condition.
- Release without testing failure paths for model, retrieval and tool errors.
- Use real personal data in test fixtures without production-equivalent protection.
