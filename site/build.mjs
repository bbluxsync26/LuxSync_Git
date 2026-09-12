import {shopPage as storeShop,storeRoutes,wishlistDialog} from './src/store/pages.mjs';
import {parseFaqs, faqLibrary} from './src/faq-content.mjs';
import {guides,guideLibrary,guidePage,accountPage as workspaceAccount,accountDashboard,savePrompt,conciergeSave} from './src/roi-pages.mjs';
import {build as bundleWorker} from 'esbuild';
import {heroAssets,headerControls,searchDialog,decoratePage,homeOverview} from './src/presentation.mjs';
import {iconFor} from './src/icon-map.js';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { readGovernedContent } from './source-content.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = fs.existsSync(path.join(HERE, 'source-data')) ? path.join(HERE, 'source-data') : path.resolve(HERE, '..');
const DIST = path.join(HERE, 'dist','client');
const BRAND = path.join(HERE, 'src', 'logos');
const ICONS = path.join(ROOT, 'brand', 'assets', 'icons', 'webp');
const DIVIDERS = path.join(ROOT, 'brand', 'assets', 'dividers', 'webp');
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



function card(title, body, href = '', image = '') {
  const tag = href ? 'a' : 'article';
  const attr = href ? ` href="${href}"` : '';
  return `<${tag} class="lux-card${image ? ' featured-solution' : ''}"${attr}>${image ? `<img class="featured-solution-image" src="${image.startsWith('hero:') ? '/assets/heroes/'+image.slice(5)+'-720.webp' : '/assets/featured-'+image+'.png'}" alt="" loading="lazy" width="1774" height="950">` : ''}<span class="card-glint" aria-hidden="true"></span><img class="card-icon" src="/assets/icons/${iconFor(title)}.webp" alt=""><h3>${escapeHtml(title)}</h3><p>${escapeHtml(body)}</p>${href ? '<span class="card-link">Explore →</span>' : ''}</${tag}>`;
}

function header(activeRoute) {
  const nav = [['/', 'Home'], ['/solutions/commercial/', 'Commercial'], ['/solutions/residential/', 'Residential'], ['/solutions/', 'All Solutions'], ['/shop/', 'Shop'], ['/guides/', 'Guides'], ['/about/', 'About'], ['/faqs/', 'FAQs'], ['/contact/', 'Contact']];
  const links = nav.map(([href, label]) => { const active = activeRoute === href || (href !== '/' && activeRoute.startsWith(href)); return `<a class="nav-link${active ? ' is-active' : ''}" href="${href}"${active ? ' aria-current="page"' : ''}>${label}</a>`; }).join('');
  return `<header class="site-header"><div class="header-inner"><div class="header-start"><button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="main-nav"><svg viewBox="0 0 28 28" aria-hidden="true"><path d="M6 7h19M4 14h19M2 21h19"/></svg></button><a class="utility-icon ls-home" href="/" aria-label="LS — Home"><img src="/assets/luxsync-orb.png" alt=""></a></div><a class="brand-link" href="/" aria-label="LuxSync home"><img src="/assets/luxsync-horizontal.png" alt="LuxSync"></a><div class="property-nav" aria-label="Property solutions"><a class="utility-icon property-icon" href="/solutions/commercial/" aria-label="Commercial solutions" title="Commercial solutions"><svg viewBox="0 0 24 24" aria-hidden="true"><path class="metal-steel" d="M4 21V3h12v18M2 21h20M16 9h4v12"/><path class="metal-rose" d="M7 7h1m3 0h1M7 11h1m3 0h1M7 15h1m3 0h1M9 21v-3h3v3"/></svg></a><a class="utility-icon property-icon" href="/solutions/residential/" aria-label="Residential solutions" title="Residential solutions"><svg viewBox="0 0 24 24" aria-hidden="true"><circle class="metal-steel" cx="8" cy="7" r="3"/><circle class="metal-rose" cx="17" cy="8" r="2.5"/><path class="metal-steel" d="M2 21v-3a6 6 0 0 1 12 0v3"/><path class="metal-rose" d="M15 14a5 5 0 0 1 7 4.6V21"/></svg></a></div><nav id="main-nav" class="main-nav" aria-label="Primary navigation">${links}</nav>${headerControls()}</div></header>`;
}

