---
name: secrets-and-identity
description: Engineers the identities and secrets of a custom AI solution - managed identities and keyless access to model endpoints, on-behalf-of user access for data and tools, agent and workload identities, least-privilege role assignments, a managed secret store, rotation and secret scanning. Use when building a Foundry or Azure AI solution, when keys appear in code or configuration, or when an agent's service identity has broad access.
license: CC-BY-4.0
metadata:
  department: ai-engineering
  lifecycle: Deliver, Assure, Improve
  maturity: builder, scaler, ai-enterprise
  risk-tiers: 1, 2, 3, 4
  platforms: ai-foundry, azure, entra, github
  edition-support: starter, scale, enterprise
  reviewers: security-privacy
  sources: ms-foundry-models, ms-agents-extensibility, ms-copilot-privacy
  status: draft
  authors: Simon Foote
---

# Secrets and identity

## Purpose

Custom AI solutions call models, search indexes, tools and business systems, and each call is made by some identity
with some permissions. When that identity is a shared key pasted into configuration, or a service principal with
broad rights, every user of the solution effectively holds those rights, and a prompt injection can use them. This
skill engineers identities and secrets so that each component authenticates without stored secrets where possible,
acts in the user's context where data is user-scoped, and holds only the permissions it needs. It goes wrong when keys
are used because they are quicker, and when a single identity is shared across environments and solutions.

## When to use

- A team is building a pro-code AI solution on Microsoft Foundry or Azure and setting up authentication.
- API keys or connection strings appear in code, configuration files, notebooks or pipeline variables.
- An agent or AI service runs under a service identity that can read or change far more than its users can.
- A secret has leaked, or a scan has found one in source history.
- Identities and role assignments need tidying before a solution moves to production.

## When not to use

- Designing the overall identity architecture for users, agents and services - use `ai-architecture:ai-identity-design`.
- The formal reviewer assessment of identity and access for an AI solution - use `security-privacy:ai-identity-and-access-review`.
- Connection ownership and service accounts for Power Automate flows - use `automation:automation-connector-governance`.
- Authentication design for Copilot Studio agents - use `copilot-studio:studio-authentication`.
- API authorisation rules within tool design - use `ai-engineering:ai-api-and-tooling`.

## Questions to ask first

1. Which components call which resources (models, indexes, storage, tools, business systems), and in which environments?
2. For each call, should it act as the signed-in user or as the solution, and why?
3. Which resources support keyless authentication with managed or workload identities, and which still need a secret?
4. What is the narrowest role that lets each identity do its job?
5. Who owns each identity and secret, and who renews or rotates them?

## Required inputs

- The solution architecture with components, resources and environments.
- The identity design from `ai-architecture:ai-identity-design`, or the organisation's identity standards.
- The data each resource holds and its sensitivity.
- The organisation's secret store and rotation standards, where they exist.

If the identity design is not settled, default to managed identities for service-to-service calls and on-behalf-of user
access for user-scoped data, and record open decisions with a named owner. Never default to shared keys.

## Decision framework

Choose the authentication pattern per call, preferring higher rows.

| Call | Preferred pattern | Acceptable when | Not acceptable |
|---|---|---|---|
| Solution to model endpoint, index, storage | Managed identity with keyless role-based access | Workload identity federation from a pipeline or external platform | Shared API keys in configuration |
| Solution to user-scoped data or tools | On-behalf-of the signed-in user, so permissions are trimmed to the user | Service identity with narrow, documented scope where the data is not user-scoped | Service identity broader than the users it serves |
| Pipeline to cloud resources | Workload identity federation, per environment | Service principal with certificate in a managed store | Long-lived secrets in pipeline variables |
| Third-party service without identity federation | Secret held in a managed secret store, accessed by managed identity, rotated | Short-lived tokens issued by a broker | Secrets in code, files or chat |
| Agent acting autonomously | Dedicated agent or workload identity with least privilege and an owner | Shared identity only for read-only, low-sensitivity resources | Reusing a person's account |

Separate identities per solution and per environment. A development identity never has access to production data.

## Practitioner approach

Draw the call map first: every component, every resource it calls, in every environment. For each arrow, ask who the
call should act as. This is the decision that matters most. A retrieval call over documents that users have different
access to should run in the user's context so results are permission-trimmed; a call to the model endpoint itself can
run as the solution.

Go keyless wherever the resource supports it. Assign a managed identity to the hosting compute and grant it a role on
the model deployment, the index and the storage it needs. Disable key-based access on resources where the platform
allows, so a leaked key is useless. For pipelines and workloads outside Azure, use workload identity federation instead
of stored client secrets.

