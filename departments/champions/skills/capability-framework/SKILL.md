---
name: capability-framework
description: Defines the Champion capability levels - verified Chat capability, productivity capability and agent capability - each with observable evidence and an evidence rubric, and offers two routes to each level, structured learning or direct evidence submission. Use when setting what a Champion must be able to do, when Champion status needs to mean something, or when experienced colleagues want to skip training.
license: CC-BY-4.0
metadata:
  department: champions
  lifecycle: Enable, Measure
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, copilot-cowork, m365-agents
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-champion-best-practice, ms-copilot-overview, ms-copilot-adoption-hub
  status: draft
  authors: Simon Foote
---

# Capability framework

## Purpose

This skill defines what a Champion can demonstrably do at each level, and how they show it. It sets three capability
levels - Chat, productivity and agent - each described as observable behaviour with a rubric, and two fair routes to
each level. Frameworks usually go wrong by describing knowledge ("understands prompting") instead of observable
practice, by tying levels to course completion, or by tying them to specific product features that change every few
months.

## When to use

- A Champions programme is being set up and needs a definition of capability.
- Champion status has lost credibility because it reflects attendance rather than ability.
- Experienced colleagues want a way to be recognised without sitting through beginner training.
- Product changes have made an existing framework's feature-based levels obsolete.

## When not to use

- Designing the overall programme, charter and boundaries - use `champions:champion-programme-design`.
- Running assessment of submitted evidence, assessor training and appeals - use `champions:evidence-assessment`.
- Designing the practical challenges that follow verified capability - use `champions:champion-challenges`.
- Recognition and progression once levels are verified - use `champions:recognition-and-progression`.
- Building role-based curricula for the wider workforce - the `learning-and-skills` department (planned).

## Questions to ask first

1. Which Copilot experiences and agent tools has the organisation approved for Champions to use?
2. What should a Champion be able to show a colleague at each level, in the organisation's own work?
3. Does the organisation want Champions to build agents at all, and under what governance?
4. What structured learning already exists that could form the learning route?
5. Who will assess evidence, and how much assessor time is available?

## Required inputs

- The Champions programme charter from `champions:champion-programme-design`.
- The approved tools list and agent governance position from the CoE.
- The scenario catalogue from `copilot-adoption:scenario-discovery`, to anchor evidence in real work.
- Existing learning material that could support the learning route.

If agent building is not approved for Champions, define the agent level as using and evaluating approved agents
rather than building them, and record the position. Never define a level around a tool the organisation has not
approved.

## Decision framework

Each level is defined by observable evidence, not by courses completed. Both routes lead to the same evidence standard.

| Level | A Champion at this level can | Observable evidence |
|---|---|---|
| 1. Verified Chat capability | Use Copilot Chat safely for real tasks, choose what not to share, and verify output | Two or three real, non-sensitive examples with prompt, output, the check applied and what changed as a result |
| 2. Verified productivity capability | Use Copilot in daily apps to improve a recurring piece of work, and teach it to a colleague | A before-and-after account of a recurring task, a reusable prompt pattern, and evidence a colleague used it |
| 3. Verified agent capability | Use approved agents well, recognise when a need justifies an agent, and, where approved, build a simple governed one | Evaluation notes on an approved agent or a governed build with an owner, test questions and a routed intake record |

Rubric dimensions apply at every level, each rated Not yet, Meets or Strong:

| Dimension | Meets looks like |
|---|---|
| Real work | The example comes from the person's actual role, not a demo |
| Safe use | No sensitive data shared inappropriately; approved tools only |
| Verification | The person checked the output and can explain how |
| Transferability | Someone else could reuse the pattern |
| Reflection | The person can say what did not work and why |

A level is verified when every dimension is at least Meets. Strong is noted for feedback, not ranking.

## Practitioner approach

Start from what the organisation needs Champions to do, not from the product. A Champion's value is that they can show
a colleague how to do something useful and safe in that colleague's own work. Write each level as a sentence that
begins "A Champion at this level can..." and test it with a few likely Champions and their managers: would they
recognise that behaviour and value it?

Keep levels tied to durable capabilities rather than features. "Verifies output against a known source" lasts;
"uses feature X in app Y" is out of date within months. Where an example needs a product name, put it in guidance
notes that can be refreshed, not in the level definition.

