---
name: effort-assessment
description: Estimates what an AI opportunity will really take - build effort by pattern, the scarce skills and owners it needs, its dependencies on knowledge, data, platforms and reviewers, and the ongoing run cost after release - as ranges with stated confidence. Use when an opportunity needs a feasibility score, when a team says an agent will take a week, or when nobody has asked who will run and pay for a solution after launch.
license: CC-BY-4.0
metadata:
  department: opportunity-management
  lifecycle: Envision, Mobilise
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: copilot-chat, m365-copilot, m365-agents, copilot-cowork, copilot-code, copilot-studio, ai-foundry, power-platform
  edition-support: starter, scale, enterprise
  reviewers: design-authority
  sources: ms-agents-compare, ms-declarative-agents, ms-agent-builder, ms-copilot-studio-guidance, ms-foundry-models
  status: draft
  authors: Simon Foote
---

# Effort assessment

## Purpose

This skill gives an honest estimate of what an AI opportunity will take to build and, just as importantly, to run. It
sizes build effort for the chosen pattern, names the scarce skills and owners it needs, exposes dependencies on
knowledge, data, platforms and review capacity, and estimates the ongoing cost of owning the solution after release.
Estimates usually go wrong by sizing only the build (a demo in a day becomes a release in three months), by ignoring the
business and knowledge owners' time, and by forgetting that every live solution needs someone to review, refresh and
eventually retire it.

## When to use

- A framed opportunity with a suitability decision needs a feasibility score for prioritisation.
- A team claims an agent or automation can be built in days and the claim needs testing.
- A business case needs build and run cost ranges.
- Several opportunities compete for the same makers, engineers, knowledge owners or reviewers.
- A live solution's actual running effort needs to be compared with what was assumed.

## When not to use

- Deciding which pattern or rung the opportunity needs - use `opportunity-management:ai-suitability`.
- Scoring and ranking opportunities against each other - use `opportunity-management:opportunity-prioritisation`.
- Tracking programme budget and capacity across workstreams - use `programme-management:budget-and-capacity`.
- Managing model and platform consumption cost for a Foundry solution in operation - use `ai-foundry:foundry-cost-management`.
- Licensing and capacity questions - use `platform-governance:ai-licensing-and-capacity`, which routes to the licensing guide or a partner.

## Questions to ask first

1. Which pattern did suitability choose, and does it combine parts (for example an automation plus an agent)?
2. Which knowledge, data and systems does the solution depend on, who owns them and what condition are they in?
3. Which scarce roles will it need: makers, engineers, knowledge owners, reviewers, the business owner?
4. What risk tier is it, and therefore which reviewer gates and evaluation will it need?
5. Who will own, support and review it once live, and how often must its knowledge or prompts change?

## Required inputs

- The framed problem and suitability decision on the `opportunity-canvas`, including pattern and preconditions.
- The initial risk tier from `opportunity-management:risk-classification`.
- The value hypothesis, so effort can be weighed against value.
- Access to someone who has built the pattern before, internally or through a partner.

Where no experienced estimator is available, widen the ranges and lower the confidence rather than guessing narrowly.
Never state platform consumption prices or licence costs; record them as "to confirm" with the licensing partner.

## Decision framework

Size build effort by pattern, then adjust for the drivers below. Sizes are relative bands to calibrate locally, not
fixed durations.

| Pattern | Usual starting band | Main effort drivers |
|---|---|---|
| Adoption scenario or prompt pattern | Extra small | Learning material, Champions time |
| Cowork task design | Small | Context design, checkpoints, validation with real work |
| Declarative agent (Agent Builder) | Small to medium | Knowledge readiness, instructions, testing with real questions |
| Copilot Studio agent with actions | Medium to large | Connectors, authentication, flows, ALM, evaluation |
| Automation with AI steps | Medium | Process redesign, exception handling, monitoring |
| Copilot Code build | Medium to large | Requirements, review, security testing, deployment |
| Foundry solution | Large to extra large | Retrieval, models, evaluation harness, operations |

Move up one band for each of these: knowledge needing clean-up or new ownership, integration with a system not yet
connected, risk tier 3 or above, external or customer-facing audience, or a team building the pattern for the first
time.

Estimate run effort as a separate figure covering owner time, knowledge refresh, review cycles, monitoring, support,
consumption and eventual retirement. Classify run effort as light, moderate or heavy.

| Confidence | Meaning |
|---|---|
| High | Pattern built here before; dependencies confirmed |
| Medium | Pattern known; one or two dependencies unconfirmed |
| Low | New pattern, or key dependencies unknown; range is wide |

## Practitioner approach

Start from the pattern suitability chose and resist re-deciding it. If the effort looks out of proportion to the value,
say so and send it back to suitability with the evidence; a cheaper rung may meet most of the need.

