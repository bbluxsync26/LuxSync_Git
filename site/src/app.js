const CONFIG = window.LUXSYNC_CONFIG || {};
const qs = (selector, root = document) => root.querySelector(selector);
const qsa = (selector, root = document) => [...root.querySelectorAll(selector)];
const escapeHtml = (value = '') => String(value)
  .replaceAll('&', '&amp;')
  .replaceAll('<', '&lt;')
  .replaceAll('>', '&gt;')
  .replaceAll('"', '&quot;')
  .replaceAll("'", '&#039;');

async function fetchJson(url) {
  const response = await fetch(url, { headers: { Accept: 'application/json' } });
  if (!response.ok) throw new Error(`Unable to load ${url}`);
  return response.json();
}

function initNavigation() {
  const toggle = qs('.nav-toggle');
  const nav = qs('#main-nav');
  if (!toggle || !nav) return;
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!open));
    nav.classList.toggle('is-open', !open);
  });
}

function faqMarkup(item, index) {
  const id = `faq-answer-${index}`;
  return `<article class="faq-item"><h3><button type="button" aria-expanded="false" aria-controls="${id}"><span>${escapeHtml(item.question)}</span><span aria-hidden="true">＋</span></button></h3><div id="${id}" class="faq-answer" hidden><p>${escapeHtml(item.answer)}</p></div></article>`;
}

function wireFaqs(root) {
  qsa('.faq-item button', root).forEach((button) => {
    button.addEventListener('click', () => {
      const expanded = button.getAttribute('aria-expanded') === 'true';
      const answer = document.getElementById(button.getAttribute('aria-controls'));
      button.setAttribute('aria-expanded', String(!expanded));
      if (answer) answer.hidden = expanded;
      const icon = button.lastElementChild;
      if (icon) icon.textContent = expanded ? '＋' : '−';
    });
  });
}

async function initFaqs() {
  const preview = qs('#faq-preview');
  const full = qs('#faq-full');
  if (!preview && !full) return;
  try {
    const faqs = await fetchJson('/data/faqs.json');
    if (preview) {
      preview.innerHTML = faqs.slice(0, 6).map(faqMarkup).join('');
      wireFaqs(preview);
    }
    if (full) {
      full.innerHTML = faqs.map(faqMarkup).join('');
      wireFaqs(full);
    }
  } catch (error) {
    const target = full || preview;
    target.innerHTML = `<p class="form-error">FAQ content could not be loaded. Please contact <a href="mailto:info@luxsync.net">info@luxsync.net</a>.</p>`;
  }
}

function catalogCard(item) {
  return `<article class="lux-card"><span class="card-glint" aria-hidden="true"></span><span class="status-chip">${escapeHtml(item.status)}</span><h3>${escapeHtml(item.name)}</h3><p>${escapeHtml(item.description || item.note || '')}</p></article>`;
}

async function initCatalog() {
  const home = qs('#home-catalog');
  const families = qs('#shop-families');
  const bundles = qs('#shop-bundles');
  const experiences = qs('#shop-experiences');
  const commerceLink = qs('#commerce-link');
  if (!home && !families && !bundles && !experiences && !commerceLink) return;
  try {
    const catalog = await fetchJson('/data/catalog.json');
    if (home) home.innerHTML = catalog.families.slice(0, 6).map(catalogCard).join('');
    if (families) families.innerHTML = catalog.families.map(catalogCard).join('');
    if (bundles) bundles.innerHTML = catalog.bundles.map(catalogCard).join('');
    if (experiences) experiences.innerHTML = catalog.experiences.map((item) => `<span class="experience-chip">${escapeHtml(item.name)}</span>`).join('');
    if (commerceLink && CONFIG.commerceUrl) {
      commerceLink.href = CONFIG.commerceUrl;
      commerceLink.rel = 'noopener';
    }
  } catch (error) {
    [home, families, bundles].filter(Boolean).forEach((target) => {
      target.innerHTML = '<p class="form-error">Catalog structure could not be loaded.</p>';
    });
  }
}

function values(answer) {
  if (answer === undefined || answer === null || answer === '') return [];
  return Array.isArray(answer) ? answer : [answer];
}

function matchesWhen(profile, when = {}) {
  return Object.entries(when).every(([field, expected]) => {
    const actual = values(profile[field]);
    return expected.some((value) => actual.includes(value));
  });
}

function matchesWhenAny(profile, when = {}) {
  return Object.entries(when).some(([field, expected]) => {
    const actual = values(profile[field]);
    return expected.some((value) => actual.includes(value));
  });
}

function questionVisible(question, profile) {
  if (question.show_when && !matchesWhen(profile, question.show_when)) return false;
  if (question.show_when_any && !matchesWhenAny(profile, question.show_when_any)) return false;
  return true;
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
  const condition = bonus?.condition?.count_selected;
  if (!condition) return false;
  const selected = values(profile[condition.field]).filter((value) => !(condition.exclude || []).includes(value));
  if (condition.gte !== undefined && selected.length < condition.gte) return false;
  if (condition.gt !== undefined && selected.length <= condition.gt) return false;
  return true;
}

