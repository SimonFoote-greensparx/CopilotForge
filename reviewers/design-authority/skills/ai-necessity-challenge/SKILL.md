---
name: ai-necessity-challenge
description: Challenges, as a reviewer, whether a designed solution needs AI at all or needs as much AI as proposed, testing it against process change, automation and simpler Copilot patterns, and classifies each finding as blocking or advisory with the simpler alternative named. Use when a design arrives at the gate with an agent or custom model, when the suitability record looks written after the fact, or when AI adds cost or risk without clear benefit.
license: CC-BY-4.0
metadata:
  department: design-authority
  lifecycle: Envision, Deliver, Assure
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-cowork, copilot-studio, ai-foundry, power-platform
  edition-support: starter, scale, enterprise
  reviewers: design-authority
  sources: ms-agents-extensibility, ms-agents-compare, ms-copilot-studio-zoned-governance, ms-responsible-ai, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# AI necessity challenge

## Purpose

Enthusiasm for AI produces designs where a model does work that a form, a rule or a flow would do more reliably and more
cheaply. This reviewer skill challenges the use of AI in a solution at the design gate: whether AI is needed at all,
whether each AI component earns its place, and whether a simpler pattern would meet the need. Each finding is blocking
or advisory and names the simpler alternative. The challenge goes wrong when it becomes opposition to AI in general,
when it repeats intake suitability without new evidence, or when it is skipped because the sponsor is keen.

## When to use

- A design arrives at the gate with an agent, custom model or Foundry solution.
- The suitability decision appears to have been written to justify a tool already chosen.
- An AI component makes decisions that a rule could make deterministically.
- Run cost, evaluation effort or risk seems out of proportion to the problem.
- A sponsor or reviewer asks why AI is used here.

## When not to use

- Making the original suitability decision at intake - use `opportunity-management:ai-suitability`.
- Deciding whether a pilot should scale or stop - use `opportunity-management:scale-or-stop`.
- Reviewing whether the chosen platform fits - use `design-authority:platform-fit-review`.
- Assessing automation candidates and whether AI is needed in a flow - use `automation:automation-assessment`.
- Identifying uses that should not be built on ethical grounds - use `responsible-ai:prohibited-use-review`.

## Questions to ask first

1. What problem does the solution solve, and what would happen if the AI component were removed?
2. Which parts of the work need judgement over language, documents or conversation, and which are fixed rules on structured data?
3. Was process change or training considered, and what was the result?
4. What does the AI component add in run cost, evaluation and oversight, compared with the alternative?
5. Is there evidence, from a pilot or test, that AI performs better than the simpler option?

## Required inputs

- The suitability decision record and framed problem from opportunity management.
- The solution design, showing each AI component and what it does.
- The value hypothesis and non-functional requirements, including cost per use.
- Any pilot or test evidence comparing AI with alternatives.

If no suitability decision exists, that is a finding in itself: blocking from tier 2, because the design has no recorded
reason for using AI. Do not reconstruct the decision on the team's behalf.

## Decision framework

Examine each AI component separately, then the solution as a whole.

| Test | Blocking when (tier 2 and above) | Advisory when |
|---|---|---|
| Deterministic work | A model makes a decision a stated rule could make, where errors have consequences | A model is used for convenience on low-impact work |
| Simpler rung | Copilot Chat, a shared prompt or automation clearly meets the need and the design adds material risk or cost | A simpler rung might work and was not tested |
| Process first | The problem is evidently a broken process or ownership gap the AI would automate | Process improvement would increase value alongside AI |
| Cost and effort | Run cost, evaluation or oversight cannot be justified by the value hypothesis | Cost is high but justified, with no review point set |
| Evidence | Claims of AI superiority are untested at tier 3 and above | Evidence is anecdotal at tier 2 |
| Suitability record | Missing, or contradicted by the design | Present but thin |

Below tier 2, findings are advisory to the owner and the CoE. Disagreement with a blocking finding escalates to the
accountable executive for written risk acceptance.

## Practitioner approach

Read the suitability record and the design side by side. Look for drift: a record that chose a declarative agent while
the design now includes a custom model, or a record that rejected automation for reasons that no longer hold. Drift is
normal; unexamined drift is the finding.

