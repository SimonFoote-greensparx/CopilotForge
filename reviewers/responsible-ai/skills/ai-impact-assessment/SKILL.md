---
name: ai-impact-assessment
description: Assesses who an AI solution affects - users, people it makes outputs about, workers whose roles change and the organisation - covering intended and foreseeable uses, benefits, harms, severity and likelihood, and the mitigations each needs, then classifies residual concerns as blocking or advisory. Use when a solution reaches its responsible AI gate, when it informs decisions about people, or when a sponsor asks what could go wrong for whom.
license: CC-BY-4.0
metadata:
  department: responsible-ai
  lifecycle: Envision, Deliver, Assure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: responsible-ai
  sources: ms-responsible-ai, nist-ai-rmf, iso-iec-42001, ico-ai-data-protection
  status: draft
  authors: Simon Foote
---

# AI impact assessment

## Purpose

An AI impact assessment asks a simple question with discipline: who could this solution help or harm, how badly, and
what will the organisation do about it? It looks beyond the users in the brief to the people outputs are about, the
workers whose tasks change and the organisation's own obligations, and it records the reasoning so later reviewers can
see why the solution was built the way it was. This reviewer skill produces the impact assessment record and classifies
residual concerns as blocking or advisory. It goes wrong when it is completed after build as a form to clear the gate,
when only intended uses are considered, or when "a human checks it" is written down without anyone asking whether the
human can.

## When to use

- A solution at risk tier 2 or above reaches its `responsible-ai` gate.
- Outputs will inform decisions about employees, candidates, customers, patients, tenants or members of the public.
- The solution changes how a role works, or what people are expected to check or decide.
- Scope, audience, data or autonomy change materially for a live solution.
- A sponsor or steering group asks what could go wrong, and for whom.

## When not to use

- Assigning the risk tier and the gates that apply - use `opportunity-management:risk-classification`.
- Screening personal data processing and DPIA need under data protection law - use `security-privacy:privacy-assessment`.
- Assessing how AI change affects groups of staff for change management - use `change-and-communications:people-change-impact`.
- Designing the human review once the assessment says it is needed - use `responsible-ai:human-oversight`.
- Checking whether a use is prohibited outright - use `responsible-ai:prohibited-use-review`.

## Questions to ask first

1. What is the solution for, who uses it, and who is affected by its outputs without ever using it?
2. Which decisions or actions does it inform or take, and how reversible are they for the person affected?
3. What are the realistic ways it could be misused or relied on beyond its purpose?
4. Which groups could be affected differently, including people with protected characteristics, disabilities or limited language skills?
5. What benefit justifies the residual risk, and who is accountable for accepting it?

## Required inputs

- The framed problem, suitability decision and risk tier from `opportunity-management`.
- The agent brief or solution design, with audience, data, actions and autonomy.
- The privacy assessment, where personal data is involved, and any security findings.
- Input from people who represent affected groups, or a record of why that was not possible.

Where affected groups were not consulted at tier 3 or above, record it as a gap. Never complete the assessment from the
build team's perspective alone and present it as the affected people's view.

## Decision framework

Rate each identified impact for severity (minor, moderate, serious, severe) and likelihood (rare, possible, likely),
then decide its treatment. From risk tier 2 every residual concern is classified blocking or advisory. The gate is
mandatory and blocking from tier 3, and from tier 2 whenever outputs inform decisions about people.

| Residual impact after mitigation | Classification | Treatment |
|---|---|---|
| Serious or severe and possible or likely, on rights, safety, livelihood or access to services | Blocking | Redesign, add controls, narrow scope, or do not build; only executive risk acceptance can override, never for prohibited uses |
| Serious but rare, with tested controls and a working appeal route | Advisory | Monitor with named owner and review date |
| Moderate, reversible, with human review that can catch it | Advisory | Document mitigations and monitoring |
| Minor and reversible | No finding | Record in the assessment |
| Impact cannot be judged because information is missing | Blocking at tier 3 and above | Obtain the information; consult affected groups |

Common mitigations to test before accepting residual risk: narrowing scope, removing an action, adding human oversight,
improving transparency, fixing data, adding an appeal route and monitoring outcomes by group.

## Practitioner approach

Begin early. The most useful impact assessment is drafted at design, when removing a feature is cheap, and updated
before release. If you are asked to assess a finished build, say so in the record and expect more blocking findings.

Map the people first. Draw three rings: the people who use the solution, the people its outputs are about, and the
people whose work changes because it exists. A triage agent used by advisers affects the customers whose cases are
triaged more than the advisers themselves. A summarisation tool used by managers affects the staff being summarised.
Write each group down with what they would want from the solution and what they would fear.

