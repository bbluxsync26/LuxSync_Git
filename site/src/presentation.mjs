// Shared LuxSync imagery and navigation. Assets come from the local brand library.
export const heroAssets = {
  '/': ['homepage-intelligent-living', 'A warmly lit living room opening onto a twilight terrace'],
  '/solutions': ['solutions', 'An open modern home with concealed amber lighting at dusk'],
  '/solutions/commercial-offices': ['plush-drift-commercial', 'A calm office lounge and meeting space with integrated lighting'],
  '/solutions/senior-living': ['aging-in-place', 'A couple relaxing in a comfortable, softly illuminated living room'],
  '/solutions/short-term-rentals': ['plush-drift-rental', 'Luggage beside a smart entry door in a welcoming rental home'],
  '/solutions/residential': ['plush-drift-residential', 'An evening living room with concealed lighting and a warm fireplace'],
  '/solutions/aging-in-place': ['plush-drift-care', 'A woman walking through her home beside softly lit steps'],
  '/find-my-luxsync-solution': ['plush-drift-concierge', 'A refined reception lounge with warm architectural lighting'],
  '/my-luxsync-blueprint': ['professionals', 'A thoughtful workspace overlooking the city at twilight'],
  '/shop': ['shop', 'Smart home controls arranged on a stone surface in a warm interior'],
  '/guides': ['library-cover', 'A modern illuminated home framed with understated metallic detailing'],
  '/account': ['member-access', 'A quiet private lounge with warm concealed lighting'],
  '/account/create': ['families', 'A family sharing a moment in a thoughtfully lit kitchen'],
  '/account/welcome': ['plush-drift-energy', 'A sunlit home with integrated shades and efficient natural light'],
  '/about': ['about', 'A welcoming conversation space framed by wood and warm shelves'],
  '/faqs': ['support', 'A person setting up a smart home device beside a tablet'],
  '/contact': ['contact', 'A welcoming reception desk with an amber illuminated base']
};

const escape = value => String(value).replaceAll('&','&amp;').replaceAll('"','&quot;').replaceAll('<','&lt;');
export function heroImage(route, className = 'page-hero-image') {
  const [name, alt] = heroAssets[route];
  return `<img class="${className}" src="/assets/heroes/${name}-1600.webp" srcset="/assets/heroes/${name}-720.webp 720w, /assets/heroes/${name}-1600.webp 1600w" sizes="100vw" width="1600" height="900" alt="${escape(alt)}" fetchpriority="high">`;
}

export function headerControls() {
  const svg = inner => `<svg class="control-icon" viewBox="0 0 24 24" aria-hidden="true">${inner}</svg>`;
  return `<div class="header-actions" role="group" aria-label="Quick actions">
    <a class="utility-icon concierge-nav" href="/find-my-luxsync-solution/" aria-label="LuxSync Concierge" title="LuxSync Concierge"><img src="/assets/icons/concierge-bell.webp" width="26" height="26" alt=""></a>
    <a class="utility-icon account-nav" href="/account/" aria-label="Account" title="Account">${svg('<circle class="metal-steel" cx="12" cy="7.5" r="3.6"/><path class="metal-rose" d="M4.5 21v-2a7.5 7.5 0 0 1 15 0v2"/>')}</a>
    <a class="utility-icon cart-nav" href="/cart/" aria-label="Shopping cart" title="Shopping cart">${svg('<path class="metal-steel" d="M2.5 3.5H5L7.2 15h11L21 7H6"/><path class="metal-rose" d="M8 10h11M9 13h9"/><circle class="metal-rose" cx="9" cy="20" r="1.25"/><circle class="metal-rose" cx="18" cy="20" r="1.25"/>')}<span class="cart-count" data-cart-count>0</span></a>
    <button class="utility-icon search-nav" type="button" aria-label="Search LuxSync" title="Search LuxSync" aria-haspopup="dialog" aria-controls="site-search">${svg('<circle class="metal-steel" cx="10.5" cy="10.5" r="6.8"/><path class="metal-rose" d="m15.7 15.7 5 5"/>')}</button>
  </div>`;
}

export const searchDialog = `<dialog id="site-search" class="search-dialog" aria-labelledby="search-title"><div class="search-dialog-top"><h2 id="search-title">Search LuxSync</h2><button type="button" class="button search-close" aria-label="Close search">Close</button></div><label for="site-search-input">What would you like to explore?</label><input id="site-search-input" type="search" placeholder="Try lighting, rentals, or support" autocomplete="off"><p class="search-status" role="status"></p><div class="search-results"></div></dialog>`;

