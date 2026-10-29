---
name: coe-charter
description: Drafts the charter for an AI Centre of Excellence - purpose, who owns what between the business, AI enablement and the sponsor, scope across the six pillars, decision rights, launch commitments and what the CoE is not - or the lighter terms of an AI working group. Use when leadership asks for an AI CoE, when a group has drifted into a reporting forum or request queue, or when a sponsor needs one page to agree before people are appointed.
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
2. Who is the executive sponsor, and will they personally attend steering, take priority decisions, remove blockers, secure resources and accept risk?
3. Which of the six pillars are in scope now, and which are deliberately deferred?
4. What may the CoE decide on its own, what does it recommend, and what stays with business owners or existing boards?
5. Which business unit benefits and will own the CoE, how many of its people can give real time, and what support can a central AI enablement function offer?
6. What already exists that the CoE must work with rather than duplicate (an architecture board, a data protection function, a Power Platform CoE, a change team)?

## Required inputs

- The strategic outcomes or AI ambition, from `ai-strategy:strategic-outcomes`, or at least the sponsor's stated goals.
- The recommended edition and archetype from `organisation-tailoring:edition-and-archetype`, which sets the charter's weight.
- The executive sponsor (as a role) and the business functions that will contribute members.
- A list of existing governance forums and policies the CoE must connect to.

If outcomes are missing, write the charter with outcome entries marked `[To confirm]` and make agreeing them the first
decision of the first steering meeting. Never invent a sponsor, a budget or a mandate the organisation has not given.

## Decision framework

Settle the ownership split first, because every later clause depends on it.

| Party | Owns or leads | Typical consequence in the charter |
|---|---|---|
| The business (the unit that benefits) | Priorities, knowledge, outcomes, adoption, return on investment | Business owners propose and rank opportunities, keep knowledge current, drive use in their teams and report benefits |
| AI and IT enablement | Governance, architecture, security, technical delivery, support | The central function sets standards, reviews risk, builds or assures what needs specialist skills and supports live solutions |
| Executive sponsor | Funding, decisions, resource allocation, adoption support | Attends steering, takes priority decisions, removes blockers, secures people and money, drives adoption and resolves conflicts |

Then set the form by edition. Team sizes are typical starting points to adjust to real capacity, not fixed rules.

| Edition | Typical form | Sponsor role | Decision rights |
|---|---|---|---|
| Starter | AI working group: a lead and a handful of people by role, one page of terms | Takes the decisions at a short monthly slot; delegate named in writing if absent | Recommends; the sponsor decides |
| Scale | Business-owned CoE: sponsor, CoE lead, often three to five core members, a Champions network, central AI enablement in support | Chairs the monthly steering group | Decides intake, risk tier and release up to tier 2; recommends above |
| Enterprise | Hub and spoke: a CoE per benefiting business unit under shared hub standards | Executive board sponsor plus a sponsor per spoke | Hub sets standards once; spokes decide within them; board accepts tier 4 risk |

Test every clause against the five principles. If a clause fails one, rewrite it.

| Principle | Test |
|---|---|
| Business-owned | Does a business role own the priority, the knowledge and the benefit, not IT? |
| AI-enabled | Does the central function enable and assure rather than own or build everything? |
| Outcome-focused | Is the clause tied to an outcome, not an activity count? |
| Govern once | Is the control defined once and reused, not re-argued per request? |
| Repeat everywhere | Can a second business unit adopt it unchanged? |

## Practitioner approach

Begin with the sponsor, not the membership. A CoE without an executive who will decide, unblock and accept risk becomes
an enthusiasts' club, so confirm sponsorship before drafting anything else. Be explicit that the sponsor is a decision
maker, not a recipient of monthly reports: they attend steering, settle priority conflicts between teams, remove
blockers and secure resources. Ask them to state what would be different in a year if the CoE worked, and translate
that into two or three outcomes with business owners.

Place ownership in the business unit that benefits. The CoE lead and core members come from that unit; a central AI
enablement function supports them as advisor, coach, governance specialist and technical specialist, but does not own
the CoE. Write this split into the charter in one table, because the commonest drift is a CoE that slowly becomes the
central AI team's request queue.

Write the purpose as one sentence a department head would recognise, such as "build business capability supported by
AI, not build AI for its own sake". Then set scope using the six pillars: opportunity management, knowledge management,
agent development, automation, adoption and change, and governance. Mark which are active now and which are deferred.
A CoE that claims all six on day one with two part-time people will deliver none of them. For most adopters, adoption
and change, opportunity management and governance come first.

State the principles and give each a local consequence. "Govern once, repeat everywhere" should say that a control or
pattern agreed for one team is reused by the next, not renegotiated.

Decision rights are where charters earn their keep. List the decisions the CoE takes (intake criteria, risk
classification, release up to an agreed tier), those it recommends (investment, tier 3 and 4 releases) and those it
never takes (priorities within a department, HR matters). Connect to existing forums by name, so the charter adds a
route rather than a rival.

Write the "is and is not" section plainly. A CoE is a business transformation capability, a structured delivery
function, a governance framework, and the home of opportunity management, knowledge management and value measurement.
It is not an IT project, a monthly reporting group, a technology experiment or a queue of requests for the central AI
team. Ideas arrive with an owner and a framed problem; the CoE supplies method, assurance and reusable patterns.

Close with launch commitments the sponsor and members sign up to: active sponsorship, Champion participation with agreed
time, knowledge ownership, opportunity prioritisation through one backlog, measurement of return against baselines, and
continuous improvement. Add membership by role, time commitment and review date. A charter nobody has signed is a
proposal, and should be labelled as one.

## Outputs

- A CoE charter on the `coe-charter` template: purpose, outcomes with owners, the ownership split between business, enablement and sponsor, pillar scope (active and deferred), principles with local consequences, sponsor commitments, decision rights, interfaces with existing forums, what the CoE is and is not, structure and membership by role, launch commitments and review date.
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

One page of terms for an AI working group: a lead and a few people by role, a monthly meeting with a short sponsor
decision slot, and partner support named for anything beyond tier 1. Adoption, safe use and a few high-value scenarios
are the whole scope. Do not make a small organisation pretend to be a large one.

### Scale

A two-page charter for a business-owned CoE: sponsor, lead, a small core team (often three to five), a Champions network
and central AI enablement in support, with monthly steering, delegated release decisions up to tier 2 and one backlog.

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
- The sponsor signs and disappears, receiving reports instead of taking decisions, and the CoE loses the authority to say no.
- The central AI team is written in as owner, so the benefiting business unit treats the CoE as someone else's project.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Write a charter that makes IT or the CoE the owner of business outcomes or benefits.
- Give a Starter organisation a full CoE structure it cannot staff.
- Name individuals in the charter; use roles.
- Promise funding, headcount or decision rights the sponsor has not agreed.
- Make the central AI enablement function the owner of a business unit's CoE.
