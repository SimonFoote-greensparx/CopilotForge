---
name: ai-stakeholder-mapping
description: Maps the stakeholders of an AI change by role and group - their interests, influence on the outcome, stated concerns about AI such as jobs, monitoring, quality and ethics, and the engagement each needs - so HR, employee representatives, functions and affected teams are involved early rather than told late. Use when an AI programme or wave is starting, when a group pushes back unexpectedly, or when engagement has been launch emails only.
license: CC-BY-4.0
metadata:
  department: change-and-communications
  lifecycle: Envision, Mobilise, Launch, Scale
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-responsible-ai, ico-ai-data-protection
  status: draft
  authors: Simon Foote
---

# AI stakeholder mapping

## Purpose

This skill identifies who has a stake in an AI change, what each group wants from it, how much each can shape the
outcome and what each is worried about, then sets how each will be engaged. It works at the level of roles and groups
(the HR function, employee representatives, contact centre team leaders, the data protection officer as an office),
because the purpose is to plan engagement, not to judge people. AI changes go wrong here in two predictable ways: the
map is drawn only of senior supporters, so the groups who can stall the change (employee representatives, the DPO,
frontline supervisors) are discovered at launch; or concerns about jobs and monitoring are filed as "resistance"
instead of being answered.

## When to use

- An AI programme, Copilot wave, agent rollout or Cowork pilot is starting and nobody has mapped who it affects.
- A function, union, works council or professional group has pushed back and the programme did not see it coming.
- Engagement so far has been announcement emails and a launch event, with no conversation.
- The programme is expanding to a new business unit, region or audience with different stakeholders.
- The communications strategy needs a stakeholder view before messages and senders are chosen.

## When not to use

- Setting who decides, who must approve and how escalation works - use `programme-management:stakeholder-governance`.
- Securing and equipping the executive sponsor - use `ai-strategy:executive-sponsorship`.
- Grouping the whole workforce into adoption audiences for onboarding and waves - use `copilot-adoption:audience-segmentation`.
- Assessing how much each group's roles and work will change - use `change-and-communications:people-change-impact`.
- Working out why a group is resisting and what to do about it - use `change-and-communications:resistance-management`.

## Questions to ask first

1. What exactly is changing, for which parts of the organisation, and over what period? A map drawn for "AI" in general is too vague to act on.
2. Who can stop, delay or materially shape this change - through approval, consultation rights, budget, expertise or informal standing?
3. Which groups will feel the change first and most, and which of them have a formal voice (employee representatives, professional bodies, staff networks)?
4. What have stakeholders already said about AI, in which forums, and what did the programme do with it?
5. Who in the programme will own each relationship, and how much engagement time do they really have?

## Required inputs

- A one-paragraph description of the change, its scope, timing and the AI experiences involved.
- The organisation chart at function and unit level, and the list of governance forums from `programme-management:stakeholder-governance` where it exists.
- Any early impact view from `change-and-communications:people-change-impact`.
- Existing feedback: pulse comments, questions raised at town halls, representations from employee representatives, and support themes.
- HR's view of any consultation or information obligations, confirmed with the legal adviser.

Where consultation obligations are unknown, record "to confirm with HR and legal" against the relevant group and do
not schedule announcements that could pre-empt consultation. Never infer a group's concerns from stereotype; mark them
"not yet heard" until someone has asked.

## Decision framework

Place each stakeholder group on two judgements - influence over the outcome and how strongly the change affects or
interests them - and choose the engagement mode from the grid. Record the evidence for each placement.

| Influence | Interest or impact | Engagement mode | Typical form |
|---|---|---|---|
| High | High | Partner | Involved in design decisions; regular one-to-one or small-group sessions; sees drafts before others |
| High | Lower | Consult | Briefed before announcements; asked for specific input; kept on the decisions that touch them |
| Lower | High | Involve | Listening sessions, pilots, feedback channels; their concerns shape messages and support |
| Lower | Lower | Inform | Standard communications through the channels they use |

Then record each group's stated concerns against a fixed set, so responses can be planned and routed rather than
improvised.

| Concern | What it usually sounds like | Route for the response |
|---|---|---|
| Jobs and roles | "Is this about cutting headcount?" | Agreed position from the sponsor and HR; `change-and-communications:people-change-impact` |
| Monitoring | "Will my prompts be read or my usage tracked?" | Approved-use guidance and the DPO's position on usage data |
| Quality and accountability | "Who is responsible when it is wrong?" | Verification guidance; `responsible-ai` department for higher-risk uses |
| Ethics and fairness | "Should we be using AI for this at all?" | `responsible-ai:ai-impact-assessment` where a solution affects people |
| Workload and time | "When am I meant to learn this?" | Manager agreement on practice time; `change-and-communications:manager-enablement` |
| Data and confidentiality | "Will client information leak?" | Security and data protection leads; approved-use guidance |
| Professional identity | "This devalues what I trained for" | Role-specific scenarios and peer voices; `change-and-communications:resistance-management` |

Formal voices override the grid. A recognised employee representative body is at least "Consult", whatever its
apparent influence, and HR and the legal adviser decide whether consultation is required before anything is announced.

## Practitioner approach

Start with the change, not the organisation chart. Write down what will be different, for whom and when. A Copilot Chat
rollout to everyone, a Microsoft 365 Copilot wave for one division and an agent that drafts responses to customers have
very different stakeholders, and one map cannot serve all three.

