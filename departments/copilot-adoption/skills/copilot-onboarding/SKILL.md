---
name: copilot-onboarding
description: Designs the onboarding experience each newly licensed or enabled Copilot user receives - access confirmed before the welcome, approved-use guidance in plain words, a first session on starting scenarios, first-week tasks and where to get help - as a repeatable flow for launch waves, new joiners and people changing role. Use when access is being switched on, when new joiners get Copilot with no guidance, or when onboarding was a one-off launch.
license: CC-BY-4.0
metadata:
  department: copilot-adoption
  lifecycle: Enable, Launch
  maturity: explorer, adopter, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, copilot-cowork
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-copilot-overview, ms-copilot-privacy
  status: draft
  authors: Simon Foote
---

# Copilot onboarding

## Purpose

The first few days with Copilot decide whether people treat it as part of their work or as something they tried once.
This skill designs the onboarding experience a person receives when they are licensed or enabled, as a repeatable flow
that works for a launch wave, a new joiner in month eight and someone whose role has just changed. It makes sure access
works before anyone is invited to use it, that approved use is understood, that the first tasks are relevant and that
help is easy to find. Onboarding usually goes wrong when it is a launch-day event that later joiners never see, when
the welcome arrives before access works, or when the first session tours features instead of real work.

## When to use

- Licences or Copilot Chat access are being switched on for a group and people need a consistent start.
- New joiners or movers receive Copilot through the normal provisioning process but no guidance follows.
- A launch included onboarding sessions, but nothing exists for people who join after the wave.
- Users report that Copilot "doesn't work" in ways that turn out to be access, app version or expectation problems.
- Licences are reassigned between people and the receiving person gets no introduction.

## When not to use

- Sequencing waves, dates and exit criteria for the launch - use `copilot-adoption:launch-plan`.
- Switching on licences and technical waves in the tenant - use `m365-copilot:m365-copilot-rollout`.
- Making Copilot Chat available safely to the whole workforce - use `m365-copilot:copilot-chat-rollout`.
- The deeper journey for a priority role after onboarding - use `copilot-adoption:role-based-adoption`.
- Teaching prompting and verification habits in depth - use `m365-copilot:prompting-practice`.
- Designing progressive learning pathways beyond the first weeks - use `learning-and-skills:ai-learning-pathway`.

## Questions to ask first

1. What triggers onboarding today - licence assignment, a wave date, joining the organisation, a role change - and who is told when it happens?
2. Which Copilot experiences will this person have on day one, and has IT confirmed they work on their devices?
3. What approved-use guidance applies, and can it be explained in a few plain sentences?
4. Which starting scenarios suit each audience, from the scenario catalogue?
5. Where does someone go with a question in their first week, and who answers it?

## Required inputs

- The audience model from `copilot-adoption:audience-segmentation` and starting scenarios from `copilot-adoption:scenario-discovery`.
- The approved-use guidance and the support route, including how to report suspected data exposure.
- IT confirmation of the access, app and device position for each audience.
- The provisioning process that assigns access, with a named owner who can trigger onboarding from it.

If IT cannot confirm that access works for an audience, onboarding for that audience waits. If approved-use guidance
does not exist, onboarding is blocked and the gap goes back to `copilot-adoption:adoption-readiness`.

## Decision framework

Design one flow with stages, then vary format by audience rather than designing separate flows.

| Stage | Purpose | Typical content |
|---|---|---|
| Before access | Make sure it works | Access, app versions and sign-in checked by IT for the audience |
| Welcome | Explain why and what next | Short message from the sponsor or manager, approved-use guidance, starting scenarios, where to get help |
| First session | Show it working on real work | Three to five starting scenarios done live, verification shown, questions answered |
| First week | Build confidence | Two or three small tasks on the person's own work; office hours available |
| First month check | Catch problems early | Short pulse at team level; route recurring issues to support or guidance owners |

Each entry route needs a trigger and an owner.

| Entry route | Trigger | Onboarding |
|---|---|---|
| Launch wave | Wave start date | Full flow with live first session |
| New joiner | Access assigned during joining | Welcome and recorded or self-paced first session, plus next scheduled live session |
| Mover or role change | Role change in HR or access change | Role-specific scenarios and a short welcome; skip what they already know |
| Access reassigned | Licence moved to a new person | Full welcome; never assume the previous holder's knowledge transfers |
| Copilot Chat only | Workforce-wide enablement | Lighter welcome focused on approved use, web grounding and verification |

Choose format by audience: live sessions for desk and hybrid waves, short shift-friendly or huddle formats for frontline
audiences, and self-paced material for everyone afterwards.

## Practitioner approach

Start by tracing what actually happens today when someone receives Copilot. Ask IT how access is assigned, who knows
when it happens and what the person sees. Very often the answer is that a licence appears and nothing else does. The
first design task is to attach a trigger to that moment, so onboarding begins without anyone remembering to start it.

