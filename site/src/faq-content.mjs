const escapeHtml = (value = '') => String(value)
  .replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
  .replaceAll('"', '&quot;').replaceAll("'", '&#39;');

export const faqSlug = value => value.toLowerCase().normalize('NFKD')
  .replace(/[\u0300-\u036f]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');

export function parseFaqs(markdown) {
  const items = [];
  let category = 'General', question = '', lines = [];
  const flush = () => {
    const answer = lines.join('\n').trim();
    if (question && answer) items.push({
      category, categoryId: faqSlug(category), id: faqSlug(question), question, answer
    });
    question = ''; lines = [];
  };
  for (const line of markdown.replace(/\r\n?/g, '\n').split('\n')) {
    if (line.startsWith('## ')) { flush(); category = line.slice(3).trim(); }
    else if (line.startsWith('### ')) { flush(); question = line.slice(4).trim(); }
    else if (question) lines.push(line);
  }
  flush();
  return items;
}

function safeHref(href) {
  if (/\s|[<>"'\\]/.test(href)) return false;
  return /^\/(?!\/)/.test(href) || /^#[a-z0-9-]+$/i.test(href)
    || /^https:\/\/[a-z0-9.-]+(?:[/?#]|$)/i.test(href)
    || /^mailto:[a-z0-9_.+%-]+@[a-z0-9.-]+$/i.test(href);
}

export function faqInline(text) {
  const pattern = /\[([^\]]+)\]\(([^)]+)\)|\*\*([^*]+)\*\*/g;
  let result = '', start = 0;
  for (const match of text.matchAll(pattern)) {
    result += escapeHtml(text.slice(start, match.index));
    if (match[3]) result += `<strong>${escapeHtml(match[3])}</strong>`;
    else if (safeHref(match[2])) result += `<a href="${escapeHtml(match[2])}">${escapeHtml(match[1])}</a>`;
    else result += escapeHtml(match[1]);
    start = match.index + match[0].length;
  }
  return result + escapeHtml(text.slice(start));
}

export function faqItem(item) {
  return `<details class="faq-item" id="${escapeHtml(item.id)}"><summary>${escapeHtml(item.question)}<span class="faq-toggle" aria-hidden="true"></span></summary><div class="faq-answer">${item.answer.split(/\n\s*\n/).map(p => `<p>${faqInline(p.replace(/\n/g, ' '))}</p>`).join('')}</div></details>`;
}

export function faqLibrary(items) {
  const categories = [...new Map(items.map(item => [item.categoryId, item.category])).entries()];
  return `<div class="faq-layout"><aside class="faq-topics"><p class="eyebrow">Find your answer</p><h2>Browse by topic</h2><nav aria-label="FAQ topics">${categories.map(([id, title]) => `<a href="#${id}">${escapeHtml(title)}</a>`).join('')}</nav></aside><div class="faq-content"><p class="faq-library-intro">${items.length} answers across ${categories.length} topics. Browse below, or use the search icon in the header.</p><div id="faq-full">${categories.map(([id, title]) => `<section class="faq-group" id="${id}" aria-labelledby="${id}-title"><h2 id="${id}-title">${escapeHtml(title)}</h2><div class="faq-list">${items.filter(item => item.categoryId === id).map(faqItem).join('')}</div></section>`).join('')}</div></div></div>`;
}
