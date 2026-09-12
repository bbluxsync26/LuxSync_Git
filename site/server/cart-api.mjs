import catalog from '../src/store/catalog.json' with {type:'json'};
import {applyCartAction} from './cart-model.mjs';
const skus=new Set(catalog.items.map(item=>item.sku));
const respond=(data,status=200,cookie)=>new Response(JSON.stringify(data),{status,headers:{'Content-Type':'application/json','Cache-Control':'private, no-store','X-Content-Type-Options':'nosniff',...(cookie?{'Set-Cookie':cookie}:{})}});
export async function cartApi(request,env) {
  const url=new URL(request.url);
  if(url.pathname!=='/api/cart')return null;
  if(!env.DB)return respond({error:'Your cart is temporarily unavailable. Please try again.'},503);
  if(!['GET','POST'].includes(request.method))return respond({error:'Method not allowed.'},405);
  if(request.method==='POST'&&(request.headers.get('origin')!==url.origin||request.headers.get('sec-fetch-site')==='cross-site'))return respond({error:'Open the cart from LuxSync.'},403);
  const existing=request.headers.get('cookie')?.match(/(?:^|;\s*)luxsync_cart=([a-f0-9]{64})(?:;|$)/)?.[1];
  const token=existing||Array.from(crypto.getRandomValues(new Uint8Array(32)),n=>n.toString(16).padStart(2,'0')).join('');
  const digest=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(token));
  const key=Array.from(new Uint8Array(digest),n=>n.toString(16).padStart(2,'0')).join('');
  const cookie=existing?undefined:`luxsync_cart=${token}; Path=/; HttpOnly; SameSite=Lax; Max-Age=2592000${url.protocol==='https:'?'; Secure':''}`;
  try {
    const row=await env.DB.prepare('SELECT data,version FROM shopping_carts WHERE token_hash=?').bind(key).first();
    const current=row?JSON.parse(row.data):[],version=row?.version||0;
    if(request.method==='GET')return respond({items:current,version},200,cookie);
    if(!request.headers.get('content-type')?.startsWith('application/json'))return respond({error:'Use a JSON request.'},415,cookie);
    const text=await request.text();if(text.length>40000)return respond({error:'This cart request is too large.'},413,cookie);
    let action;try{action=JSON.parse(text);}catch{return respond({error:'The cart request could not be read.'},400,cookie);}
    if(!Number.isInteger(action.version)||action.version!==version)return respond({error:'Your cart changed in another tab. Please try again.'},409,cookie);
    let items;try{items=applyCartAction(current,action,skus);}catch(error){return respond({error:error.message},400,cookie);}
    const now=new Date().toISOString();
    const result=row
      ?await env.DB.prepare('UPDATE shopping_carts SET data=?,version=version+1,updated_at=? WHERE token_hash=? AND version=?').bind(JSON.stringify(items),now,key,version).run()
      :await env.DB.prepare('INSERT OR IGNORE INTO shopping_carts (token_hash,data,version,updated_at) VALUES (?,?,1,?)').bind(key,JSON.stringify(items),now).run();
    if(!result.meta.changes)return respond({error:'Your cart changed in another tab. Please try again.'},409,cookie);
    return respond({items,version:version+1},200,cookie);
  }catch(error){console.error('Cart storage failure',error);return respond({error:'Your cart could not be saved. Please retry.'},503,cookie);}
}
