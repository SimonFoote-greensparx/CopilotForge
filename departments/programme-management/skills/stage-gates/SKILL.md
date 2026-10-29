---
name: stage-gates
description: Defines the stage gates of an AI programme along the CopilotForge lifecycle - from mobilisation through enablement, delivery, launch and scale to closure - with the evidence each gate needs, who signs it off, how reviewer findings carry into it, and the outcomes go, conditional go, hold or stop. Use when a programme needs control points, when gates have become ceremonies, or when a sponsor asks what must be true before the next stage.
license: CC-BY-4.0
metadata:
  department: programme-management
  lifecycle: Mobilise, Enable, Deliver, Assure, Launch, Measure, Scale
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: security-privacy, responsible-ai, evaluation-quality, design-authority
  sources: nist-ai-rmf, iso-iec-42001, ms-copilot-adoption-hub, ms-copilot-studio-guidance
  status: draft
  authors: Simon Foote
---

# Stage gates

## Purpose

A stage gate is the point at which a programme stops to ask whether it should continue, change or stop, on evidence. This
skill defines the programme's gates along the CopilotForge lifecycle, the evidence each one needs, who signs it off, how
reviewer findings from solution gates feed into it, and what each possible outcome means. Programme gates are not
solution release gates: they decide whether the programme moves to its next stage, and they rely on solution gates
having done their work. Gates go wrong when they become ceremonies that always say go, when evidence is a slide of
assertions, and when a blocking reviewer finding is traded off against a date.

## When to use

- A programme has been chartered and needs control points agreed with the sponsor.
- The sponsor asks what must be true before the programme launches, scales or closes.
- Existing gates have become ceremonies with no evidence and no real choice.
- A programme is moving to a new stage (from pilot to scale-out, for example) and the decision needs a structure.
- Reviewer departments ask how their findings are reflected in programme decisions.

## When not to use

- Releasing an individual agent to its audience - use `m365-agents:agent-release-readiness`.
- Setting the release policy for AI solutions by risk tier - use `platform-governance:ai-release-policy`.
- Assembling the evaluation evidence pack for a solution - use `evaluation-quality:ai-release-evidence`.
- Deciding whether a single pilot should scale, iterate, pivot or stop - use `opportunity-management:scale-or-stop`.
- Reporting programme health between gates - use `programme-management:programme-health`.

## Questions to ask first

1. Which stages does this programme pass through, and which ones carry real choices for the sponsor?
2. Who holds the gate decision at each stage, and what does the charter allow them to decide?
3. Which solution-level gates (security, privacy, responsible AI, evaluation, design authority) will the programme's solutions pass, and from which risk tier?
4. What evidence already exists or is produced by workstreams, so gates can reuse it rather than demand new papers?
5. What would a stop or hold mean in practice for people, suppliers and live solutions?

## Required inputs

- The programme charter with stages, decision rights and tolerances.
- The integrated plan, so gates sit at real points in time.
- The risk tiers of the programme's solutions and the reviewer gates they trigger, from `opportunity-management:risk-classification`.
- The health report and risk log, which every gate reads.

If a gate's decision owner or evidence is not agreed, mark it `[To confirm: ...]` and resolve it before the gate date,
not at the gate.

## Decision framework

Use gates aligned to the CopilotForge lifecycle. Not every programme needs all of them.

| Gate | Sits between | Key question | Core evidence |
|---|---|---|---|
| G1 Mobilise | Envision and Mobilise | Is this worth mobilising as a programme? | Outcomes, charter draft, edition and archetype, funding route, sponsor |
| G2 Enable | Mobilise and Enable | Are foundations ready to start? | Signed charter, integrated plan, owners, governance, approved-use guidance, risk log |
| G3 Deliver | Enable and Deliver | Can delivery start safely at the planned pace? | Readiness assessments, reviewer capacity, knowledge readiness, supplier mobilisation |
| G4 Launch | Assure and Launch | Is the programme ready to put solutions and change in front of people? | Solution gate outcomes, support route, communications, baselines captured |
| G5 Scale | Measure and Scale | Should the programme extend to more people, units or solutions? | Measured value against baseline, adoption by team, quality, cost, scale-or-stop decisions |
| G6 Close | Improve and closure | Can the programme hand over and close? | Closure criteria met, owners and review dates for live solutions, transfer of open items |

Gate outcomes.

| Outcome | Meaning |
|---|---|
| Go | Evidence complete; proceed |
| Conditional go | Proceed with named conditions, owners and dates; conditions cannot include unresolved blocking findings |
| Hold | Evidence incomplete or a blocking finding open; reconvene on a date |
| Stop or re-scope | Evidence shows the stage should not proceed as planned; record the decision and its effect |

Rule: any open blocking finding from `security-privacy`, `responsible-ai`, `evaluation-quality` or `design-authority`
on a solution included in the gate's scope means that solution cannot pass, whatever the date. The gate may pass the rest
of the scope without it.

## Practitioner approach

