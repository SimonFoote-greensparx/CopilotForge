---
name: backlog-management
description: Sets up and operates the AI opportunity backlog as one visible board - choosing the tool, defining stages with entry and exit rules, mandatory fields per stage, work-in-progress limits, ageing rules, merges, archiving and a regular hygiene routine - so it stays the single route to resources. Use when there is no backlog or several competing lists, when the board is stale or cluttered, or when nobody trusts its status fields.
license: CC-BY-4.0
metadata:
  department: opportunity-management
  lifecycle: Mobilise, Deliver, Measure
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: sharepoint, power-platform, m365-copilot, github
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-coe-starter-kit, ms-copilot-studio-guidance
  status: draft
  authors: Simon Foote
---

# Backlog management

## Purpose

This skill runs the opportunity backlog as a working tool rather than a list nobody trusts. It sets up one board with
clear stages, entry and exit rules, mandatory fields and limits on work in progress, and keeps it clean through a
regular hygiene routine, so that the board remains the single route to resources and anyone can see where an idea
stands. Backlogs usually go wrong by multiplying (every unit keeps its own spreadsheet), by filling with stale entries
nobody dares close, or by carrying status fields that were last updated months ago, at which point leaders stop
believing it and decisions move back to corridors.

## When to use

- There is no backlog, or several competing lists of AI ideas and projects.
- A CoE or programme is launching and needs its board set up.
- The board is cluttered with stale or duplicate entries, and statuses cannot be trusted.
- Items are stuck in a stage with nobody noticing.
- Leaders ask for a view of the pipeline and nobody can produce one quickly.

## When not to use

- Designing the route by which staff submit ideas - use `opportunity-management:idea-capture`.
- Scoring and ranking entries - use `opportunity-management:opportunity-prioritisation`.
- Rebalancing the mix of work across the portfolio - use `opportunity-management:portfolio-balancing`.
- Keeping the register of live agents, flows and solutions - use `platform-governance:ai-solution-inventory`.
- Running the CoE's portfolio of live and planned solutions - use `ai-centre-of-excellence:coe-portfolio-management`.

## Questions to ask first

1. Where are AI ideas and projects tracked today, and which list do leaders actually use?
2. Who owns the board, and how much time do they have to maintain it?
3. Which collaboration tools does the organisation already use and support?
4. Who needs to see the board, and who needs to edit it?
5. How will business units and the CoE share one board without losing local control?

## Required inputs

- The opportunity lifecycle stages agreed in `opportunity-management:opportunity-prioritisation`.
- The canvas fields from the `opportunity-canvas` template, so entries link to their records.
- A named backlog owner (usually the AI portfolio manager) and agreed maintenance time.
- The collaboration tools available and supported in the organisation.

Where existing lists hold entries with missing owners or problems, migrate them into the capture stage with the gap
recorded. Never invent an owner, value or status to make an entry look complete.

## Decision framework

Use the five lifecycle stages from `opportunity-management:opportunity-prioritisation`, and set the rules for each.

| Stage | Mandatory fields to enter | Exit rule | Ageing alert |
|---|---|---|---|
| Capture | Reference, originating team, request, date | Business owner and framed problem recorded | No movement for a few weeks |
| Assessment | Owner, problem, outcome, baseline plan, suitability, risk tier | Value range, effort range and priority recorded, decision taken | Waiting for an owner or baseline beyond the agreed period |
| Delivery | Priority, effort, value, return estimate, build owner, target gate dates | Passes release gates | Past a target gate date |
| Live | Release date, registered in the solution inventory, owners | Benefits measurement started | No measurement after the agreed period |
| Value tracking | Measure, baseline, review date | Scale-or-stop decision recorded | Past review date |

Set work-in-progress limits on assessment and delivery, sized to the capacity of the people who do that work. When a
stage is full, nothing new enters until something leaves.

Choose the tool by what the organisation already supports.

| Tool | Fits when |
|---|---|
| SharePoint list or Microsoft Lists | Most organisations; good permissions, views and forms, low maintenance |
| Planner board | Small programmes wanting a visual board with little configuration |
| Dataverse table with a model-driven or canvas app | Volumes are high, approvals or reporting need automation, and Power Platform skills exist |
| Work-tracking tool already used for engineering (for example Azure Boards or GitHub issues) | The CoE is engineering-led and business users can still see the board |

## Practitioner approach

Consolidate first. Gather every existing list, spreadsheet and tracker, and agree with the sponsor that from a set date
there will be one board and that nothing is resourced unless it is on it. Migrate old entries into the capture stage
with their gaps noted. Expect resistance from teams who like their own lists; the answer is a filtered view of the
shared board for each unit, not a separate list.

