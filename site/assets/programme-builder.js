/* CopilotForge programme builder. Hand-written. Runs entirely in the browser: nothing is sent anywhere.
   The form is generated from the profile schema embedded in the page; the recommendation applies the same rules as
   scripts/tailor.py (data/tailoring-rules.yaml), and scripts/check-programme-builder.py proves the two agree. */
(function () {
  "use strict";

  // ------------------------------------------------------------------ rules (mirror of scripts/tailor.py)
  function get(obj, dotted) {
    let cur = obj;
    for (const part of dotted.split(".")) {
      if (cur === null || typeof cur !== "object" || !(part in cur)) return undefined;
      cur = cur[part];
    }
    return cur;
  }
  function holds(profile, c) {
    const v = get(profile, c.field);
    if (v === undefined || v === null) return false;
    switch (c.op) {
      case "==": return v === c.value;
      case "!=": return v !== c.value;
      case "in": return c.value.indexOf(v) !== -1;
      case ">=": return v >= c.value;
      case ">": return v > c.value;
      case "<": return v < c.value;
      case "<=": return v <= c.value;
    }
    throw new Error("unknown operator " + c.op);
  }
  function matches(profile, rule) {
    if (rule.any_of) return rule.any_of.some(c => holds(profile, c));
    return (rule.all_of || []).every(c => holds(profile, c));
  }
  function first(profile, rules) {
    for (const r of rules) if (matches(profile, r)) return r;
    throw new Error("no rule matched");
  }
  function condition(when, ctx, order) {
    if (!when) return true;
    return (when.any_of || []).some(c => {
      if (c.signal) return ctx.signals.indexOf(c.signal) !== -1;
      if (c.archetype_at_least) return order.indexOf(ctx.archetype) >= order.indexOf(c.archetype_at_least);
      if (c.edition_in) return c.edition_in.indexOf(ctx.edition) !== -1;
      return false;
    });
  }
  function plan(profile, D) {
    const R = D.rules;
    const ed = first(profile, R.edition_rules), ov = first(profile, R.assurance_overlay_rules), ar = first(profile, R.archetype_rules);
    const sigs = R.signal_rules.filter(s => matches(profile, s));
    const ctx = { edition: ed.edition, archetype: ar.archetype, signals: sigs.map(s => s.signal) };
    const top = D.programmes["ai-transformation"];
    const chosen = ["ai-transformation"].concat(top.includes.filter(i => condition(i.when, ctx, D.archetype_order)).map(i => i.programme));
    const artefacts = [], gates = {};
    for (const pid of chosen) {
      const p = D.programmes[pid];
      for (const a of p.artefacts || []) {
        const depth = a.depth[ctx.edition];
        if (depth === "omit") continue;
        artefacts.push({ programme: pid, artefact: a.id, title: a.title, depth: depth, stage: a.stage, skill: a.skill, template: a.template });
      }
      for (const g of p.gates || []) {
        const key = g.reviewer + "|" + g.stage;
        if (!(key in gates)) gates[key] = { reviewer: g.reviewer, stage: g.stage, from_risk_tier: g.from_risk_tier,
          active: D.departments[g.reviewer].status === "active" };
      }
    }
    const order = {}; top.lifecycle.forEach((s, i) => { order[s] = i; });
    artefacts.sort((a, b) => (order[a.stage] - order[b.stage]) || a.programme.localeCompare(b.programme) || a.artefact.localeCompare(b.artefact));
    const gateList = Object.values(gates).sort((a, b) => (order[a.stage] - order[b.stage]) || a.reviewer.localeCompare(b.reviewer));
    const toConfirm = D.optional_facts.filter(f => { const v = get(profile, f); return v === undefined || v === null || v === "" || (Array.isArray(v) && !v.length); });
    return { edition: ed, overlay: ov, archetype: ar, signals: sigs, programmes: chosen, artefacts: artefacts, gates: gateList, toConfirm: toConfirm };
  }

  // ------------------------------------------------------------------ schema subset validator (mirror of _common.py)
  function typeOk(v, t) {
    if (t === "null") return v === null;
    if (t === "object") return v !== null && typeof v === "object" && !Array.isArray(v);
    if (t === "array") return Array.isArray(v);
    if (t === "string") return typeof v === "string";
    if (t === "integer") return Number.isInteger(v);
    if (t === "number") return typeof v === "number";
    if (t === "boolean") return typeof v === "boolean";
    return true;
  }
  function validate(v, s, where) {
    where = where || "$";
    let errs = [];
    if (s.type) {
      const ts = Array.isArray(s.type) ? s.type : [s.type];
      if (!ts.some(t => typeOk(v, t))) return [where + ": expected " + ts.join(" or ")];
    }
    if (s.enum && s.enum.indexOf(v) === -1) errs.push(where + ": must be one of " + s.enum.join(", "));
    if (typeof v === "number" && s.minimum !== undefined && v < s.minimum) errs.push(where + ": below " + s.minimum);
    if (v && typeof v === "object" && !Array.isArray(v)) {
      for (const r of s.required || []) if (!(r in v)) errs.push(where + ": missing " + r);
      for (const k of Object.keys(v)) {
        if (s.properties && k in s.properties) errs = errs.concat(validate(v[k], s.properties[k], where + "." + k));
        else if (s.additionalProperties === false) errs.push(where + ": unexpected " + k);
      }
    }
    if (Array.isArray(v)) {
      if (s.minItems !== undefined && v.length < s.minItems) errs.push(where + ": needs at least " + s.minItems + " item(s)");
      if (s.items) v.forEach((x, i) => { errs = errs.concat(validate(x, s.items, where + "[" + i + "]")); });
    }
    return errs;
  }

  // ------------------------------------------------------------------ YAML writer (block style, quoted where needed)
  function scalar(v) {
    if (typeof v === "number" || typeof v === "boolean") return String(v);
    const s = String(v);
    if (s === "" || /^[\s-?:,\[\]{}#&*!|>'"%@`]|[:#]\s|\s$|^(true|false|yes|no|null|~|[0-9.+-]+)$/i.test(s)) return JSON.stringify(s);
    return s;
  }
  function toYaml(v, indent) {
    indent = indent || "";
    let out = "";
    for (const k of Object.keys(v)) {
      const x = v[k];
      if (Array.isArray(x)) {
        out += indent + k + ":\n";
        for (const item of x) {
          if (item && typeof item === "object") {
            const keys = Object.keys(item);
            keys.forEach((ik, i) => { out += indent + (i === 0 ? "  - " : "    ") + ik + ": " + scalar(item[ik]) + "\n"; });
          } else out += indent + "  - " + scalar(item) + "\n";
        }
      } else if (x && typeof x === "object") {
        out += indent + k + ":\n" + toYaml(x, indent + "  ");
      } else out += indent + k + ": " + scalar(x) + "\n";
    }
    return out;
  }

  if (typeof module !== "undefined") module.exports = { plan: plan, validate: validate, toYaml: toYaml };
  if (typeof document === "undefined") return;

  // ------------------------------------------------------------------ the page
  const D = JSON.parse(document.getElementById("builder-data").textContent);
  const S = D.schema, form = document.getElementById("f");
  const fields = [];
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const label = k => k.replace(/_/g, " ").replace(/^m365/, "Microsoft 365").replace(/^./, c => c.toUpperCase());

  function control(pathStr, s, required) {
    const id = "f_" + pathStr.replace(/\./g, "__");
    const req = required ? ' <span aria-hidden="true">*</span>' : "";
    const hint = s.description ? '<span class="meta">' + esc(s.description) + "</span>" : "";
    const name = label(pathStr.split(".").pop());
    let html;
    if (s.type === "string" && s.enum) {
      html = '<select id="' + id + '"><option value="">Not stated</option>' + s.enum.map(o => "<option>" + esc(o) + "</option>").join("") + "</select>";
    } else if (s.type === "boolean") {
      html = '<select id="' + id + '"><option value="">Not stated</option><option value="true">Yes</option><option value="false">No</option></select>';
    } else if (s.type === "integer") {
      html = '<input type="number" min="' + (s.minimum || 0) + '" id="' + id + '">';
    } else if (s.type === "array" && s.items && s.items.type === "object") {
      const cols = Object.keys(s.items.properties);
      html = '<textarea rows="3" id="' + id + '" placeholder="One per line: ' + esc(cols.join(" | ")) + '"></textarea>';
    } else if (s.type === "array") {
      html = '<textarea rows="2" id="' + id + '" placeholder="One per line"></textarea>';
    } else {
      html = '<input type="text" id="' + id + '">';
    }
    fields.push({ path: pathStr, schema: s, id: id });
    return '<div><label for="' + id + '">' + esc(name) + req + "</label>" + html + hint + "</div>";
  }
  function group(prefix, s) {
    let simple = "", nested = "";
    for (const k of Object.keys(s.properties)) {
      const sub = s.properties[k], p = prefix ? prefix + "." + k : k;
      const req = (s.required || []).indexOf(k) !== -1;
      if (sub.type === "object" && sub.properties) nested += "<h3>" + esc(label(k)) + (req ? " *" : "") + "</h3>" + group(p, sub);
      else simple += control(p, sub, req);
    }
    return '<div class="row">' + simple + "</div>" + nested;
  }
  let html = "";
  for (const k of Object.keys(S.properties)) {
    if (k === "profile_version" || k === "fictional") continue;
    const s = S.properties[k], req = (S.required || []).indexOf(k) !== -1;
    html += "<fieldset><legend>" + esc(label(k)) + (req ? " *" : "") + "</legend>" + group(k, s) + "</fieldset>";
  }
  form.innerHTML = '<p class="meta">Fields marked * are required. Leave anything you do not know as "Not stated"; it is listed as a fact to confirm rather than guessed.</p>' + html;

  function setPath(obj, dotted, value) {
    const parts = dotted.split(".");
    let cur = obj;
    for (let i = 0; i < parts.length - 1; i++) { cur[parts[i]] = cur[parts[i]] || {}; cur = cur[parts[i]]; }
    cur[parts[parts.length - 1]] = value;
  }
  function read() {
    const out = { profile_version: "1.0" };
    for (const f of fields) {
      const el = document.getElementById(f.id), raw = el.value.trim(), s = f.schema;
      if (raw === "") continue;
      let v;
      if (s.type === "integer") v = parseInt(raw, 10);
      else if (s.type === "boolean") v = raw === "true";
      else if (s.type === "array" && s.items && s.items.type === "object") {
        const cols = Object.keys(s.items.properties);
        v = raw.split("\n").map(l => l.trim()).filter(Boolean).map(l => {
          const parts = l.split("|").map(x => x.trim()), o = {};
          cols.forEach((c, i) => { if (parts[i]) o[c] = s.items.properties[c].type === "integer" ? parseInt(parts[i], 10) : parts[i]; });
          return o;
        });
      } else if (s.type === "array") v = raw.split("\n").map(l => l.trim()).filter(Boolean);
      else v = raw;
      if (Number.isNaN(v)) continue;
      setPath(out, f.path, v);
    }
    return out;
  }
  function fill(profile) {
    for (const f of fields) {
      const el = document.getElementById(f.id), v = get(profile, f.path), s = f.schema;
      if (v === undefined) { el.value = ""; continue; }
      if (s.type === "array" && s.items && s.items.type === "object") {
        const cols = Object.keys(s.items.properties);
        el.value = v.map(o => cols.map(c => o[c] === undefined ? "" : o[c]).join(" | ")).join("\n");
      } else if (Array.isArray(v)) el.value = v.join("\n");
      else el.value = String(v);
    }
  }
  const rec = document.getElementById("rec"), status = document.getElementById("status"), yaml = document.getElementById("yaml");
  function render() {
    const profile = read();
    const errs = validate(profile, S);
    yaml.value = "# CopilotForge organisation profile. Created in the programme builder; keep it in your own storage.\n" + toYaml(profile);
    if (errs.length) {
      status.innerHTML = '<div class="check-warnings"><strong>Still needed:</strong><ul>' + errs.slice(0, 8).map(x => "<li>" + esc(x.replace(/^\$\.?/, "").replace(/^: /, "")) + "</li>").join("") + "</ul></div>";
      rec.innerHTML = '<h2>Recommendation</h2><p class="meta">Complete the required fields to see a recommendation.</p>';
      return;
    }
    status.innerHTML = '<div class="check-ok">The profile is valid.</div>';
    const p = plan(profile, D);
    const ed = D.editions[p.edition.edition], ar = D.archetypes[p.archetype.archetype];
    const progTitles = p.programmes.map(id => esc(D.programmes[id].title));
    rec.innerHTML = "<h2>Recommendation</h2><dl>" +
      "<dt>Edition</dt><dd><strong>" + esc(ed.title) + '</strong><div class="why">' + esc(p.edition.rationale) + " (rule " + esc(p.edition.id) + ")</div></dd>" +
      "<dt>Archetype</dt><dd><strong>" + esc(ar.title) + '</strong><div class="why">' + esc(p.archetype.rationale) + " (rule " + esc(p.archetype.id) + ")</div></dd>" +
      "<dt>Assurance</dt><dd>" + esc(p.overlay.overlay) + "</dd>" +
      "<dt>CoE form</dt><dd>" + esc(ed.coe_form) + "</dd></dl>" +
      (p.signals.length ? "<p><strong>Signals</strong></p><ul>" + p.signals.map(s => "<li>" + esc(s.note) + "</li>").join("") + "</ul>" : "") +
      "<p><strong>Programmes</strong></p><ul>" + progTitles.map(t => "<li>" + t + "</li>").join("") + "</ul>" +
      "<p><strong>" + p.artefacts.length + " artefacts</strong> in the pack, and " + p.gates.length + " reviewer gate(s).</p>" +
      (p.toConfirm.length ? '<p class="why">' + p.toConfirm.length + " fact(s) to confirm before the pack is written.</p>" : "");
  }
  form.addEventListener("input", render);
  form.addEventListener("change", render);
  document.getElementById("load-sample").addEventListener("click", () => { fill(D.sample); render(); });
  document.getElementById("clear").addEventListener("click", () => { fill({}); render(); });
  document.getElementById("copy").addEventListener("click", () => { navigator.clipboard && navigator.clipboard.writeText(yaml.value); });
  document.getElementById("dl").addEventListener("click", () => {
    const blob = new Blob([yaml.value], { type: "text/yaml" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "organisation-profile.yaml";
    a.click();
    setTimeout(() => URL.revokeObjectURL(a.href), 1000);
  });
  render();
})();