Decide which gates the programme needs. A Starter adoption programme may need only G2, G4 and G6; a transformation
programme at Scale or Enterprise will use most of them. Put each gate on the integrated plan with a date, a decision
owner and the forum that will take it. Agree with the sponsor what each gate is for: a gate exists to make a choice
possible, and a gate where stopping is unthinkable is not a gate.

Define evidence as artefacts that already exist. G4 evidence for an agent-heavy programme is the release readiness
records from `m365-agents:agent-release-readiness`, the reviewer outcomes, the support route and the baselines captured,
not a new slide deck summarising them. Give each evidence item an owner and a standard ("baseline captured and agreed by
the business owner"), so the gate can check it rather than discuss it.

Keep the boundary with solution gates clear. Solution gates release individual agents, automations or engineered
solutions, by risk tier. Programme gates decide whether the programme moves on, using the solution gate outcomes as
evidence. Programme gates never re-review a solution and never override a reviewer's classification. When a solution
has an open blocking finding, the programme gate excludes it or holds; disagreement goes to the accountable executive for
written risk acceptance where policy allows, never to the gate chair.

Prepare gates in advance. Two weeks before, the programme manager checks the evidence list with owners and flags gaps.
One week before, a short pre-gate review sorts gaps into those that will close in time, those that become conditions,
and those that mean hold. The gate meeting itself should then be about the choice.

Record each gate decision in the decision log with the evidence relied on, the outcome, conditions with owners and dates,
and dissent where it existed. Follow up conditions at the next board. A conditional go whose conditions are never checked
teaches everyone that gates do not matter.

Treat G5 as the most important gate in AI programmes. Scaling a solution or a rollout multiplies cost, risk and support
load, so it needs measured value against a baseline, adoption by team or role, quality from evaluation, and the cost of
scaling, taken together. Where evidence is weak, a hold is the right answer.

## Outputs

- A gate plan: gates in use, timing, decision owner and forum, key question, evidence list with owners and standards.
- Gate evidence checklists, and the gate decision record with outcome, conditions, owners, dates and dissent.
- A gate section in the `programme-charter` template and gate status in the `programme-health-report` template.

## Microsoft platform considerations

Evidence that relies on a platform capability, licence position or admin control records the source record checked and
the date. For G3 and G4, confirm that environments, data and connector policies and admin controls the solutions rely on
are in place, using `references/sources.md` for current product facts.

## Adoption considerations

G4 must include adoption evidence (scenarios, Champions, communications, support) as well as technical readiness, and G5
must include adoption by team or role. Launch gates that check only technology produce launches nobody uses.

## Knowledge considerations

For agent and Cowork work, knowledge readiness verdicts are G3 and G4 evidence. A gate cannot pass an agent whose sources
are not ready.

## Security and privacy considerations

The `security-privacy` gate applies to solutions from risk tier 2 and is blocking. The programme gate records the
reviewer's outcome as given and never downgrades it. Data protection questions arising at a gate go to the DPO or legal
adviser.

## Responsible AI considerations

Tier 3 and 4 solutions need the `responsible-ai` review outcome and any risk acceptance by the accountable executive as
gate evidence. Some uses should stop at a gate; record that outcome plainly as a success of governance.

## Evaluation requirements

From tier 2, gate evidence includes the evaluation results and thresholds agreed with the business owner, from
`evaluation-quality`. G5 adds regression evidence where solutions have changed since launch.

## Value measures

Track gate predictability (gates held on the planned date with evidence complete), conditions closed by their date, and
the share of gates with a real hold or stop option exercised over time, reported at programme level. A programme where
every gate is a go deserves scrutiny.

## Scale notes

### Starter

Two or three light gates taken by the sponsor at the working group, each with a one-page checklist and a decision note.

### Scale

Four to six gates on the integrated plan, evidence checklists with owners, pre-gate reviews, and decisions at the
programme board.

### Enterprise

Gates per tranche and business unit, with a programme-level G5 and G6 at the portfolio board and formal evidence where
the assurance overlay is formal.

## Hand-offs

- To `programme-management:programme-board-cadence` for gate decisions and the decision log.
- To `programme-management:programme-health` for gate status between gates.
- To `opportunity-management:scale-or-stop` for solution-level scale decisions feeding G5.
- To `m365-agents:agent-release-readiness` and `platform-governance:ai-release-policy` for solution release.

## Reviewer gates

`security-privacy` from risk tier 2, and `evaluation-quality`, `design-authority` and `responsible-ai` from the tiers
those departments set, provide evidence into programme gates. Each finding keeps the reviewer's blocking or advisory
classification; a blocking finding stops the affected solution at the gate and is not traded off against a date.

## Failure modes

- Gates are ceremonies where stopping is unthinkable, so every outcome is go.
- Evidence is a slide of assertions rather than the artefacts the workstreams produce.
- A programme gate passes a solution with an open blocking finding to protect a launch date.
- Conditions from a conditional go are never followed up.
- G5 is skipped because a pilot "went well", and scaling multiplies an unmeasured cost.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Pass a solution with an open blocking reviewer finding.
- Re-review or reclassify a solution's reviewer findings at a programme gate.
- Hold a gate without an agreed decision owner and evidence list.
- Accept a stage outcome on assertion where the gate requires evidence.
