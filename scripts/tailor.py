#!/usr/bin/env python3
"""Turn an organisation profile into a deterministic tailoring plan (design brief section 9.3).

    python3 scripts/tailor.py profiles/samples/<file>.yaml            # print the plan as YAML
    python3 scripts/tailor.py <profile> --out <plan.yaml>             # write it

The plan is the spine of a transformation pack: recommended edition, assurance overlay and maturity archetype (each
with the rule that produced it), emerging signals, the programmes and artefacts to produce at what depth, the skill and
template responsible for each artefact, reviewer gates, a role-based ownership map, and the facts the profile did not
supply. The organisation-tailoring skills write the documents themselves; this script makes the decisions repeatable
and testable (golden-output tests in evaluations/golden/). It never invents facts: anything missing is listed under
to_confirm.
"""
import os, sys
from _common import (load_yaml, load_schema, validate_schema, programmes, editions, archetypes, department_index,
                     ARCHETYPES, path, rel, yaml)

RULES = path("data", "tailoring-rules.yaml")


def get(profile, dotted):
    cur = profile
    for part in dotted.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur


def holds(profile, cond):
    v = get(profile, cond["field"])
    op, target = cond["op"], cond["value"]
    if v is None:
        return False
    if op == "==": return v == target
    if op == "!=": return v != target
    if op == "in": return v in target
    if op == ">=": return v >= target
    if op == ">": return v > target
    if op == "<": return v < target
    if op == "<=": return v <= target
    raise ValueError(f"unknown operator {op}")


def matches(profile, rule):
    if "any_of" in rule:
        return any(holds(profile, c) for c in rule["any_of"])
    return all(holds(profile, c) for c in rule.get("all_of", []))


def first(profile, rules):
    for r in rules:
        if matches(profile, r):
            return r
    raise SystemExit("no rule matched; the last rule in each list must be a default")


def condition(when, ctx):
    if not when:
        return True
    tests = []
    for c in when.get("any_of", []):
        if "signal" in c:
            tests.append(c["signal"] in ctx["signals"])
        elif "archetype_at_least" in c:
            tests.append(ARCHETYPES.index(ctx["archetype"]) >= ARCHETYPES.index(c["archetype_at_least"]))
        elif "edition_in" in c:
            tests.append(ctx["edition"] in c["edition_in"])
    return any(tests)


OPTIONAL_FACTS = [
    "organisation.executive_sponsor", "organisation.target_outcomes", "organisation.maturity_target",
    "people.personas", "knowledge.ownership_model", "knowledge.quality", "data.sensitivity",
    "governance.security", "governance.privacy", "governance.responsible_ai", "adoption.measurement",
    "portfolio.candidate_opportunities", "constraints.budget", "constraints.timeline", "constraints.capacity",
]


def plan(profile_path):
    profile = load_yaml(profile_path)
    errors = validate_schema(profile, load_schema_profile())
    if errors:
        return None, errors
    rules = load_yaml(RULES)
    ed = first(profile, rules["edition_rules"])
    ov = first(profile, rules["assurance_overlay_rules"])
    ar = first(profile, rules["archetype_rules"])
    sigs = [s for s in rules["signal_rules"] if matches(profile, s)]
    ctx = {"edition": ed["edition"], "archetype": ar["archetype"], "signals": [s["signal"] for s in sigs]}

    progs = programmes()
    top = progs["ai-transformation"]
    chosen = ["ai-transformation"] + [i["programme"] for i in top["includes"] if condition(i.get("when"), ctx)]
    artefacts, gates = [], {}
    depts = department_index()
    for pid in chosen:
        p = progs[pid]
        for a in p.get("artefacts", []):
            depth = a["depth"][ctx["edition"]]
            if depth == "omit":
                continue
            artefacts.append({"programme": pid, "artefact": a["id"], "title": a["title"], "depth": depth,
                              "stage": a["stage"], "skill": a["skill"], "template": a["template"]})
        for g in p.get("gates", []):
            key = (g["reviewer"], g["stage"])
            if key not in gates:
                status = depts[g["reviewer"]]["status"]
                gates[key] = {"reviewer": g["reviewer"], "stage": g["stage"], "from_risk_tier": g["from_risk_tier"],
                              "blocking": g["blocking"],
                              "evidence": "formal" if ov["overlay"] == "formal" else "proportionate",
                              "reviewer_status": "active" if status == "active" else "contract-only (department planned)"}
    order = {s: i for i, s in enumerate(top["lifecycle"])}
    artefacts.sort(key=lambda a: (order[a["stage"]], a["programme"], a["artefact"]))
    engaged = sorted({a["skill"].split(":")[0] for a in artefacts} | {g["reviewer"] for g in gates.values()})
    ownership = [{"department": d, "accountable_role": depts[d]["lead_role"],
                  "named_owner": "to confirm from declared roles"} for d in engaged]
    sub = top.get("starter_substitutions", {}) if ctx["edition"] == "starter" else {}
    out = {
        "profile": rel(os.path.abspath(profile_path)) if os.path.abspath(profile_path).startswith(path("")) else os.path.basename(profile_path),
        "organisation": get(profile, "organisation.name"),
        "fictional": bool(profile.get("fictional")),
        "edition": {"id": ed["edition"], "rule": ed["id"], "rationale": ed["rationale"],
                    "coe_form": editions()[ed["edition"]]["coe_form"],
                    "champions_form": editions()[ed["edition"]]["champions_form"],
                    "governance_form": editions()[ed["edition"]]["governance_form"]},
        "assurance_overlay": {"id": ov["overlay"], "rule": ov["id"], "rationale": ov["rationale"]},
        "archetype": {"id": ar["archetype"], "rule": ar["id"], "rationale": ar["rationale"],
                      "output_emphasis": archetypes()[ar["archetype"]]["output_emphasis"]},
        "emerging_signals": [{"signal": s["signal"], "rule": s["id"], "note": s["note"]} for s in sigs],
        "programmes": chosen,
        "substitutions": sub,
        "artefacts": artefacts,
        "reviewer_gates": sorted(gates.values(), key=lambda g: (order[g["stage"]], g["reviewer"])),
        "ownership_map": ownership,
        "to_confirm": [f for f in OPTIONAL_FACTS if get(profile, f) in (None, [], "")],
    }
    return out, []


def load_schema_profile():
    import json
    with open(path("profiles", "schema.json"), encoding="utf-8") as f:
        return json.load(f)


def dump(data):
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=120)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__); sys.exit(2)
    result, errors = plan(args[0])
    if errors:
        print("Profile is not valid against profiles/schema.json:")
        for e in errors: print("  -", e)
        sys.exit(1)
    text = "# Tailoring plan generated by scripts/tailor.py. Do not edit by hand.\n" + dump(result)
    if "--out" in sys.argv:
        open(sys.argv[sys.argv.index("--out") + 1], "w", encoding="utf-8").write(text)
    else:
        print(text, end="")
