---
name: human-oversight
description: Decides the level of human oversight an AI solution needs - review of every output, approval before action, sampling or monitoring - and reviews whether the reviewers have the time, information, competence and authority to catch and overturn errors, classifying gaps as blocking or advisory. Use when outputs affect people, money or safety, when an agent will act with less supervision, or when human review exists only on paper.
license: CC-BY-4.0
metadata:
  department: responsible-ai
  lifecycle: Envision, Deliver, Assure, Launch, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 2, 3, 4
  platforms: m365-agents, copilot-cowork, copilot-studio, ai-foundry, power-platform
  edition-support: starter, scale, enterprise
  reviewers: responsible-ai
  sources: ms-responsible-ai, nist-ai-rmf, iso-iec-42001, ico-ai-data-protection
  status: draft
  authors: Simon Foote
---

# Human oversight

## Purpose

"A human stays in the loop" is the most common responsible AI control and the most often hollow. People asked to
approve hundreds of AI outputs a day, with no time, no context and no real authority to disagree, approve them all.
This reviewer skill decides how much human oversight a solution needs, where it sits, and what the people providing it
need to make it real, then reviews the design and classifies gaps as blocking or advisory. It goes wrong when oversight
is counted rather than tested, or when the reviewer becomes the person blamed for the system's errors.

## When to use

- An impact assessment calls for human oversight.
- Outputs inform decisions about people, money, safety, legal position or access to services.
- An agent or automation is about to act with less supervision than before.
- Reviewers approve almost everything, or nobody can say what they check.
- A tier 3 or 4 solution reaches its `responsible-ai` gate.

## When not to use

- Building approval checkpoints inside a delegated Cowork task - use `copilot-cowork:human-checkpoint-design`.
- Building approval and review steps in a Power Automate flow - use `automation:human-in-the-loop`.
- Assessing the overall impacts that determine whether oversight is needed - use `responsible-ai:ai-impact-assessment`.
- Routes for affected people to challenge an outcome after the fact - use `responsible-ai:escalation-and-appeal`.

## Questions to ask first

1. Which outputs or actions could cause harm if wrong, and how quickly and reversibly?
2. At what point can a person still prevent that harm - before the output is used, before the action, or only afterwards?
3. Who will provide oversight, how many items will they see, and how much time will they have for each?
4. What will they see - the output alone, or the sources, confidence signals and the case it relates to?
5. Can they overturn the output without penalty, and is their decision recorded and fed back?

## Required inputs

- The AI impact assessment record and risk tier.
- The solution design showing outputs, actions and where they take effect.
- Expected volumes and the capacity of the reviewing role.
- Evaluation results showing how often and how the solution is wrong.

Where volumes or error rates are unknown, design oversight conservatively and record the assumption for review after
the first weeks of operation. Never assume reviewer capacity that the business owner has not confirmed.

## Decision framework

Choose the oversight mode from the impact and reversibility of an error, then test whether it is effective.

| Mode | Use when | Minimum conditions |
|---|---|---|
| Review every output before use | Errors affect individuals' rights, safety, money or access, or are hard to reverse | Reviewer sees sources and case context; realistic time per item; authority to reject |
| Approve before action | The solution proposes actions in systems or communications | Clear summary of the action and its effect; easy reject and edit; no default approval |
| Sampled review | High volume, low individual impact, reversible errors | Sample size and frequency agreed; findings change the system |
| Monitoring and exception review | Very low impact or fully reversible outcomes | Signals, thresholds and an owner who acts on them |
| Human decision on every case | Tier 4 decisions about individuals, where AI only informs a competent person who decides | All of the above, plus a documented rationale for each decision |

| Gap | Blocking when | Advisory when |
|---|---|---|
| Oversight mode | Mode is weaker than the impact requires | Mode is right but sampling rates are undocumented |
| Capacity | Reviewers cannot realistically review the volume | Capacity is tight but monitored |
| Information | Reviewers see only the output with no sources or context | Context is available but awkward to reach |
| Authority | Reviewers cannot reject, or rejection carries pressure or penalty | Authority exists but is not written down |
| Competence | Reviewers lack the expertise to judge the output | Training planned but not yet complete |
| Feedback | Rejections are not recorded or never change the solution | Feedback recorded but reviewed infrequently |

From risk tier 2 every gap is classified; the gate is mandatory and blocking from tier 3, and from tier 2 when outputs
inform decisions about people.

## Practitioner approach

Start from the harm, not the workflow. For each output or action the impact assessment flagged, ask when a person can
still stop the harm. If an agent sends a message to a customer, oversight after sending is incident response, not
oversight. Place the human at the last point where they can prevent the effect.

