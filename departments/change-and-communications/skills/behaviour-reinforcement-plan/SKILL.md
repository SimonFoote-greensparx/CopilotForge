---
name: behaviour-reinforcement-plan
description: Plans how new AI-enabled ways of working are embedded so they stick - naming target behaviours, then building them into processes, templates, team routines, role expectations, onboarding and leadership routines, removing old-way pull-backs and handing ownership to the business. Use when adoption gains fade after launch or a campaign, when new practice depends on enthusiasts, or before a programme hands over to business as usual.
license: CC-BY-4.0
metadata:
  department: change-and-communications
  lifecycle: Launch, Measure, Scale, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-cowork, copilot-studio, power-platform
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-champion-best-practice, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# Behaviour reinforcement plan

## Purpose

New ways of working last when the organisation's systems expect them: the process, the template, the meeting, the
onboarding, the way leaders ask questions and what gets recognised. This skill plans that embedding for AI-enabled
behaviours, so practice no longer depends on reminders, enthusiasts or a programme team. It names the behaviours that
should persist, finds what currently pulls people back to old habits, and changes the surrounding system with owners in
the business. Reinforcement plans usually go wrong by relying on more communications, by quietly writing usage targets
into performance objectives, or by ending when the programme closes so that practice drifts back.

## When to use

- Adoption rose during launch or a campaign and is now fading back towards the old way of working.
- New practice depends on a few enthusiasts and would collapse if they moved on.
- An AI-enabled process change (for example AI-drafted first versions with human review) needs to become the standard.
- The programme is preparing to hand over to business as usual and must leave the change embedded.
- Old templates, approvals or tools still assume the pre-AI way of working and push people back to it.

## When not to use

- Running the always-on nudge and refresher calendar for Copilot after launch - use `copilot-adoption:adoption-reinforcement`.
- Planning a time-boxed campaign around a scenario theme - use `change-and-communications:adoption-campaign-plan`.
- Recognising and progressing Champions - use `champions:recognition-and-progression`.
- Redesigning an end-to-end process before automating it - use `automation:automation-process-design`.
- Measuring whether adoption leads to benefits - use `value-realisation:adoption-to-value-metrics`.

## Questions to ask first

1. Which specific behaviours should still be normal a year from now, for which role groups, and why do they matter?
2. What pulls people back to the old way - templates, approvals, tools, deadlines, habits, a manager's preference?
3. Which processes, routines and artefacts could carry the new behaviour, and who owns each?
4. Who in the business will own each behaviour after the programme moves on?
5. What team-level signal will show whether a behaviour has held?

## Required inputs

- The target behaviours, drawn from scenarios, role journeys and campaign reviews in `copilot-adoption:role-based-adoption` and `change-and-communications:adoption-campaign-plan`.
- Group-level impact from `change-and-communications:people-change-impact`.
- Team-level adoption and behaviour signals from `copilot-adoption:adoption-measurement`.
- The owners of the relevant processes, templates, onboarding and leadership routines.
- HR's position on any change to role descriptions, objectives or recognition schemes.

If target behaviours have not been named precisely, name them before planning reinforcement; "use Copilot more" cannot
be embedded. If HR has not agreed how role expectations may change, leave role-level mechanisms out of the plan until
it has.

## Decision framework

For each target behaviour, choose mechanisms from the reinforcement levers, favouring the structural ones that work
without anyone remembering.

| Lever | Example for an AI-enabled behaviour | Strength | Owner |
|---|---|---|---|
| Process and workflow | Review step for AI-drafted responses built into the case process | Structural | Process owner |
| Templates and artefacts | Report template starts from a Copilot summary with a verification checklist | Structural | Template owner |
| Remove friction | Retire the old manual tracker that duplicated the agent | Structural | Business owner |
| Team routines | Weekly meeting includes a short "what AI helped with" item | Social | Manager |
| Onboarding | New joiners learn the AI-enabled way as the standard way | Structural | HR or onboarding owner |
| Role expectations | Role guidance describes verified, responsible use, never usage volume | Formal | HR with business owner |
| Leadership routines | Leaders ask how a piece of work was checked, not whether AI was used | Social | Leadership team |
| Recognition | Teams thanked for improving a shared practice or template | Social | Managers, sponsor |
| Reminders | Nudges and refreshers | Light | Adoption lead |

Aim for at least one structural lever per target behaviour. A plan made only of reminders and recognition is a
communications plan, and will fade when they stop.

Set checkpoints after launch at roughly one, three and six months, and decide at each whether the behaviour is holding,
needs another lever, or should be dropped because it is not worth sustaining.

## Practitioner approach

Name the behaviours precisely. Work with business owners and managers to write each as an observable practice:
"Contract managers start the monthly site report from a Copilot summary of the site channel and check every figure
against the source system." Limit the plan to the few behaviours that matter most; reinforcing everything reinforces
nothing.

