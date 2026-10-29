---
name: benefit-realisation-plan
description: Plans how AI benefits will be realised over time - the benefits register, each benefit's profile by period, the enabling changes and decisions as milestones, measurement points, owners, review cadence, tolerances and closure rules - so value is tracked to closure rather than declared at launch. Use when a case is approved, when benefits have no dates or tracking, or when a portfolio needs one register and review rhythm.
license: CC-BY-4.0
metadata:
  department: value-realisation
  lifecycle: Mobilise, Deliver, Launch, Measure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, iso-iec-42001, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Benefit realisation plan

## Purpose

Approving a case is a promise; the realisation plan is how the organisation keeps it. This skill sets up the benefits
register and the plan around it: when each benefit should appear and grow, which enabling changes and decisions must
happen first, when each benefit is measured, who reviews it, what tolerance triggers action, and when a benefit is
closed or handed to business as usual. It goes wrong when benefits are declared at launch and never tracked, when the
plan schedules technology milestones but not the business changes that create value, and when the register becomes a
spreadsheet nobody opens between annual reports.

## When to use

- A business or investment case has been approved and its benefits need a plan and a register.
- Benefits exist on paper with no dates, measurement points or reviews.
- A portfolio of AI initiatives needs one register and one review rhythm.
- A sponsor asks when the promised value will actually appear.
- Benefits have slipped and the plan needs re-profiling with owners.

## When not to use

- Integrating workstream plans into one programme roadmap - use `programme-management:integrated-roadmap`.
- Writing the benefit statements that enter the register - use `value-realisation:benefit-hypothesis`.
- Assigning and supporting benefit owners - use `value-realisation:benefit-owner`.
- Reviewing results against the case after go-live - use `value-realisation:post-implementation-review`.
- Defining programme stage gates and their evidence - use `programme-management:stage-gates`.

## Questions to ask first

1. Which approved case or cases does the plan cover, and which benefits did they commit to?
2. Which business changes and decisions, beyond the technology, must happen before each benefit can appear?
3. When should each benefit first be visible, and when should it reach full level?
4. Which forum will review benefits, how often, and what can it decide?
5. What tolerance on each benefit should trigger escalation rather than a note?

## Required inputs

- Approved benefit statements and dependency maps from `value-realisation:benefit-hypothesis`.
- Owners agreed through `value-realisation:benefit-owner`.
- Baselines and measurement methods from `value-realisation:baseline-design` and the measurement skills.
- The delivery and rollout plan, and the assumption test dates from `value-realisation:roi-model`.
- The governance forums from `ai-centre-of-excellence:coe-cadence` or the programme board.

Where an input is missing, the benefit enters the register with its status set to "not ready" and the missing item
marked `[To confirm]` with a role and date. A benefit is not reported as on track until it has an owner, a baseline and
a measurement point.

## Decision framework

Each benefit in the register carries these elements before the plan is approved.

| Element | Content |
|---|---|
| Profile | Expected level by period from first appearance to full level, as a range |
| Enablers | Business changes and decisions (process change, redeployment, retirement of old tools, knowledge clean-up) with owners and dates |
| Measurement points | When and how the benefit is measured, using the agreed method and baseline |
| Review | The forum and frequency at which the benefit is reviewed |
| Tolerance | The variance that triggers escalation, agreed with the owner |
| Closure | When the benefit is closed, handed to business as usual or retired |

| Status | Meaning | Action |
|---|---|---|
| Not ready | Missing owner, baseline or measurement point | Complete before launch |
| On track | Within tolerance of the profile at the last measurement | Continue |
| At risk | Outside tolerance, or an enabler is late | Owner presents recovery actions at the next review |
| Off track | Outside tolerance with no agreed recovery | Escalate to sponsor; re-profile or retire |
| Realised | Full level reached and sustained over agreed periods | Close or hand to business as usual |
| Retired | No longer expected, with reason recorded | Remove from totals, keep the record |

## Practitioner approach

Build the register first, and make it the single source of truth. One row per benefit, with the statement, type,
class, owner, baseline, target range, profile, status and confidence. Use the `benefits-register` template and keep it
somewhere the organisation already works, with clear edit rights. Every report, dashboard and review reads from it;
nothing keeps its own copy.

Plan the business changes, not just the technology. For each benefit, take the dependency map and turn every enabler
into a milestone with an owner and date: the old template withdrawn, the review step redesigned, the decision on how
released capacity is used, the knowledge source cleaned. These are the milestones that create value, and they are the
ones technology-led plans leave out. Where an enabler belongs in the programme roadmap, link to it rather than
duplicating it.

