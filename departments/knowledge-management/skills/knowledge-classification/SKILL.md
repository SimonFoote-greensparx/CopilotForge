---
name: knowledge-classification
description: Classifies knowledge collections by sensitivity, intended audience and knowledge status (authoritative, reference, working, archive) using the organisation's existing scheme, then aligns labels, permissions and AI grounding eligibility with that classification. Use when collections are unlabelled or labelled inconsistently, when audiences are unclear before Copilot or agent rollout, or when owners ask who should see their content.
license: CC-BY-4.0
metadata:
  department: knowledge-management
  lifecycle: Mobilise, Enable, Deliver
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: sharepoint, purview, m365-copilot, m365-agents
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-privacy, ms-agent-builder, ico-ai-data-protection
  status: draft
  authors: Simon Foote
---

# Knowledge classification

## Purpose

AI makes everything a person can open easy to find, so the question "who should see this?" matters far more than it did
when content was hard to locate. This skill applies the organisation's classification scheme to knowledge collections,
records three facts for each - sensitivity, intended audience and knowledge status - and makes sure labels, permissions
and AI grounding eligibility all agree with them. It goes wrong when classification is treated as a labelling exercise
alone, leaving permissions that contradict the label, or when the knowledge team invents its own scheme alongside the
one data governance already owns.

## When to use

- Knowledge collections are unlabelled, or labels are applied inconsistently across similar content.
- Intended audiences are unclear before a Copilot rollout wave or before agents ground on a domain.
- An owner asks who should be able to see their content, or whether it may be used by an agent.
- Readiness or inventory work has found sensitive content in broadly shared locations.

## When not to use

- Designing the organisation's classification scheme and label taxonomy itself - use `data-governance:data-classification-for-ai`.
- The formal review of what an AI solution could expose - use `security-privacy:data-exposure-review`.
- Assessing personal data processing and lawful basis - use `security-privacy:privacy-assessment`.
- Designing site and library structures that put audiences in the right places - use `knowledge-management:sharepoint-knowledge-design`.

## Questions to ask first

1. What classification scheme and sensitivity labels does the organisation already use, and who owns them?
2. For each collection, who is the intended audience in plain words, and who can actually open it today?
3. Which collections contain personal data, commercially sensitive material or regulated content?
4. Which collections are authoritative, which are reference or working material, and which should be archived?
5. Which AI uses would ground on each collection, and are their audiences the same as the content's?

## Required inputs

- The organisation's classification scheme and label definitions from the data governance owner, or confirmation that none exists.
- The collections in scope with owners, from `knowledge-management:knowledge-inventory`.
- Actual access for each collection from administrative reports or the site administrator.
- The AI uses and audiences that depend on each collection.

If no scheme exists, record the owner's plain-language view of sensitivity, flag the gap to the `data-governance`
department, and do not invent labels. Where actual access cannot be inspected, the collection is not eligible for AI
grounding until it can be.

## Decision framework

Record three classifications per collection and derive eligibility from them.