function resolveFoundation(profile, derived) {
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
  if (profile.current_setup_health === 'fragmented' || tech.includes('unknown_mix')) return { id: 'compatibility_review', label: 'Compatibility Review' };
  if (tech.includes('smartthings')) return { id: 'existing_smartthings_foundation', label: 'Existing SmartThings Foundation' };
  if (tech.includes('nothing_yet')) return { id: 'smartthings_foundation_recommended', label: 'SmartThings Foundation Recommended' };
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
  return { id, ...(engine.implementation_paths[id] || {}) };
}

function resolveCTA(engine, profile, flags) {
  const sorted = [...engine.cta_logic].sort((a, b) => b.priority - a.priority);
  for (const rule of sorted) {
    if (rule.default) return rule.cta;
    if (rule.when && matchesWhen(profile, rule.when)) return rule.cta;
    if (rule.when_flag && flags.has(rule.when_flag)) return rule.cta;
    if (rule.when_any_flag && rule.when_any_flag.some((flag) => flags.has(flag))) return rule.cta;
  }
  return { id: 'build_solution', label: 'Build My Solution' };
}

function tierFor(score, thresholds) {
  if (score >= thresholds.primary) return 'primary';
  if (score >= thresholds.strong) return 'strong';
  if (score >= thresholds.optional) return 'optional';
  return 'suppressed';
}

function evaluate(engine, profile) {
  const scores = Object.fromEntries(engine.experience_catalog.map((item) => [item.id, 0]));
  const flags = new Set();
  const derived = {};
  for (const rule of engine.scoring.rules) {
    if (!ruleMatches(profile, rule)) continue;
    for (const [id, points] of Object.entries(rule.add || {})) scores[id] = (scores[id] || 0) + points;
    for (const flag of rule.flags || []) flags.add(flag);
    Object.assign(derived, rule.adjustments || {});
  }
  for (const bonus of engine.scoring.context_bonuses || []) {
    if (!bonusMatches(profile, bonus)) continue;
    for (const [id, points] of Object.entries(bonus.add || {})) scores[id] = (scores[id] || 0) + points;
  }
  const priorityRank = values(profile.priority_rank).slice(0, 3);
  const multipliers = [engine.constants.priority_multipliers.priority_1, engine.constants.priority_multipliers.priority_2, engine.constants.priority_multipliers.priority_3];
  priorityRank.forEach((id, index) => {
    if (scores[id] !== undefined) scores[id] = Math.round(scores[id] * multipliers[index] * 100) / 100;
  });
  const catalog = Object.fromEntries(engine.experience_catalog.map((item) => [item.id, item]));
  let ranked = Object.entries(scores)
    .map(([id, score]) => ({ id, name: catalog[id]?.name || id, score, tier: tierFor(score, engine.constants.recommendation_thresholds) }))
    .filter((item) => item.score >= engine.constants.recommendation_thresholds.suppress_below)
    .sort((a, b) => b.score - a.score || a.name.localeCompare(b.name));
  const minimum = engine.constants.minimum_recommended_experiences;
  if (ranked.length < minimum) {
    const remaining = Object.entries(scores)
      .filter(([id]) => !ranked.some((item) => item.id === id))
      .map(([id, score]) => ({ id, name: catalog[id]?.name || id, score, tier: 'optional' }))
      .sort((a, b) => b.score - a.score)
      .slice(0, minimum - ranked.length);
    ranked = ranked.concat(remaining);
  }
  return {
    flags: [...flags].sort(),
    recommended_foundation: resolveFoundation(profile, derived),
    recommended_experiences: ranked.filter((item) => ['primary', 'strong'].includes(item.tier)),
    optional_experiences: ranked.filter((item) => item.tier === 'optional'),
    implementation_path: resolveImplementationPath(engine, profile, flags, ranked),
    next_best_action: resolveCTA(engine, profile, flags),
    all_scores: scores
  };
}

function renderQuestion(question, profile) {
  const required = question.required ? '<span class="required-mark" aria-hidden="true">*</span><span class="sr-only"> required</span>' : '';
  const current = profile[question.id];
  if (question.type === 'single_select' || question.type === 'multi_select') {
    const type = question.type === 'multi_select' ? 'checkbox' : 'radio';
    const options = (question.options || []).map((option, index) => {
      const selected = values(current).includes(option.value) ? ' checked' : '';
      const id = `${question.id}-${index}`;
      return `<div class="option-card"><input id="${escapeHtml(id)}" type="${type}" name="${escapeHtml(question.id)}" value="${escapeHtml(option.value)}"${selected}><label for="${escapeHtml(id)}">${escapeHtml(option.label)}</label></div>`;
    }).join('');
    return `<fieldset class="question-group" data-question="${escapeHtml(question.id)}"><legend>${escapeHtml(question.prompt)}${required}</legend><div class="option-grid">${options}</div></fieldset>`;
  }
  const value = current ?? '';
  const type = question.type === 'number' ? 'number' : 'text';
  const min = question.validation?.min !== undefined ? ` min="${question.validation.min}"` : '';
  const max = question.validation?.max !== undefined ? ` max="${question.validation.max}"` : '';
  return `<div class="field question-group" data-question="${escapeHtml(question.id)}"><label for="${escapeHtml(question.id)}">${escapeHtml(question.prompt)}${required}</label><input id="${escapeHtml(question.id)}" type="${type}" name="${escapeHtml(question.id)}" value="${escapeHtml(value)}"${min}${max}${question.required ? ' required' : ''}></div>`;
}

