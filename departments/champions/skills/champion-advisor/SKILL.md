---
name: champion-advisor
description: Specifies the Champions advisor, a self-service agent that explains requirements, routes, criteria and next steps from the champion guide - its question set, grounding, what it must refuse such as verification decisions and other people's status, escalation and test questions - before agent design. Use when the programme owner is a bottleneck for questions, or when a Champions advisor is proposed or misbehaving.
license: CC-BY-4.0
metadata:
  department: champions
  lifecycle: Enable, Deliver, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2
  platforms: m365-agents, copilot-studio, sharepoint
  edition-support: scale, enterprise
  reviewers: security-privacy, evaluation-quality
  sources: ms-agent-builder, ms-declarative-agents, ms-agents-compare, ms-copilot-studio-guidance, ms-champion-programme
  status: draft
  authors: Simon Foote
---

# Champion advisor

## Purpose

As a Champions programme grows, the same questions reach the programme owner every day: what do I need to submit, which
route suits me, what happens after verification, can I count this session. A Champions advisor answers these from the
published guide at any hour, freeing the owner for work only they can do, and gives Champions a live, governed example
of a useful agent. This skill specifies what the advisor should know, answer, refuse and escalate, and how to test it,
then hands the brief to the agent design route. It usually goes wrong when the advisor is asked to decide whether
someone is verified, when it can see other participants' records, or when the guide it grounds on goes stale.

## When to use

- The programme owner or assessors spend much of their time answering the same questions about requirements and next steps.
- The charter calls for self-service guidance and agent building is approved, so an advisor is preferred to a static guide.
- An advisor already exists and gives outdated, overconfident or out-of-scope answers.
- The programme wants the advisor to show participants their own progress and the risk of doing so needs thinking through.
- Champions working on agent capability need a safe, real example to study and help test.

## When not to use

- Deciding whether self-service guidance should be an agent at all - use `opportunity-management:ai-suitability`.
- Writing the agent brief, choosing the build tool and configuring the agent - use `m365-agents:agent-use-case-design`.
- Building the test plan and evaluation set in full - use `m365-agents:agent-testing`.
- Checking the guide and tracker as knowledge sources - use `m365-agents:knowledge-source-readiness`.
- Writing the champion guide the advisor explains - use `champions:champion-recruitment`.
- Assessing evidence and keeping the tracker - use `champions:evidence-assessment`.

## Questions to ask first

1. Which questions reach the programme owner most often, and which of them can be answered from the published guide alone?
2. Is the champion guide current, owned, versioned and stored where the advisor's users already have permission to read it?
3. Should the advisor give general guidance only, or also show each participant their own status, and has anyone weighed the extra risk?
4. Who owns the advisor's instructions, knowledge and review cycle, and who answers the questions it escalates?
5. Is agent building approved in the organisation, and through which governed route?

## Required inputs

- The published `champion-guide`, with an owner, version and review date, from `champions:champion-recruitment`.
- The capability framework, Challenge criteria and recognition model the guide summarises.
- A list of the questions the programme owner receives, grouped by theme, with names removed.
- The organisation's agent governance position and approved build tools, from `ai-centre-of-excellence:coe-governance-model` or the CoE.
- Where personal status is in scope, the tracker design and access rules from `champions:evidence-assessment`.

If the guide is incomplete or out of date, fix it first: an advisor over a poor guide gives confident wrong answers. If
agent building is not approved, publish the guide with a searchable question-and-answer section instead and record the
advisor as deferred.

## Decision framework

Fix the advisor's scope before anything is built.

| The advisor answers | The advisor refuses or redirects | The advisor escalates |
|---|---|---|
| Requirements for each stage, the two routes and the verification criteria | Whether a particular person is verified or recognised | Questions the guide does not answer |
| What good evidence looks like, using published exemplars | Anything about another participant | Appeals and disagreements with assessments |
| Challenge options, scope rules and how Challenges are assessed | Faults, access and licence problems (to the service desk) | Requests for exceptions to time or criteria |
| What recognition opens and how renewal works | Approval of agents or solutions (to intake) | Concerns about safety, data or conduct |
| Where things go: community, learning calendar, intake, service desk | Drafting evidence on the participant's behalf | Repeated questions showing the guide is unclear |

Choose the status option deliberately, because it changes the risk.

| Option | What it means | Implications |
|---|---|---|
| General guidance only | Grounded on the published guide and criteria; no personal data | Simplest; usually the right first release |
| Own status shown | Looks up the signed-in participant's stage in the tracker | Needs reliable identity, strict permission trimming and testing that nobody sees anyone else's record; reclassify the risk tier |
| Status changed by the advisor | The advisor updates records | Not recommended; status changes stay with assessors and the programme owner |

## Practitioner approach

Begin with the questions, not the tool. Collect the questions the programme owner, assessors and community manager
receive over a few weeks, remove names, and group them by theme. Most will be about requirements, routes, evidence,
Challenges and where to go for help. This list becomes both the advisor's scope and the backbone of its test set.

Fix the guide before grounding on it. Read the champion guide against the question list. Wherever a common question has
no clear answer in the guide, improve the guide; the advisor can only be as good as its source. Confirm the guide has an
owner, a version, a review date and permissions that match the advisor's audience.

