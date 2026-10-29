---
name: dependency-management
description: Manages the dependencies an AI programme relies on - between workstreams, on platform and tenant changes, on suppliers and partners, on other programmes and on Microsoft releases and retirements - each with a giver, receiver, need-by date, status and fallback, watched through a release watch. Use when milestones wait on others, when a Microsoft change could move the plan, or when a partner or IT team must deliver something first.
license: CC-BY-4.0
metadata:
  department: programme-management
  lifecycle: Mobilise, Enable, Deliver, Launch, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral, m365-copilot, copilot-studio, ai-foundry, power-platform, entra, purview
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-overview, ms-copilot-studio-guidance, ms-managed-environments, ms-foundry-models
  status: draft
  authors: Simon Foote
---

# Dependency management

## Purpose

AI programmes are unusually dependent on things they do not control: tenant configuration owned by IT, permissions
clean-up owned by content owners, partner deliverables, other programmes' data work and Microsoft's own release and
retirement schedule. This skill keeps a dependency register in which every dependency has a giver, a receiver, a
need-by date, an agreed status and a fallback, and runs a release watch so Microsoft changes are noticed before they
move the plan. Dependency management fails when dependencies are drawn on a plan but never agreed with the giver, when
Microsoft changes are discovered by users, and when every late dependency is escalated rather than negotiated.

## When to use

- Workstream milestones are waiting on other workstreams, IT teams, partners or other programmes.
- A milestone relies on a Microsoft capability, licence change, preview becoming generally available, or a retirement date.
- A partner or supplier must deliver something before the programme can move.
- A dependency has slipped and its receiver needs a fallback or a decision.
- Microsoft has announced a change and the programme needs to know what it affects.

## When not to use

- Building the integrated plan and critical path in the first place - use `programme-management:integrated-roadmap`.
- Recording risks and issues that are not dependencies - use `programme-management:programme-risk-log`.
- Managing the partner relationship and contract as a whole - use `programme-management:supplier-management`.
- Assessing how a change affects a specific live AI solution - use `design-authority:ai-change-impact-review`.
- Licensing and capacity questions about Microsoft AI - use `platform-governance:ai-licensing-and-capacity`.

## Questions to ask first

1. What does each workstream need from outside itself before its next milestones, from whom, and by when?
2. Has the giver agreed to provide it by that date, or has the receiver only assumed they will?
3. Which milestones rely on a Microsoft capability, licence term, preview or retirement, and which source record says so?
4. What would the receiver do if the dependency arrived late or not at all?
5. Who in IT or the CoE already watches Microsoft service communications, and can the programme use that route rather than create another?

## Required inputs

- The integrated plan and critical path from `programme-management:integrated-roadmap`.
- Supplier deliverables and dates from `programme-management:supplier-management` or the contracts.
- The list of Microsoft capabilities the plan relies on, with the source record checked for each.
- Access to the organisation's route for Microsoft service communications (usually the Message center in the Microsoft 365 admin center and the published Microsoft roadmap), held by IT or the platform team.

If the giver of a dependency is unknown, record it as `[To confirm: giver]` and treat it as a risk until someone accepts
it. Never record a dependency as agreed because the receiver expects it.

## Decision framework

Classify each dependency and manage it by class.

| Class | Examples | Managed through |
|---|---|---|
| Internal, between workstreams | Knowledge readiness before agent testing; scenarios before Champion learning | Workstream leads meeting |
| Internal, outside the programme | Tenant settings, identity, permissions clean-up, data platform work | Agreement with the owning team, escalation through the board |
| Supplier | Partner build, training delivery, ISV component | Supplier management and the contract |
| Other programme | Data platform, intranet, records management | Programme-to-programme agreement |
| Microsoft | Feature availability, licence change, preview status, retirement, admin control | Release watch, source records, fallback |

Rate each dependency by need-by date and confidence.

| Status | Meaning | Action |
|---|---|---|
| Agreed | Giver has accepted the date and scope | Monitor |
| At risk | Giver signals possible slippage or confidence is low | Agree a fallback; inform the receiver |
| Late | Need-by date passed or certain to be missed | Invoke the fallback or take a decision at the right forum |
| Unagreed | No giver has accepted it | Treat as a risk until agreed |

Escalate only when the receiver's milestone is on the critical path or beyond tolerance; negotiate everything else
between giver and receiver.

## Practitioner approach

Build the register from the integrated plan. For every milestone ask the owner what they need from outside their
workstream and write each answer as a dependency: what is needed, giver, receiver, need-by date. Then take every entry to
its giver and ask them to agree it. The conversation matters more than the register; most dependency failures happen
because the giver never knew the date mattered.

