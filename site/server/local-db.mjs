import {DatabaseSync} from 'node:sqlite';
import fs from 'node:fs';
import path from 'node:path';
export function openDatabase(filename,migrations) {
  fs.mkdirSync(path.dirname(filename),{recursive:true});
  const sqlite=new DatabaseSync(filename);
  sqlite.exec('PRAGMA journal_mode=WAL; CREATE TABLE IF NOT EXISTS local_migrations (name TEXT PRIMARY KEY)');
  for(const file of fs.readdirSync(migrations).filter(n=>n.endsWith('.sql')).sort()) {
    if(!sqlite.prepare('SELECT name FROM local_migrations WHERE name=?').get(file)) {
      sqlite.exec('BEGIN');
      try {sqlite.exec(fs.readFileSync(path.join(migrations,file),'utf8'));sqlite.prepare('INSERT INTO local_migrations(name) VALUES (?)').run(file);sqlite.exec('COMMIT');}catch(e){sqlite.exec('ROLLBACK');throw e;}
    }
  }
  return {sqlite,prepare(sql){return {bind(...args){const query=sqlite.prepare(sql);return {async first(){return query.get(...args)||null;},async all(){return {results:query.all(...args)};},async run(){const r=query.run(...args);return {meta:{changes:r.changes}};}};}};}};
}
