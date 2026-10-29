---
name: ai-assisted-prototyping
description: Sets the boundaries for prototyping with Copilot Code - a question, a time box, a sandbox, safe data, no production connections and an end decision to discard, rebuild or promote - so quick prototypes never become unowned software. Use when a team wants to try an idea in code with AI, when a prototype has started being used for real, or when sponsors ask how to encourage experiments safely.
license: CC-BY-4.0
metadata:
  department: copilot-code
  lifecycle: Discover, Envision, Deliver
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2
  platforms: copilot-code, github, azure, power-platform
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: nist-ai-rmf, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# AI-assisted prototyping

## Purpose

AI coding agents make prototypes cheap and fast, which is genuinely valuable: a working sketch in an afternoon can settle
an argument that would otherwise take weeks of meetings. The risk is not the prototype but what happens next. People start
using it, it acquires real data and real users, and the organisation finds itself running software that nobody reviewed,
owns or can support. This skill sets the boundaries that let teams prototype freely: a question to answer, a time box, a
safe place to build, safe data, and a decision at the end. It goes wrong when the end decision never happens.

## When to use

- A team wants to explore an idea, interface or integration in code with AI help.
- A prototype has quietly started being used for real work.
- A sponsor wants to encourage experimentation with Copilot Code without creating unmanaged software.
- A hackathon, innovation day or proof of concept is being planned.

## When not to use

- Deciding whether the outcome needs software at all - use `copilot-code:code-use-case-assessment`.
- Promoting a prototype into a production build - start with `copilot-code:code-solution-brief`.
- Choosing and designing pilots that test a value hypothesis with real users - use `opportunity-management:pilot-selection`.
- Designing safe hands-on learning labs and sandboxes - use `learning-and-skills:practice-labs`.

## Questions to ask first

1. What question is the prototype meant to answer, and what result would change a decision?
2. How long will it run, and who will make the decision at the end?
3. Where will it be built and run, and is that place isolated from production systems and data?
4. What data will it use, and is it synthetic, public or approved for this purpose?
5. Who will see or use it, and how will they know it is a prototype?

## Required inputs

- A short statement of the idea and the question to answer.
- The organisation's sandbox or prototyping environment and its rules, if one exists.
- The organisation's data handling rules for test and synthetic data.
- A named sponsor who will make the end decision.

If no sandbox exists, prototypes stay on approved developer environments with synthetic data only, and the gap is routed
to the platform team. Never connect a prototype to production systems or real personal data without moving it into the
production route first.

## Decision framework

Every prototype has a charter with five boundaries, and ends in one of three decisions.

| Boundary | Rule |
|---|---|
| Question | One question the prototype answers, written before building |
| Time box | A fixed end date, usually days or a few weeks, not open-ended |
| Place | An approved sandbox or developer environment, isolated from production |
| Data | Synthetic, public or explicitly approved test data only; no real personal data |
| Audience | The team and named testers, told it is a prototype; no reliance in daily work |

| End decision | When | What happens |
|---|---|---|
| Discard | The question is answered, or the idea did not work | Archive the learning, delete the deployment and data |
| Rebuild properly | The idea works and should become real software | Start the production route from a solution brief; treat prototype code as a reference, not a foundation, unless it passes review |
| Promote | The code is sound and the production route can adopt it | Full brief, review, security review, validation and deployment readiness, as for any build |

A prototype past its time box without a decision is escalated to the sponsor and switched off until one is made.

## Practitioner approach

Write the question first. "Can site managers complete an inspection on a tablet in under five minutes?" is a prototype
question; "build an inspection app" is not. The question keeps the prototype small and tells everyone when it is finished.
It also makes the end decision easier, because the prototype is judged on whether it answered the question rather than on
how much it looks like a product.

Set the time box and the decision maker together. A few days to a few weeks is typical. Name the sponsor who will decide
at the end and put the date in their calendar. Prototypes rarely fail by being stopped too early; they fail by never being
stopped.

Build in a safe place. Use the organisation's sandbox or an approved developer environment, isolated from production
systems. Do not connect to live systems of record, even read-only, because a prototype with a live connection is one step
from being relied on. Use synthetic data or approved test data; AI coding agents can help generate realistic synthetic
data, which removes the temptation to copy a production extract.

