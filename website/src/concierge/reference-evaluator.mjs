import fs from 'node:fs';

export function loadEngine(path) {
  return JSON.parse(fs.readFileSync(path, 'utf8'));
}

function values(answer) {
  if (answer === undefined || answer === null) return [];
  return Array.isArray(answer) ? answer : [answer];
}

function matchesWhen(profile, when = {}) {
  return Object.entries(when).every(([field, expected]) => {
    const actual = values(profile[field]);
    return expected.some(v => actual.includes(v));
  });
}

function matchesNumeric(profile, spec = {}) {
  return Object.entries(spec).every(([field, ops]) => {
    const actual = Number(profile[field]);
    if (!Number.isFinite(actual)) return false;
    if (ops.gte !== undefined && !(actual >= ops.gte)) return false;
    if (ops.gt !== undefined && !(actual > ops.gt)) return false;
    if (ops.lte !== undefined && !(actual <= ops.lte)) return false;
    if (ops.lt !== undefined && !(actual < ops.lt)) return false;
    if (ops.eq !== undefined && !(actual === ops.eq)) return false;
    return true;
  });
}

function matchesBand(profile, spec = {}) {
  return Object.entries(spec).every(([field, expected]) => expected.includes(profile[field]));
}

function ruleMatches(profile, rule) {
  if (rule.when && !matchesWhen(profile, rule.when)) return false;
  if (rule.when_numeric && !matchesNumeric(profile, rule.when_numeric)) return false;
  if (rule.when_band && !matchesBand(profile, rule.when_band)) return false;
  return Boolean(rule.when || rule.when_numeric || rule.when_band);
}

function bonusMatches(profile, bonus) {
  const c = bonus?.condition?.count_selected;
  if (!c) return false;
  const selected = values(profile[c.field]).filter(v => !(c.exclude || []).includes(v));
  if (c.gte !== undefined && selected.length < c.gte) return false;
  if (c.gt !== undefined && selected.length <= c.gt) return false;
  return true;
}

function resolveFoundation(engine, profile, derived) {
  if (derived.foundation) {
    const labels = {
      compatibility_review: 'Compatibility Review',
      existing_smartthings_foundation: 'Existing SmartThings Foundation',
      smartthings_foundation_recommended: 'SmartThings Foundation Recommended',
      light_foundation: 'Light Foundation'
    };
    return { id: derived.foundation, label: labels[derived.foundation] || derived.foundation };
  }
  const tech = values(profile.technology_profile);
  if (profile.current_setup_health === 'fragmented' || tech.includes('unknown_mix'))
    return { id: 'compatibility_review', label: 'Compatibility Review' };
  if (tech.includes('smartthings'))
    return { id: 'existing_smartthings_foundation', label: 'Existing SmartThings Foundation' };
  if (tech.includes('nothing_yet'))
    return { id: 'smartthings_foundation_recommended', label: 'SmartThings Foundation Recommended' };
  return { id: 'light_foundation', label: 'Light Foundation' };
}

function resolveImplementationPath(engine, profile, flags, ranked) {
  const pref = profile.implementation_preference;
  let id = pref === 'focused' ? 'essential_intelligence'
    : (pref === 'comprehensive' || pref === 'ideal') ? 'complete_luxsync'
    : pref === 'phased' ? 'elevated_living'
    : ranked.length >= 8 ? 'complete_luxsync'
    : ranked.length >= 5 ? 'elevated_living'
    : 'essential_intelligence';

  if (flags.has('large_property') && id === 'essential_intelligence') id = 'elevated_living';
  return { id, ...engine.implementation_paths[id] };
}

function resolveCTA(engine, profile, flags) {
  const sorted = [...engine.cta_logic].sort((a,b) => b.priority - a.priority);
  for (const rule of sorted) {
    if (rule.default) return rule.cta;
    if (rule.when && matchesWhen(profile, rule.when)) return rule.cta;
    if (rule.when_flag && flags.has(rule.when_flag)) return rule.cta;
    if (rule.when_any_flag && rule.when_any_flag.some(f => flags.has(f))) return rule.cta;
  }
  return { id: 'build_solution', label: 'Build My Solution' };
}

function tierFor(score, thresholds) {
  if (score >= thresholds.primary) return 'primary';
  if (score >= thresholds.strong) return 'strong';
  if (score >= thresholds.optional) return 'optional';
  return 'suppressed';
}

export function evaluate(engine, profile) {
  const scores = Object.fromEntries(engine.experience_catalog.map(e => [e.id, 0]));
  const flags = new Set();
  const derived = {};

  for (const rule of engine.scoring.rules) {
    if (!ruleMatches(profile, rule)) continue;
    for (const [id, points] of Object.entries(rule.add || {})) scores[id] += points;
    for (const flag of rule.flags || []) flags.add(flag);
    Object.assign(derived, rule.adjustments || {});
  }

  for (const bonus of engine.scoring.context_bonuses || []) {
    if (!bonusMatches(profile, bonus)) continue;
    for (const [id, points] of Object.entries(bonus.add || {})) scores[id] += points;
  }

  // Optional direct Experience priority multiplier support.
  // priority_rank may contain Experience IDs in this reference implementation.
  const priorityRank = values(profile.priority_rank).slice(0,3);
  const mult = [engine.constants.priority_multipliers.priority_1, engine.constants.priority_multipliers.priority_2, engine.constants.priority_multipliers.priority_3];
  priorityRank.forEach((id, i) => {
    if (scores[id] !== undefined) scores[id] = Math.round(scores[id] * mult[i] * 100) / 100;
  });

  const catalog = Object.fromEntries(engine.experience_catalog.map(e => [e.id, e]));
  let ranked = Object.entries(scores)
    .map(([id, score]) => ({ id, name: catalog[id].name, score, tier: tierFor(score, engine.constants.recommendation_thresholds) }))
    .filter(x => x.score >= engine.constants.recommendation_thresholds.suppress_below)
    .sort((a,b) => b.score - a.score || a.name.localeCompare(b.name));

  const min = engine.constants.minimum_recommended_experiences;
  if (ranked.length < min) {
    const remaining = Object.entries(scores)
      .filter(([id]) => !ranked.some(r => r.id === id))
      .map(([id, score]) => ({id, name: catalog[id].name, score, tier: 'optional'}))
      .sort((a,b) => b.score - a.score)
      .slice(0, min - ranked.length);
    ranked = ranked.concat(remaining);
  }

  const foundation = resolveFoundation(engine, profile, derived);
  const path = resolveImplementationPath(engine, profile, flags, ranked);
  const cta = resolveCTA(engine, profile, flags);

  return {
    flags: [...flags].sort(),
    recommended_foundation: foundation,
    recommended_experiences: ranked.filter(r => ['primary','strong'].includes(r.tier)),
    optional_experiences: ranked.filter(r => r.tier === 'optional'),
    implementation_path: path,
    next_best_action: cta,
    all_scores: scores
  };
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const [enginePath, profilePath] = process.argv.slice(2);
  if (!enginePath || !profilePath) {
    console.error('Usage: node reference-evaluator.mjs <engine.json> <profile.json>');
    process.exit(1);
  }
  const engine = loadEngine(enginePath);
  const profile = JSON.parse(fs.readFileSync(profilePath, 'utf8'));
  console.log(JSON.stringify(evaluate(engine, profile), null, 2));
}
