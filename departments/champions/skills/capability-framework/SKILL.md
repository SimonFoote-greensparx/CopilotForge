---
name: capability-framework
description: Defines the three Champion capabilities - Chat, productivity and agents - each with an objective, a training option, an evidence option, verification criteria and an outcome, so training is one route rather than the gate, and maps learning sessions open to the wider business onto the journey. Use when setting what a Champion must show, when status needs to mean something, or when experienced colleagues want to skip training.
license: CC-BY-4.0
metadata:
  department: champions
  lifecycle: Enable, Measure
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, copilot-cowork, m365-agents
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-champion-best-practice, ms-copilot-overview, ms-copilot-adoption-hub, ms-agent-builder
  status: draft
  authors: Simon Foote
---

# Capability framework

## Purpose

This skill defines what a Champion can demonstrably do in each capability area and how they show it. Each of three
capabilities - Chat, productivity and agents - is defined by five elements: an objective, a training option, an
evidence option, verification criteria and an outcome. Training is one route, not the gate, so experienced colleagues
can be recognised without sitting through learning they do not need. Frameworks usually go wrong by describing
knowledge ("understands prompting") instead of observable practice, by tying status to course completion, or by tying
it to product features that change every few months.

## When to use

- A Champions programme is being set up and needs a definition of capability.
- Champion status has lost credibility because it reflects attendance rather than ability.
- Experienced colleagues want a way to be recognised without sitting through beginner training.
- The organisation runs recurring Copilot learning sessions and wants them to count towards the journey without becoming the gate.
- Product changes have made an existing framework's feature-based levels obsolete.

## When not to use

- Designing the overall programme, journey and boundaries - use `champions:champion-programme-design`.
- Assessing submitted evidence, keeping the tracker, assessor training and appeals - use `champions:evidence-assessment`.
- Designing the Champion Challenge that follows the three capabilities - use `champions:champion-challenges`.
- Recognition and progression once capabilities are verified - use `champions:recognition-and-progression`.
- Building role-based curricula for the whole workforce - use `learning-and-skills:ai-role-curriculum`.

## Questions to ask first

1. Which Copilot experiences and agent tools has the organisation approved for Champions to use?
2. What should a Champion be able to show a colleague in each capability, in the organisation's own work?
3. Does the organisation want Champions to configure agents at all, and under what governance?
4. Which recurring learning sessions already exist, and are they open to everyone?
5. Who will assess evidence, and how much assessor time is available?

## Required inputs

- The Champions programme charter and journey from `champions:champion-programme-design`.
- The approved tools list and agent governance position from the CoE.
- The scenario catalogue from `copilot-adoption:scenario-discovery`, to anchor evidence in real work.
- The current learning calendar and material from the foundation adoption programme.

If agent building is not approved for Champions, define the agent capability as explaining agents, judging use cases
and evaluating approved agents, and record the position. Never define a capability around a tool the organisation has
not approved. If no learning sessions exist yet, mark the training option "to confirm" rather than invent a curriculum.

## Decision framework

Define each capability with the same five elements. Both routes lead to the same verification criteria.

| Element | Chat capability | Productivity capability | Agent capability |
|---|---|---|---|
| Objective | Use Copilot Chat effectively and safely for real tasks - clear prompts, iterative refinement, relevant context, verified output | Use Copilot across the Microsoft 365 apps to produce useful, validated outputs from recurring work, and help a colleague do the same | Explain what agents are, judge good and poor use cases, and, where approved, configure a basic agent and test its behaviour |
| Training option | A Chat session plus a guided exercise on the person's own non-sensitive work | Sessions on Copilot in the apps plus an exercise on a recurring task | An agent design session plus a guided configuration or evaluation exercise |
| Evidence option | Two or three real examples showing prompt, refinement, output, the check applied and what changed | A before-and-after account of a recurring task, a reusable prompt pattern and evidence a colleague used it | A note on one good and one poor agent candidate, plus a governed basic build with owner and test questions, or evaluation notes on an approved agent |
| Verification criteria | Every rubric dimension at least Meets; refinement and choice of context visible | Every dimension at least Meets; output validated against its source; transfer to a colleague shown | Every dimension at least Meets; use-case reasoning sound; tests with expected and observed behaviour; intake record for any build |
| Outcome | Chat verified; can support colleagues with everyday Chat use | Productivity verified; pattern offered to the scenario catalogue | Agent verified; eligible for the Champion Challenge once all three are verified |

Rubric dimensions apply to every capability, each rated Not yet, Meets or Strong:

| Dimension | Meets looks like |
|---|---|
| Real work | The example comes from the person's actual role, not a demo |
| Safe use | No sensitive data shared inappropriately; approved tools only |
| Verification | The person checked the output and can explain how |
| Transferability | Someone else could reuse the pattern |
| Reflection | The person can say what did not work and why |

Map recurring learning sessions to the journey. Sessions stay open to everyone; the guided exercise is what counts.

| Session type | Counts towards |
|---|---|
| Getting started and approved use | Joining the community |
| Copilot Chat | Chat capability, training option |
| Copilot in the Microsoft 365 apps, including meetings and collaboration in Teams | Productivity capability, training option |
| Agent design and evaluation | Agent capability, training option |

## Practitioner approach

Start from what the organisation needs Champions to do, not from the product. A Champion's value is that they can show
a colleague how to do something useful and safe in that colleague's own work. Write each objective as a sentence that
begins "A Champion with this capability can..." and test it with a few likely Champions and their managers.

