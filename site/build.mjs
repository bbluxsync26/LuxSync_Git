import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { readGovernedContent } from './source-content.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(HERE, '..');
const DIST = path.join(HERE, 'dist');
const BRAND = path.join(ROOT, 'brand', 'assets', 'logos', 'png');
const ENGINE = path.join(ROOT, 'website', 'src', 'concierge', 'luxsync-concierge-engine.v1.json');
const FAQ_SOURCE = path.join(ROOT, 'content', 'faqs.md');
const MANIFEST = JSON.parse(fs.readFileSync(path.join(ROOT, 'website', 'implementation-manifest.json'), 'utf8'));

const GOVERNED = readGovernedContent(ROOT);
const { homepage: HOME, leadership: LEADERSHIP, catalog } = GOVERNED;
const SLOGAN = HOME.slogan;
const routes = MANIFEST.routes.map((item) => item.route);

const escapeHtml = (value = '') => String(value)
  .replaceAll('&', '&amp;')
  .replaceAll('<', '&lt;')
  .replaceAll('>', '&gt;')
  .replaceAll('"', '&quot;');

function parseFaqs(markdown) {
  const items = [];
  const re = /^###\s+(.+?)\n\n([\s\S]*?)(?=^###\s+|^##\s+|\Z)/gm;
  let match;
  while ((match = re.exec(markdown)) !== null) {
    const question = match[1].trim();
    const answer = match[2]
      .replace(/`([^`]+)`/g, '$1')
      .replace(/\*\*([^*]+)\*\*/g, '$1')
      .replace(/\[([^\]]+)\]\([^\)]+\)/g, '$1')
      .replace(/\n+/g, ' ')
      .trim();
    if (question.endsWith('?') && answer) items.push({ question, answer });
  }
  return items;
}

const solutionPages = {
  '/solutions/commercial-offices': {
    eyebrow: 'Commercial Offices',
    title: 'A calmer, more intelligent workday.',
    intro: 'Coordinate lighting, comfort, energy-conscious routines, shared spaces, and property awareness around the way your team actually uses the workplace.',
    cards: [
      ['Intelligent Opening', 'Prepare selected lighting, climate, access-related routines, and shared spaces for the start of the day.'],
      ['Business Energy Intelligence', 'Use occupancy-aware routines and selected controls to reduce avoidable energy use without turning comfort into a spreadsheet.'],
      ['Business Property Pulse', 'Create a clearer remote view of selected property conditions using compatible sensors and notifications.']
    ],
    guide: 'Commercial Offices ROI Guide'
  },
  '/solutions/senior-living': {
    eyebrow: 'Senior Living',
    title: 'Technology that supports everyday confidence.',
    intro: 'Use thoughtful, non-intrusive smart-living technology to support comfort, pathway lighting, property awareness, water awareness, and easier daily routines.',
    cards: [
      ['Accessible Living', 'Simplify selected everyday controls through appropriate lighting, voice control, routines, climate, and entry technology.'],
      ['Night Path', 'Support nighttime movement with context-aware low-level pathway lighting.'],
      ['Water Watch', 'Improve awareness of leaks and water events using compatible sensors and, where appropriate, water-control products.']
    ],
    guide: 'Senior Living Communities ROI Guide'
  },
  '/solutions/short-term-rentals': {
    eyebrow: 'Short-Term Rentals',
    title: 'Guest-ready when you are miles away.',
    intro: 'Coordinate guest access, lighting, climate, turnovers, water awareness, and remote property status through a privacy-conscious SmartThings-first approach.',
    cards: [
      ['Guest Ready', 'Transition the property into a polished arrival state before check-in.'],
      ['Turnover', 'Support the handoff between checkout, cleaning, and the next guest-ready state.'],
      ['STR Property Pulse', 'Keep an eye on selected property conditions between stays without turning the property into a surveillance project.']
    ],
    guide: 'STR Owner / Operator / Manager ROI Guides'
  },
  '/solutions/residential': {
    eyebrow: 'Residential',
    title: 'Smart living that feels like home, not a control room.',
    intro: 'Begin with routines, comfort, awareness, ambience, and convenience. LuxSync turns those goals into compatible experiences and a phased Blueprint.',
    cards: [
      ['Welcome Home', 'Coordinate arrival lighting, climate, and selected entry or entertainment experiences.'],
      ['Goodnight', 'Bring lighting, climate, selected devices, and overnight routines into one calm transition.'],
      ['Intelligent Evening', 'Shape lighting, comfort, shades, and ambience around the rhythm of the evening.']
    ],
    guide: 'Residential ROI Guide Library'
  },
  '/solutions/aging-in-place': {
    eyebrow: 'Seniors, Caregivers & Aging in Place',
    title: 'Everyday ease, designed with dignity.',
    intro: 'Curate non-intrusive technology that can make common household tasks easier while keeping medical care, emergency response, and life-safety systems in their proper professional roles.',
    cards: [
      ['Accessible Living', 'Make selected controls easier to use through voice, routines, lighting, climate, and entry technology.'],
      ['Night Path', 'Use low-level pathway lighting to make nighttime navigation gentler.'],
      ['Property Pulse', 'Create optional, privacy-conscious awareness of selected property conditions for households that want it.']
    ],
    guide: 'Seniors, Caregivers & Aging in Place ROI Guide'
  }
};

function card(title, body, href = '') {
  const tag = href ? 'a' : 'article';
  const attr = href ? ` href="${href}"` : '';
  return `<${tag} class="lux-card"${attr}><span class="card-glint" aria-hidden="true"></span><h3>${escapeHtml(title)}</h3><p>${escapeHtml(body)}</p>${href ? '<span class="card-link">Explore →</span>' : ''}</${tag}>`;
}

function header(activeRoute) {
  const nav = [
    ['/', 'Home'], ['/solutions/', 'Solutions'], ['/find-my-luxsync-solution/', 'Concierge'], ['/shop/', 'Shop'],
    ['/guides/', 'Guides'], ['/about/', 'About'], ['/faqs/', 'FAQs'], ['/contact/', 'Contact']
  ];
  const links = nav.map(([href, label]) => {
    const active = activeRoute === href || (href !== '/' && activeRoute.startsWith(href));
    return `<a class="nav-link${active ? ' is-active' : ''}" href="${href}"${active ? ' aria-current="page"' : ''}>${label}</a>`;
  }).join('');
  return `<header class="site-header"><div class="header-inner"><a class="brand-link" href="/" aria-label="LuxSync home"><img src="/assets/luxsync-horizontal-combo.png" alt="LuxSync"></a><button class="nav-toggle" type="button" aria-expanded="false" aria-controls="main-nav"><span></span><span></span><span></span><span class="sr-only">Menu</span></button><nav id="main-nav" class="main-nav" aria-label="Primary navigation">${links}<a class="button button-small" href="/find-my-luxsync-solution/">${escapeHtml(HOME.primaryCta)}</a></nav></div></header>`;
}

function footer() {
  return `<footer class="site-footer"><div class="footer-grid"><div><img class="footer-logo" src="/assets/luxsync-horizontal-combo.png" alt="LuxSync"><p class="footer-slogan">${SLOGAN}</p><p>Curated smart-living guidance built around comfort, control, compatibility, and confidence.</p></div><div><h2>Explore</h2><a href="/solutions/">Solutions</a><a href="/shop/">Shop</a><a href="/guides/">Guides</a><a href="/about/">About</a></div><div><h2>Help</h2><a href="/contact/?intent=support">Get Support</a><a href="/faqs/">FAQs</a><a href="mailto:support@luxsync.net">support@luxsync.net</a><a href="mailto:info@luxsync.net">info@luxsync.net</a></div><div><h2>Policies</h2><span class="footer-muted">Privacy policy pending publication</span><span class="footer-muted">Terms pending publication</span></div></div><div class="footer-bottom"><span>© ${new Date().getFullYear()} LuxSync LLC</span><span>${SLOGAN}</span></div></footer>`;
}

function shell({ route, title, description, main, bodyClass = '' }) {
  const active = route.endsWith('/') ? route : `${route}/`;
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0D1526">
  <meta name="description" content="${escapeHtml(description)}">
  <title>${escapeHtml(title)} | LuxSync</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500&family=Manrope:wght@500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/styles.css">
  <script src="/config.js"></script>
  <script type="module" src="/app.js"></script>
</head>
<body class="${escapeHtml(bodyClass)}" data-route="${escapeHtml(route)}">
  <a class="skip-link" href="#main">Skip to content</a>
  ${header(active)}
  <main id="main">${main}</main>
  ${footer()}
</body>
</html>`;
}

