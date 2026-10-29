---
name: foundry-production-readiness
description: Assembles and tests the evidence that a custom Microsoft Foundry solution is ready for live use - evaluation and safety results, security and identity, deployment and capacity, observability, cost controls, resilience, support, model lifecycle and rollback - and records a go, go with conditions or no-go. Use when a Foundry build is nearing release, when a pilot is about to widen, or when a partner hands over a solution.
license: CC-BY-4.0
metadata:
  department: ai-foundry
  lifecycle: Assure, Launch
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure, entra
  edition-support: starter, scale, enterprise
  reviewers: design-authority, security-privacy, responsible-ai, evaluation-quality
  sources: ms-foundry-models, ms-responsible-ai, nist-ai-rmf, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# Foundry production readiness

## Purpose

A Foundry solution that works in a demonstration is not yet a service the organisation can rely on. This skill brings
together, in one place, the evidence that the solution is good enough, safe enough, secure, affordable, observable,
supportable and reversible, and turns it into a release recommendation the accountable owner can sign. It does not
redo the specialist work; it checks that each piece exists, is current for the version being released, and has been
accepted by the right people. Readiness goes wrong when it becomes a meeting rather than evidence, when the evaluation
results relate to an earlier prompt or model version, and when nobody has rehearsed turning the solution off.

## When to use

- A Foundry build is nearing its first production release.
- A pilot is about to widen its audience, add a surface or gain a write action.
- A partner is handing over a solution and the organisation must decide whether to accept it into service.
- A significant change, such as a new model, prompt or tool, needs a proportionate readiness check before release.

## When not to use

- Deciding whether the solution should be built at all - use `ai-foundry:foundry-solution-assessment`.
- Assembling the formal evaluation evidence pack as a reviewer gate - that is the reviewer skill `evaluation-quality:ai-release-evidence`.
- Release readiness for a Microsoft 365 agent - use `m365-agents:agent-release-readiness`.
- Deployment readiness for an application built with Copilot Code - use `copilot-code:code-deployment-readiness`.
- Setting the organisation's release policy by risk tier - use `platform-governance:ai-release-policy`.
- Judging the impact of a change to a live solution - that is the reviewer skill `design-authority:ai-change-impact-review`.

## Questions to ask first

1. Exactly which version is being released: model and version, prompt and instruction versions, tools, grounding sources and configuration?
2. What is the confirmed risk tier, and which reviewer gates does the release policy require for it?
3. Who is the accountable owner who will sign the release, and who supports the solution from the first day?
4. What happens if the solution must be switched off or rolled back in the first week, and has that been tried?
5. Which conditions, if any, would the owner accept as open at release, and who closes them by when?

## Required inputs

- The solution design on the `foundry-solution-design` template, with every section completed for this version.
- Evaluation and safety results from `ai-foundry:model-evaluation` and `ai-foundry:foundry-safety-evaluation`, run on the release version.
- Reviewer findings for the gates the risk tier requires.
- The support and monitoring arrangements on the `support-and-monitoring-plan` template.

Where an item of evidence is missing or relates to a different version, mark it `[To confirm: ...]` and treat it as not
met. Never accept a verbal assurance in place of evidence for a blocking item.

## Decision framework

Each area is checked against evidence for the release version. Any unmet blocking item means no-go; advisory items may
become conditions with an owner and date.

| Area | Evidence of readiness | Blocking when |
|---|---|---|
| Quality | Evaluation on the release version meets thresholds agreed beforehand | No evaluation on this version, or below threshold |
| Safety | Safety evaluation and content controls tested; red-team findings closed or accepted | Open high-severity safety findings |
| Security and identity | Least-privilege identities, private networking where required, no stored keys, security testing passed | Untested tools with external effect, or shared keys in production |
| Data and privacy | Processing location confirmed, retention set for threads, traces and indexes, privacy assessment done where needed | Personal data processed without agreed basis or retention |
| Human oversight | Checkpoints on consequential actions in place and tested | Irreversible effects without a checkpoint |
| Deployment and capacity | Production built in governed environments, quota granted, load tested | Quota unconfirmed or prototype resources in use |
| Observability | Run tracing proven by a failed-run test; quality and safety signals live | A failure cannot be reconstructed |
| Cost | Budget, alerts and owner in place; cost per outcome known | No budget owner |
| Resilience and rollback | Fallback tested; rollback and kill switch rehearsed | Never rehearsed |
| Support and ownership | Named owner, support route, runbook, knowledge transfer complete | No internal owner able to change and operate it |
| Lifecycle | Model retirement dates tracked, review date set | Model already deprecated with no plan |
| Transparency | Users told they are using AI, what it does and how to reach a person | No disclosure |

## Practitioner approach

Pin the release version first. List the model and version, prompt and instruction versions, tool contracts, grounding
sources, configuration and infrastructure versions that make up the release. Every piece of evidence is then checked
against this list. The most common readiness failure is evaluation evidence from three prompt revisions ago presented
as current.

Collect evidence, do not convene opinions. For each area in the framework, ask for the artefact: the evaluation report
with the version on it, the security test results, the load test, the rollback rehearsal record. Where the evidence
belongs to a reviewer gate, take the reviewer's recorded finding rather than re-reviewing. Your job is completeness and
currency, not a second opinion on specialist work.