function footer() {
  return `<footer class="site-footer"><div class="footer-grid"><div><img class="footer-logo" src="/assets/luxsync-horizontal-combo.png" alt="LuxSync"><p class="footer-slogan">${SLOGAN}</p><p>Curated smart-living guidance built around comfort, control, compatibility, and confidence.</p></div><div><h2>Explore</h2><a href="/solutions/commercial/">Commercial Solutions</a><a href="/solutions/residential/">Residential Solutions</a><a href="/solutions/">Choose a Solution</a><a href="/shop/?solution=all">All Products & Bundles</a><a href="/guides/">Guides</a><a href="/about/">About</a></div><div><h2>Your LuxSync</h2><a href="/find-my-luxsync-solution/">Concierge</a><a href="/account/">Account</a><a href="/account/wishlists/">My Wishlists</a><a href="/cart/">Cart</a><h2>Help</h2><a href="/contact/?intent=support">Get Support</a><a href="/faqs/">FAQs</a><a href="mailto:support@luxsync.net">support@luxsync.net</a><a href="mailto:info@luxsync.net">info@luxsync.net</a></div><div><h2>Policies</h2><span class="footer-muted">Privacy policy pending publication</span><span class="footer-muted">Terms pending publication</span></div></div><div class="footer-bottom"><span>© ${new Date().getFullYear()} LuxSync LLC</span><span>${SLOGAN}</span></div></footer>`;
}

