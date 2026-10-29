---
name: programme-board-cadence
description: Sets the governance rhythm of an AI programme - programme board, workstream leads meeting, design and change forum and sponsor checkpoints - with terms of reference, reporting flow, paper deadlines and a programme decision log, aligned with the CoE's forums rather than duplicating them. Use when a chartered programme needs its meetings set up, when the board has become a status briefing, or when programme decisions cannot be traced.
license: CC-BY-4.0
metadata:
  department: programme-management
  lifecycle: Mobilise, Deliver, Measure
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral, m365-copilot
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# Programme board cadence

## Purpose

A programme needs a small number of forums that take decisions on time, and a record of those decisions that anyone can
find later. This skill sets the programme's governance rhythm: the programme board, the workstream leads meeting, a
design and change forum where needed, and sponsor checkpoints, each with terms of reference, inputs, deadlines and a
decision log. It aligns these forums with the AI CoE's standing cadence so the same people are not asked the same
questions twice. Programme cadences fail when boards become status briefings, when papers arrive on the morning of the
meeting, and when decisions live only in people's memories.

## When to use

- A programme has been chartered and needs its forums and reporting flow set up.
- The programme board has become a status update that decides nothing.
- Decisions are being re-opened because nobody can find what was agreed or why.
- A CoE already meets and the programme risks running a parallel set of meetings with the same people.
- A programme is moving into a new stage and its governance needs to change weight.

## When not to use

- The CoE's own standing forums (working group, steering, strategy review, community) - use `ai-centre-of-excellence:coe-cadence`.
- Agreeing who holds which decision rights and how escalation works across stakeholders - use `programme-management:stakeholder-governance`.
- Writing the programme's mandate, scope and tolerances - use `programme-management:programme-charter`.
- Recording risks, assumptions, issues and the decisions that resolve them - use `programme-management:programme-risk-log`.
- Producing the health report the board reviews - use `programme-management:programme-health`.

## Questions to ask first

1. What decisions does the charter give the programme board, and what does the sponsor reserve?
2. Which forums already exist (CoE steering, IT change board, architecture board, executive committee) and which programme decisions belong there instead?
3. Who must attend for the board to be quorate, and how much time can they give?
4. How fast must decisions be taken to keep the critical path moving?
5. Where will papers, minutes and the decision log be stored, and who may see them?

## Required inputs

- The signed charter from `programme-management:programme-charter`, with decision rights and tolerances.
- The CoE cadence from `ai-centre-of-excellence:coe-cadence`, where a CoE exists.
- The integrated plan from `programme-management:integrated-roadmap`, showing gate dates and the critical path.
- Declared roles from `organisation-tailoring:ownership-map`.

If the charter does not say which decisions the board takes, stop and resolve that first; a cadence without decision
rights produces meetings, not governance.

## Decision framework

Create a forum only where it has decisions only it can take. Lengths and frequencies are starting points to adjust.

| Forum | Typical rhythm | Inputs | Decides |
|---|---|---|---|
| Programme board (sponsor or delegate chairs) | Monthly, 60 to 90 minutes | Health report, exceptions, gate submissions, change requests | Changes within the sponsor's delegation, gate outcomes, re-baselines, escalated risks |
| Workstream leads meeting | Weekly or fortnightly, 30 to 45 minutes | Milestones due, dependencies, new risks and issues | Re-sequencing within tolerance, dependency resolution, what to escalate |
| Design and change forum | Fortnightly or on demand | Change requests, design questions crossing workstreams | Changes below board tolerance, design choices to refer to `design-authority` |
| Sponsor checkpoint | Monthly, 20 minutes before the board | Exceptions and reserved decisions | Reserved decisions, board agenda |

Align with the CoE by edition.

| Edition | Arrangement |
|---|---|
| Starter | No separate board; a programme slot at the AI working group with the sponsor present |
| Scale | Programme board separate from CoE steering, meeting in the same week, with shared members and a single combined pack where agendas overlap |
| Enterprise | Programme board per tranche reporting to a portfolio or executive board; CoE hub steering receives programme decisions for standards it owns |

Each forum passes three tests: decisions only it can take, papers circulated at least two working days ahead, and
decisions published within two working days. A forum failing all three is merged or stopped.

## Practitioner approach

Begin with the decisions, not the diary. List every decision the charter gives the programme: gate outcomes, changes to
scope or dates beyond tolerance, risk responses, supplier changes, re-baselines. Assign each to the lowest forum that can
take it. Only then decide how often each forum meets; frequency follows decision volume and the pace of the critical
path.