Start with general guidance only. A first release that explains requirements and next steps from the published guide
solves most of the bottleneck with little risk. Showing each participant their own status is attractive, but it adds
personal data, identity and permission trimming, and the cost of a mistake is a participant seeing someone else's
record. Defer it until the general advisor has proved itself, and reclassify the risk tier through
`opportunity-management:risk-classification` before adding it.

Write the behaviour rules plainly. The advisor explains and points; it never decides. It does not say whether
evidence will pass, does not draft evidence for people, and does not comment on any individual. When it does not know,
it says so and gives the escalation route. It always names the guide section it relied on, so people can check.

Build the test set from real questions. Include the common questions with expected answers from the guide, edge cases
such as a participant changing role mid-journey, out-of-scope requests such as "has my colleague passed", and attempts
to get the advisor to decide outcomes. Agree an acceptance threshold with the programme owner. Invite Champions working
on agent capability to help test; it is a safe, real exercise.

Hand the specification to `m365-agents:agent-use-case-design` for the brief and build, typically a declarative agent
built in Agent Builder for general guidance, with Copilot Studio considered only if status lookup or richer
integration is later approved. The build follows the organisation's agent governance like any other agent.

Plan its life. The programme owner owns the advisor's content; whenever the guide, criteria or Challenge options change,
the advisor's knowledge and test set are updated. Review escalated questions monthly: they show where the guide is
unclear and where the advisor's scope should grow or shrink.

## Outputs

- An advisor specification: purpose, audience, question themes, answer, refuse and escalate rules, status option chosen, grounding, owner and review cycle, handed to `m365-agents:agent-use-case-design` for the `agent-brief`.
- A test set of real questions with expected answers, out-of-scope probes and an acceptance threshold agreed with the programme owner.
- A list of guide improvements made before grounding.
- An escalation route and a monthly review of escalated questions.

## Microsoft platform considerations

A general-guidance advisor is usually a good fit for a declarative agent built in Agent Builder, grounded on the guide
in SharePoint, while status lookup or actions would point towards Copilot Studio and bring more governance. Which
option fits, and what each supports, changes over time; check `references/sources.md` and the organisation's approved
tools before choosing. Sharing scope should match the Champion audience, not the whole organisation, unless the
programme decides otherwise.

## Adoption considerations

The advisor is itself an adoption asset: a visible, useful, governed agent that Champions can point to when they explain
what agents are for. Announce it through the community, show how it was tested, and invite feedback.

## Knowledge considerations

The champion guide is the advisor's only authoritative source. It needs an owner, a version, a review date and a rule
that any change to the charter, criteria or Challenge options triggers an update to the guide and a re-run of the test
set. Do not ground the advisor on community conversations, which are unreviewed.

## Security and privacy considerations

A general-guidance advisor holds no personal data and grounds only on content its audience can already read. If status
lookup is added, the tracker becomes personal data exposed through an agent: identity, permission trimming and testing
that each participant sees only their own record are essential, and the change goes to `security-privacy` before
release. Data protection questions end with the organisation's DPO.

## Responsible AI considerations

The advisor must never decide verification, recognition or appeals, and must say plainly that it explains rules rather
than making judgements. It should be transparent that it is an agent, cite the guide section it used, and route anything
it cannot answer to a person.

## Evaluation requirements

Evaluate against the test set before release and after every change to the guide or instructions: correct answers to
common questions, correct refusals for decisions and other people's status, correct escalation, and citation of the
guide. The acceptance threshold is agreed with the programme owner and reviewed by `evaluation-quality` from tier 2.

## Value measures

Owned by the Champions programme owner, with a baseline of questions reaching the owner before release: reduction in
routine questions to the owner and assessors, share of advisor answers rated helpful, escalations by theme, and guide
improvements made. Reported at programme level, never by individual participant.

## Scale notes

### Starter

Usually a well-structured published guide with a question-and-answer section is enough; build an advisor only when
agent building is approved and questions genuinely overwhelm the owner.

### Scale

A general-guidance advisor grounded on the guide, tested against real questions, owned by the programme owner and
reviewed monthly.

### Enterprise

A shared advisor across regional programmes with localised guide sections, status lookup considered only after risk
reclassification and security review, and evaluation run as part of the agent's lifecycle.

## Hand-offs

- To `m365-agents:agent-use-case-design` for the agent brief and build.
- To `m365-agents:agent-testing` to run the evaluation set.
- To `m365-agents:agent-release-readiness` before the advisor is shared.
- To `champions:champion-recruitment` when escalations show the guide needs changing.
- To `opportunity-management:risk-classification` before status lookup is added.

## Reviewer gates

`security-privacy` reviews grounding permissions and sharing scope before release, and any status lookup is blocking
until permission trimming has been tested. From tier 2, `evaluation-quality` reviews the test set and threshold;
findings are classified blocking or advisory. A general-guidance advisor at tier 1 follows the organisation's standard
agent release checks.

## Failure modes

- The advisor is built over an incomplete guide and gives confident wrong answers about requirements.
- It starts telling people whether their evidence will pass, and appeals rise.
- Status lookup is added without proper permission trimming, and a participant sees another person's record.
- The guide changes but the advisor's knowledge and tests do not, so answers drift out of date.
- Nobody owns the advisor, and escalated questions go unanswered.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Let the advisor decide verification, recognition or appeals.
- Let the advisor reveal any information about another participant.
- Ground the advisor on unreviewed community content or an unowned guide.
- Release status lookup without risk reclassification and a security review.
