# TouchGrass Music Fest · Set Times

A one-page, mobile-first schedule for both stages. No build step, no
dependencies: upload the folder to any static host and it works.

## Hosting it

Upload the whole folder (keep `index.html`, `css/` and `js/` together).
Any of these work:

- **Netlify Drop** (netlify.com/drop): drag the folder onto the page.
- **GitHub Pages**: push the folder to a repo, enable Pages in Settings.
- **Vercel / Cloudflare Pages**: import the folder or repo, no framework needed.
- **Shared hosting / cPanel**: upload to `public_html` (or a subfolder like `public_html/settimes`).

Fonts load from Google Fonts. If the host blocks that, the page falls back
to Impact / Arial Narrow and still works.

## Updating set times

Everything lives in `js/data.js`. Times are 24-hour `"HH:MM"`:

```js
{ stage: "touch-grass", artist: "JID", start: "20:00", end: "20:45" },
```

- Add or remove lines in `sets`; the page sorts them itself.
- `date` (YYYY-MM-DD) and `timeZone` control the live features. On that
  day the page shows a "Right now" bar, a now-line on the timeline,
  dims finished sets and opens scrolled to the current time.
- `stages` sets each stage's name and color.
- `dayStart` / `dayEnd` set the hours shown on the timeline.

## Preview the live features before the day

Add `?now=HH:MM` to the URL to pretend it is that time on festival day:

```
index.html?now=15:30
```

## What's on the page

- **Timeline**: both stages side by side, time down the left. Zoom with − / +.
- **List**: chronological cards, grouped by hour.
- **Stage filter**: All / Touch Grass / Meadows.
- **My sets**: tap any set to save it (stored in the visitor's browser).
  Overlapping saved sets get an "Overlap" tag. "Copy list" copies the
  saved sets as text for sharing.
- `#list` / `#timeline` in the URL opens that view directly.
