---
name: stakeholder-governance
description: Governs how stakeholders take part in an AI programme's decisions - decision rights by decision type, who must be consulted or must approve (security, data protection, legal, HR, employee representatives, business units), escalation routes and time limits, and an engagement plan for governance stakeholders. Use when nobody knows who can approve a change, when decisions stall between functions, or when a required voice was left out.
license: CC-BY-4.0
metadata:
  department: programme-management
  lifecycle: Mobilise, Deliver, Assure, Launch
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: nist-ai-rmf, iso-iec-42001, ico-ai-data-protection
  status: draft
  authors: Simon Foote
---

# Stakeholder governance

## Purpose

AI programmes cross functional lines that rarely meet in other programmes: IT, security, data protection, legal, HR,
employee representatives, records management, procurement and every business unit that owns knowledge or outcomes. This
skill sets who holds which decision rights in the programme, who must be consulted or must approve before a decision is
valid, how disagreements escalate and how quickly, and how governance stakeholders are kept engaged. It goes wrong when
decision rights are implied, when a function with a legitimate veto finds out late, and when escalation has no time limit
so decisions stall indefinitely.

## When to use

- A programme is mobilising and needs explicit decision rights before its first contested decision.
- A decision has stalled between functions, for example IT and a business unit, or the DPO and the build team.
- A required voice (employee representatives, HR, legal, records management) was left out of a decision and it is being reopened.
- The programme's scope widens to a new business unit, country or solution type that brings new stakeholders.
- The sponsor asks who can actually approve a change to scope, a supplier or a release.

## When not to use

- Mapping stakeholders' interests, influence and concerns about AI for change and communications - use `change-and-communications:ai-stakeholder-mapping`.
- Securing and equipping the executive sponsor - use `ai-strategy:executive-sponsorship`.
- Activity-level responsibilities in the AI CoE - use `ai-centre-of-excellence:coe-raci`.
- Setting meeting frequencies, agendas and the decision log - use `programme-management:programme-board-cadence`.
- Assigning accountable roles to departments and pack artefacts - use `organisation-tailoring:ownership-map`.

## Questions to ask first

1. What kinds of decision will the programme take (scope, funding, supplier, release, policy, people impact), and which of them does the charter already assign?
2. Which functions hold a legitimate right to approve or block some of those decisions, by law, policy or agreement?
3. Are there employee representatives, works councils or trade unions whose consultation is required or expected for changes to how people work or are monitored?
4. Where have decisions stalled or been reopened in this or earlier programmes, and why?
5. How quickly must an escalated decision be taken before it harms the plan?

## Required inputs

- The programme charter with the sponsor's reserved decisions and the board's tolerances.
- The forum map from `programme-management:programme-board-cadence`, where it exists.
- The organisation's existing policies on approvals (security, data protection, procurement, HR consultation).
- Declared roles from `organisation-tailoring:ownership-map`.

Whether consultation with employee representatives is legally required is a question for HR and the legal adviser; record
their answer, and mark it `[To confirm: ...]` until they give it. Never decide it within the programme.

## Decision framework

Build a decision rights matrix by decision type. Use four roles per decision: who decides, who must approve (a veto),
who must be consulted before, and who is informed after.

| Decision type | Typically decides | Typically must approve | Typically consulted |
|---|---|---|---|
| Scope or outcome change | Sponsor | None beyond the sponsor | Business owners, programme board |
| Change within tolerance | Programme board | None | Affected workstream leads |
| Supplier selection or change | Programme board within delegation | Procurement | Security, data protection where data is shared |
| Solution release at tier 2 and above | Business owner | Reviewer gates (blocking findings) | Support, adoption lead |
| Policy (acceptable use, monitoring, retention) | Policy owner | Legal, DPO, HR as relevant | Employee representatives where required |
| Change to how people work or are measured | Business owner and HR | HR | Employee representatives, line managers |
| Residual risk acceptance at tier 3 and 4 | Accountable executive | None | Reviewers, DPO, legal |

Set escalation routes with time limits: a decision unresolved at its forum by the agreed date moves up one level, and
the sponsor resolves anything that reaches them. A veto from a reviewer or a statutory role is not overruled by
escalation; it is resolved by changing the proposal or by written risk acceptance where policy allows it.

## Practitioner approach

List the decisions before the people. Walk the charter, the integrated plan and the risk log and write down the decisions
the programme will need to take over the next two stages. Group them into types. People argue less about a matrix built
from real decisions than one built from organisation charts.

