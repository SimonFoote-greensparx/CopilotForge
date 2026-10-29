---
name: foundry-prompt-engineering
description: Engineers the system prompts and prompt templates of a Microsoft Foundry model or agent for production - structure, scope and refusal rules, grounding and citation instructions, output contracts, injection resistance - and keeps them versioned, reviewed and regression-tested like code. Use when a Foundry prototype prompt must become production-grade, when outputs drift after a prompt edit, or when prompts change outside source control.
license: CC-BY-4.0
metadata:
  department: ai-foundry
  lifecycle: Deliver, Assure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure, github
  edition-support: starter, scale, enterprise
  reviewers: evaluation-quality, security-privacy
  sources: ms-foundry-models, ms-responsible-ai, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Foundry prompt engineering

## Purpose

In a Foundry solution the system prompt is executable behaviour: it decides scope, tone, refusals, how sources are used
and the shape of every output another system depends on. This skill turns the prompt a developer tuned in a playground
into a production artefact with a clear structure, a defined output contract, an owner, a version history and a
regression run behind every change. Prompt work goes wrong when one long prompt accumulates patches for every reported
problem, when edits are made directly in a live deployment, and when nobody can say which prompt version produced an
answer that is now being questioned.

## When to use

- A Foundry prototype works in the playground and its prompt now needs to be fit for production.
- Outputs changed after someone edited a prompt, and nobody can say which edit caused it or roll it back.
- A downstream system parses model output and breaks when the format varies.
- An agent ignores its scope, over-refuses, or follows instructions found inside documents it reads.
- Prompts live in portal settings, notebooks or configuration files outside source control.
- A model version change is coming and the prompt must be re-tuned and re-tested.

## When not to use

- Writing instructions for a Microsoft 365 declarative agent - use `m365-agents:agent-instructions`.
- Designing topic and orchestration behaviour in Copilot Studio - use `copilot-studio:topics-and-orchestration`.
- Teaching staff to prompt Microsoft Copilot in their daily work - use `m365-copilot:prompting-practice`.
- Deciding the agent's responsibility, tools and identity - use `ai-foundry:foundry-agent-architecture`.
- Building the pipeline that deploys prompts with code - use `ai-engineering:ai-ci-cd`.
- Deciding at the gate what must be re-evaluated after a change - that is the reviewer skill `evaluation-quality:regression-evaluation`.

## Questions to ask first

1. What exactly must the model produce, for whom or for which system, and what does an unacceptable output look like?
2. What is in scope, what must be refused, and where should out-of-scope requests be sent instead?
3. Which content will the model read that the organisation does not control, such as user uploads, emails or web pages?
4. Which model and version is the prompt being written for, and is a model change expected during the solution's life?
5. Where will prompts be stored, who may change them, and what evidence must exist before a change reaches production?

## Required inputs

- The agent architecture or solution design on the `foundry-solution-design` template, including responsibility statement and tool list.
- The model selection record on the `model-selection-record` template, naming the model and version.
- A set of representative inputs with expected outputs, ideally the evaluation set from `ai-foundry:model-evaluation`.
- Any output schema a consuming system requires, agreed with that system's owner.
- The organisation's tone and accessibility standards for user-facing text, if they exist.

Where the expected outputs or the output schema are missing, mark them `[To confirm: ...]` and do not tune. A prompt
tuned without examples is tuned to the last person who complained.

## Decision framework

| Concern | Put it in | Not in |
|---|---|---|
| Role, scope, refusals, tone, citation rules | The system prompt, as short structured sections | Scattered examples or user-turn text |
| Output format a system parses | A structured output schema where the model and platform support it, backed by a format statement in the prompt | Prose descriptions alone |
| Facts that change (prices, policies, dates) | Retrieved knowledge or tool results | The prompt, where they go stale silently |
| Hard rules (never send, never approve) | Code, tool permissions and confirmation steps | The prompt alone, because prompts can be overridden |
| Variable per-request data | A template with named, escaped slots | String concatenation of untrusted text into instructions |

| Change type | Minimum evidence before release |
|---|---|
| Wording or tone, tier 0 or 1 | Regression subset passes |
| Scope, refusal or citation rules | Full evaluation set plus refusal and injection cases |
| Output contract change | Contract tests with every consuming system, versioned schema |
| Model version change | Full evaluation, safety evaluation and comparison with the last baseline |

## Practitioner approach

Start with the output, not the prompt. Agree with the business owner and any consuming system what a correct output
looks like, with examples of good, borderline and unacceptable answers. If a system parses the output, define the
schema first and version it; prompt wording then serves the contract rather than the other way round.

Write the system prompt in short, labelled sections: role and audience, scope and refusals with where to redirect,
how to use sources and cite them, how to behave when sources are silent or contradictory, output format, and tone. Keep
each instruction testable. Remove anything that restates a rule enforced elsewhere unless the model needs it to
explain a refusal. Long prompts built from accumulated patches contradict themselves, and the model resolves the
contradictions unpredictably.

Separate instructions from data. Untrusted content, whether retrieved passages, user uploads or tool results, goes into
clearly delimited slots and the prompt tells the model that such content is information, not instruction. This reduces
but never removes the risk of indirect prompt injection, so anything consequential must also be controlled by tool
permissions and confirmation steps designed with `ai-foundry:foundry-tool-design`.

