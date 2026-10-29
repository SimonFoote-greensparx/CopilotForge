---
name: knowledge-owner-model
description: Defines the knowledge ownership model for the organisation - domain owner, content owner, steward, subject matter reviewer and site administrator - with responsibilities, decision rights, time expectations, succession and escalation, so every source AI grounds on has an accountable role. Use when sources have no owner, when owners leave and content goes stale, or when IT is being asked to vouch for business content.
license: CC-BY-4.0
metadata:
  department: knowledge-management
  lifecycle: Mobilise, Enable, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-studio-guidance, ms-copilot-adoption-hub
  status: draft
  authors: Simon Foote
---

# Knowledge owner model

## Purpose

Every knowledge problem that hurts AI answers - stale policy, competing versions, overshared folders - is at root an
ownership problem. This skill defines the roles that keep knowledge accurate, current and correctly shared, what each
role decides, how much time it needs and what happens when the person in it moves on. It goes wrong when ownership is
assigned to whoever administers the site, when the role is given without time to do it, or when the model is so
elaborate that nobody can tell who to call.

## When to use

- The readiness assessment or inventory found sources with no owner, or owners who have left.
- Agents are being built on content whose accuracy nobody will vouch for.
- IT or the CoE is being asked to answer for the correctness of business content.
- A reorganisation is about to move teams and the content they maintain.

## When not to use

- Naming the business, knowledge and technical owners for one specific agent - use `m365-agents:agent-ownership`.
- The organisation-wide RACI across AI work - use `ai-centre-of-excellence:coe-raci`.
- Mapping declared people roles to the AI programme's departments - use `organisation-tailoring:ownership-map`.
- Data ownership for structured data sets - the `data-governance` department, for example `data-governance:ai-data-inventory`.

## Questions to ask first

1. Which roles already exist that carry some knowledge responsibility (policy owners, site owners, records officers, editors), and what do they actually do today?
2. At what level should accountability sit - knowledge domain, source, or document - for the decisions AI use depends on?
3. What time can owners realistically give, and will their managers recognise it as part of the job?
4. Who resolves disputes when two teams claim the same topic, or nobody does?
5. What should happen to content when its owner leaves, moves or the team is restructured?

## Required inputs

- The knowledge domains and sources in scope, from `knowledge-management:knowledge-inventory`.
- The organisation's declared roles and structure; never infer roles from individuals' activity.
- Any existing policy ownership, records management or intranet governance arrangements.
- The AI uses that depend on each domain, so ownership can be prioritised where it matters.

Where a domain has no plausible owner, record it as a gap for the sponsor rather than defaulting it to IT or the
knowledge team. Never record a person as an owner until they have accepted the role.

## Decision framework

Use five roles and assign the minimum that each domain needs.

| Role | Accountable for | Typical holder | Required when |
|---|---|---|---|
| Domain owner | What the organisation treats as true in a knowledge domain; resolves conflicts; accepts AI use | Senior business role (head of HR policy, service owner) | Always, one per domain |
| Content owner | Accuracy, currency and audience of a source or collection; approves publication and review | Team lead or specialist in the business | Always, one per registered source |
| Steward | Day-to-day upkeep: metadata, structure, review reminders, archiving | Editor, coordinator or knowledge champion | Where volume or change rate exceeds what the content owner can maintain |
| Subject matter reviewer | Technical correctness of specific content at review | Specialist, often in another team | Where content is regulated, technical or safety-related |
| Site administrator | Permissions, configuration and platform health; never content accuracy | IT or a business site owner | Always, but never as a substitute for a content owner |

Rules: exactly one accountable domain owner and one content owner per source; a named deputy for each; ownership moves
with the function, not the person; and any agent grounding on a source must have that source's content owner aware and
consenting.

## Practitioner approach

Start from what exists. Most organisations already have policy owners, intranet editors, records officers and site
owners; the model should formalise and connect them, not replace them with new titles. Interview a handful of people in
each role and ask what they actually do, how long it takes and what stops them. The gap between the role as written and
the role as practised is usually where content decays.

Set accountability at the level of decisions. A domain owner decides which source is authoritative when two teams
disagree and whether the domain may be used for AI grounding. A content owner decides what is published, who can see
it and when it is reviewed. Separate both clearly from the site administrator, who controls the platform but cannot
know whether a policy is correct. When those roles collapse into one, the result is an IT team answering for business
content it does not understand.

