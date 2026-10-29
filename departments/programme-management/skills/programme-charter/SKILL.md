---
name: programme-charter
description: Charters an AI adoption, delivery or transformation programme - mandate, the outcomes it serves, scope and exclusions, workstreams, governance and decision rights, tolerances, funding envelope, roles and closure criteria - so the sponsor signs one agreed basis for running it. Use when an agreed pack or roadmap needs mobilising, when AI initiatives run without a common mandate, or when a sponsor asks what the programme is committing to.
license: CC-BY-4.0
metadata:
  department: programme-management
  lifecycle: Mobilise
  maturity: explorer, adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: platform-neutral
  edition-support: starter, scale, enterprise
  reviewers: none
  sources: ms-copilot-adoption-hub, nist-ai-rmf, iso-iec-42001
  status: draft
  authors: Simon Foote
---

# Programme charter

## Purpose

A Microsoft AI programme touches licences, platforms, knowledge, people, governance and suppliers at once, and without a
single mandate each workstream optimises for itself. This skill writes the programme charter: why the programme exists,
which strategic outcomes it serves, what is in and out of scope, how it is organised and governed, what tolerances the
programme manager may work within, and how it will end. Charters go wrong when they restate the strategy, when they
promise outcomes the programme cannot deliver alone, or when they are signed and never consulted again.

## When to use

- A transformation pack or AI roadmap has been agreed and someone must now run it as a programme.
- Several AI initiatives (a Copilot rollout, an agent build route, a CoE launch) are running without a common mandate.
- A sponsor asks what the programme is committing to, by when, and with what money and people.
- A programme has drifted and needs re-chartering after a change in scope, sponsor or funding.

## When not to use

- Agreeing the strategic outcomes and principles the programme serves - use `ai-strategy:strategic-outcomes`.
- Writing the charter of the AI Centre of Excellence, which outlives the programme - use `ai-centre-of-excellence:coe-charter`.
- Producing the tailored set of transformation artefacts - use `organisation-tailoring:transformation-pack`.
- Building the funding case before the programme is approved - use `ai-strategy:investment-case`.
- Planning milestones and dependencies across workstreams in detail - use `programme-management:integrated-roadmap`.
- Defining the evidence each programme gate needs - use `programme-management:stage-gates`.

## Questions to ask first

1. Which agreed strategic outcomes does this programme serve, and which of them can it influence directly rather than only contribute to?
2. Who is the accountable sponsor, and what decisions are they reserving for themselves rather than delegating to a programme board?
3. What is explicitly out of scope, including platforms, business units and solution types the organisation has decided not to pursue yet?
4. What funding envelope and people capacity have been committed, and for how long?
5. What would make the sponsor stop or re-scope the programme early?

## Required inputs

- Agreed strategic outcomes from `ai-strategy:strategic-outcomes`, or the outcomes section of the transformation pack.
- The AI roadmap or pack index showing the initiatives and artefacts the programme will deliver.
- The confirmed edition and assurance overlay from `organisation-tailoring:edition-and-archetype`, which set the weight of governance.
- The ownership map from `organisation-tailoring:ownership-map`, showing declared roles and vacancies.
- Any approved funding decision or investment case.

Where an input is missing, write `[To confirm: ...]` in the charter and list it as a condition of sign-off. Never invent a
budget, a date or an owner to make the charter look complete; a charter with visible gaps is more useful than one that
hides them.

## Decision framework

Decide the shape of the charter from the programme type and edition. The programme manager runs within tolerances; any
forecast breach goes to the board, and any breach of the sponsor's reserved limits goes to the sponsor.

| Programme type | Typical workstreams | Main risk to manage in the charter |
|---|---|---|
| Adoption (Copilot Chat or Microsoft 365 Copilot) | Readiness, scenarios, Champions, learning, communications, measurement | Treating licence assignment as success |
| Delivery (agents, Cowork task designs, automations, Foundry solutions) | Intake, build, assurance, release, operations | Building faster than reviewers and owners can absorb |
| Transformation (both, plus CoE and operating model) | All of the above, plus governance, knowledge, operating model and value | Running too many workstreams for the declared capacity |

| Charter element | Starter | Scale | Enterprise |
|---|---|---|---|
| Form | One or two pages agreed at the working group | Full charter, signed by the sponsor | Full charter with business-unit annexes |
| Governance | Sponsor decides at a monthly slot | Programme board with delegated tolerances | Programme board plus portfolio or executive board above it |
| Tolerances | Time and money only | Time, money, scope and risk | Time, money, scope, risk, benefits and quality |
| Closure | Review at an agreed date | Closure criteria plus hand-over to the CoE | Closure criteria per tranche plus hand-over to run organisations |

Every outcome the charter names must pass one test: can the programme show its contribution with a measure and a
baseline? If not, the outcome belongs to the strategy, and the charter names the programme's contribution instead.

## Practitioner approach

Start from the outcomes, not the activities. Write one sentence for each strategic outcome the programme serves and,
beside it, what the programme will deliver that moves it. "Reduce time spent on case summaries" becomes "deliver role
scenarios and a governed summarisation agent for case handlers, with a measured baseline". This separates what the
programme controls from what the business must do with it, which is where most disputes about AI programme success
start.