Break the work into build, assure and run. Build covers design, configuration or code, knowledge preparation and
integration. Assure covers testing, evaluation and the reviewer gates the risk tier requires. Run covers everything
after release. Teams nearly always estimate build alone, so put assure and run on the page first to make the point.

Estimate with someone who has built the pattern before. Walk through the steps together and ask where the last similar
build spent its time. Typical surprises are knowledge clean-up, authentication and connector approvals, waiting for
reviewers, and gathering realistic test questions. A demo built in a day says little about these.

List dependencies explicitly, with an owner and status for each: knowledge sources, data access, a connector or
environment, a platform capability, a reviewer slot, a partner. Mark any dependency outside the team's control. A
single unconfirmed dependency on another team often matters more than the whole build estimate.

Name the people, by role, and the time each needs: business owner, knowledge owner, maker or engineer, tester,
reviewers. Check with their managers that the time can be released. Owner time is the constraint most often missed and
the one that most often stalls delivery.

Estimate run effort honestly. How often will knowledge change, and who will update it? How often will the solution be
reviewed? Who handles user questions and failures? What consumption costs will grow with use, and who pays? Record
consumption as a range with assumptions and leave prices to the licensing partner.

Express everything as ranges with a confidence level, and record the assumptions behind each. Feed the result to
prioritisation as the feasibility evidence, and to the business case where one is needed. When delivery completes,
compare actual effort with the estimate and feed the difference back into the local bands; that is how estimates
improve.

## Outputs

- An effort assessment: pattern, build, assure and run effort as ranges with confidence, roles and time needed, dependencies with owners and status, and assumptions.
- The feasibility evidence for the backlog entry on the `prioritisation-matrix` template.
- A run-cost profile (light, moderate or heavy) with the owner and the items that drive it.
- After delivery, an estimate-versus-actual note that recalibrates local bands.

## Microsoft platform considerations

Effort differs sharply between patterns. Declarative agents reuse Microsoft 365 orchestration and are quicker to build
but limited in control; custom engine agents and Foundry solutions give control at the cost of engineering, evaluation
and operations. Copilot Studio agents depend on environments, connectors and data policies being in place. Check
current capabilities, limits and licensing against `references/sources.md` before an estimate relies on them.

## Adoption considerations

Include the effort to bring the solution to its users: learning, communications, Champions support and manager
briefing. A solution with no adoption effort budgeted will be built and not used.

## Knowledge considerations

Knowledge preparation is frequently the largest hidden effort for agents. Size clean-up, ownership and review work with
the knowledge owner, and treat unowned knowledge as a dependency, not a task for the build team.

## Security and privacy considerations

Higher risk tiers bring security and privacy reviews, identity design and data access work. Include them in assure
effort and check reviewer availability; a solution waiting weeks for a review slot has an effort problem, not just a
scheduling one.

## Responsible AI considerations

For tier 3 and tier 4 opportunities, include impact assessment, oversight design and responsible AI review time. If
that capacity is not available in the horizon, record it as a blocking dependency.

## Evaluation requirements

Include the effort to build test sets, run evaluations and repeat them after changes. For agents and engineered
solutions this is often a significant share of assure effort and should never be omitted.

## Value measures

Measure estimation quality at portfolio level: the share of delivered initiatives whose actual effort fell within the
estimated range, and the share whose run cost matched the profile. The AI portfolio manager owns these. Never use
estimate accuracy to judge individual estimators.

## Scale notes

### Starter

Use the pattern bands and a short dependency list in one conversation with a partner or experienced maker. Run effort
is usually the business owner's time, so name it.

### Scale

A standard effort record for every opportunity entering assessment, with local bands recalibrated each quarter from
estimate-versus-actual notes.

### Enterprise

Shared bands across business units, with the hub providing estimators for engineered solutions and tracking scarce
roles across the portfolio so competing opportunities are visible early.

## Hand-offs

- To `opportunity-management:opportunity-prioritisation` with the feasibility evidence.
- To `opportunity-management:business-case` with build and run cost ranges.
- To `opportunity-management:portfolio-balancing` where scarce roles constrain the portfolio.
- Back to `opportunity-management:ai-suitability` when effort is out of proportion to value.

## Reviewer gates

From risk tier 2, `design-authority` may challenge an estimate that relies on an unsupported pattern or understates run
effort. Until challenged, the CoE lead records the assumptions on the assessment.

## Failure modes

- Only the build is estimated, and assurance and run effort appear as surprises after approval.
- A one-day demo is taken as evidence that the production solution is small.
- Owner and knowledge owner time is assumed rather than agreed, and delivery stalls waiting for them.
- Consumption is ignored, and run costs grow with adoption until someone asks who is paying.
- Estimates are never compared with actuals, so the same optimism repeats.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Give a single-figure estimate without a range, confidence and assumptions.
- State platform prices, consumption rates or licence costs; leave them to the licensing guide or a licensing partner.
- Leave run effort, owner time or reviewer time out of the estimate.
- Use estimate accuracy to assess or rank individual estimators.
