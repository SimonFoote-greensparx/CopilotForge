---
name: copilot-chat-rollout
description: Plans a safe workforce-wide rollout of Copilot Chat as the organisation's approved everyday AI assistant, deciding settings for web grounding, agents and app placement, approved-use guidance, displacement of unapproved AI tools, light-touch enablement and the route to licensed Copilot. Use when Copilot Chat is to be made available to everyone, when staff use consumer AI tools for work, or when Chat was enabled with no plan.
license: CC-BY-4.0
metadata:
  department: m365-copilot
  lifecycle: Mobilise, Enable, Launch
  maturity: explorer, adopter, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, entra, purview
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-overview, ms-copilot-privacy, ms-copilot-adoption-hub
  status: draft
  authors: Simon Foote
---

# Copilot Chat rollout

## Purpose

Copilot Chat is often the first Microsoft AI capability that reaches the whole workforce, and for many people it will
be the only one for some time. This skill makes that rollout deliberate: settings decided, guidance written, people
shown how to use it well, and a clear message that it is the approved place for AI-assisted work instead of unapproved
consumer tools. It usually goes wrong when Chat simply appears in people's apps one morning with no explanation, so
usage stays shallow, unapproved tools carry on, and nobody can say what the organisation decided about web content or
agents.

## When to use

- Copilot Chat is to be made available to all or most staff and nobody has written down how.
- Staff are known to be pasting work content into consumer AI tools and the organisation wants a safe alternative.
- Copilot Chat has already been switched on without communication, guidance or a settings review.
- Leaders want a broad, low-cost first step before deciding where licensed Microsoft 365 Copilot is worth it.

## When not to use

- Rolling out licensed Microsoft 365 Copilot to selected roles in waves - use `m365-copilot:m365-copilot-rollout`.
- Confirming identity, apps, oversharing controls and admin settings at tenant level - use `m365-copilot:copilot-technical-readiness`.
- Sequencing the people-side launch, persona onboarding and reinforcement for the whole adoption programme - use `copilot-adoption:launch-plan`.
- Teaching prompting and verification in depth - use `m365-copilot:prompting-practice`.
- Deciding whether staff may use non-Microsoft AI tools at all - an acceptable-use policy matter for the `ai-centre-of-excellence` governance model through `ai-centre-of-excellence:coe-governance-model`.

## Questions to ask first

1. What is the organisation's position on staff using unapproved AI tools for work today, and is that written down?
2. Which Copilot Chat settings matter here (web content, agents users can find, where Chat appears in apps), and who decides each?
3. Which groups should not receive Chat yet, and why (for example, roles under specific regulatory restrictions)?
4. What short approved-use guidance exists, covering what may and may not be entered and how to check outputs?
5. How will people move from Chat to licensed Microsoft 365 Copilot or to agents, and what evidence will inform that?

## Required inputs

- A technical readiness verdict for the workforce from `m365-copilot:copilot-technical-readiness`.
- The organisation's acceptable-use, information security and AI policies, and the owner of each.
- Current Copilot Chat settings and the admin who owns them.
- Any knowledge of unapproved AI tool use, from security tooling or staff surveys, at aggregate level.
- The communications channels that reach the whole workforce, including frontline staff.

Where approved-use guidance does not exist, writing it is the first task, not an optional extra. Never assume what
Copilot Chat includes, how it handles data or who is entitled to it; confirm with the source records and the licensing route.

## Decision framework

| Decision | Recommended default | Change the default when |
|---|---|---|
| Audience | Everyone with a work identity, minus named exclusions with reasons | Regulatory or works-council constraints require a phased or consulted start |
| Web content | Decide explicitly and explain the choice to users | Policy requires stricter control over queries leaving the tenant boundary |
| Agents available in Chat | Only agents that are approved and registered | A governed agent catalogue is not yet in place, in which case restrict |
| Placement in apps | Make Chat easy to find in the apps people already use | Change fatigue or a concurrent major change argues for a quieter start |
| Unapproved tools | Position Chat as the approved alternative, then apply technical controls in line with policy | No approved alternative exists for a specific need yet |
| Enablement | Short guidance, a few starter scenarios, office hours | High-risk roles need mandatory briefing before access |
| Path to licensed Copilot | Use aggregate demand signals and role scenarios to target licences | Leadership has already fixed the licensed audience |

Every row needs an owner and a recorded reason. Where a decision depends on a feature, check that it exists and how it is
licensed in the current source records before relying on it.

## Practitioner approach

Start with the policy question, because the rollout is only as clear as the organisation's position on AI use. Agree
with the information security lead and the policy owner what Copilot Chat is approved for, what must never be entered
and what happens to unapproved tools. Write that as one short page in plain language. People will not read a long
policy, but they will read a page that says "use this, not that, and check what it tells you".

Next, walk through the settings with the tenant admin and record a position on each. The questions that matter most
are whether web content is used and how that is explained, which agents people can discover and use from Chat, and
where Chat appears in the apps. Microsoft changes these controls often; check the current source records and admin
documentation, and date the decisions.

