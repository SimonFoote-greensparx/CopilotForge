---
name: work-delegation-design
description: Designs the delegation boundary for work handed to Copilot Cowork, deciding which parts Cowork does, which stay with people, who stays accountable and what authority Cowork is given to read, draft, send or change. Use when a team has a task that suits Cowork and must agree what to hand over, when delegated work has overstepped, or when a manager asks who answers for delegated output.
license: CC-BY-4.0
metadata:
  department: copilot-cowork
  lifecycle: Envision, Deliver
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3
  platforms: copilot-cowork, m365-copilot
  edition-support: starter, scale, enterprise
  reviewers: responsible-ai, security-privacy
  sources: ms-copilot-cowork-customise, ms-copilot-privacy, ms-responsible-ai, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# Work delegation design

## Purpose

Delegating to Copilot Cowork is a management decision before it is a technical one: what is handed over, what is kept,
and who still answers for the result. This skill produces a delegation map for a piece of work that has already been
judged suitable, separating the parts Cowork does from the judgements, relationships and approvals that stay with
people, and stating the authority Cowork is given. Delegation goes wrong when the boundary is left implicit, so Cowork
ends up drafting the sensitive message the manager meant to write, or nobody can say who approved what it sent.

## When to use

- A task has passed `copilot-cowork:cowork-use-case-assessment` and the team must agree what to hand over.
- Delegated work has overstepped, for example sending, filing or deciding something a person expected to do.
- A manager or sponsor asks who is accountable for output that Cowork produced.
- A team wants to delegate more of an existing task and needs to move the boundary deliberately.

## When not to use

- Deciding whether the task suits Cowork at all - use `copilot-cowork:cowork-use-case-assessment`.
- Breaking the delegated part into ordered steps with outputs - use `copilot-cowork:multi-step-work-design`.
- Designing the specific checkpoints and approvals inside the run - use `copilot-cowork:human-checkpoint-design`.
- Assessing how AI changes roles and jobs across a group of people - use `change-and-communications:people-change-impact`.
- Formal review of human oversight for a tier 2 or higher solution - use `responsible-ai:human-oversight`.

## Questions to ask first

1. Who owns the outcome today, and will that person still answer for it once part of the work is delegated?
2. Which parts of the work rely on judgement, relationships or knowledge that only a person holds?
3. What is Cowork allowed to do with what it produces: only draft, or also send, file, book, publish or update records?
4. Who outside the team will see or be affected by the output, and would they expect a person to have written it?
5. What would make the delegator take the work back mid-way?

## Required inputs

- The Cowork fit verdict and conditions from `copilot-cowork:cowork-use-case-assessment`.
- A plain description of how the work is done today, step by step, from the people who do it.
- The organisation's Cowork governance position, including any restrictions on sending or acting, from `copilot-cowork:cowork-governance`.
- The risk tier where one has been set.

Where today's process is undocumented, walk it with the person who does it rather than guessing. Never assume an action
permission is allowed; mark it to confirm with the governance owner.

## Decision framework

Classify each part of the work into one of four delegation levels, then apply the rules below.

| Level | Cowork may | Person keeps | Typical parts |
|---|---|---|---|
| D0 Keep | Nothing | All of it | Decisions about individuals, negotiation, sensitive relationship messages, final sign-off |
| D1 Prepare | Find, gather, summarise, compare | The judgement and the draft | Research, collating evidence, listing options |
| D2 Draft | Produce a complete draft for review | Edit and decide whether to use | Reports, replies, plans, trackers |
| D3 Act with approval | Prepare and then carry out an action once approved | The approval at a named checkpoint | Sending agreed messages, filing, scheduling |

- Anything that decides an outcome for a person, a payment or a legal position stays at D0 or D1 unless risk classification and `responsible-ai` review say otherwise.
- D3 is only allowed where the action is reversible or low consequence, the approval is explicit, and governance permits it.
- Accountability never moves to Cowork. Every part, at every level, has a named human owner.
- If more than half the parts sit at D0, question whether delegation is worth the overhead.

## Practitioner approach

Start by mapping the work as it is done now, not as it is imagined. Ask the person who does it to talk through the last
real instance: where they started, what they opened, what they decided, who they spoke to and what they sent. Write each
part on its own line. This list becomes the delegation map, and it usually reveals judgement buried in tasks that looked
mechanical, such as deciding which supplier complaint deserves a phone call.

For each part, ask two questions: does doing this well need something only a person has, and what is the cost of getting
it wrong? Judgement about people, trust-sensitive communication and anything with legal or financial effect sits at D0
or D1. Gathering, summarising and comparing sit comfortably at D1 or D2. Drafting is the sweet spot for most teams,
because the delegator reads and edits before anything leaves their hands.