Keep the capability areas few. Three areas, verified in order, give a clear path and a manageable assessment load. Tie
each to durable practice rather than features: "verifies output against a known source" lasts, "uses feature X in app
Y" is out of date within months. Where an example needs a product name, put it in guidance notes that can be refreshed.

Complete all five elements for every capability before launch. The objective says what good looks like; the training
and evidence options say how someone gets there; the verification criteria say how an assessor decides; the outcome
says what changes for the participant and what the next milestone is. If any element is vague, participants will ask
the programme owner, and self-service guidance will have nothing reliable to explain.

Design two routes that meet the same standard. The training route combines a session with a guided exercise on the
person's own work; the exercise output is the evidence, so attendance alone never verifies anything. The evidence route
lets experienced colleagues submit directly. Neither is a lesser badge, which keeps the programme fair to novices and
respectful of experts.

Treat learning sessions as an ecosystem shared with the foundation adoption programme. Run them on a recurring rhythm,
keep them open to the wider business, record them, and mark which ones count towards which capability. This avoids
duplicating foundation training and stops the programme looking like a closed club.

Define evidence a busy person can produce from real work, and require redaction of anything sensitive; evidence that
cannot be shared safely is not suitable evidence. For productivity, ask for proof of transfer, because that is the
difference between a good user and a Champion.

Treat the agent capability carefully. Configuring agents carries ownership, knowledge and governance obligations.
Where Champions may build, evidence includes an owner, test questions with expected answers and an intake record.
Where they may not, the capability focuses on judging use cases and evaluating approved agents, and on routing needs
to `opportunity-management:problem-framing`.

Write the rubric in plain language with fictional examples of each rating, pilot it on a few submissions, and adjust
where assessors disagree. Version the framework, because it is the main knowledge source for any advisor agent, and
review it at least twice a year.

## Outputs

- A Champion capability framework on the `champion-capability-framework` template: a capability card per capability with objective, training option, evidence option, verification criteria and outcome.
- An evidence rubric in the rubric section of the same template, with plain-language examples for each rating.
- A learning session map showing which recurring sessions count towards which capability.
- A submission guide explaining what to submit, how to redact and how it will be assessed.

## Microsoft platform considerations

Capabilities map loosely onto Copilot Chat, Copilot in the Microsoft 365 apps, Copilot Cowork and agents built with
approved tools such as Agent Builder or Copilot Studio, but the definitions should not depend on any one product.
Availability and naming change; refresh guidance notes from `references/sources.md` and the approved tools list
rather than editing the objectives.

## Adoption considerations

The framework gives Champions and their managers a shared language for capability. Publish it openly so anyone can see
what good looks like, and let the same learning sessions serve both the wider workforce and the Champion journey.

## Knowledge considerations

The framework is the primary knowledge source for self-service guidance and any advisor agent. Version it and tell the
guidance owner whenever it changes. Where submissions reveal stale or unowned team content, pass it to
`knowledge-management:knowledge-lifecycle`.

## Security and privacy considerations

Submission guidance must require redaction of personal, confidential and client data, and evidence must be stored with
access limited to assessors and the programme owner, with a retention period. Guided exercises use non-sensitive
material. Agent capability builds follow the organisation's agent governance.

## Responsible AI considerations

Verification and safe use are rubric dimensions in every capability, so responsible behaviour is part of capability
rather than an add-on. The framework assesses evidence of practice, never personal traits or general performance.

## Evaluation requirements

For the agent capability, evidence includes test questions with expected answers and a note of how the agent behaved.
The rubric itself is evaluated by piloting it on sample submissions and measuring assessor agreement.

## Value measures

Programme-level measures, owned by the programme owner: participants verified in each capability, share using each
route, milestone conversion from one capability to the next and time from joining to each verification. Reported in
aggregate above the minimum group size, never as individual rankings.

## Scale notes

### Starter

Chat and productivity may be enough at first, with the programme owner assessing and an existing session or two
serving as the training option. Keep the capability cards and rubric to two pages.

### Scale

All three capabilities, both routes, a recurring session calendar open to the wider business and a small trained
assessor group. Publish worked fictional examples.

### Enterprise

A governed framework with version control, localised examples, calibrated assessors across regions, and alignment with
the organisation's wider skills framework and `learning-and-skills:ai-learning-pathway`.

## Hand-offs

- To `champions:evidence-assessment` to assess submissions and keep the tracker.
- To `champions:champion-challenges` once all three capabilities are verified.
- To `champions:recognition-and-progression` to connect verified capabilities to recognition.
- To `learning-and-skills:ai-role-curriculum` for session content and curricula at scale.

## Reviewer gates

Not applicable as a formal gate, because the framework defines people capability rather than releasing a solution;
agent builds made as evidence pass through CoE intake, where risk tiers and reviewer gates apply.

## Failure modes

- Capabilities describe product features, and the framework is out of date by the next release.
- The training route becomes the only route, and experienced colleagues disengage.
- Sessions are closed to the wider business, so the programme duplicates foundation training and looks exclusive.
- Evidence requires sharing real sensitive material, so people either cannot submit or submit unsafely.
- The framework changes but self-service guidance does not, so participants are told outdated requirements.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Verify a capability on attendance or course completion alone.
- Treat the training route as superior to the evidence route, or the reverse.
- Require evidence that cannot be shared without exposing sensitive data.
- Use the framework to rank Champions or assess their general job performance.
- Define a capability around a tool the organisation has not approved.
