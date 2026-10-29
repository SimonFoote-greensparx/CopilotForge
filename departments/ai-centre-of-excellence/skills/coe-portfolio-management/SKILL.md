---
name: coe-portfolio-management
description: Manages the CoE's whole portfolio of live and planned agents, automations and AI solutions as one view - lifecycle state, owners, tier, value against hypothesis, run cost and review dates - finding duplicates to consolidate, patterns to reuse and solutions to retire, through a quarterly portfolio review. Use when nobody can say what is live or who owns it, when similar agents multiply, or when steering wants to know what the estate delivers.
license: CC-BY-4.0
metadata:
  department: ai-centre-of-excellence
  lifecycle: Deliver, Measure, Scale, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: m365-agents, copilot-cowork, copilot-studio, ai-foundry, power-platform
  edition-support: scale, enterprise
  reviewers: design-authority
  sources: ms-coe-starter-kit, ms-copilot-studio-zoned-governance, ms-managed-environments, ms-copilot-studio-guidance
  status: draft
  authors: Simon Foote
---

# CoE portfolio management

## Purpose

Once a CoE has released a dozen solutions, the hard questions are no longer about the next build but about the estate:
what is live, who owns it, whether it still earns its keep, and whether three teams have built the same agent. This
skill runs the portfolio as one managed view across planned and live solutions, with a quarterly review that
consolidates duplicates, promotes reusable patterns and retires what no longer pays back. Portfolios go wrong when the
register is a one-off inventory that decays, when nothing is ever retired, and when value is reported only for the
newest, most visible solutions.

## When to use

- The CoE has several live solutions and nobody can produce a current list with owners.
- Similar agents or automations are appearing in different teams.
- Steering asks what the whole estate delivers, costs and risks, not just the latest pilot.
- Solutions have passed their review dates without anyone deciding whether to keep them.

## When not to use

- Balancing the mix of opportunities waiting in the backlog before build - use `opportunity-management:portfolio-balancing`.
- Building the technical inventory of agents, flows and environments from admin tooling - use `platform-governance:ai-solution-inventory`.
- Deciding whether one specific solution scales or stops - use `opportunity-management:scale-or-stop`.
- Scheduling the operational review of each live solution - use `ai-operations:ai-review-calendar`.
- Running the pipeline of ideas before release - use `ai-centre-of-excellence:coe-opportunity-pipeline`.

## Questions to ask first

1. Is there a register of agents and automations today, and how was it built: from admin inventory, from intake, or by asking people?
2. Which solutions are live, in pilot or in build, and does each have a business, knowledge and technical owner?
3. Which forum will take portfolio decisions such as consolidation and retirement, and how often?
4. What run costs are visible for each solution, and who can provide them?
5. What would make two solutions duplicates here: same audience, same knowledge, or same outcome?

## Required inputs

- The agent portfolio register defined in `ai-centre-of-excellence:coe-governance-model`.
- The technical inventory from `platform-governance:ai-solution-inventory` or admin tooling, where available.
- Value records from `ai-centre-of-excellence:coe-value-tracking`.
- Items in flight from `ai-centre-of-excellence:coe-opportunity-pipeline`.

If the register and the technical inventory disagree, the disagreement is itself a finding. Mark ownerless items "owner
to confirm" and never assign an owner without their agreement.

## Decision framework

Hold one record per solution in the portfolio, with at least these fields: name, purpose, audience, platform, lifecycle
state, risk tier, business owner, knowledge owner, technical owner, value hypothesis and latest measured value, run cost
or "to confirm", last review date, next review date and reuse status.

Classify every live solution at each quarterly review.

| Health | Test | Portfolio action |
|---|---|---|
| Healthy | Owners in place, reviewed on time, value at or near hypothesis, no open blocking findings | Keep; consider for reuse |
| Watch | One of owner, review, value or quality has slipped | Owner sets a recovery action and date |
| At risk | Two or more slipped, or an open blocking finding | Steering decides fix, pause or retire |
| Orphaned | No business owner | Find an owner within one cycle or retire |
| Duplicate | Same audience and outcome as another solution | Consolidate onto the stronger solution |

Classify reuse potential separately.

| Reuse status | Meaning |
|---|---|
| Pattern | The approach (instructions, knowledge structure, flow) can be copied by other teams with light change |
| Shared service | One solution can serve several audiences if its scope and owner widen |
| Local | Specific to one team and best left there |

Balance the portfolio view by lifecycle state and tier, so steering sees whether the estate is weighted towards pilots
that never finish, or towards high-risk solutions the CoE can barely support.

## Practitioner approach

Build the first portfolio view by reconciling three lists: what intake knows about, what the technical inventory shows
and what people say they use. Expect gaps in every direction. Solutions in the inventory with no intake record are the
unregistered estate; solutions people mention that appear nowhere may live in personal environments. Record each, and
treat registration as the first portfolio action rather than a compliance exercise.