const hero = `<section class="hero"><div class="hero-aura" aria-hidden="true"></div><div class="hero-inner"><div class="hero-copy"><p class="eyebrow">Intelligent living, curated</p><h1>${SLOGAN}</h1><p class="hero-lede">${escapeHtml(HOME.supportingCopy)}</p><div class="button-row"><a class="button" href="/find-my-luxsync-solution/">${escapeHtml(HOME.primaryCta)}</a><a class="button button-secondary" href="/shop/">${escapeHtml(HOME.secondaryCta)}</a><a class="text-link" href="/guides/">${escapeHtml(HOME.supportingCta)} →</a></div></div><div class="hero-visual" aria-label="LuxSync intelligent living concept"><div class="orbital-shell"><img src="/assets/luxsync-orb.png" alt=""><span class="orbit orbit-one"></span><span class="orbit orbit-two"></span><span class="orbit orbit-three"></span></div><div class="hero-stat"><span>Outcome first</span><strong>Lifestyle → Experience → Intelligence → Technology</strong></div></div></div></section>`;

function homePage() {
  const featured = [
    ['Short-Term Rentals', 'Guest-ready routines, remote property awareness, climate, entry, water awareness, and turnover support.', '/solutions/short-term-rentals/'],
    ['Seniors & Caregivers', 'Comfort, pathway lighting, accessibility-oriented routines, and property awareness without intrusive complexity.', '/solutions/aging-in-place/'],
    ['Smart Office & Property', 'Opening, closing, energy, shared-space, and remote-awareness experiences for professional spaces.', '/solutions/commercial-offices/'],
    ['Intentional Families', 'Lighting, routines, comfort, awareness, and technology that can support calmer household rhythms.', '/solutions/residential/'],
    ['Busy Professionals', 'Arrival, departure, climate, lighting, and property-status experiences designed to reduce daily friction.', '/solutions/residential/']
  ];
  return `${hero}
<section class="section"><div class="section-heading"><p class="eyebrow">Featured Solutions</p><h2>Start with the life you want the space to support.</h2><p>LuxSync organizes technology around outcomes first, then connects those outcomes to compatible products and a phased path.</p></div><div class="card-grid card-grid-five">${featured.map(([a,b,c]) => card(a,b,c)).join('')}</div></section>
<section class="section section-dark"><div class="split"><div><p class="eyebrow">Why LuxSync</p><h2>Less gadget aisle. More intelligent curation.</h2><p>We begin with what you want a space to do, then simplify the technology choices around compatibility, quality, and real-world use.</p></div><div class="feature-list"><div><strong>Curated Catalog</strong><span>Thoughtful selection rather than endless choice.</span></div><div><strong>SmartThings Compatibility</strong><span>A common launch ecosystem with compatibility made easier to understand.</span></div><div><strong>Intelligent Discovery</strong><span>Begin with your routines, priorities, and desired outcomes.</span></div><div><strong>Simplified Buying</strong><span>Clear collections, bundles, and guided next steps.</span></div><div><strong>Premium Customer Experience</strong><span>Elegant presentation, guidance, and support.</span></div></div></div></section>
<section class="section concierge-teaser"><div class="section-heading"><p class="eyebrow">LuxSync Intelligent Living Concierge</p><h2>Tell us how you want your space to live.</h2><p>LuxSync starts with your space, routines, priorities, and existing technology. We translate those goals into recommended intelligent-living experiences, compatible technology categories, and a phased Blueprint you can build at your own pace.</p><div class="button-row"><a class="button" href="/find-my-luxsync-solution/">${escapeHtml(HOME.primaryCta)}</a><a class="text-link" href="/my-luxsync-blueprint/">See how the Blueprint works →</a></div></div><div class="journey-line" aria-label="Lifestyle to technology journey"><span>Lifestyle</span><i></i><span>Experience</span><i></i><span>Intelligence</span><i></i><span>Technology</span></div></section>
<section class="section"><div class="section-heading"><p class="eyebrow">Product Collections</p><h2>A curated foundation for intelligent living.</h2><p>Browse LuxSync's approved product-family structure. Exact live products, pricing, inventory, and compatibility come from validated Commerce Plus data.</p></div><div id="home-catalog" class="card-grid"></div><div class="section-cta"><a class="button button-secondary" href="/shop/">Shop Collections</a></div></section>
<section class="section section-soft"><div class="section-heading"><p class="eyebrow">How It Works</p><h2>Four calm steps from idea to intelligent living.</h2></div><ol class="steps"><li><span>01</span><div><h3>Discover</h3><p>Tell LuxSync about the space, routine, property, or outcome.</p></div></li><li><span>02</span><div><h3>Design</h3><p>Receive recommended Experiences and My LuxSync Blueprint.</p></div></li><li><span>03</span><div><h3>Choose</h3><p>Select validated compatible products or bundles.</p></div></li><li><span>04</span><div><h3>Evolve</h3><p>Add compatible experiences over time.</p></div></li></ol></section>
<section class="section"><div class="section-heading"><p class="eyebrow">Meet the Founders</p><h2>Technology strategy meets customer-centered operations.</h2></div><div class="founder-grid"><article class="founder-card"><div class="founder-monogram">BB</div><h3>Bridgette Beardsley</h3><p class="role">${escapeHtml(LEADERSHIP.bridgette.role)}</p><p>${escapeHtml(LEADERSHIP.bridgette.compactBiography)}</p></article><article class="founder-card"><div class="founder-monogram">SB</div><h3>Sheldon Bardol</h3><p class="role">${escapeHtml(LEADERSHIP.sheldon.role)}</p><p>${escapeHtml(LEADERSHIP.sheldon.compactBiography)}</p></article></div><div class="section-cta"><a class="text-link" href="/about/">Meet LuxSync leadership →</a></div></section>
<section class="section section-dark"><div class="section-heading"><p class="eyebrow">Frequently Asked Questions</p><h2>Clear answers, without the technical fog.</h2></div><div id="faq-preview" class="faq-list"></div><div class="button-row"><a class="button button-secondary" href="/faqs/">View All FAQs</a><a class="text-link" href="/contact/">Contact LuxSync →</a></div></section>
<section class="section"><div class="split"><div><p class="eyebrow">ROI Guide Library</p><h2>Choose the guide built for your environment.</h2><p>Explore audience-specific ROI frameworks for offices, senior living, short-term rentals, residential households, families, and aging in place.</p><a class="button" href="/guides/">Get the ROI Guide</a></div><div class="contact-gateway"><a href="/contact/?intent=support"><strong>Get Support</strong><span>Help with an existing product, solution, setup, compatibility question, or order.</span></a><a href="/contact/?intent=general_question"><strong>Ask a Question</strong><span>General information, compatibility, company, or product questions.</span></a><a href="/contact/?intent=consultation"><strong>Request a Consultation</strong><span>Plan a new space, upgrade an existing setup, or review a Blueprint.</span></a></div></div></section>`;
}

