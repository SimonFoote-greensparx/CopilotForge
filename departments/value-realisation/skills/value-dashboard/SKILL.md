---
name: value-dashboard
description: Specifies a sponsor value dashboard for the AI portfolio across value, adoption, capability and governance, with each tile's measure, method, confidence, baseline, owner and source, plus the data flow from the benefits register, refresh, access, minimum group size and caveats, ready for a report builder. Use when sponsors need one view of realised value, when a dashboard shows usage alone, or when a chosen scorecard now needs building.
license: CC-BY-4.0
metadata:
  department: value-realisation
  lifecycle: Measure, Scale, Improve
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: fabric, power-platform, sharepoint
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-copilot-adoption-hub, ms-coe-starter-kit, ms-copilot-privacy
  status: draft
  authors: Simon Foote
---

# Value dashboard

## Purpose

Sponsors need one honest view of whether AI is paying off, and most AI dashboards show usage because usage is what the
tools export. This skill specifies a dashboard that leads with realised value and shows adoption, capability and
governance as the conditions behind it, with every figure carrying its method, confidence and owner. It produces a
specification a report builder can implement, including data flow, refresh, access and caveats. It goes wrong when
usage tiles crowd out value, when figures appear without their method, and when drill-downs reach individuals.

## When to use

- A sponsor or executive needs a single view of realised AI value across the portfolio.
- An existing dashboard shows licences and active users but no outcomes.
- The CoE scorecard measures are agreed and now need turning into a built dashboard.
- Value figures from several business units need presenting consistently.
- A renewal or budget round needs a current, traceable view of value achieved.

## When not to use

- Choosing the CoE's KPI families and measures - use `ai-centre-of-excellence:coe-kpi-framework`.
- Tracking value delivered by the CoE as a function - use `ai-centre-of-excellence:coe-value-tracking`.
- Designing adoption measures and reporting rules - use `copilot-adoption:adoption-measurement`.
- Building admin monitoring of the AI estate - use `platform-governance:ai-admin-monitoring`.
- Linking adoption indicators to benefits - use `value-realisation:adoption-to-value-metrics`.

## Questions to ask first

1. Who will use the dashboard, how often, and which decisions will they take from it?
2. Which measures are already agreed (CoE scorecard, benefits register), and which still lack baselines or owners?
3. Where does each measure's data live, who owns it, and how often can it be refreshed?
4. What minimum group size and access rules apply to adoption and staff measures?
5. What reporting tools does the organisation already use and support?

## Required inputs

- The agreed measure set from `ai-centre-of-excellence:coe-kpi-framework` and the `coe-kpi-scorecard`.
- The `benefits-register` with benefits, classes, baselines, results, confidence and owners.
- Adoption-to-value chains from `value-realisation:adoption-to-value-metrics`.
- Data source inventory with owners, and the agreed minimum group size and data protection position.

Where a measure has no data source yet, the specification shows the tile as "awaiting data" with the date it is
expected. Never populate a tile with an estimate presented as a measurement.

## Decision framework

Lay out four quadrants, with value first and largest. Every tile follows the tile rules.

| Quadrant | Question it answers | Typical tiles |
|---|---|---|
| Value | Is it worth it? | Realised benefits against target by class (cashable, non-cashable, cost avoidance, revenue, non-financial); estimated versus actual return; benefits at risk |
| Adoption | Are people using it where it matters? | Scenario behaviour by team or role; adoption-to-value chain status for priority benefits |
| Capability | Are we getting better at delivering it? | Opportunities reaching decision; solutions live with owner, baseline and measured value; share of teams able to own AI work |
| Governance | Is it safe and controlled? | Solutions with current reviews; tier controls in place; quality guards met; open incidents |

| Tile rule | Requirement |
|---|---|
| Method | Every value figure shows its method and confidence on hover or beside it |
| Comparison | Every figure shows baseline and target, not a number alone |
| Owner | Every tile names the owner role responsible for its figure |
| Class | Financial value is split by class and never summed into one headline |
| Aggregation | Adoption and staff measures by team or role above the minimum group size; no drill to individuals |
| Currency | Each tile shows the date of its data |

## Practitioner approach

Begin with the decisions. Ask the sponsor what they will do differently depending on what the dashboard shows: release
funding, push a struggling business unit, stop an initiative, renew licences. Each decision needs one or two tiles;
anything that informs no decision belongs in the detailed scorecard, not the sponsor view.

Lead with value and make it honest. The value quadrant shows benefits realised against target, split by class, with
confidence visible. Show the estimated return at approval beside the return achieved, and a short list of benefits at
risk with their owners. If the honest picture is that little value is yet evidenced, the dashboard should say so; a
dashboard that hides this loses its credibility the first time a finance lead asks a question.