Take the design apart into components and ask what each AI component decides or produces. For each, write the rule a
person would follow if there were no AI. If the rule is short and complete ("route to finance when the invoice value is
above the threshold"), a model should not be making that decision. If the rule cannot be written because the work is
interpretation of language, AI may well be appropriate.

Test the simpler rungs honestly. Could the people involved use Copilot Chat with a shared prompt pattern? Could a flow
with one AI step do the job, with the model only extracting fields and the flow doing the deciding? Could a form
redesign remove the need entirely? Name the alternative specifically, so the team can evaluate it rather than argue
about principle.

Weigh cost and effort. AI components carry ongoing evaluation, monitoring, knowledge upkeep and consumption cost. Compare
these with the value hypothesis. A solution whose value only appears at a scale it will never reach is a finding.

Look for evidence. At tier 3 and above, ask for a comparison between the AI approach and the simpler option on real
cases. At tier 2, accept reasoned judgement but set a review point after release.

Be fair. The challenge is not opposition to AI. Where the design is reasoned and the AI component is the simplest thing
that works, say so plainly; a pass is a valid and useful outcome. Where the finding is "use less AI", help the team find
the smaller design rather than simply blocking.

Record each finding with the component, the test, the risk, the simpler alternative and the owner, and pass it to the
consolidated design review.

## Outputs

- A necessity section in the `design-review-record`: each AI component, tests applied, findings classified as blocking or advisory with the simpler alternative, fix and owner.
- A note to opportunity management where the suitability record needs updating.
- Where AI is removed or reduced, a referral to the route that will deliver the simpler option.

## Microsoft platform considerations

Simpler alternatives often exist inside the platforms the organisation already uses: Copilot in the Microsoft 365 apps,
shared prompts, agents built in Agent Builder, or flows with a single AI step. Check `ms-agents-extensibility` and
`ms-agents-compare` for current options before naming an alternative, and avoid stating availability from memory.

## Adoption considerations

Teams who hear "you do not need AI" can feel their work has been wasted. Frame findings as a faster, cheaper route to the
same outcome, and route individual-use alternatives to `copilot-adoption:scenario-discovery` so the need is still met.

## Knowledge considerations

Many proposed agents are really knowledge problems: content that is hard to find or out of date. Where fixing the
content would meet the need, say so and route it to `knowledge-management`.

## Security and privacy considerations

Unnecessary AI components widen the attack surface and the data processed. Removing them is often the most effective
security improvement; note this for the `security-privacy` reviewers.

## Responsible AI considerations

Using AI where a transparent rule would do can make decisions about people harder to explain and appeal. Treat such
uses as blocking from tier 3 and refer them to the `responsible-ai` reviewers.

## Evaluation requirements

Where the team claims AI outperforms the simpler option, ask for a comparison on the same real cases with an agreed
measure, using `evaluation-quality` methods. Without it, the claim is recorded as unproven.

## Value measures

At portfolio level, track AI components removed or simplified at the gate, estimated run cost avoided, and solutions
whose value hypothesis held after release. The design authority chair owns these measures, with a baseline from the
first quarter of reviews.

## Scale notes

### Starter

The CoE lead asks the necessity questions informally at design, recorded on the review record. Most starter solutions
should be simple; challenge anything that is not.

### Scale

Apply the challenge to every tier 2 design and to any Foundry or custom model proposal, and feed patterns back to intake.

### Enterprise

Federate the challenge to business-unit design authorities with shared tests, and analyse findings across the estate to
improve intake guidance.

## Hand-offs

- Back to `opportunity-management:ai-suitability` where the record needs revisiting.
- To `automation:automation-assessment` where a deterministic flow should replace an AI component.
- To `design-authority:ai-design-review` with findings for the consolidated verdict.

## Reviewer gates

This skill is part of the `design-authority` gate, blocking from risk tier 2 and advisory below it. Findings about
decisions affecting people are shared with `responsible-ai`. Disagreement escalates to the accountable executive for
written risk acceptance.

## Failure modes

- The challenge becomes general scepticism about AI, and teams stop bringing designs to the gate.
- A keen sponsor means the challenge is skipped, and the solution automates a broken process.
- Findings say "too much AI" without naming the simpler alternative, so nothing changes.
- The challenge repeats intake suitability without looking at how the design has drifted.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Block a design without naming the simpler alternative and the risk it avoids.
- Accept a model making a decision that a stated rule could make where errors have consequences.
- Skip the challenge because a sponsor is enthusiastic.
- Treat a reasoned pass as a failure of the review.