function solutionsIndex() {
  const items = [
    ['Commercial Offices', 'Lighting, comfort, energy, shared spaces, opening/closing, and property awareness.', '/solutions/commercial-offices/'],
    ['Senior Living', 'Accessible living, pathway lighting, comfort, water awareness, and non-intrusive property awareness.', '/solutions/senior-living/'],
    ['Short-Term Rentals', 'Guest access, climate, turnover, remote awareness, water awareness, and energy-conscious routines.', '/solutions/short-term-rentals/'],
    ['Residential', 'Arrival, departure, bedtime, comfort, ambience, entertainment, and property awareness.', '/solutions/residential/'],
    ['Aging in Place', 'Everyday ease, pathway lighting, simple controls, and privacy-conscious awareness for seniors and caregivers.', '/solutions/aging-in-place/']
  ];
  return `<section class="page-hero"><div><p class="eyebrow">LuxSync Solutions</p><h1>Choose the outcome. Then choose the technology.</h1><p>Every LuxSync solution begins with how a space should feel and function. The Concierge translates that intention into a compatible Blueprint.</p></div></section><section class="section"><div class="card-grid">${items.map(([a,b,c]) => card(a,b,c)).join('')}</div><div class="section-cta"><a class="button" href="/find-my-luxsync-solution/">${escapeHtml(HOME.primaryCta)}</a></div></section>`;
}

