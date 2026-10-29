---
name: application-validation
description: Validates an application built with Copilot Code against its solution brief, tracing every acceptance criterion to reviewed tests, negative and edge cases, non-functional checks and business owner acceptance, and records a pass, conditional pass or fail. Use when an AI-built application is feature-complete, when a business owner must accept a build, or when generated tests look thorough but nobody has checked them against requirements.
license: CC-BY-4.0
metadata:
  department: copilot-code
  lifecycle: Assure, Launch
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: copilot-code, github, azure
  edition-support: starter, scale, enterprise
  reviewers: evaluation-quality
  sources: nist-ai-rmf, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# Application validation

## Purpose

When a coding agent writes both the code and the tests, a green test run proves only that the code does what the tests
say, and the tests may say the wrong thing. This skill validates an AI-built application against what was actually
required: it traces every acceptance criterion in the solution brief to independent evidence, adds negative, edge and
non-functional checks, and closes with acceptance by the business owner using real scenarios. It goes wrong when
validation is a demonstration of the happy path, or when the generated test suite is accepted as proof without anyone
reading it.

## When to use

- An AI-built application is feature-complete and needs acceptance before deployment.
- The business owner must formally accept a build.
- The generated test suite looks comprehensive but has never been checked against the brief.
- A significant change has been made to a live AI-built application.

## When not to use

- Reviewing individual code changes as they are made - use `copilot-code:generated-code-review`.
- Security review of the generated code - use `copilot-code:generated-code-security-review`.
- Checking operational readiness to deploy - use `copilot-code:code-deployment-readiness`.
- Testing the AI features inside a pro-code AI solution (model quality, groundedness) - use `ai-engineering:ai-solution-testing`.
- Validating a Copilot Cowork workflow - use `copilot-cowork:workflow-validation`.

## Questions to ask first

1. Does every acceptance criterion in the brief have at least one test or check, and has someone other than the agent confirmed the test asserts the right thing?
2. Which negative and edge cases matter most: wrong user, missing data, bad input, lost connection, duplicate submission?
3. Which non-functional requirements apply (accessibility, performance, availability, retention, logging), and how will each be shown?
4. Who will carry out user acceptance, with which real scenarios, and what threshold will the business owner accept?
5. What has changed since the brief, and was each change agreed?

## Required inputs

- The agreed solution brief with acceptance criteria and non-functional requirements.
- The work items and their acceptance tests from `copilot-code:requirements-to-build`.
- A test environment with synthetic or approved test data, isolated from production.
- A business owner and a few representative users available for acceptance.

If acceptance criteria are missing or were changed without agreement, return to the brief before validating. Never
validate with real personal data outside an approved environment.

## Decision framework

Build a traceability matrix and judge each criterion.

| Evidence type | Required for | Notes |
|---|---|---|
| Automated test, reviewed by a person against the criterion | Every functional criterion | Read the assertion, not just the test name |
| Negative test | Every access rule and every "must not" criterion | For example a user cannot see another site's records |
| Edge case test | Inputs, failures and concurrency relevant to the brief | Missing data, invalid input, retries, duplicates |
| Non-functional check | Each stated non-functional requirement | Accessibility check, performance under expected load, logging content |
| User acceptance | The outcome as a whole | Representative users run real scenarios with test data |

| Verdict | Criteria |
|---|---|
| Pass | Every criterion has reviewed evidence; negative and edge cases pass; non-functional requirements met; business owner accepts |
| Conditional pass | Minor gaps with a named fix and date, none affecting access, data integrity or safety |
| Fail | Any access, data integrity or safety criterion unproven or failing, or business owner does not accept |

## Practitioner approach

Start with the brief, not the test suite. List every acceptance criterion and non-functional requirement, then find the
evidence for each. This order matters: starting from the tests shows what was built, starting from the brief shows what
was required, and the gaps between them are the point of validation.

Read the tests. For each criterion, open the test that claims to cover it and check that the assertion actually expresses
the requirement. AI-generated tests commonly assert what the code does, test only the happy path, mock away the part that
matters, or assert something trivially true. A reviewer who reads assertions will find more problems in an hour than a
coverage report will in a week.

