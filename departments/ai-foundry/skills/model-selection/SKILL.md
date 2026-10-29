---
name: model-selection
description: Shortlists and selects models from the Microsoft Foundry catalogue, including partner and third-party models, against task fit, data handling, hosting terms, lifecycle, latency and cost, and records the choice and its fallback on a model selection record. Use when a Foundry solution needs a model, when a team asks for a specific third-party model, or when a model is being retired or replaced.
license: CC-BY-4.0
metadata:
  department: ai-foundry
  lifecycle: Mobilise, Deliver, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure
  edition-support: starter, scale, enterprise
  reviewers: design-authority, security-privacy, responsible-ai
  sources: ms-foundry-models, ms-responsible-ai, ico-ai-data-protection
  status: draft
  authors: Simon Foote
---

# Model selection

## Purpose

The Foundry catalogue offers many models from Microsoft, from partners and from the community, and they differ in far
more than benchmark scores: who hosts them, under what terms, where data is processed, how long they will be supported
and what they cost to run. This skill turns a task into a short, justified list of candidate models, selects one with a
named fallback, and records why. Selection goes wrong when teams pick the newest or largest model by default, when a
third-party model is adopted without anyone reading its terms, or when nobody tracks the retirement date until the
deployment stops working.

## When to use

- A Foundry solution has been approved and needs its first model choice.
- A team asks for a specific partner or third-party model and the organisation needs to decide whether it may be used.
- A deployed model is approaching retirement or a newer version is offered, and the replacement needs choosing.
- A solution is too slow or too costly and a smaller or different model might do the task.
- The organisation wants a shortlist of approved models for common tasks.

## When not to use

- Deciding whether Foundry is justified at all - use `ai-foundry:foundry-solution-assessment`.
- Running the comparative tests that prove which candidate performs best - use `ai-foundry:model-evaluation`.
- Choosing deployment type, region and capacity for the chosen model - use `ai-foundry:foundry-deployment-architecture`.
- Estimating and controlling the consumption cost of the chosen model - use `ai-foundry:foundry-cost-management`.
- Choosing between Microsoft platforms rather than models - use `ai-architecture:platform-selection`.

## Questions to ask first

1. What exactly must the model do (classify, extract, summarise, reason over documents, call tools, generate code, handle images or speech), and what does a good output look like?
2. What data will the model see, how sensitive is it, and are there constraints on where it may be processed?
3. What latency, volume and cost envelope must the solution live within?
4. Is the model hosted and sold by Microsoft, or provided by a partner or the community under separate terms, and has anyone with authority read those terms?
5. How long must the solution run before the model can be changed, and who will own the replacement when the model is retired?

## Required inputs

- The approved solution design, normally on the `foundry-solution-design` template, with risk tier and data sensitivity.
- A task definition with example inputs and expected outputs, ideally the seed of the evaluation set.
- Non-functional requirements for latency, throughput and availability, from `ai-architecture:ai-non-functional-requirements` where they exist.
- The organisation's approved model list and any data-processing constraints, if they exist.

Where the task or data constraints are missing, mark them `[To confirm: ...]` on the model selection record and do
not shortlist. A model chosen before the task is defined is chosen by fashion.

## Decision framework

Filter first, then rank. A model that fails a filter is out regardless of quality.

| Filter | Out when |
|---|---|
| Task and modality fit | It cannot accept the inputs or produce the outputs the task needs |
| Data handling | Its hosting or processing location conflicts with the data constraints, or that cannot be confirmed from the source |
| Terms and provenance | Partner or community terms have not been reviewed and accepted by someone with authority |
| Lifecycle | It is already deprecated, or its support window is shorter than the solution needs without a replacement plan |
| Responsible use | Its documented intended uses or limitations exclude the task |

| Ranking criterion | Weight it higher when |
|---|---|
| Task quality on the organisation's own examples | Always the primary criterion; benchmarks are a starting hint only |
| Latency | A person is waiting, or the model sits in a multi-step chain |
| Cost per task | Volume is high or the solution runs in batch |
| Tool calling and structured output reliability | The model drives an agent or feeds a system |
| Operational maturity | The risk tier is 2 or above and the solution must be supported |

Select the smallest model that meets the quality threshold, and always name a fallback from a different family or
size where one passes the filters.

## Practitioner approach

Write the task down before opening the catalogue. One paragraph covering inputs, outputs, quality bar and the volume
and latency envelope is enough, with five to ten real examples. This becomes the seed of the evaluation set and stops
the conversation drifting into which model is best in general, which is not a useful question.

Apply the filters with the people who own them. Security and privacy confirm the data constraints; whoever holds
procurement or legal authority reviews partner and community model terms; the solution owner confirms how long the
solution must run. Record who confirmed each filter. Third-party models available through Microsoft are within scope,
but their terms, hosting and support arrangements can differ from models Microsoft sells directly, so read the current
catalogue entry rather than assuming parity.