export function decoratePage(route, main) {
  if (!heroAssets[route] || route === '/') return main;
  if (route === '/about') {
    main += `<section class="section"><div class="section-heading"><p class="eyebrow">Why LuxSync</p><h2>From possibility to a practical plan.</h2></div><div class="feature-list"><div><strong>Purposeful curation</strong><span>A considered catalog, organized around useful experiences and compatible foundations.</span></div><div><strong>Clear compatibility</strong><span>A SmartThings-first approach, with product requirements and limitations explained before you choose.</span></div><div><strong>Personal guidance</strong><span>Discovery starts with your routines. Products, bundles, and a phased Blueprint follow from those priorities.</span></div></div></section>`;
  }
  if (route === '/find-my-luxsync-solution') {
    main += `<section class="section section-soft"><div class="section-heading"><p class="eyebrow">How it works</p><h2>From your first idea to everyday ease.</h2></div><ol class="steps"><li><span>01</span><div><h3>Discover</h3><p>Tell us about your space, routines, and priorities.</p></div></li><li><span>02</span><div><h3>Design</h3><p>Review recommended experiences in My LuxSync Blueprint.</p></div></li><li><span>03</span><div><h3>Choose</h3><p>Select products and bundles after compatibility is confirmed.</p></div></li><li><span>04</span><div><h3>Evolve</h3><p>Add compatible experiences as your needs grow.</p></div></li></ol></section>`;
  }
  if (route.startsWith('/account')) {
    return main.replace(/<img src="\/assets\/(?:member-access|homepage-intelligent-living)[^"]*" alt="[^"]*">/, heroImage(route,'account-scene'));
  }
  return main.replace(/<section class="page-hero([^"]*)"><div>/, `<section class="page-hero image-led$1">${heroImage(route)}<div class="page-hero-copy">`);
}

export function homeOverview({HOME, SLOGAN, card}) {
  const featured = [
    ['Commercial','Connected workplaces, rental properties, and senior living communities.','/solutions/commercial/','commercial'],
    ['Residential','Comfort, convenience, and independent living for your home.','/solutions/residential/','residential']
  ];
  return `<section class="hero home-hero">${heroImage('/','home-hero-image')}<div class="home-hero-copy"><p class="eyebrow">Smart living. Thoughtfully curated.</p><h1>${escape(SLOGAN)}</h1><p class="hero-lede">${escape(HOME.supportingCopy)}</p><div class="button-row"><a class="button" href="/find-my-luxsync-solution/">${escape(HOME.primaryCta)}</a><a class="button button-secondary" href="/shop/">${escape(HOME.secondaryCta)}</a></div></div><div class="hero-caption">Comfort · Control · Confidence</div></section>
  <section class="section company-overview"><p class="eyebrow">The LuxSync approach</p><div><h2>Technology that belongs<br>in the way you live.</h2><p>We bring together curated smart-home products, compatible automation, and personal guidance—for homes, rental properties, and workplaces.</p><a class="text-link" href="/about/">Get to know LuxSync →</a></div></section>
  <section class="section featured-section" id="featured-solutions"><div class="section-heading"><p class="eyebrow">Featured Solutions</p><h2>Find your kind of intelligent living.</h2></div><div class="property-grid">${featured.map(args=>card(...args)).join('')}</div><a class="text-link section-more" href="/solutions/">Explore all solutions →</a></section>
  <section class="section concierge-overview"><div class="concierge-intro"><img src="/assets/icons/concierge-bell.webp" alt="" width="64" height="64"><p class="eyebrow">Your LuxSync Concierge</p><h2>Start with your day.<br>We’ll help with the details.</h2><p>Tell us what matters in your space. Get a personalized Blueprint with recommended experiences and practical next steps.</p><a class="button" href="/find-my-luxsync-solution/">Find My LuxSync Solution</a></div><ol class="journey-teasers"><li><span>01</span><div><h3>Discover</h3><p>Your space, your routines, your priorities.</p></div></li><li><span>02</span><div><h3>Plan</h3><p>A compatible foundation and a clear path forward.</p></div></li><li><span>03</span><div><h3>Evolve</h3><p>Start with what matters. Build at your own pace.</p></div></li></ol></section>
  <section class="section next-chapters"><div class="section-heading"><p class="eyebrow">A little guidance goes a long way</p><h2>Explore what comes next.</h2></div><div class="card-grid">${card('Curated technology','Explore lighting, climate, access, and more.','/shop/')}${card('Make an informed plan','Find the ROI guide for your home or property.','/guides/')}${card('Real people. Clear answers.','Meet our founders and the thinking behind LuxSync.','/about/')}</div><div class="button-row section-more"><a class="text-link" href="/guides/">${escape(HOME.supportingCta)} →</a><a class="text-link" href="/faqs/">Browse the FAQs →</a><a class="text-link" href="/contact/">Talk with LuxSync →</a></div></section>`;
}