Give each dependency a fallback. If the permissions clean-up for a site is late, the agent can launch with a narrower
knowledge set; if the partner's build slips, the pilot can start with a smaller audience. Fallbacks turn a late dependency
into a decision rather than a crisis, and they are much easier to agree before the slip than after.

Treat Microsoft as a giver you cannot negotiate with. List every capability the plan relies on and record the source
record checked and its date. Agree with IT or the platform team how Microsoft service communications and roadmap changes
reach the programme: a short weekly scan of announced changes against the dependency list is usually enough. For each
relevant change, say which milestones it affects and whether it is an opportunity, a threat or neutral. Previews deserve
particular care; a plan that needs a preview capability in production rests on an assumption the programme cannot
control, and the fallback must be real.

Retirements and deprecations are dependencies too. If a capability a live solution uses is being retired, the programme
or the owning team has a dated piece of work; route the solution-level impact to the design authority and put the work
on the plan.

Review the register weekly with workstream leads, focusing on dependencies due in the next four to six weeks and anything
at risk on the critical path. Update status from the giver's view, not the receiver's hope. When a dependency is late,
decide at the lowest forum that can: re-sequence, invoke the fallback, or escalate with options.

At closure, hand ongoing release-watch responsibility to the CoE or platform team, with the list of live solutions and
the capabilities each depends on.

## Outputs

- A dependency register: description, class, giver, receiver, need-by date, status, confidence, fallback, linked milestone, source record for Microsoft dependencies, and last review date.
- A release watch log: Microsoft changes reviewed, date, affected milestones or solutions, assessment and action.
- Escalations to the programme board with options, where dependencies on the critical path are late.

## Microsoft platform considerations

Microsoft capabilities across Copilot, agents, Copilot Studio, Foundry, Power Platform, Entra and Purview change
frequently, including names, licensing, preview status and retirements. Rely on the organisation's service communications
route and the source records in `references/sources.md`, recording the date checked. Model availability and retirement in
Foundry follow the model lifecycle described in the source records; plan for model changes as dependencies of any Foundry
solution.

## Adoption considerations

Adoption milestones depend on things outside the adoption team: licence assignment, technical readiness, support routes
and communications approval. Record these as dependencies with givers so launches are not announced before they can
happen.

## Knowledge considerations

Knowledge owners are often the most overlooked givers. Agree content clean-up and review dates with them directly, and
give the knowledge dependency a fallback such as a narrower first release.

## Security and privacy considerations

Security configuration, sensitivity labels and permissions remediation are common dependencies for agent and Copilot
work. Agree them with the security and IT teams, and never bypass a security dependency to keep a date.

## Responsible AI considerations

Not applicable in depth, because dependencies are a delivery mechanism; where a fallback would change who is affected by
a solution or how much it decides, route the change through `opportunity-management:risk-classification`.

## Evaluation requirements

Not applicable to the register itself; a model or platform change that affects a live solution triggers regression
evaluation through `evaluation-quality:regression-evaluation`.

## Value measures

Track the share of dependencies agreed by their giver, dependencies delivered by their need-by date, and Microsoft changes
identified before they affected the plan, reported by the AI Programme Manager at programme level.

## Scale notes

### Starter

A short list of the dependencies that matter, mostly on IT, a partner and Microsoft, reviewed monthly, with the partner or
IT lead watching announced changes.

### Scale

A full register with agreed givers and fallbacks, weekly review, and a weekly release watch shared with the CoE and
platform team.

### Enterprise

Registers per tranche with cross-programme agreements, a release watch run once by the platform team for all programmes,
and dependencies on shared platforms visible at the portfolio board.

## Hand-offs

- To `programme-management:integrated-roadmap` when a dependency moves a milestone.
- To `programme-management:programme-risk-log` for unagreed or at-risk dependencies that become risks or issues.
- To `programme-management:supplier-management` for supplier dependencies that need contract action.
- To `design-authority:ai-change-impact-review` when a Microsoft change affects a live solution.

## Reviewer gates

Not applicable, because the register releases no solution; a fallback that changes a solution's scope, knowledge or
audience returns it to the gates set by its risk tier, including `security-privacy` from tier 2.

## Failure modes

- Dependencies are drawn on the plan but never agreed with the giver.
- The programme learns about a Microsoft change from users after it has happened.
- A plan relies on a preview capability with no real fallback.
- Every late dependency is escalated, and the board becomes a dependency negotiation forum.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Record a dependency as agreed without the giver's acceptance.
- Assume Microsoft availability, licensing or retirement dates from memory.
- Bypass a security or privacy dependency to protect a date.
- Leave a dependency on the critical path without a fallback.