Shortlist two to four candidates that pass every filter, deliberately including at least one smaller or cheaper option.
Teams often jump to the most capable model and never discover that a smaller one does the task well enough at a
fraction of the cost and latency. For multi-step solutions, consider different models for different steps: a capable
model for planning and a smaller one for extraction or classification.

Hand the shortlist to `ai-foundry:model-evaluation` to test against the task examples and an agreed threshold. Do not
select on benchmark tables or a demonstration; the organisation's own examples decide. When results return, choose the
smallest model that meets the threshold, and name a fallback that also passed, so a retirement, regional outage or
price change does not leave the solution without options.

Record the decision on the `model-selection-record` template: the task, filters and who confirmed them, candidates,
evaluation evidence, choice, fallback, model version, and the date and trigger for the next review. Retirement dates
and version changes are volatile; note where the current dates are published rather than copying them, and make the
review a calendar entry owned by a named role.

Finally, say what the selection cannot determine. It cannot guarantee behaviour on inputs unlike the examples, and it
cannot fix poor grounding or a vague prompt; those belong to retrieval and prompt engineering.

## Outputs

- A model selection record on the `model-selection-record` template: task, filters, candidates, evidence, choice, fallback, version and review trigger.
- An entry in the organisation's approved model list where one exists.
- A request to `ai-foundry:model-evaluation` for the comparative test.

## Microsoft platform considerations

The Foundry catalogue distinguishes models sold and hosted by Microsoft from models provided by partners and the
community, and the deployment options, terms and support differ between them. Models are versioned and retired on a
published lifecycle, and new versions may be offered automatically or by choice depending on configuration. All of this
is volatile; read the current catalogue entry and lifecycle information in `references/sources.md` before recording a
fact. Licensing and commercial terms route to the Microsoft licensing guide, a licensing partner or procurement.

## Adoption considerations

Not applicable for most selections, because users experience the solution rather than the model. Where a model change
alters tone, length or behaviour noticeably, tell users through the solution's normal release communications.

## Knowledge considerations

Not applicable to the model choice itself, because grounding quality is decided by retrieval and content rather than
the model. Record any knowledge cut-off that matters to the task so the grounding strategy can compensate.

## Security and privacy considerations

Confirm where each candidate processes data and under which terms, with the `security-privacy` department for tier 2
and above. Partner and community models may carry different data-handling commitments from models sold by Microsoft;
the DPO decides whether they are acceptable for personal data.

## Responsible AI considerations

Read each candidate's documented intended uses, limitations and transparency information and record any that touch the
task. A model whose documentation excludes the use is filtered out, whatever its quality.

## Evaluation requirements

Selection depends on a comparative evaluation on the organisation's own examples, with a threshold agreed before
results are seen. Benchmarks published by vendors are a hint for shortlisting and never evidence for selection.

## Value measures

Measure quality against threshold, cost per task and latency for the chosen model against the shortlist, owned by the
solution owner. Track how often model changes are forced by retirement rather than chosen, as a signal of lifecycle
planning.

## Scale notes

### Starter

Keep it simple: one model that meets the threshold, one fallback, and a calendar reminder for retirement. A partner
can run the evaluation, but the organisation owns the record.

### Scale

Maintain an approved model list by task type, with terms already reviewed, so most solutions select from it rather
than starting again. New models join the list through the same filters.

### Enterprise

Run a model governance forum that owns the approved list, terms reviews and lifecycle tracking across all Foundry
solutions, and plans coordinated migrations when a widely used model is retired.

## Hand-offs

- To `ai-foundry:model-evaluation` for the comparative test of the shortlist.
- To `ai-foundry:foundry-deployment-architecture` to deploy the chosen model.
- To `ai-foundry:foundry-cost-management` to budget the chosen model's consumption.
- To `ai-operations:ai-review-calendar` to schedule the lifecycle review.

## Reviewer gates

From risk tier 2, `security-privacy` confirms data-handling and hosting filters, `responsible-ai` confirms the model's
documented limitations do not exclude the use, and `design-authority` checks the choice conforms to the approved model
list or records the exception.

## Failure modes

- The largest model is chosen by default, and the solution is slow and costly for a task a smaller model handled.
- A third-party model is adopted without anyone reviewing its terms, and the organisation later finds it cannot use it for that data.
- The model is retired and nobody noticed the date, so the solution stops or changes behaviour without testing.
- Selection relies on a vendor benchmark, and the model underperforms on the organisation's own documents.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Select a model before the task, data constraints and quality threshold are written down.
- Use a partner or community model whose terms nobody with authority has reviewed.
- Copy model availability, regions, prices or retirement dates into the record from memory; cite the current source.
- Deploy without a named fallback and a lifecycle review date owned by a role.