Tell users it is a prototype. Label it on screen, in its name and in every message about it. Limit testers to named people
who understand it may disappear. This protects the organisation and also improves feedback: people tell you what is wrong
with a prototype more readily than with something presented as finished.

Capture the learning as you go. Note what worked, what did not, what the users said and what you would do differently.
This record is the main output of most prototypes, more valuable than the code.

Make the end decision deliberately. If the idea failed, discard it and share what was learned. If it worked, decide
between rebuilding properly and promoting. Prototype code written quickly with an AI agent often lacks tests, error
handling, security and structure; rebuilding from a proper brief with the prototype as a reference is frequently faster
than retrofitting all of that. Promote only when the code passes `copilot-code:generated-code-review` and the production
route accepts it.

Keep a register of live prototypes with their questions, owners and end dates. Review it monthly and switch off anything
past its date without a decision.

## Outputs

- A prototype charter: question, time box, place, data, audience, sponsor and end date.
- A learning record capturing what the prototype showed.
- An end decision (discard, rebuild properly or promote), recorded with reasons.
- An entry in the prototype register.

## Microsoft platform considerations

Sandboxes may be Azure subscriptions or resource groups, Power Platform developer environments or isolated repositories,
depending on the organisation's platform choices. Use the organisation's approved sandbox pattern and check current
platform capabilities and limits in the relevant source records. Keep prototype repositories under organisational
control, even when they are short-lived.

## Adoption considerations

Make prototyping easy and visible within the boundaries, so people do not build out of sight. Celebrate discarded
prototypes that answered their question as much as successful ones; a culture that only rewards "launches" pushes
prototypes into production.

## Knowledge considerations

The learning record is the knowledge asset. Store it where the next team with a similar idea can find it, linked to the
opportunity backlog.

## Security and privacy considerations

Sandboxes are isolated, data is synthetic or approved, and no prototype connects to production. Secrets used in prototypes
are short-lived sandbox credentials, never production ones. From risk tier 2 or where any real data is involved, the
`security-privacy` reviewer confirms the sandbox and data arrangements.

## Responsible AI considerations

Prototypes that explore decisions about people use synthetic data only and must not be tried on real cases. Be clear with
testers about what the prototype does and that its results are not to be acted on.

## Evaluation requirements

Evaluation is the answer to the prototype's question, judged against the result that would change the decision. Record it
in the learning record; formal validation belongs to the production route.

## Value measures

Track at programme level the number of prototypes that reached a decision on time, the share discarded with recorded
learning, and the share rebuilt or promoted. A prototype that answers its question cheaply is a success whatever the answer.

## Scale notes

### Starter

A one-paragraph charter, a developer environment with synthetic data, and a sponsor who decides at the end. Keep a simple
list of live prototypes.

### Scale

Provide a standard sandbox, a charter template and a register reviewed monthly by the CoE or engineering lead.

### Enterprise

Offer self-service sandboxes with automatic expiry, synthetic data tooling and a central register; prototypes that are
promoted enter the engineering portfolio through the standard route.

## Hand-offs

- To `copilot-code:code-solution-brief` when the end decision is rebuild or promote.
- To `copilot-code:generated-code-review` before any promotion.
- To `opportunity-management:pilot-selection` when the next step is a pilot with real users.

## Reviewer gates

From risk tier 2, or when any real data is proposed, `security-privacy` confirms the sandbox isolation and data
arrangements. Findings are blocking or advisory; a prototype connected to production systems or holding real personal data
without approval is blocking.

## Failure modes

- The prototype is never stopped, acquires real users and data, and becomes unowned production software.
- A production data extract is copied into the prototype because synthetic data seemed like extra work.
- Prototype code is promoted as-is, without tests, error handling or security review.
- No learning is recorded, so the next team repeats the same experiment.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Connect a prototype to production systems or real personal data without moving it into the production route.
- Let a prototype run past its time box without a decision.
- Promote prototype code without code review and security review.
- Present a prototype to users as finished software.
