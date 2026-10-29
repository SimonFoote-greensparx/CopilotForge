---
name: foundry-deployment-architecture
description: Chooses how a Microsoft Foundry solution is deployed - model deployment type, data processing location, capacity and quota, resource and project layout, environments, network exposure and failover - and records each choice with its trade-off. Use when a chosen model needs deploying, when data must stay in a geography, when throttling or regional outages hit, or when a prototype must move into governed environments.
license: CC-BY-4.0
metadata:
  department: ai-foundry
  lifecycle: Mobilise, Deliver, Launch, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure, entra
  edition-support: starter, scale, enterprise
  reviewers: design-authority, security-privacy
  sources: ms-foundry-models, ico-ai-data-protection
  status: draft
  authors: Simon Foote
---

# Foundry deployment architecture

## Purpose

The same model can be deployed in several ways that differ in where data is processed, how capacity is guaranteed,
what it costs and what happens when a region is busy or down. This skill turns the solution's data, performance and
resilience requirements into a deployment topology: which deployment type for each model, in which locations, with
what capacity and quota, inside which resources, projects and environments, and behind which network boundary. It goes
wrong when the prototype's deployment becomes production by default, when a globally routed deployment is chosen
without anyone checking the data constraint, and when quota limits are discovered on launch day.

## When to use

- A model has been selected and needs a deployment design for test and production.
- Data constraints require processing within a particular geography and the deployment options must respect them.
- Users meet throttling, rate-limit errors or slow responses at peak, or a regional incident took the solution down.
- A prototype built in a developer's project must move into governed environments.
- Several solutions are about to share Foundry resources and the layout needs deciding.

## When not to use

- Choosing which model to use - use `ai-foundry:model-selection`.
- Estimating and controlling cost once the topology is set - use `ai-foundry:foundry-cost-management`.
- Environment topology across Microsoft 365, Power Platform and Azure as a whole - use `ai-architecture:environment-topology`.
- Build and release pipelines that promote changes between environments - use `ai-engineering:ai-ci-cd`.
- Retry, fallback and degradation patterns in the application code - use `ai-engineering:ai-resilience`.

## Questions to ask first

1. What data will each model see, and is there a requirement, contractual or regulatory, on where it may be processed or stored?
2. What latency and throughput must the solution sustain at peak, and is the load steady, spiky or batch?
3. What is the availability target, and what should users experience if the primary deployment is unavailable?
4. Which environments does the solution need, and who may deploy to and call each one?
5. Must the endpoints be reachable only from private networks, or also from the internet or Microsoft 365?

## Required inputs

- The model selection record, including the fallback model, from `ai-foundry:model-selection`.
- Non-functional requirements for latency, throughput and availability, ideally on the `non-functional-requirements` template.
- Data classification and processing-location constraints confirmed by the data owner or DPO.
- The organisation's Azure landing zone, network and identity standards.

Where the processing-location constraint is unconfirmed, mark it `[To confirm: ...]` and design for the strictest
plausible reading until it is answered. Never treat a deployment's processing location as acceptable because nobody
has objected yet.

## Decision framework

Decide in this order, because each choice narrows the next.

| Decision | Options in principle | Choose by |
|---|---|---|
| Processing location | Global routing, a defined data zone or geography, or a single region | The confirmed data constraint first; then capacity and price |
| Capacity model | Shared pay-per-use, reserved throughput, batch, or dedicated managed compute for models hosted that way | Load shape and latency needs; reserved only with measured, steady demand and an owner |
| Resource and project layout | One project per solution, with shared resources only by design | Ownership, access boundaries and cost attribution |
| Environments | Development, test and production as a minimum, with production isolated | Risk tier and the release policy |
| Network exposure | Private endpoints with public access disabled, or controlled public access | Data sensitivity and where callers sit |
| Resilience | Single deployment, secondary deployment in another region, or fallback model | Availability target and the cost of downtime |

Not every option exists for every model, provider or region. A partner or community model may only offer some
deployment types. Confirm availability in the current source before designing around an option.

## Practitioner approach

Start from the data constraint, because it removes options rather than ranking them. Ask the data owner, and the DPO
where personal data is involved, what processing locations are acceptable, and record the answer with its source.
Then read the current documentation for how each candidate deployment type handles processing and storage, including
for logs, fine-tuning data and stored conversation state, which may sit somewhere different from inference. Only after
that consider price and capacity.

Size capacity from measured load. Use evaluation or pilot runs to establish tokens per request and requests at peak,
then compare that with the quota and rate limits the subscription has for the chosen deployment type and region. Quota
is allocated per subscription and region and can take time to raise, so request it early and record what was granted.
Where demand is steady and latency matters, reserved throughput can give predictable performance; where demand is
spiky, pay-per-use with client-side retry and back-off is usually better; where work can wait, batch keeps it off the
interactive path entirely. Pass the capacity choice to `ai-foundry:foundry-cost-management` before committing.

