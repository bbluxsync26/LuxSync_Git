const url=new URL(location.href);
let type=url.searchParams.get('solution');
if(location.pathname.startsWith('/solutions/commercial')||/\/solutions\/(short-term-rentals|senior-living)/.test(location.pathname))type='commercial';
if(location.pathname.startsWith('/solutions/residential')||location.pathname.startsWith('/solutions/aging-in-place'))type='residential';
if(!['commercial','residential'].includes(type))type=null;
const main=document.querySelector('main');
const relevant=/^\/(shop|guides|find-my-luxsync-solution)(\/|$)/.test(location.pathname);
if(type){
 const label=type==='commercial'?'Commercial':'Residential';
 const nav=document.createElement('nav');nav.className='property-context';nav.setAttribute('aria-label',label+' solution navigation');
 nav.innerHTML=`<strong>${label}</strong><a href="/solutions/${type}/">Solutions</a><a href="/shop/?solution=${type}">Products & bundles</a><a href="/guides/?solution=${type}">ROI guides</a><a href="/find-my-luxsync-solution/?solution=${type}">Concierge</a><a href="/solutions/">Change property type</a>`;
 main?.prepend(nav);
 document.querySelectorAll('.property-nav a').forEach(a=>{if(a.pathname===`/solutions/${type}/`)a.setAttribute('aria-current','page');});
 for(const a of document.querySelectorAll('a[href]')){const next=new URL(a.href,location.origin);if(next.origin===location.origin&&/^\/(shop|guides|find-my-luxsync-solution)(\/|$)/.test(next.pathname)&&!next.searchParams.has('solution')){next.searchParams.set('solution',type);a.href=next.pathname+next.search+next.hash;}}
 if(location.pathname==='/shop/'||location.pathname==='/shop'){
  const all=document.createElement('a');all.className='button button-secondary';all.href='/shop/?solution=all';all.textContent='View all products and bundles';main.querySelector('.store-hero .button-row')?.append(all);
  document.querySelectorAll('.store-category').forEach(a=>{if(!a.pathname.includes('-bundles'))return;const commercial=/commercial-bundles|rental-bundles|senior-bundles/.test(a.pathname);const residential=/residential-bundles|senior-bundles/.test(a.pathname);a.hidden=type==='commercial'?!commercial:!residential;});
 }
 if(location.pathname==='/guides/'||location.pathname==='/guides'){
  document.querySelectorAll('.roi-library-card').forEach(card=>{const path=card.querySelector('a[href^="/guides/"]')?.pathname||'';const commercial=/commercial|nursing-homes|str-|senior-living/.test(path);card.hidden=type==='commercial'?!commercial:commercial;});
  document.querySelectorAll('.guide-group').forEach(group=>{group.hidden=![...group.querySelectorAll('.roi-library-card')].some(c=>!c.hidden);});
 }
}else if(relevant){
 const prompt=document.createElement('section');prompt.className='property-prompt';prompt.innerHTML='<h2>Which property are you planning for?</h2><p>Choose a path for relevant solutions and guides. You can add products from either path to your cart.</p><div class="button-row"></div>';
 for(const value of ['commercial','residential']){const link=document.createElement('a');link.className='button';const next=new URL(url);next.searchParams.set('solution',value);link.href=next.pathname+next.search+next.hash;link.textContent=value==='commercial'?'Commercial':'Residential';prompt.querySelector('.button-row').append(link);}
 main?.prepend(prompt);
}