Then walk the uses. Start with the intended use, then the foreseeable ones: users copying outputs into decisions the
solution was never meant to inform, relying on it out of hours when nobody checks, or using it for a group it was not
tested on. Misuse that is easy and tempting is foreseeable, not hypothetical.

For each group and use, name the potential harms concretely: a wrong answer that denies a service, a summary that
misrepresents someone, an outcome that is worse for people who write in a second language, a loss of skills or
discretion for workers, a decision nobody can explain. Rate severity and likelihood honestly, then test mitigations.
Ask whether the human reviewer has the time, information and authority to catch the error; if not, the mitigation is
on paper only.

Consult. For tier 3 and 4, involve people who represent affected groups, such as employee representatives, customer
panels or accessibility advisers. Record what they said and what changed as a result.

Write the record on the `ai-impact-assessment-record` template: purpose, affected groups, uses, impacts, ratings,
mitigations, residual concerns classified blocking or advisory, and the accountable owner. Be proportionate: a tier 2
internal knowledge agent may need two pages. Agree the review trigger, because impacts change when audience, data or
autonomy change. Where residual risk remains disputed, route it to `responsible-ai:ai-risk-acceptance`; never trade a
blocking concern against a launch date.

## Outputs

- An AI impact assessment record on the `ai-impact-assessment-record` template, with each residual concern classified blocking or advisory, its owner and review date.
- Referrals to `responsible-ai:human-oversight`, `responsible-ai:ai-transparency`, `responsible-ai:fairness-review` and `responsible-ai:escalation-and-appeal` for the controls the assessment calls for.
- A plain-language summary for the business owner and sponsor.

## Microsoft platform considerations

The assessment is platform-neutral, but the route affects which mitigations are available: human approval steps in
flows, confirmation before actions, content filtering, citations and transparency messages differ across Copilot,
agents, Copilot Studio and Foundry. Microsoft publishes responsible AI principles and transparency resources for its
services; use `ms-responsible-ai` to understand the provider's position, without treating it as the organisation's
own assessment.

## Adoption considerations

Workers whose roles change are an affected group. Where the assessment finds loss of discretion, deskilling or new
checking burdens, pass the findings to `change-and-communications:people-change-impact` so change plans address them.

## Knowledge considerations

Outdated or partial knowledge is a common cause of harm in grounded solutions. Where impacts depend on knowledge
quality, record the dependency and the knowledge owner.

## Security and privacy considerations

Personal data impacts are assessed with `security-privacy:privacy-assessment`; the two records should reference each
other rather than duplicate. Security failures that would harm people, such as data leaks, are noted as impacts.

## Responsible AI considerations

This skill is the core responsible AI assessment. It decides which other responsible AI controls the solution needs and
records why.

## Evaluation requirements

Mitigations that rely on solution behaviour need evaluation evidence, for example tests across affected groups or
refusal tests for out-of-scope uses, agreed with the `evaluation-quality` reviewers. Record the evidence against each
mitigation.

## Value measures

Track at portfolio level the share of tier 2+ solutions with a current assessment, the number assessed at design rather
than after build, and residual concerns closed by their review date. The responsible AI lead owns these measures.

## Scale notes

### Starter

Run the assessment as a facilitated session with the business owner and one reviewer, recorded on the template. Avoid
tier 3 and 4 uses until the organisation has a reviewer with the time to assess them properly.

### Scale

Make the assessment a standing step at design for tier 2 and above, reuse assessments for similar solutions, and keep a
library of common impacts and tested mitigations.

### Enterprise

Federate tier 2 assessments to trained business-unit reviewers, with the central responsible AI function reviewing tier
3 and 4 and maintaining consistency across the portfolio.

## Hand-offs

- To `responsible-ai:human-oversight`, `responsible-ai:ai-transparency`, `responsible-ai:fairness-review` and `responsible-ai:escalation-and-appeal` for required controls.
- To `responsible-ai:ai-risk-acceptance` for disputed or residual blocking concerns.
- To `security-privacy:privacy-assessment` where personal data impacts need a DPIA.
- To `m365-agents:agent-release-readiness` with the verdict.

## Reviewer gates

This skill is the `responsible-ai` gate's impact assessment. It is mandatory and blocking from risk tier 3, and from
tier 2 when outputs inform decisions about people; otherwise advisory at tier 2. Blocking concerns are not traded
against dates; disagreement escalates to the accountable executive for written risk acceptance.

## Failure modes

- The assessment lists only users and misses the people outputs are about.
- "A human reviews it" is accepted without checking whether the reviewer has time, information or authority.
- The assessment is written after build to clear the gate, so findings are framed to avoid rework.
- Scope widens after release and the assessment is never revisited.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Present the build team's view as the view of affected people.
- Accept a mitigation that exists on paper but has not been tested.
- Trade a blocking concern against a launch date.
- Give a legal opinion; legal and data protection questions go to the legal adviser and DPO.
