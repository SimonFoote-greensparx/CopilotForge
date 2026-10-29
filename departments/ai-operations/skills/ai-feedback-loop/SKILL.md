---
name: ai-feedback-loop
description: Runs the feedback loop for live agents and AI solutions - collecting in-product ratings, comments, support tickets and Champion reports, triaging them by cause to knowledge, instruction, scope or training owners, acting on themes, and telling users what changed. Use when a solution goes live, when feedback piles up unread, or when users say nothing happens after they report a problem.
license: CC-BY-4.0
metadata:
  department: ai-operations
  lifecycle: Measure, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-studio, copilot-cowork, ai-foundry, power-platform
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-studio-guidance, ms-agent-builder, ms-copilot-privacy, ms-copilot-adoption-hub, ms-champion-best-practice
  status: draft
  authors: Simon Foote
---

# AI feedback loop

## Purpose

Users are the largest test team any AI solution will ever have, but only if their feedback reaches someone who can act
on it and they can see that it did. This skill sets up how feedback on a live solution is collected, triaged by cause,
turned into fixes and improvements, and reported back to users. Feedback loops usually fail at one of two points:
ratings and comments are collected and never read, or they are read but routed to the maker for everything, so
knowledge problems are patched in instructions and training problems are treated as defects.

## When to use

- A solution is going live and needs a way to hear from its users.
- Feedback is being collected but nobody reviews it on a regular cycle.
- Users say they reported problems and nothing changed.
- The owner wants to know what to improve next and has no evidence beyond anecdotes.

## When not to use

- Handling a single serious failure or harm - use `ai-operations:ai-incident-management`.
- Day-to-day user support for a solution - use `ai-operations:ai-support-model`.
- Using Copilot Studio analytics to improve an agent's topics and conversations - use `copilot-studio:studio-analytics`.
- Measuring Copilot adoption across the organisation - use `copilot-adoption:adoption-measurement`.
- Gathering feedback from Champions about their programme - use `champions:champion-metrics`.

## Questions to ask first

1. Where will users give feedback - inside the solution, through support, through Champions or managers - and is each route visible?
2. Who reads feedback, how often, and with what authority to act?
3. Which causes can owners fix - knowledge, instructions, scope, actions, training - and who owns each?
4. How will users hear what changed as a result of their feedback?
5. What personal or sensitive content might appear in feedback, and how will it be handled?

## Required inputs

- The support plan with named roles, from `ai-operations:ai-support-model`.
- The feedback features the route offers, confirmed in the current source records.
- The known limits statement from release, so expected behaviour is not logged as a defect.
- Agreed rules on handling feedback content that contains personal data.

Where the route offers no in-product feedback, use a simple form or channel linked from the solution and record that
choice; never rely on users finding the maker by name.

## Decision framework

Triage every item into one cause and route it.

| Cause | Typical signs | Owner | Action |
|---|---|---|---|
| Knowledge | Wrong, outdated or missing information; contradictions | Knowledge owner | Fix at source through `ai-operations:knowledge-refresh` |
| Instructions or behaviour | Wrong tone, format, scope or refusal | Maker or solution owner | Change with regression run |
| Scope | Requests for things the solution was not designed to do | Business owner | Decide whether to extend, redirect or say no |
| Actions | Failed or unexpected actions | Maker or engineer | Fix with action tests |
| Training or expectations | Users asking in ways the solution cannot handle, or expecting what it was never meant to do | Adoption lead or Champions | Guidance, examples, communication |
| Harm or exposure | Harmful, offensive or exposing output | Incident lead | Incident route immediately |
| Praise | What works well | Solution owner | Keep, share as a pattern |

Act on themes, not single items, unless an item is harmful, exposing or a clear factual error on a high-consequence
topic. A theme is the same cause recurring across users; the owner sets the review rhythm by tier.

## Practitioner approach

Make feedback easy where people already are. Turn on the route's in-product feedback if it exists, add a short line in
the solution's welcome or description saying how to report a problem, and brief the service desk and Champions to pass on
what they hear. Ask for the question that was asked and what was wrong, not a long form; every extra field loses
reporters.

Read it on a rhythm. The solution owner, or a delegate with authority to route, reviews feedback on a cycle that
matches the tier and volume. Each item gets a cause from the triage table and goes to the owner of that cause. Harmful
or exposing items go to incident handling the moment they are seen.