Find the pull-backs. For each behaviour, ask the people who do the work what makes the old way easier: a template that
assumes manual drafting, an approval that requires an old format, a tool that still holds the master data, a deadline
that leaves no time for the new step, a manager who prefers the old output. These pull-backs explain most fading, and
removing them often does more than any new reinforcement.

Choose levers and owners. Use the lever table, starting with process, templates, friction removal and onboarding.
Agree each change with the owner of that process or artefact; the programme can propose but rarely owns these. Add
social levers - team routines and leadership questions - through `change-and-communications:manager-enablement` and the
sponsor.

Handle role expectations with care. If role guidance or objectives are to reflect AI-enabled work, HR owns the change,
consultation may be required, and wording must describe verified, responsible practice and outcomes, never volume of AI
use. Usage counts in performance objectives push people towards shallow, unchecked use and damage trust.

Make the new way the default for newcomers. New joiners and people changing role should learn the AI-enabled practice
as simply "how we do it here", through onboarding owned by the business, linked to `copilot-adoption:copilot-onboarding`.

Plan the hand-over. For each behaviour, name a business owner who will keep it alive after the programme, with the
signal they will watch and a review point in their existing routines. A behaviour without a business owner is a
behaviour the programme is still carrying.

Check and adjust. At each checkpoint, read team-level signals and talk to managers and change agents. Where a behaviour
is holding, reduce reminders. Where it is fading, look for a pull-back that was missed before adding more messaging.
Where it is not delivering value, drop it openly and say why.

## Outputs

- A behaviour reinforcement plan: target behaviours, role groups, pull-backs, levers with owners and dates, business owner, signal, checkpoints and decisions.
- A list of process, template and onboarding changes agreed with their owners.
- A hand-over note to business owners for each behaviour.
- Checkpoint notes to the sponsor showing which behaviours are holding, adjusted or dropped.

## Microsoft platform considerations

Structural levers often involve Microsoft 365 artefacts: templates, Teams channels and meeting routines, SharePoint
pages, an agent placed where work happens, or a Power Automate step that routes AI-drafted work to review. Confirm
current capability against `references/sources.md`, and send any new build through the normal intake and governance
route rather than the reinforcement plan.

## Adoption considerations

This plan takes over where launch, campaigns and reinforcement nudges leave off. Coordinate with
`copilot-adoption:adoption-reinforcement` so nudges support the same behaviours, and reduce them as structural levers
take hold.

## Knowledge considerations

Behaviours that depend on shared content (a library, an agent's sources, a template set) only hold while that content
is current. Name the knowledge owner for each and include its upkeep in the hand-over.

## Security and privacy considerations

Templates and process changes must keep the approved-use rules visible, especially on confidential and personal data.
Signals are read at team or role level above the minimum group size. Questions about employee data end with the DPO.

## Responsible AI considerations

Reinforce verification and accountability, not volume. Where a process now relies on AI-drafted work that affects
people, confirm the human review step is designed through `responsible-ai:human-oversight` rather than assumed.

## Evaluation requirements

Not applicable as solution evaluation. Each behaviour is checked at its checkpoints against its team-level signal and
manager feedback, and the plan records why levers were kept, added or removed.

## Value measures

Owned by the business owner for each behaviour, with the end-of-launch position as baseline: behaviour still present
at three and six months at team level, pull-backs removed, and the work measure the behaviour was meant to move. Never
individual usage or performance.

## Scale notes

### Starter

Three to five behaviours, one structural lever each, owners named in a short table and a review at three months.

### Scale

Plans by function, with process and template owners engaged, managers carrying team routines, and checkpoints built
into business reviews.

### Enterprise

A common behaviour library with local plans, onboarding and role guidance changes coordinated with HR across divisions,
and sustainment reviewed by the CoE.

## Hand-offs

- To `copilot-adoption:copilot-onboarding` so new joiners learn the AI-enabled way by default.
- To `change-and-communications:manager-enablement` for team routines and leadership questions.
- To `value-realisation:benefit-owner` where a behaviour underpins a tracked benefit.
- To `automation:automation-process-design` where embedding needs a process redesign.

## Reviewer gates

Not applicable as a formal gate, because reinforcement embeds approved practice. Any new agent or automation proposed as
a lever passes its own release gates through normal intake.

## Failure modes

- The plan is all reminders and recognition, and behaviour fades when the reminders stop.
- Usage targets enter performance objectives, and people use AI to hit numbers rather than to do better work.
- Old templates and approvals stay in place and quietly pull people back.
- No business owner takes over, and the behaviour lapses when the programme closes.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Put AI usage volume into anyone's objectives or performance assessment.
- Change role descriptions or objectives without HR ownership and any required consultation.
- Rely on reminders alone to sustain a behaviour.
- Hand over a behaviour without a named business owner and a signal to watch.