function solutionDetail(route) {
  const data = solutionPages[route];
  return `<section class="page-hero"><div><p class="eyebrow">${escapeHtml(data.eyebrow)}</p><h1>${escapeHtml(data.title)}</h1><p>${escapeHtml(data.intro)}</p><div class="button-row"><a class="button" href="/find-my-luxsync-solution/?context=${encodeURIComponent(route)}">Build My Blueprint</a><a class="button button-secondary" href="/contact/?intent=consultation">Request Consultation</a></div></div></section><section class="section"><div class="section-heading"><p class="eyebrow">Experience Concepts</p><h2>Designed around real routines.</h2><p>These are solution concepts, not automatically live SKUs. Exact compatible products and bundle contents are validated before purchase.</p></div><div class="card-grid">${data.cards.map(([a,b]) => card(a,b)).join('')}</div></section><section class="section section-soft"><div class="split"><div><p class="eyebrow">ROI Guide</p><h2>${escapeHtml(data.guide)}</h2><p>Use the LuxSync ROI framework to identify measurable benefits, assumptions, implementation costs, and payback without promising a specific return.</p><a class="button button-secondary" href="/guides/">Open the Guide Library</a></div><div class="safety-note"><strong>Important boundary</strong><p>LuxSync convenience and awareness technology does not replace professional monitoring, emergency services, medical care, required life-safety systems, or manufacturer instructions.</p></div></div></section>`;
}

