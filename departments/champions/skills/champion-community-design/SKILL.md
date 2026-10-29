---
name: champion-community-design
description: Designs the Champion community - the space and its channels, a community manager and moderation, rituals such as community calls, show-and-tell and prompt clinics, peer learning through pairing and learning circles, local spokes, and the route by which good material reaches the scenario catalogue. Use when a new network needs a home, when the Champion channel has gone quiet, or when peer learning depends on one organiser.
license: CC-BY-4.0
metadata:
  department: champions
  lifecycle: Enable, Launch, Scale
  maturity: explorer, adopter, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: m365-copilot, sharepoint, platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-champion-programme, ms-champion-best-practice, ms-copilot-adoption-hub
  status: draft
  authors: Simon Foote
---

# Champion community design

## Purpose

Champions learn most from each other. A well-run community turns a list of volunteers into a network that shares what
works, solves problems together, keeps up with product change and passes good material on to the rest of the
organisation. This skill designs that community: the space, its structure and moderation, the rituals that give it a
pulse, the peer learning formats that build capability, and the routes by which useful material leaves the community.
Communities usually go wrong when a channel is created and left to run itself, when the only activity is
announcements from the centre, or when everything depends on one energetic organiser who then moves on.

## When to use

- A Champions programme is launching and its community space needs designing before the first cohort joins.
- The Champion channel has gone quiet, or is used only for central announcements.
- Champions say they learn more from colleagues than from sessions, and the programme wants to build on that.
- The network has grown across business units or regions and needs local spokes without fragmenting.
- Good prompts and examples are shared in the community but never reach the wider workforce.

## When not to use

- Deciding whether a community is needed and its place in the programme charter - use `champions:champion-programme-design`.
- Designing the learning offer and sessions mapped to the Champion journey - use `champions:champion-learning`.
- Building a change network of change agents alongside Champions - use `change-and-communications:change-network`.
- Running office hours for the whole workforce - use `learning-and-skills:office-hours`.
- Defining programme-level measures for the network - use `champions:champion-metrics`.

## Questions to ask first

1. Who will manage the community day to day, and how much time do they have?
2. Where do Champions already collaborate, and which tools are approved for a community space?
3. How large is the network now and in a year, and is it one community or several connected spokes?
4. What should Champions get from the community each month that they cannot get elsewhere?
5. How will good material be checked and moved into the scenario catalogue or self-service guidance?

## Required inputs

- The programme charter and network shape from `champions:champion-programme-design`.
- The current or planned cohort size and spread from `champions:champion-recruitment`.
- The approved collaboration tools and any rules for communities, from IT.
- The scenario catalogue process from `copilot-adoption:scenario-discovery`, so material has somewhere to go.
- The learning calendar from `champions:champion-learning`, so community rituals complement rather than duplicate it.

If nobody can be named as community manager, record it as a precondition: a community without a manager decays
quickly. If no route to the scenario catalogue exists, material will stay trapped in the community; agree one first.

## Decision framework

Structure the space around how Champions will use it, not around the org chart.

| Element | Purpose | Minimum design |
|---|---|---|
| General channel | News, questions, quick wins | Pinned guide, posting norms, moderation |
| Show and share | Examples, prompts and stories | A simple format: task, prompt, how it was checked, result |
| Questions and help | Peer answers to Champion questions | Answered within an agreed time by peers or the manager |
| Local spokes | Business-unit, regional or frontline groups | Local lead, linked to the central space |
| Resources | Guide, capability framework, recordings | Owned, versioned, searchable |

Give the community a pulse with a small set of rituals.

| Ritual | Purpose | Typical rhythm | Owner |
|---|---|---|---|
| Community call | News, product changes, one Champion demonstration, open questions | Monthly | Community manager |
| Show-and-tell | Champions present what worked in their team | Monthly or within the call | Rotating Champions |
| Prompt clinic | Bring a real task; improve the prompt together | Fortnightly or monthly | Experienced Champions |
| Product change briefing | What changed and what it means for guidance | When Copilot changes | Adoption lead |
| Showcase with sponsor | Recognise contributions and Challenge outputs | Quarterly | Programme owner and sponsor |

Choose peer learning formats by the network's maturity: buddy pairing for new Champions, learning circles of four to
six people working on a shared theme for established networks, and mentoring by recognised Champions for people
starting the Challenge.

## Practitioner approach

Appoint a community manager before opening the space. This is a role, not a job title: someone with time to welcome
newcomers, seed conversations, answer or route questions, moderate and keep the rituals running. In small programmes
it is the programme owner; in larger ones it is a dedicated role with local spoke leads.

Design the first week of membership. New Champions should be welcomed by name, pointed to the guide and the pinned
norms, introduced to a buddy, and invited to the next community call. People who feel welcome in their first week
contribute; people who join a silent channel lurk and drift.

