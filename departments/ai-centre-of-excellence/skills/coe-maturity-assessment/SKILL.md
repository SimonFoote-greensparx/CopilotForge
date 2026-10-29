---
name: coe-maturity-assessment
description: Assesses how mature a running AI Centre of Excellence is across sponsorship, team, opportunity pipeline, knowledge, delivery, governance, adoption and Champions, portfolio and value, using evidence from its own records, and sets the three to five next moves, including whether it is ready for spokes or federation. Use when a CoE has run for six months or more, at its annual review, or when the sponsor asks whether it is working.
license: CC-BY-4.0
metadata:
  department: ai-centre-of-excellence
  lifecycle: Measure, Scale, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: scale, enterprise
  reviewers: none
  sources: ms-coe-starter-kit, ms-copilot-adoption-hub, ms-copilot-studio-guidance, nist-ai-rmf, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# CoE maturity assessment

## Purpose

After its launch, a CoE needs an honest view of what is working and what to fix next, not a celebration of activity.
This skill assesses the CoE as a capability, dimension by dimension, using evidence from its own records: decision logs,
the backlog, the register, the ledger. It ends with a short list of next moves and a clear view on whether the CoE is
ready to change shape. Maturity reviews go wrong when they are self-scored by the CoE team, when they reward the number
of agents built, and when they recommend federation because it sounds mature rather than because standards are stable.

## When to use

- The CoE has run for six months or more and the sponsor wants to know whether it is working.
- The annual strategy review needs an evidence-based view of the CoE.
- The organisation is considering moving to hub and spoke or federation.
- The CoE feels busy but steering cannot say what has improved.

## When not to use

- Diagnosing the whole organisation's AI maturity and archetype - use `ai-strategy:ai-maturity-assessment`.
- Checking whether a CoE can launch at all - use `ai-centre-of-excellence:coe-readiness`.
- Reviewing the health of the Champions programme - use `champions:champions-health-check`.
- Assessing the health of a wider AI programme - use `programme-management:programme-health`.
- Redesigning the CoE shape once the assessment recommends it - use `ai-centre-of-excellence:coe-operating-model`.

## Questions to ask first

1. How long has the CoE been running, and what did its charter and launch plan commit to?
2. Which records exist and can be inspected: decision log, backlog, register, knowledge register, value ledger, scorecard?
3. Who outside the CoE team can give an independent view: business owners, makers, reviewers, Champions?
4. What decision is the assessment meant to inform: continue as is, invest more, change shape, or reset?
5. Has a previous assessment been done, and which of its actions were completed?

## Required inputs

- The charter, operating model and launch plan, as the CoE's own commitments.
- The CoE's records: decision log, backlog with dates, portfolio register, knowledge register, value ledger and scorecard.
- Interviews with a sample of business owners, makers, reviewers and Champions, recorded by role.
- Any earlier assessment and its action list.

Where a record does not exist, the dimension it evidences cannot score above the first level. Note that as a finding,
not as an inconvenience.

## Decision framework

Score each dimension at the highest level whose evidence is fully met. A level counts only when shown in a record or
confirmed by at least two independent roles outside the CoE team.

| Dimension | 1 Forming | 2 Operating | 3 Repeatable | 4 Scaling | 5 Embedded |
|---|---|---|---|---|---|
| Sponsorship and decisions | Sponsor named | Sponsor attends; some decisions logged | Most decisions taken on time and logged | Sponsors in place for each spoke | AI decisions part of normal business governance |
| Team and capacity | Volunteers | Core team with agreed time | Roles stable, capacity reviewed against demand | Pillar leads and spoke teams | Roles built into job design and succession |
| Opportunity pipeline | Ideas in an inbox | Backlog with owners | Stages, exit tests and service levels met most of the time | Spokes run pipelines under common rules | Pipeline is the normal route for improvement ideas |
| Knowledge | No register | Register started | Owners and in-date reviews for most grounding sources | Register across units with issue loop working | Knowledge managed as shared infrastructure |
| Delivery | Ad hoc builds | Routes defined | Definition of done applied; support accepts releases | Patterns reused across teams | Delivery standards part of normal engineering and making |
| Governance | No tiers | Tiers and register in use | Reviewer gates applied consistently from tier 2 | Federated gates with hub assurance | Governance proportionate and largely automated by platform controls |
| Adoption and Champions | Enthusiasts only | Champions linked to CoE | Champion roles active in most teams; feedback loop working | Network spans units | AI use part of everyday work in most roles |
| Portfolio | Unknown estate | List of live solutions | Owners, review dates and health for every solution | Consolidation, reuse and retirement happening | Portfolio decisions part of business planning |
| Value | Anecdotes | Some baselines | Ledger with confidence grades for most solutions | Value reviewed and acted on across units | Benefits reported through normal business reporting |

The overall level is capped at the lowest score among sponsorship, governance and value, because a CoE cannot be more
mature than its ability to decide, stay safe and show results. Report stronger dimensions as strengths, not as the
headline.

