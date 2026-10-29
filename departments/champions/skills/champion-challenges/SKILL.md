---
name: champion-challenges
description: Designs the Champion Challenge - one practical contribution after the three capabilities are verified, such as an envisioning workshop, team training, a governed business agent, a prompt library, a departmental playbook or support for the Centre of Excellence - with a safety and scope check and assessment on impact, reusability, quality and strategic alignment. Use when Champions are ready to contribute or a challenge idea needs checking.
license: CC-BY-4.0
metadata:
  department: champions
  lifecycle: Enable, Deliver, Scale
  maturity: adopter, builder, scaler, ai-enterprise
  risk-tiers: 0, 1
  platforms: copilot-chat, m365-copilot, copilot-cowork, m365-agents
  edition-support: scale, enterprise
  reviewers: security-privacy
  sources: ms-champion-programme, ms-copilot-adoption-hub, ms-copilot-privacy
  status: draft
  authors: Simon Foote
---

# Champion challenges

## Purpose

A Champion Challenge turns verified capability into contribution. Once a participant has verified Chat, productivity
and agent capability, they complete one practical contribution that creates value for others and leaves something
reusable behind. This skill designs the Challenge options, the safety and scope check, the assessment criteria and the
route for bigger ideas. Challenges usually go wrong when they become hackathons that build ungoverned agents, when they
solve invented problems, or when the useful output stays in one person's head.

## When to use

- Participants have verified all three capabilities and need the practical step before recognition.
- The programme needs a published set of Challenge options and criteria for judging them.
- A proposed Challenge needs checking for safety, scope and fit before it starts.
- Completed Challenges need assessing consistently on impact, reusability, quality and strategic alignment.
- The community is losing energy and needs real work to focus on.

## When not to use

- Designing the programme, journey and boundaries - use `champions:champion-programme-design`.
- Defining the capabilities and verification criteria - use `champions:capability-framework`.
- Running assessor calibration, the tracker and appeals - use `champions:evidence-assessment`.
- Framing a significant opportunity that needs a business case or delivery team - use `opportunity-management:problem-framing`.
- Deciding whether a problem needs an agent, automation or a built solution - use `opportunity-management:ai-suitability`.
- Recognising completed Challenges - use `champions:recognition-and-progression`.

## Questions to ask first

1. What real, recurring problem or need will the Challenge address, and who owns it?
2. Which Challenge option fits the Champion's role and the team's need?
3. Which approved tools would it use, and what data and content would it touch?
4. What reusable asset would show it worked, and who would maintain it afterwards?
5. How much time has the Champion's manager agreed for the Challenge?

## Required inputs

- A participant with all three capabilities verified, from `champions:evidence-assessment`.
- A problem or need agreed with an owner, in a few sentences, with how they would judge improvement.
- The approved tools list, approved-use guidance and the organisation's agent governance.
- Manager agreement to the time involved, and the programme's current strategic priorities.

If the problem has no owner, it is not a Challenge yet. If it needs tools beyond the approved list, external access or
data above the agreed sensitivity, it is not a Challenge at all; route it to intake.

## Decision framework

Offer a small set of options so Champions contribute in ways that suit their role. Each produces a reusable asset.

| Option | What the Champion delivers | Reusable asset | Watch for |
|---|---|---|---|
| Envisioning workshop | Facilitates a team session to find where Copilot helps its real work | Workshop outline and scenario candidates | Ideas that outgrow individual use go to intake |
| Team training | Runs a practical session on the scenarios that matter to a team | Session materials, recording, linked guidance | Supplements formal training; does not replace it |
| Business agent | Configures a simple governed agent for a team need, where approved | Agent with owner, knowledge source, tests and intake record | Agent governance, data class, no external audience |
| Reusable prompt library | Curates tested prompt patterns for a role or process | Patterns with verification step, owner and review date | Confidential examples left in prompts |
| Departmental playbook | Documents how a department uses Copilot well in recurring work | Playbook of scenarios, guidance and checks | Must match approved-use guidance |
| Support for the Centre of Excellence | Contributes to CoE work, such as testing an agent, documenting a pattern or preparing intake material | Test notes, pattern write-up or intake summaries | The Champion supports; the CoE decides |

Every Challenge passes a scope and safety check before it starts.

| Check | A Challenge must | If not |
|---|---|---|
| Real need | Address a recurring issue a named owner confirms | Find a real need or drop it |
| Approved tools | Use only tools approved for Champions | Route to `opportunity-management:problem-framing` |
| Data safety | Use content the team already handles, with no special category or client-confidential data | Route to intake with a `security-privacy` review |
| Audience | Stay within the organisation; nothing externally facing | Route to intake |
| Size | Be completable in a few weeks within the agreed time | Split it, or route the larger part to intake |

Completed Challenges are assessed on four criteria, each Not yet, Meets or Strong. All four at Meets completes stage 5.

| Criterion | Meets looks like |
|---|---|
| Impact | The owner confirms a real improvement or benefit against their stated measure |
| Reusability | Another team could use the asset with little change |
| Quality | Accurate, checked for sensitive content, consistent with approved-use guidance |
| Strategic alignment | Supports a priority scenario, the adoption plan or the CoE portfolio |

## Practitioner approach

Position the Challenge clearly. It is stage 5 of the journey, taken once all three capabilities are verified, and it
is the step that turns a capable user into a Champion. Smaller practice tasks at earlier stages belong to the training
route, not here. One Challenge per participant is enough; its purpose is contribution, not another test.

