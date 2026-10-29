---
name: coe-charter
description: Drafts the charter for an AI Centre of Excellence - purpose, scope across the six pillars, principles, sponsorship, decision rights and what the CoE is not - or the lighter terms of an AI working group for a small organisation. Use when management asks for an AI CoE, when an existing group has drifted into a reporting forum or request queue, or when a sponsor needs one page to agree before people are appointed.
license: CC-BY-4.0
metadata:
  department: ai-centre-of-excellence
  lifecycle: Mobilise, Scale
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, ms-coe-starter-kit, ms-copilot-studio-guidance, nist-ai-rmf
  status: draft
  authors: Simon Foote
---

# CoE charter

## Purpose

A charter turns "management wants an AI Centre of Excellence" into an agreed mandate: why the CoE exists, which
outcomes it serves, what it decides, what it leaves to the business and what it will not become. It is the document
everything else in the CoE hangs from, so it must be short enough for a sponsor to sign and specific enough to settle
arguments later. Charters usually go wrong in one of two ways: they describe a technology team that IT owns, or they
describe a committee that meets monthly, receives reports and changes nothing.

## When to use

- Leadership has asked for an AI Centre of Excellence and nobody has yet written down what it is for.
- An AI working group exists but its purpose, membership or authority is unclear.
- A CoE has drifted into a monthly reporting group, an IT project or a queue of build requests and needs resetting.
- A small organisation needs the lighter terms of reference for an AI working group instead of a full CoE.
- The organisation is moving edition (for example from working group to a core CoE team) and the mandate must change with it.

## When not to use

- Designing the CoE team, the hub-and-spoke shape and the intake-to-delivery flow - use `ai-centre-of-excellence:coe-operating-model`.
- Assigning who is responsible and accountable for each activity - use `ai-centre-of-excellence:coe-raci`.
- Setting the meetings, agendas and terms of reference for each forum - use `ai-centre-of-excellence:coe-cadence`.
- Writing the governance framework, risk tiers and acceptable-use starter - use `ai-centre-of-excellence:coe-governance-model`.
- The organisation-wide target operating model for AI, of which the CoE is one part - use `ai-strategy:ai-operating-model`.
- Agreeing the strategic outcomes the CoE serves - use `ai-strategy:strategic-outcomes`.

## Questions to ask first

1. Which two or three business outcomes should the CoE move in the next twelve months, and who owns each of them?
2. Who is the executive sponsor, and what will they personally do: chair, unblock, accept risk, fund?
3. Which of the six pillars are in scope now, and which are deliberately deferred?
4. What may the CoE decide on its own, what does it recommend, and what stays with business owners or existing boards?
5. How many people, and how much of their time, can realistically be given to the CoE, and from which parts of the business?
6. What already exists that the CoE must work with rather than duplicate (an architecture board, a data protection function, a Power Platform CoE, a change team)?

## Required inputs

- The strategic outcomes or AI ambition, from `ai-strategy:strategic-outcomes`, or at least the sponsor's stated goals.
- The recommended edition and archetype from `organisation-tailoring:edition-and-archetype`, which sets the charter's weight.
- The executive sponsor (as a role) and the business functions that will contribute members.
- A list of existing governance forums and policies the CoE must connect to.

If outcomes are missing, write the charter with outcome entries marked `[To confirm]` and make agreeing them the first
decision of the first steering meeting. Never invent a sponsor, a budget or a mandate the organisation has not given.

## Decision framework

Set the charter's form by edition, then check each clause against the principles.

| Edition | Form | Sponsor role | Decision rights |
|---|---|---|---|
| Starter | AI working group of three to five people, one page of terms | Attends quarterly, approves the acceptable-use starter | Recommends; the sponsor decides |
| Scale | Core CoE team with business representatives, two-page charter | Chairs the monthly steering group | Decides intake, risk tier and release up to tier 2; recommends above |
| Enterprise | Hub with business-unit spokes, charter plus spoke mandates | Executive board sponsor, delegates to a CoE board | Hub sets standards; spokes decide within them; board accepts tier 4 risk |

Test every clause against the five principles. If a clause fails one, rewrite it.

| Principle | Test |
|---|---|
| Business-owned | Does a business role own the priority, the knowledge and the benefit, not IT? |
| AI-enabled | Does the CoE enable and assure rather than build everything itself? |
| Outcome-focused | Is the clause tied to an outcome, not an activity count? |
| Govern once | Is the control defined once and reused, not re-argued per request? |
| Repeat everywhere | Can a second business unit adopt it unchanged? |

## Practitioner approach

Begin with the sponsor, not the membership. A CoE without an executive who will chair, unblock and accept risk becomes
an enthusiasts' club, so confirm sponsorship before drafting anything else. Ask the sponsor to state, in their own
words, what would be different in a year if the CoE worked. Translate that into two or three outcomes with business
owners; these head the charter and every later section must serve them.

Write the purpose as one sentence that a department head would recognise, such as "help every department use AI safely
to improve the outcomes they already own". Then set scope using the six pillars: opportunity management, knowledge
management, agent development, automation, adoption and change, and governance. Be explicit about which pillars are
active now and which are deferred. A CoE that claims all six on day one with two part-time people will deliver none of
them. For most organisations at the adopter stage, adoption and change, opportunity management and governance come
first, with agent development following once intake and ownership exist.

