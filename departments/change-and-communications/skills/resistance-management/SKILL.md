---
name: resistance-management
description: Understands and responds to resistance, fear and scepticism about AI as information about the change - listening at group level, diagnosing causes such as job fear, monitoring worries, quality doubts, ethical objection, workload and change fatigue, separating legitimate risks from misunderstanding, and choosing a fitting response with an owner. Use when a group pushes back, when fear or rumour spreads, or when scepticism stalls adoption.
license: CC-BY-4.0
metadata:
  department: change-and-communications
  lifecycle: Enable, Launch, Measure, Improve
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-responsible-ai, ms-copilot-privacy, ico-ai-data-protection
  status: draft
  authors: Simon Foote
---

# Resistance management

## Purpose

Resistance to AI is rarely irrational. People worry about their jobs, about being watched, about being blamed for an
AI mistake, about professional standards, about ethics, and about finding time to learn yet another thing. Some of those
worries point to real risks the programme has not handled. This skill treats resistance as information: it listens at
group level, diagnoses causes, separates legitimate risks from misunderstandings, and chooses a response that fits the
cause. It usually goes wrong when programmes label people as "resistors", answer every concern with more enthusiasm,
or push harder on adoption when the honest answer was to fix something.

## When to use

- A team, function or professional group is pushing back on an AI change, openly or by quietly not engaging.
- Fear or rumour about AI (job cuts, monitoring, data leaks) is spreading.
- Experienced professionals are sceptical about AI quality and their scepticism is discouraging others.
- Employee representatives or a staff network have raised formal concerns.
- Adoption has stalled in a group despite access, onboarding and support being in place.

## When not to use

- Mapping all stakeholders and their influence before the change - use `change-and-communications:ai-stakeholder-mapping`.
- Assessing how roles and work will change - use `change-and-communications:people-change-impact`.
- Diagnosing low use caused by access, onboarding or support gaps - use `copilot-adoption:adoption-readiness`.
- Formal decisions on whether a specific AI use should be allowed - use `responsible-ai:prohibited-use-review`.
- Building the overall communication strategy - use `change-and-communications:ai-communication-strategy`.

## Questions to ask first

1. Which group is resisting, what exactly are they saying or doing, and since when?
2. What have they been told about the change, by whom, and what did they hear?
3. Is any part of the concern a real risk, gap or unanswered question that the programme should fix?
4. What has already been tried, and how did the group respond?
5. Does the group have a formal voice (employee representatives, professional body) that must be engaged through its own route?

## Required inputs

- The concern register from `change-and-communications:ai-stakeholder-mapping`.
- Group-level impact for the group from `change-and-communications:people-change-impact`.
- Listening data at group level: pulse comments, questions from sessions, manager and change network themes, support themes.
- The agreed answers on jobs, monitoring and data from `change-and-communications:ai-communication-strategy`.
- Any formal representations, handled through HR.

If listening data is thin, gather it before acting: a short facilitated session or a few conversations through managers
and the change network. Do not diagnose a group from one loud voice or from the programme's assumptions.

## Decision framework

Diagnose the cause, then choose the response that fits it. Several causes often apply at once.

| Cause | Signals | Fitting response | Owner |
|---|---|---|---|
| Job fear | Questions about cuts, silence in sessions, rumours | Honest, agreed position from the sponsor and HR; manager conversations; role impact shared | Sponsor, HR |
| Monitoring fear | "Will they read my prompts?", reluctance to try | Clear statement agreed with the DPO on what is and is not seen, backed by configuration | DPO, change lead |
| Quality scepticism | "It gets things wrong", experts disengage | Acknowledge limits, show verification practice, involve sceptics in testing scenarios | Adoption lead, Champions |
| Ethical objection | Concern that a use is unfair or inappropriate | Route to the responsible AI process; do not argue it away | `responsible-ai` department |
| Professional identity | "This devalues my expertise" | Role-specific scenarios where expertise checks and directs AI; peer voices from the profession | Business owner, managers |
| Workload and fatigue | "No time", competing changes | Protected practice time, resequencing, fewer asks | Managers, programme lead |
| Poor early experience | Tried once, failed, gave up | Targeted help on a real task; fix access or guidance problems | Champions, adoption lead |
| Misinformation | Specific false claims circulating | Correct the specific claim quickly through trusted senders | Change lead |

Classify each concern before responding: a legitimate risk to fix, a gap to close (time, guidance, access), an
unanswered question to answer, or a misunderstanding to correct. Legitimate risks are fixed first, not communicated
around.

## Practitioner approach

Start by listening, not persuading. Arrange a session with the group, facilitated by someone they trust, and ask what
worries them about the change, what would need to be true for them to be comfortable, and what they have heard. Record
themes, not names. Make it clear that raising concerns is welcome and has no consequences.