Be explicit about actions. The jump from "draft the reply" to "send the reply" is the one that causes most trouble,
because it removes the moment where a person notices the error. Treat D3 as an exception that needs a reason, an
explicit approval and a governance position that allows it. If you are unsure, design for D2 first and move to D3 only
after `copilot-cowork:workflow-validation` shows the drafts are reliably right.

Name the accountable person for the whole outcome and for each part. In most cases this is the person who delegated, and
the delegation map should say so in plain words. Where the output reaches customers, suppliers or colleagues outside the
team, decide whether they should be told that AI helped to prepare it, and record that decision for the
`responsible-ai` reviewer.

Agree the take-back triggers: the conditions under which the delegator stops the run and does the work themselves. Good
triggers are concrete, such as "a source contradicts the policy", "the customer has complained before" or "the draft
names an individual". These become inputs to `copilot-cowork:human-checkpoint-design`.

Finally, test the boundary with the team. Read the delegation map to the people who will work with it and ask what
would surprise them. If a manager expects to see every external message and the map puts sending at D3, resolve that
now. Record the map with the task design, and revisit it whenever the work, the team or the governance position changes.

## Outputs

- A delegation map in the `cowork-task-design` template: each part of the work, its delegation level, the human owner and the reason.
- The accountable owner for the delegated outcome, stated in plain words.
- The authority granted to Cowork (read, draft, act with approval) and the take-back triggers.
- Open questions for governance, security or responsible AI review, each with an owner.

## Microsoft platform considerations

Cowork works within the delegating person's Microsoft 365 context and permissions, and what it can do is shaped by the
plugins, skills and custom instructions the organisation enables. Check the current capabilities and controls in the
source records (`ms-copilot-cowork-customise`, `ms-copilot-privacy`) before setting a part at D3, and match the map to what
the organisation's governance actually allows rather than to what the product can do.

## Adoption considerations

People accept delegation more readily when they can see what stays with them. Share the map with the team, explain that
accountability does not move, and start at D1 and D2 so confidence grows from evidence. Route role-level concerns about
changing work to `change-and-communications:people-change-impact`.

## Knowledge considerations

Parts delegated at D1 and above depend on the sources Cowork will read. List them against each part so that
`copilot-cowork:task-context-design` and `copilot-cowork:grounding-readiness` can act on them.

## Security and privacy considerations

Delegation inherits the delegator's access. Check that no delegated part would draw sensitive content into an output
for a wider audience, and that any D3 action that sends or shares information has been agreed with the
`security-privacy` reviewer from risk tier 2.

## Responsible AI considerations

Decisions about people stay with people. Record where AI-prepared content reaches others and whether they are told. From
risk tier 2, the delegation map is evidence for `responsible-ai:human-oversight`.

## Evaluation requirements

The map must state what a correct output looks like for each delegated part, so that `copilot-cowork:workflow-validation`
has criteria to test against before any part moves from D2 to D3.

## Value measures

Use the baseline from the use-case assessment and add the measure that reflects the delegated parts, such as time from
request to usable draft. Report at team level; never use delegation data to compare individuals.

## Scale notes

### Starter

A single page listing the parts, their level and the owner is enough. Keep everything at D1 or D2 until the team has
experience.

### Scale

Champions help teams draw maps using the shared levels, and the CoE publishes example maps for common tasks so teams
start from a tested boundary.

### Enterprise

Business units set default levels for common work types within the central policy; any D3 design at risk tier 2 or above
is reviewed centrally before use.

## Hand-offs

- To `copilot-cowork:multi-step-work-design` to sequence the delegated parts.
- To `copilot-cowork:human-checkpoint-design` with the take-back triggers and D3 approvals.
- To `copilot-cowork:task-context-design` with the sources each part needs.
- To `responsible-ai:human-oversight` from risk tier 2.

## Reviewer gates

From risk tier 2, `responsible-ai` reviews the boundary for decisions about people and for transparency to those affected,
and `security-privacy` reviews any part that sends, shares or files information. Both classify findings as blocking or
advisory, and D3 actions do not go live with an open blocking finding.

## Failure modes

- The boundary is never written down, so Cowork drafts and sends a message the manager expected to handle personally.
- Accountability is assumed to sit with "the AI", and no person can explain an output when it is challenged.
- Parts move from D2 to D3 because drafts look good, before any validation evidence exists.
- Judgement hidden inside an apparently mechanical step is delegated without anyone noticing.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Delegate a decision about an individual's employment, pay, performance or rights.
- Leave any delegated part without a named human owner.
- Allow Cowork to send, publish or change records without an explicit approval designed in.
- Use the delegation map to assess or compare the performance of individual staff.