function conciergePage() {
  return `<section class="page-hero compact"><div><p class="eyebrow">LuxSync Intelligent Living Concierge</p><h1>Find My LuxSync Solution</h1><p>Begin with your routines, priorities, property, and existing technology. The Concierge turns those answers into recommended Experiences and My LuxSync Blueprint.</p></div></section><section class="section app-section"><div id="concierge-app" class="app-shell" aria-live="polite"><div class="loading-state">Preparing your intelligent-living journey…</div></div></section>`;
}

function blueprintPage() {
  return `<section class="page-hero compact"><div><p class="eyebrow">Personalized result</p><h1>My LuxSync Blueprint</h1><p>Your Blueprint explains the experiences LuxSync recommends, the foundation they depend on, a practical implementation path, and the next best action.</p></div></section><section class="section app-section"><div id="blueprint-app" class="app-shell" aria-live="polite"></div></section>`;
}

function shopPage() {
  return `<section class="page-hero"><div><p class="eyebrow">LuxSync Shop</p><h1>Curated technology, organized by the life it supports.</h1><p>Explore the approved LuxSync product-family structure and planning bundles. Exact live products, prices, stock, shipping, and compatibility remain governed by validated GoDaddy Commerce Plus data.</p><div class="button-row"><a id="commerce-link" class="button" href="/contact/?intent=product_information">Browse Current Store</a><a class="button button-secondary" href="/find-my-luxsync-solution/">Need Guidance First?</a></div></div></section><section class="section"><div class="section-heading"><p class="eyebrow">Product Families</p><h2>Build from a compatible foundation.</h2></div><div id="shop-families" class="card-grid"></div></section><section class="section section-dark"><div class="section-heading"><p class="eyebrow">Curated Bundle Concepts</p><h2>Clear starting points, validated before sale.</h2></div><div id="shop-bundles" class="card-grid"></div></section><section class="section"><div class="section-heading"><p class="eyebrow">LuxSync Experiences</p><h2>Outcome-first concepts that can map to products, bundles, setup guidance, and automation recommendations.</h2></div><div id="shop-experiences" class="chip-grid"></div></section>`;
}

