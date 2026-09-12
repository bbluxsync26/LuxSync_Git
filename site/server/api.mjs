import guides from '../src/roi/catalog.json' with {type:'json'};
const guideIds=new Set(guides.map(g=>g.id));
export function safeReturn(value) {
  if(typeof value!=='string'||!value.startsWith('/')||value.startsWith('//'))return '/account/welcome/';
  const u=new URL(value,'https://local.invalid');
  return u.origin==='https://local.invalid'&&!/^\/(signin-with-chatgpt|signout-with-chatgpt|callback)/.test(u.pathname)?u.pathname+u.search+u.hash:'/account/welcome/';
}
const json=(data,status=200)=>new Response(JSON.stringify(data),{status,headers:{'Content-Type':'application/json','Cache-Control':'private, no-store','X-Content-Type-Options':'nosniff'}});
function user(request) {
  const id=request.headers.get('oai-authenticated-user-id'), email=request.headers.get('oai-authenticated-user-email');
  return id&&email?{id,email}:null;
}
function validPayload(body) {
  if(!body||!['guide','concierge'].includes(body.kind)||typeof body.title!=='string'||body.title.length>160||!body.title.trim()||!body.data||typeof body.data!=='object'||Array.isArray(body.data))return false;
  if(body.kind==='guide'&&!guideIds.has(body.guideId))return false;
  if(JSON.stringify(body.data).length>180000)return false;
  if(body.kind==='guide') {
    if(body.data.logs!==undefined&&(!Array.isArray(body.data.logs)||body.data.logs.length>100))return false;
    if(body.data.logs?.some(l=>!l||typeof l!=='object'||typeof l.label!=='string'||l.label.length>160||typeof l.date!=='string'||!/^\d{4}-\d{2}-\d{2}$/.test(l.date)||!l.metrics||typeof l.metrics!=='object'))return false;
  }
  return true;
}
const unpack=row=>row?{...row,data:JSON.parse(row.data)}:null;
export async function api(request,env) {
  const url=new URL(request.url);
  if(!url.pathname.startsWith('/api/'))return null;
  const me=user(request);
  if(url.pathname==='/api/session'&&request.method==='GET')return json({user:me,localPreview:!!env.LOCAL_PREVIEW});
  if(!me)return json({error:'Sign in to save or open your account records.'},401);
  if(!env.DB)return json({error:'Account storage is unavailable. Your open worksheet has not been discarded.'},503);
  if(!['GET','HEAD'].includes(request.method)) {
    if(request.headers.get('origin')!==url.origin||request.headers.get('sec-fetch-site')==='cross-site')return json({error:'This request must come from LuxSync.'},403);
    if(!request.headers.get('content-type')?.startsWith('application/json'))return json({error:'Use a JSON request.'},415);
  }
  try {
    if(url.pathname==='/api/items'&&request.method==='GET') {
      const rows=await env.DB.prepare('SELECT id,kind,guide_id,title,version,created_at,updated_at FROM saved_items WHERE owner_id=? ORDER BY updated_at DESC LIMIT 200').bind(me.id).all();
      return json({items:rows.results});
    }
    const match=url.pathname.match(/^\/api\/items\/([a-f0-9-]{36})$/);
    if(match&&request.method==='GET') {
      const row=await env.DB.prepare('SELECT * FROM saved_items WHERE id=? AND owner_id=?').bind(match[1],me.id).first();
      return row?json({item:unpack(row)}):json({error:'This saved item was not found in your account.'},404);
    }
    if((url.pathname==='/api/items'&&request.method==='POST')||(match&&request.method==='PUT')) {
      const text=await request.text();
      if(text.length>190000)return json({error:'This worksheet is too large to save. Keep up to 100 measurement periods.'},413);
      let body;try{body=JSON.parse(text);}catch{return json({error:'The saved data could not be read.'},400);}
      if(!validPayload(body))return json({error:'Check the worksheet title, measurement dates, and entries before saving.'},400);
      const now=new Date().toISOString();
      if(request.method==='POST') {
        const count=await env.DB.prepare('SELECT COUNT(*) AS total FROM saved_items WHERE owner_id=?').bind(me.id).first();
        if(count.total>=200)return json({error:'Your account has reached its saved-item limit.'},409);
        const id=crypto.randomUUID();
        await env.DB.prepare('INSERT INTO saved_items (id,owner_id,kind,guide_id,title,data,version,created_at,updated_at) VALUES (?,?,?,?,?,?,1,?,?)').bind(id,me.id,body.kind,body.kind==='guide'?body.guideId:null,body.title.trim(),JSON.stringify(body.data),now,now).run();
        return json({id,version:1,updatedAt:now},201);
      }
      if(!Number.isInteger(body.version)||body.version<1)return json({error:'Reload the saved item before updating it.'},409);
      const existing=await env.DB.prepare('SELECT kind,guide_id FROM saved_items WHERE id=? AND owner_id=?').bind(match[1],me.id).first();
      if(!existing)return json({error:'This saved item was not found in your account.'},404);
      if(body.kind!==existing.kind||(body.guideId||null)!==existing.guide_id)return json({error:'The item type cannot be changed.'},400);
      const result=await env.DB.prepare('UPDATE saved_items SET title=?,data=?,version=version+1,updated_at=? WHERE id=? AND owner_id=? AND version=?').bind(body.title.trim(),JSON.stringify(body.data),now,match[1],me.id,body.version).run();
      if(!result.meta.changes)return json({error:'A newer version was saved in another tab. Your current entries are still here; reload the saved version before replacing it.'},409);
      return json({id:match[1],version:body.version+1,updatedAt:now});
    }
    return json({error:'Endpoint not found.'},404);
  }catch(error){console.error('Account storage failure',error);return json({error:'Account storage is temporarily unavailable. Your open entries are still here; please retry.'},503);}
}
