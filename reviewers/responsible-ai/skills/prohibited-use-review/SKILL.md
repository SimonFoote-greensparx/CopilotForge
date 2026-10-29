---
name: prohibited-use-review
description: Screens a proposed or live AI use against the organisation's prohibited and restricted uses, Microsoft's acceptable use terms and regulation as advised by legal - covert monitoring of staff, emotion inference, social scoring, manipulation, unreviewed decisions about individuals - and records a stop, restrict or proceed verdict. Use when a sensitive idea arrives at intake, when a solution's purpose drifts, or when asked if a use is allowed.
license: CC-BY-4.0
metadata:
  department: responsible-ai
  lifecycle: Discover, Envision, Assure, Improve
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: responsible-ai
  sources: ms-responsible-ai, ico-ai-data-protection, nist-ai-rmf, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# Prohibited use review

## Purpose

Some AI uses should not be built however well they are engineered, and some should be built only under strict
conditions. This reviewer skill screens a proposed or live use against the organisation's own list of prohibited and
restricted uses, the provider's acceptable use terms and the regulation that applies, as advised by the legal adviser,
and records a clear verdict: stop, restrict with conditions, or proceed to the normal gates. It works best early, before
anyone has invested in a build. It goes wrong when the organisation has no list at all, when the screen is skipped for
"internal only" uses, or when a use drifts after approval into something nobody would have approved.

## When to use

- An idea at intake involves monitoring people, inferring emotions or characteristics, scoring individuals or influencing behaviour.
- Outputs could decide something about a person without meaningful human review.
- A live solution's purpose, audience or data is drifting from what was approved.
- Someone asks "are we allowed to use AI for this?"
- The organisation needs its first prohibited and restricted uses list.

## When not to use

- Deciding whether AI is the right answer for a legitimate problem - use `opportunity-management:ai-suitability`.
- Challenging unnecessary AI on design grounds - use `design-authority:ai-necessity-challenge`.
- Assessing the impacts of a permitted use in detail - use `responsible-ai:ai-impact-assessment`.
- Writing the organisation's AI principles and statement of where AI will not be used - use `ai-strategy:strategic-outcomes`.

## Questions to ask first

1. What exactly will the solution do, to whom, and what decision or effect follows from its output?
2. Does it monitor, profile, score, categorise or infer anything about individuals, including emotions, health, beliefs or characteristics?
3. Could it influence people's choices in ways they would not notice or agree to?
4. Is a person meaningfully involved before anything significant happens to someone?
5. Has the legal adviser confirmed which regulation applies in each jurisdiction where the solution operates?

## Required inputs

- A clear description of the use, from the problem framing or brief.
- The organisation's prohibited and restricted uses list, or its AI principles if no list exists.
- The provider's acceptable use and product terms for the chosen service, as confirmed by the person responsible for them.
- Legal advice on applicable regulation where the screen raises a possible legal prohibition.

Where no list exists, screen against the indicators below, record that the verdict rests on them, and recommend the
list be approved by the accountable executive. Never conclude that a use is lawful; that is the legal adviser's call.

## Decision framework

| Indicator | Default verdict | Conditions to consider restriction instead of stop |
|---|---|---|
| Covert monitoring of staff or customers, or inferring productivity, sentiment or emotion of individuals at work | Stop | None for covert use; any overt, proportionate use needs legal and DPO approval and employee consultation |
| Scoring or ranking individuals for general trustworthiness or social behaviour | Stop | None |
| Manipulating people's decisions through techniques they would not notice | Stop | None |
| Inferring sensitive characteristics (health, beliefs, sexuality, ethnicity) from content or behaviour | Stop | Only with explicit legal basis confirmed by legal adviser and DPO |
| Decisions with legal or similarly significant effects on individuals made without meaningful human review | Stop | Restrict to decision support with human oversight designed in `responsible-ai:human-oversight` |
| Uses the provider's terms exclude | Stop | None; the organisation cannot accept this risk |
| Uses the organisation lists as restricted (for example HR decisions, safety advice, legal advice) | Restrict | Conditions set by the responsible AI reviewer and recorded |
| None of the above | Proceed | Normal gates by risk tier |

A stop verdict is blocking at every risk tier. It cannot be overridden through `responsible-ai:ai-risk-acceptance`;
only a change to the use, or a formally approved change to the organisation's list, can alter it. A restrict verdict
sets conditions that later gates check.

## Practitioner approach

Run the screen early, in minutes rather than weeks. Most uses pass quickly, and the value is in catching the few that
should not proceed before anyone builds them. Ask the five questions in plain terms and listen for the words that
signal trouble: monitor, score, detect mood, flag risky employees, nudge, decide automatically.