function shell({ route, title, description, main, bodyClass = '' }) {
  const active = route.endsWith('/') ? route : `${route}/`;
  const documentTitle = title === 'LuxSync' ? 'LuxSync' : `${title} | LuxSync`;
  const canonicalUrl = `https://luxsync-intelligent-living.bridgette-beardsley.chatgpt.site${active}`;
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/png" href="/assets/luxsync-orb.png">
  <link rel="apple-touch-icon" href="/assets/luxsync-orb.png">
  <meta name="theme-color" content="#0D1526">
  <meta name="description" content="${escapeHtml(description)}">
  <link rel="canonical" href="${canonicalUrl}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="LuxSync">
  <meta property="og:title" content="${escapeHtml(documentTitle)}">
  <meta property="og:description" content="${escapeHtml(description)}">
  <meta property="og:url" content="${canonicalUrl}">
  <meta property="og:image" content="https://luxsync-intelligent-living.bridgette-beardsley.chatgpt.site/assets/og.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${escapeHtml(documentTitle)}">
  <meta name="twitter:description" content="${escapeHtml(description)}">
  <meta name="twitter:image" content="https://luxsync-intelligent-living.bridgette-beardsley.chatgpt.site/assets/og.png">
  <title>${escapeHtml(documentTitle)}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500&family=Manrope:wght@500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/styles.css">
  <script src="/config.js"></script>
  <script type="module" src="/store-client.js"></script><script type="module" src="/app.js"></script><script type="module" src="/property-flow.js"></script>
</head>
<body class="${escapeHtml(bodyClass)}" data-route="${escapeHtml(route)}">
  <a class="skip-link" href="#main">Skip to content</a>
  ${header(active)}
  ${searchDialog}
${savePrompt}
  <main id="main">${decoratePage(route, main)}${['/find-my-luxsync-solution','/my-luxsync-blueprint'].includes(route)?conciergeSave:''}</main>
  ${footer()}
${wishlistDialog}</body>
</html>`;
}

function homePage() { return homeOverview({HOME,SLOGAN,card}); }

function solutionsIndex() { return propertyChoice(); }
function previousSolutionsIndex() {
  const items = [
    ['Commercial Offices', 'Lighting, comfort, energy, shared spaces, opening/closing, and property awareness.', '/solutions/commercial-offices/'],
    ['Senior Living', 'Accessible living, pathway lighting, comfort, water awareness, and non-intrusive property awareness.', '/solutions/senior-living/'],
    ['Short-Term Rentals', 'Guest access, climate, turnover, remote awareness, water awareness, and energy-conscious routines.', '/solutions/short-term-rentals/'],
    ['Residential', 'Arrival, departure, bedtime, comfort, ambience, entertainment, and property awareness.', '/solutions/residential/'],
    ['Aging in Place', 'Everyday ease, pathway lighting, simple controls, and privacy-conscious awareness for seniors and caregivers.', '/solutions/aging-in-place/']
  ];
  return `<section class="page-hero"><div><p class="eyebrow">LuxSync Solutions</p><h1>Choose the outcome. Then choose the technology.</h1><p>Every LuxSync solution begins with how a space should feel and function. The Concierge translates that intention into a compatible Blueprint.</p></div></section><section class="section"><div class="card-grid">${items.map(([a,b,c],i) => card(a,b,c,'hero:'+['plush-drift-commercial','aging-in-place','plush-drift-rental','plush-drift-residential','plush-drift-care'][i])).join('')}</div><div class="section-cta"><a class="button" href="/find-my-luxsync-solution/">${escapeHtml(HOME.primaryCta)}</a></div></section>`;
}

function solutionDetail(route) {
  const data = solutionPages[route];
  const type=['/solutions/commercial-offices','/solutions/short-term-rentals','/solutions/senior-living'].includes(route)?'commercial':'residential';
  const bundle=route.includes('short-term')?'rental-bundles':route.includes('senior')||route.includes('aging')?'senior-bundles':type==='commercial'?'commercial-bundles':'residential-bundles';
  return `<section class="page-hero"><div><a class="text-link" href="/solutions/${type}/">← ${type==='commercial'?'Commercial':'Residential'} Solutions</a><p class="eyebrow">${escapeHtml(data.eyebrow)}</p><h1>${escapeHtml(data.title)}</h1><p>${escapeHtml(data.intro)}</p><div class="button-row"><a class="button" href="/find-my-luxsync-solution/?solution=${type}&context=${encodeURIComponent(route)}">Build My Blueprint</a><a class="button button-secondary" href="/contact/?intent=consultation">Request Consultation</a></div></div></section><section class="section"><div class="section-heading"><div class="button-row"><a class="button" href="/shop/category/${bundle}/?solution=${type}">Explore relevant bundles</a><a class="button button-secondary" href="/shop/?solution=${type}">Browse all devices</a></div><p class="eyebrow">Experience Concepts</p><h2>Designed around real routines.</h2><p>These are solution concepts, not automatically live SKUs. Exact compatible products and bundle contents are validated before purchase.</p></div><div class="card-grid">${data.cards.map(([a,b]) => card(a,b)).join('')}</div></section><section class="section section-soft"><div class="split"><div><p class="eyebrow">ROI Guide</p><h2>${escapeHtml(data.guide)}</h2><p>Use the LuxSync ROI framework to identify measurable benefits, assumptions, implementation costs, and payback without promising a specific return.</p><a class="button button-secondary" href="/guides/?solution=${type}">Open the Guide Library</a></div><div class="safety-note"><strong>Important boundary</strong><p>LuxSync convenience and awareness technology does not replace professional monitoring, emergency services, medical care, required life-safety systems, or manufacturer instructions.</p></div></div></section>`;
}

function conciergePage() {
  return `<section class="page-hero compact"><div><p class="eyebrow">LuxSync Intelligent Living Concierge</p><h1>Find My LuxSync Solution</h1><p>Begin with your routines, priorities, property, and existing technology. The Concierge turns those answers into recommended Experiences and My LuxSync Blueprint.</p></div></section><section class="section app-section"><div id="concierge-app" class="app-shell" aria-live="polite"><div class="loading-state">Preparing your intelligent-living journey…</div></div></section>`;
}

function blueprintPage() {
  return `<section class="page-hero compact"><div><p class="eyebrow">Personalized result</p><h1>My LuxSync Blueprint</h1><p>Your Blueprint explains the experiences LuxSync recommends, the foundation they depend on, a practical implementation path, and the next best action.</p></div></section><section class="section app-section"><div id="blueprint-app" class="app-shell" aria-live="polite"></div></section>`;
}

function shopPage() { return storeShop(); }
function legacyShopPage() {
  return `<section class="page-hero"><div><p class="eyebrow">LuxSync Shop</p><h1>Curated technology, organized by the life it supports.</h1><p>Explore the approved LuxSync product-family structure and planning bundles. Exact live products, prices, stock, shipping, and compatibility remain governed by validated GoDaddy Commerce Plus data.</p><div class="button-row"><a id="commerce-link" class="button" href="/contact/?intent=product_information">Browse Current Store</a><a class="button button-secondary" href="/find-my-luxsync-solution/">Need Guidance First?</a></div></div></section><section id="planning-cart" class="section section-soft" aria-live="polite"></section><section class="section"><div class="section-heading"><p class="eyebrow">Product Families</p><h2>Build from a compatible foundation.</h2></div><div id="shop-families" class="card-grid"></div></section><section class="section section-dark"><div class="section-heading"><p class="eyebrow">Curated Bundle Concepts</p><h2>Clear starting points, validated before sale.</h2></div><div id="shop-bundles" class="card-grid"></div></section><section class="section"><div class="section-heading"><p class="eyebrow">LuxSync Experiences</p><h2>Outcome-first concepts that can map to products, bundles, setup guidance, and automation recommendations.</h2></div><div id="shop-experiences" class="chip-grid"></div></section>`;
}


function accountPage(){return `<section class="auth-page"><div class="auth-visual"><img src="/assets/member-access.png" alt=""><div><img src="/assets/luxsync-horizontal-combo.png" alt="LuxSync"><p class="eyebrow">Private member access</p><h1>Welcome Back</h1><p>Sign in to continue to your LuxSync account, orders, and saved recommendations.</p></div></div><div class="auth-panel"><form id="login-form" class="auth-card"><h2>Member Sign In</h2><p>Authentication is securely handled by the connected Commerce Plus account service.</p><label>Email address<input type="email" autocomplete="email" required></label><label>Password<input type="password" autocomplete="current-password" required></label><button class="button" type="submit">Continue to Secure Sign In</button><p id="login-status" role="status"></p><a class="auth-card__primary-link" href="/account/create/">Create your LuxSync account</a><a href="/contact/?intent=support">Need account help?</a></form></div></section>`;}
function createAccountPage(){return `<section class="auth-page"><div class="auth-visual"><img src="/assets/member-access.png" alt=""><div><img src="/assets/luxsync-horizontal-combo.png" alt="LuxSync"><p class="eyebrow">Private member access</p><h1>Create Your LuxSync Account</h1><p>Save preferences, follow orders, revisit recommendations, and keep your LuxSync experience connected.</p></div></div><div class="auth-panel"><form id="create-account-form" class="auth-card"><p class="eyebrow">New member</p><h2>Create Your Account</h2><p>Your account is created through LuxSync’s secure Commerce Plus account service.</p><label>First name<input name="firstName" type="text" autocomplete="given-name" required></label><label>Last name<input name="lastName" type="text" autocomplete="family-name" required></label><label>Email address<input name="email" type="email" autocomplete="email" required></label><label>Password<input name="password" type="password" autocomplete="new-password" minlength="8" required></label><label>Confirm password<input name="confirmPassword" type="password" autocomplete="new-password" minlength="8" required></label><p class="auth-security-note">This preview never stores your credentials. Account creation continues only through the connected Commerce Plus service.</p><button class="button" type="submit">Continue to Secure Account Creation</button><p id="create-account-status" role="status"></p><a href="/account/">Already have an account? Sign in</a></form></div></section>`;}
function welcomePage(){return `<section class="welcome-hero"><img src="/assets/member-access.png" alt=""><div><p class="eyebrow">LuxSync Member Access</p><h1>Welcome Back</h1><p>Your calm starting point for orders, saved recommendations, support, and account preferences.</p></div></section><section class="section"><div class="card-grid"><a class="lux-card" href="/shop/"><h3>Orders & Shopping</h3><p>Continue with the connected Commerce Plus account experience.</p></a><a class="lux-card" href="/my-luxsync-blueprint/"><h3>Saved Recommendations</h3><p>Return to your latest intelligent-living Blueprint on this device.</p></a><a class="lux-card" href="/contact/?intent=support"><h3>Support</h3><p>Get help with products, orders, setup, or account access.</p></a></div></section>`;}

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
  return `<section class="page-hero"><div><p class="eyebrow">About LuxSync</p><h1>Luxury is confidence.</h1><p>LuxSync was created to simplify smart-home technology without sacrificing elegance, quality, or confidence.</p></div></section><section class="section"><div class="prose"><p>Too often, smart living begins with a wall of technical specifications, disconnected products, and too many decisions. LuxSync takes a different approach. We begin with the way a customer wants a home, rental property, or professional space to feel and function, then organize compatible products and guidance around that outcome.</p><p>Our mission is to help customers create environments that are safer, smarter, and more comfortable through trusted curation, thoughtful automation, and technology that belongs naturally in the space.</p><blockquote>We believe luxury is not complexity. <strong>Luxury is confidence.</strong></blockquote></div></section><section class="section section-dark"><div class="section-heading"><p class="eyebrow">Leadership</p><h2>Two disciplines. One customer experience.</h2></div><div class="founder-grid"><article class="founder-card"><img class="founder-photo" src="/assets/bridgette-beardsley.jpg" alt="Bridgette Beardsley"><h3>Bridgette Beardsley</h3><p class="role">${escapeHtml(LEADERSHIP.bridgette.role)}</p><p>${escapeHtml(LEADERSHIP.bridgette.compactBiography)}</p></article><article class="founder-card"><img class="founder-photo" src="/assets/sheldon-bardol.jpg" alt="Sheldon Bardol"><h3>Sheldon Bardol</h3><p class="role">${escapeHtml(LEADERSHIP.sheldon.role)}</p><p>${escapeHtml(LEADERSHIP.sheldon.compactBiography)}</p></article></div></section><section class="section"><div class="section-heading"><p class="eyebrow">Our Promise</p><h2>Quiet technology. Clear guidance.</h2></div><div class="promise-grid"><div>Begin with the customer's desired experience.</div><div>Make compatibility and limitations understandable.</div><div>Curate with purpose rather than overwhelm with choice.</div><div>Keep technology quiet, useful, and at home in the environment.</div></div></section>`;
}

