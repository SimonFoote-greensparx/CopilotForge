---
name: agentic-workflow-design
description: Designs multi-step agentic workflows in Microsoft Foundry with bounded autonomy - the steps, which are deterministic and which are agentic, the decisions each agent may take alone, checkpoints, budgets, stop conditions and recovery. Use when a process spans several agents or steps, when a team wants an agent to run unattended, or when an autonomous prototype keeps looping or overreaching.
license: CC-BY-4.0
metadata:
  department: ai-foundry
  lifecycle: Mobilise, Deliver, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure, entra
  edition-support: starter, scale, enterprise
  reviewers: design-authority, responsible-ai, security-privacy
  sources: ms-foundry-models, ms-agents-compare, ms-responsible-ai, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Agentic workflow design

## Purpose

An agentic workflow lets models plan, call tools and hand work between steps with less direction from a person, which
is exactly what makes it useful and what makes it risky. This skill designs the workflow so that autonomy is a
deliberate, bounded grant: each step is either deterministic or agentic for a stated reason, each agent has a written
decision boundary, and the whole run has checkpoints, budgets and stop conditions. Workflows go wrong when the model is
asked to orchestrate what a fixed sequence would do better, when nothing stops a run that has lost its way, and when a
failure halfway through leaves records half changed and nobody knows which.

## When to use

- A process spans several steps or agents and the team must decide how much of it the model directs.
- A team wants an agent to run unattended, on a schedule or on an event, rather than in a conversation.
- An autonomous prototype loops, repeats tool calls, wanders off task or takes actions nobody expected.
- `ai-foundry:foundry-agent-architecture` has found that the hard question is the flow between agents, not the agents themselves.
- A workflow is being extended with a new step that writes, sends or spends.

## When not to use

- Designing a single agent's responsibility, identity, tools and state - use `ai-foundry:foundry-agent-architecture`.
- Designing the contract of one tool - use `ai-foundry:foundry-tool-design`.
- Multi-agent hand-offs inside Copilot Studio - use `copilot-studio:multi-agent-design`.
- Multi-step delegated work in Copilot Cowork - use `copilot-cowork:multi-step-work-design`.
- A fixed flow in Power Automate with an AI step - use `automation:flow-design-patterns`.
- Formal design and review of human oversight - that is the reviewer skill `responsible-ai:human-oversight`.

## Questions to ask first

1. What is the outcome of a complete run, how will anyone know it succeeded, and what is the worst outcome of a run that goes wrong?
2. Which steps are genuinely variable and need judgement, and which always happen in the same order with the same rules?
3. Which actions change something outside the workflow, and can each be undone?
4. Who is accountable for a run that is in progress, and how quickly could they intervene if it misbehaved?
5. What may a run spend, in time, tool calls, tokens and money, before it must stop and ask?
6. What triggers a run, and what happens if the same trigger fires twice?

## Required inputs

- The approved solution design on the `foundry-solution-design` template, with risk tier and the agent architecture.
- A current-state description of the process the workflow replaces or supports, with its exceptions.
- The tool inventory with effect classes from `ai-foundry:foundry-tool-design`.
- Human-oversight requirements already set for the risk tier.

Where the process exceptions, the accountable owner or the effect class of a tool are unknown, mark them
`[To confirm: ...]` and design that step as deterministic or human-performed until they are known. Never grant
autonomy to cover a gap in understanding.

## Decision framework

Place every step on the autonomy ladder and use the lowest level that does the job. Controls accumulate as autonomy
rises.

| Level | The step | Use it when | Minimum controls |
|---|---|---|---|
| A. Deterministic | Runs fixed code or a flow; no model decision | The rule is known and stable | Normal testing and error handling |
| B. Model assists | A model classifies, extracts or drafts; code decides what happens next | Judgement is needed over content but the routing is known | Output schema validation, confidence threshold, fall back to a person |
| C. Model chooses within a set | An agent picks among a fixed list of next steps or tools | The right path depends on content and the options are enumerable | Allowed-action list, step and tool-call budget, trace of each choice |
| D. Model plans | An agent decomposes the goal and sequences its own steps | The path cannot be enumerated and the effects are reversible | Plan shown before effects, per-run budgets, checkpoint before any write, kill switch |
| E. Unattended with external effect | The workflow acts without a person in the run | Low impact, reversible, high volume, proven at level D | All of the above, plus effect limits, sampling review, automatic suspension on anomaly, and responsible AI approval from tier 2 |

Irreversible effects that touch people, money, safety or rights always pass a human checkpoint, whatever the level.

## Practitioner approach

Draw the process before drawing agents. Write the steps of a complete run as plainly as possible, including the
exceptions people handle today, and mark where judgement over language or documents is really needed. In most
processes that is two or three points; the rest is routing, lookup and record-keeping that code does more cheaply and
more predictably. Assign each step a level from the ladder and write one sentence on why it is not one level lower. If
nobody can write that sentence, drop the level.

Prefer an explicit orchestration skeleton with agentic steps inside it over a single planner agent that improvises the
whole run. A skeleton gives you known checkpoints, resumable state and a trace a support engineer can read. Reserve
level D planning for the parts of the work where the path truly cannot be predicted, and keep it inside a bounded
sub-flow with its own budget.

Write a decision boundary for each agent: what it may decide alone, what it must propose for confirmation, what it must
refuse and when it must hand to a person. Express budgets in terms the platform can enforce, such as maximum steps,
tool calls, elapsed time and tokens per run, and define what happens when one is reached: stop, summarise progress and
escalate, never silently continue.