Fill ownership before anything else. A solution without a business owner is a liability whatever its value. Ask the
team that benefits to name an owner; if nobody will, the solution is orphaned and the review should decide whether to
retire it.

Add value and cost. Pull value records from value tracking, and ask the technical owner or platform team for run cost,
including capacity, consumption and support effort. Where cost is unknown, record "to confirm" rather than zero, because
an estate that looks free is an estate nobody prunes.

Run a quarterly portfolio review in the strategy review or a dedicated steering slot. Present health by solution,
duplicates found, reuse candidates and retirement proposals. Take decisions solution by solution, and record them.
Retirement is a success when a solution has served its purpose or been replaced; plan it through
`ai-operations:ai-solution-retirement` so users and data are handled properly.

Look for patterns. When two or three teams have solved similar problems, choose the strongest and either widen it into
a shared service or publish it as a pattern other teams can copy. This is how the CoE turns isolated builds into
repeatable capability and cuts duplicate effort and risk.

Keep the portfolio connected to the pipeline. New releases enter the portfolio with their review date, and portfolio
decisions such as "widen this agent's audience" go back through the pipeline because wider reach can change the risk
tier.

Say what the portfolio cannot do: it shows what the estate delivers relative to its hypotheses, but it cannot prove
attribution of business outcomes to a single solution. Report confidence alongside value.

## Outputs

- A portfolio register view across planned, in-build, pilot and live solutions, with owners, tier, value, cost, review dates and reuse status.
- A quarterly portfolio review pack: health by solution, duplicates, reuse candidates, retirement proposals and decisions needed.
- A portfolio decision record: keep, recover, consolidate, widen, publish as pattern or retire, with owner and date.
- A pattern catalogue of reusable approaches published in the CoE's collaboration space.

## Microsoft platform considerations

Agents built in Copilot Studio and flows in Power Platform live in environments, so environment zoning and the CoE
Starter Kit or admin inventory are the most reliable sources for what exists technically. Agents built in Agent Builder,
Cowork tasks and Foundry solutions may surface through different admin routes. Check current inventory and admin
capability in `references/sources.md` and do not assume one tool sees the whole estate.

## Adoption considerations

Publish the gallery of live solutions so people find and reuse what exists instead of building again. When a solution
is consolidated or retired, tell its users what replaces it and why, before access changes.

## Knowledge considerations

Many duplicates share the same knowledge sources. Record knowledge owners for each solution, and use the portfolio view
to spot sources that several solutions depend on, which deserve priority in the knowledge pillar.

## Security and privacy considerations

Orphaned and unregistered solutions are the largest security exposure in most estates. Prioritise registering those
with wide sharing or sensitive knowledge, and bring forward a `security-privacy` review where a widened audience
changes the tier.

## Responsible AI considerations

Record which solutions inform decisions about people, money, safety or rights, and make sure each has human oversight
recorded and a review date that has not lapsed. Overdue reviews on these solutions go to steering first.

## Evaluation requirements

Each live solution at tier 2 and above should show a recent evaluation against its agreed threshold. Where the evidence
is older than its review cycle, mark the solution "watch" and route re-testing to `m365-agents:agent-testing` or the
platform's equivalent.

## Value measures

Measure the estate, not single solutions: share of live solutions with all three owners, share reviewed on time,
share at or near their value hypothesis, duplicates consolidated, patterns reused and solutions retired. The CoE lead
owns these measures and reports them quarterly through `ai-centre-of-excellence:coe-kpi-framework`.

## Scale notes

### Starter

Not usually needed as a separate discipline. A Starter working group keeps a simple list of what is live with owners and
review dates, and looks at it every quarter.

### Scale

One register, a quarterly portfolio review in steering, health classification and a published gallery. Consolidation
and retirement decisions start to matter as the estate grows.

### Enterprise

Spokes maintain their own entries in one shared register; the hub runs the cross-unit view, finds duplicates between
spokes, owns the pattern catalogue and takes portfolio decisions for shared services and tier 3-4 solutions.

## Hand-offs

- To `ai-operations:ai-solution-retirement` for solutions the review retires.
- To `ai-centre-of-excellence:coe-opportunity-pipeline` for widening or consolidation work that needs assessment.
- To `platform-governance:ai-solution-inventory` to close gaps between the register and the technical inventory.
- To `ai-centre-of-excellence:coe-value-tracking` for value records.

## Reviewer gates

From tier 2, `design-authority:platform-fit-review` and `design-authority:supportability-review` should challenge
consolidation and shared-service decisions for platform fit and supportability. Widened audiences return to `security-privacy` and `responsible-ai` review as the new tier requires.

## Failure modes

- The register is built once for a launch report and never updated.
- Nothing is ever retired, so support effort and risk grow while value stays flat.
- Duplicates are discovered but each team defends its own, and no decision is taken.
- Run costs are left blank and the estate is treated as free.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Keep a solution live without a business owner beyond one review cycle.
- Record unknown run cost as zero.
- Widen a solution's audience without returning it through risk classification.
- Use portfolio data to judge the makers who built solutions.