function guidesPage() {
  const groups = [
    ['Commercial & Care Environments', [
      'Commercial Offices', 'Nursing Homes', 'Senior Living Communities'
    ]],
    ['Short-Term Rentals', ['STR Owners', 'STR Operators', 'STR Managers']],
    ['Residential Living', ['Residential Homeowners', 'Busy Professionals', 'Intentional Parents & Families', 'Seniors, Caregivers & Aging in Place']]
  ];
  return `<section class="page-hero"><div><p class="eyebrow">LuxSync ROI Guide Library</p><h1>Measure the value that matters in your space.</h1><p>LuxSync ROI guides help you frame verified benefits, implementation cost, simple ROI, and payback without turning estimates into promises.</p></div></section><section class="section"><div class="guide-groups">${groups.map(([group, items]) => `<section class="guide-group"><h2>${group}</h2><div class="card-grid">${items.map((name) => card(name, 'Explore the LuxSync ROI framework for this audience, including measurable benefit categories, assumptions, boundaries, and next-step planning.', '/contact/?intent=consultation')).join('')}</div></section>`).join('')}</div></section>`;
}

function aboutPage() {
  return `<section class="page-hero"><div><p class="eyebrow">About LuxSync</p><h1>Luxury is confidence.</h1><p>LuxSync was created to simplify smart-home technology without sacrificing elegance, quality, or confidence.</p></div></section><section class="section"><div class="prose"><p>Too often, smart living begins with a wall of technical specifications, disconnected products, and too many decisions. LuxSync takes a different approach. We begin with the way a customer wants a home, rental property, or professional space to feel and function, then organize compatible products and guidance around that outcome.</p><p>Our mission is to help customers create environments that are safer, smarter, and more comfortable through trusted curation, thoughtful automation, and technology that belongs naturally in the space.</p><blockquote>We believe luxury is not complexity. <strong>Luxury is confidence.</strong></blockquote></div></section><section class="section section-dark"><div class="section-heading"><p class="eyebrow">Leadership</p><h2>Two disciplines. One customer experience.</h2></div><div class="founder-grid"><article class="founder-card"><div class="founder-monogram">BB</div><h3>Bridgette Beardsley</h3><p class="role">${escapeHtml(LEADERSHIP.bridgette.role)}</p><p>${escapeHtml(LEADERSHIP.bridgette.compactBiography)}</p></article><article class="founder-card"><div class="founder-monogram">SB</div><h3>Sheldon Bardol</h3><p class="role">${escapeHtml(LEADERSHIP.sheldon.role)}</p><p>${escapeHtml(LEADERSHIP.sheldon.compactBiography)}</p></article></div></section><section class="section"><div class="section-heading"><p class="eyebrow">Our Promise</p><h2>Quiet technology. Clear guidance.</h2></div><div class="promise-grid"><div>Begin with the customer's desired experience.</div><div>Make compatibility and limitations understandable.</div><div>Curate with purpose rather than overwhelm with choice.</div><div>Keep technology quiet, useful, and at home in the environment.</div></div></section>`;
}

function faqPage() {
  return `<section class="page-hero"><div><p class="eyebrow">Frequently Asked Questions</p><h1>Smart living, explained clearly.</h1><p>Browse the launch FAQ library for LuxSync, compatibility, shopping, setup, support, seniors and caregivers, and roadmap boundaries.</p></div></section><section class="section"><div id="faq-full" class="faq-list"></div><div class="section-cta"><a class="button" href="/contact/">Contact LuxSync</a></div></section>`;
}

function contactPage() {
  return `<section class="page-hero compact"><div><p class="eyebrow">Contact LuxSync</p><h1>Smart living questions deserve intelligent answers.</h1><p>Choose the reason for your inquiry and the form will guide you to the right next step without asking for information you do not need to provide.</p><div class="direct-contact"><a href="mailto:support@luxsync.net"><strong>Customer Support</strong><span>support@luxsync.net</span></a><a href="mailto:info@luxsync.net"><strong>General Information</strong><span>info@luxsync.net</span></a></div></div></section><section class="section app-section"><div id="contact-app" class="app-shell"></div></section>`;
}

const pageBuilders = {
  '/': homePage,
  '/find-my-luxsync-solution': conciergePage,
  '/my-luxsync-blueprint': blueprintPage,
  '/solutions': solutionsIndex,
  '/shop': shopPage,
  '/guides': guidesPage,
  '/about': aboutPage,
  '/faqs': faqPage,
  '/contact': contactPage
};