Lay out resources around ownership. Give each solution its own Foundry project inside the organisation's governed
subscriptions, so access, connections and cost are bounded. Share a resource between solutions only when someone owns
it and an allocation key is agreed. Keep production in its own environment with its own identities and connections,
and promote changes through pipelines rather than by editing in the portal.

Close the network by default. Disable public access where the callers allow it, use private endpoints for the Foundry
resource and the services it depends on, and authenticate with managed identities rather than keys. Where the solution
must be reached from Microsoft 365 or the internet, put a gateway in front that enforces authentication, rate limits
and logging, and agree the exposure with `security-privacy`.

Design for the day the deployment is unavailable. Decide whether a secondary deployment in another permitted location,
the named fallback model or a graceful message is the right response, and test the switch. A fallback that has never
been exercised is a hope, not a design.

Record each decision as an architecture decision with its trade-off and the source consulted, and note which facts are
volatile and when they were checked. State what the design cannot determine: real capacity headroom at launch, which
only load testing in the target environment shows.

## Outputs

- The deployment section of the `foundry-solution-design` template: deployment per model with type, location, capacity and quota granted, resource and project layout, environments, network design and failover.
- An `architecture-decision-record` for each significant choice, citing the source and date checked.
- A quota and capacity request list with owners and lead times.
- A tested failover or degradation procedure handed to operations.

## Microsoft platform considerations

Foundry deployment types, their processing-location behaviour, quota, reserved capacity terms and regional
availability vary by model and provider and change frequently. Some models are hosted and sold by Microsoft and others
by partners, with different deployment options and terms. Check the current source records for each fact before
recording it, note preview capabilities as risks, and keep the Foundry project inside the organisation's Azure landing
zone and policy. Licensing and commercial terms route to the Microsoft licensing guide or a licensing partner.

## Adoption considerations

Not applicable to most deployment decisions, because users see only responsiveness and availability. Where a
degradation mode changes what users experience, explain it to them in advance through the solution's communications.

## Knowledge considerations

Not applicable to model deployment itself. Grounding stores such as search indexes need the same location, network
and resilience decisions; make them together with `ai-foundry:retrieval-design` so knowledge is not left outside the
boundary.

## Security and privacy considerations

Processing location, network exposure, key handling and environment isolation are the main security decisions here.
Use managed identities, private networking and separate production identities, and confirm processing location for
inference, logs and stored state with the DPO. `security-privacy:ai-identity-and-access-review` reviews the topology
from tier 2.

## Responsible AI considerations

Not applicable to topology in most cases, because deployment choices rarely change what the solution decides. Where a
fallback model behaves differently from the primary, it must pass the same safety evaluation before it can serve users.

## Evaluation requirements

Load test the production topology at expected peak and beyond, including throttling behaviour and failover. Evaluate
the fallback model against the same quality and safety thresholds as the primary with `ai-foundry:model-evaluation`.

## Value measures

Track availability, latency at peak and throttled-request rate against the non-functional requirements, owned by the
solution owner. Track lead time from model selection to production deployment as a measure of platform readiness.

## Scale notes

### Starter

Use one project per solution in a governed subscription, pay-per-use in a location that meets the data constraint,
separate test and production, and a simple degradation message. Request quota before launch.

### Scale

Publish standard deployment patterns by data constraint and load shape, with network and identity baselines, so
solutions choose from reviewed options. Track quota across solutions.

### Enterprise

Run a shared AI platform with gateways, quota management, reserved capacity governance and multi-region resilience
patterns, and require architecture review for any deployment outside the standard patterns.

## Hand-offs

- To `ai-foundry:foundry-cost-management` for the cost of the chosen capacity model.
- To `ai-engineering:ai-ci-cd` for promotion between environments.
- To `ai-engineering:ai-resilience` for retry, back-off and fallback in code.
- To `ai-foundry:foundry-observability` to monitor capacity, throttling and failover.
- To `ai-foundry:foundry-production-readiness` once the topology is built.

## Reviewer gates

From risk tier 2, `security-privacy` reviews processing location, network exposure and identities, and
`design-authority` checks conformance to the reference architecture and landing zone. A deployment whose processing
location has not been confirmed against the data constraint is a blocking finding at any tier.

## Failure modes

- A globally routed deployment is chosen for capacity, and data is processed outside the permitted geography.
- Quota is requested the week of launch, and the solution is throttled from its first morning.
- The prototype's project, keys and public endpoint become production unchanged.
- The fallback deployment was never tested and fails when the primary region has an incident.
- Several solutions share one deployment, and one batch job starves the others of capacity.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Choose a deployment type before the data processing constraint is confirmed.
- State quota, capacity, regional availability or processing-location facts from memory.
- Promote a prototype deployment to production without rebuilding it in the governed environment.
- Rely on a failover or fallback model that has not been tested and evaluated.