Define evidence that a busy person can produce from their real work. Two or three examples per level, each with the
prompt or approach, the output, the check applied and the result, are usually enough. Ask for redaction of anything
sensitive; evidence that cannot be shared safely is not suitable evidence. For the productivity level, ask for proof of
transfer: that a colleague used the pattern. That is the difference between a good user and a Champion.

Treat the agent level carefully. Building agents carries ownership, knowledge and governance obligations. Where the
organisation allows Champions to build, the evidence must include an owner, test questions with expected answers and
an intake record through the CoE. Where it does not, the level focuses on using approved agents critically and
recognising when a need should go to `opportunity-management:problem-framing`.

Design two routes to every level. The learning route offers structured sessions, practice exercises and a guided first
submission, for people building capability. The evidence route lets experienced colleagues submit evidence directly.
Both meet the same rubric, so neither is a lesser badge. This keeps the programme fair to novices and respectful of
experts.

Write the rubric in plain language with examples of Not yet, Meets and Strong for each dimension, using fictional
cases. Assessors will rely on these examples more than on the definitions. Pilot the rubric with a few submissions
before launch, and adjust where assessors disagree.

Finally, set a review date. Revisit the framework at least twice a year, because capability expectations shift as the
organisation matures and tools change.

## Outputs

- A Champion capability framework on the `champion-capability-framework` template: levels, observable evidence, both routes and guidance notes.
- An evidence rubric in the rubric section of the same template, with plain-language examples for each rating.
- A submission guide for Champions explaining what to submit, how to redact and how it will be assessed.

## Microsoft platform considerations

Levels map loosely onto Copilot Chat, Copilot in the Microsoft 365 apps, Copilot Cowork and agents built with approved
tools, but the definitions should not depend on any one product. Availability and naming change; refresh guidance notes
from `references/sources.md` and the approved tools list rather than editing level definitions.

## Adoption considerations

The framework gives Champions and their managers a shared language for capability. Publish it openly so anyone can see
what good looks like, not only Champions.

## Knowledge considerations

Evidence at the productivity and agent levels often depends on good team knowledge. Where submissions reveal that
content is stale or unowned, note it and pass it to the `knowledge-management` department (planned).

## Security and privacy considerations

Submission guidance must require redaction of personal, confidential and client data, and evidence must be stored with
access limited to assessors and the programme owner, with a retention period. Agent-level builds must follow the
organisation's agent governance.

## Responsible AI considerations

Verification and safe use are rubric dimensions at every level, so responsible behaviour is part of capability rather
than an add-on. The framework assesses evidence of practice, never personal traits or general performance.

## Evaluation requirements

At the agent level, evidence includes test questions with expected answers and a note of how the agent was checked.
The rubric itself is evaluated by piloting it on sample submissions and measuring assessor agreement.

## Value measures

Programme-level measures, owned by the programme owner: number of Champions verified at each level, share using each
route, and time from joining to first verification. Reported in aggregate, never as individual rankings.

## Scale notes

### Starter

Two levels may be enough, Chat and productivity, with the programme owner assessing evidence. Keep the rubric to one
page.

### Scale

All three levels, both routes, and a small trained assessor group. Publish worked fictional examples.

### Enterprise

A governed framework with version control, localised examples, calibrated assessors across regions, and alignment with
the organisation's wider skills framework.

## Hand-offs

- To `champions:evidence-assessment` to assess submissions against the rubric.
- To `champions:champion-challenges` once a Champion has verified capability and is ready for a challenge.
- To `champions:recognition-and-progression` to connect verified levels to recognition.
- To the `learning-and-skills` department (planned) for structured learning content at scale.

## Reviewer gates

Not applicable as a formal gate, because the framework defines people capability rather than releasing a solution;
agent-level builds pass through CoE intake, where risk tiers and reviewer gates apply.

## Failure modes

- Levels describe product features, and the framework is out of date by the next release.
- The learning route becomes the only route, and experienced colleagues disengage.
- Evidence requires sharing real sensitive material, so people either cannot submit or submit unsafely.
- The agent level encourages ungoverned building with no owner or intake record.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Define a level by attendance or course completion alone.
- Require evidence that cannot be shared without exposing sensitive data.
- Use the framework to rank Champions or assess their general job performance.
- Define a level around a tool the organisation has not approved.