function faqPage() {
  return `<section class="page-hero"><div><p class="eyebrow">The LuxSync FAQ Library</p><h1>Smart living, explained clearly.</h1><p>Get to know LuxSync, find your starting point, and learn how to keep building your plan.</p><div class="button-row"><a class="button" href="#about-luxsync">Browse answers</a><a class="text-link" href="#video-guides">Video guide links →</a></div></div></section><section class="section">${faqLibrary(faqs)}<div class="section-cta"><p>Still have a question?</p><a class="button" href="/contact/">Contact LuxSync</a></div></section>`;
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
  '/guides': guideLibrary,
  '/account': () => workspaceAccount(false),
  '/account/create': () => workspaceAccount(true),
  '/account/welcome': accountDashboard,
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
    '/account': ['Member Sign In', 'Sign in securely to access your LuxSync account, orders, and saved recommendations.'],
    '/account/create': ['Create Your LuxSync Account', 'Create a secure LuxSync member account to save preferences, follow orders, and revisit recommendations.'],
    '/account/welcome': ['Welcome Back', 'Access orders, saved recommendations, support, and LuxSync account preferences.'],
    '/guides': ['ROI Guide Library', 'Explore LuxSync ROI guides for commercial, STR, residential, senior living, and caregiving environments.'],
    '/about': ['About LuxSync', 'Learn how LuxSync simplifies smart living through trusted curation, thoughtful automation, and intelligent guidance.'],
    '/faqs': ['Frequently Asked Questions', 'Answers about LuxSync, smart-home basics, Concierge, accounts, ROI guides, bundles, setup, and video resources.'],
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
fs.mkdirSync(path.join(DIST, 'assets', 'icons'), { recursive: true });
fs.mkdirSync(path.join(DIST, 'assets', 'dividers'), { recursive: true });

for (const file of ['luxsync-horizontal-combo.png', 'luxsync-horizontal.png', 'luxsync-orb.png']) {
  fs.copyFileSync(path.join(BRAND, file), path.join(DIST, 'assets', file));
}
for (const file of fs.readdirSync(ICONS)) fs.copyFileSync(path.join(ICONS,file),path.join(DIST,'assets','icons',file));
for (const file of fs.readdirSync(DIVIDERS)) fs.copyFileSync(path.join(DIVIDERS,file),path.join(DIST,'assets','dividers',file));
fs.copyFileSync(ENGINE, path.join(DIST, 'data', 'luxsync-concierge-engine.v1.json'));
fs.writeFileSync(path.join(DIST,'styles.css'), fs.readFileSync(path.join(HERE,'src','styles.css'),'utf8') + '\n' + fs.readFileSync(path.join(HERE,'src','brand-refresh.css'),'utf8'));
fs.copyFileSync(path.join(HERE,'src','icon-map.js'),path.join(DIST,'icon-map.js'));
fs.copyFileSync(path.join(HERE,'src','account-workspace.js'),path.join(DIST,'account-workspace.js'));
fs.appendFileSync(path.join(DIST,'styles.css'),fs.readFileSync(path.join(HERE,'src','roi-workspace.css'),'utf8'));
fs.mkdirSync(path.join(DIST,'assets','roi'),{recursive:true});
fs.copyFileSync(path.join(HERE,'src','roi','cover-master.png'),path.join(DIST,'assets','roi','cover-master.png'));
fs.cpSync(path.join(HERE,'src','roi','pdfs'),path.join(DIST,'downloads','roi'),{recursive:true});
fs.writeFileSync(path.join(DIST,'data','roi-guides.json'),JSON.stringify(guides));
fs.cpSync(path.join(HERE,'src','heroes'),path.join(DIST,'assets','heroes'),{recursive:true});
fs.copyFileSync(path.join(HERE, 'src', 'app.js'), path.join(DIST, 'app.js'));
fs.copyFileSync(path.join(HERE, 'src', 'og.png'), path.join(DIST, 'assets', 'og.png'));
for (const file of [
  'bridgette-beardsley.jpg','sheldon-bardol.jpg','homepage-intelligent-living.png','member-access.png',
  'plush-drift-residential.png','plush-drift-commercial.png','plush-drift-rental.png',
  'plush-drift-care.png','plush-drift-concierge.png','plush-drift-energy.png','intelligent-living-master-v1.png'
]) fs.copyFileSync(path.join(HERE,'src',file),path.join(DIST,'assets',file));

for (const image of ['rental','care','commercial','residential','energy']) fs.copyFileSync(path.join(HERE,'src',`featured-${image}.png`),path.join(DIST,'assets',`featured-${image}.png`));

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
  const builder = route==='/solutions/residential' ? ()=>propertyHub('residential') : pageBuilders[route] || (solutionPages[route] ? () => solutionDetail(route) : null);
  if (!builder) throw new Error(`No page builder for ${rawRoute}`);
  const [title, description] = pageMeta(route);
  const dir = routePath(rawRoute);
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, 'index.html'), shell({ route, title, description, main: builder() }));
}

