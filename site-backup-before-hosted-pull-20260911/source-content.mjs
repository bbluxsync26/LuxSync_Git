import fs from 'node:fs';
import path from 'node:path';

function read(root, relativePath) {
  return fs.readFileSync(path.join(root, relativePath), 'utf8');
}

function getSection(markdown, heading, level = 2) {
  const marker = `${'#'.repeat(level)} ${heading}`;
  const markerIndex = markdown.indexOf(marker);
  if (markerIndex < 0) throw new Error(`Missing governed section: ${marker}`);
  const tail = markdown.slice(markerIndex + marker.length).replace(/^\s*\n/, '');
  const nextHeading = tail.search(new RegExp(`^#{1,${level}}\\s+`, 'm'));
  return (nextHeading >= 0 ? tail.slice(0, nextHeading) : tail).trim();
}

function stripInline(markdown = '') {
  return String(markdown)
    .replace(/<[^>]+>/g, '')
    .replace(/!\[([^\]]*)\]\([^\)]+\)/g, '$1')
    .replace(/\[([^\]]+)\]\([^\)]+\)/g, '$1')
    .replace(/\*\*([^*]+)\*\*/g, '$1')
    .replace(/\*([^*]+)\*/g, '$1')
    .replace(/`([^`]+)`/g, '$1')
    .replace(/\s+/g, ' ')
    .trim();
}

function firstParagraph(block) {
  const paragraph = block
    .split(/\n\s*\n/)
    .map((item) => item.trim())
    .find((item) => item && !item.startsWith('#') && !item.startsWith('-'));
  if (!paragraph) throw new Error('Governed section has no paragraph value');
  return stripInline(paragraph);
}

function sectionValue(markdown, heading) {
  return firstParagraph(getSection(markdown, heading));
}

function listSections(markdown, heading, level, childLevel) {
  const block = getSection(markdown, heading, level);
  const childMarker = `${'#'.repeat(childLevel)} `;
  const sections = [];
  let current = null;

  for (const line of block.split('\n')) {
    if (line.startsWith(childMarker)) {
      if (current) sections.push({ name: current.name, body: current.lines.join('\n').trim() });
      current = { name: stripInline(line.slice(childMarker.length)), lines: [] };
    } else if (current) {
      current.lines.push(line);
    }
  }

  if (current) sections.push({ name: current.name, body: current.lines.join('\n').trim() });
  return sections;
}

function summarizeFamily(body) {
  const items = body
    .split('\n')
    .filter((line) => /^-\s+/.test(line))
    .map((line) => stripInline(line.replace(/^-\s+/, '')))
    .filter(Boolean);
  if (!items.length) return firstParagraph(body);
  return `Includes ${items.join('; ')}.`;
}

function parseCatalog(markdown) {
  const families = listSections(markdown, '1. Physical Product Families', 1, 2)
    .map(({ name, body }) => ({
      name,
      description: summarizeFamily(body),
      status: 'Planning Product Family'
    }));

  const bundleBlock = getSection(markdown, '2. Existing Curated Bundle Concepts', 1);
  const bundles = [...bundleBlock.matchAll(/^-\s+\*\*(.+?)\*\*(?:\s+—\s+(.+))?$/gm)]
    .map((match) => ({
      name: stripInline(match[1]),
      status: 'Planning Bundle',
      note: match[2]
        ? stripInline(match[2])
        : 'Exact contents and public pricing require Commerce Plus validation.'
    }));

  const residential = listSections(markdown, '3. Concierge-Linked Solution Concepts', 1, 3);
  const shortTermRental = listSections(markdown, '4. Short-Term Rental Solution Concepts', 1, 2);
  const business = listSections(markdown, '5. Business / Commercial Solution Concepts', 1, 2);
  const experiences = [...residential, ...shortTermRental, ...business]
    .map(({ name }) => ({ name, status: 'Solution Concept' }));

  if (families.length < 10 || bundles.length < 4 || experiences.length < 20) {
    throw new Error('Canonical product catalog parsing produced an incomplete production catalog');
  }

  return { families, bundles, experiences };
}

function parseLeader(markdown) {
  const nameMatch = markdown.match(/^#\s+(.+)$/m);
  const roleMatch = markdown.match(/^##\s+(.+)$/m);
  if (!nameMatch || !roleMatch) throw new Error('Leadership source is missing a name or role');
  return {
    name: stripInline(nameMatch[1]),
    role: stripInline(roleMatch[1]),
    biography: firstParagraph(getSection(markdown, 'Website Biography')),
    compactBiography: firstParagraph(getSection(markdown, 'Compact Biography'))
  };
}

export function readGovernedContent(root) {
  const homepageMarkdown = read(root, 'content/homepage.md');
  const catalogMarkdown = read(root, 'content/product-catalog.md');

  const homepage = {
    slogan: sectionValue(homepageMarkdown, 'Official Slogan and Hero Line'),
    supportingCopy: sectionValue(homepageMarkdown, 'Supporting Copy'),
    primaryCta: sectionValue(homepageMarkdown, 'Primary CTA'),
    secondaryCta: sectionValue(homepageMarkdown, 'Secondary CTA'),
    supportingCta: sectionValue(homepageMarkdown, 'Supporting CTA')
  };

  if (homepage.slogan !== 'Where Luxury Lives Intelligently') {
    throw new Error(`Unexpected governed slogan: ${homepage.slogan}`);
  }

  return {
    homepage,
    catalog: parseCatalog(catalogMarkdown),
    leadership: {
      bridgette: parseLeader(read(root, 'docs/leadership/bridgette-beardsley.md')),
      sheldon: parseLeader(read(root, 'docs/leadership/sheldon-bardol.md'))
    },
    sources: [
      'content/homepage.md',
      'content/product-catalog.md',
      'docs/leadership/bridgette-beardsley.md',
      'docs/leadership/sheldon-bardol.md'
    ]
  };
}