Then size the work honestly. Multiply expected volume by the time a careful review takes and compare it with the
reviewers' real capacity. If the numbers do not fit, the design is wrong: reduce volume, narrow scope, move to sampling
for lower-impact items, or accept that the solution is not ready. Oversight that cannot be done properly will not be.

Design what the reviewer sees. A bare output invites approval. Show the sources the output relied on, highlight what is
uncertain or unusual, and present the case it relates to. Make rejecting and editing as easy as approving, and avoid
defaults that pre-select approval. Watch for automation bias: if a solution is usually right, people stop looking.
Periodic seeded errors or calibration sessions help reviewers stay alert, provided they are used to improve the
process and never to assess individuals.

Confirm authority and competence. The reviewer must be allowed to disagree without having to justify it to the system
or a manager, and must know enough about the subject to spot a plausible error. Write the authority into the role
description or procedure, not just the design.

Close the loop. Record rejections and edits at aggregate level, review them with the solution owner and feed them into
evaluation and improvement. A rejection rate near zero is a signal to investigate, not a success measure.

Record the design on the `human-oversight-plan` template and test it before release with real reviewers and realistic
volumes. Re-review when volume, scope or autonomy changes.

## Outputs

- A human oversight plan on the `human-oversight-plan` template: oversight mode per output or action, reviewer role, capacity calculation, information shown, authority, competence, feedback route and review trigger.
- Gaps classified blocking or advisory with fix and owner, recorded with the `ai-impact-assessment-record`.
- Design requirements handed to the build team.

## Microsoft platform considerations

Approval steps in Power Automate, confirmation before actions in Copilot Studio, checkpoints in Copilot Cowork and
human review patterns in Foundry solutions are implemented differently and change over time. The oversight design is
platform-neutral; confirm the mechanism available on the chosen route in the platform's source records before
committing to it.

## Adoption considerations

Reviewers are users too. Involve them in designing what they see, train them on the solution's known weaknesses, and
explain that their role is to judge, not to rubber-stamp. Measure oversight at role level, never by individual reviewer.

## Knowledge considerations

Reviewers judge better when they can see the sources behind an output. Where sources are poor, oversight carries more
of the load; record the dependency with the knowledge owner.

## Security and privacy considerations

Reviewers may see personal or confidential data they would not otherwise see. Check the reviewing role's access with
`security-privacy:data-exposure-review`, and keep review records within agreed retention.

## Responsible AI considerations

This skill is the responsible AI review of human oversight. Meaningful human involvement can also matter for data
protection when decisions about individuals are made with AI support; route that question to the DPO through
`security-privacy:privacy-assessment`.

## Evaluation requirements

Test oversight before release: present reviewers with outputs that include known errors and check that they catch
them in realistic conditions. Results are reported at role level and used to improve the design, never to judge people.

## Value measures

Track override and edit rates, errors caught before effect versus found afterwards, and reviewer time per item against
the plan, at role level. The business owner owns these measures, with baselines from the pre-release test.

## Scale notes

### Starter

Keep early solutions in the "review every output" or "approve before action" modes, with volumes small enough that
review is real.

### Scale

Use a standard oversight plan per pattern, track override rates across solutions and move to sampling only when
evidence supports it.

### Enterprise

Set organisation-wide minimum oversight modes per risk tier, audit oversight effectiveness on tier 3 and 4 solutions,
and share calibration practice across business units.

## Hand-offs

- To `copilot-cowork:human-checkpoint-design` and `automation:human-in-the-loop` to build the designed checkpoints.
- To `evaluation-quality:ai-evaluation-strategy` for the evidence oversight relies on.
- To `responsible-ai:escalation-and-appeal` for what happens after a decision.
- To `responsible-ai:ai-risk-acceptance` where a disputed gap remains.

## Reviewer gates

This skill is part of the `responsible-ai` gate. It is mandatory and blocking from risk tier 3, and from tier 2 when
outputs inform decisions about people; otherwise advisory at tier 2. Disagreement escalates to the accountable
executive for written risk acceptance.

## Failure modes

- Reviewers approve hundreds of outputs a day and catch nothing, so oversight exists only on paper.
- The reviewer sees the output but not its sources, so plausible errors pass.
- Oversight is placed after the effect, so it becomes complaint handling.
- Override data is used to judge individual reviewers, and people stop disagreeing with the system.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Accept human oversight without checking capacity, information, competence and authority.
- Use oversight or override data to assess or rank individual reviewers.
- Place the only human check after the harm has already happened.
- Trade a blocking gap against a launch date.
