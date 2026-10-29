---
name: knowledge-review-cycles
description: Sets how often each kind of knowledge is reviewed, what events trigger an early review, what a review must check and record, and how overdue reviews escalate, with reviews linked to the agents and Copilot scenarios that depend on the content. Use when content has no review dates, when reviews are agreed but never happen, or when a policy change is not reflected in AI answers.
license: CC-BY-4.0
metadata:
  department: knowledge-management
  lifecycle: Enable, Deliver, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: sharepoint, m365-agents, copilot-studio, power-platform
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-studio-guidance, ms-agent-builder
  status: draft
  authors: Simon Foote
---

# Knowledge review cycles

## Purpose

Knowledge decays quietly. A policy changes, a product is withdrawn, a team is restructured, and the old content stays
exactly where it was, now ready to be quoted by Copilot with full confidence. This skill sets review cycles that match
how fast each kind of content changes and how much a wrong answer would cost, adds event triggers so reviews happen
when the world changes rather than only on the calendar, and makes overdue reviews visible. It usually fails when
every document gets the same annual date, or when reviews are scheduled but nobody is prompted, recognised or chased.

## When to use

- Registered sources have no review dates, or the same date has been applied to everything.
- Reviews are agreed on paper but are not happening, and content is visibly stale.
- A policy, product or regulation changed and AI answers did not follow.
- New agents are about to ground on content and need a review cadence linked to their own review date.

## When not to use

- Keeping a specific live agent's knowledge current in operation, including re-indexing and re-testing - use `ai-operations:knowledge-refresh`.
- Scheduled reviews of live AI solutions themselves - use `ai-operations:ai-review-calendar`.
- Designing the whole lifecycle from creation to disposal - use `knowledge-management:knowledge-lifecycle`.
- Deciding what to remove from a backlog of stale content - use `knowledge-management:knowledge-cleanup`.

## Questions to ask first

1. What kinds of content are in scope (policy, procedure, product, reference, guidance), and how often does each genuinely change?
2. What is the consequence of an out-of-date answer for each kind - inconvenience, rework, or compliance and safety risk?
3. What events in the organisation should force an early review - regulatory change, policy approval, product launch, reorganisation?
4. Who carries out the review, how long does it take, and how are they prompted?
5. Which agents and Copilot scenarios depend on the content, and when are they reviewed?

## Required inputs

- The register of sources with owners and dependent AI uses, from `knowledge-management:knowledge-inventory`.
- The ownership model, from `knowledge-management:knowledge-owner-model`, so reviews have someone to do them.
- A list of change events the organisation recognises, from policy, legal, product and HR owners.
- Any regulatory or contractual review requirements, from the content owner or legal adviser.

Where a source has no owner, do not set a cycle against it: route it to ownership first, because a review date nobody
owns is decoration. Regulatory review periods are confirmed by the owner or legal adviser, never assumed.

## Decision framework

Set the cycle from volatility and consequence, then add triggers.

| Volatility \ consequence | Low (inconvenience) | Medium (rework, cost) | High (compliance, safety, people decisions) |
|---|---|---|---|
| High (changes monthly or with releases) | Quarterly | Quarterly | Monthly, plus event triggers |
| Medium (changes a few times a year) | Annually | Six-monthly | Quarterly, plus event triggers |
| Low (rarely changes) | Every two years or on event | Annually | Six-monthly, plus event triggers |

A review must record four things: confirmed accurate or updated, still needed or archived, audience and classification
still right, and the next review date. Overdue reviews escalate in steps: reminder to the owner at the due date, to the
deputy after a set interval, to the domain owner after a further interval; content that remains overdue on a high
consequence row is withdrawn from agent grounding until reviewed.

## Practitioner approach

Group content by kind before setting any dates. Most estates have a handful of content kinds that behave similarly:
policies, procedures, product and service information, reference material, guidance and templates. Agree a default
cycle per kind with the domain owners using the matrix, and let content owners shorten it for specific sources. Avoid
the single annual date for everything; it is too slow for product content and too frequent for stable reference, and it
teaches owners that review is a box to tick.

Add event triggers, because calendar reviews alone miss the moments that matter. List the events that should force a
review: a new policy approved, a regulation changed, a product launched or withdrawn, a reorganisation, an incident
caused by wrong content. For each, name who announces the event and how affected owners are told. A simple routine
where the policy approval step also notifies the owners of dependent sources prevents most "the agent still quotes the
old rule" incidents.

