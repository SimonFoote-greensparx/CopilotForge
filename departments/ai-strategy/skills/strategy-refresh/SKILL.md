---
name: strategy-refresh
description: Refreshes an existing AI strategy on a fixed cycle or a defined trigger, testing the vision, outcomes, platform position and roadmap against measured outcomes, a re-run maturity baseline, Microsoft product change and new regulation, and records what changed and why. Use when the annual strategy review is due, when outcomes are off track, or when a major Microsoft or regulatory change makes the current strategy doubtful.
license: CC-BY-4.0
metadata:
  department: ai-strategy
  lifecycle: Measure, Improve, Scale
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-overview, ms-copilot-adoption-hub, nist-ai-rmf, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# Strategy refresh

## Purpose

This skill keeps the AI strategy honest after it has been agreed. On a fixed cycle, or when a defined trigger fires, it
tests each element of the strategy against evidence (outcome measures, a re-run maturity baseline, what Microsoft has
changed and what regulation now requires) and decides for each element whether to keep, adjust or retire it. The
result is a versioned strategy with a clear record of what changed and why. Refreshes usually go wrong by becoming a
rewrite from scratch that discards what was learned, by becoming a rubber stamp that changes nothing, or by chasing
every Microsoft announcement so that the strategy never settles long enough to deliver.

## When to use

- The scheduled annual (or half-yearly) strategy review is due.
- Outcome measures are persistently off track, or have been met early.
- Microsoft has introduced, retired or substantially changed a platform the strategy depends on.
- New regulation, a significant incident or a change of leadership raises doubts about the principles or ambition.
- The organisation has moved archetype and the strategy still describes the previous one.

## When not to use

- Writing a first strategy where none exists - start with `ai-strategy:ai-vision` and `ai-strategy:strategic-outcomes`.
- Re-sequencing the roadmap within an unchanged strategy - use `ai-strategy:ai-roadmap`.
- Re-running only the maturity diagnosis - use `ai-strategy:ai-maturity-assessment`.
- Refreshing a transformation pack after the organisation profile changes - use `organisation-tailoring:transformation-pack-refresh`.
- Reviewing one initiative's outcomes against its case - use `value-realisation:post-implementation-review`.

## Questions to ask first

1. What triggered this refresh: the cycle, an outcome signal, Microsoft change, regulation, an incident or leadership change?
2. Which outcome measures have moved, which have not, and how confident are we in the data?
3. Has the maturity baseline been re-run, and has the archetype changed?
4. Which Microsoft platform changes since the last version affect the platform position or roadmap?
5. Who must approve a changed strategy, and how much change can the organisation absorb this cycle?

## Required inputs

- The current strategy set: vision, outcomes, principles, platform position, roadmap and investment case, with version and date.
- Outcome measures against baseline, from `value-realisation:value-dashboard` or the CoE scorecard.
- A re-run maturity assessment from `ai-strategy:ai-maturity-assessment`, or a note of why it was not re-run.
- A summary of relevant Microsoft changes since the last version, checked against current source records.
- Any regulatory, incident or audit findings since the last version, and the programme health view.

Where evidence is missing (for example, no outcome data yet), record the gap and limit the refresh to elements the
evidence can support. Never refresh a strategy on opinion alone and present it as evidence-based.

## Decision framework

Test each strategy element and give it one disposition.

| Element | Keep when | Adjust when | Retire or replace when |
|---|---|---|---|
| Ambition level and vision | Maturity and investment still match | Maturity has moved one stage, or investment changed | Leadership or purpose has changed fundamentally |
| Strategic outcomes | Measures are moving as expected | Off track with a known, fixable cause, or met early | No longer a business priority, or AI is shown not to help |
| Principles and exclusions | No incidents or regulatory change contradict them | A real decision exposed a gap | Regulation or an incident shows they are wrong |
| Platform position | Postures still match capability and support | A Microsoft change or new evidence shifts a posture | A platform is retired or the organisation cannot support it |
| Roadmap and investment | Tranche evidence arrived as planned | Evidence is late or partial | A tranche gate failed and the option is no longer viable |

Distinguish signal from noise. A single quarter's dip or a single product announcement rarely justifies changing an
outcome or posture; two consecutive review points or a confirmed, generally available change usually does.

## Practitioner approach

Agree the refresh triggers when the strategy is first approved, so a refresh is an expected event rather than a
crisis. A sensible default is a full refresh annually, a light check at each quarterly strategy review, and an
unscheduled refresh when a defined trigger fires. Record the triggers alongside the strategy.

Gather the evidence before anyone opens the strategy document. Outcome measures against baseline, the re-run maturity
assessment, programme health, incidents, audit findings and scale-or-stop decisions tell you what actually happened.
Prepare a short summary of Microsoft changes since the last version from the current source records, limited to
changes that affect the organisation's postures or roadmap. A long list of announcements is noise.