Next, write scope as decisions. Name the platforms in scope, the business units and personas, the solution types and
the risk tiers the programme will deliver. Then write the exclusions with equal care: tier 3 and 4 solutions deferred
until responsible AI review capacity exists, for example, or Foundry work excluded from the first tranche. Exclusions
prevent the programme quietly absorbing every AI request in the organisation.

Organise the work into a small number of workstreams, each with an accountable role from the ownership map. Use the
programme type table as a starting point and merge workstreams where one role leads several. A programme with more
workstreams than accountable people will not hold together.

Agree governance and tolerances with the sponsor before writing them down. The sponsor reserves some decisions (risk
acceptance above an agreed tier, changes to outcomes, funding beyond the envelope); the board takes others; the
programme manager acts within tolerance. Keep the CoE's standing governance separate from the programme's: the
programme delivers change, the CoE runs what remains afterwards, and the charter should say when responsibilities pass
from one to the other.

Record the funding envelope and committed capacity as they have been approved, not as hoped. Licence and consumption
costs are often the least certain lines; mark them `[To confirm: ...]` and route licensing questions to the Microsoft
licensing guide or a licensing partner rather than estimating them in the charter.

Write closure criteria at the start. A programme closes when its outcomes have measured contributions, its products
have owners, support routes and review dates, and its remaining work has been handed to the CoE or business units.
Without these criteria AI programmes either never close or close when the money runs out.

Finally, take the charter to the sponsor for signature with the open items listed. Store it with the programme's
records, review it at each stage gate, and re-charter rather than drift if scope, sponsor or funding changes materially.

## Outputs

- A programme charter on the `programme-charter` template: mandate, outcomes served and the programme's contribution, scope and exclusions, workstreams with accountable roles, governance and decision rights, tolerances, funding envelope and capacity, key assumptions, closure criteria and sign-off.
- A list of open items and conditions of sign-off, each with the role who will resolve it.
- A record of the sponsor's approval and the date of the first charter review.

## Microsoft platform considerations

Name the Microsoft platforms in scope as patterns of work (individual Copilot use, shared agents, delegated Cowork
tasks, engineered Foundry solutions, Power Platform automation) rather than relying on product names, which change.
Where scope depends on a capability being available or licensed, mark it as an assumption and check it against the
source records in `references/sources.md` before the charter is signed.

## Adoption considerations

An adoption programme's charter must name the business roles accountable for adoption in their areas; an IT-led charter
for Copilot rollout tends to end at licence assignment. Include Champions and line managers as contributors, not as
accountable owners.

## Knowledge considerations

Where agents or knowledge-grounded scenarios are in scope, list knowledge readiness as a named workstream or dependency
with an accountable role. Programmes that assume content is ready discover otherwise during testing.

## Security and privacy considerations

The charter should state that solutions at risk tier 2 and above pass the `security-privacy` gate before release, and
that the programme does not decide data protection questions; those route to the DPO or legal adviser. Store the
charter in the organisation's own location with access limited to the programme team and board.

## Responsible AI considerations

State whether tier 3 and 4 uses are in scope. If they are, the charter names the accountable executive for risk
acceptance and the `responsible-ai` review route; if not, it says so plainly so requests can be redirected.

## Evaluation requirements

Not applicable to the charter itself, which is a governance document; it should commit the programme to the evaluation
gates its solutions need, held by `evaluation-quality` from risk tier 2.

## Value measures

The charter names, for each outcome, the measure, the baseline or the plan to establish it, and the business owner,
drawing on `value-realisation:benefit-realisation-plan` where it exists. Programme measures are reported at team or
role level, never for individuals.

## Scale notes

### Starter

A two-page charter: three outcomes, scope and exclusions, the sponsor's decisions, a funding note, and a review date.
Often agreed at the AI working group and kept with its terms of reference.

### Scale

A full charter with a programme board, three to six workstreams with accountable roles, tolerances for time, money,
scope and risk, and closure criteria that hand ownership to the CoE.

### Enterprise

A programme charter with business-unit annexes, tranches with their own closure criteria, and an explicit link to the
portfolio or executive board that sits above the programme.

## Hand-offs

- To `programme-management:integrated-roadmap` to plan milestones and dependencies within the chartered scope.
- To `programme-management:programme-board-cadence` to set up the forums the charter describes.
- To `programme-management:stage-gates` to define the gates and evidence the charter commits to.
- To `programme-management:budget-and-capacity` to track the funding envelope and capacity.
- To `programme-management:programme-risk-log` with the assumptions recorded in the charter.

## Reviewer gates

Not applicable, because the charter releases no solution; it must still name `security-privacy` from risk tier 2 and,
where in scope, `responsible-ai`, `evaluation-quality` and `design-authority` as gates the programme's solutions pass.

## Failure modes

- The charter promises business outcomes the programme cannot deliver alone, and the programme is later judged a failure for things it never controlled.
- Scope has no exclusions, so every AI request in the organisation lands on the programme.
- Workstreams outnumber accountable people, and the programme manager quietly becomes owner of everything.
- Licence and consumption costs are estimated from memory and the envelope proves wrong within months.
- The charter is signed once and never reviewed, so scope drifts without a decision.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Invent budgets, dates, owners or licence positions to complete the charter.
- Charter a programme without a named accountable sponsor role.
- Merge the programme's temporary governance with the CoE's standing governance without saying when one hands over to the other.
- State a licensing conclusion; route it to the Microsoft licensing guide or a licensing partner.