Put adoption, capability and governance in their place. They explain value rather than substitute for it. Use scenario
behaviour rather than raw active users, show adoption-to-value chain status for the priority benefits, and keep
licence counts off the sponsor page. Capability tiles count outcomes, such as solutions with an owner and measured
value, rather than volume.

Design the data flow from the register. The benefits register is the single source for value tiles, so the dashboard
reads from it rather than holding its own figures. Adoption data comes from the organisation's aggregated reporting,
governance data from the solution register. Specify each source, owner, extract method and refresh frequency. Keep the
refresh rhythm aligned with the value review, because figures that change daily invite reaction to noise.

Specify access and privacy explicitly. Define who sees the sponsor view, who sees business-unit drill-downs and where
drill-down stops. Apply the minimum group size in the data model, not by convention, so a filter cannot reveal a small
team. Confirm the position with the data protection officer before the first release.

Write the caveats on the dashboard. State that it does not prove causation, that early adoption may not yet show in
value, and that self-reported measures are perceptions. Keep these visible, not in a footnote nobody opens.

Finish with a build-ready specification: page layout, each tile's definition, visual type, source, calculation,
filters, refresh, owner and access. Hand it to the organisation's report builder, then review the first version with
the sponsor and change it once, before it becomes the standard.

## Outputs

- A value dashboard specification: purpose and decisions, quadrant layout, tile definitions with method, source, calculation, refresh, owner and access.
- A data flow diagram from the `benefits-register`, adoption reporting and the solution register to the dashboard.
- An access and privacy specification including the minimum group size rule as implemented.
- Dashboard caveat text, agreed with the sponsor.

## Microsoft platform considerations

Dashboards are commonly built in Power BI over data held in SharePoint lists, Dataverse or Microsoft Fabric, and the
CoE Starter Kit provides inventory data for Power Platform solutions. Choose the tool the organisation already supports,
keep the register as the source of value figures, and check `references/sources.md` for what adoption reports and
inventory tools currently provide. Do not state licensing requirements for reporting tools; route those to the
licensing guide or a licensing partner.

## Adoption considerations

Share business-unit views with adoption leads and Champions so they can act on adoption tiles, at team level only. A
dashboard that only flows upwards teaches teams that measurement is about scrutiny.

## Knowledge considerations

Include a governance tile on knowledge health for live agents, such as the share of knowledge sources with an owner and
a review date in cycle, because knowledge decay undermines value before it shows elsewhere.

## Security and privacy considerations

Adoption data is often personal data. Aggregate in the data model, enforce the minimum group size technically, restrict
access by role, and keep raw data with its owner. Value figures from finance may be commercially sensitive and need
their own access rule.

## Responsible AI considerations

Avoid tiles that reward volume of AI use, such as prompts per person, which create pressure to use AI where it does not
fit. Include incidents and quality guard results so the sponsor sees harms beside benefits.

## Evaluation requirements

Quality tiles draw on live quality measurement and current evaluation results. Show the date of the last evaluation
for each live solution so stale evidence is visible.

## Value measures

Success is that the sponsor forum takes recorded decisions from the dashboard each cycle, and that every value tile
traces to a register entry with method and owner, checked by the Benefits Realisation Lead at each release of the
dashboard.

## Scale notes

### Starter

A single page or slide refreshed twice a year from a simple register: three or four value figures with method, two
adoption measures by team, and a short governance line. A built dashboard is optional.

### Scale

A built dashboard with the four quadrants, register-driven value tiles, quarterly refresh aligned with the value review,
and business-unit drill-downs above the minimum group size.

### Enterprise

A hub dashboard with spoke views that roll up quadrant by quadrant, shared definitions across business units, governed
data in a central platform, and an annual review of tiles nobody uses.

## Hand-offs

- To the organisation's report builder with the specification.
- To `ai-centre-of-excellence:coe-cadence` for the value review that uses the dashboard.
- To `value-realisation:benefit-realisation-plan` when benefits at risk need action.
- To `value-realisation:post-implementation-review` for initiatives whose tiles show sustained variance.

## Reviewer gates

From the first release, `security-privacy` confirms aggregation, minimum group size enforcement and access rules before
adoption or staff measures are published. Not otherwise a release gate, because the dashboard reports rather than acts.

## Failure modes

- Usage tiles dominate and the sponsor reads active users as return.
- Value figures appear without method or confidence and are dismissed at the first finance challenge.
- A business-unit filter reveals a small team's usage, breaching the minimum group size.
- The dashboard holds its own copy of figures, drifts from the register, and two versions of the truth circulate.
- The dashboard refreshes daily, and the sponsor reacts to noise instead of trends.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Show a value figure without its method, confidence and owner.
- Allow drill-down to individuals or below the minimum group size.
- Sum cashable, non-cashable and cost avoidance benefits into one headline.
- Put licence counts or active users in the value quadrant.
