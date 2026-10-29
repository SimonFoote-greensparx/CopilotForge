---
name: adoption-support-model
description: Designs the user support model for Copilot - self-help, Champions as first-line peer guidance, office hours, the IT service desk, admin escalation to Microsoft, the security route for suspected data exposure and the intake route for ideas - with triage categories, capacity and a feedback loop. Use when Copilot is about to launch, when Champions or the service desk are overwhelmed, or when nobody knows where Copilot questions go.
license: CC-BY-4.0
metadata:
  department: copilot-adoption
  lifecycle: Mobilise, Launch, Improve
  maturity: explorer, adopter, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, copilot-cowork, m365-agents
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-adoption-hub, ms-champion-best-practice, ms-copilot-privacy, ms-copilot-overview
  status: draft
  authors: Simon Foote
---

# Adoption support model

## Purpose

People using Copilot ask questions that do not fit a traditional service desk: "how do I", "why did it say that", "is
it allowed to use this file", "could we build an agent for this". This skill designs a support model that sends each
kind of need to the right place, from self-help and peers through the service desk to security and opportunity intake,
with enough capacity and a feedback loop that improves guidance over time. Support models usually go wrong in one of
two ways: everything lands on the service desk, which cannot answer usage questions, or everything lands on Champions,
who become an unpaid help desk and burn out.

## When to use

- Copilot is about to launch to a new audience and the support route must be ready first.
- The service desk receives Copilot "how do I" questions it cannot answer, or closes them unhelpfully.
- Champions report that most of their time goes on support rather than on spreading capability.
- Users do not know where to report a worrying answer, a suspected data exposure or an idea.
- A readiness assessment has rated the support route as not ready.

## When not to use

- Support, monitoring and incident handling for deployed agents and AI solutions - use `ai-operations:ai-support-model`.
- Managing an AI incident or harm once reported - use `ai-operations:ai-incident-management`.
- Running office hours and drop-in clinics as a learning service - use `learning-and-skills:office-hours`.
- Setting the Champions' role and boundaries in the programme charter - use `champions:champion-programme-design`.
- Sequencing the launch the support model serves - use `copilot-adoption:launch-plan`.

## Questions to ask first

1. What types of Copilot need are arising or expected - how-to, access, faults, answer quality, data concerns, ideas - and roughly in what proportion?
2. What can the service desk handle today, what knowledge articles does it have, and who can escalate to Microsoft on its behalf?
3. What time have Champions agreed to give, and what is outside their boundary?
4. What is the agreed route for suspected data exposure, and who owns it out of hours?
5. Where do ideas for shared prompts, Cowork tasks or agents go, and who responds?
6. How will repeated questions reach the owners of guidance, scenarios and training?

## Required inputs

- The approved-use guidance and the readiness assessment from `copilot-adoption:adoption-readiness`.
- The service desk's current scope, tooling and escalation routes, from the IT service owner.
- The Champions boundary and time commitment from `champions:champion-programme-design`, where a programme exists.
- The security route for suspected data exposure, agreed with `security-privacy`.
- The opportunity intake route from `opportunity-management:problem-framing` or the CoE.

If no data exposure route exists, the support model cannot be signed off and the launch is blocked. If no intake route
exists, record it as a gap; otherwise ideas will accumulate with Champions and the service desk.

## Decision framework

Design tiers by type of need, not by seniority of the person answering.

| Tier | Handles | Owner |
|---|---|---|
| Self-help | Getting started, approved use, starting scenarios, known issues | Adoption lead (content), guidance owners |
| Peer guidance | "How do I do this in my work" questions, prompt tips, showing good practice | Champions, within agreed time and boundary |
| Office hours | Questions needing a demonstration or discussion; recurring themes | Adoption team with Champions |
| Service desk | Access, licence assignment, app and sign-in faults, errors | IT service desk |
| Admin and vendor escalation | Tenant settings, service issues, faults needing Microsoft support | Microsoft 365 administrators |
| Security route | Suspected data exposure, oversharing, sensitive content in answers | Security and privacy owner |
| Intake | Ideas for shared prompts, Cowork tasks, agents or automation | Opportunity intake or CoE |

Triage each contact into one category and route it. Answer-quality reports need particular care.

| Category | Example | Route |
|---|---|---|
| How-to | "How do I summarise this thread?" | Self-help, then Champions or office hours |
| Access | "Copilot isn't in my app" | Service desk |
| Fault | Error messages, features failing for many users | Service desk, then admin escalation |
| Answer quality | "It gave me a wrong figure" | Guidance on verification; repeated patterns to the adoption lead and, for agents, the agent owner |
| Data concern | "It showed me a file I shouldn't see" | Security route immediately |
| Idea | "Could we build an agent for onboarding packs?" | Intake |

## Practitioner approach

Start from the needs, not the org chart. List the questions people are likely to ask in their first months, using
support logs from pilots, Champion feedback and the readiness findings. Group them into the categories above and
decide where each should go. Most organisations find that the largest category is how-to, which the service desk is
least able to answer.

