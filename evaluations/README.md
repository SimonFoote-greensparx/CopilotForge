# Evaluations

- `golden/*.plan.yaml` - the reviewed tailoring plan for each fictional sample profile. `scripts/check-profiles.py`
  fails if `scripts/tailor.py` would now produce anything different, so a change to rules, programmes or editions is
  always visible. After reviewing a difference, regenerate with `python3 scripts/check-profiles.py --update`.
- `acceptance.yaml` - the v1 acceptance assertions: the 600-person golden scenario and the 40-person contrast, which
  must land in different editions with a materially smaller pack.

Golden *document* packs (the Word and Excel outputs a runtime writes) are added in phase 1 as worked examples in
`examples/`.
