# TouchGrass Music Fest · Set Times

A one-page, mobile-first schedule for both stages, styled after the
festival poster. No build step, no dependencies: upload the folder to any
static host and it works.

## Hosting it

Upload the whole folder (keep `index.html`, `css/`, `js/` and `img/` together).
Any of these work:

- **Netlify Drop** (netlify.com/drop): drag the folder onto the page.
- **GitHub Pages**: push the folder to a repo, enable Pages in Settings.
- **Vercel / Cloudflare Pages**: import the folder or repo, no framework needed.
- **Shared hosting / cPanel**: upload to `public_html` (or a subfolder like `public_html/settimes`).

Fonts load from Google Fonts. If a visitor's network blocks that, the page
falls back to Impact / Arial Narrow and still works.

## Updating set times

Everything lives in `js/data.js`. Times are 24-hour `"HH:MM"`:

```js
{ stage: "touch-grass", artist: "JID", start: "20:00", end: "20:45", photo: "img/jid.jpg" },
```

- Add or remove lines in `sets`; the page sorts them itself.
- `date`, `startTime` and `timeZone` drive the countdown and the live
  features. The countdown runs to `startTime` on `date` in that time zone,
  correct for every visitor wherever they are. On the day it hands off to
  the "Right now" bar, a now-line on the timeline, dims finished sets and
  opens scrolled to the current time.
- `stages` sets each stage's name, short name and color.
- `dayStart` / `dayEnd` set the hours shown on the timeline.

## Artist photos

Drop image files into `img/` and point each set's `photo` at the file.
`img/README.md` lists the filenames already wired up. Missing photos show a
monogram tile, so the page never looks broken while you collect them.
Photos are printed as a two-color duotone in the stage's color, so mixed
press shots and phone photos read as one set.

## Preview the live features before the day

Add `?now=HH:MM` to the URL to pretend it is that time on festival day:

```
index.html?now=15:30
```

## What's on the page

- **Countdown** to the first set, ticking every second, in the masthead.
- **Timeline**: both stages side by side, time down the left. Zoom with − / +.
- **List**: chronological cards with photos, grouped by hour.
- **Stage filter**: All / Touch Grass / Meadows.
- **My sets**: tap any set to save it (stored in the visitor's browser).
  Overlapping saved sets get an "Overlap" tag. "Copy list" copies the
  saved sets as text for sharing.
- `#list` / `#timeline` in the URL opens that view directly.