Look for themes. Group items by cause and topic. Five comments about the same outdated policy page are one knowledge fix;
a cluster of requests for something out of scope is a business owner decision; repeated "it didn't understand me" may
be a training need rather than a defect. Pair feedback with usage trends and quality sampling from monitoring so
decisions rest on more than the loudest voices.

Fix causes, not symptoms. Resist patching instructions for every complaint; route knowledge problems to knowledge
owners, and re-run the regression subset after any change. Add confirmed failures to the golden dataset so they stay
fixed.

Close the loop visibly. Tell users what changed, in a short note in the channel they use, on the solution's description
or through Champions: "You told us the travel policy answers were out of date; the policy source was updated on this
date." Where an item cannot be acted on, say why. Users who see results keep reporting; users who hear nothing stop.

Protect people. Feedback can contain personal or sensitive details, and comments sometimes describe colleagues.
Restrict access, keep it only as long as the agreed retention, and never use feedback to judge individual users or
makers. Report feedback at solution and team level.

Feed the wider cycle. Bring feedback themes to each scheduled review, and pass recurring patterns across solutions to
the CoE so standards, training and knowledge practices improve.

## Outputs

- A feedback plan for each solution, recorded in the `support-and-monitoring-plan`: routes, review rhythm, triage owner and the cause-to-owner table.
- A feedback log with cause, owner, action and status for each item or theme.
- "You said, we did" updates to users.
- New golden dataset items for confirmed failures.

## Microsoft platform considerations

In-product feedback, ratings and analytics differ by route and change over time; confirm current options in
`ms-copilot-studio-guidance` and `ms-agent-builder`, and check how feedback and conversation data are stored and
retained in `ms-copilot-privacy`. Microsoft's adoption resources in `ms-copilot-adoption-hub` and Champion guidance in
`ms-champion-best-practice` offer approaches for gathering feedback through communities.

## Adoption considerations

Visible responses to feedback are among the strongest adoption levers available to a solution owner. Champions, where
they exist, are a natural feedback route; give them a simple way to pass on what they hear.

## Knowledge considerations

Knowledge is the most common cause of negative feedback. Route those items to knowledge owners and track them through
to a fixed source, not just a closed ticket.

## Security and privacy considerations

Feedback may include personal data or confidential content copied from answers. Restrict access, align retention with
`security-privacy:ai-interaction-retention`, and treat any item revealing exposure as an incident.

## Responsible AI considerations

Feedback from or about people affected by a solution's outputs can reveal unfair or harmful patterns. Route those to
the `responsible-ai` reviewers, and never use feedback to profile or assess individual users.

## Evaluation requirements

Confirmed failures from feedback become golden dataset items through `evaluation-quality:golden-dataset`, and changes
made in response run through `evaluation-quality:regression-evaluation`.

## Value measures

Track feedback volume and sentiment per solution, time from theme to action, the share of themes closed with a visible
response, and repeat themes after a fix. The solution owner owns these measures; report by solution and team, never by
individual user.

## Scale notes

### Starter

In-product ratings or a simple form, read by the owner every couple of weeks, with fixes announced in the team channel.

### Scale

A standard feedback triage table across solutions, Champions passing on themes, feedback logs per solution and themes
reviewed in the scheduled reviews.

### Enterprise

Feedback aggregated across the portfolio by cause and theme, cross-solution patterns acted on centrally, and "you said,
we did" reporting as part of the CoE's communication rhythm.

## Hand-offs

- To `ai-operations:knowledge-refresh` for knowledge causes.
- To `evaluation-quality:regression-evaluation` after changes made in response.
- To `ai-operations:ai-incident-management` for harmful or exposing items.
- To `ai-operations:ai-review-calendar` with themes for each scheduled review.

## Reviewer gates

Not applicable as a gate; the feedback loop is an operating practice. Its outputs inform `evaluation-quality` regression
work and the `responsible-ai` reviewers when feedback reveals harm.

## Failure modes

- Ratings are collected but nobody reads them, and users stop giving feedback.
- Every complaint becomes an instruction patch, and the solution grows brittle.
- Feedback reveals a training need, but it is logged as a defect and never resolved.
- Feedback content is used to judge individual users, and reporting stops.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Collect feedback with no owner reading it on a regular cycle.
- Use feedback to assess, rank or monitor individual users or makers.
- Treat a harmful or exposing feedback item as a routine improvement request.
- Close a knowledge-caused item without the source being fixed.