Map the existing forums before adding any. In most organisations an AI programme overlaps with the CoE steering group,
an IT change board and an architecture or design board. Route decisions to the forum that already owns them: solution
release standards to the CoE, platform changes to IT change, architecture to `design-authority`. The programme board
keeps the decisions about the programme itself. Say this in the terms of reference so nobody has to guess.

Set the reporting flow backwards from the board date. Workstream leads update milestones, risks and dependencies at the
weekly meeting; the programme manager prepares the health report and exceptions; the sponsor sees exceptions at a short
checkpoint; papers go out two working days before the board. Reporting by exception keeps the board on decisions: a
workstream on track gets one line, a workstream breaching tolerance gets a paper with options.

Keep one programme decision log. Each entry records the decision, the options considered, who decided, the date, the
forum and the evidence or paper behind it. Link each decision to the risk, issue or change it resolves. A decision log
that only says "agreed" is useless six months later; one that says why is the programme's memory.

Write short terms of reference for each forum: purpose, decisions, chair, members by role, quorum, inputs, frequency and
how decisions are published. Review them at each stage gate. As the programme moves from mobilisation into delivery and
then into handing over to the CoE, the weight of governance should change; a board that still meets monthly with
nothing to decide is a sign the programme should be closing.

Teams meetings with Copilot can help draft minutes and capture actions, but a person confirms each decision in the log;
generated recap text is a draft, not the record.

## Outputs

- Terms of reference for each programme forum: purpose, decisions, chair, members by role, quorum, inputs, frequency and publication, recorded in the governance section of the `programme-charter` template.
- A forum map showing which decisions go to the programme board and which to existing forums, including the CoE.
- A reporting calendar with paper deadlines, sponsor checkpoints and gate dates.
- A programme decision log with its fields and first entries.

## Microsoft platform considerations

Teams, SharePoint and Planner or Loop are common places to hold papers, the decision log and actions. If Copilot is used
to draft minutes, check what is recorded and retained against the organisation's policy and the source records in
`references/sources.md`; meeting recordings and transcripts may carry retention and privacy obligations.

## Adoption considerations

Include an adoption lead and a business owner on the board so adoption progress and blockers are discussed alongside
build. Use the board's own use of Copilot for papers and summaries as a visible example of approved practice.

## Knowledge considerations

The decision log and papers are programme knowledge. Store them where the CoE can find them after the programme closes,
with an owner and a retention period agreed with records management.

## Security and privacy considerations

Board papers may include risk, supplier and security information; restrict access to members and the programme office.
If meetings are recorded or transcribed, confirm the lawful basis and retention with the DPO before relying on them.

## Responsible AI considerations

Reserve risk acceptance for tier 3 and 4 solutions to the accountable executive named in the charter, not to a workstream
meeting. Record each acceptance in the decision log with the `responsible-ai` review it relied on.

## Evaluation requirements

Not applicable, because the cadence governs the programme rather than an AI solution; gate decisions at the board rely on
evaluation evidence produced through `evaluation-quality`.

## Value measures

Measure decision latency (time from a decision being needed to it being taken), the share of board items that are
decisions rather than updates, and attendance by role, reported by the AI Programme Manager. Never report individual
attendance as a performance measure.

## Scale notes

### Starter

A standing programme item at the monthly AI working group, a simple decision log in a shared list, and a fortnightly
check-in between the lead and the sponsor's delegate.

### Scale

A monthly programme board, a weekly workstream meeting, a design and change forum when needed, and a combined pack with
CoE steering where membership overlaps.

### Enterprise

Tranche boards reporting to a portfolio board, a programme office running the reporting calendar, and explicit interfaces
with CoE hub steering, IT change and the design authority.

## Hand-offs

- To `programme-management:stakeholder-governance` for decision rights and escalation routes the cadence relies on.
- To `programme-management:programme-health` for the report the board receives.
- To `programme-management:stage-gates` for gate submissions the board decides.
- To `ai-centre-of-excellence:coe-cadence` when standing forums should absorb programme governance at closure.

## Reviewer gates

Not applicable, because forums release no solution; the board must not overturn a blocking finding from
`security-privacy`, `responsible-ai`, `evaluation-quality` or `design-authority`, which escalates to the accountable
executive for written risk acceptance instead.

## Failure modes

- The board hears status updates for an hour and defers every decision.
- Programme and CoE forums run in parallel with the same people and contradict each other.
- Decisions are recorded as "agreed" with no rationale, and are re-opened every quarter.
- AI-generated meeting recaps are treated as the record without a person confirming them.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Create a forum that has no decisions only it can take.
- Let the programme board override a blocking reviewer finding.
- Treat an AI-generated recap as the decision record without human confirmation.
- Report individual attendance or contribution as a measure of people.
