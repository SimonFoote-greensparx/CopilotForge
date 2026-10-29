---
name: frontline-enablement
description: Enables frontline and deskless workers to adopt AI safely - confirming with IT and the licensing route which experience and device each frontline audience can use, choosing a few shift-relevant scenarios, teaching in huddles and on mobile within paid time, involving supervisors and employee representatives, and adapting support and Champions. Use when frontline teams join a rollout, were left out of one, or found desk-based training useless.
license: CC-BY-4.0
metadata:
  department: copilot-adoption
  lifecycle: Envision, Enable, Launch
  maturity: adopter, scaler, ai-enterprise
  risk-tiers: 0, 1, 2
  platforms: copilot-chat, m365-copilot, m365-agents, entra
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-adoption-hub, ms-copilot-overview, ms-copilot-privacy, ms-champion-best-practice
  status: draft
  authors: Simon Foote
---

# Frontline enablement

## Purpose

Frontline and deskless workers - in stores, plants, depots, wards, sites and vehicles - are often the largest part of
the workforce and the last to be considered in an AI programme. This skill enables them to adopt AI in ways that fit
their work: the right access on the devices they actually carry, a handful of scenarios that help during a shift,
learning delivered in paid time and in the formats they use, and support from supervisors and peers who understand
their work. It usually goes wrong when office onboarding is reused for people who have ten minutes between tasks, when
access decisions are assumed rather than confirmed, or when scenarios ignore safety, customer contact and the
sensitivity of the information involved.

## When to use

- Frontline or deskless teams are being included in a Copilot or agent rollout for the first time.
- A previous rollout left frontline teams out, or included them with desk-based sessions that did not land.
- A business leader wants AI to help shift workers with procedures, handovers or customer questions.
- Supervisors ask how they are supposed to make time for AI learning on a full rota.
- Employee representatives or works councils have raised questions about AI in frontline roles.

## When not to use

- Defining frontline Copilot scenarios and their product constraints in detail - use `m365-copilot:copilot-for-frontline`.
- Grouping the whole workforce into audiences - use `copilot-adoption:audience-segmentation`.
- Sequencing waves across the organisation - use `copilot-adoption:launch-plan`.
- Deciding licences, plans or capacity for frontline staff - use `platform-governance:ai-licensing-and-capacity`, ending with the Microsoft licensing guide or a licensing partner.
- Designing an agent that frontline workers will use - use `opportunity-management:ai-suitability`, then `m365-agents:agent-use-case-design`.
- Assessing how frontline roles will change - use `change-and-communications:people-change-impact`.

## Questions to ask first

1. Which frontline audiences are in scope, what devices do they use at work (personal, shared, kiosk, none), and do they have an organisational identity and mailbox?
2. Which AI experience, if any, has IT confirmed each audience can use, and what has the licensing route said about it?
3. Where in a shift could AI genuinely help - procedures, handovers, customer questions, reporting - and where would it be unsafe or unwelcome?
4. How will learning happen in paid time, given rotas, shift patterns, languages and literacy needs?
5. Who needs to be consulted - supervisors, health and safety, HR, employee representatives - before anything is introduced?

## Required inputs

- The frontline audiences from `copilot-adoption:audience-segmentation`, with work patterns and devices.
- IT's confirmed position on identity, devices and which AI experiences each audience can use, and any decision from the licensing route.
- Frontline scenarios from `m365-copilot:copilot-for-frontline` or `copilot-adoption:scenario-discovery`.
- HR's position on paid learning time and any consultation obligations with employee representatives.
- The approved-use guidance, adapted where frontline work involves customers, patients, safety or personal data.

If access is not confirmed, do not promise frontline teams anything; plan awareness and consultation first. Licensing
questions end with the Microsoft licensing guide or a licensing partner, never with an assumption. If consultation with
employee representatives is required, it comes before any pilot.

## Decision framework

Start with the access pathway, because it decides what is possible.

| Situation | What to confirm with IT and the licensing route | Typical enablement |
|---|---|---|
| Organisational identity on a personal or issued mobile device | Which AI experiences are available on mobile, device management and data rules | Short mobile-first scenarios, huddle learning |
| Shared or kiosk devices | Sign-in model, session clearing, whether AI use is appropriate on shared devices | Awareness and supervised scenarios only until confirmed safe |
| No organisational identity or device | Whether access is planned at all | Awareness, supervisor-led use, or a deliberate decision to defer |
| Access to an agent for procedures or questions | Owner, grounding, risk tier and support route for the agent | Agent-specific briefing once the agent is released |

Test each scenario before including it.

| Test | Include when |
|---|---|
| Fits the shift | Can be done in a few minutes on the device in use |
| Verifiable | The worker or supervisor can tell if the output is wrong |
| Safe | Does not replace a safety-critical procedure or a professional judgement |
| Appropriate content | Does not expose customer, patient or colleague personal data beyond what the role already sees |
| Welcome | Workers and their representatives see it as help, not surveillance |

## Practitioner approach

Go and see the work. Spend time with supervisors and workers on shift, not only with their managers' managers. Watch
handovers, look at how procedures are found, listen to the questions customers ask. Note the devices people actually
carry and when they have a few minutes. Frontline enablement designed from head office usually solves the wrong problem.

Settle access before building enthusiasm. Work with IT to confirm, audience by audience, what is possible on the
devices in use, and with the licensing route for anything that depends on entitlement. Be honest with frontline teams
about what they will and will not have. Promising "AI for everyone" and then delivering it only to desk staff damages
trust for years.

