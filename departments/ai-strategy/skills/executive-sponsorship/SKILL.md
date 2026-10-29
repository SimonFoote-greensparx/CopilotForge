---
name: executive-sponsorship
description: Secures and equips an active executive sponsor for the whole AI programme - choosing the right executive, agreeing time, decision rights and visible behaviours in a sponsor agreement, building a peer sponsor coalition and checking sponsor engagement each quarter. Use when an AI programme has no sponsor or only a nominal one, when the sponsor has gone quiet, or when the sponsor changes role.
license: CC-BY-4.0
metadata:
  department: ai-strategy
  lifecycle: Envision, Mobilise, Scale
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-copilot-studio-guidance
  status: draft
  authors: Simon Foote
---

# Executive sponsorship

## Purpose

This skill makes sure the AI programme has an executive who owns it in practice, not just on the org chart. It
selects the sponsor against what the programme will need from them, agrees their time, decisions and visible
behaviours in writing, builds a small coalition of peer executives so sponsorship does not rest on one person, and
checks quarterly that the sponsor is still doing the job. Sponsorship usually fails quietly: the most senior available
name is chosen, they open the launch event, and the programme loses its authority the first time two functions
disagree.

## When to use

- An AI programme, strategy or transformation is being set up and no executive has been asked to own it.
- A sponsor exists in name but has missed steering meetings, delegated every decision or stopped speaking about AI.
- The programme keeps escalating cross-functional conflicts that nobody senior resolves.
- The sponsor is leaving, changing role or losing interest, and succession is needed.
- Several executives each claim the AI agenda and the programme receives conflicting direction.

## When not to use

- Defining the sponsor role inside the CoE's own structure and forums - use `ai-centre-of-excellence:coe-sponsor-role`.
- Helping executives use Copilot personally and role-model it - use `copilot-adoption:executive-enablement`.
- Mapping all stakeholders and their concerns about AI - use `change-and-communications:ai-stakeholder-mapping`.
- Setting decision rights and escalation across the programme's wider stakeholders - use `programme-management:stakeholder-governance`.
- Agreeing the outcomes the sponsor will be accountable for - use `ai-strategy:strategic-outcomes`.

## Questions to ask first

1. What will the programme need from its sponsor in the next twelve months: funding decisions, cross-functional authority, risk acceptance, public advocacy or all of these?
2. Which executive owns the business results the AI outcomes are meant to move, and do they have authority across the functions involved?
3. How much time can the candidate genuinely commit each month, and what would they stop doing to make room?
4. Which other executives must actively support the programme for it to succeed, and what does each need from it?
5. What happens today when the programme needs a decision nobody below executive level can make?

## Required inputs

- The AI vision and strategic outcomes from `ai-strategy:ai-vision` and `ai-strategy:strategic-outcomes`, or drafts.
- The operating model from `ai-strategy:ai-operating-model`, showing where decisions sit.
- A list of decisions the programme expects to escalate in the coming year (funding, policy, risk, cross-functional priorities).
- The current governance calendar, so sponsor time can be placed in real forums.

If no outcomes exist yet, sponsorship can still be secured, but record that the sponsor's accountability is
provisional until outcomes are agreed. Never record a time commitment the sponsor has not personally confirmed.

## Decision framework

Assess each candidate against what the programme needs. A strong sponsor meets the first three; the others decide
whether a coalition is required to compensate.

| Criterion | Strong | Weak |
|---|---|---|
| Owns the results | Accountable for at least one strategic outcome AI must move | Owns no affected business result (often a pure technology role) |
| Cross-functional authority | Can settle priority conflicts between the functions involved | Can direct only their own function |
| Time | Confirms a specific monthly commitment and protects it | "Whatever is needed", with no diary time |
| Risk appetite | Will accept residual risk in writing within the governance model | Expects others to carry risk decisions |
| Visible use | Willing to use AI personally and talk about it openly | Supportive in private, silent in public |
| Continuity | Likely to stay in role for the programme horizon | Known to be moving within months |

Where no single candidate meets the first three criteria, appoint the strongest as lead sponsor and add one or two
peer co-sponsors whose authority fills the gap. Never split accountability equally; one person remains accountable.

## Practitioner approach

Begin with the decisions, not the person. List what the programme will need decided over the next year: funding
tranches, which functions go first, acceptable-use exceptions, risk acceptance for higher-tier solutions, and conflicts
over scarce owners and reviewers. That list defines the sponsor job and makes the conversation with candidates concrete.

Prefer a business executive who owns the results over the most senior technology leader. Technology leaders are
essential partners, but when the sponsor owns none of the outcomes, the programme drifts toward deployment metrics and
business units treat AI as something done to them. Where the chief executive wants to sponsor, accept gladly but agree
a delegate for routine steering so that the sponsor's attention is reserved for the decisions only they can make.

Hold a direct conversation with the preferred candidate. Show them the decision list, the outcomes and what weak
sponsorship has cost similar programmes in terms of stalled pilots and unowned agents. Ask for a specific commitment:
chairing the monthly or quarterly steering, a short regular slot with the programme lead, two or three visible moments
a quarter, and named decisions reserved to them. Write it down in a one-page sponsor agreement and let them edit it.

