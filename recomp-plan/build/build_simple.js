const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path'); const os = require('os'); const { execFileSync } = require('child_process');
// Builds the simple plan: node build_simple.js <markdown> <pdf>
(async () => {
  const [md, pdf] = process.argv.slice(2);
  let body = execFileSync('pandoc', ['-f', 'gfm', '-t', 'html5', '--wrap=none', md], { encoding: 'utf8', maxBuffer: 64e6 });
  body = body.replace(/<div style="page-break-after: always;"><\/div>/g, '<div class="pb"></div>');
  body = body.replace(/<table>([\s\S]*?)<\/table>/g, (m, inner) => {
    if (!/<th[^>]*>Week<\/th>\s*<th[^>]*>Dates<\/th>/.test(inner)) return m;
    const w = inner.includes('Incline block') ? [9, 29, 16, 14, 12, 20] : [6, 18, 10, 9, 21, 21, 15];
    const cg = '<colgroup>' + w.map(p => `<col style="width:${p}%">`).join('') + '</colgroup>';
    inner = inner.replace(/<colgroup>[\s\S]*?<\/colgroup>/, '').replace(/<tr([^>]*)>(\s*<td[^>]*><strong>)/g, '<tr class="brk"$1>$2');
    return `<table class="weeks">${cg}${inner}</table>`;
  });
  const css = fs.readFileSync(path.join(__dirname, 'simple.css'), 'utf8');
  const html = `<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Your Plan</title><style>${css}</style></head><body>${body}</body></html>`;
  const htmlPath = path.join(os.tmpdir(), 'simple-plan-build.html'); fs.writeFileSync(htmlPath, html);
  const browser = await chromium.launch(); const page = await browser.newPage();
  await page.goto('file://' + htmlPath); await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: pdf, format: 'Letter', printBackground: true, displayHeaderFooter: true, preferCSSPageSize: true,
    headerTemplate: '<span></span>',
    footerTemplate: `<div style="font-family:Inter,sans-serif;font-size:7pt;color:#6b7480;width:100%;padding:0 0.6in;display:flex;justify-content:space-between;"><span>Your Plan · Nov 16, 2026 to 200 lb</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>`,
    margin: { top: '0.55in', bottom: '0.65in', left: '0.6in', right: '0.6in' } });
  await browser.close(); console.log('pdf written', pdf, fs.statSync(pdf).size);
})();