Apply least privilege at role level. Prefer narrow data-plane roles over broad management roles, scope assignments to
the specific resource rather than the resource group or subscription, and avoid granting owner or contributor to
runtime identities. Review assignments before production and remove what is unused.

Handle user context carefully. On-behalf-of flows pass the user's identity through to downstream calls; check that every
tool and data source honours it, and that caching does not serve one user's results to another. Where an agent acts on
its own schedule without a user, give it a dedicated identity with an owner and the narrowest rights its tasks need,
and log every action.

Store what cannot be avoided in a managed secret store. Access it through managed identity, never copy values into
configuration, set expiry and rotation, and alert before expiry. Treat any secret that has appeared in source, logs,
tickets or chat as compromised: rotate it, then remove it from history.

Scan continuously. Enable secret scanning and push protection on repositories, scan pipeline logs and container images,
and fail the pipeline on findings. Record every identity and secret with its owner, purpose, scope and renewal date in a
register the operations team can use.

## Outputs

- A call map showing each component, resource, identity used and whether it acts as user or solution.
- Role assignments per identity and environment, with justification for anything broader than data-plane read.
- A secrets register: what remains a secret and why, store location, owner, rotation interval and expiry alert.
- Pipeline and repository settings for secret scanning and push protection.

## Microsoft platform considerations

Microsoft Entra managed identities, workload identity federation, role-based access on Azure and Foundry resources, Azure
Key Vault and keyless access to model endpoints are the usual building blocks; agent identity capabilities for Microsoft
agents are evolving. Supported authentication modes differ by resource and change, so check current behaviour in
`references/sources.md` and record what was confirmed for each resource.

## Adoption considerations

Engineers use keys because the first example they found did. Provide starter code and templates that use managed
identities from the first line, and show how to run locally with developer credentials so nobody needs a key on their
machine.

## Knowledge considerations

Not applicable to knowledge content itself. Permission-trimmed retrieval depends on the identity design here, so tell
knowledge owners whether their content is accessed in the user's context or the solution's.

## Security and privacy considerations

This skill is the engineering control set for identities and secrets; its evidence goes to
`security-privacy:ai-identity-and-access-review`. Over-privileged runtime identities and stored keys are among the most
exploited weaknesses in AI solutions, because prompt injection can direct a solution to use whatever access it holds.

## Responsible AI considerations

Actions taken by agents under their own identity must be attributable: log which identity acted, on whose request and
with what result, so accountability is not lost when software acts.

## Evaluation requirements

Test that permission trimming works: run the same request as users with different access and confirm they see different
results. Test that development identities cannot reach production, and that disabled keys are rejected.

## Value measures

Track, across solutions, the share of calls using keyless authentication, secrets past rotation date, runtime identities
with broad roles and secret scanning findings. The AI engineering lead and security lead own these jointly.

## Scale notes

### Starter

Use managed identities for model and storage access, a managed secret store for anything else, secret scanning on the
repository and separate identities for development and production.

### Scale

Standardise identity patterns in templates, disable key access on AI resources by policy, run access reviews of runtime
identities, and keep a shared secrets register.

### Enterprise

Enforce keyless access and least privilege through platform policy, manage agent identities as a governed population with
owners and reviews, and monitor estate-wide for over-privileged identities and secret exposure.

## Hand-offs

- To `security-privacy:ai-identity-and-access-review` with the call map, role assignments and secrets register.
- To `ai-engineering:ai-ci-cd` for pipeline workload identities.
- To `ai-engineering:ai-api-and-tooling` for user-context authorisation in tools.
- To `ai-architecture:ai-identity-design` where architectural identity decisions need revisiting.

## Reviewer gates

From risk tier 2, `security-privacy` reviews identities and secrets. Shared keys for model access in production, runtime
identities with access beyond their users for user-scoped data, and secrets in source are blocking findings.

## Failure modes

- A model key is committed to a repository, removed in the next commit and remains valid for months.
- A retrieval service runs as a broad service identity, so every user can find documents they could not otherwise open.
- One identity serves development and production, and a test script changes live data.
- An agent identity is created for a pilot, granted wide rights for convenience and never reviewed.

## Sources

`references/sources.md` in this skill lists the source records behind this skill, what each is authoritative for, how volatile it is and what you may do with it. Product availability, licensing, limits and preview status change often, so check the current source before stating them, and cite what you used.

## Never

- Put keys, secrets or connection strings in code, configuration files, notebooks, tickets or chat.
- Give a runtime identity wider access to user-scoped data than the users it serves.
- Share an identity between development and production.
- Leave a leaked secret unrotated because it was removed from the latest commit.
