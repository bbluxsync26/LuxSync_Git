import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {api,safeReturn} from './api.mjs';
import {openDatabase} from './local-db.mjs';

test('account ownership, persistence, validation and version conflicts',async()=>{
  const folder=fs.mkdtempSync(path.join(os.tmpdir(),'luxsync-account-test-'));
  const filename=path.join(folder,'accounts.sqlite');
  const migrations=new URL('../drizzle/',import.meta.url).pathname.replace(/^\/(\w:)/,'$1');
  let DB=openDatabase(filename,decodeURIComponent(migrations));
  const call=(route,method='GET',body,who='alice',origin='https://luxsync.test')=>api(new Request('https://luxsync.test'+route,{method,headers:{...(who?{'oai-authenticated-user-id':who,'oai-authenticated-user-email':who+'@example.test'}:{}),'Content-Type':'application/json',Origin:origin},...(body?{body:JSON.stringify(body)}:{})}),{DB});
  const payload={kind:'guide',guideId:'commercial-offices',title:'QA worksheet',data:{worksheet:{'input-1':'1500'},logs:[{label:'January',date:'2026-01-31',metrics:{'metric-1':{value:'1500',unit:'kWh'}}}]}};
  try {
    assert.equal((await call('/api/items','GET',null,null)).status,401);
    assert.equal((await call('/api/items','POST',payload,'alice','https://elsewhere.test')).status,403);
    assert.equal((await call('/api/items','POST',{...payload,guideId:'missing'})).status,400);
    const created=await call('/api/items','POST',payload);assert.equal(created.status,201);
    const {id}=await created.json();
    assert.equal((await call('/api/items/'+id,'GET',null,'bob')).status,404);
    assert.deepEqual((await (await call('/api/items','GET',null,'bob')).json()).items,[]);
    assert.equal((await call('/api/items/'+id,'PUT',{...payload,version:1},'bob')).status,404);
    assert.equal((await call('/api/items/'+id,'PUT',{...payload,title:'Updated QA worksheet',version:1})).status,200);
    assert.equal((await call('/api/items/'+id,'PUT',{...payload,version:1})).status,409);
    DB.sqlite.close();DB=openDatabase(filename,decodeURIComponent(migrations));
    const item=(await (await call('/api/items/'+id)).json()).item;
    assert.equal(item.version,2);assert.equal(item.title,'Updated QA worksheet');assert.deepEqual(item.data,payload.data);
    const concierge=await call('/api/items','POST',{kind:'concierge',title:'QA journey',data:{profile:{property_type:'residential'},stageIndex:2}});
    assert.equal(concierge.status,201);
    assert.equal((await (await call('/api/items')).json()).items.length,2);
  }finally{DB.sqlite.close();fs.rmSync(folder,{recursive:true,force:true});}
});
test('sign-in returns stay on the site',()=>{
  for(const url of ['https://example.com','//example.com','/\\example.com','/signin-with-chatgpt'])assert.equal(safeReturn(url),'/account/welcome/');
  assert.equal(safeReturn('/guides/commercial-offices/?resume=1'),'/guides/commercial-offices/?resume=1');
});
