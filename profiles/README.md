# Organisation profiles

An organisation profile is a structured statement of the context CopilotForge needs to tailor its advice: size, sector,
regulatory context, Microsoft estate, current AI use, knowledge, governance, adoption, delivery capability, portfolio
and constraints (design brief section 9). It is YAML, validated against [`schema.json`](schema.json).

- Capture only what tailoring needs. Use roles and aliases, never personal names or personal data.
- Real profiles never belong in this repository. Keep them in your own OneDrive or a private project location, or in the
  git-ignored `input/` folder of a local clone.
- Files in [`samples/`](samples/) are fictional, carry `fictional: true`, and are checked by `scripts/check-profiles.py`.

## Try it

```
python3 scripts/tailor.py profiles/samples/larkfield-services-scale.yaml
```

prints the deterministic tailoring plan: edition, assurance overlay, maturity archetype, emerging signals, programmes,
artefacts with the responsible skill and template, reviewer gates, ownership map and the facts still to confirm. The
expected plans for each sample are kept in [`../evaluations/golden/`](../evaluations/golden/).

| Sample | Fictional organisation | Purpose |
|---|---|---|
| `larkfield-services-scale.yaml` | 600-person UK facilities services company | The v1 acceptance organisation (brief section 17.2) |
| `ashby-studio-starter.yaml` | 40-person UK design practice | The proportionality contrast for the same request |