| Proposed shape change | Ready when |
|---|---|
| Add spokes (hub and spoke) | Pipeline, governance and knowledge at level 3 or above; each spoke has a sponsor and lead |
| Federate | Governance at level 4 and pipeline at level 3 or above across spokes, with trained reviewers and one register |
| Consolidate or reset | Sponsorship or value at level 1 after six months of operation |

## Practitioner approach

Agree the decision the assessment informs before collecting anything. "Should we federate?" needs a different depth
from "is it working?". Write the question at the top of the report and come back to it at the end.

Collect evidence from records first. Read the decision log for decisions taken versus deferred, the backlog for time from
submission to decision, the register for owners and review dates, the knowledge register for in-date reviews, and the
ledger for measured value and confidence. Records reveal what interviews soften.

Then interview a sample of people outside the CoE team: two or three business owners, makers, reviewers and Champions.
Ask what happened when they brought an idea or a solution, how long it took, and what they would change. Record views by
role, never by name, and look for patterns rather than single complaints.

Score each dimension against the framework, writing the evidence beside every score. The CoE team should see the scores
and evidence and may add evidence, but should not score itself; an assessor from outside the team, or the sponsor's
delegate, holds the pen. This is an assessment of a capability, never of the people in it.

Apply the cap and write the headline honestly. A CoE with an excellent delivery route but no measured value is at
level 2, whatever it has built. Show strengths clearly so the team sees what to keep.

Choose three to five next moves, no more. Each targets a dimension below the cap or a blocker to the decision the
assessment informs, with an owner, a date and the evidence that will show it is done. If the question was about shape,
apply the shape table and say plainly whether the CoE is ready, with the conditions if it is not.

Present to the sponsor and steering together, and record the agreed actions in the decision log. Schedule the next
assessment, usually annually, sooner if a shape change is under way. Be clear about limits: the assessment shows how
well the CoE operates, not whether the organisation as a whole is getting value from AI, which is the organisation-wide
maturity assessment's job.

## Outputs

- A CoE maturity assessment: decision question, evidence log, dimension scores with evidence, overall level after the cap, strengths and gaps.
- Three to five next moves with owners, dates and completion evidence.
- A shape-change recommendation where asked, with conditions.
- A one-page sponsor summary, and actions recorded in the steering decision log.

## Microsoft platform considerations

Admin inventory, the CoE Starter Kit and platform analytics can supply evidence for the portfolio, governance and
delivery dimensions. Check what they currently report in `references/sources.md` and treat them as evidence sources,
not as the assessment itself.

## Adoption considerations

Share the headline and next moves with the wider CoE community, not just steering. A CoE that publishes its own gaps and
plans to fix them earns trust with business units and Champions.

## Knowledge considerations

Knowledge is often the weakest dimension and the one that limits delivery. Where it scores lowest, make a knowledge move
one of the next moves, routed to `ai-centre-of-excellence:coe-knowledge-pillar`.

## Security and privacy considerations

Check from records that tier 2 and above releases had `security-privacy` reviews completed before release, and that the
register has no ownerless shared solutions. Gaps here count against the governance dimension and may need immediate
action outside the assessment cycle.

## Responsible AI considerations

Check that solutions which inform decisions about people, money, safety or rights have recorded human oversight and in-date
reviews. A lapse here is reported to the sponsor directly, not left for the next moves list.

## Evaluation requirements

Not applicable to the assessment as an AI output, because it judges an organisational capability. Its own quality comes
from evidence: every score cites a record or two independent views.

## Value measures

Track the CoE's level by dimension over successive assessments and the completion of next moves by their dates. The CoE
lead owns the action list; the sponsor owns the decision the assessment informs. Never use the assessment to evaluate
individual team members.

## Scale notes

### Starter

Not usually needed. A Starter working group reviews its charter commitments once a year with the sponsor and decides
whether to continue, stop or grow into a CoE.

### Scale

An annual assessment by someone outside the core team, with records, a handful of interviews and three to five next
moves agreed at steering.

### Enterprise

The hub assesses itself and each spoke on the same framework, compares patterns across units without ranking them, and
uses the results to decide which spokes are ready for more delegated authority.

## Hand-offs

- To `ai-centre-of-excellence:coe-operating-model` when a shape change is recommended.
- To `ai-centre-of-excellence:coe-cadence` to record actions in the decision log.
- To `ai-strategy:ai-maturity-assessment` when the wider organisation's maturity needs reassessing.
- To `ai-centre-of-excellence:coe-kpi-framework` where measures need changing as a result.

## Reviewer gates

Not applicable, because the assessment releases no solution. Findings about governance lapses are passed to
`security-privacy` or `responsible-ai` for the specific solutions concerned.

## Failure modes

- The CoE team scores itself and the result is a celebration rather than a diagnosis.
- Maturity is equated with the number of agents built, so value and knowledge gaps are hidden.
- Federation is recommended because it sounds advanced, before shared standards are stable.
- The next moves list runs to twenty items and none is completed.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Score a dimension above the first level without a record or two independent views.
- Let the CoE team score its own maturity.
- Rank spokes, teams or people against each other.
- Recommend federation before governance and the pipeline meet the shape-change criteria.