| Classification | Values (adapt to the organisation's scheme) | Who decides |
|---|---|---|
| Sensitivity | The organisation's levels, for example public, internal, confidential, highly confidential | Content owner, within the scheme |
| Intended audience | All staff, a function, a named group, a role, external parties | Content owner, confirmed by domain owner |
| Knowledge status | Authoritative, reference, working, archive | Content owner |

| Combination | AI grounding eligibility |
|---|---|
| Authoritative, audience matches actual access, sensitivity labelled | Eligible for agents whose audience is within the content's audience |
| Reference | Eligible with conditions; agents must distinguish it from authoritative content |
| Working | Not eligible for shared agents; remains available to Copilot for people who already have access |
| Archive | Not eligible; move out of active locations |
| Any status where actual access is wider than intended audience | Not eligible until access is corrected at source |
| Highest sensitivity level | Not eligible for shared agents without a security-privacy review |

## Practitioner approach

Begin with the scheme the organisation already has. Meet its owner, usually in data governance, security or records
management, and agree how knowledge collections map to it. Knowledge management applies the scheme; it does not design
a second one. If the scheme is unusable in practice, for example too many levels or definitions nobody understands,
raise that with its owner rather than working around it.

Classify at collection level first. Owners can make a sound judgement about a policy library or a project archive in
minutes; asking them to label thousands of files individually produces fatigue and random choices. Use default labels
on libraries where the platform supports it, and reserve item-level decisions for exceptions the owner identifies.

Record intended audience in plain words and then compare it with actual access. This comparison is the heart of the
skill. A library intended for HR advisers that is open to all staff through an inherited group is a finding, whatever
its label says, because Copilot grounding is permission-trimmed and will surface it to anyone with access. Fix access at
source, through the site administrator, and record the change. Never rely on an agent's instructions or a label alone
to keep content away from people who can open it.

Add knowledge status, which most schemes lack and AI needs. Marking content as authoritative, reference, working or
archive lets makers choose grounding sources sensibly and lets owners move working and archive material out of the way.
It also gives `knowledge-management:knowledge-cleanup` a clear target.

Derive grounding eligibility from the table and record it in the knowledge register. Where personal data or regulated
content appears, flag it to `security-privacy:privacy-assessment` and, for questions of law, to the DPO or legal
adviser; do not decide lawful basis here.

Finally, make classification part of the lifecycle. New libraries should be created with a default label, an intended
audience and a status, so classification happens at creation rather than in periodic catch-up exercises.

## Outputs

- A classification record per collection: sensitivity, intended audience, actual access, knowledge status and AI grounding eligibility, held in the `knowledge-asset-register`.
- A list of access corrections, each with the site administrator responsible and a date.
- Referrals for personal data, regulated content and scheme gaps.

## Microsoft platform considerations

Microsoft Purview sensitivity labels can be applied to files, sites and Teams and can carry protection, and SharePoint
libraries can apply default labels; how labelled and encrypted content behaves in Copilot and in each agent route
depends on configuration and changes over time. Confirm current behaviour in the source records (`ms-copilot-privacy`,
`ms-agent-builder`) before advising. Labels and permissions are separate controls, and both must agree.

## Adoption considerations

Owners classify more accurately when the choice is small and explained with examples from their own content. Brief
users that Copilot respects access, so correcting oversharing protects them as well as the organisation.

## Knowledge considerations

Knowledge status and grounding eligibility are inputs to `knowledge-management:knowledge-grounding-standards` and
`knowledge-management:sharepoint-knowledge-design`; keep definitions identical across those skills.

## Security and privacy considerations

This skill finds exposure; it does not accept it. Every collection where actual access exceeds intended audience is
corrected at source or recorded as a finding for `security-privacy:data-exposure-review`. The highest sensitivity
levels need that review before any shared agent uses them.

## Responsible AI considerations

Audience decisions affect who benefits from AI help. Check that frontline, part-time and partner-facing roles are not
excluded from content they legitimately need simply because it sits in a restricted location.

## Evaluation requirements

Each access correction must be re-checked after it is made. Pass audience boundaries to `m365-agents:agent-testing` as
tests that users outside the audience cannot obtain the content through an agent.

## Value measures

Track the share of AI-dependent collections with all three classifications recorded, the number of collections where
access exceeds intended audience, and the time to correct them. The Knowledge Manager and the security lead share these,
reported by domain.

## Scale notes

### Starter

Classify the collections the first agents and Copilot scenarios depend on, with their owners, and fix the access
mismatches found.

### Scale

Classify every registered collection, apply default labels on libraries, and make classification a required step when
new knowledge sites are created.

### Enterprise

Align classification with records management and data governance across business units, use administrative reports to
find mismatches continuously, and report coverage to steering.

## Hand-offs

- To the site administrator and `security-privacy:data-exposure-review` for access corrections and exposure findings.
- To `knowledge-management:knowledge-cleanup` for working and archive material in active locations.
- To `data-governance:data-classification-for-ai` when the scheme itself needs change.

## Reviewer gates

From risk tier 2, `security-privacy` reviews collections at the highest sensitivity levels, any mismatch between access
and audience that is not yet corrected, and any personal data; its blocking findings must be resolved before grounding.
Below tier 2 the content owner signs the classification.

## Failure modes

- Labels are applied but permissions are left wider than the label implies.
- A parallel knowledge classification scheme appears and conflicts with the data governance scheme.
- Item-by-item labelling fatigue produces random labels that nobody trusts.
- Working drafts remain in authoritative locations and agents quote them as policy.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Invent a classification scheme alongside the one data governance owns.
- Rely on a label or an agent instruction to hide content people can open.
- Decide lawful basis or legal questions about personal data; route them to the DPO or legal adviser.
- Mark a collection eligible for grounding when its actual access has not been checked.