Build the coalition next. Identify the two to four executives whose functions are most affected or whose support is
essential (often operations, HR, finance and the data protection lead). Agree what each will do: sponsor a business-unit
outcome, release owners and Champions, or speak at their own forums. A coalition protects the programme when the lead
sponsor is unavailable and reduces the perception that AI belongs to one function.

Equip the sponsor. Give them a short briefing pack: the vision, outcomes, principles and a few honest talking points on
jobs, risk and value. Arrange hands-on time with the tools through `copilot-adoption:executive-enablement`, because a
sponsor who has not used AI cannot speak credibly about it. Prepare them for the questions staff actually ask.

Then check engagement every quarter using observable signals: attendance and decisions at steering, time to resolve
escalations, visible moments delivered, and whether the coalition still holds. Discuss the results with the sponsor
openly. When signals decline, renegotiate the commitment or begin succession early; a sponsor change handled in the
open costs far less than one discovered after months of drift.

## Outputs

- A sponsor agreement: accountable sponsor, outcomes owned, decisions reserved, monthly time committed, forums chaired, visible commitments, delegate and review date.
- A sponsor coalition map: peer executives, what each commits and what each needs from the programme.
- A sponsor briefing pack with talking points aligned to the vision and principles.
- A quarterly sponsorship health note with observable signals and agreed actions.

## Microsoft platform considerations

Not applicable to sponsorship itself, which must hold whatever platform the organisation uses. Where the sponsor's
briefing refers to Microsoft products, check current naming and capability against the source records in
`references/sources.md`, and route any licensing question to the Microsoft licensing guide or a licensing partner.

## Adoption considerations

Staff take their cue from what senior leaders do, not what they sign. Plan the sponsor's visible moments with
`change-and-communications:ai-communication-strategy`, and make at least one of them a candid conversation about how
the sponsor uses AI and where they choose not to.

## Knowledge considerations

Not applicable in detail. Where outcomes depend on knowledge owned across functions, the sponsor's authority is often
needed to secure knowledge owners; record that as a reserved decision.

## Security and privacy considerations

The sponsor may be asked to accept residual risk on higher-tier solutions. Make sure the sponsor agreement states that
risk acceptance follows the governance model, is recorded in writing, and is informed by the security lead and data
protection officer rather than decided alone.

## Responsible AI considerations

The sponsor is usually the accountable executive for responsible AI escalations. Confirm they understand that role and
the route through `responsible-ai:ai-risk-acceptance`, and that blocking findings from reviewers are not traded off
against delivery dates.

## Evaluation requirements

Not applicable to solution testing. Sponsorship is evaluated through the quarterly health signals, which describe
behaviours against the agreement, not the sponsor's personal performance.

## Value measures

Measure sponsorship through programme-level signals: time from escalation to decision, steering meetings with quorum
and decisions made, and coalition commitments delivered. The programme lead owns the measures and reports them to the
sponsor. Never present them as a rating of the sponsor as an individual.

## Scale notes

### Starter

The sponsor is usually the chief executive or a director, the agreement is half a page, and engagement is checked in a
short quarterly conversation. A coalition may be unnecessary.

### Scale

A business executive leads with two or three peer co-sponsors. The agreement is reviewed at each quarterly strategy
review, and the briefing pack is refreshed with each roadmap horizon.

### Enterprise

An executive board member sponsors the enterprise programme, and each business unit has its own sponsor with an
agreement that mirrors the enterprise one. The enterprise sponsor chairs a sponsor forum across units to resolve
cross-unit conflicts.

## Hand-offs

- To `ai-centre-of-excellence:coe-sponsor-role` to place the sponsor in the CoE's forums and decision rights.
- To `copilot-adoption:executive-enablement` to give the sponsor and coalition hands-on confidence with the tools.
- To `programme-management:stakeholder-governance` to align sponsor decisions with the programme's escalation routes.
- To `ai-strategy:investment-case` when the sponsor must champion the funding request.

## Reviewer gates

Not applicable. Sponsorship is an executive arrangement, not a release. Reviewer departments rely on the sponsor as the
accountable executive for risk acceptance, which the agreement records.

## Failure modes

- The most senior technology leader is chosen by default, owns none of the outcomes, and business units disengage.
- The sponsor agrees in principle but no time is diarised, and steering decisions slide month after month.
- Sponsorship rests on one person, who moves role, and the programme loses authority overnight.
- The sponsor speaks about AI but never uses it, and staff notice the gap.
- Declining engagement is noticed but never raised, because nobody below the sponsor feels able to say it.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Accept a sponsor who has not personally confirmed a specific time commitment and the decisions reserved to them.
- Split accountability equally between co-sponsors so that nobody is finally accountable.
- Present sponsorship health signals as a performance rating of an individual executive.
- Let the sponsor accept residual AI risk verbally or outside the governance model.
