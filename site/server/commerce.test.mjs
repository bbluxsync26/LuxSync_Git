import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {api} from './api.mjs';
import {openDatabase} from './local-db.mjs';
import catalog from '../src/store/catalog.json' with {type:'json'};
test('catalog routes, bundle quantities, assets and price placeholders',()=>{
  assert.equal(catalog.items.filter(i=>i.kind==='product').length,38);assert.equal(catalog.items.filter(i=>i.kind==='bundle').length,32);
  for(const item of catalog.items){assert.equal(item.price,null);assert.ok(catalog.categories.some(c=>c.id===item.categoryId));for(const c of item.components)assert.ok(c.quantity>0&&catalog.items.some(p=>p.sku===c.sku&&p.kind==='product'));const html=fs.readFileSync(new URL('../dist/client/shop/items/'+item.sku+'/index.html',import.meta.url),'utf8');assert.ok(html.includes('Pricing coming soon'));const main=html.match(/<main[^>]*>([\s\S]*?)<\/main>/)[1];assert.ok(!main.includes('<img'));}
  for(const c of catalog.categories)assert.ok(fs.existsSync(new URL('../src/heroes/'+c.image+'-720.webp',import.meta.url)));
});
test('durable guest carts and account-only wishlists preserve ownership and versions',async()=>{
  const folder=fs.mkdtempSync(path.join(os.tmpdir(),'luxsync-commerce-'));
  const filename=path.join(folder,'test.sqlite'),migrations=fileURLToPath(new URL('../drizzle/',import.meta.url));
  let DB=openDatabase(filename,migrations),cookie='';
  const call=(route,method='GET',body,who='',cartCookie=cookie,origin='https://luxsync.test')=>api(new Request('https://luxsync.test'+route,{method,headers:{'Content-Type':'application/json',Origin:origin,Cookie:cartCookie,...(who?{'oai-authenticated-user-id':who,'oai-authenticated-user-email':who+'@example.test'}:{})},...(body?{body:JSON.stringify(body)}:{})}),{DB});
  try{
    const first=await call('/api/cart');cookie=first.headers.get('set-cookie').split(';')[0];assert.match(cookie,/luxsync_cart=[a-f0-9]{64}/);assert.match(first.headers.get('set-cookie'),/HttpOnly/);
    const sku=catalog.items[0].sku,bundle=catalog.items.find(i=>i.kind==='bundle').sku;
    let r=await call('/api/cart','POST',{action:'add',sku,quantity:2,version:0});assert.equal(r.status,200);
    assert.equal((await call('/api/cart','POST',{action:'add',sku,quantity:1,version:0})).status,409);
    assert.equal((await call('/api/cart','POST',{action:'add',sku:'unknown',quantity:1,version:1})).status,400);
    assert.equal((await call('/api/cart','POST',{action:'add',sku,quantity:1,version:1},'',cookie,'https://evil.test')).status,403);
    r=await call('/api/cart','POST',{action:'add',sku:bundle,quantity:1,version:1});assert.equal(r.status,200);
    assert.deepEqual((await(await call('/api/cart','GET',null,'','')).json()).items,[]);
    r=await call('/api/cart','POST',{action:'quantity',id:sku,quantity:3,version:2});assert.equal(r.status,200);
    const payload={kind:'wishlist',title:'Our future home',data:{items:[{sku,quantity:2},{sku:bundle,quantity:1}]}};
    assert.equal((await call('/api/items','POST',payload)).status,401);
    r=await call('/api/items','POST',payload,'alice');assert.equal(r.status,201);const {id}=await r.json();
    assert.equal((await call('/api/items/'+id,'GET',null,'bob')).status,404);
    assert.equal((await call('/api/items/'+id,'PUT',{...payload,version:1},'bob')).status,404);
    assert.equal((await call('/api/items/'+id,'PUT',{...payload,title:'Lake house',version:1},'alice')).status,200);
    assert.equal((await call('/api/items/'+id,'PUT',{...payload,version:1},'alice')).status,409);
    assert.equal((await call('/api/items','POST',{...payload,data:{items:[{sku:'bad',quantity:1}]}},'alice')).status,400);
    DB.sqlite.close();DB=openDatabase(filename,migrations);
    assert.equal((await(await call('/api/cart')).json()).items[0].quantity,3);
    const saved=(await(await call('/api/items/'+id,'GET',null,'alice')).json()).item;assert.equal(saved.title,'Lake house');assert.deepEqual(saved.data,payload.data);
    assert.equal((await call('/api/cart','POST',{action:'remove',id:sku,version:3})).status,200);
  }finally{DB.sqlite.close();fs.rmSync(folder,{recursive:true,force:true});}
});
