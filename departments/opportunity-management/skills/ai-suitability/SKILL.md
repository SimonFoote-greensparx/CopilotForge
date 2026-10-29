---
name: ai-suitability
description: Decides whether a framed business problem should be solved with AI at all, and if so which pattern fits - Copilot Chat, a Cowork task, an agent, Copilot Code, a Foundry solution or plain automation - with the reasoning recorded. Use when an idea arrives at intake, when a team has already picked a tool, or when a sponsor asks why AI is preferable to process change or training.
license: CC-BY-4.0
metadata:
  department: opportunity-management
  lifecycle: Envision, Deliver
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-cowork, copilot-code, copilot-studio, ai-foundry, power-platform
  edition-support: starter, scale, enterprise
  reviewers: design-authority
  sources: ms-agents-extensibility, ms-agents-compare, ms-copilot-studio-zoned-governance, ms-foundry-models, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# AI suitability

## Purpose

Most requests reach an AI programme with the answer already chosen: "we need an agent", "can Copilot do this". This skill
steps back and asks whether AI is the right answer before anyone asks which AI. It records why AI beats the cheaper
alternatives (fixing the process, ordinary automation, training, or a capability the organisation already owns), and
when AI does fit, it selects the simplest pattern that will work. Programmes go wrong here by building agents for
problems that were really broken processes, and by choosing a pro-code platform for a need a prompt pattern would meet.

## When to use

- An opportunity has been framed and needs a go or no-go on AI before it joins the backlog.
- A team arrives with a solution already chosen and the choice needs testing.
- A sponsor asks why AI is preferable to process change, automation or training.
- Several ideas look similar and need consistent treatment across business units.

## When not to use

- Framing the business problem, owner and outcome in the first place - use `opportunity-management:problem-framing`.
- Classifying the risk tier of a solution already chosen - use `opportunity-management:risk-classification`.
- Ranking suitable opportunities against each other - use `opportunity-management:opportunity-prioritisation`.
- Designing the agent once the agent pattern is chosen - use `m365-agents:agent-use-case-design`.
- Formal architecture and platform conformance for tier 2 and above - the `design-authority` and `ai-architecture` departments (planned).

## Questions to ask first

1. What exactly fails today, for whom, how often, and what does it cost? Without a framed problem this skill cannot decide anything, so send it back to framing.
2. Has anyone tried fixing the process, clarifying ownership or training people? Many "AI problems" disappear when a form is redesigned or a policy is written down.
3. Does the task need judgement over language, documents or conversation, or is it a fixed sequence of steps on structured data? The second is automation, not AI.
4. Who checks the output before it has an effect, and could they tell if it were wrong?
5. Is the knowledge or data the solution would rely on owned, current and accessible to the people who would use it?

## Required inputs