Tune against the evaluation set, not against anecdotes. Change one thing at a time, run the regression subset, and keep
a short note of why each change was made. When a reported failure appears, add it to the set before fixing it, so the
fix is proven and stays proven. Watch for over-refusal as closely as for unsafe answers; a prompt that refuses too much
pushes users back to unapproved tools.

Treat prompts as code. Store them in the solution repository with the code that calls them, review changes through pull
requests, tag versions, and record the prompt version in every trace so an answer can be traced to the exact prompt
that produced it. Production deployments read the prompt from the released artefact, never from an editable portal
field. Repository layout belongs to `ai-engineering:ai-solution-repository` and deployment to `ai-engineering:ai-ci-cd`.

Re-tune when the model changes. A prompt is tuned to one model's habits, and a new version or a different model can
respond differently to the same wording. Plan the re-tune and full evaluation into every model change.

Say what prompt engineering cannot do. It cannot make up for missing knowledge, a model that lacks the capability, or a
tool that is too powerful. When tuning stalls, the fix is usually in retrieval, model choice or tool design.

## Outputs

- A versioned system prompt and any prompt templates, stored with the solution code, each with an owner and change note.
- The prompt and output contract section of the `foundry-solution-design` template: structure, output schema and version, untrusted-content handling and change evidence rules.
- Additions to the evaluation set for every defect fixed, handed to `ai-foundry:model-evaluation`.
- A change log linking prompt versions to evaluation results, used as evidence on the `evaluation-plan` template.

## Microsoft platform considerations

Microsoft Foundry offers playgrounds, prompt tooling, structured output options on some models and evaluation features,
and these change frequently and differ by model. Check the current source records for which models support structured
outputs, how system messages are handled by each model family, and which prompt management features are generally
available rather than in preview. Third-party models in the catalogue may follow different prompt conventions, so
confirm each model's documentation rather than reusing a prompt written for another family.

## Adoption considerations

Users notice prompt changes as changes in tone, length or willingness to help. Tell users through the solution's normal
release notes when behaviour changes materially, and give them a way to report answers that feel wrong.

## Knowledge considerations

Not applicable to the facts themselves, because changing facts belong in retrieved knowledge rather than the prompt.
The prompt does set how sources are cited and what happens when knowledge is silent, which the knowledge owner should
agree.

## Security and privacy considerations

Never put secrets, keys, internal hostnames or personal data in a prompt; assume the prompt can be extracted. Delimit
untrusted content, log the prompt version rather than full prompt text where content is sensitive, and include
injection and instruction-extraction cases in testing reviewed by `security-privacy:ai-security-testing`.

## Responsible AI considerations

The prompt is where disclosure, refusal of harmful or out-of-scope requests and the route to a person are usually
expressed. Agree these with the business owner and `responsible-ai:ai-transparency`, and do not rely on the prompt alone
for anything that must never happen.

## Evaluation requirements

Every prompt change runs at least the regression subset; scope, refusal and contract changes run the full set,
including over-refusal, injection and format cases. Thresholds are agreed before results are seen, and the prompt
version is recorded with each result.

## Value measures

Track the defect rate per prompt release, regressions caught before production, and time from reported failure to
proven fix, owned by the solution owner. Rising patch frequency on one prompt signals a design problem elsewhere.

## Scale notes

### Starter

Keep one prompt per solution in source control with a simple change note and a small regression set. A partner may
write it, but an internal owner approves every change.

### Scale

Share a prompt style guide and reusable sections for disclosure, citation and refusal across solutions, and run
regression automatically on every prompt change.

### Enterprise

Treat prompts as governed configuration items with owners, versions and release evidence, and coordinate re-tuning
across solutions when a widely used model changes.

## Hand-offs

- To `ai-foundry:model-evaluation` for full evaluation of a prompt release.
- To `ai-foundry:foundry-safety-evaluation` for safety testing of scope and refusal changes.
- To `ai-engineering:ai-ci-cd` to deploy prompts with the code that uses them.
- To `ai-engineering:ai-telemetry` so prompt versions appear in traces.
- To `ai-foundry:retrieval-design` when failures come from missing or poor context rather than wording.

## Reviewer gates

From risk tier 2, `evaluation-quality` checks that prompt releases carry regression evidence against thresholds set in
advance, and `security-privacy` reviews untrusted-content handling and injection testing. A prompt edited directly in
production is a finding at any tier.

## Failure modes

- Patches pile up in one prompt until instructions contradict each other, and behaviour becomes erratic after every fix.
- A prompt is edited in the portal to fix one complaint, and a downstream system breaks because the output format changed.
- Instructions hidden in a retrieved document override the system prompt, because untrusted content was pasted into the instructions.
- The model version changes and the prompt is not re-tested, so tone, refusals and format shift without anyone noticing.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Edit a production prompt outside source control and the release process.
- Rely on prompt wording alone to prevent a consequential or irreversible action.
- Put secrets, credentials or personal data in a prompt.
- Ship a prompt change without running at least the regression subset against agreed thresholds.
