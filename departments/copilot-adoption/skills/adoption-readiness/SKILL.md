---
name: adoption-readiness
description: Assesses whether an organisation or business unit is ready to adopt Microsoft Copilot across sponsorship, licences assigned versus used, IT-led technical enablement, data and permissions hygiene, approved-use guidance, support and communications, and records the gaps to close before launch. Use when licences have been bought or are about to be, before a launch date is fixed, or when early use has stalled.
license: CC-BY-4.0
metadata:
  department: copilot-adoption
  lifecycle: Discover, Mobilise
  maturity: explorer, adopter, scaler
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, sharepoint, purview, entra
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-adoption-hub, ms-copilot-overview, ms-copilot-privacy
  status: draft
  authors: Simon Foote
---

# Adoption readiness

## Purpose

This skill tells an organisation, honestly, whether it is ready to put Microsoft Copilot in front of its people and
what must be fixed first. It looks at seven readiness areas: sponsorship, licences, technical enablement, data and
permissions hygiene, approved-use guidance, support and communications. Readiness work usually goes wrong in one of
two ways: it becomes a technical deployment checklist that ignores people, or it is skipped because licences have
already been paid for and someone wants a launch date.

## When to use

- Licences have been bought, or a purchase is being considered, and nobody has yet asked whether people, data and support are ready.
- A launch date is being set and the sponsor wants to know what could make it fail.
- Early use has stalled and the organisation needs to know which readiness area is the cause.
- A business unit wants to join an existing rollout and its local position differs from the pilot group's.

## When not to use

- Deciding whether a specific business problem should use AI at all - use `opportunity-management:ai-suitability`.
- Finding and prioritising the role-based scenarios people will use - use `copilot-adoption:scenario-discovery`.
- Planning the phased launch, onboarding and reinforcement once readiness gaps are known - use `copilot-adoption:launch-plan`.
- Setting baselines and adoption measures - use `copilot-adoption:adoption-measurement`.
- A formal review of oversharing, sensitivity labelling or access controls - the `security-privacy` department owns that review.
- Licence purchasing, entitlement or commercial questions - these end with the Microsoft licensing guide or a licensing partner.

## Questions to ask first

1. Who is the accountable executive sponsor, and what outcome have they said Copilot should help achieve?
2. How many licences are assigned, to which roles, and how many of those people have actually used Copilot in the last month?
3. Has IT confirmed the technical prerequisites for the intended audience, and who in IT owns them?
4. Do we know where content is overshared today, and has anyone reviewed permissions on the sites and libraries the first audience uses?
5. Is there written guidance on approved and prohibited uses, and do people know where to find it?
6. Where will a user go on day one when an answer looks wrong or something does not work?

## Required inputs

- The organisation profile or a short description of the audience in scope: roles, locations, ways of working.
- Licence assignment and usage figures from the organisation's own reporting, at team or role level.
- IT's statement of technical enablement status and named owner.
- Any existing data governance, sensitivity labelling or permissions review results.
- Current acceptable-use, information security and AI policies.
- The existing support model and communications channels.

Where an input is missing, record the area as "unknown" with a named person to confirm it. Never infer licence
entitlements, technical status or permission hygiene; an unknown is a readiness gap in its own right.

## Decision framework

Rate each area Ready, Partly ready or Not ready, with evidence. The overall position follows the weakest critical area,
not the average.

| Area | Ready looks like | Critical before launch? |
|---|---|---|
| Sponsorship | A named executive who states the outcome, attends launch and asks about progress | Yes |
| Licences assigned vs used | Licences assigned to roles with scenarios; low use explained and owned | No, but low use blocks expansion |
| Technical enablement | IT confirms prerequisites for the audience and owns the remaining items | Yes |
| Data and permissions hygiene | Oversharing on the audience's main content reviewed and high-risk locations remediated or restricted | Yes |
| Approved-use guidance | Short, written guidance on what is approved, what is not and how to verify output | Yes |
| Support | A route for questions, issues and suspected data exposure, with owners | Yes |
| Communications | A plan to tell people why, what, how and where to get help | No for a pilot; yes for broad launch |

Any critical area at Not ready means "do not launch to this audience yet". Partly ready areas may launch with a dated
mitigation and an owner. Present this as a recommendation to the sponsor; the decision to launch is theirs.

## Practitioner approach

Start with the sponsor, not the tenant. Ask what they expect Copilot to change and for whom. A sponsor who can only
say "productivity" has not yet given the programme anything to aim at, and that is the first readiness gap to record.
Agree the audience in scope at the same time, because readiness is always readiness for someone.

Next, look at licences as an adoption signal rather than a commercial one. Compare licences assigned with licences
actually used, by team or role. Large gaps usually mean licences were assigned by seniority or availability rather than
by scenario, or that people received access with no explanation. Do not comment on whether the organisation has the
right licences or how many it should buy; that question belongs with the licensing guide or a partner.

Technical enablement is IT's responsibility. Your job is to get a clear statement from a named IT owner of what is done,
what remains and when, using the current Microsoft prerequisites in the source records. Do not attempt to configure the
tenant or certify technical readiness yourself.

