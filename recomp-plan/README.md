# Road to 200

A week-by-week fat-loss plan: start Mon Nov 16, 2026 at 271 lb, finish at 200 lb (about Aug 1, 2027 on plan).

| File | What it is |
|---|---|
| `Your-Plan.pdf` | **The current plan.** Four pages: the weekly split, lifts, calories and protein, food, walking, and a goal weight for every week |
| `Your-Plan.md` | The same plan in Markdown |
| `tracker/road-to-200.html` | Source of the daily tracker page (weight chart against the plan, water, food log with saved foods) |
| `25-Week-Recomposition-Blueprint.pdf` / `.md` | The earlier long manual. Background reading only: it starts at 270 lb, uses a different exercise list and schedules diet-break weeks. Where it differs from `Your-Plan.pdf`, the plan wins |
| `Weekly-Check-In-Sheet.pdf`, `Quick-Reference-Card.pdf` | Print pages that belong to the long manual |
| `build/` | The scripts and stylesheets that turn the Markdown into the PDFs |

## Rebuilding the PDFs

Requires `pandoc`, Node.js and Playwright with Chromium.

```
node build/build_simple.js Your-Plan.md Your-Plan.pdf
node build/build_pdf.js 25-Week-Recomposition-Blueprint.md 25-Week-Recomposition-Blueprint.pdf
```

This is training and nutrition education, not medical care.
