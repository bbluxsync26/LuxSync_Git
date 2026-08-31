import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const modulesDir = path.join(here, 'modules');
const read = name => JSON.parse(fs.readFileSync(path.join(modulesDir, name), 'utf8'));

const questionnaire = fs.readdirSync(modulesDir)
  .filter(name => /^2\d-.*\.json$/.test(name))
  .sort()
  .map(read);

const scoringRules = fs.readdirSync(modulesDir)
  .filter(name => /^3[0-4]-scoring-rules\.json$/.test(name))
  .sort()
  .flatMap(read);

const engine = {
  meta: read('00-meta.json'),
  constants: read('01-constants.json'),
  experience_catalog: read('10-experiences.json'),
  questionnaire,
  scoring: {
    rules: scoringRules,
    context_bonuses: read('35-context-bonuses.json')
  },
  compatibility: read('40-compatibility.json'),
  foundation_logic: read('41-foundation.json'),
  implementation_paths: read('50-implementation-paths.json'),
  implementation_path_rules: read('51-implementation-path-rules.json'),
  roadmap: read('52-roadmap.json'),
  consultation_triggers: read('60-consultation-triggers.json'),
  cta_logic: read('61-cta-logic.json'),
  routing: read('62-routing.json'),
  blueprint_schema: read('63-blueprint-schema.json'),
  state_models: read('70-state-models.json'),
  analytics_events: read('71-analytics-events.json')
};

const output = path.join(here, 'luxsync-concierge-engine.v1.json');
fs.writeFileSync(output, JSON.stringify(engine, null, 2) + '\n', 'utf8');
console.log(`Built ${output}`);