List stakeholders as groups and offices. Include the obvious (sponsor, IT, security, HR, the functions going first) and
the ones programmes forget: employee representatives, the DPO, internal audit, frontline supervisors, people who own
the knowledge an agent will draw on, and teams whose work will change because another team uses AI. Keep named
individuals out of the map except where an office is held by one person, and then record the office, not opinions
about the holder.

Hear concerns directly. Hold short conversations with each high-influence or high-impact group and ask three things:
what they hope AI will do, what worries them, and what would make them confident. Write down what they said in their
words. A map built from the programme team's assumptions about other people's views is usually wrong about exactly the
groups that matter most.

Place each group on the grid and challenge the placements in a short session with the change lead, HR and an
adoption lead. Influence is often under-estimated for groups with formal rights or deep expertise, and over-estimated
for senior people who are supportive but not affected. Note where a group's support depends on a specific commitment,
such as no use of usage data in performance management.

Turn the map into an engagement plan: for each group, the mode, the owner, the first conversation, the rhythm, and
what the programme needs from them. Agree with HR and the legal adviser which groups must be informed or consulted
before announcements, and put those steps ahead of the communications calendar rather than after it.

Map concerns to responses. Each recurring concern needs an agreed, honest answer and an owner. Where the honest answer
is "we have not decided", say so and give the date when a decision is expected. Pass the answers to
`change-and-communications:ai-communication-strategy` so that every sender uses the same words.

Review the map at each phase gate and whenever a new audience, solution or region joins. Stakeholder positions move as
people experience AI. A group that was sceptical before a pilot may become the best advocate after it, and a group that
was neutral may harden after a poorly handled announcement. Record what changed and why, so the programme learns.

## Outputs

- A stakeholder map by group and office: interest or impact, influence, evidence, engagement mode, owner and rhythm, recorded in the stakeholder section of the `ai-communications-plan` template.
- A concern register: concerns in the groups' own words, the agreed response, the owner and the date a pending decision is due.
- A pre-announcement engagement sequence agreed with HR and the legal adviser, showing who is informed or consulted before whom.
- A short note to the sponsor naming the two or three relationships that most need their personal attention.

## Microsoft platform considerations

Not applicable to the mapping method, which holds whatever Microsoft AI experience is being introduced. The platform
matters only for the substance of concerns: what is stored, who can see prompts and outputs, and what usage reporting
shows. Answer those from the current source records in `references/sources.md` and the organisation's own settings,
never from memory.

## Adoption considerations

The map feeds audience work in `copilot-adoption:audience-segmentation` and the choice of senders in the communications
strategy. Groups placed at "Involve" are good candidates for pilots and for the change network, because their
experience will be trusted by peers.

## Knowledge considerations

Knowledge owners are stakeholders in any agent or Cowork change that draws on their content. Include them explicitly,
because their time is usually the hidden constraint, and pass ownership gaps to `knowledge-management:knowledge-owner-model`.

## Security and privacy considerations

The map and concern register record views of groups, not people. Keep them in a restricted location, avoid recording
named individuals' personal opinions, and set a retention period. Questions about consultation duties and the use of
employee data end with HR, the DPO or the legal adviser.

## Responsible AI considerations

Groups who will be affected by an AI solution but will not use it (customers, applicants, colleagues whose work is
reviewed by AI) are stakeholders too. Where such groups appear, flag the solution for `responsible-ai:ai-impact-assessment`
rather than treating their concerns as a communications task.

## Evaluation requirements

Not applicable as solution evaluation, because stakeholder mapping is a change practice. The map is tested by whether
any group with formal rights or material influence was missed, checked at each phase review.

## Value measures

Owned by the change lead, with the first map as baseline: share of high-influence and high-impact groups engaged before
announcements, concerns with an agreed answer and owner, and time from a concern being raised to an answer. Reported
for the programme as a whole, never as a rating of individuals.

## Scale notes

### Starter

One page for the whole organisation, drawn in a short session with the sponsor and HR, with five to ten groups and a
handful of recurring concerns.

### Scale

A map per business unit or wave, a shared concern register, and phase-gate reviews led by the change lead with the
change network's input.

### Enterprise

A federated map with a common concern taxonomy, regional variations for differing consultation arrangements, and a
consolidated view for the enterprise sponsor forum.

## Hand-offs

- To `change-and-communications:ai-communication-strategy` to turn the map and agreed answers into messages, senders and channels.
- To `change-and-communications:people-change-impact` for the groups whose roles and work change most.
- To `programme-management:stakeholder-governance` where a group needs a formal decision or approval right.
- To `change-and-communications:resistance-management` where concerns have hardened into opposition.

## Reviewer gates

Not applicable as a formal gate, because the map is an engagement plan rather than a released solution. Where it
surfaces people affected by a solution at risk tier 2 or above, the `responsible-ai` review of that solution must see it.

## Failure modes

- Only supportive senior stakeholders are mapped, and employee representatives first hear of the change in the launch email.
- The map records opinions about named individuals, leaks, and damages trust in the whole programme.
- Concerns are captured but never answered, so the same questions resurface at every town hall.
- The map is drawn once and never revisited, while positions shift after pilots and announcements.
- Consultation obligations are checked after the announcement, forcing a public reversal.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Score, rank or label named individuals as supporters or resistors.
- Announce a change to a group with consultation rights before HR and the legal adviser have confirmed the sequence.
- Record a group's concerns from assumption rather than from hearing them.
- Give an answer on jobs or monitoring that the sponsor, HR and the DPO have not agreed.