Profile each benefit realistically. AI benefits usually ramp with adoption and often dip at first while people learn
and verify. Draw the expected curve by period as a range, starting when the enablers and adoption make it possible,
not on go-live day. A realistic profile prevents early panic and late surprise.

Set measurement points from the profile. Measure when a change is expected, not on an arbitrary calendar. Schedule the
assumption tests from the ROI model early, because finding out in month two that an adoption assumption was wrong is far
cheaper than finding out at the post-implementation review.

Agree tolerances and the review rhythm with owners. A benefit slightly behind profile in a noisy measure needs a note,
not an escalation; a benefit well outside tolerance needs recovery actions. Put benefits on the agenda of the forum that
can act, usually the value review, and make owners present their own benefits, supported by the Benefits Realisation
Lead.

Plan closure as carefully as start. Benefits should not stay open forever. Define when a benefit counts as realised,
usually full level sustained over an agreed number of periods, and who then tracks it as business as usual. Retire
benefits that will not appear, record why, and remove them from totals openly.

Finally, set the date of the post-implementation review in the plan at the point benefits should be visible, and give
the plan to the sponsor as a one-page timeline of benefits, enablers and reviews.

## Outputs

- A `benefits-register` with every benefit's statement, owner, baseline, target range, profile, status, confidence and closure rule.
- A benefit realisation plan: enabler milestones, measurement points, review cadence, tolerances and the post-implementation review date.
- A one-page benefits timeline for the sponsor.
- A register maintenance rule: who updates what, when, and with which evidence.

## Microsoft platform considerations

The register can be kept in a Microsoft list, a Dataverse table or a governed spreadsheet in SharePoint; choose what the
organisation already supports and can secure. Where Power Platform is used for reminders or approvals around reviews,
follow the organisation's environment and data policy. Check `references/sources.md` for current capabilities.

## Adoption considerations

Most enabler milestones involve people changing how they work. Align the benefit profile with the adoption plan and
reinforcement activity, and share at-risk benefits with the adoption lead early.

## Knowledge considerations

For benefits relying on grounded agents, include knowledge clean-up and ongoing review as enabler milestones with the
knowledge owner named, because knowledge decay quietly erodes realised benefits.

## Security and privacy considerations

The register holds team-level and financial information, not individual data. Restrict editing to owners and the
Benefits Realisation Lead, and keep supporting evidence with its source owner.

## Responsible AI considerations

Where benefits come from solutions that inform decisions about people, include the planned review of human oversight
as a milestone so that pressure to realise benefits does not erode safeguards.

## Evaluation requirements

Schedule quality measurement points beside benefit measurement points for any benefit with a quality guard, and align
them with the solution's re-evaluation schedule.

## Value measures

Success is the share of registered benefits with a complete plan before launch, the share reviewed at each scheduled
point, and the share closed as realised or retired with a record, tracked by the Benefits Realisation Lead.

## Scale notes

### Starter

A simple register of a handful of benefits, two or three enabler milestones each, measurement twice a year and one
review at the point benefits should be visible.

### Scale

A full register with profiles, tolerances and statuses, quarterly benefit reviews in the value review, and enablers
linked to the programme roadmap.

### Enterprise

A portfolio register with business-unit registers rolling up, shared status and tolerance rules, register data feeding
the value dashboard, and annual reconciliation with finance.

## Hand-offs

- To `value-realisation:value-dashboard` with the register as its data source.
- To `value-realisation:post-implementation-review` at the scheduled review date.
- To `programme-management:integrated-roadmap` with enabler milestones that belong in the programme plan.
- To `ai-centre-of-excellence:coe-cadence` to place benefit reviews on the value review agenda.

## Reviewer gates

Not applicable, because the realisation plan schedules and tracks benefits rather than releasing a solution. The
sponsor approves the plan and resolves escalations at the value review.

## Failure modes

- Benefits are declared at launch, never measured again, and cannot be shown at renewal.
- The plan schedules only technology milestones, and the business changes that create value never happen.
- Every benefit is profiled from go-live day at full level, and the first review finds them all off track.
- Dashboards and reports keep their own copies of figures, and the register stops being trusted.
- Benefits stay open indefinitely, so the register fills with stale entries and nobody can see what matters.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Report a benefit as on track without an owner, a baseline and a measurement point.
- Schedule benefits from go-live day without regard to enablers and adoption.
- Remove a benefit from the register without recording why.
- Keep benefit figures anywhere other than the register.