Run the refresh element by element, using the disposition table. Start with outcomes, because they anchor everything
else. Where an outcome is off track, find the cause before changing it: often the outcome is right and the roadmap,
adoption or knowledge work behind it is wrong. Where an outcome has been met, decide whether to raise the target or
replace it with the next priority.

Test the principles against real decisions made since the last version. Were any principles bypassed, contested or
silent when they were needed? Incidents and difficult approvals are the best evidence. Adjust wording where a gap was
exposed, and check new regulatory obligations with the legal adviser and data protection officer.

Review the platform position last among the strategic elements, so that product change serves the outcomes rather
than driving them. Adjust postures only for confirmed changes, and record the source used.

Keep change proportionate. Most refreshes should adjust a few elements and keep the rest. If the refresh would change
everything, ask whether the organisation's purpose or leadership has changed; if not, the original strategy was
probably never properly adopted, and that is a different problem.

Publish a new version with a change log: what changed, why, on what evidence, and what it means for the roadmap,
investment case and operating model. Brief the sponsor first, then managers, then staff, so nobody learns of changed
priorities from a project being stopped.

## Outputs

- A refresh record: trigger, evidence considered, disposition for each strategy element with reasoning, and approval.
- A new strategy version with a change log, and updated `ai-vision-and-principles`, `ai-roadmap` and `investment-case` documents where affected.
- A list of consequential actions for the roadmap, investment case, operating model and portfolio, each with an owner.
- The next refresh date and triggers.

## Microsoft platform considerations

Microsoft changes names, packaging and capability frequently. Treat a change as relevant only when it is confirmed in a
current source record and affects a posture or roadmap item; preview features are noted but rarely change a posture.
Licensing changes are referred to the Microsoft licensing guide or a licensing partner, never interpreted here.

## Adoption considerations

Changed priorities unsettle people who invested in the old ones. Explain what changed and why, recognise work on
initiatives that are stopped, and route communications through `change-and-communications:ai-communication-strategy`.

## Knowledge considerations

Check whether knowledge ownership and readiness kept pace with the strategy. Persistent knowledge gaps are a common
cause of off-track outcomes; where found, raise them as a strategic constraint rather than a delivery issue.

## Security and privacy considerations

Include security and privacy incidents, audit findings and regulatory changes in the evidence. Changes to principles on
data use are checked with the security lead and data protection officer before publication.

## Responsible AI considerations

Review whether the principles and exclusions held up in practice, using incidents, escalations and risk acceptances
since the last version. The risk management and AI management system source records help structure the review.

## Evaluation requirements

Not applicable to solution testing. The refresh is checked by whether every changed element cites evidence and
whether the sponsor can explain each change in one sentence.

## Value measures

Report outcome movement since the last version, the share of strategy elements kept, adjusted or retired, and the
number of consequential actions closed by the next review. The AI strategy lead owns these. All measures are at
organisation, unit or team level.

## Scale notes

### Starter

An annual one-hour review with the sponsor using the disposition table, producing a short change log. Light quarterly
checks are folded into steering.

### Scale

A structured annual refresh with evidence prepared by the CoE, a re-run maturity assessment, and a quarterly light
check. Platform changes are summarised by the platform owners.

### Enterprise

The enterprise refresh is aligned with the corporate planning cycle; business units refresh their derived strategies
afterwards. A standing horizon-scanning role tracks Microsoft and regulatory change between refreshes.

## Hand-offs

- To `ai-strategy:ai-roadmap` to re-sequence work after the refresh.
- To `ai-strategy:investment-case` when funding or tranches must change.
- To `opportunity-management:portfolio-balancing` to rebalance the portfolio against changed outcomes.
- To `ai-strategy:ai-operating-model` when the refresh changes who decides, builds or supports AI.

## Reviewer gates

Not applicable. A strategy refresh is an executive decision, not a release. Changed principles may be referred to the
`responsible-ai` department for advice before approval.

## Failure modes

- The refresh is skipped because the programme is busy, and the strategy quietly stops guiding decisions.
- Every Microsoft announcement prompts a strategy change, and teams stop trusting priorities that keep moving.
- Off-track outcomes are replaced rather than diagnosed, hiding fixable delivery problems.
- The refresh rewrites everything, discarding lessons and leaving people unsure what was wrong with the old version.
- Changes are published without explaining what happens to work already under way.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Change an outcome or principle without recording the evidence and reasoning.
- Change a platform posture on the strength of a preview announcement or an unconfirmed product claim.
- Present opinion gathered in a workshop as measured evidence.
- Publish a refreshed strategy without telling the owners of affected initiatives first.
