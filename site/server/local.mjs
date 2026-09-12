import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {api,safeReturn} from './api.mjs';
import {openDatabase} from './local-db.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const port=Number(process.env.PORT||4177);
const publicRoot=path.join(root,'dist','client');
const DB=openDatabase(process.env.LUXSYNC_LOCAL_DB||path.join(root,'.local-data','accounts.sqlite'),path.join(root,'drizzle'));
const mime={'.html':'text/html; charset=utf-8','.js':'text/javascript; charset=utf-8','.css':'text/css; charset=utf-8','.json':'application/json','.png':'image/png','.webp':'image/webp','.jpg':'image/jpeg','.pdf':'application/pdf'};
const server=http.createServer(async(req,res)=>{
  try {
    const url=new URL(req.url,`http://${req.headers.host}`);
    if(!['localhost','127.0.0.1'].includes(url.hostname)){res.writeHead(403);res.end();return;}
    const signIn=url.pathname==='/signin-with-chatgpt',signOut=url.pathname==='/signout-with-chatgpt';
    if(signIn||signOut){
      if(req.method!=='GET'||req.headers['sec-fetch-site']==='cross-site'||(req.headers.origin&&req.headers.origin!==url.origin)){res.writeHead(403);res.end();return;}
      res.writeHead(302,{'Location':safeReturn(url.searchParams.get('return_to')),'Set-Cookie':`luxsync_local_preview=${signIn?'1':''}; Path=/; HttpOnly; SameSite=Lax${signOut?'; Max-Age=0':''}`,'Cache-Control':'no-store'});res.end();return;
    }
    const headers=new Headers();
    for(const [key,value] of Object.entries(req.headers)) if(!key.startsWith('oai-authenticated-user-')&&value)headers.set(key,Array.isArray(value)?value.join(','):value);
    const cookies=(req.headers.cookie||'').split(';').map(x=>x.trim());
    if(cookies.filter(x=>x==='luxsync_local_preview=1').length===1){headers.set('oai-authenticated-user-id','luxsync-local-preview');headers.set('oai-authenticated-user-email','local-preview@luxsync.invalid');}
    const chunks=[];let bytes=0;
    for await(const chunk of req){bytes+=chunk.length;if(bytes>200000){res.writeHead(413);res.end();return;}chunks.push(chunk);}
    const request=new Request(url,{method:req.method,headers,...(!['GET','HEAD'].includes(req.method)?{body:Buffer.concat(chunks)}:{})});
    const answer=await api(request,{DB,LOCAL_PREVIEW:true});
    if(answer){res.writeHead(answer.status,Object.fromEntries(answer.headers));res.end(Buffer.from(await answer.arrayBuffer()));return;}
    if(!['GET','HEAD'].includes(req.method)){res.writeHead(405);res.end();return;}
    const pathname=decodeURIComponent(url.pathname);
    if(pathname.split('/').some(part=>part.startsWith('.'))){res.writeHead(404);res.end();return;}
    let file=path.resolve(publicRoot,'.'+pathname);
    if(!file.startsWith(publicRoot+path.sep)&&file!==publicRoot){res.writeHead(403);res.end();return;}
    if(fs.existsSync(file)&&fs.statSync(file).isDirectory())file=path.join(file,'index.html');
    let status=200;if(!fs.existsSync(file)){file=path.join(publicRoot,'404.html');status=404;}
    res.writeHead(status,{'Content-Type':mime[path.extname(file)]||'application/octet-stream','Cache-Control':'no-cache','X-Content-Type-Options':'nosniff'});
    if(req.method==='HEAD')res.end();else fs.createReadStream(file).pipe(res);
  }catch(e){console.error(e);if(!res.headersSent)res.writeHead(500);res.end('Unable to load this page.');}
});
server.listen(port,'127.0.0.1',()=>console.log(`LuxSync local account preview\nhttp://localhost:${port}\nSaves persist in ${process.env.LUXSYNC_LOCAL_DB||path.join(root,'.local-data','accounts.sqlite')}\nLocal sign-in is a clearly labeled preview identity. Hosted sign-in is owned by Sites.`));