Choose few scenarios and make them excellent. Two or three shift-relevant uses that pass the tests above are enough to
start: finding the right section of a procedure, drafting a handover note, preparing for a customer conversation,
translating a notice. Test each on real work with workers and supervisors, and drop any that fail the safety or
content test.

Teach in the flow of the shift. Short huddle sessions led by supervisors or frontline Champions, quick-reference cards
on the device, and short videos work better than long sessions. Learning must happen in paid time; agree this with HR
and supervisors before launch. Provide material in the languages and reading levels the audience needs, and check
accessibility.

Make supervisors the centre of enablement. They control time, set expectations and see whether something helps. Give
them a short briefing, the scenarios, the approved-use guidance and a simple way to report what is and is not working.
Recruit frontline Champions through `champions:champion-recruitment`, with agreed time on the rota.

Consult early where AI touches frontline roles. Employee representatives and works councils often have legitimate
questions about monitoring, workload and job design. Bring HR in, explain what the programme will and will not do, and
make clear that usage data is never used to judge individuals. Legal and employment questions go to the organisation's
legal adviser and HR.

Adapt support. Frontline workers cannot always raise a ticket or attend office hours. Route questions through
supervisors and frontline Champions, keep the data exposure route simple and mobile-friendly, and schedule help around
shifts.

## Outputs

- A frontline enablement plan recorded in the waves, onboarding and support sections of the `adoption-plan` template: audiences, access pathway, scenarios, formats, supervisor role, consultation and support.
- An access decision record per frontline audience, with what IT and the licensing route confirmed and what remains open.
- Tested frontline scenarios entered in the `scenario-catalogue`, with the safety and content test recorded.
- A supervisor briefing pack and quick-reference cards for the device in use.
- A consultation record with HR and employee representatives where applicable.

## Microsoft platform considerations

What frontline workers can use depends on identity, device management, mobile experiences and licensing, all of which
change. Shared devices raise specific sign-in and session questions. Confirm each point with IT and check
`references/sources.md`; never state licensing conclusions, and route them to the Microsoft licensing guide or a
licensing partner. Agents for frontline use follow the organisation's agent governance like any other agent.

## Adoption considerations

Frontline adoption is won by supervisors and peers, not central campaigns. Time frontline waves around operational
peaks, include frontline stories in communications, and make sure frontline Champions are recognised on equal terms.

## Knowledge considerations

Frontline scenarios often depend on procedures, product information and policies that are out of date or scattered.
Assess that content before promoting scenarios that ground on it, and pass gaps to
`knowledge-management:knowledge-gap-analysis`; an AI answer from a stale procedure is worse than no answer.

## Security and privacy considerations

Shared devices, customer contact and personal data in frontline work raise specific risks. Confirm session handling on
shared devices, keep scenarios away from data the role should not see, and make the data exposure route easy to use on
mobile. Usage data is never used to monitor frontline workers. Data protection questions end with the organisation's
DPO.

## Responsible AI considerations

Frontline AI use can affect customers, patients and safety. AI must not replace safety-critical procedures or
professional judgement, and any scenario that informs decisions about people goes through risk classification. Workers
are told plainly that AI use will not be used to assess their individual performance.

## Evaluation requirements

Each frontline scenario is tested on real work with workers and supervisors against the five tests before release.
Where frontline workers will use an agent, its evaluation follows `m365-agents:agent-testing` before the agent reaches
them.

## Value measures

Owned by the business owner of each frontline audience with the adoption lead, with baselines before the pilot: time to
find procedures or complete handovers where observable at team level, supervisor-reported usefulness, scenarios in use
by site or team, and support themes. Reported above the minimum group size, never for individuals.

## Scale notes

### Starter

One frontline audience, two or three tested scenarios, supervisor-led huddles and a clear statement of what is and is
not available yet.

### Scale

Several frontline audiences with confirmed access pathways, frontline Champions on the rota, localised material and
consultation with representatives where required.

### Enterprise

A frontline enablement model shared across regions and sites, consistent access decisions, multilingual material,
frontline-specific agents through the CoE, and consultation built into the programme governance.

## Hand-offs

- To `m365-copilot:copilot-for-frontline` for scenario detail and product constraints.
- To `champions:champion-recruitment` to recruit frontline Champions with rota time.
- To `opportunity-management:ai-suitability` when a frontline need points to an agent.
- To `copilot-adoption:adoption-support-model` to adapt support for shifts and mobile.
- To `change-and-communications:people-change-impact` for role impact and consultation.

## Reviewer gates

`security-privacy` reviews shared-device use, customer and personal data in frontline scenarios and the mobile data
exposure route before the first frontline wave. Unconfirmed session handling on shared devices is blocking; other
findings are usually advisory. Frontline agents follow the gates set by their risk tier.

## Failure modes

- Desk-based onboarding is reused for shift workers, who cannot attend and see no relevance.
- Access is promised before it is confirmed, and frontline trust is lost when it does not arrive.
- Learning is expected in unpaid time, and participation collapses.
- A scenario quietly replaces a safety procedure or exposes customer data on a shared device.
- Representatives hear about AI in frontline roles from rumour rather than consultation.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Promise frontline teams access that IT and the licensing route have not confirmed.
- Expect frontline learning to happen in unpaid time.
- Let AI replace a safety-critical procedure or professional judgement.
- Use AI usage data to monitor or assess frontline workers.
