---
name: golden-dataset
description: Builds, maintains and reviews the golden dataset an AI solution is judged against - real questions or tasks from users, expected answers and sources confirmed by knowledge owners, edge, refusal and adversarial cases, versioning and safe handling of test data - with findings classed blocking or advisory. Use when evaluation needs a trusted reference set, when expected answers have drifted, or when a test set looks too friendly.
license: CC-BY-4.0
metadata:
  department: evaluation-quality
  lifecycle: Deliver, Assure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-cowork, copilot-studio, ai-foundry, sharepoint
  edition-support: starter, scale, enterprise
  reviewers: evaluation-quality, security-privacy
  sources: nist-ai-rmf, ms-copilot-studio-guidance, ms-foundry-models, ms-copilot-privacy, ico-ai-data-protection
  status: draft
  authors: Simon Foote
---

# Golden dataset

## Purpose

A golden dataset is the set of questions or tasks, with expected answers and expected sources, that an AI solution is
measured against before release and after every change. It is the most reused evaluation asset an organisation owns,
and the one most often built badly. This reviewer skill builds and maintains golden datasets that represent real users,
probe the edges deliberately and stay true to current knowledge, and reviews datasets that teams submit, classifying
each finding as blocking or advisory. Datasets usually fail because the maker writes friendly questions they know the
solution can answer, or because expected answers go stale while the knowledge moves on.

## When to use

- An evaluation plan calls for a reference set and none exists yet.
- A team submits a test set to the `evaluation-quality` gate and it needs judging for coverage and trustworthiness.
- Knowledge has changed and expected answers may no longer be correct.
- Evaluation results look suspiciously good, or users report failures the test set never caught.
- Several similar agents need a shared core dataset with solution-specific additions.

## When not to use

- Deciding which dimensions, methods and cadence evaluation needs overall - use `evaluation-quality:ai-evaluation-strategy`.
- Writing the scoring scale and pass thresholds applied to dataset results - use `evaluation-quality:ai-quality-rubric`.
- Running a single agent's tests and recording results - use `m365-agents:agent-testing`.
- Deliberately adversarial exercises led by a red team - use `evaluation-quality:red-team-plan`.
- Inventorying and fixing the knowledge sources themselves - use `knowledge-management:knowledge-inventory` or `m365-agents:knowledge-source-readiness`.

## Questions to ask first

1. Who will actually use the solution, and where can we collect the questions they ask today, in their own words?
2. Who has the authority to confirm that an expected answer is correct, and will they commit time to it?
3. What must the solution refuse, redirect or say it does not know?
4. Does any candidate item contain personal or confidential data, and who may see the dataset?
5. How often does the underlying knowledge change, and who will update expected answers when it does?

## Required inputs

- The approved evaluation plan with dimensions and risk tier, from `evaluation-quality:ai-evaluation-strategy`.
- The solution's scope, exclusions and behaviour rules from its brief or design.
- Real questions or task examples from users, service desk logs, mailboxes or workshops, collected with permission.
- Knowledge source list with owners, and known contradictions or gaps from knowledge readiness.

Where real user questions are unavailable, mark the dataset as provisional and plan to replace synthetic items with
real ones after the first live weeks. Never present a synthetic-only dataset as representative.

## Decision framework

Build to a coverage matrix, then size by risk tier. Sizes are a CopilotForge starting convention, consistent with
`m365-agents:agent-testing`; validate them against your own evaluation plan.

| Category | What it contains | Tier 1 | Tier 2 | Tier 3 and 4 |
|---|---|---|---|---|
| Core in-scope | Common real questions or tasks with expected answer and source | Most of the set | Most of the set, spread across sub-topics | Plus paraphrased variants of each |
| Edge | Ambiguous, incomplete, multi-part or badly worded requests | A few | Required | Required, with variants |
| Refusal and redirect | Out-of-scope requests and those the brief says to redirect | At least three | Required | Required |
| Knowledge silent | Questions the knowledge does not answer | Optional | Required | Required |
| Contradiction | Questions where sources disagree | Optional | Required where contradictions are known | Required |
| Adversarial | Attempts to override instructions or extract restricted content | Optional | A small set | Full set, refreshed from red teaming |
| Held out | Items builders never see, used only at the gate | Not needed | Optional | Required at tier 4 |
| Overall size | | 15-25 | 30-60 | 60 or more |

When reviewing a submitted dataset, classify each finding.

| Finding | Blocking from tier 2 when | Advisory when |
|---|---|---|
| Provenance | All items written by the maker; no user-sourced items | Some categories lack user items |
| Expected answers | Not confirmed by an authoritative owner, or contradict current knowledge | Confirmation older than the last review cycle |
| Coverage | No refusal, knowledge-silent or edge items | A minor sub-topic is thin |
| Data handling | Contains personal or confidential data beyond testers' entitlement | Storage location broader than necessary for low-sensitivity items |
| Versioning | No version or owner, so results cannot be compared | Change log incomplete |

## Practitioner approach

Collect before you write. Ask the future users, their service desk and their managers for the questions people
actually ask, and harvest them from shared mailboxes or ticket logs where that is permitted. Keep the wording as found,
including typos and half-sentences, because real phrasing is what breaks solutions. Remove or replace personal details
before anything enters the dataset.