Publish the options and let Champions choose. People contribute best in ways that suit their role: a team leader may
run an envisioning workshop, an analyst may build a prompt library, a maker may configure a business agent. Ask each
Champion to agree the problem or need with an owner in a few sentences, including how the owner would know it had
improved. A Challenge without an owner tends to solve something nobody needed solved.

Run the scope and safety check before any work starts, ideally with the programme owner. Most proposals pass easily.
Those that do not are routed, not rejected: work needing new connectors, external access, sensitive data or wider
release becomes an opportunity for `opportunity-management:problem-framing` through the CoE, with the Champion
credited as the person who found it.

Treat the business agent option with the same governance as any other agent: a named owner, knowledge that is owned
and current, test questions with expected answers and an intake record. The Centre of Excellence option is valuable
in its own right, because it gives Champions a supervised route into governed delivery and gives the CoE capable help.

Keep Challenges small and time-boxed, with a light midway check-in from the programme owner or an experienced
Champion to unblock rather than inspect.

Insist on a reusable asset. The value of a Challenge is that the next team does not start from scratch. Review each
asset for sensitive data and accuracy before publication, then add it to the scenario catalogue or community library
with an owner and review date.

Assess against the four criteria using the procedure in `champions:evidence-assessment`. Ask the owner for their view
of impact, judge reusability by whether another team could pick the asset up, check quality against the approved-use
guidance, and judge alignment against the adoption plan and CoE priorities. Strong ratings are feedback, not ranking.

Close each Challenge with a short write-up: need, approach, asset, result against the owner's measure, and what others
should know. Showcase good Challenges in community calls and to the sponsor, and collect them so Champions can reuse
proven ideas as well as bring their own.

## Outputs

- A Champion Challenge catalogue on the `champion-challenge-catalogue` template: options, proven Challenges, owners, tools, data class, reusable asset and status.
- A scope and safety check record for each Challenge.
- An assessment record against impact, reusability, quality and strategic alignment.
- A Challenge write-up and a reviewed reusable asset for each completed Challenge.
- Opportunity referrals to `opportunity-management:problem-framing` for anything outside Challenge scope.

## Microsoft platform considerations

Challenges use only the Copilot experiences and agent tools approved for Champions, such as Copilot Chat, Copilot in
the Microsoft 365 apps, Copilot Cowork or approved agent building tools. Where agent building is allowed, the
organisation's environment and data policy controls apply. Availability and naming change; check
`references/sources.md` and the approved tools list.

## Adoption considerations

Challenges create the local success stories that persuade sceptical colleagues more than central messages. Feed
workshop outputs, prompt libraries and playbooks into the scenario catalogue and launch reinforcement.

## Knowledge considerations

Many Challenges depend on team knowledge, and playbooks and prompt libraries become knowledge themselves. Give every
asset an owner and review date, and pass stale or unowned content to the `knowledge-management` department (planned)
rather than building on it.

## Security and privacy considerations

The data safety check is mandatory. Challenges must not use special category, client-confidential or highly sensitive
data, and assets must be reviewed for sensitive content before sharing. Anything that would widen access to content
goes to intake with a `security-privacy` review.

## Responsible AI considerations

Challenges must not automate decisions about people, money or safety. If a team need touches those areas, it is routed
to intake for risk classification rather than tackled as a Challenge.

## Evaluation requirements

Each Challenge measures its result against the owner's stated measure and is assessed on the four criteria. Business
agent Challenges include test questions with expected answers and a record of how the agent performed against them.

## Value measures

Programme-level measures, owned by the programme owner: Challenges started and completed by option, assets published
and reused, opportunities routed to intake and owner-reported results. Reported in aggregate, never as individual
league tables.

## Scale notes

### Starter

Usually omitted at this size; where a small organisation wants Challenges, offer two or three options such as team
training or a prompt library, checked and assessed by the owner.

### Scale

All six options published, a scope and safety check by the programme owner, trained assessors for the four criteria
and quarterly showcases.

### Enterprise

A curated catalogue by function, a standing asset review, business agent Challenges under formal governance, a defined
CoE support route, and regular reporting of routed opportunities to the CoE portfolio.

## Hand-offs

- To `champions:evidence-assessment` to assess completed Challenges against the four criteria.
- To `opportunity-management:problem-framing` for needs outside Challenge scope.
- To `ai-centre-of-excellence:coe-operating-model` so routed opportunities, CoE support and assets reach CoE governance.
- To `champions:recognition-and-progression` when a Challenge is completed.
- To `copilot-adoption:scenario-discovery` to add new scenarios and prompt patterns to the catalogue.

## Reviewer gates

From risk tier 1, `security-privacy` reviews any Challenge that touches content beyond the team's own working material
or produces an agent shared with others, looking for data exposure and appropriate access. Business agent Challenges
also pass CoE intake.

## Failure modes

- Challenges become hackathons that produce ungoverned agents with no owner.
- Problems are invented for the Challenge, so nothing useful changes in the team.
- Assets are not reviewed, and a shared prompt library includes confidential examples.
- Larger opportunities are tackled as Challenges instead of being routed, and stall half-built.
- Only the agent option is valued, so Champions without maker interest stall before recognition.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Start a Challenge that uses unapproved tools, sensitive data or an external audience.
- Let a Challenge release an agent or solution without an owner and intake record.
- Treat a routed opportunity as a failed Challenge.
- Publish an asset without checking it for sensitive content.
