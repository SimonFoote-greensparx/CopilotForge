---
name: coe-readiness
description: Checks whether an organisation is ready to launch an AI Centre of Excellence - a sponsor who will decide, an owning business unit, a lead with real time, core team capacity, starting demand, knowledge owners, approved-use guidance and enablement support - and returns a launch, launch-with-conditions or not-yet verdict. Use when leadership wants a CoE before anyone has checked the preconditions, or when an earlier CoE attempt stalled.
license: CC-BY-4.0
metadata:
  department: ai-centre-of-excellence
  lifecycle: Discover, Mobilise
  maturity: explorer, adopter, builder, scaler
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-coe-starter-kit, ms-copilot-studio-guidance, ms-champion-programme
  status: draft
  authors: Simon Foote
---

# CoE readiness

## Purpose

A Centre of Excellence launched without a sponsor who decides, a business unit that owns it and people with real time
becomes a monthly meeting with a logo. This skill checks the preconditions before a charter is signed or a launch date
announced, separates what must exist on day one from what the CoE can build in its first months, and gives a clear
verdict. Readiness checks usually go wrong by counting enthusiasm as capacity and by treating the existence of licences
or a central AI team as proof that a CoE can run.

## When to use

- Leadership has asked for an AI CoE and nobody has yet checked whether the people, ownership and starting material exist.
- A sponsor wants to announce a CoE and needs to know what must be true first.
- A previous CoE or AI working group stalled and the organisation wants to relaunch without repeating the same mistakes.
- A business unit wants its own CoE under a hub and the hub needs a consistent test before agreeing.

## When not to use

- Judging whether the organisation is ready to roll out Microsoft Copilot to users - use `copilot-adoption:adoption-readiness`.
- Diagnosing the organisation's overall AI maturity and archetype - use `ai-strategy:ai-maturity-assessment`.
- Assessing how well an existing, running CoE performs - use `ai-centre-of-excellence:coe-maturity-assessment`.
- Writing the charter once readiness is confirmed - use `ai-centre-of-excellence:coe-charter`.
- Planning the dated launch itself - use `ai-centre-of-excellence:coe-launch-roadmap`.

## Questions to ask first

1. Which executive will sponsor the CoE, and have they agreed to attend steering and take priority decisions, or only to be kept informed?
2. Which business unit benefits most and will own the CoE, and who in it could lead with a stated number of days each month?
3. Where are AI ideas, agents and automations appearing today, and is anyone already keeping a list?
4. Is there approved guidance on acceptable AI use, and who would classify risk for anything shared beyond one team?
5. What can the central AI or IT enablement function realistically offer: advice, platform administration, technical specialists, or none yet?

## Required inputs

- The organisation profile and edition from `organisation-tailoring:edition-and-archetype`, or at least the size and number of business units.
- The strategic outcomes the CoE would serve, from `ai-strategy:strategic-outcomes`, even in draft.
- Any existing list of AI ideas, pilots, agents or automations, however partial.
- Current AI policy or acceptable-use guidance, if one exists.
- Declared availability of candidate roles, agreed with their managers.

Record every missing input as "to confirm" against the relevant criterion. A criterion with no evidence is not met; do
not infer availability or sponsorship from job titles.

## Decision framework

Rate each criterion as met, partly met or not met, using evidence rather than intent. The gate column says whether the
criterion must be met before launch or may be closed during the Foundation phase.

| Criterion | Evidence that it is met | Gate |
|---|---|---|
| Active sponsor | Sponsor has agreed in writing to chair or attend steering and make priority decisions | Before launch |
| Owning business unit | A unit has accepted ownership of outcomes, not just hosting | Before launch |
| CoE lead with time | A lead role with days per month agreed by their manager | Before launch |
| Core team capacity | At least two further people with agreed time and complementary skills (one for Starter) | Before launch |
| Starting demand | A list of real ideas or problems with business owners, even if short | Before launch |
| Approved-use guidance | Acceptable-use guidance exists or a date to approve one is agreed | Foundation phase |
| Risk tiering | A tiering approach is available or adopted from `ai-centre-of-excellence:coe-governance-model` | Foundation phase |
| Knowledge owners | Owners named for the knowledge most ideas would rely on | Foundation phase |
| Central enablement support | The enablement function has agreed what it will provide | Foundation phase |
| Champions or volunteers | Some people have offered time, with manager agreement | Foundation phase |
| Collaboration space | A shared space on tools the organisation already runs | Foundation phase |

| Verdict | Rule |
|---|---|
| Launch | All "before launch" criteria met; no more than three Foundation criteria not met |
| Launch with conditions | All "before launch" criteria met or partly met with a dated action and an owner |
| Not yet | Any "before launch" criterion not met, most often sponsor, owning unit or lead time |

A "not yet" verdict comes with the smallest useful alternative, usually an AI working group with a sponsor-approved
remit and a review date.

## Practitioner approach

Start with the sponsor conversation, because everything else depends on it. Ask the sponsor what decisions they expect
to make in the first three months and how often they will be in the room. A sponsor who wants monthly updates but
delegates every decision is a stakeholder, not a sponsor; record "partly met" and say so plainly. If the sponsor role is
uncertain, pause the assessment and route to `ai-centre-of-excellence:coe-sponsor-role` before going further.

