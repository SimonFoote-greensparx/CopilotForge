---
name: m365-copilot-rollout
description: Plans the wave-by-wave rollout of licensed Microsoft 365 Copilot, choosing which roles receive licences first, the technical and work-context gates each wave must pass, licence allocation and reallocation rules agreed at role level, wave exit criteria and the rollout plan that ties them together. Use when licences are being allocated, when a wave is about to start, or when licences sit unused.
license: CC-BY-4.0
metadata:
  department: m365-copilot
  lifecycle: Mobilise, Launch, Scale
  maturity: adopter, scaler, ai-enterprise
  risk-tiers: 0, 1, 2
  platforms: m365-copilot, entra, sharepoint, purview
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-overview, ms-copilot-privacy, ms-copilot-adoption-hub
  status: draft
  authors: Simon Foote
---

# Microsoft 365 Copilot rollout

## Purpose

Licensed Microsoft 365 Copilot works on a person's mail, meetings, chats and files, so who receives it, in what order
and under what conditions is a design decision, not an administrative task. This skill plans the rollout in waves: it
chooses the roles that go first on the strength of their scenarios and the condition of their work context, sets the
gates each wave must pass, agrees licence allocation rules at role level and defines what "done" means before the next
wave starts. Rollouts usually go wrong when licences are handed to senior staff and enthusiasts by default, the waves
have no exit criteria, and the organisation discovers months later that a large share of licences are unused.

## When to use

- Licences have been bought or committed and someone must decide who gets them first.
- A wave is about to start and the technical, content and support gates need confirming.
- Licences are sitting unused and the allocation rules need revisiting.
- The organisation wants to move from a pilot to a broader rollout and needs a plan with criteria.

## When not to use

- Rolling out Copilot Chat to the whole workforce - use `m365-copilot:copilot-chat-rollout`.
- Confirming tenant prerequisites and admin settings - use `m365-copilot:copilot-technical-readiness`.
- People-side launch activities such as executive and manager enablement, onboarding sessions and reinforcement - use `copilot-adoption:launch-plan`.
- Licence purchasing, entitlement or commercial terms - use `platform-governance:ai-licensing-and-capacity`, which ends with the Microsoft licensing guide or a licensing partner.
- Measuring whether the rollout delivers value - use `copilot-adoption:adoption-measurement` and the `value-realisation` department.

## Questions to ask first

1. How many licences are available now and later, as confirmed by the licence owner, and what has already been promised to whom?
2. Which roles have validated scenarios where Copilot's use of their mail, meetings and files clearly helps?
3. Is each candidate group's work context ready, and is the technical readiness verdict Ready for their segment?
4. What support, Champions and onboarding capacity exists for each wave?
5. What rule will the organisation use to reallocate licences, and have HR and the data protection lead agreed it?

## Required inputs

- Licence quantities and timing, confirmed by the licence owner; never estimated.
- The scenario catalogue by role from `copilot-adoption:scenario-discovery` and `m365-copilot:copilot-role-scenarios`.
- Technical readiness verdicts per segment from `m365-copilot:copilot-technical-readiness`.
- Work context readiness per candidate group from `m365-copilot:work-context-readiness`.
- The adoption plan and support model, so waves match onboarding capacity.

Missing inputs are marked "to confirm" in the rollout plan. A wave whose readiness verdict or scenarios are missing does
not have a start date.

## Decision framework

Score candidate groups on four criteria, each High, Medium or Low, and start with groups strong on all four.

| Criterion | High | Low |
|---|---|---|
| Scenario strength | Validated, frequent scenarios that rely on mail, meetings or files | Generic interest with no named scenario |
| Work context condition | Content in Microsoft 365, permissions reviewed, meetings recorded or transcribed where appropriate | Work lives in other systems or local files; permissions unknown |
| Leadership and support | Business owner engaged, Champions present, manager willing to lead | No owner, no local support |
| Risk profile | Content and decisions at low sensitivity | Highly sensitive content not yet protected |

Each wave has entry gates (technical Ready, work context Ready or Ready with conditions, onboarding scheduled, support
briefed) and exit criteria agreed before it starts (for example, scenarios in use across the group, support tickets
stabilised, feedback reviewed and guidance updated). The next wave starts when the previous one meets its exit criteria
or the rollout owner records why not.

## Practitioner approach

Resist two common shortcuts: giving the first licences to the most senior people, and giving them to whoever asks
loudest. Both produce visible but unrepresentative pilots. Instead, build a short list of candidate groups and score them
against the four criteria with the business owners in the room. Include at least one group whose work is heavy on
meetings and mail, and at least one that is document-heavy, so early learning covers different patterns. Senior leaders
may be in an early wave, but because they are a role with scenarios, not as a perk.

For each wave, write the entry gates as checks with owners. The technical gate comes from
`m365-copilot:copilot-technical-readiness`; the content gate from `m365-copilot:work-context-readiness`; the people
gate from the adoption plan. A wave that starts with an unresolved oversharing finding on its main sites will teach the
organisation the wrong lesson about Copilot.