Sort the collection into the categories in the coverage matrix and look for holes. Users rarely volunteer the refusal
cases, the contradictions or the questions the knowledge cannot answer, so add those deliberately from the brief and
from knowledge readiness findings. Write variants of the most important core items, because a solution that answers
one phrasing correctly can fail a close paraphrase.

For each item, record the expected answer in substance rather than exact wording, the source and section it should come
from, the category, and any must-include or must-not-include elements. For task-based solutions such as Cowork
workflows or flows, record the expected end state and the checkpoints a person should see. Then send the expected
answers to the knowledge owners for confirmation and record who confirmed each and when. An item without a confirmed
answer is not golden; mark it provisional.

Version the dataset from the first run. Store it with its owner, its version, the knowledge versions it reflects and a
change log, in a location limited to the evaluation team. Results are only comparable across runs that used the same
dataset version, so record the version on every results sheet.

Protect against contamination. If makers tune instructions against every item, the set stops measuring generalisation.
From tier 3, keep a held-out portion that only the evaluators use at the gate, and refresh the adversarial category with
findings from red teaming.

Maintain it as a living asset. When a knowledge owner changes a policy, the dataset owner updates affected expected
answers before the next regression run. When users report a failure the set missed, add an item for it. Retire items
for topics that are out of scope. Review the whole set on the cadence in the evaluation plan, and never let it grow so
large that nobody can run it.

## Outputs

- A versioned golden dataset: items, categories, expected answers, expected sources, confirmation owner and date, and data handling notes, referenced from the `evaluation-plan`.
- A coverage summary showing items per category against the matrix for the tier.
- A dataset review record with findings classified blocking or advisory, the fix and an owner.
- A change log tying dataset versions to knowledge changes.

## Microsoft platform considerations

Some routes, including Copilot Studio and Microsoft Foundry, can import test sets and run evaluations against them;
capabilities and formats change, so confirm them in `ms-copilot-studio-guidance` and `ms-foundry-models` and keep a
route-neutral master copy. Datasets stored in SharePoint or similar locations follow normal permissions; restrict them
so the dataset does not itself become overshared content an agent could ground on.

## Adoption considerations

Inviting users to contribute questions builds ownership and surfaces the language people really use. Thank contributors
as a group and show them how their questions improved the solution.

## Knowledge considerations

The dataset is only as current as the knowledge it reflects. Tie expected-answer reviews to the knowledge owners'
review cycles set through `knowledge-management:knowledge-review-cycles`, and treat a contradiction found while writing
expected answers as a knowledge defect to fix at source.

## Security and privacy considerations

Never place real personal data in items or expected answers beyond what every tester may see; use realistic fictional
details instead. Check the lawful basis with the DPO before reusing real service desk or mailbox content, and keep
datasets out of locations that agents ground on.

## Responsible AI considerations

Include items that test how the solution treats different groups of people, and items inviting speculation about named
individuals, where the solution affects people. Coordinate those items with `responsible-ai:fairness-review` so they
test the harms that matter.

## Evaluation requirements

This skill produces the reference for evaluation. Minimum from tier 2: user-sourced items in every core sub-topic,
refusal, edge and knowledge-silent categories present, every expected answer confirmed and dated, and a version on every
results record.

## Value measures

Track the share of live failures that the dataset would have caught, the age of expected-answer confirmations and the
time to update the set after a knowledge change. The dataset owner reports these by solution; never measure individual
contributors or testers.

## Scale notes

### Starter

A spreadsheet of 15-25 real questions with expected answers confirmed by one knowledge owner, three refusal cases and a
version number in the file name.

### Scale

A standard dataset format across solutions, shared core sets for common domains such as HR or IT policy, and dataset
owners named in the solution register.

### Enterprise

A managed dataset library with versions, owners, held-out sets for tier 3 and 4, and contributions from red teaming and
live feedback flowing in on a defined cadence.

## Hand-offs

- To `m365-agents:agent-testing`, `copilot-studio:studio-testing-and-evaluation` or `ai-engineering:evaluation-harness` to run the dataset.
- To `evaluation-quality:ai-quality-rubric` for scoring.
- To `evaluation-quality:regression-evaluation` for the regression subset.
- Back to `knowledge-management:content-quality` for contradictions and gaps found while writing expected answers.

## Reviewer gates

This skill operates within the `evaluation-quality` gate. From risk tier 2 a dataset with blocking findings cannot be
used as release evidence; below tier 2 findings are advisory. Datasets drawn from real records also need
`security-privacy` agreement on handling. Disagreement escalates to the accountable executive for written risk acceptance.

## Failure modes

- The maker writes every item, so the dataset tests what the maker already knows works.
- Expected answers are never re-confirmed and the solution is marked wrong for giving the current, correct answer.
- Makers tune against every item until results are perfect and live performance is not.
- The dataset grows without pruning until nobody runs it after changes.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Treat an item without an owner-confirmed expected answer as golden.
- Put real personal or confidential data into a dataset beyond what every tester is entitled to see.
- Compare results produced with different dataset versions as if they were like for like.
- Present a synthetic-only dataset as representative of real users.