Build self-help first, because it scales and is available at three in the morning. A short getting-started page, the
approved-use guidance in plain words, starting scenarios by audience, a known-issues list and the routes for
everything else will deflect many contacts. Give it an owner and a review rhythm; stale self-help creates more contacts
than it prevents.

Agree the service desk's part explicitly. Give the desk knowledge articles for access and common faults, a triage
script that recognises how-to questions and routes them to self-help or office hours, and clear escalation to
administrators. Agree that "Copilot gave a wrong answer" is not closed as user error: the desk explains verification,
records the pattern and passes repeated themes on.

Use Champions as first-line peer guidance within a boundary. They answer how-to questions in their own teams and model
good practice, inside the time their managers agreed. They do not handle faults, access, data concerns or approvals.
Make the boundary visible to users as well as Champions, so people know what to ask whom.

Make the security route unmistakable. Every user should know, from onboarding onwards, how to report something they
should not have seen. The route must be fast, owned out of hours where needed, and connected to whoever manages
permissions remediation. Test it before launch with a walk-through.

Size capacity for the launch peak, then for steady state. Contacts are highest in the weeks after each wave. Add
office hours during those weeks rather than stretching Champions, and agree with the service desk how it will flex.

Close the loop. Review contact themes regularly with the adoption lead, guidance owners and the service desk. Repeated
how-to questions mean the self-help or onboarding is weak; repeated answer-quality reports may point to knowledge
problems or unsuitable scenarios. Publish what changed, so users see that reporting helps.

## Outputs

- An adoption support model on the `adoption-support-model` template: tiers, triage categories, routes, owners, hours, capacity plan, Champion boundary and feedback loop.
- A self-help content list with owners and review dates.
- Service desk knowledge articles and a triage script for Copilot contacts.
- A tested security route for suspected data exposure, recorded with its owner.
- The support row of the `adoption-plan` template completed for each wave.

## Microsoft platform considerations

The service desk and administrators need to know which Copilot experiences each audience has, where tenant settings
are managed, and how to raise a support request with Microsoft. Admin roles, reporting and support routes change;
confirm current details against `references/sources.md`. Support for agents built in Agent Builder or Copilot Studio
follows each agent's own support route, set through `ai-operations:ai-support-model`.

## Adoption considerations

Good support is an adoption lever: people experiment more when help is easy to find and does not make them feel
foolish. Point every onboarding message and reinforcement nudge at the same simple set of routes.

## Knowledge considerations

Self-help content and service desk articles are knowledge assets that need owners, versions and review dates. Repeated
answer-quality reports on organisational content should go to `knowledge-management:knowledge-gap-analysis`.

## Security and privacy considerations

The data exposure route is the critical part of this model. It must be known to every user, fast, owned and connected
to permissions remediation. Contact records may contain personal data or sensitive content; keep only what is needed
and restrict access. Data protection questions end with the organisation's DPO.

## Responsible AI considerations

Reports of harmful, biased or misleading output are taken seriously and routed to the right owner, never dismissed as
user error. Users are reminded that they remain accountable for output they use, and support staff explain
verification rather than promising accuracy.

## Evaluation requirements

Not applicable as solution evaluation, because this skill designs a support service rather than an AI solution. The
model is tested before launch by walking sample contacts from each category through their routes.

## Value measures

Owned by the adoption lead with the IT service owner, with baselines from the first wave: contacts by category, share
resolved through self-help or peers, time to resolve access issues, data concerns handled within the agreed time, and
repeat themes fixed at source. Reported at team or audience level, never for individuals.

## Scale notes

### Starter

A one-page self-help guide, the service desk briefed with a few knowledge articles, a named security contact, a weekly
office hour and a simple route for ideas.

### Scale

Tiered model with triage script, Champions inside a published boundary, office hours flexed around waves, a tested
security route and a monthly theme review.

### Enterprise

A consistent model across regions with local self-help, service desk integration, follow-the-sun security handling,
admin escalation to Microsoft and theme reporting to the CoE.

## Hand-offs

- To `ai-operations:ai-support-model` for the support of individual agents and AI solutions.
- To `learning-and-skills:office-hours` to run office hours as a service.
- To `champions:champion-programme-design` when the boundary or time commitment needs revisiting.
- To `copilot-adoption:adoption-reinforcement` with repeated themes that need a refresher.
- To `security-privacy` for the data exposure route and its testing.

## Reviewer gates

`security-privacy` reviews the data exposure route and the handling of contact records before the first launch wave.
Its absence is blocking for launch at any tier; other findings are advisory unless they leave sensitive content
exposed.

## Failure modes

- Every Copilot contact goes to the service desk, which closes how-to questions as out of scope.
- Champions become the default help desk, burn out and leave the programme.
- Users cannot find the route for suspected data exposure, so incidents surface late or not at all.
- Answer-quality reports are dismissed, and genuine knowledge or scenario problems persist.
- Self-help goes stale and creates more contacts than it prevents.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Launch without a known, tested route for suspected data exposure.
- Make Champions responsible for faults, access, data concerns or approvals.
- Close answer-quality reports as user error without recording the pattern.
- Report support contacts by named individual.
