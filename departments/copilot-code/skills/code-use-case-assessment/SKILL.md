---
name: code-use-case-assessment
description: Assesses whether a desired outcome genuinely needs software built with Copilot Code, or is better met by configuration, an existing product, a Power Platform app or flow, an agent, a Cowork task or no build, and whether the organisation can own what gets built. Use when a business team asks AI to build them an app or script, when a prototype is proposed, or when someone asks why not just have AI write it.
license: CC-BY-4.0
metadata:
  department: copilot-code
  lifecycle: Envision, Deliver
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 0, 1, 2, 3, 4
  platforms: copilot-code, github, power-platform, copilot-cowork, m365-agents, azure
  edition-support: starter, scale, enterprise
  reviewers: design-authority
  sources: ms-agents-extensibility, ms-agents-compare, ms-responsible-ai
  status: draft
  authors: Simon Foote
---

# Code use-case assessment

## Purpose

AI coding agents make software feel cheap to create, and that changes the question teams ask: not "should we build
this?" but "why not just have AI write it?". The build may be cheap; owning, securing, running and changing the result is
not. This skill tests a desired outcome against the alternatives and against the organisation's ability to own what gets
built, then gives a verdict: build with Copilot Code, prototype only, use another route, or do not build. It goes wrong
when the speed of generation hides the cost of everything that follows, and the organisation wakes up with dozens of
unowned applications.

## When to use

- A business team asks for an application, tool, script or integration and proposes AI to build it.
- A prototype has been suggested and someone needs to decide whether it should exist.
- A sponsor asks why the organisation does not simply have AI write the software it needs.
- An outcome sits between Power Platform, an agent, a Cowork task and custom code, and the route is unclear.

## When not to use

- Deciding at intake whether a framed opportunity needs AI at all - use `opportunity-management:ai-suitability`.
- Selecting the Microsoft platform for a solution at architecture level - use `ai-architecture:platform-selection`.
- Assessing whether a need justifies a custom AI solution on Microsoft Foundry - use `ai-foundry:foundry-solution-assessment`.
- Deciding whether a piece of work suits delegation to Copilot Cowork - use `copilot-cowork:cowork-use-case-assessment`.
- Writing the solution brief once a build is agreed - use `copilot-code:code-solution-brief`.

## Questions to ask first

1. What outcome is needed, for whom, and what do they do today without it?
2. Does an existing product, a configuration of something already owned, or a Power Platform app or flow meet most of the need?
3. Is the outcome working software at all, or is it a document, an analysis or a repeated task that Cowork or an agent could handle?
4. Who will own, support, secure and change the software for as long as it is used, and do they have engineering capability?
5. What data, systems and people would the software touch, and what happens if it fails or is wrong?
6. Is this a throwaway exploration or something people will rely on?

## Required inputs

- A framed outcome with a named business owner, from `opportunity-management:problem-framing` or equivalent.
- The organisation's approved build routes, engineering standards and owned platforms.
- An initial view of data sensitivity, systems touched and expected users.
- The organisation's position on AI-assisted development, if one exists.

Where ownership cannot be named, the verdict cannot be "build for production"; record it as a precondition. Never assume a
route, tool or licence is approved; mark it to confirm.

## Decision framework

Work down the options and stop at the first that meets the need with acceptable ownership.

| Option | Choose when | Reject when |
|---|---|---|
| No build | The need is a process, policy or training gap | Real software capability is missing after the fix |
| Existing product or configuration | Something owned or available meets most of the need | Material gaps remain that configuration cannot close |
| Power Platform app or flow | Business data, forms and workflow within governed environments; maker capability exists | Logic, scale or integration exceed what low-code can sustain |
| Agent or Cowork task | The outcome is answers, documents or delegated work rather than an application | Users need a persistent application or system integration |
| Copilot Code - prototype only | The aim is to learn, test an idea or show a concept, with a planned end | Anyone expects to rely on it in daily work |
| Copilot Code - production build | Software is the right answer, an engineering owner exists, and normal engineering controls apply | No owner, no review capacity, or no route to deploy and support |

Ownership test for production builds: a named business owner, a named engineering owner, a repository under organisational
control, code review and security review capacity, and a support route. If any is missing, the verdict is prototype only
or another route.

## Practitioner approach

Start with the outcome and the current workaround. Ask what people do today: a spreadsheet with macros, a manual
copy-and-paste between systems, a chain of emails. The workaround tells you the real requirement and often reveals that
the need is narrower than the request. "We need an app" frequently turns out to mean "we need one form and a weekly
report".

Check the cheaper routes honestly. Many requests are met by configuring something already owned, by a Power Platform app
under existing governance, or by a Cowork task that prepares the output a person needs. These routes come with existing
support, security and lifecycle arrangements. Custom code, however fast to generate, comes with none of them by default.

