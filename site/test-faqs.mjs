import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {parseFaqs, faqInline} from './src/faq-content.mjs';
const root = path.dirname(new URL(import.meta.url).pathname.replace(/^\/(?=[A-Za-z]:)/, ''));
const read = file => fs.readFileSync(path.join(root, file), 'utf8');

test('FAQ parsing preserves the final answer, paragraphs, categories and safe links', () => {
  const items = parseFaqs('## Accounts\r\n\r\n### How can I save?\r\n\r\nFirst paragraph.\r\n\r\n[Open account](/account/)\r\n\r\n## Videos\r\n### Where can I learn?\r\n\r\nLast answer.');
  assert.equal(items.length, 2);
  assert.equal(items[1].answer, 'Last answer.');
  assert.equal(items[0].categoryId, 'accounts');
  assert.match(items[0].answer, /\n\n/);
  assert.match(faqInline(items[0].answer), /href="\/account\/"/);
  for (const unsafe of ['javascript:alert', 'data:text/html,bad', '//evil.example', '/\\evil.example']) {
    assert.doesNotMatch(faqInline(`[unsafe](${unsafe})`), /href=/);
  }
  assert.equal(faqInline('<img src=x onerror=alert(1)>'), '&lt;img src=x onerror=alert(1)&gt;');
});

test('built FAQs contain every question and resolve internal links and search destinations', () => {
  const source = read('source-data/content/faqs.md');
  const faqs = JSON.parse(read('dist/client/data/faqs.json'));
  const html = read('dist/client/faqs/index.html');
  assert.equal(faqs.length, [...source.matchAll(/^### /gm)].length);
  assert.ok(faqs.length >= 50);
  assert.equal(new Set(faqs.map(faq => faq.id)).size, faqs.length);
  assert.equal([...html.matchAll(/<details class="faq-item"/g)].length, faqs.length);
  assert.equal(new Set(faqs.map(faq => faq.category)).size, 9);
  assert.match(html, /https:\/\/www.youtube.com\/watch\?v=UPj32rMGmS4/);
  assert.match(html, /https:\/\/www.youtube.com\/watch\?v=5WDCht0aGVs/);
  for (const faq of faqs) {
    assert.ok(html.includes(`id="${faq.id}"`));
    for (const match of faq.answer.matchAll(/\[[^\]]+\]\(([^)]+)\)/g)) {
      const href = match[1];
      if (!href.startsWith('/') && !href.startsWith('#')) continue;
      const url = new URL(href, 'https://local.test/faqs/');
      const relative = url.pathname.slice(1);
      const file = path.join(root, 'dist/client', relative, url.pathname.endsWith('/') ? 'index.html' : '');
      assert.ok(fs.existsSync(file), 'Missing FAQ destination: ' + href);
      if (url.hash) assert.ok(fs.readFileSync(file, 'utf8').includes(`id="${url.hash.slice(1)}"`), 'Missing FAQ anchor: ' + href);
    }
  }
  const index = JSON.parse(read('dist/client/data/search.json'));
  for (const faq of faqs) assert.ok(index.some(item => item.url === '/faqs/#' + faq.id && item.title === faq.question));
});
