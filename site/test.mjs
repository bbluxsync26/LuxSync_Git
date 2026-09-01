import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(HERE, '..');
const DIST = path.join(HERE, 'dist');
const manifest = JSON.parse(fs.readFileSync(path.join(ROOT, 'website', 'implementation-manifest.json'), 'utf8'));
const approvedColors = new Set(['#0D1526', '#172036', '#D0BEB0', '#9E8B85', '#967878', '#7B96B2', '#D6B0A0']);
const retired = 'Smart Living' + '. ' + 'Elevated' + '.';
const errors = [];

function hash(file) {
  return crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
}

for (const item of manifest.routes) {
  const dir = item.route === '/' ? DIST : path.join(DIST, item.route.replace(/^\//, '').replace(/\/$/, ''));
  const file = path.join(dir, 'index.html');
  if (!fs.existsSync(file)) errors.push(`Missing built route ${item.route}`);
  else {
    const html = fs.readFileSync(file, 'utf8');
    if (!html.includes('Where Luxury Lives Intelligently')) errors.push(`${item.route}: official slogan missing`);
    if (html.includes(retired)) errors.push(`${item.route}: retired slogan present`);
    if (/brand\/assets\/(?!01-logos)/.test(html)) errors.push(`${item.route}: reference-only brand asset wired directly`);
    if (/\.svg(?:["'?#]|$)/i.test(html)) errors.push(`${item.route}: SVG asset reference remains active`);
  }
}

const css = fs.readFileSync(path.join(DIST, 'styles.css'), 'utf8');
for (const match of css.matchAll(/#[0-9A-Fa-f]{6}/g)) {
  const color = match[0].toUpperCase();
  if (!approvedColors.has(color)) errors.push(`Unapproved brand color in site CSS: ${color}`);
}

for (const logo of ['LuxSync_Logo_Horizontal_Combo.png', 'LuxSync_Logo_Horizontal_Final.png', 'LuxSync_Logo_Orb.png']) {
  const source = path.join(ROOT, 'brand', 'source-logo', logo);
  const production = path.join(ROOT, 'brand', 'assets', '01-logos', logo);
  const built = path.join(DIST, 'assets', logo);
  if (![source, production, built].every(fs.existsSync)) {
    errors.push(`Missing protected logo path for ${logo}`);
    continue;
  }
  const hashes = [hash(source), hash(production), hash(built)];
  if (new Set(hashes).size !== 1) errors.push(`${logo}: production/built copy differs from protected source master`);
}

for (const required of [
  'data/luxsync-concierge-engine.v1.json',
  'data/faqs.json',
  'data/catalog.json',
  'config.js',
  'app.js',
  '404.html',
  '.htaccess'
]) {
  if (!fs.existsSync(path.join(DIST, required))) errors.push(`Missing build artifact ${required}`);
}

if (errors.length) {
  console.error('LuxSync site validation FAILED:');
  errors.forEach((error) => console.error(`- ${error}`));
  process.exit(1);
}
console.log(`LuxSync site validation PASSED (${manifest.routes.length} routes)`);