- A framed problem statement with a named business owner, from `opportunity-management:problem-framing`.
- The volume and frequency of the task, and the people affected (roles, not names).
- What the organisation already licenses and has approved (from the organisation profile or the CoE's approved tools list).
- An initial view of data sensitivity and who would see the output.

Where an input is missing, record it as "to confirm" in the decision record and lower the confidence of the
recommendation. Never assume an approved tool or a licence.

## Decision framework

Work down the ladder and stop at the first rung that meets the need. Each rung down adds capability and also adds
ownership, testing and operating cost.

| Rung | Choose it when | Stop and reconsider if |
|---|---|---|
| 0. No AI - fix the process, policy or training | The failure is unclear ownership, a missing rule, poor data entry or a skills gap | Volume and variability of language-based work remain high after the fix |
| 1. Deterministic automation | Steps are fixed, inputs are structured, and exceptions are rare and well defined | The work needs judgement over unstructured content |
| 2. Copilot Chat or Copilot in the apps (individual use) | One person needs help to think, draft, summarise or analyse, and can verify the result | The same prompt pattern is being repeated by many people, or the knowledge is not in their own work context |
| 3. Copilot Cowork task | A person wants to delegate a bounded multi-step outcome with explicit checkpoints and a final review | Many people need the same capability every day, or it must run without a person directing it |
| 4. Agent (declarative, built in Agent Builder or Copilot Studio) | A defined audience needs a reusable capability grounded in governed knowledge, with an owner | It needs custom models, retrieval engineering, complex orchestration or production-grade evaluation |
| 5. Copilot Code build | The outcome is working software, scripts or repository changes | Generated code would escape normal engineering review |
| 6. Microsoft Foundry solution | Specialist models, retrieval, tools or orchestration are genuinely required, and the organisation can operate them | The added complexity cannot be justified by value or cannot be supported |

Before walking the ladder, use the problem type recorded at framing as a first pass. It points to a likely starting
rung; the ladder still decides. Not every problem requires AI, and the first three rows usually end at rung 0 or 1.

| Problem type | Usual answer | Starting rung to test |
|---|---|---|
| Process issue | Change the process, ownership or policy | 0 |
| Education gap | Training, or an adoption scenario for tools people already have | 0, then 2 |
| Repetitive task on structured inputs | Ordinary automation | 1 |
| Knowledge issue in owned content | An agent grounded in that content, often built in Agent Builder | 4 (test 2 and 3 first) |
| Business data workflow with judgement and actions | An agent built in Copilot Studio, with automation doing the acting | 4 with 1 (test 6 only if 4 cannot meet it) |

Combine rungs when the work has distinct parts, for example an automation that routes documents and an agent that
answers questions about them. Record the rung for each part.

## Practitioner approach

Start by restating the problem in one sentence, using the owner's words and a measure: "Contract managers spend most of
Monday compiling site reports from emails, and the reports are late." If you cannot write that sentence, stop and hand
back to framing. Suitability decisions made on vague problems are the main reason pilots stall later.

Next, test rung 0 honestly. Ask what would happen if the process were simplified, the policy clarified or people were
shown how to use what they already have. Look for signs that the problem is organisational: nobody owns the data, three
teams keep the same list, or the "knowledge" lives in one person's head. AI layered over these problems scales the
confusion. Where rung 0 resolves most of the issue, recommend it and record the AI idea as deferred rather than rejected,
so the conversation can resume once the basics are fixed.

If language, documents or conversation are central and the volume justifies it, walk the remaining rungs in order. Ask
who does the work, how often, and who checks the result. A task done occasionally by one person, who can verify the
output, belongs at rung 2 even if it looks impressive enough to justify an agent. When the same prompt pattern spreads
across a team, that is the signal for a shared asset: a published prompt, a Cowork task design, or an agent with an
owner. When the work needs actions in other systems, check whether deterministic automation should do the acting and AI
only the interpreting.

For each candidate rung, write down the governance question from the decision framework and answer it. If nobody can
say who would own an agent's instructions, knowledge and review cycle, the agent rung is not yet available, however
well it fits technically. Name the knowledge the solution depends on and its owner; if that knowledge is poor, the
recommendation carries a precondition to fix it.

Product capability changes month by month. Before recommending a rung that depends on a specific feature, check the
current source records for availability, licensing and limits, and cite them in the decision record rather than
relying on memory.

Finally, record the decision: the rung chosen, the rungs rejected and why, the preconditions, the open questions, the
initial risk tier to be confirmed by `opportunity-management:risk-classification`, and who made the decision. Share it
with the business owner in plain language. A good suitability record lets someone six months later understand why the
organisation did not build the obvious agent.

## Outputs

- An AI suitability decision record on the `opportunity-canvas` template: problem, rung chosen, rungs rejected with reasons, preconditions, open questions and decision owner.
- A short plain-language summary for the business owner.
- Where AI is not recommended, a referral to the route that will help (process improvement, automation or training).

## Microsoft platform considerations

Copilot Chat, Copilot in the Microsoft 365 apps, Copilot Cowork, agents built in Agent Builder or Copilot Studio,
Copilot Code and Microsoft Foundry serve different levels of reuse, autonomy and engineering effort. Prefer what the
organisation already licenses and has approved. Agents built in Copilot Studio run inside Power Platform environments,
so the environment and data-policy position matters to the choice. Availability, licensing and naming change often;
confirm them against the source records in `references/sources.md`.

## Adoption considerations

A rung 2 recommendation is an adoption outcome, not a rejection: route it to `copilot-adoption:scenario-discovery` so the
pattern reaches the people who need it. Explain "no AI" decisions carefully, because teams who hear only "no" stop
bringing ideas.

## Knowledge considerations

Any rung from 3 upwards depends on knowledge the solution can ground on. Name the sources, their owner and their
condition. Poor or unowned knowledge is a precondition to fix, recorded against the decision.

## Security and privacy considerations

Note the sensitivity of the data involved and who would see outputs. A rung that widens access to sensitive content
(an agent shared beyond the original audience, for example) raises the risk tier and brings the `security-privacy`
gate forward.

## Responsible AI considerations

Ask whether the output informs decisions about people, money, safety or rights. If so, the solution needs explicit human
oversight whatever the rung, and the case moves to the `responsible-ai` department (planned) through risk
classification. Some uses should not be built at all; record that outcome plainly.

## Evaluation requirements

For rungs 4 to 6, name the evidence that would show the solution works well enough: a small set of real questions with
known good answers, and the acceptance threshold the business owner agrees. For rungs 2 and 3, the evidence is that the
person checking the output can verify it.

## Value measures

Record the baseline the problem statement implies (time, delay, error rate, rework) and the measure the owner will use
to judge success. The value hypothesis must be achievable at the chosen rung; if it needs rung 6 to pay back, say so.

## Scale notes

### Starter

Make the decision in a short conversation between the business owner and whoever leads AI, recorded on one page. Most
needs land at rungs 0 to 3, and that is a good outcome. Use a partner's view for anything at rung 5 or 6.

### Scale

Run suitability as a standing step in the CoE intake, with a consistent decision record so similar ideas are treated
alike across business units. Reuse previous decisions as precedents.

### Enterprise

Federate first-pass suitability to business-unit spokes using the shared ladder, with the hub reviewing anything at rung
4 and above. Track decisions in the portfolio so patterns of rejected ideas inform training and process work.

## Hand-offs

- To `opportunity-management:risk-classification` to confirm the risk tier of the chosen rung.
- To `opportunity-management:opportunity-prioritisation` when the opportunity joins the backlog.
- To `m365-agents:agent-use-case-design` when the agent rung is chosen.
- To `copilot-adoption:scenario-discovery` when the answer is individual Copilot use.

## Reviewer gates

From risk tier 2, the rung choice is open to challenge by `design-authority` (planned) for unnecessary AI or the wrong
platform. Until that department is built, the CoE lead records the challenge and the response on the decision record.

## Failure modes

- The rung is chosen to match a tool the team already wanted, and the record is written to justify it afterwards.
- Rung 0 is skipped because process change is less exciting, so the agent automates a broken process.
- An agent is approved without an owner for its knowledge, and its answers decay within months.
- A feature assumed from memory turns out to be unavailable or unlicensed, and the plan stalls.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Recommend AI before the problem is framed with an owner and a measure.
- Choose a pattern because it is new or impressive rather than because it is the simplest that works.
- Assert product availability, licensing or limits from memory.
- Treat "no AI" as a failure, or reject an idea without routing it somewhere useful.
