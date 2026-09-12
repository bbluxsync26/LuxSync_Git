const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
const esc=s=>String(s??'').replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;').replaceAll("'",'&#39;');
async function request(url,options={}) {
  const response=await fetch(url,{credentials:'same-origin',...options,headers:{Accept:'application/json',...(options.body?{'Content-Type':'application/json'}:{}),...options.headers}});
  const data=await response.json();
  if(!response.ok){const error=new Error(data.error||'Unable to complete this request.');error.status=response.status;throw error;}
  return data;
}
let sessionPromise;
const session=()=>sessionPromise ||= request('/api/session').catch(error=>{sessionPromise=null;throw error;});
function returnPath(value){try{const u=new URL(value,location.origin);return u.origin===location.origin&&!/^\/(signin-with-chatgpt|signout-with-chatgpt|callback)/.test(u.pathname)?u.pathname+u.search:'/account/welcome/';}catch{return '/account/welcome/';}}
function notices(s){$$('[data-account-notice]').forEach(n=>{n.textContent=s.localPreview?'Local preview: sign-in uses a test workspace, and saved records stay on this computer. Published accounts use ChatGPT sign-in.':s.user?'Signed in. Save to keep your work in your LuxSync account.':'Sign in or create an account to keep your guides and Concierge choices.';});}
function promptAccount(back){
  const d=$('#account-save-prompt');
  $('[data-prompt-signin]',d).href='/account/?return_to='+encodeURIComponent(returnPath(back));
  $('[data-prompt-create]',d).href='/account/create/?return_to='+encodeURIComponent(returnPath(back));
  d.showModal();
}
const draftPut=(key,value)=>sessionStorage.setItem(key,JSON.stringify(value));
function draftGet(key){try{return JSON.parse(sessionStorage.getItem(key)||'null');}catch{return null;}}
function installPrompt(){
  const d=$('#account-save-prompt');if(!d)return;
  let trigger;
  document.addEventListener('click',e=>{if(e.target.closest('[data-save-guide],[data-save-concierge]'))trigger=e.target.closest('button');});
  $('[data-close-save]',d).addEventListener('click',()=>d.close());
  d.addEventListener('close',()=>trigger?.focus());
}
async function initAccount(){
  try {
    const s=await session();notices(s);
    const back=returnPath(new URLSearchParams(location.search).get('return_to')||'/account/welcome/');
    const link=$('[data-account-signin]');
    if(link){link.href=s.user?back:'/signin-with-chatgpt?return_to='+encodeURIComponent(back);if(s.user)link.textContent='Continue to my saved work';else if(s.localPreview)link.textContent='Continue in local preview account';}
    const switchLink=$('[data-account-switch]');if(switchLink)switchLink.href+='?return_to='+encodeURIComponent(back);
    const root=$('#saved-work');if(!root)return;
    if(!s.user){root.innerHTML='<h2>Sign in to see your saved work.</h2><p>Your ROI worksheets and Concierge choices belong to your account.</p><a class="button" href="/account/">Sign in or create an account</a>'; $('[data-account-signout]')?.setAttribute('hidden','');return;}
    const {items}=await request('/api/items');
    root.innerHTML=['guide','concierge'].map(kind=>`<section class="saved-group"><h2>${kind==='guide'?'My ROI guides':'My Concierge choices'}</h2>${items.some(i=>i.kind===kind)?`<div class="card-grid">${items.filter(i=>i.kind===kind).map(i=>`<article class="lux-card"><p class="eyebrow">${kind==='guide'?'Online guide':'Saved journey'}</p><h3>${esc(i.title)}</h3><p>Saved ${esc(new Date(i.updated_at).toLocaleDateString())}</p><a class="text-link" href="${kind==='guide'?'/guides/'+encodeURIComponent(i.guide_id)+'/':'/find-my-luxsync-solution/'}?saved=${encodeURIComponent(i.id)}">${kind==='guide'?'Open worksheet & logs':'Resume choices'} →</a></article>`).join('')}</div>`:`<p>No saved ${kind==='guide'?'guides':'journeys'} yet.</p>`}</section>`).join('');
  }catch(e){$$('[data-account-notice]').forEach(n=>n.textContent='Account service unavailable. You can still read and download the guides.');if($('#saved-work'))$('#saved-work').textContent=e.message;}
}
export async function restoreSavedConcierge(){
  const id=new URLSearchParams(location.search).get('saved');if(!id)return;
  const {item}=await request('/api/items/'+encodeURIComponent(id));
  if(item.kind!=='concierge')throw new Error('This is not a saved Concierge journey.');
  localStorage.setItem('luxsyncProfile',JSON.stringify(item.data.profile||{}));
  sessionStorage.setItem('luxsyncStageIndex',String(item.data.stageIndex||0));
  if(item.data.blueprint)localStorage.setItem('luxsyncBlueprint',JSON.stringify(item.data.blueprint));else localStorage.removeItem('luxsyncBlueprint');
  const u=new URL(location.href);u.searchParams.delete('saved');history.replaceState(null,'',u.pathname+u.search);
}
async function initConciergeSave(){
  const button=$('[data-save-concierge]');if(!button)return;
  const status=$('[data-concierge-save-status]');
  button.addEventListener('click',async()=>{
    button.disabled=true;
    try {
      document.dispatchEvent(new Event('luxsync:collect-concierge'));
      const profile=JSON.parse(localStorage.getItem('luxsyncProfile')||'{}');
      const blueprint=JSON.parse(localStorage.getItem('luxsyncBlueprint')||'null');
      const payload={kind:'concierge',title:profile.property_type?String(profile.property_type).replaceAll('_',' ')+' - Concierge':'My Concierge choices',data:{profile,stageIndex:Number(sessionStorage.getItem('luxsyncStageIndex')||0),blueprint}};
      if(!Object.keys(profile).length&&!blueprint){status.textContent='Choose an option in the Concierge first, then save your choices.';return;}
      const s=await session();
      if(!s.user){draftPut('luxsyncConciergePending',payload);promptAccount(location.pathname+'?resumeSave=1');return;}
      const result=await request('/api/items',{method:'POST',body:JSON.stringify(payload)});status.innerHTML='Saved to your account. <a href="/account/welcome/">View my saved work →</a>';sessionStorage.removeItem('luxsyncConciergePending');
    }catch(e){status.textContent=e.message;}finally{button.disabled=false;}
  });
  if(new URLSearchParams(location.search).get('resumeSave')==='1') {
    try {
      const pending=draftGet('luxsyncConciergePending');const s=await session();
      if(pending&&s.user){await request('/api/items',{method:'POST',body:JSON.stringify(pending)});sessionStorage.removeItem('luxsyncConciergePending');status.innerHTML='Your choices are saved. <a href="/account/welcome/">View my saved work →</a>';history.replaceState(null,'',location.pathname);}
    }catch(e){status.textContent=e.message;}
  }
}
async function initGuide(){
  const root=$('[data-roi-guide]');if(!root)return;
  const status=$('[data-guide-status]',root), worksheet=$('#guide-worksheet'), logForm=$('#measurement-form');
  let guide,state={projectName:'',notes:'',worksheet:{},logs:[]},id=null,version=null,dirty=false,editingIndex=null;
  const key='luxsyncGuideDraft:'+root.dataset.roiGuide;
  const buttons=$$('[data-save-guide]');
  const message=s=>status.textContent=s;
  function collect(){const f=new FormData(worksheet);state.projectName=String(f.get('projectName')||'');state.notes=String(f.get('notes')||'');for(const field of guide.worksheet)state.worksheet[field.id]=String(f.get(field.id)||'');return {kind:'guide',guideId:guide.id,title:state.projectName||guide.title,data:state,...(id?{version}:{})};}
  function populate(){worksheet.elements.projectName.value=state.projectName||'';worksheet.elements.notes.value=state.notes||'';for(const f of guide.worksheet)worksheet.elements[f.id].value=state.worksheet?.[f.id]||'';renderLogs();}
  function renderComparison(){
    const logs=state.logs||[],a=logs[Number($('[data-compare-a]').value)],b=logs[Number($('[data-compare-b]').value)];
    $('[data-comparison]').innerHTML=logs.length<2?'<p>Add at least two periods to compare your recorded values.</p>':`<table><thead><tr><th scope="col">Measure</th><th scope="col">${esc(a.label)}<br>${esc(a.date)}</th><th scope="col">${esc(b.label)}<br>${esc(b.date)}</th></tr></thead><tbody>${guide.metrics.map(m=>`<tr><th scope="row">${esc(m.label)}</th><td>${esc(a.metrics[m.id]?.value||'Not recorded')} ${esc(a.metrics[m.id]?.unit||'')}</td><td>${esc(b.metrics[m.id]?.value||'Not recorded')} ${esc(b.metrics[m.id]?.unit||'')}</td></tr>`).join('')}<tr><th scope="row">Context</th><td>${esc(a.notes||'—')}</td><td>${esc(b.notes||'—')}</td></tr></tbody></table>`;
  }
  function renderLogs(){
    const logs=state.logs||[];
    $('[data-log-list]').innerHTML=logs.length?`<h3>${logs.length} recorded period${logs.length===1?'':'s'}</h3><ul>${logs.map((l,i)=>`<li><strong>${esc(l.label)}</strong> · ${esc(l.date)} · ${esc(l.phase)} <button class="button button-secondary" type="button" data-edit-period="${i}">Edit ${esc(l.label)}</button></li>`).join('')}</ul>`:'<p>No periods recorded yet.</p>';
    const options=logs.map((l,i)=>`<option value="${i}">${esc(l.label)} · ${esc(l.date)}</option>`).join('');
    $('[data-compare-a]').innerHTML=options;$('[data-compare-b]').innerHTML=options;
    $('[data-compare-b]').value=String(Math.max(0,logs.length-1));renderComparison();
    $$('[data-compare-a],[data-compare-b]').forEach(s=>s.disabled=logs.length<2);
    $$('[data-edit-period]').forEach(button=>button.addEventListener('click',()=>{
      editingIndex=Number(button.dataset.editPeriod);const period=logs[editingIndex];
      for(const key of ['label','date','phase','notes'])logForm.elements[key].value=period[key]||'';
      for(const m of guide.metrics){logForm.elements[m.id+'-value'].value=period.metrics[m.id]?.value||'';logForm.elements[m.id+'-unit'].value=period.metrics[m.id]?.unit||'';}
      $('button[type="submit"]',logForm).textContent='Update measurement period';
      logForm.elements.label.focus();message('Editing '+period.label+'. Update the period, then save the guide.');
    }));
  }
  async function save(){
    if(!worksheet.reportValidity())return;
    buttons.forEach(b=>b.disabled=true);
    try {
      const payload=collect();const s=await session();
      if(!s.user){draftPut(key,{payload,id,version});promptAccount(location.pathname+'?resume=1');return;}
      const result=await request(id?'/api/items/'+id:'/api/items',{method:id?'PUT':'POST',body:JSON.stringify(payload)});
      id=result.id;version=result.version;dirty=false;sessionStorage.removeItem(key);history.replaceState(null,'',location.pathname+'?saved='+id);message('Saved to your account. Your worksheet and recorded periods are ready to revisit.');
    }catch(e){message(e.message);}finally{buttons.forEach(b=>b.disabled=false);}
  }
  try {
    const catalog=await request('/data/roi-guides.json');guide=catalog.find(g=>g.id===root.dataset.roiGuide);if(!guide)throw new Error('Guide not found.');
    const params=new URLSearchParams(location.search);id=params.get('saved');
    if(id){const {item}=await request('/api/items/'+encodeURIComponent(id));if(item.kind!=='guide'||item.guide_id!==guide.id)throw new Error('This saved worksheet belongs to a different guide.');state=item.data;version=item.version;message('Loaded your saved guide.');}
    else if(params.has('resume')){const draft=draftGet(key);if(draft){state=draft.payload.data;id=draft.id;version=draft.version;dirty=true;message('Your draft is restored. Select Save guide to keep it in your account.');}}
    if(!state.worksheet)state.worksheet={};if(!state.logs)state.logs=[];populate();
    logForm.elements.date.value=new Date().toISOString().slice(0,10);
    worksheet.addEventListener('submit',e=>e.preventDefault());
    worksheet.addEventListener('input',()=>{dirty=true;message('Unsaved changes. Save the guide to keep them in your account.');});
    buttons.forEach(b=>b.addEventListener('click',save));
    $$('[data-compare-a],[data-compare-b]').forEach(select=>select.addEventListener('change',renderComparison));
    logForm.addEventListener('submit',e=>{e.preventDefault();if(!logForm.reportValidity())return;if(editingIndex===null&&state.logs.length>=100){message('This worksheet supports up to 100 measurement periods.');return;}const f=new FormData(logForm),metrics={};for(const m of guide.metrics)metrics[m.id]={value:String(f.get(m.id+'-value')||''),unit:String(f.get(m.id+'-unit')||'')};const period={id:editingIndex===null?crypto.randomUUID():state.logs[editingIndex].id,label:String(f.get('label')),date:String(f.get('date')),phase:String(f.get('phase')),notes:String(f.get('notes')||''),metrics};if(editingIndex===null)state.logs.push(period);else state.logs[editingIndex]=period;editingIndex=null;dirty=true;renderLogs();logForm.reset();$('button[type="submit"]',logForm).textContent='Add measurement period';logForm.elements.date.value=new Date().toISOString().slice(0,10);message('Period recorded in this worksheet. Save the guide to keep it in your account.');});
    window.addEventListener('beforeunload',e=>{if(dirty){e.preventDefault();e.returnValue='';}});
    // A sign-in navigation explicitly preserves the current temporary draft.
    $$('[data-prompt-signin],[data-prompt-create]').forEach(a=>a.addEventListener('click',()=>dirty=false));
  }catch(e){message(e.message);buttons.forEach(b=>b.disabled=true);}
}
installPrompt();initAccount();initGuide();initConciergeSave();