Then design light-touch enablement for a very large audience. Pick five to eight starter scenarios that work without
organisational data in the prompt context or with files people attach themselves: drafting, rewriting for a different
audience, summarising a document they have open, structuring a plan, explaining a concept. Each scenario needs a
verification habit, drawn from `m365-copilot:prompting-practice`. Make sure frontline and non-desk staff are reached
through the channels they actually use.

Address unapproved tools carefully. Telling people to stop without offering a safe alternative drives use underground;
offering the alternative first and then applying technical controls in line with policy works better. Keep any
measurement of unapproved use at aggregate level.

Finally, treat Chat as the discovery ground for what comes next. Collect aggregate signals through
`m365-copilot:copilot-usage-reporting`, office hours and feedback about which roles keep hitting the limits of Chat
because they need their mail, meetings and files in context. That evidence informs where licensed Copilot pays back,
through `m365-copilot:m365-copilot-rollout`, and which repeated needs warrant agents. Licensing conclusions themselves go
to the licensing guide or a partner.

## Outputs

- A Copilot Chat rollout decision record: audience, exclusions, each setting position with reason and owner.
- One-page approved-use guidance for all staff.
- A starter scenario set with verification habits, suitable for the whole workforce.
- A demand signal summary, at role or team level, feeding licensed Copilot and agent decisions.

## Microsoft platform considerations

Copilot Chat's scope, data handling, web grounding behaviour, agent access and entitlement are described in
`ms-copilot-overview` and `ms-copilot-privacy`, and they change frequently. Do not state what is included or how it is
licensed without checking the current records. Settings sit in the Microsoft 365 admin centre and related admin
experiences; identity and conditional access come from Microsoft Entra; labels and data loss prevention from Microsoft
Purview.

## Adoption considerations

Workforce-wide availability is not adoption. Pair the rollout with the communications and reinforcement planned in
`copilot-adoption:launch-plan`, involve Champions where they exist, and make office hours available in the first weeks.
Explain the "why" in terms of safety and everyday usefulness rather than features.

## Knowledge considerations

Not applicable in depth, because Chat's starter scenarios rely mainly on content people supply themselves; where agents
in Chat ground on organisational knowledge, that is handled through `m365-agents:agent-grounding`.

## Security and privacy considerations

The core risks are sensitive content being entered without a decision on how it is handled, and web content being used
without users understanding it. Confirm data handling with the source records, record the decisions, and route any
open question to the `security-privacy` department and the data protection lead.

## Responsible AI considerations

Guidance must tell people that they remain responsible for what they do with outputs, that outputs can be wrong, and
that Chat must not be used to make or justify decisions about individuals without the organisation's approved process.

## Evaluation requirements

Before broad release, test the starter scenarios with a small mixed group, including frontline staff, and confirm the
guidance is understood. Check that the settings behave as decided using test accounts.

## Value measures

Baseline unapproved AI tool use and staff confidence before rollout, at aggregate level, then track the share of the
workforce using Chat, the spread across roles, and the reduction in unapproved tool use. The adoption lead owns these
measures; they are reported at team or role level only.

## Scale notes

### Starter

Write the one-page guidance, decide the main settings, announce through existing channels and run weekly office hours
for the first month. Keep the decision record short.

### Scale

Run the rollout through the adoption programme with Champions, a starter scenario library per major role family, and a
monthly review of aggregate demand signals for licensed Copilot.

### Enterprise

Coordinate settings centrally with regional variation only where law or consultation requires it, localise guidance,
and link demand signals to the licensing and capacity process.

## Hand-offs

- To `copilot-adoption:launch-plan` for the people-side launch and reinforcement.
- To `m365-copilot:copilot-usage-reporting` for aggregate usage reporting.
- To `m365-copilot:m365-copilot-rollout` when demand evidence supports licensed Copilot for specific roles.
- To `platform-governance:ai-licensing-and-capacity` for licensing questions.

## Reviewer gates

From risk tier 1, the settings decision record and the approved-use guidance are reviewed by `security-privacy`, which
classifies findings as blocking or advisory. A blocking finding on data handling stops the broad release until fixed or
accepted in writing by the accountable executive.

## Failure modes

- Chat appears without explanation, so people treat it as a novelty and keep using consumer tools for real work.
- Web content and agent settings are left at defaults that nobody can explain to staff or auditors.
- Frontline staff are excluded by accident because communications only reach desk workers.
- Unapproved tools are blocked before an alternative is available, and use moves to personal devices.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- State what Copilot Chat includes, how it handles data or who is entitled to it without checking the current source records.
- Switch Chat on for the workforce without approved-use guidance and recorded setting decisions.
- Measure or report unapproved AI tool use or Chat usage by named individual.
- Present Chat as a replacement for checking outputs or for the organisation's approved decision processes.