fs.writeFileSync(path.join(DIST, '404.html'), shell({ route: '/404', title: 'Page Not Found', description: 'The requested LuxSync page could not be found.', main: `<section class="page-hero"><div><p class="eyebrow">404</p><h1>This room is not in the Blueprint.</h1><p>The page you requested could not be found.</p><a class="button" href="/">Return Home</a></div></section>` }));

fs.writeFileSync(path.join(DIST, '.htaccess'), `Options -MultiViews\nErrorDocument 404 /404.html\nDirectoryIndex index.html\n`);
console.log(`Built LuxSync site with ${routes.length} governed routes.`);





const searchPages = routes.filter(route=>!route.startsWith('/account') && !route.startsWith('/my-luxsync-blueprint')).map(raw=>{
  const route = raw === '/' ? '/' : raw.replace(/\/$/,'');
  const html = fs.readFileSync(path.join(routePath(raw),'index.html'),'utf8');
  const text = (html.match(/<main[^>]*>([\s\S]*?)<\/main>/)?.[1] || '').replace(/<[^>]*>/g,' ').replace(/&amp;/g,'&').replace(/\s+/g,' ').trim();
  return {url: route === '/' ? '/' : route+'/', title:pageMeta(route)[0],text};
});
for(const family of catalog.families) searchPages.push({url:'/shop/',title:family.name,text:family.description||''});
for(const faq of faqs) searchPages.push({url:'/faqs/#'+faq.id,title:faq.question,text:faq.answer||''});
fs.writeFileSync(path.join(DIST,'data','search.json'),JSON.stringify(searchPages,null,2));