State the principles - business-owned, AI-enabled, outcome-focused, govern once, repeat everywhere - and give each one
a consequence in this organisation. "Business-owned" should say that every opportunity has a named business owner
before it enters delivery and that benefits are reported by the business, not the CoE.

Decision rights are where charters earn their keep. List the decisions the CoE takes (approved tools list, intake
criteria, risk classification, release up to an agreed tier), the decisions it recommends (investment, tier 3 and 4
releases) and those it never takes (business priorities within a department, HR matters, procurement outside its
remit). Connect to existing forums by role or board name, so the charter adds a route rather than a rival.

Write the "what the CoE is not" section plainly. It is not an IT project, a monthly reporting group, a technology
experiment or a request queue where departments drop ideas for someone else to build. Say what happens instead: ideas
arrive with an owner and a framed problem, and the CoE provides method, assurance and reusable patterns.

For a Starter organisation, write terms of reference for an AI working group instead: purpose, three to five members by
role, a monthly meeting, sponsor attendance each quarter, and the same principles in a sentence each. Do not make a
small organisation pretend to be a large one.

Close with membership by role, time commitment, review date and how the charter is changed. Take the draft to the
sponsor for sign-off and record the decision. A charter nobody has signed is a proposal, and should be labelled as one.

## Outputs

- A CoE charter on the `coe-charter` template: purpose, outcomes with owners, pillar scope (active and deferred), principles with local consequences, sponsorship, decision rights, interfaces with existing forums, what the CoE is not, membership by role and review date.
- For Starter, AI working group terms of reference on the same `coe-charter` template in light form.
- A sign-off record naming the sponsor role and the date agreed.

## Microsoft platform considerations

The charter is platform-neutral. Where agent building on Power Platform is already happening, the charter should state
that the CoE sets the environment and data-policy position for it and works with whoever administers the tenant.
Microsoft publishes a Power Platform CoE Starter Kit and Copilot adoption resources; treat them as tooling the CoE may
use, not as the CoE itself, and check the current source records in `references/sources.md` before naming components.

## Adoption considerations

The charter is itself a change message. Publish a plain-language summary so staff know where to take ideas and
questions, and make the adoption and change pillar visible so the CoE is not perceived as a gatekeeper. Link the CoE to
the Champion community from `champions:champion-programme-design`.

## Knowledge considerations

Name knowledge management as a pillar even if it is deferred, and state that knowledge used by agents has an owner in
the business. Until the `knowledge-management` department is built, the CoE records knowledge owners against each
solution in the register.

## Security and privacy considerations

The charter should state that the CoE does not override the organisation's information security or data protection
functions; it routes solutions from risk tier 2 to the `security-privacy` review and records the result.

## Responsible AI considerations

Include a commitment that some uses will not be built, that human accountability stays explicit, and that tier 3 and 4
solutions go to the `responsible-ai` department (planned) or, until it exists, to an agreed accountable executive.

## Evaluation requirements

Not applicable to the charter itself, which is a mandate rather than a solution; evaluation standards for solutions are
set in `ai-centre-of-excellence:coe-governance-model`.

## Value measures

Tie the charter's outcomes to the scorecard from `ai-centre-of-excellence:coe-kpi-framework`, with a baseline and a
business owner for each. The charter's own test is whether decisions are taken in the forums it defines within the
agreed cycle time, measured by the CoE lead from the decision log.

## Scale notes

### Starter

One page of working-group terms. Three to five people by role, monthly, sponsor quarterly, partner support named for
anything beyond tier 1. Adoption, safe use and a few high-value scenarios are the whole scope.

### Scale

A two-page charter for a small core team with business representatives, monthly steering, delegated release decisions
up to tier 2 and a published intake route.

### Enterprise

A hub charter with spoke mandates per business unit, explicit federation rules (what spokes decide, what the hub
standardises), links to enterprise risk and architecture boards, and executive acceptance for tier 4.

## Hand-offs

- To `ai-centre-of-excellence:coe-operating-model` to design the team and flow.
- To `ai-centre-of-excellence:coe-raci` to assign responsibilities.
- To `ai-centre-of-excellence:coe-cadence` to set up the forums the charter names.
- To `ai-centre-of-excellence:coe-governance-model` for the governance framework.

## Reviewer gates

Not applicable as a release gate, because a charter is a mandate rather than a solution. The sponsor signs it off; any
reviewer-class department it names, such as `security-privacy`, should confirm the interface clause describes its role
correctly.

## Failure modes

- IT drafts and owns the charter, so departments see the CoE as an IT service and bring requests rather than ownership.
- All six pillars are claimed with no capacity, and nothing visible happens for months.
- Decision rights are vague, so every release is escalated and the CoE becomes a bottleneck.
- The sponsor signs and disappears, and the CoE loses the authority to say no.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Write a charter that makes IT or the CoE the owner of business outcomes or benefits.
- Give a Starter organisation a full CoE structure it cannot staff.
- Name individuals in the charter; use roles.
- Promise funding, headcount or decision rights the sponsor has not agreed.