Write each role as a short description: purpose, decisions, recurring tasks, expected time per month, skills needed and
how the role is recognised. Be realistic about time. A content owner for a busy policy library may need a few hours a
month; if that time is not agreed with their manager, reviews will slip within a quarter. Record expectations in the
role description, and leave recognition to managers and HR rather than tracking individuals.

Design succession deliberately. Ownership should belong to a function or post, with a named deputy, so that a leaver
triggers a handover rather than an orphaned library. Link the knowledge register to joiner, mover and leaver processes
so owner changes are prompted, not discovered when an agent fails.

Define escalation for the two common disputes: competing claims to a topic, and topics nobody wants. The domain owner
resolves the first; the sponsor or CoE steering resolves the second, because an unowned topic is a business risk rather
than a knowledge-team task.

Finally, apply the model to the inventory. Fill in owners for the domains and sources that current AI uses depend on
first, and record the remainder as a prioritised gap list. Tell each new owner which agents and Copilot scenarios rely
on their content; people look after what they can see being used.

## Outputs

- A knowledge ownership model: role descriptions, decision rights, time expectations, succession and escalation rules.
- Owner assignments recorded against domains and sources in the `knowledge-asset-register`.
- A prioritised list of ownership gaps for the sponsor, starting with sources AI already depends on.

## Microsoft platform considerations

Platform roles such as SharePoint site owner, Teams owner or agent maker grant control, not accountability for content.
Map each knowledge role to the platform permissions it needs, and avoid giving content owners administrative rights
they do not need. Microsoft guidance on agent governance (`ms-copilot-studio-guidance`) describes ownership expectations
for agents; align knowledge roles with it rather than duplicating it.

## Adoption considerations

Owners are the people who make AI answers trustworthy. Brief them on what AI will do with their content, involve them
in testing agents that use it, and share good outcomes. Owners who only hear about problems disengage.

## Knowledge considerations

This skill sets who does the work in `knowledge-management:knowledge-review-cycles`, `knowledge-management:knowledge-lifecycle`
and `knowledge-management:knowledge-cleanup`; change those skills' assumptions if the model changes.

## Security and privacy considerations

Content owners decide intended audience, so they need to understand sensitivity and the effect of permission-trimmed
grounding. Site administrators implement access, and neither role should approve exceptions to the classification
scheme alone.

## Responsible AI considerations

Domain owners accept that AI may answer from their content. For domains that inform decisions about people, money or
safety, the domain owner must be part of the human oversight design for any agent that uses them.

## Evaluation requirements

Check the model works by sampling sources each quarter: is the recorded owner still in post, aware of the role and able
to name the last review? Report the result by domain.

## Value measures

Track the share of registered sources with an accepted owner and deputy, the share of AI-dependent sources whose owner
knows they are used, and the time to reassign ownership after a leaver. Report at domain level; never measure or rank
individual owners.

## Scale notes

### Starter

Name a domain owner and content owner for each source the first agents use, with a one-paragraph role description.

### Scale

Publish the full role set, link owner changes to joiner, mover and leaver processes, and run a community for owners and
stewards.

### Enterprise

Federate domain ownership to business units under a shared model, with a central knowledge team resolving cross-unit
disputes and reporting ownership coverage to steering.

## Hand-offs

- To `knowledge-management:knowledge-inventory` to record owners against sources.
- To `knowledge-management:knowledge-review-cycles` to set the review duties owners carry.
- To `ai-centre-of-excellence:coe-raci` so knowledge roles appear in the wider RACI.

## Reviewer gates

Not applicable; the model assigns accountability rather than releasing a solution. Reviewer gates apply to the agents
and rollouts that depend on owned sources.

## Failure modes

- Site administrators are recorded as content owners and cannot judge accuracy.
- Ownership is assigned to individuals, not posts, and lapses when they leave.
- Owners are named without agreed time, and reviews quietly stop.
- Unowned topics default to the knowledge team, which becomes the bottleneck for every correction.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Record someone as an owner who has not accepted the role.
- Make IT or the platform team accountable for the accuracy of business content.
- Monitor, score or rank individual owners; measure ownership coverage by domain.
- Leave an AI-dependent source without a deputy owner.