Add the negative and edge cases the agent did not think of. Access rules need negative tests from the point of view of
each role. Data entry needs invalid, missing and boundary inputs. Integrations need failure cases: the other system is
slow, returns an error or returns something unexpected. Offline or retry behaviour needs duplicate and partial-submission
cases. These are where AI-built software most often breaks.

Check non-functional requirements explicitly. Run an accessibility check, a basic performance test at expected load, and
inspect logs for personal data and useful diagnostics. Confirm data retention behaves as specified. These are rarely
covered by generated tests unless the work items demanded them.

Run user acceptance with real scenarios. Ask two to five representative users to complete the journeys in the brief with
test data, without coaching. Watch where they hesitate, where the software surprises them, and whether the outcome in the
brief is achieved. The business owner then decides whether to accept, using the evidence rather than a demonstration.

Record the matrix, the verdict and any conditions. Keep the reviewed tests as a regression suite so the same evidence can be
regenerated after changes. When the agent makes later changes, re-run the suite and re-check the assertions of any tests it
modified, because a changed test can quietly redefine "correct".

## Outputs

- A traceability matrix from each acceptance criterion and non-functional requirement to reviewed evidence.
- A validation verdict (pass, conditional pass, fail) with conditions, owners and dates.
- A user acceptance record signed by the business owner.
- A reviewed regression suite for future changes.

## Microsoft platform considerations

Test environments, pipelines and test tooling sit on the organisation's development and hosting platforms (for example
Azure and the repository's pipeline service). Confirm current platform capabilities and limits from the relevant source
records. Validation environments must be isolated from production and use synthetic or approved data.

## Adoption considerations

User acceptance is the first adoption moment. Users who test the software and see their feedback acted on become its
advocates; record their feedback and tell them what changed.

## Knowledge considerations

Not applicable as a primary concern, because validation tests software behaviour; where the application surfaces reference
content, confirm the content source named in the brief is the one used.

## Security and privacy considerations

Negative access tests are part of validation, but they do not replace `copilot-code:generated-code-security-review`. Check
logs and error messages for leaked personal data or internal details. Use only synthetic or approved test data.

## Responsible AI considerations

Where the application supports decisions about people, validate that the human decision step exists, is clear and cannot be
bypassed, and that users can tell what is automated. Route material concerns to the `responsible-ai` department.

## Evaluation requirements

This skill is the evaluation for AI-built applications. From risk tier 2, align the evidence standard with
`evaluation-quality:ai-release-evidence` so validation results form part of the release evidence pack.

## Value measures

Track at team level defects found in validation versus after release, and the share of criteria with reviewed evidence.
Use the brief's outcome measure as the baseline for post-release value. Never use validation findings to judge individual
engineers.

## Scale notes

### Starter

A simple matrix in a spreadsheet, reading the key tests, a handful of negative cases, and acceptance by the business owner
with two or three users.

### Scale

Use a standard traceability template, require reviewed negative tests for every access rule, and keep regression suites in
the pipeline.

### Enterprise

Integrate validation evidence into the release evidence pack, with independent validation for builds at risk tier 3 and
above.

## Hand-offs

- To `copilot-code:code-deployment-readiness` with the verdict and regression suite.
- Back to `copilot-code:requirements-to-build` with gaps needing new work items.
- To `evaluation-quality:ai-release-evidence` from risk tier 2.

## Reviewer gates

From risk tier 2, `evaluation-quality` reviews the traceability matrix and evidence quality before release. Findings are
blocking or advisory; an unproven access, data integrity or safety criterion is blocking.

## Failure modes

- The generated test suite is accepted as proof without anyone reading the assertions.
- Validation demonstrates the happy path, and the first missing-data case fails in production.
- Non-functional requirements are assumed rather than checked, so logs fill with personal data.
- A later change by the agent modifies a test, quietly redefining what counts as correct.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Accept generated tests as evidence without a person checking them against the requirement.
- Pass an application with unproven access or data integrity criteria.
- Validate with real personal data outside an approved environment.
- Replace business owner acceptance with a demonstration.