Separate exploration from reliance. A prototype built in an afternoon to test an idea is valuable and cheap, provided it
has a planned end. The danger is the prototype that people start using, because then it has users without an owner,
security review or support. Make the distinction explicit in the verdict and route prototypes through
`copilot-code:ai-assisted-prototyping`, which sets the boundaries.

Apply the ownership test before recommending a production build. Ask who will review the generated code, who will fix it
at the weekend when it breaks, who will update its dependencies, and where it will run. If the answers are "the person
who asked for it" and "their laptop", it is not ready for production, whatever its technical merit. AI-generated code still
needs people who understand it.

Weigh consequence. Software that writes to systems of record, handles personal data, makes or supports decisions about
people, or faces customers carries a higher risk tier and brings security, responsible AI and design reviews forward.
Software that reads data and produces a report for its own author is lower risk, though still not free of ownership
needs.

Record the verdict on the `code-solution-brief` template's assessment section: the route chosen, the routes rejected and
why, the ownership answers, the risk tier to confirm through `opportunity-management:risk-classification`, and any
preconditions. Product capabilities for Copilot Code and coding agents change quickly, so check current source records
before relying on a specific feature.

## Outputs

- A code use-case verdict: no build, other route (named), prototype only, or production build, with the deciding reasons.
- The ownership test answers and any preconditions.
- A referral to the right route for outcomes that should not be built with Copilot Code.
- For production builds, the starting point for the `code-solution-brief`.

## Microsoft platform considerations

Copilot Code, Power Platform, Copilot Studio agents, Copilot Cowork and Azure-hosted custom solutions serve different
levels of control, governance and engineering effort. Prefer the route the organisation already governs. Where code is
built, the repository, pipelines and hosting must sit under organisational control. Check current capabilities and
extensibility options in the source records (`ms-agents-extensibility`, `ms-agents-compare`) rather than memory, and route
licensing questions to the Microsoft licensing guide or a licensing partner.

## Adoption considerations

Saying "not with code" should still help: point the team to the route that will meet their need and, where useful, to
learning for that route. Teams who are refused without an alternative build software anyway, out of sight.

## Knowledge considerations

Not applicable as a primary concern at assessment, because the decision turns on outcome and ownership; where the outcome
is really about finding or using knowledge, route it to an agent or Cowork task instead.

## Security and privacy considerations

Note the data, systems and identities the software would touch. Anything handling personal or confidential data, writing
to systems of record or exposed outside the organisation raises the risk tier and needs
`copilot-code:generated-code-security-review` before release.

## Responsible AI considerations

If the software would make or support decisions about people, money, safety or rights, record it and route through risk
classification to the `responsible-ai` department before build. Some outcomes should not be automated at all.

## Evaluation requirements

Not applicable at assessment beyond stating what success would look like; acceptance criteria are set in
`copilot-code:code-solution-brief` and tested in `copilot-code:application-validation`.

## Value measures

Record the baseline cost of the current workaround (time, errors, delay) and the measure the business owner will use. For
production builds, include an honest estimate of ongoing ownership effort so value is judged net of it.

## Scale notes

### Starter

Most requests should end at no build, configuration, Power Platform or a prototype. Production builds need a partner or an
internal engineering team that can own them.

### Scale

Run the assessment as part of CoE intake with a consistent verdict record, and keep a register of approved builds and
prototypes with their end dates.

### Enterprise

Business units assess against the shared options and ownership test; production builds at risk tier 2 and above are
confirmed centrally and enter the engineering portfolio.

## Hand-offs

- To `copilot-code:code-solution-brief` for production builds.
- To `copilot-code:ai-assisted-prototyping` for prototype-only verdicts.
- To `opportunity-management:risk-classification` to confirm the risk tier.
- To `copilot-cowork:cowork-use-case-assessment`, `m365-agents:agent-opportunity-assessment` or `automation:automation-assessment` for other routes.

## Reviewer gates

From risk tier 2, `design-authority` reviews the verdict through `design-authority:platform-fit-review` and
`design-authority:ai-necessity-challenge` for unnecessary custom code and unsupportable builds. Findings are blocking or
advisory.

## Failure modes

- Software is built because generation was quick, and nobody owns it once it is in use.
- A prototype becomes a daily tool without security review, support or a repository the organisation controls.
- Custom code duplicates something a governed low-code app or existing product already does.
- The ownership test is answered with the requester's name by default.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Recommend a production build without a named engineering owner and a support route.
- Treat speed of code generation as evidence that building is the right answer.
- Let a prototype become relied on without passing through the production route.
- Assert product capabilities, availability or licensing from memory.
