# The 25-Week Recomposition Blueprint

A week-by-week fat-loss and recomposition manual: Phase 1 runs Mon Nov 16, 2026 to Sun May 9, 2027 (25 weeks), and Phase 2 continues the same system to a finish line of 200 lb or a waist of 35.5 in, followed by a 4-week reverse diet.

| File | What it is |
|---|---|
| `Simple-Plan.pdf` | Start here: three pages with the daily split, calories, protein and walking minutes for every week |
| `Simple-Plan.md` | The simple plan in Markdown |
| `25-Week-Recomposition-Blueprint.pdf` | The full manual, laid out for printing (US Letter) |
| `25-Week-Recomposition-Blueprint.md` | The same manual in Markdown, with page-break markers between sections |
| `Weekly-Check-In-Sheet.pdf` | Section 6.2 on its own: two pages, print one per week |
| `Quick-Reference-Card.pdf` | The one-page appendix for the gym bag |
| `build/` | The scripts and stylesheets that turn the Markdown into the PDFs |

## Rebuilding the PDF

Requires `pandoc`, Node.js and Playwright with Chromium.

```
node build/build_pdf.js 25-Week-Recomposition-Blueprint.md 25-Week-Recomposition-Blueprint.pdf
```

The simple plan builds the same way with its own script:

```
node build/build_simple.js Simple-Plan.md Simple-Plan.pdf
```

Any Markdown-to-PDF tool that honors `<div style="page-break-after: always;"></div>` will also work.

This manual is training and nutrition education, not medical care. Section 1.8 lists what to get checked before starting and the signs that mean stop and see a doctor.