async function initConcierge() {
  const root = qs('#concierge-app');
  if (!root) return;
  try {
    const engine = await fetchJson('/data/luxsync-concierge-engine.v1.json');
    let profile = {};
    try { profile = JSON.parse(localStorage.getItem('luxsyncProfile') || '{}'); } catch { profile = {}; }
    let stageIndex = Number(sessionStorage.getItem('luxsyncStageIndex') || 0);
    if (!Number.isInteger(stageIndex) || stageIndex < 0 || stageIndex >= engine.questionnaire.length) stageIndex = 0;

    function collectVisibleAnswers(stage) {
      const visible = stage.questions.filter((q) => questionVisible(q, profile));
      for (const question of visible) {
        if (question.type === 'multi_select') {
          profile[question.id] = qsa(`input[name="${CSS.escape(question.id)}"]:checked`, root).map((input) => input.value);
        } else if (question.type === 'single_select') {
          const checked = qs(`input[name="${CSS.escape(question.id)}"]:checked`, root);
          profile[question.id] = checked ? checked.value : '';
        } else {
          const input = qs(`[name="${CSS.escape(question.id)}"]`, root);
          profile[question.id] = input?.value ?? '';
        }
      }
      localStorage.setItem('luxsyncProfile', JSON.stringify(profile));
      return visible;
    }

    function validateStage(stage) {
      const visible = collectVisibleAnswers(stage);
      const missing = visible.filter((question) => question.required && values(profile[question.id]).length === 0);
      const error = qs('#concierge-error', root);
      if (missing.length) {
        error.hidden = false;
        error.textContent = 'Please answer the required questions before continuing.';
        const first = qs(`[data-question="${CSS.escape(missing[0].id)}"] input`, root);
        first?.focus();
        return false;
      }
      error.hidden = true;
      return true;
    }

    function renderStage() {
      const stage = engine.questionnaire[stageIndex];
      const visibleQuestions = stage.questions.filter((q) => questionVisible(q, profile));
      const progress = Math.round(((stageIndex + 1) / engine.questionnaire.length) * 100);
      root.innerHTML = `<div class="app-topbar"><div class="app-progress-label"><span>${escapeHtml(stage.progress_label || stage.stage_label)}</span><span>${stageIndex + 1} of ${engine.questionnaire.length}</span></div><div class="app-progress" aria-label="Concierge progress"><span style="width:${progress}%"></span></div></div><div class="app-content"><p class="eyebrow">${escapeHtml(stage.stage_label)}</p><h2>${stageIndex === 0 ? 'Let’s design how your space lives.' : escapeHtml(stage.progress_label || 'Creating Your Blueprint')}</h2><p class="app-intro">Your answers stay in this browser while you build your Blueprint. You can move backward without losing progress.</p><form id="concierge-form" novalidate><div class="question-stack">${visibleQuestions.map((question) => renderQuestion(question, profile)).join('')}</div><div id="concierge-error" class="form-error" role="alert" hidden></div><div class="app-actions">${stageIndex > 0 ? '<button class="button button-secondary" type="button" data-back>Back</button>' : '<span></span>'}<div class="button-row"><button class="button" type="submit">${stageIndex === engine.questionnaire.length - 1 ? 'Create My Blueprint' : 'Continue'}</button></div></div></form></div>`;
      qsa('input', root).forEach((input) => {
        input.addEventListener('change', () => {
          collectVisibleAnswers(stage);
          const newVisible = stage.questions.filter((q) => questionVisible(q, profile));
          if (newVisible.length !== visibleQuestions.length) renderStage();
        });
      });
      qs('[data-back]', root)?.addEventListener('click', () => {
        collectVisibleAnswers(stage);
        stageIndex -= 1;
        sessionStorage.setItem('luxsyncStageIndex', String(stageIndex));
        renderStage();
        root.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
      qs('#concierge-form', root)?.addEventListener('submit', (event) => {
        event.preventDefault();
        if (!validateStage(stage)) return;
        if (stageIndex < engine.questionnaire.length - 1) {
          stageIndex += 1;
          sessionStorage.setItem('luxsyncStageIndex', String(stageIndex));
          renderStage();
          root.scrollIntoView({ behavior: 'smooth', block: 'start' });
          return;
        }
        const result = evaluate(engine, profile);
        const blueprint = {
          id: globalThis.crypto?.randomUUID?.() || `luxsync-${Date.now()}`,
          createdAt: new Date().toISOString(),
          engineVersion: engine.meta?.config_version || engine.meta?.version || '1',
          profile,
          result
        };
        localStorage.setItem('luxsyncBlueprint', JSON.stringify(blueprint));
        sessionStorage.removeItem('luxsyncStageIndex');
        window.location.assign('/my-luxsync-blueprint/');
      });
    }
    renderStage();
  } catch (error) {
    root.innerHTML = `<div class="empty-state"><h2>The Concierge could not load.</h2><p>Please try again, or contact LuxSync for guided help.</p><a class="button" href="/contact/?intent=consultation">Request Consultation</a></div>`;
  }
}

function blueprintList(items = []) {
  if (!items.length) return '<p>No additional items were surfaced in this category.</p>';
  return `<ul>${items.map((item) => `<li><strong>${escapeHtml(item.name)}</strong>${Number.isFinite(item.score) ? ` <span class="sr-only">score ${item.score}</span>` : ''}</li>`).join('')}</ul>`;
}

function humanize(value = '') {
  return String(value).replaceAll('_', ' ').replace(/\b\w/g, (m) => m.toUpperCase());
}


function recommendedBundle(b){const e=(b.result?.recommended_experiences||[]).map(x=>x.name),r=[["Entry & Access",/departure|away|vacation|guest|opening|closing/i],["Lighting & Ambience",/welcome|goodnight|morning|evening|night path|cinema|entertain|relax|accessible/i],["Comfort & Climate",/climate|morning|goodnight|guest/i],["Property Awareness",/protect|pulse|turnover|away|vacation/i],["Water Protection",/water/i],["Energy & Power",/energy/i],["Entertainment & Ambience",/cinema|entertain|relax/i]];return{id:"blueprint-"+b.id,name:"My LuxSync Recommended Bundle",foundation:b.result?.recommended_foundation?.label||"Compatibility review recommended",experiences:e,families:r.filter(([,x])=>e.some(n=>x.test(n))).map(([n])=>n)}}
function readCart(){try{return JSON.parse(localStorage.getItem("luxsyncCart")||"[]")}catch{return[]}}
function writeCart(c){localStorage.setItem("luxsyncCart",JSON.stringify(c));qsa("[data-cart-count]").forEach(n=>n.textContent=String(c.length))}
function itemList(x=[]){return x.length?"<ul>"+x.map(n=>"<li>"+escapeHtml(n)+"</li>").join("")+"</ul>":"<p>LuxSync will confirm the right product families during compatibility review.</p>"}

function initBlueprint() {
  const root = qs('#blueprint-app');
  if (!root) return;
  let blueprint;
  try { blueprint = JSON.parse(localStorage.getItem('luxsyncBlueprint') || 'null'); } catch { blueprint = null; }
  if (!blueprint) {
    root.innerHTML = `<div class="empty-state"><h2>Your Blueprint begins with the Concierge.</h2><p>Tell LuxSync about your space, priorities, routines, and existing technology to create a personalized intelligent-living direction.</p><a class="button" href="/find-my-luxsync-solution/">LuxSync Concierge</a></div>`;
    return;
  }
  const { profile, result } = blueprint;
  const path = result.implementation_path || {};
  const pathLabel = path.label || path.name || humanize(path.id);
  const ctaLabel = result.next_best_action?.label || 'Talk With LuxSync';
  const bundle = recommendedBundle(blueprint);
  root.innerHTML = `<div class="blueprint-hero"><p class="blueprint-id">Blueprint ${escapeHtml(blueprint.id)}</p><h2>Your intelligent-living direction is ready.</h2><p>LuxSync starts with your desired experiences, then uses compatibility and implementation context to guide the technology behind them.</p><div class="blueprint-grid"><article class="blueprint-card"><h3>Your Space</h3><p>${escapeHtml(humanize(profile.property_type || 'Not specified'))}${profile.square_feet_band ? ` · ${escapeHtml(humanize(profile.square_feet_band))}` : ''}</p></article><article class="blueprint-card"><h3>Recommended Foundation</h3><p>${escapeHtml(result.recommended_foundation?.label || 'Compatibility review recommended')}</p></article><article class="blueprint-card"><h3>Recommended Experiences</h3>${blueprintList(result.recommended_experiences)}</article><article class="blueprint-card"><h3>Optional Experiences</h3>${blueprintList(result.optional_experiences)}</article><article class="blueprint-card"><h3>Implementation Path</h3><p>${escapeHtml(pathLabel)}</p></article><article class="blueprint-card"><h3>Why LuxSync Chose This</h3><p>Your recommendations reflect the routines, priorities, property context, pain points, implementation preference, and technology information you shared.</p></article></div><article class="recommended-bundle"><p class="eyebrow">Your Recommended Bundle</p><h3>${escapeHtml(bundle.name)}</h3><p>One planning bundle built from your recommended foundation and experiences.</p><div class="bundle-columns"><div><h4>Foundation</h4><p>${escapeHtml(bundle.foundation)}</p></div><div><h4>Experiences</h4>${itemList(bundle.experiences)}</div><div><h4>Product families to validate</h4>${itemList(bundle.families)}</div></div><p class="bundle-disclaimer">Exact products, compatibility, availability, and pricing are confirmed before checkout.</p><div class="button-row"><button class="button" type="button" id="add-bundle-to-cart">Add Recommended Bundle to Cart</button><a class="button button-secondary" href="/shop/#planning-cart">View Cart</a></div><p id="bundle-cart-status" class="cart-status" role="status" aria-live="polite"></p></article><div class="button-row blueprint-actions"><a class="button" href="/contact/?intent=consultation&source=blueprint">${escapeHtml(ctaLabel)}</a><a class="button button-secondary" href="/shop/">Explore Product Families</a><button class="button button-secondary" type="button" id="restart-blueprint">Start Over</button></div></div>`;
  qs("#add-bundle-to-cart",root)?.addEventListener("click",e=>{const c=readCart().filter(x=>x.id!==bundle.id);c.push(bundle);writeCart(c);e.currentTarget.textContent="Bundle Added";qs("#bundle-cart-status",root).textContent="Your recommended bundle is in the cart and ready for validation."});
  qs('#restart-blueprint', root)?.addEventListener('click', () => {
    localStorage.removeItem('luxsyncBlueprint');
    localStorage.removeItem('luxsyncProfile');
    sessionStorage.removeItem('luxsyncStageIndex');
    window.location.assign('/find-my-luxsync-solution/');
  });
}


function initCart(){const c=readCart();writeCart(c);const r=qs("#planning-cart");if(!r)return;if(!c.length){r.innerHTML='<div class="empty-state"><h2>Your cart is ready for a Blueprint.</h2><p>Complete the Concierge and add your recommended bundle here.</p><a class="button" href="/find-my-luxsync-solution/">LuxSync Concierge</a></div>';return}r.innerHTML='<div class="section-heading"><p class="eyebrow">Planning Cart</p><h2>Your recommended bundle</h2><p>Review the bundled direction before LuxSync validates exact products, compatibility, availability, and pricing.</p></div><div class="cart-items">'+c.map(x=>'<article class="cart-item"><div><span class="status-chip">Blueprint bundle</span><h3>'+escapeHtml(x.name)+'</h3><p>'+escapeHtml(x.foundation)+'</p></div><div><h4>Included experiences</h4>'+itemList(x.experiences)+'</div><div><h4>Product families</h4>'+itemList(x.families)+'</div><button class="text-link cart-remove" type="button" data-remove-cart="'+escapeHtml(x.id)+'">Remove</button></article>').join("")+'</div><div class="cart-checkout"><p><strong>Next step:</strong> LuxSync will translate this planning bundle into validated, purchasable products.</p><a class="button" href="'+(CONFIG.commerceUrl?escapeHtml(CONFIG.commerceUrl):"/contact/?intent=product_information&source=cart")+'">'+(CONFIG.commerceUrl?"Continue to Store":"Validate Bundle With LuxSync")+'</a></div>';qsa("[data-remove-cart]",r).forEach(b=>b.addEventListener("click",()=>{writeCart(readCart().filter(x=>x.id!==b.dataset.removeCart));initCart()}))}

const contactIntents = {
  support: { label: 'Support', description: 'Existing product, solution, setup, compatibility, order, or troubleshooting help.', route: 'support@luxsync.net', submit: 'Send Support Request' },
  product_information: { label: 'Product Information', description: 'Questions about LuxSync product families, compatibility, bundles, or solution concepts.', route: 'info@luxsync.net', submit: 'Request Information' },
  consultation: { label: 'Consultation', description: 'Plan a new smart space, upgrade an existing setup, or review My LuxSync Blueprint.', route: 'info@luxsync.net', submit: 'Request Consultation' },
  general_question: { label: 'General Question', description: 'Products, compatibility, ordering, services, company information, or another question.', route: 'info@luxsync.net', submit: 'Send Question' },
  business_partnership: { label: 'Business / Partnership', description: 'Property management, design, construction, supplier, manufacturer, corporate, or media inquiries.', route: 'info@luxsync.net', submit: 'Send Business Inquiry' },
  other: { label: 'Other', description: 'Something else that does not fit the choices above.', route: 'info@luxsync.net', submit: 'Send Message' }
};

const branchOptions = {
  support: ['Product Setup', 'Device Compatibility', 'SmartThings Connection', 'Automation or Routine', 'Device Not Responding', 'Wi-Fi or Connectivity', 'Account or App Question', 'Order Question', 'Installation Question', 'Troubleshooting', 'Other'],
  product_information: ['LuxSync Solution Bundles', 'Smart Lighting & Ambience', 'Smart Entry & Access', 'Property Awareness & Security', 'Comfort & Climate', 'Energy Intelligence', 'Water Protection', 'Entertainment', 'SmartThings', 'Matter-Compatible Devices', 'Accessible Living', 'Short-Term Rental Solutions', 'Business / Office Solutions', 'Other'],
  consultation: ['New Smart Home Planning', 'Existing Smart Home Upgrade', 'SmartThings Setup', 'Home Automation Planning', 'Short-Term Rental Automation', 'Accessible Living Technology', 'Home Entertainment', 'Smart Lighting', 'Business / Office Automation', 'New Construction Planning', 'My LuxSync Blueprint Review', 'Other'],
  general_question: ['Products', 'Compatibility', 'SmartThings', 'Ordering', 'Shipping', 'Installation', 'Services', 'Consultations', 'Website or Account', 'Company Information', 'Other'],
  business_partnership: ['Property Management', 'Short-Term Rental Management', 'Real Estate', 'Interior Design', 'Home Builder / Construction', 'Technology Partnership', 'Device Manufacturer', 'Distributor / Supplier', 'Corporate / Office Solutions', 'Media / Press', 'Affiliate Opportunity', 'Other'],
  other: ['General Message']
};

function selectField(id, label, options, required = true) {
  return `<div class="field"><label for="${id}">${escapeHtml(label)}${required ? '<span class="required-mark" aria-hidden="true">*</span>' : ''}</label><select id="${id}" name="${id}"${required ? ' required' : ''}><option value="">Choose one</option>${options.map((option) => `<option value="${escapeHtml(option)}">${escapeHtml(option)}</option>`).join('')}</select></div>`;
}

const propertyTypeOptions = ['Private Residence', 'Short-Term Rental', 'Business / Commercial Property', 'Other'];
const squareFootageOptions = ['Under 1,000 sq. ft.', '1,000–1,999 sq. ft.', '2,000–2,999 sq. ft.', '3,000–4,999 sq. ft.', '5,000+ sq. ft.', 'Not Sure'];

function checkboxGroup(name, legend, options) {
  return `<fieldset class="field"><legend>${escapeHtml(legend)}</legend><div class="choice-grid">${options.map((option) => `<label class="check-row"><input type="checkbox" name="${name}" value="${escapeHtml(option)}"><span>${escapeHtml(option)}</span></label>`).join('')}</div></fieldset>`;
}

function propertyTypeFields(propertyType) {
  if (propertyType === 'Private Residence') {
    return `<div class="field-row">${selectField('residence_type', 'Residence type', ['Single-Family Home', 'Apartment', 'Condominium', 'Townhome', 'Vacation Home', 'New Construction', 'Other'], false)}<div class="field"><label for="residence_levels">Number of levels</label><input id="residence_levels" name="residence_levels" type="number" min="1" step="1" inputmode="numeric"></div></div>`;
  }
  if (propertyType === 'Short-Term Rental') {
    return `<div class="field-row">${selectField('str_property_type', 'Short-term rental property type', ['Single-Family Home', 'Apartment', 'Condominium', 'Townhome', 'Vacation Home', 'Multi-Unit Property', 'Other'], false)}<div class="field"><label for="rental_units">Number of rental units</label><input id="rental_units" name="rental_units" type="number" min="1" step="1" inputmode="numeric"></div></div><div class="field-row">${selectField('booking_platform', 'Booking platform', ['Airbnb', 'Vrbo', 'Both or Multiple', 'Direct Booking', 'Other', 'Not Yet Listed'], false)}${selectField('remote_management_status', 'Remote-management status', ['Managed On Site', 'Managed Remotely', 'Hybrid', 'Not Sure'], false)}</div>${checkboxGroup('desired_automation', 'Desired automation areas', ['Guest Entry', 'Smart Locks', 'Lighting', 'Climate', 'Energy', 'Noise Awareness', 'Water / Leak Awareness', 'Occupancy Awareness', 'Turnover', 'Property Monitoring', 'Guest Experience', 'Other'])}`;
  }
  if (propertyType === 'Business / Commercial Property') {
    return `<div class="field-row">${selectField('business_type', 'Business type', ['Office', 'Retail', 'Hospitality', 'Professional Services', 'Medical / Healthcare Office', 'Property Management', 'Multi-Family', 'Restaurant', 'Studio', 'Other'], false)}<div class="field"><label for="number_of_locations">Number of locations</label><input id="number_of_locations" name="number_of_locations" type="number" min="1" step="1" inputmode="numeric"></div></div>`;
  }
  if (propertyType === 'Other') {
    return `<div class="field"><label for="property_description">Describe the property</label><textarea id="property_description" name="property_description"></textarea></div>`;
  }
  return '<small>Select a property type to reveal only the relevant profile questions.</small>';
}

function propertyFields() {
  return `<section class="form-section"><h3>Property Profile</h3><div class="field-row">${selectField('property_type', 'Property type', propertyTypeOptions, false)}<div class="field"><label for="square_feet_exact">Approximate square footage</label><input id="square_feet_exact" name="square_feet_exact" type="number" min="1" step="1" inputmode="numeric"><small>An estimate is acceptable.</small></div></div><div class="field-row">${selectField('square_feet_band', 'Square-footage range', squareFootageOptions, false)}<div class="field"><label for="city">City</label><input id="city" name="city" autocomplete="address-level2"></div></div><div class="field-row"><div class="field"><label for="state">State</label><input id="state" name="state" autocomplete="address-level1"></div></div><div id="property-type-details" aria-live="polite"></div><small>A street address is not required for an initial inquiry.</small></section>`;
}

function initPropertyProfile(form) {
  if (!form) return;
  const propertyType = qs('#property_type', form);
  const details = qs('#property-type-details', form);
  if (!propertyType || !details) return;

  const update = () => {
    details.innerHTML = propertyTypeFields(propertyType.value);
  };

  propertyType.addEventListener('change', update);

  try {
    const fromBlueprint = new URLSearchParams(location.search).get('source') === 'blueprint';
    const blueprint = fromBlueprint ? JSON.parse(localStorage.getItem('luxsyncBlueprint') || 'null') : null;
    if (blueprint?.profile) {
      propertyType.value = blueprint.profile.property_type || '';
      const band = qs('#square_feet_band', form);
      if (band) band.value = blueprint.profile.square_feet_band || '';
    }
  } catch {
    // Ignore malformed or unavailable local Blueprint context.
  }

  update();
}

function branchFields(intent) {
  const topicLabels = {
    support: 'What do you need help with?',
    product_information: 'What would you like information about?',
    consultation: 'What type of consultation are you interested in?',
    general_question: 'What is your question about?',
    business_partnership: 'What are you contacting LuxSync about?',
    other: 'Message type'
  };
  const mainSelect = selectField('topic', topicLabels[intent], branchOptions[intent] || [], true);
  if (intent === 'support') {
    return `${mainSelect}<div class="field-row">${selectField('existing_customer', 'Do you already own or use a LuxSync product or solution?', ['Yes', 'No', 'Not Sure'], true)}${selectField('platform', 'Device or platform involved', ['Samsung SmartThings', 'Matter', 'Amazon Alexa', 'Google Home', 'Smart Lighting', 'Locks', 'Cameras', 'Sensors', 'Climate', 'Entertainment', 'Networking / Wi-Fi', 'Other'], false)}</div><div class="field"><label for="message">Describe the issue<span class="required-mark" aria-hidden="true">*</span></label><textarea id="message" name="message" required></textarea><small>Please include error messages, device names, and steps you have already tried. Do not include passwords or access codes.</small></div>`;
  }
  if (intent === 'business_partnership') {
    return `${mainSelect}<div class="field-row"><div class="field"><label for="company">Company name</label><input id="company" name="company" autocomplete="organization"></div><div class="field"><label for="company_website">Company website</label><input id="company_website" name="company_website" inputmode="url"></div></div><div class="field"><label for="message">Describe the opportunity<span class="required-mark" aria-hidden="true">*</span></label><textarea id="message" name="message" required></textarea></div>${propertyFields()}`;
  }
  if (intent === 'general_question' || intent === 'other') {
    return `${mainSelect}<div class="field"><label for="message">Your question or message<span class="required-mark" aria-hidden="true">*</span></label><textarea id="message" name="message" required></textarea></div>`;
  }
  return `${mainSelect}${propertyFields()}<div class="field"><label for="goals">What are you hoping to accomplish?</label><textarea id="goals" name="goals" placeholder="Comfort, lighting, climate, accessibility, guest experience, remote management, energy awareness, entertainment, or another outcome."></textarea></div><div class="field"><label for="message">Anything else we should know?</label><textarea id="message" name="message"></textarea></div>`;
}

function serializeForm(form) {
  const formData = new FormData(form);
  const data = Object.fromEntries(formData.entries());
  const desiredAutomation = formData.getAll('desired_automation');
  if (desiredAutomation.length) data.desired_automation = desiredAutomation;
  data.marketing_consent = Boolean(qs('[name="marketing_consent"]', form)?.checked);
  data.privacy_acknowledgment = Boolean(qs('[name="privacy_acknowledgment"]', form)?.checked);
  let blueprint = null;
  try { blueprint = JSON.parse(localStorage.getItem('luxsyncBlueprint') || 'null'); } catch { blueprint = null; }
  if (blueprint && new URLSearchParams(location.search).get('source') === 'blueprint') {
    data.blueprint = {
      id: blueprint.id,
      property_type: blueprint.profile?.property_type,
      square_feet_band: blueprint.profile?.square_feet_band,
      technology_profile: blueprint.profile?.technology_profile,
      recommended_experiences: blueprint.result?.recommended_experiences?.map((item) => item.name),
      flags: blueprint.result?.flags,
      implementation_path: blueprint.result?.implementation_path?.id
    };
  }
  return data;
}

function mailtoFallback(payload, email) {
  const subject = `LuxSync ${contactIntents[payload.contact_intent]?.label || 'Contact'} — ${payload.topic || 'Inquiry'}`;
  const lines = Object.entries(payload)
    .filter(([key, value]) => key !== 'blueprint' && value !== '' && value !== false)
    .map(([key, value]) => `${humanize(key)}: ${Array.isArray(value) ? value.join(', ') : value}`);
  if (payload.blueprint?.id) lines.push(`Blueprint ID: ${payload.blueprint.id}`);
  return `mailto:${email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(lines.join('\n'))}`;
}

function initContact() {
  const root = qs('#contact-app');
  if (!root) return;
  const params = new URLSearchParams(location.search);
  let selectedIntent = params.get('intent');
  if (!contactIntents[selectedIntent]) selectedIntent = '';

  function render() {
    const buttons = Object.entries(contactIntents).map(([key, item]) => `<button class="intent-button${selectedIntent === key ? ' is-selected' : ''}" type="button" data-intent="${key}">${escapeHtml(item.label)}<span>${escapeHtml(item.description)}</span></button>`).join('');
    root.innerHTML = `<div class="app-content"><p class="eyebrow">Adaptive Contact</p><h2>What can we help you with?</h2><p class="app-intro">Choose one path. We will reveal only the information that helps route your request.</p><div class="intent-grid">${buttons}</div>${selectedIntent ? `<form id="contact-form" novalidate><input type="hidden" name="contact_intent" value="${selectedIntent}"><section class="form-section"><h3>${escapeHtml(contactIntents[selectedIntent].label)}</h3>${branchFields(selectedIntent)}</section><section class="form-section"><h3>Contact Information</h3><div class="field-row"><div class="field"><label for="first_name">First name<span class="required-mark" aria-hidden="true">*</span></label><input id="first_name" name="first_name" autocomplete="given-name" required></div><div class="field"><label for="last_name">Last name<span class="required-mark" aria-hidden="true">*</span></label><input id="last_name" name="last_name" autocomplete="family-name" required></div></div><div class="field-row"><div class="field"><label for="email">Email address<span class="required-mark" aria-hidden="true">*</span></label><input id="email" name="email" type="email" autocomplete="email" required></div><div class="field"><label for="phone">Phone number</label><input id="phone" name="phone" type="tel" autocomplete="tel"></div></div>${selectField('preferred_contact_method', 'Preferred contact method', ['Email', 'Phone'], true)}</section><section class="form-section"><label class="check-row"><input type="checkbox" name="privacy_acknowledgment" required><span>I understand that LuxSync may use the information I provide to respond to this inquiry in accordance with the LuxSync Privacy Policy.</span></label><label class="check-row"><input type="checkbox" name="marketing_consent"><span>I'd like to receive occasional LuxSync product news, intelligent-living tips, and updates.</span></label></section><div id="contact-error" class="form-error" role="alert" hidden></div><div class="app-actions"><span></span><div class="button-row"><button class="button" type="submit">${escapeHtml(contactIntents[selectedIntent].submit)}</button></div></div></form>` : ''}</div>`;
    qsa('[data-intent]', root).forEach((button) => {
      button.addEventListener('click', () => {
        selectedIntent = button.dataset.intent;
        render();
        qs('#contact-form', root)?.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    });
    const form = qs('#contact-form', root);
    initPropertyProfile(form);
    form?.addEventListener('submit', async (event) => {
      event.preventDefault();
      const error = qs('#contact-error', root);
      if (!form.checkValidity()) {
        error.hidden = false;
        error.textContent = 'Please complete the required fields and confirm the privacy acknowledgment.';
        form.reportValidity();
        return;
      }
      const payload = serializeForm(form);
      const routeEmail = contactIntents[selectedIntent].route;
      const submit = qs('button[type="submit"]', form);
      submit.disabled = true;
      submit.textContent = 'Sending…';
      if (CONFIG.contactEndpoint) {
        try {
          const response = await fetch(CONFIG.contactEndpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
            body: JSON.stringify(payload)
          });
          if (!response.ok) throw new Error('Submission failed');
          root.innerHTML = `<div class="contact-confirmation"><p class="eyebrow">Thank You</p><h2>Your message has been received.</h2><p>A LuxSync team member will review your request and respond using the contact information you provided.</p><div class="button-row" style="margin-top:1.5rem"><a class="button" href="/">Return Home</a></div></div>`;
          return;
        } catch (error) {
          error.hidden = false;
          error.textContent = 'The web form could not send your message. Your email app will open as a fallback.';
        }
      }
      const fallback = mailtoFallback(payload, routeEmail);
      window.location.href = fallback;
      submit.disabled = false;
      submit.textContent = contactIntents[selectedIntent].submit;
      error.hidden = false;
      error.innerHTML = `The web form is not connected to a delivery endpoint yet. Please send the prepared email to <a href="mailto:${routeEmail}">${routeEmail}</a>.`;
    });
  }
  render();
}

function initLogin(){const f=qs("#login-form");if(!f)return;f.addEventListener("submit",e=>{e.preventDefault();const s=qs("#login-status");if(CONFIG.commerceUrl){window.location.assign(CONFIG.commerceUrl);return}s.textContent="The secure Commerce Plus account connection is not configured yet. Contact LuxSync support for access.";});}

function initCreateAccount(){
  const form=qs("#create-account-form");
  if(!form)return;
  form.addEventListener("submit",e=>{
    e.preventDefault();
    const status=qs("#create-account-status");
    const password=qs('[name="password"]',form);
    const confirmation=qs('[name="confirmPassword"]',form);
    if(password.value!==confirmation.value){
      status.textContent="Passwords do not match. Please re-enter your confirmation.";
      confirmation.focus();
      return;
    }
    if(CONFIG.commerceUrl){window.location.assign(CONFIG.commerceUrl);return;}
    status.textContent="Secure account creation will continue through Commerce Plus once the account connection is configured. No details were saved by this page.";
    form.reset();
  });
}

function initCommerceLink() {
  const link = qs('#commerce-link');
  if (!link || !CONFIG.commerceUrl) return;
  link.href = CONFIG.commerceUrl;
  link.rel = 'noopener';
}

initNavigation();
initFaqs();
initCatalog();
initConcierge();
initBlueprint();
initContact();
initCommerceLink();
initLogin();
initCreateAccount();