Make the review itself small and specific. A review is not a rewrite; it is a check against four questions, recorded
in metadata. Give owners a short checklist and a way to record the outcome in a minute or two, ideally in the library
itself. Where content is regulated or technical, include the subject matter reviewer.

Link content reviews to AI. Each source in the register lists the agents and scenarios that depend on it. When a
review changes content materially, the owners of dependent agents are told so they can re-test, through
`ai-operations:knowledge-refresh`. Agent review dates should never be later than the review dates of their sources.

Prompt, do not police. Automated reminders from the library or a simple flow, a monthly overdue list to domain owners,
and visible thanks for owners who keep content current work better than league tables. Report overdue reviews by
domain, never by individual.

Finally, decide what happens when reviews do not happen. For low-consequence content, overdue items are flagged. For
high-consequence content that informs AI answers, an overdue review removes the source from grounding until it is
reviewed. That rule needs the domain owner's agreement in advance, so it is a known consequence rather than a surprise.

## Outputs

- A review cycle standard: content kinds, default cycles, event triggers, the review checklist and the escalation steps.
- Review dates, triggers and dependent AI uses recorded against each source in the `knowledge-asset-register`.
- A reminder and escalation routine, with an overdue report by domain.

## Microsoft platform considerations

SharePoint columns can hold review dates, and reminders can be automated with Power Automate or built-in library
features where available; confirm current capabilities in the source records before designing around them. Changes to
SharePoint content may reach agents at different speeds depending on the grounding route, and uploaded files do not
update themselves, so dependent agents need an explicit refresh step.

## Adoption considerations

Owners keep reviewing when the effort is small and they see the effect. Show them which agents depend on their content
and share examples where a timely review prevented a wrong answer.

## Knowledge considerations

Review cycles are the maintenance engine of `knowledge-management:knowledge-lifecycle`; review outcomes feed
`knowledge-management:knowledge-cleanup` (archive decisions) and `knowledge-management:content-quality` (periodic
checks).

## Security and privacy considerations

Each review re-confirms audience and classification, catching access that has widened since the last review. Changes go
to the site administrator and, from risk tier 2, to `security-privacy:data-exposure-review`.

## Responsible AI considerations

High-consequence content that informs decisions about people needs the shortest cycles and event triggers, because an
outdated rule applied by AI to people is a harm, not an inconvenience.

## Evaluation requirements

Check the routine works: sample sources each quarter to confirm reviews happened when recorded and that dependent
agents were notified of material changes. Track the time between a change event and the update of affected content.

## Value measures

Track the share of AI-dependent sources with in-date reviews, the time from change event to updated content, and
wrong-answer reports traced to stale content. The Knowledge Manager owns these, reported by domain; never rank owners.

## Scale notes

### Starter

Set review dates for the sources the first agents use, with a calendar reminder and a single event trigger for policy
changes.

### Scale

Apply default cycles by content kind across the register, automate reminders and escalation, and link source reviews to
agent reviews.

### Enterprise

Integrate event triggers with policy, product and regulatory change processes across business units, and report review
health by domain to steering.

## Hand-offs

- To content owners and stewards to carry out reviews, under `knowledge-management:knowledge-owner-model`.
- To `ai-operations:knowledge-refresh` when a review materially changes content used by live agents.
- To `knowledge-management:knowledge-cleanup` when reviews conclude content should be archived.

## Reviewer gates

Not applicable as a release gate; review cycles maintain content rather than release solutions. The withdrawal rule for
overdue high-consequence content is agreed with domain owners and recorded.

## Failure modes

- One annual date for everything, so fast-changing content is stale for most of the year.
- Reviews rely on memory with no reminder, and quietly stop after the first cycle.
- Content changes after a review but dependent agents are never told, so answers stay wrong.
- Overdue reviews are reported by individual, owners feel monitored, and engagement drops.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Set a review cycle on a source that has no accepted owner.
- Assume a regulatory review period; confirm it with the owner or legal adviser.
- Report overdue reviews by individual or use them to judge performance.
- Let an agent's review date fall later than the review dates of the sources it grounds on.