Keep the board simple. Use the five stages, the mandatory fields and a small number of optional fields. Every extra
field is a field that will go stale. Link each entry to its canvas and other records rather than copying their
content into the board.

Set the hygiene routine and protect it. A weekly half-hour review by the backlog owner checks new entries, ageing
alerts, missing fields and work-in-progress limits. A monthly review with the CoE checks duplicates and merges, closes
dead entries with a reason, and prepares the views for steering. Status updates are the responsibility of the entry
owner, prompted by the backlog owner; the board owner should not be guessing status.

Close entries deliberately. Every closed entry has a closure reason (delivered, routed to adoption, merged, declined,
stopped after review, withdrawn) and a note for the originator. Archive closed entries rather than deleting them;
later reviews and post-implementation reviews need the history.

Publish standard views: by stage for the CoE, by outcome for the sponsor, by unit for business leaders, and an ageing
view for the hygiene review. Make the board readable by anyone with an interest, and editable only by those who own
entries or run the process.

Automate sparingly. Reminders for ageing items and a weekly digest are worth building; elaborate approval workflows
usually are not until volumes demand them. If you build automation or an agent on the backlog, treat it as a small
solution with an owner.

Review the board's design every quarter. If a field is never used, remove it. If entries regularly stall at the same
stage, the problem is usually capacity or ownership at that stage, and the portfolio review should hear about it.

## Outputs

- A backlog design: tool, stages, entry and exit rules, mandatory fields per stage, work-in-progress limits, ageing alerts, views and permissions.
- The live backlog register, aligned with the `prioritisation-matrix` template fields.
- A hygiene routine: weekly and monthly checks, owners and closure reasons.
- A quarterly backlog health note: entries by stage, ageing items, duplicates merged and closures by reason.

## Microsoft platform considerations

SharePoint lists suit most organisations because permissions, forms and views are already understood. Dataverse with a
Power Apps front end suits higher volumes or automated reporting, but becomes a solution needing an owner and an
environment. Engineering boards suit engineering-led teams if business users can see them. Check current features and
licensing against `references/sources.md` before committing to a tool.

## Adoption considerations

The board is visible evidence that ideas are taken seriously. Make sure originators can see their idea's stage, and
use the board in CoE community sessions to show flow and outcomes.

## Knowledge considerations

Not applicable to the board itself. The board should, however, record knowledge dependencies for each entry so that
knowledge owners can see the demand on them.

## Security and privacy considerations

Entries may describe sensitive processes or contain personal data. Restrict editing, avoid personal data in free-text
fields, and agree retention of archived entries with the data protection officer.

## Responsible AI considerations

Record the risk tier and any responsible AI conditions on each entry so that tier 3 and tier 4 work is visible at a
glance and cannot move to delivery without its required reviews.

## Evaluation requirements

Not applicable to solution testing. The board is checked by its health measures: share of entries with complete
mandatory fields, ageing items and the time from capture to decision.

## Value measures

Measure entries by stage, time in each stage, share of entries with complete fields, ageing items resolved and closures
by reason. The backlog owner reports these monthly. Never report entries or ageing by named individual.

## Scale notes

### Starter

A single SharePoint list with the five stages, a weekly fifteen-minute review and a monthly view for the sponsor.

### Scale

One board for the organisation with unit views, work-in-progress limits, automated ageing reminders and a monthly
hygiene review at the CoE.

### Enterprise

Business units run filtered views of a shared board, or local boards feeding one enterprise view through common fields.
The hub owns the field definitions and checks cross-unit duplicates.

## Hand-offs

- To `opportunity-management:opportunity-prioritisation` for entries ready for scoring.
- To `opportunity-management:portfolio-balancing` with stage, ageing and capacity signals.
- To `platform-governance:ai-solution-inventory` when an entry goes live.
- To `opportunity-management:scale-or-stop` for entries past their review date.

## Reviewer gates

Not applicable. The backlog records and routes work; it does not release anything. Its fields show which reviewer gates
each entry must pass under its risk tier.

## Failure modes

- Units keep private lists alongside the board, and resources flow to work leaders cannot see.
- Status fields are updated by the board owner from memory, and the board stops being trusted.
- Stale entries are never closed, so the board looks like a graveyard and nobody uses it.
- Fields multiply until nobody completes them.
- Work-in-progress limits are ignored, everything is in delivery, and nothing finishes.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Allow work to be resourced that is not on the board.
- Delete closed entries instead of archiving them with a reason.
- Fill missing owners, values or statuses with guesses.
- Report backlog activity or ageing by named individual.