for(const guide of guides) {
  const dir=path.join(DIST,'guides',guide.id);fs.mkdirSync(dir,{recursive:true});
  fs.writeFileSync(path.join(dir,'index.html'),shell({route:'/guides/'+guide.id,title:guide.title+' ROI Guide',description:guide.audience,main:guidePage(guide)}));
}
fs.mkdirSync(path.join(HERE,'dist','server'),{recursive:true});
await bundleWorker({entryPoints:[path.join(HERE,'server','worker.mjs')],outfile:path.join(HERE,'dist','server','index.js'),bundle:true,format:'esm',platform:'browser',target:'es2022'});
fs.mkdirSync(path.join(HERE,'dist','.openai'),{recursive:true});
fs.copyFileSync(path.join(HERE,'.openai','hosting.json'),path.join(HERE,'dist','.openai','hosting.json'));
fs.cpSync(path.join(HERE,'drizzle'),path.join(HERE,'dist','.openai','drizzle'),{recursive:true});
console.log('Built 10 downloadable and online ROI guides plus the account storage service.');

for(const file of ['client.js','device-icons.js'])fs.copyFileSync(path.join(HERE,'src','store',file),path.join(DIST,file==='client.js'?'store-client.js':file));
fs.copyFileSync(path.join(HERE,'src','store','catalog.json'),path.join(DIST,'data','store-catalog.json'));
fs.appendFileSync(path.join(DIST,'styles.css'),fs.readFileSync(path.join(HERE,'src','store','store.css'),'utf8'));
for(const page of storeRoutes){const dir=routePath(page.route);fs.mkdirSync(dir,{recursive:true});fs.writeFileSync(path.join(dir,'index.html'),shell({route:page.route,title:page.title,description:page.description,main:page.main()}));if(!page.route.startsWith('/account'))searchPages.push({url:page.route+'/',title:page.title,text:page.description});}
fs.writeFileSync(path.join(DIST,'data','search.json'),JSON.stringify(searchPages));