Fix access before welcome. Nothing undermines confidence faster than an invitation to try something that is not there
or does not work on the person's device. Agree with IT that each audience's access is confirmed before its welcome is
sent, and give the support desk a short checklist for the common "it isn't there" cases.

Write the welcome for people, not for the programme. It should say in a few lines why the organisation is using
Copilot, what it is good for in their work, the approved-use guidance in plain words, three starting scenarios, and
where to get help. A message from the person's manager or sponsor is read more than one from a central mailbox.

Make the first session about real work. Use realistic, fictional or approved material from the audience's own domain,
do the starting scenarios live, and show verification every time: check the summary against the source, check figures,
check that the draft says what you mean. Show what to do when the answer is wrong. Record the session, keep it short,
and make sure later joiners can reach a live session within a few weeks.

Give the first week a shape. Two or three small tasks on the person's own work, chosen from the starting scenarios,
are better than a long list of tips. Point to office hours, the Champions community and the scenario catalogue. Tell
managers what their new starters have been asked to try, so they can ask how it went.

Design for every entry route, not only the launch. New joiners and movers are a steady stream that outlasts any wave.
Hand the welcome, recorded session and first-week tasks to whoever owns business-as-usual onboarding, and fold Copilot
into the organisation's wider joiner process where possible.

Close the loop. A short pulse at around a month, reported at team level, tells you whether access, guidance and
starting scenarios are working. Feed recurring problems to the support and guidance owners, and update the onboarding
material whenever Copilot or the guidance changes.

## Outputs

- An onboarding flow recorded in the onboarding section of the `adoption-plan` template: stages, entry routes, triggers, owners and formats by audience.
- A welcome message template for each audience, approved by the sponsor or manager who will send it.
- A first-session outline with starting scenarios, verification demonstrations and approved-use guidance.
- A first-week task card per audience, drawn from the `scenario-catalogue`.
- A business-as-usual hand-over note for joiner and mover onboarding.

## Microsoft platform considerations

What a person sees on day one differs between Copilot Chat, Copilot in the Microsoft 365 apps and Copilot Cowork, and
between desktop, web and mobile. Onboarding material must match the experience each audience actually has and must be
refreshed as Microsoft changes the interface or naming. Confirm current capability, availability and data handling
against `references/sources.md` before each refresh.

## Adoption considerations

Onboarding is the first adoption moment, so tie it to manager expectations and the Champions community from the start.
A welcome that arrives with a manager's message and a named local Champion is far more effective than a generic email.

## Knowledge considerations

People's first questions are often about the organisation's own policies and procedures. Note where onboarding
scenarios fail because content is stale or hard to find, and pass the pattern to
`knowledge-management:knowledge-gap-analysis`.

## Security and privacy considerations

Every onboarding route covers the approved-use guidance, what data Copilot can draw on, and how to report suspected
data exposure. Demonstrations use fictional or approved material only. Do not send welcomes to audiences whose
permissions position has not been reviewed.

## Responsible AI considerations

Onboarding teaches verification as the default habit and makes clear that people remain accountable for anything they
use or send. Say plainly what Copilot is not suited to, and that its output must not be the sole basis for decisions
about people.

## Evaluation requirements

Not applicable as solution evaluation, because onboarding is an adoption design rather than an AI solution. The flow is
reviewed against the first-month pulse and support demand for access and expectation problems.

## Value measures

Owned by the adoption lead, with a baseline from the first wave: time from access to first use at team level, share of
newly enabled people reached by a first session, access-related support requests in the first fortnight, and pulse
results by audience. Reported above the minimum group size, never for individuals.

## Scale notes

### Starter

One welcome message, one recorded first session and a monthly live session, with the owner told by IT when access is
assigned.

### Scale

A triggered flow per audience, live first sessions for each wave, a business-as-usual route for joiners and movers, and
a first-month pulse.

### Enterprise

Onboarding integrated with the organisation's joiner and mover processes, localised material, regional live sessions
and a central owner who refreshes content as Copilot changes.

## Hand-offs

- To `copilot-adoption:adoption-reinforcement` once the first month ends.
- To `copilot-adoption:role-based-adoption` for people in priority roles.
- To `copilot-adoption:adoption-support-model` for the help routes the welcome points to.
- To `learning-and-skills:ai-learning-pathway` for learning beyond the first weeks.

## Reviewer gates

Not applicable as a formal gate, because onboarding to approved Copilot experiences at tiers 0 and 1 relies on the
readiness assessment, where `security-privacy` has already reviewed data and permissions hygiene.

## Failure modes

- The welcome arrives before access works, and the first experience is a support ticket.
- Onboarding happens only at launch, so later joiners and movers receive nothing.
- The first session tours features, and people cannot see how Copilot fits their work.
- Verification is mentioned but never shown, and early mistakes damage trust.
- Material goes stale as the interface changes, and users stop trusting the guidance.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Send a welcome before IT has confirmed access works for that audience.
- Onboard people without the approved-use guidance and the route for reporting data exposure.
- Use real personal or confidential data in onboarding demonstrations.
- Treat onboarding as a launch event with no route for later joiners and movers.
