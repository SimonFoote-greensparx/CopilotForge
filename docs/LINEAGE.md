# Lineage

CopilotForge is a successor *pattern* to D365Forge, not a fork or a new version of it.

| | D365Forge | CopilotForge |
|---|---|---|
| Models | The team that delivers Dynamics 365 Customer Engagement | The organisation that transforms a business with Microsoft AI |
| Repository | https://github.com/SimonFoote-greensparx/D365Forge | https://github.com/SimonFoote-greensparx/CopilotForge |
| Website | https://d365forge.ai/ | https://copilotforge.ai/ |
| Plugins | Department names | `copilotforge-<department>` |

## What CopilotForge keeps from D365Forge

The engineering model: departments as independently installable plugins, skills with explicit scope and triggers,
reviewer-class departments that can block, a structured source catalogue, generated manifests and Cowork archives,
organisation profiles with a tailoring engine, edition overlays, and one local check command shared with CI.

## What is different

- The organisation modelled, and therefore every department, skill, programme and template.
- A full section anatomy from the CopilotForge design brief, including adoption, knowledge, security, responsible AI,
  evaluation and value sections in every skill.
- Three editions (Starter, Scale, Enterprise), five maturity archetypes and progressive risk tiers.
- Programmes as first-class orchestration units with blocking gates that cannot be skipped.
- Structured source records with volatility and review intervals.
- Deterministic tailoring plans with golden-output tests.

## Separation rules

- No D365Forge content (skills, templates, programmes, documentation) is copied into this repository, and no CopilotForge
  change is ever made in D365Forge. Some build tooling (for example the Markdown renderer, Cowork packager and website
  builders) is adapted from the same author's MIT-licensed D365Forge scripts and maintained independently here.
- CopilotForge skill and plugin names never reuse D365Forge names (`data/reserved-names.toml`, decision D9).
- Each project has its own maintainer skills in Copilot Cowork.