Spend the most time on data and permissions hygiene. Copilot works with the content each person can already access, so
overshared sites, open team spaces and broad "everyone" permissions become far more visible once people can ask for
summaries across them. Ask which locations the first audience relies on, whether permissions on those have been
reviewed, and whether sensitive content is labelled. Where nobody knows, record oversharing risk as unassessed and route
it to the `security-privacy` department. This is the area most often waved through and most often regretted.

Then check the human scaffolding. Is there short, plain approved-use guidance that tells people what they may use
Copilot for, what they must not paste or ask, and that they remain responsible for checking output? Is there a support
route that distinguishes "how do I" questions from faults and from suspected data exposure? Is there a communications
plan that explains the purpose before the feature list?

Write the assessment as evidence, a rating and a gap for each area, then a short overall recommendation. For each gap,
name an owner and a date, and say whether it blocks launch. Share it with the sponsor in a conversation rather than by
email; readiness findings often reveal uncomfortable truths about ownership that need discussing. Repeat the assessment
for each new audience, because readiness in finance says little about readiness on the shop floor.

## Outputs

- An adoption readiness assessment in the readiness section of the `adoption-plan` template: each area rated with evidence, gaps, owners and dates.
- A readiness gap list classified as blocking launch or launch with mitigation.
- A one-page recommendation for the sponsor: launch, launch to a narrower audience, or delay, with reasons.
- Referrals: oversharing and labelling concerns to `security-privacy`; technical items to the named IT owner.

## Microsoft platform considerations

Copilot grounds answers in content the signed-in user can already access, so existing permissions in SharePoint,
OneDrive and Teams, and any sensitivity labels applied with Microsoft Purview, shape what people will see. Identity and
access are managed in Microsoft Entra. Technical prerequisites, admin controls and product naming change regularly;
check the current position in `references/sources.md` and let IT confirm it. Do not state licence names or
entitlements; refer licensing questions to the Microsoft licensing guide or a licensing partner.

## Adoption considerations

Readiness is the first adoption intervention, not a gate before it. Involve managers and likely Champions early,
because they will explain the gaps to their teams. Treat low usage of assigned licences as a signal to investigate with
teams, never as evidence against individuals.

## Knowledge considerations

Copilot surfaces whatever content people can reach, including outdated and duplicated material. Note where the first
audience's key knowledge is stale or has no owner, and pass it to the `knowledge-management` department (planned) as a
precondition for a good first experience.

## Security and privacy considerations

Oversharing is the dominant readiness risk: content that was technically accessible but practically hidden becomes easy
to find. Record unassessed or high-risk locations, and never mark this area Ready without evidence from a permissions
review. Confirm that the support route can receive reports of suspected data exposure and escalate them promptly.

## Responsible AI considerations

Approved-use guidance must make clear that people remain accountable for what they send, decide or publish using
Copilot output, and that some uses are prohibited. Where the first audience makes decisions about people, money or
safety, note that human verification needs explicit emphasis in onboarding.

## Evaluation requirements

Not applicable as model or output evaluation, because this skill assesses organisational readiness rather than an AI
solution. The assessment itself is checked by confirming every rating has evidence and every gap has an owner.

## Value measures

The readiness baseline becomes part of the adoption baseline: proportion of critical areas Ready, licences assigned
versus used by team or role, and the number of open blocking gaps. The adoption lead owns these measures and reports
them to the sponsor at team or role level only.

## Scale notes

### Starter

A one-hour conversation with the owner, the IT provider and whoever handles data protection, recorded on two pages.
Focus on oversharing in shared drives and a one-page approved-use note.

### Scale

Assess each business unit or wave separately, reuse the same areas and ratings, and keep a register of gaps across
waves so recurring issues reach the right owner.

### Enterprise

Federate assessments to business-unit adoption leads using a shared rubric, with the central programme validating
critical areas. Align the permissions review with the formal `security-privacy` process and track gaps in the
programme risk log.

## Hand-offs

- To `copilot-adoption:scenario-discovery` once the audience is agreed, to find the scenarios that will make the launch worthwhile.
- To `copilot-adoption:launch-plan` with the gap list and mitigations.
- To `copilot-adoption:adoption-measurement` with the readiness baseline.
- To the `security-privacy` department for oversharing, labelling and access findings.

## Reviewer gates

From risk tier 1, `security-privacy` reviews the data and permissions hygiene rating before any launch to a new
audience, looking for evidence of a permissions review on the audience's main content and a working route for data
exposure reports. A Not ready rating in that area is blocking.

## Failure modes

- Readiness is reduced to a technical checklist, so the launch goes ahead with no sponsor outcome and no support route.
- Oversharing is marked Ready because nobody has looked, and the first week produces a data exposure incident.
- Licences are assigned by seniority, usage stays low, and the programme blames users instead of the missing scenarios.
- The assessment is done once for a pilot and assumed to hold for very different audiences later.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- State licence names, entitlements, prices or prerequisites from memory.
- Mark data and permissions hygiene as Ready without evidence of a review.
- Use licence usage data to single out, compare or judge individual people.
- Present the launch decision as yours; it belongs to the sponsor.