Diagnose before responding. Use the cause table and look for the root. A team that says "it gets things wrong" may have
been given an unsuitable scenario, may have a genuine quality issue with an agent's knowledge, or may be voicing a
deeper fear about their role. Check impact ratings, support themes and what their managers have said. Test the
diagnosis with the group's manager and change agent.

Take legitimate concerns seriously and visibly. When resistance reveals a real problem - an overshared site, a scenario
that does not work, an agent drawing on stale content, a use that troubles people ethically - fix it or route it to the
owner, and tell the group what changed because they spoke up. Nothing reduces resistance faster than seeing concerns
acted on. Ethical objections go to the responsible AI process; they are not a communications problem.

Answer fears with agreed facts. On jobs, the sponsor and HR must give the honest position, including what has not been
decided. On monitoring, the DPO must confirm what usage information exists, who sees it and for what purpose, and the
statement must match the configuration. Vague reassurance makes fear worse.

Use credible voices. Sceptical professionals listen to peers in their profession, not to programme enthusiasm. Involve
sceptics in testing scenarios; they are often the best at finding the limits, and when they find a valuable use their
endorsement carries weight. Never use them as targets for persuasion.

Respect choice where it exists. Where policy allows people to choose whether to use an AI experience for a task, say so
plainly. Pressure to adopt in those cases produces the shallow, unverified use the programme least wants.

Track themes over time at group level. Resistance that persists after the root cause is fixed often signals another
cause, such as fatigue or a manager who is not on board. Feed what you learn into the communications strategy, manager
enablement and the impact assessment, and report themes to the sponsor in the monthly change update.

## Outputs

- A resistance diagnosis by group: concerns in the group's words, classified causes, evidence and the agreed response with owner and date.
- A "you said, we did" summary for each group showing concerns acted on.
- Referrals to owners for legitimate risks: security, data protection, responsible AI, knowledge owners, HR.
- Updated concern answers for the questions-and-answers section of the `ai-communications-plan`.

## Microsoft platform considerations

Many fears concern what Microsoft AI experiences can access, store or reveal. Answer them from the organisation's
configuration and the current source records in `references/sources.md`, especially the privacy records, and involve
the security lead when a concern reveals a real permissions or oversharing issue.

## Adoption considerations

Resistance is often the first sign that onboarding, scenarios or support do not fit a group. Share diagnoses with the
adoption lead so the group's journey can be adjusted rather than repeated louder.

## Knowledge considerations

Quality scepticism frequently traces to poor knowledge: outdated pages, conflicting documents or content an agent should
not use. Pass these findings to `knowledge-management:knowledge-gap-analysis` and tell the group what was fixed.

## Security and privacy considerations

Listening data is collected and reported by theme and group, above the minimum group size, with no attribution to
individuals. Concerns that reveal a possible data exposure follow the security route immediately. Questions about
employee monitoring and data end with the DPO and HR.

## Responsible AI considerations

Ethical objections and concerns about fairness are routed to the `responsible-ai` department and may stop or change a
use. Never treat a principled objection as a barrier to be overcome by communications.

## Evaluation requirements

Not applicable as solution evaluation. The response is checked by whether the group's concern themes change after the
action, through a follow-up conversation or pulse at group level.

## Value measures

Owned by the change lead: concerns with an agreed response, time from concern raised to response, share of legitimate
risks fixed, and group-level pulse items on confidence and willingness to raise concerns, against the first listening
baseline. Never reported for individuals.

## Scale notes

### Starter

A facilitated conversation with each concerned group, a short concern log and a "you said, we did" note, led by the
adoption lead and HR.

### Scale

A standing concern log fed by the change network and managers, monthly theme review, and agreed answers maintained
centrally.

### Enterprise

Common cause categories across divisions, formal engagement with employee representative bodies through HR, and theme
reporting to the enterprise sponsor forum.

## Hand-offs

- To `change-and-communications:ai-communication-strategy` to update answers and messages.
- To `change-and-communications:manager-enablement` when managers need support to handle concerns.
- To `responsible-ai:ai-impact-assessment` for concerns about how a solution affects people.
- To `copilot-adoption:role-based-adoption` when a group's journey needs redesign.

## Reviewer gates

Not applicable as a formal gate, because resistance management does not release a solution. Concerns that point to
risk in a solution at tier 2 or above are passed to its `responsible-ai` and `security-privacy` reviewers.

## Failure modes

- People who raise concerns are labelled resistors, and others stop speaking up.
- Legitimate risks are treated as communication problems and remain unfixed.
- Vague reassurance on jobs or monitoring increases fear rather than reducing it.
- More pressure is applied to a fatigued group, producing token use and resentment.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Label, list or report named individuals as resistant.
- Penalise anyone, formally or informally, for raising a concern about AI.
- Argue away an ethical objection instead of routing it to the responsible AI process.
- Offer reassurance on jobs, monitoring or data that has not been agreed and is not true.