Agree licence allocation and reallocation rules at role level before the first wave, with HR and the data protection
lead. Good rules allocate by role and scenario, ask managers and users to release licences they do not need, and review
uptake at team level. Any proposal to use person-level activity data for reallocation is a policy decision for the data
protection lead and HR, recorded separately, and never a measure of performance.

Assign licences through groups that map to waves so the rollout is traceable and reversible. Before each wave, brief the
service desk on that group's scenarios and known limitations, and confirm the onboarding sessions are booked.

Define exit criteria in terms that a sponsor would recognise: the priority scenarios are in use across the team, the
volume of "how do I" questions has fallen, and the feedback has been reviewed and has changed the guidance. Hold a short
wave review, record what changed, and adjust the next wave's scenarios, readiness work and support.

Keep the whole plan in the `copilot-rollout-plan` and revisit it monthly. Capability and licensing change, so check the
source records before each wave rather than relying on the assumptions made at the start.

## Outputs

- A rollout plan on the `copilot-rollout-plan` template: waves, candidate scoring, entry gates, exit criteria, licence allocation rules, owners and dates.
- A wave review record after each wave, with the changes made to the next one.
- Licence allocation and reallocation rules agreed at role level, with HR and data protection sign-off recorded.

## Microsoft platform considerations

Licensed Microsoft 365 Copilot grounds on the user's mail, meetings, chats and files according to their permissions,
as described in `ms-copilot-privacy`. Assign licences through groups in Microsoft Entra so waves are controlled.
Prerequisites, included capabilities, extensibility and licensing change often; confirm them in `ms-copilot-overview`
and the licensing route before each wave, and never state a licensing conclusion yourself.

## Adoption considerations

Waves should match onboarding and support capacity, not licence availability. Coordinate dates with
`copilot-adoption:launch-plan` so every wave has manager briefings, onboarding by persona and reinforcement in the weeks
that follow.

## Knowledge considerations

Licensed Copilot is only as useful as the content a person can reach. Where a wave's scenarios rely on shared team
content, the content owner and its condition are part of the work context gate; curated knowledge improvements route to
the `knowledge-management` department.

## Security and privacy considerations

Each wave widens the set of people who can find overshared content quickly. The work context gate must include
permissions on the group's main sites. Any decision on using person-level activity data for licence management goes to
the data protection lead and HR, and is never made by the rollout team alone.

## Responsible AI considerations

Guidance for each wave reminds people that outputs from their own mail and documents can still be wrong or incomplete,
and that decisions about people require the organisation's approved process. Roles that make such decisions get
specific guidance before their wave starts.

## Evaluation requirements

Before each wave, test the group's priority scenarios with two or three members on their real content, and record
whether results were usable and verifiable. Failures go back to work context readiness or scenario design, not into
the launch.

## Value measures

Track, at team or role level, the share of licensed people using the priority scenarios, licence uptake by wave and
the outcome measures each scenario owner agreed, against baselines taken before the wave. The rollout owner owns the
plan measures; scenario owners own outcomes.

## Scale notes

### Starter

One or two waves, often a pilot group of mixed roles followed by a targeted second group. A single page plan with entry
gates and exit criteria is enough.

### Scale

Multiple waves by business unit or role family, each with gates and reviews, coordinated with the adoption programme
and a standing licence allocation review.

### Enterprise

Regional or business-unit wave plans under a common framework, with central licence allocation rules, shared exit
criteria and a portfolio view of uptake across waves.

## Hand-offs

- To `copilot-adoption:launch-plan` for onboarding and reinforcement per wave.
- To `m365-copilot:copilot-usage-reporting` for aggregate uptake reporting per wave.
- To `copilot-adoption:adoption-measurement` for outcome measurement.
- To `platform-governance:ai-licensing-and-capacity` for licence quantity and commercial questions.

## Reviewer gates

From risk tier 1, `security-privacy` reviews each wave's work context gate where the group handles sensitive content,
classifying findings as blocking or advisory. A blocking finding stops that wave until it is fixed or accepted in writing
by the accountable executive; it is not traded against the wave date.

## Failure modes

- Licences go to senior staff and enthusiasts by default, so early evidence reflects a few individuals rather than roles.
- Waves have no exit criteria, so problems from one wave are repeated in the next.
- A group starts before its oversharing findings are fixed, and an early incident damages trust in the whole rollout.
- Licence reallocation drifts into monitoring individuals, and trust with staff and employee representatives is lost.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Allocate licences by seniority or enthusiasm rather than by role, scenario and readiness.
- Start a wave without entry gates passed and exit criteria agreed.
- Use person-level activity data to judge individuals, or for reallocation without an agreed policy.
- State licence entitlements or commercial conclusions; route them to the licensing guide or a partner.