Design state and recovery next. Decide where run state lives, how a failed run resumes from its last checkpoint rather
than from the start, and how every write step is made idempotent so a retry or a duplicate trigger does not repeat an
effect. Where several writes must succeed together, design the compensating action for each so a partial run can be
unwound, and name who runs it.

Place checkpoints where a person can add real judgement, with enough context to decide quickly: what the workflow
intends to do, why, and what it has done so far. A checkpoint that asks for approval of a raw tool call teaches people
to click through. Agree the design with `responsible-ai:human-oversight` for tier 2 and above.

Treat everything an agent reads as potentially hostile. Content from documents, mail or the web can carry instructions,
so no step should gain a more powerful action merely because of something it read; effect-bearing steps take their
parameters from validated state, not from free text.

Finally, plan to earn autonomy. Launch at a lower level than the target, observe runs through
`ai-foundry:foundry-observability`, and raise a step's level only when evidence shows it behaves. Record what the
design cannot determine, chiefly how the model will behave on inputs unlike the test set, which only monitored
operation reveals.

## Outputs

- The workflow section of the `foundry-solution-design` template: step map with the level of each step and its rationale, decision boundary per agent, budgets and stop conditions, checkpoints, state and recovery design, and compensating actions.
- A kill-switch and suspension procedure for the operations team.
- An autonomy progression plan stating the evidence needed before any step moves up a level.

## Microsoft platform considerations

Foundry offers more than one way to orchestrate agents, from service-managed multi-agent and workflow features to
orchestration written in code with Microsoft's agent frameworks, and these capabilities are changing quickly, with some
in preview. Check the current source records before relying on a specific orchestration feature, its state handling or
its approval mechanism, and record any preview dependency as a risk. Run long or scheduled workflows inside the
organisation's Azure governance, with managed identities scoped per step rather than one identity for the whole run.

## Adoption considerations

People whose work is partly taken over by a workflow need to know what it now does, what still reaches them and how to
stop or correct it. Involve them in placing checkpoints; they know where errors hurt. Communicate autonomy increases as
changes, not as quiet configuration.

## Knowledge considerations

Steps that ground on organisational content inherit its quality. Name the sources each agentic step uses and their
owners, and route grounding choices to `ai-foundry:foundry-grounding-strategy`. A workflow acting on stale knowledge
does damage faster than a chat agent answering from it.

## Security and privacy considerations

Unattended workflows run with service identities and can act at volume, so a compromised or confused run has a large
blast radius. Scope identities per step, limit the volume and value of effects per run, protect run state that holds
personal data, and set its retention with the data owner. `security-privacy:ai-identity-and-access-review` reviews the
design from tier 2.

## Responsible AI considerations

Autonomy shifts accountability unless it is designed back in. Name the accountable person for each run type, keep a
human checkpoint on consequential effects, and make sure affected people can challenge an outcome through
`responsible-ai:escalation-and-appeal`. Some decisions should never be delegated to a workflow; record them as out of
scope.

## Evaluation requirements

Evaluate whole runs as well as individual steps: task completion, correct path selection, budget adherence, correct
stopping and escalation, recovery from injected tool failures and resistance to instructions planted in content. Agree
thresholds per level before testing, with `ai-foundry:model-evaluation` and `ai-foundry:foundry-safety-evaluation`.

## Value measures

Measure completed runs without intervention, escalation rate, reversal or compensation rate and elapsed time per case
against the process baseline, owned by the business owner. A falling escalation rate is only good news if the reversal
rate is not rising.

## Scale notes

### Starter

Keep workflows at levels A to C, with a person confirming every write. One well-traced workflow teaches more than an
ambitious planner that nobody can debug.

### Scale

Standardise the skeleton, budgets, kill switch and run-state pattern so each workflow starts from a reviewed baseline,
and require evidence before any step moves to level D or E.

### Enterprise

Maintain a register of workflows with their autonomy levels, identities and effect limits, review level E workflows on
a fixed cycle, and coordinate suspension across workflows that share tools or systems.

## Hand-offs

- To `ai-foundry:foundry-tool-design` for each tool the workflow calls.
- To `ai-foundry:foundry-observability` so runs, choices and checkpoints are traced.
- To `ai-engineering:ai-resilience` for retry, timeout and degradation patterns.
- To `responsible-ai:human-oversight` to review checkpoints from tier 2.
- To `ai-foundry:foundry-production-readiness` before the workflow runs on live work.

## Reviewer gates

From risk tier 2, `responsible-ai` reviews the autonomy levels and human checkpoints, `security-privacy` reviews
identities and effect limits, and `design-authority` checks that agentic steps are justified over deterministic ones.
Any level E step with an irreversible external effect needs explicit approval at any tier.

## Failure modes

- A single planner agent orchestrates a process that was really a fixed sequence, and becomes slow, costly and unpredictable.
- A run has no budget or stop condition, loops on a failing tool and consumes quota until someone notices the bill.
- A retry repeats a send or payment step because writes were not idempotent.
- Checkpoints ask people to approve raw tool calls without context, so approval becomes a reflex and errors pass.
- Instructions hidden in a processed document steer the workflow into an action outside its purpose.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Make a step agentic when a deterministic step would do the job.
- Run a workflow without per-run budgets, stop conditions and a kill switch.
- Let an irreversible effect on people, money, safety or rights happen without a human checkpoint.
- Raise a step's autonomy without evidence from monitored operation.
