const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path'); const { execFileSync } = require('child_process');
// column widths (percent) for the widest tables, keyed by the start of their header row
const WIDTHS = [
  { sig: ['Wk', 'Dates', 'Incline walk', 'Flat walk', 'Lifting focus'], w: [5, 10, 19, 15, 51], cls: 'dense' },
  { sig: ['Wk', 'Dates (Mon–Sun)', 'Mode', 'Target 7-day avg'], w: [5, 16, 24, 15, 16, 10, 14] },
  { sig: ['Wk', 'Dates (Mon–Sun, 2027)', 'Mode', 'kcal'], w: [5, 17, 25, 7, 15, 18, 13] },
  { sig: ['Flag', 'Trips when', 'Tripped?'], w: [15, 69, 16] },
  { sig: ['Date', 'Week', 'What happens'], w: [16, 7, 77] },
  { sig: ['Day', 'Weight (lb)', 'kcal', 'Protein (g)', 'Steps'], w: [9, 10, 10, 10, 10, 8, 9, 9, 10, 15], cls: 'form' },
  { sig: ['#', 'Exercise', 'Sets × Reps', 'RIR', 'Rest', 'Key cue', 'PF substitute'], w: [3, 29, 11, 6, 9, 22, 20] },
];
const strip = s => s.replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim();
(async () => {
  const [md, pdf] = process.argv.slice(2);
  const dir = __dirname;
  let body = execFileSync('pandoc', ['-f', 'gfm', '-t', 'html5', '--wrap=none', md], { encoding: 'utf8', maxBuffer: 64e6 });
  body = body.replace(/<div style="page-break-after: always;"><\/div>/g, '<div class="pb"></div>');
  body = body.replace(/<table>([\s\S]*?)<\/table>/g, (m, inner) => {
    const ths = (inner.match(/<th[^>]*>[\s\S]*?<\/th>/g) || []).map(strip);
    const hit = WIDTHS.find(x => x.sig.every((s, i) => (ths[i] || '').startsWith(s)) && x.w.length === ths.length);
    if (hit) {
      const cg = '<colgroup>' + hit.w.map(p => `<col style="width:${p}%">`).join('') + '</colgroup>';
      return `<table class="fixed ${hit.cls || ''}">${cg}${inner.replace(/<colgroup>[\s\S]*?<\/colgroup>/, '')}</table>`;
    }
    // blank-cell tables are fill-in forms: give their rows writing height
    const cells = (inner.match(/<td[^>]*>/g) || []).length; const empty = (inner.match(/<td[^>]*>\s*<\/td>/g) || []).length;
    return cells && empty / cells > 0.4 ? `<table class="form">${inner}</table>` : m;
  });
  // the appendix is a one-page card: set it tighter
  body = body.replace(/(<h2[^>]*>Appendix: Quick Reference Card<\/h2>)([\s\S]*)$/, '<div class="qr">$1$2</div>');
  const css = fs.readFileSync(path.join(dir, 'style.css'), 'utf8');
  const html = `<!doctype html><html lang="en"><head><meta charset="utf-8"><title>The 25-Week Recomposition Blueprint</title><style>${css}</style></head><body>${body}</body></html>`;
  const htmlPath = path.join(require('os').tmpdir(), 'blueprint-build.html'); fs.writeFileSync(htmlPath, html);
  const browser = await chromium.launch(); const page = await browser.newPage();
  await page.goto('file://' + htmlPath); await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: pdf, format: 'Letter', printBackground: true, displayHeaderFooter: true, preferCSSPageSize: true,
    headerTemplate: '<span></span>',
    footerTemplate: `<div style="font-family:Inter,sans-serif;font-size:7pt;color:#6b7480;width:100%;padding:0 0.6in;display:flex;justify-content:space-between;"><span>The 25-Week Recomposition Blueprint · Phase 1: Nov 16, 2026 – May 9, 2027 · Phase 2: on to 200 lb</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>`,
    margin: { top: '0.62in', bottom: '0.72in', left: '0.6in', right: '0.6in' } });
  await browser.close(); console.log('pdf written', pdf, fs.statSync(pdf).size);
})();