Seed before you expect. In the early months, the community manager and a few experienced Champions post examples,
questions and short wins regularly, so the space feels alive. Make it easy to share: a simple format for examples
(task, prompt, how it was checked, result) lowers the barrier and models verification.

Run rituals reliably. A monthly community call that always happens, with one Champion demonstration and an honest
discussion of what did not work, is the backbone of most healthy communities. Rotate presenters, record calls for
those on shifts, and keep them short. Use prompt clinics to make learning practical rather than theoretical.

Build peer learning into the structure. Pair each new Champion with a buddy for their first stage. Once the network is
established, form learning circles around themes such as meeting preparation, reporting or agent use cases, each
producing something reusable. Recognised Champions can mentor those working on Challenges.

Moderate for safety and boundaries. Agree and pin norms: no personal or confidential data in examples, no sharing of
unapproved tools, ideas for agents go to intake, faults go to the service desk. The community manager gently redirects
posts that drift outside the boundary, so the community does not become a shadow support desk.

Connect the community to the rest of the organisation. Agree a route by which good examples are reviewed and added to
the scenario catalogue and self-service guidance, credited to their authors. Bring the sponsor in quarterly. Feed
recurring themes to the adoption lead and the CoE.

Watch the community's health at programme level: questions answered by peers, share of posts from Champions rather
than the centre, attendance at rituals and material reaching the catalogue. A community that only receives
announcements needs a reset, not more announcements.

## Outputs

- A community design recorded in the community section of the `champion-programme-charter` template: space structure, community manager, spoke leads, norms, rituals, peer learning formats and routes out.
- A pinned community guide and posting norms, linked from the `champion-guide`.
- A ritual calendar with owners.
- A content route from the community to the `scenario-catalogue`, with review and credit.

## Microsoft platform considerations

Champion communities commonly run in Teams or Viva Engage, with resources in SharePoint. Choose what the organisation
already uses and has approved, so Champions are not asked to adopt another tool. Features, naming and availability
change; check `references/sources.md` and the approved tools list. Any community agent or bot follows the
organisation's agent governance.

## Adoption considerations

The community is where Champions keep their own practice current and pick up what to share with their teams. Align
community themes with the adoption reinforcement cycle, so Champions arrive at team meetings with the same new
scenarios the programme is promoting.

## Knowledge considerations

Community material is valuable but unreviewed. Treat it as raw material: good examples are checked, given an owner and
moved into the scenario catalogue or self-service guidance, and resources in the space carry versions and review
dates.

## Security and privacy considerations

Norms prohibit personal or confidential data in shared examples, and the community manager removes it if posted.
Membership of the community is not a route to wider access. Recordings of calls are stored with appropriate access and
retention. Data protection questions end with the organisation's DPO.

## Responsible AI considerations

The community models responsible practice: examples show how output was checked, limitations are discussed openly, and
Champions are encouraged to share failures as well as wins. Ideas that touch decisions about people are routed to
intake and risk classification, not built in the community.

## Evaluation requirements

Not applicable as solution evaluation, because a community is a people practice rather than an AI solution. Its health
is reviewed through the programme-level signals in this skill and the measures in `champions:champion-metrics`.

## Value measures

Owned by the community manager, with baselines at launch: share of questions answered by peers, share of contributions
from Champions rather than the centre, ritual attendance, examples moved into the scenario catalogue and reuse of those
examples. Reported at programme level, never as individual rankings or activity counts.

## Scale notes

### Starter

One channel, a monthly call run by the programme owner, a buddy for each new Champion and a simple route for good
examples into the catalogue.

### Scale

A structured space with a community manager, rotating show-and-tell, prompt clinics, learning circles and spoke leads
for larger business units.

### Enterprise

A federated community with regional spokes on a shared structure and norms, local-language spaces where needed, a
central community manager role, and themes coordinated with the CoE.

## Hand-offs

- To `champions:champion-learning` to align rituals with the learning offer.
- To `copilot-adoption:scenario-discovery` to test and add community examples to the catalogue.
- To `champions:champion-metrics` for programme-level community measures.
- To `champions:champions-health-check` when the community needs a reset.

## Reviewer gates

Not applicable as a formal gate, because a community does not release an AI solution; content and recordings follow
the organisation's existing information and data protection controls.

## Failure modes

- A channel is created with no community manager, and it goes quiet within weeks.
- The space is used only for central announcements, so Champions stop contributing.
- The community becomes a shadow support desk for faults and access problems.
- Good examples stay in the channel and never reach the wider workforce.
- Everything depends on one organiser, and the community collapses when they move on.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Open a community space without a named community manager.
- Allow personal or confidential data in shared examples.
- Publish individual activity counts or leader boards from community data.
- Let the community become the default route for faults, access or approvals.