Describe the use precisely. "Analyse team meetings" could mean summarising decisions for attendees, which is
ordinary, or scoring individuals' engagement, which is monitoring. Write the precise version in the record, because
uses that are vague at screening are the ones that drift.

Check the provider terms. Microsoft and other model providers available through Microsoft publish acceptable use and
responsible AI terms that restrict certain uses. Do not paraphrase them from memory; ask whoever manages the
organisation's Microsoft agreements to confirm the current position for the service in question, and record what was
checked.

Involve legal early where a legal prohibition is possible. Regulation on AI differs by jurisdiction and is changing.
The reviewer's job is to recognise the indicators and route the case, not to interpret the law.

Give a clear verdict. Stop means stop, with a short explanation and, where possible, an alternative that meets the
legitimate need, for example aggregate meeting insights instead of individual scoring. Restrict means proceed with
written conditions. Proceed means the use joins the normal route with its risk tier.

Watch for drift. Approved uses change: a summarisation agent gains a feature that rates contributions, a support agent
starts recommending refunds. Ask solution owners at each review whether the purpose has changed, and re-screen when it
has.

If the organisation has no list, draft one from the indicators above with the responsible AI lead, legal adviser and
DPO, and take it to the accountable executive for approval. A short, specific list helps makers far more than broad
principles.

## Outputs

- A prohibited use screening record: use described precisely, indicators checked, provider terms confirmed, legal advice reference, verdict (stop, restrict, proceed) and conditions.
- Where stopped, a plain-language explanation and an alternative route for the legitimate need.
- Where no list exists, a draft prohibited and restricted uses list for executive approval.
- The verdict recorded in the `ai-impact-assessment-record` where an assessment follows.

## Microsoft platform considerations

Microsoft's responsible AI resources in `ms-responsible-ai` describe the provider's principles and transparency
material. Specific acceptable use terms and any limited-access features vary by service and change over time; confirm
the current terms for the chosen route rather than relying on recollection.

## Adoption considerations

Publish the prohibited and restricted list in plain language so people do not propose prohibited uses in good faith.
Explain stop verdicts respectfully; people who understand why come back with better ideas.

## Knowledge considerations

Not applicable, because the screen concerns the purpose of the use rather than the knowledge it grounds on.

## Security and privacy considerations

Many prohibited uses involve personal or special category data. Route any proposed processing of such data to
`security-privacy:privacy-assessment` and the DPO, even when the use is restricted rather than stopped.

## Responsible AI considerations

This skill is the responsible AI screen for unacceptable uses. Uses that proceed go on to
`responsible-ai:ai-impact-assessment` where their tier requires it.

## Evaluation requirements

Where a use is restricted, its conditions need evidence at later gates, for example refusal tests showing the solution
declines out-of-scope requests that would cross into prohibited territory.

## Value measures

Track the number of screens, the share completed before build, stop and restrict verdicts by theme, and re-screens
triggered by drift, at portfolio level. The responsible AI lead owns these measures.

## Scale notes

### Starter

Use the indicator table as a short screen at intake and agree a first list with the sponsor and legal adviser.

### Scale

Embed the screen in the CoE intake form and in agent review cycles, and keep a log of verdicts as precedents.

### Enterprise

Maintain the list centrally with legal input across jurisdictions, federate screening to business-unit reviewers, and
reserve stop verdicts for central confirmation.

## Hand-offs

- To `responsible-ai:ai-impact-assessment` for uses that proceed or are restricted at tier 2 and above.
- To `opportunity-management:ai-suitability` with an alternative for stopped uses.
- To the legal adviser and DPO for possible legal prohibitions.
- To `ai-strategy:strategic-outcomes` to reflect the list in the statement of where AI will not be used.

## Reviewer gates

This skill is part of the `responsible-ai` gate and applies at every risk tier. A stop verdict is blocking and cannot be
overridden by risk acceptance; restrict verdicts set conditions that `responsible-ai` and `security-privacy` check at
later gates.

## Failure modes

- The organisation has no list, so each case is argued from scratch and outcomes are inconsistent.
- A use is described vaguely at screening and later drifts into individual scoring.
- Provider terms are paraphrased from memory and turn out to be wrong.
- "Internal only" is treated as an exemption, so covert staff monitoring proceeds.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Allow a stop verdict to be overridden by risk acceptance or a launch date.
- Conclude that a use is lawful; route legal questions to the legal adviser.
- Treat internal use as an exemption from the screen.
- Approve covert monitoring or emotion inference about individuals at work.