Next, test ownership. Ask which business unit's outcomes will improve and whether that unit accepts that it owns
priorities, knowledge and benefits. The common trap is a central IT or AI team volunteering to "own the CoE" because
nobody in the business stepped forward. That can host a working group, but it is a warning sign for a CoE, and the
verdict should carry a condition to transfer ownership within a stated period.

Then check capacity with arithmetic, not goodwill. For each candidate role, write the days per month their manager has
agreed. Add them up and compare with what the first two phases need: triage, framing, a first knowledge register and
one or two quick wins. If the total is a handful of days, the honest answer is a working group, not a CoE.

Check demand next. Ask for the ideas already circulating, the agents and automations people have built, and the
pilots nobody owns. A CoE launched without a starting backlog spends its first quarter looking for work and loses
credibility. Where nothing is listed, make "find what already exists" the first condition.

Work through the Foundation criteria quickly. These can be built in the first months, but each needs an owner and a
date. Approved-use guidance and a risk tiering approach matter most, because without them the CoE cannot route ideas
safely. Knowledge owners matter next, because most early ideas depend on content someone has to maintain.

Interview widely enough to avoid a single view: the sponsor, the proposed lead, the enablement function, someone from
information security or data protection, and two or three people who have already tried building something. Look for
evidence in artefacts, not in enthusiasm.

Write the verdict, the criteria table, the conditions with owners and dates, and the recommended form: AI working group,
business-owned CoE, or a spoke under an existing hub. Present it to the sponsor in one page. Say what the assessment
cannot tell you: it does not predict whether people will use what the CoE delivers, and it does not replace the
organisation-wide maturity view.

## Outputs

- A CoE readiness assessment: criteria table with ratings and evidence, verdict, recommended form, and conditions with owner role and date.
- A one-page sponsor summary with the verdict and the two or three actions that would change it.
- The readiness section of the `coe-launch-plan` template, carrying open conditions into the launch.
- Where the verdict is "not yet", a working group remit and a reassessment date.

## Microsoft platform considerations

Readiness is mostly about people and ownership, but the existing estate matters. If makers already build agents in
Copilot Studio or flows in Power Platform, the CoE will inherit them, so check whether the CoE Starter Kit or admin
inventory can show what exists. Check current capability in `references/sources.md` before relying on any inventory
component, and route licensing questions to the Microsoft licensing guide or a licensing partner.

## Adoption considerations

A visible CoE raises expectations. Do not announce it until the verdict is "launch" or "launch with conditions", and
make sure the first message explains how to bring an idea and what will happen to it. Existing enthusiasts who built
things without permission are a readiness asset; invite them in rather than treating them as a compliance problem.

## Knowledge considerations

Ask which knowledge the first ideas will rely on and whether each source has an owner. Unowned knowledge does not stop
a launch, but it shapes which quick wins are safe to start, so record it as a Foundation condition.

## Security and privacy considerations

Check that information security and the data protection officer know the CoE is coming and agree how they will be
involved from tier 2. Where agents already exist without owners, list them as a Foundation priority for registration
rather than an immediate shutdown, unless one exposes sensitive data.

## Responsible AI considerations

Ask whether any idea already circulating would inform decisions about people, money, safety or rights. If so, the CoE
must have a route to responsible AI review before it touches that idea; note this as a condition.

## Evaluation requirements

Not applicable to the readiness verdict itself, which is a judgement on evidence of people and ownership rather than an
AI output. Record the evidence behind each rating so the assessment can be checked.

## Value measures

Baseline the starting position the CoE will be judged against: the number of ideas waiting without a decision, agents
or automations with no owner, and the time a team waits for help today. The CoE lead owns these baselines and passes
them to `ai-centre-of-excellence:coe-kpi-framework`.

## Scale notes

### Starter

A short conversation with the sponsor and the proposed lead, recorded on one page. The usual outcome is an AI working
group, and that is a good result. Core team capacity may be one person beside the lead.

### Scale

Interview the sponsor, the proposed lead, the enablement function, security and a few builders. Expect "launch with
conditions" and track the conditions through the Foundation phase.

### Enterprise

Apply the same criteria to each proposed spoke, with the hub confirming shared standards exist first. A spoke that
fails "before launch" criteria joins the hub's intake rather than launching alone.

## Hand-offs

- To `ai-centre-of-excellence:coe-sponsor-role` when sponsorship is uncertain.
- To `ai-centre-of-excellence:coe-charter` when the verdict allows launch.
- To `ai-centre-of-excellence:coe-team-design` to turn agreed capacity into roles.
- To `ai-centre-of-excellence:coe-launch-roadmap` to carry conditions into the launch plan.

## Reviewer gates

Not applicable, because readiness is a planning judgement and releases no AI solution. The sponsor accepts the verdict
and any conditions; reviewer departments such as `security-privacy` are engaged later through the CoE's intake.

## Failure modes

- Enthusiasm in a workshop is recorded as capacity, and the CoE launches with nobody who has time.
- The central IT team accepts ownership by default, and the business never takes responsibility for outcomes.
- The verdict is softened to "launch" because a date was already announced, and the conditions are never closed.
- Existing unofficial builders are excluded, so the CoE starts without its most capable people.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Record a sponsor, lead or team member as available without their manager's agreement.
- Turn a "not yet" into "launch" to protect an announced date.
- Assess or compare individuals' suitability; assess roles, time and ownership.
- State licensing conclusions; route them to the licensing guide or a licensing partner.