function pageMeta(route) {
  const metas = {
    '/': ['LuxSync', 'Curated smart-living technology and guidance built around comfort, compatibility, control, and confidence.'],
    '/find-my-luxsync-solution': ['Find My LuxSync Solution', 'Use the LuxSync Intelligent Living Concierge to create My LuxSync Blueprint.'],
    '/my-luxsync-blueprint': ['My LuxSync Blueprint', 'Review your personalized LuxSync experiences, foundation, roadmap, and next best action.'],
    '/solutions': ['Smart Living Solutions', 'Explore LuxSync solution pathways for homes, rentals, offices, senior living, and aging in place.'],
    '/shop': ['Shop Smart Home', 'Explore LuxSync product families, curated bundle concepts, and outcome-first smart-living experiences.'],
    '/guides': ['ROI Guide Library', 'Explore LuxSync ROI guides for commercial, STR, residential, senior living, and caregiving environments.'],
    '/about': ['About LuxSync', 'Learn how LuxSync simplifies smart living through trusted curation, thoughtful automation, and intelligent guidance.'],
    '/faqs': ['Frequently Asked Questions', 'Clear answers about LuxSync, compatibility, products, setup, support, seniors, caregivers, and future services.'],
    '/contact': ['Contact LuxSync', 'Contact LuxSync for support, product information, consultations, general questions, or business partnerships.']
  };
  if (solutionPages[route]) return [`${solutionPages[route].eyebrow} Solutions`, solutionPages[route].intro];
  return metas[route] || ['LuxSync', SLOGAN];
}

function routePath(route) {
  if (route === '/') return DIST;
  return path.join(DIST, route.replace(/^\//, '').replace(/\/$/, ''));
}

fs.rmSync(DIST, { recursive: true, force: true });
fs.mkdirSync(DIST, { recursive: true });
fs.mkdirSync(path.join(DIST, 'assets'), { recursive: true });
fs.mkdirSync(path.join(DIST, 'data'), { recursive: true });

for (const file of ['luxsync-horizontal-combo.png', 'luxsync-horizontal.png', 'luxsync-orb.png']) {
  fs.copyFileSync(path.join(BRAND, file), path.join(DIST, 'assets', file));
}
fs.copyFileSync(ENGINE, path.join(DIST, 'data', 'luxsync-concierge-engine.v1.json'));
fs.copyFileSync(path.join(HERE, 'src', 'styles.css'), path.join(DIST, 'styles.css'));
fs.copyFileSync(path.join(HERE, 'src', 'app.js'), path.join(DIST, 'app.js'));

const faqs = parseFaqs(fs.readFileSync(FAQ_SOURCE, 'utf8'));
fs.writeFileSync(path.join(DIST, 'data', 'faqs.json'), JSON.stringify(faqs, null, 2) + '\n');
fs.writeFileSync(path.join(DIST, 'data', 'catalog.json'), JSON.stringify(catalog, null, 2) + '\n');

const config = {
  commerceUrl: process.env.LUXSYNC_COMMERCE_URL || '',
  contactEndpoint: process.env.LUXSYNC_CONTACT_ENDPOINT || '',
  siteUrl: process.env.LUXSYNC_SITE_URL || ''
};
fs.writeFileSync(path.join(DIST, 'config.js'), `window.LUXSYNC_CONFIG = ${JSON.stringify(config)};\n`);

for (const rawRoute of routes) {
  const route = rawRoute === '/' ? '/' : rawRoute.replace(/\/$/, '');
  const builder = pageBuilders[route] || (solutionPages[route] ? () => solutionDetail(route) : null);
  if (!builder) throw new Error(`No page builder for ${rawRoute}`);
  const [title, description] = pageMeta(route);
  const dir = routePath(rawRoute);
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, 'index.html'), shell({ route, title, description, main: builder() }));
}

fs.writeFileSync(path.join(DIST, '404.html'), shell({ route: '/404', title: 'Page Not Found', description: 'The requested LuxSync page could not be found.', main: `<section class="page-hero"><div><p class="eyebrow">404</p><h1>This room is not in the Blueprint.</h1><p>The page you requested could not be found.</p><a class="button" href="/">Return Home</a></div></section>` }));

fs.writeFileSync(path.join(DIST, '.htaccess'), `Options -MultiViews\nErrorDocument 404 /404.html\nDirectoryIndex index.html\n`);
console.log(`Built LuxSync site with ${routes.length} governed routes.`);