For each decision type, identify the functions with a legitimate stake. Distinguish carefully between a veto and a voice.
Security and privacy reviewers, the DPO and legal hold real approval rights over specific matters; employee representatives
may have consultation rights that are formal in some jurisdictions and informal in others; business units hold the right
to decide about their own knowledge and outcomes. Give each its correct role. Over-assigning vetoes slows everything,
under-assigning them produces decisions that are reopened later.

Agree the matrix with the people named in it, not just with the sponsor. Each function should confirm the decisions it
expects to approve and how quickly it can do so. Where a function cannot meet the programme's pace, solve it with
pre-agreed standards (for example, an approved pattern that needs no further approval below tier 2) rather than by
skipping them.

Set escalation with time limits. Most stalls happen because nobody owns the next step when two functions disagree. Write
down who decides when the workstream cannot, and by when, up to the sponsor. Make clear that escalation resolves
priorities and trade-offs, not reviewer findings: a blocking security or responsible AI finding is resolved by changing
the design or by written risk acceptance from the accountable executive.

Plan engagement with governance stakeholders as a rhythm rather than a series of surprises. Brief the DPO, security,
HR and employee representatives before each stage, not after decisions are taken, and give them the information they need
in a form they can act on. Where people are affected, engage employee representatives early about what AI will and will
not be used for, including the commitment that adoption data is reported at team or role level and never used to monitor
individuals.

Review the matrix at each stage gate and whenever scope widens to a new unit, country or solution type.

## Outputs

- A decision rights matrix by decision type: decides, must approve, must be consulted, informed, and time limit.
- An escalation route with time limits from workstream to sponsor, recorded in the governance section of the `programme-charter` template.
- A governance stakeholder engagement plan: stakeholder by role, interest in the programme, decisions they hold, engagement rhythm and owner.
- A record of agreement to the matrix by each function named in it.

## Microsoft platform considerations

Not applicable in depth, because decision rights are organisational; platform administration roles (tenant, Power
Platform, Copilot Studio, security and compliance tooling) should appear as stakeholders for decisions that change
platform configuration.

## Adoption considerations

Line managers and business owners need a voice in decisions that change how teams work. Including them early is one of
the most effective ways to reduce later resistance.

## Knowledge considerations

Knowledge owners decide what content an agent may ground on and when it is ready. Record that right in the matrix so
build teams do not decide it for them.

## Security and privacy considerations

Record the `security-privacy` gate as an approval right from risk tier 2, and the DPO's role in decisions involving
personal data. Data protection questions route to the DPO or legal adviser; the programme does not answer them.

## Responsible AI considerations

Decisions that change how people are assessed, monitored or affected by AI need HR, the accountable executive and,
where required, employee representatives. Record that AI-derived data is never used to rank or monitor individuals as a
standing constraint.

## Evaluation requirements

Not applicable, because the matrix governs decisions rather than an AI solution; it should name `evaluation-quality` as
an approval right on release evidence from tier 2.

## Value measures

Track decision latency by decision type, the number of decisions reopened, and the share of escalations resolved within
their time limit, reported at programme level by the AI Programme Manager.

## Scale notes

### Starter

A one-page matrix covering five or six decision types, with the sponsor as the escalation end point and the DPO and IT
lead named for their approvals.

### Scale

A full matrix agreed with each function, escalation with time limits, and a governance stakeholder rhythm aligned to stage
gates.

### Enterprise

A matrix at programme level and per business unit or country, reflecting local consultation requirements confirmed by HR
and legal, with escalation to a portfolio or executive board.

## Hand-offs

- To `programme-management:programme-board-cadence` to place each decision type in a forum.
- To `change-and-communications:ai-stakeholder-mapping` for the wider change and communications view of stakeholders.
- To `ai-strategy:executive-sponsorship` where the sponsor's own role needs strengthening.
- To `responsible-ai:ai-risk-acceptance` for decisions on residual solution risk.

## Reviewer gates

Not applicable, because the matrix releases no solution; it must record that blocking findings from `security-privacy`,
`responsible-ai`, `evaluation-quality` and `design-authority` cannot be overruled by escalation.

## Failure modes

- Decision rights are implied, and the first contested decision becomes a turf dispute.
- Employee representatives or HR learn about a change late and the decision is reopened or paused.
- Escalation has no time limit, and decisions wait for months.
- Every function is given a veto, and the programme slows to the pace of the slowest approver.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Decide within the programme whether legal or employee consultation is required; route it to HR and the legal adviser.
- Allow escalation to overrule a blocking reviewer finding.
- Use the stakeholder plan to rate or rank individuals.
- Leave an escalation route without a time limit and an end point.