function propertyChoice(){return '<section class="page-hero"><div><p class="eyebrow">LuxSync Solutions</p><h1>What kind of property are you planning for?</h1><p>Choose your starting point. We’ll help you find relevant experiences, bundles, and guides.</p></div></section><section class="section"><div class="property-grid">'+card('Commercial','For workplaces, rental operations, and senior living communities.','/solutions/commercial/','hero:plush-drift-commercial')+card('Residential','For your home, everyday routines, and independent living.','/solutions/residential/','hero:plush-drift-residential')+'</div></section>';}
function propertyHub(type){const commercial=type==='commercial';const choices=commercial?[['Offices & Workplaces','Coordinate lighting, comfort, energy, and awareness around your working day.','/solutions/commercial-offices/','plush-drift-commercial'],['Rental Properties','Plan guest access, turnovers, and property awareness for your rental operation.','/solutions/short-term-rentals/','plush-drift-rental'],['Senior Living Communities','Thoughtful controls and routines for managed senior living spaces.','/solutions/senior-living/','aging-in-place']]:[['Homes & Everyday Living','Comfort, ambience, convenience, and connected routines for your household.','/solutions/residential/homes/','plush-drift-residential'],['Aging in Place & Caregiving','Everyday ease and independence for a private home.','/solutions/aging-in-place/','plush-drift-care']];return '<section class="page-hero image-led"><img class="page-hero-image" src="/assets/heroes/plush-drift-'+(commercial?'commercial':'residential')+'-1600.webp" alt=""><div class="page-hero-copy"><p class="eyebrow">'+(commercial?'Commercial':'Residential')+' Solutions</p><h1>'+(commercial?'A property that works with you.':'A home that fits your life.')+'</h1><p>'+(commercial?'Plan connected experiences for the spaces you operate.':'Bring comfort, control, and thoughtful routines into your home.')+'</p></div></section><section class="section"><h2>'+(commercial?'What type of property do you operate?':'What would you like to plan for?')+'</h2><p>Choose a path to see the relevant solutions and next steps.</p><div class="property-grid">'+choices.map(([a,b,c,d])=>card(a,b,c+'?solution='+type,'hero:'+d)).join('')+'</div><div class="button-row section-more"><a class="button" href="/find-my-luxsync-solution/?solution='+type+'">Help me choose</a><a class="button button-secondary" href="/shop/?solution='+type+'">Browse products & bundles</a><a class="text-link" href="/guides/?solution='+type+'">'+(commercial?'Commercial':'Residential')+' ROI guides →</a></div><p>Every product can be added to the same cart. Your property choice guides browsing and does not restrict what you can select.</p></section>';}
for(const [route,title,main] of [['/solutions/commercial','Commercial Property Solutions',propertyHub('commercial')],['/solutions/residential/homes','Homes & Everyday Living',decoratePage('/solutions/residential',solutionDetail('/solutions/residential'))]]){const dir=routePath(route);fs.mkdirSync(dir,{recursive:true});fs.writeFileSync(path.join(dir,'index.html'),shell({route,title,description:title,main}));searchPages.push({url:route+'/',title,text:title});}
fs.copyFileSync(path.join(HERE,'src','property-flow.js'),path.join(DIST,'property-flow.js'));
fs.writeFileSync(path.join(DIST,'data','search.json'),JSON.stringify(searchPages));