Rehearse the bad days. Before release, switch the solution off and back on in production or a production-equivalent
environment, roll back one configuration change, and trigger one alert to confirm it reaches a person who acts. Run a
deliberately failing scenario and have support explain it from the traces. These rehearsals find more real problems
than any checklist, especially in solutions handed over by a partner.

Check ownership in practice. Ask the internal owner to make a small, safe change, such as updating an instruction or
rotating a credential through the pipeline, and to find the runbook. If they cannot, the solution is not ready to be
owned, whatever the contract says. Confirm the support route, the incident route through
`ai-operations:ai-incident-management`, and the review calendar entry for model lifecycle and periodic evaluation.

Plan the release itself. Prefer a staged release to a defined audience with an agreed observation period and explicit
criteria for widening, rather than switching everyone on at once. Confirm users will be told what the solution does,
that it is AI and how to reach a person.

Then write the recommendation: go, go with conditions, or no-go. Conditions are advisory items with a named owner, a
date and a check; blocking items are never converted into conditions to meet a deadline. Disagreement goes to the
accountable executive through `responsible-ai:ai-risk-acceptance`, recorded in writing. State plainly what readiness
cannot determine: behaviour on real traffic, which the observation period exists to reveal.

## Outputs

- A production readiness record in the `foundry-solution-design` template: release version, evidence per area with status and source, blocking and advisory findings, conditions with owners and dates, rehearsal results and the recommendation.
- A staged release plan with audience, observation period and widening criteria.
- A signed release decision by the accountable owner.

## Microsoft platform considerations

Foundry solutions depend on Azure resources, model deployments and service features whose availability, quota,
lifecycle and preview status change. Confirm in the current source records that no production dependency is on a
retired or soon-to-retire model or on an unsupported preview feature, or record the dependency as an accepted risk.
Licensing questions route to the Microsoft licensing guide or a licensing partner.

## Adoption considerations

Production release is when people start relying on the solution. Confirm the business owner has prepared users with
what the solution does and does not do, how to give feedback and how to reach a person, and that the people whose work
changes have been briefed.

## Knowledge considerations

Confirm every grounding source in the release has an owner, a refresh route and a review date, and that the content
precondition from the grounding strategy has been met. A solution released on unowned knowledge decays from launch.

## Security and privacy considerations

Confirm security testing, identity review and privacy assessment are complete for the release version, that secrets
are in managed stores, and that retention for threads, traces and indexes is set and enforced. The
`security-privacy` gate findings are taken as recorded.

## Responsible AI considerations

Confirm the impact assessment, human oversight design and transparency measures required for the risk tier are in
place and tested. Residual risk that the owner accepts is recorded through `responsible-ai:ai-risk-acceptance`, never
assumed.

## Evaluation requirements

Quality and safety evaluation must have been run on the exact release version against thresholds agreed before
results were seen, with the evidence pack accepted by `evaluation-quality` from tier 2. Any change after evaluation
invalidates it until rerun.

## Value measures

Confirm the baseline exists and the value measures can be collected from the first day, owned by the business owner.
Track readiness findings that later caused incidents, to improve the checklist.

## Scale notes

### Starter

Use the framework as a one-page checklist with evidence links, rehearse the switch-off and rollback, and release to a
small audience first. A partner may compile evidence; the internal owner signs.

### Scale

Standardise the readiness record and rehearsals across Foundry solutions, automate evidence collection from pipelines
and evaluation runs, and keep a log of conditions and their closure.

### Enterprise

Integrate readiness with the organisation's release management and service transition processes, with reviewer gates
scheduled into delivery plans and readiness evidence retained for audit against the AI management system.

## Hand-offs

- To `evaluation-quality:ai-release-evidence` for the formal evidence pack from tier 2.
- To `ai-operations:ai-support-model` for transition into support.
- To `ai-operations:ai-review-calendar` for lifecycle and periodic evaluation reviews.
- To `platform-governance:ai-solution-inventory` to register the live solution.
- To `responsible-ai:ai-risk-acceptance` for residual risk the owner accepts.

## Reviewer gates

The release policy sets the gates by risk tier. From tier 2, `evaluation-quality` accepts the evidence pack,
`security-privacy` confirms security and privacy findings are closed, `responsible-ai` confirms oversight and
transparency, and `design-authority` checks supportability. Each gate classifies findings as blocking or advisory, and
a blocking finding stops release.

## Failure modes

- Evaluation results from an earlier prompt or model version are accepted as evidence for the release.
- The kill switch and rollback were never rehearsed, and the first incident becomes an outage.
- A partner-built solution goes live without a handover, and nobody internal can operate it.
- Blocking findings are relabelled as conditions to hit a launch date, and the risk is never closed.
- The solution is switched on for everyone at once, and a problem reaches every user before it is seen.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Accept evidence that does not relate to the exact release version.
- Convert a blocking finding into a condition to meet a deadline.
- Release a solution whose switch-off and rollback have not been rehearsed.
- Recommend go without a named internal owner able to change and operate the solution.
