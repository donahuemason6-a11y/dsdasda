/* =====================================================================
   TouchGrass Music Fest · Set Times
   Reads window.FESTIVAL (js/data.js) and renders the timeline and list
   views, saved sets, overlap warnings and the live "Right now" bar.
   No build step, no dependencies.
   ===================================================================== */
(function () {
  'use strict';

  var F = window.FESTIVAL;
  if (!F) return;

  /* ---------- helpers ---------- */
  var $ = function (sel, root) { return (root || document).querySelector(sel); };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };
  var toMin = function (t) { var p = t.split(':'); return Number(p[0]) * 60 + Number(p[1]); };
  var pad = function (n) { return (n < 10 ? '0' : '') + n; };
  var slug = function (s) { return String(s).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, ''); };
  var esc = function (s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  };
  function fmt(min, withMeridiem) {
    var h = Math.floor(min / 60) % 24, m = min % 60;
    var mer = h >= 12 ? 'PM' : 'AM';
    h = h % 12; if (h === 0) h = 12;
    return h + ':' + pad(m) + (withMeridiem ? ' ' + mer : '');
  }
  function fmtHour(min) {
    var h = Math.floor(min / 60) % 24;
    var mer = h >= 12 ? 'PM' : 'AM';
    h = h % 12; if (h === 0) h = 12;
    return h + ' ' + mer;
  }
  function fmtRange(s, e) {
    var sameMer = (Math.floor(s / 60) >= 12) === (Math.floor(e / 60) >= 12);
    return sameMer ? fmt(s) + '–' + fmt(e, true) : fmt(s, true) + '–' + fmt(e, true);
  }
  var store = {
    get: function (k) { try { return window.localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { window.localStorage.setItem(k, v); } catch (e) { /* private mode etc. */ } }
  };

  function initials(name) {
    var words = String(name).replace(/[_]/g, ' ').split(/[\s&]+/).filter(Boolean);
    if (!words.length) return '?';
    if (words.length === 1) {
      var caps = words[0].match(/[A-Z]/g) || [];
      var lower = words[0].match(/[a-z]/g) || [];
      /* mixed case like TiaCorine keeps its capitals; JID or Cochise use one letter */
      return (caps.length > 1 && lower.length ? caps.slice(0, 2).join('') : words[0][0]).toUpperCase();
    }
    return (words[0][0] + words[1][0]).toUpperCase();
  }
  /* The festival's wall clock, expressed as a UTC timestamp (handles daylight saving). */
  function wallClockUTC(ms, tz) {
    var parts = new Intl.DateTimeFormat('en-US', {
      timeZone: tz, year: 'numeric', month: '2-digit', day: '2-digit',
      hour: '2-digit', minute: '2-digit', second: '2-digit', hourCycle: 'h23'
    }).formatToParts(new Date(ms));
    var g = function (t) { var p = parts.filter(function (x) { return x.type === t; })[0]; return p ? parseInt(p.value, 10) : 0; };
    return Date.UTC(g('year'), g('month') - 1, g('day'), g('hour') % 24, g('minute'), g('second'));
  }
  function zonedToUTC(dateStr, timeStr, tz) {
    var d = dateStr.split('-').map(Number), t = timeStr.split(':').map(Number);
    var target = Date.UTC(d[0], d[1] - 1, d[2], t[0], t[1], 0);
    var utc = target;
    try { for (var i = 0; i < 3; i++) utc = utc - (wallClockUTC(utc, tz) - target); }
    catch (e) { return target; }
    return utc;
  }

  /* ---------- data ---------- */
  var DAY_START = toMin(F.dayStart), DAY_END = toMin(F.dayEnd), DAY_MINS = DAY_END - DAY_START;
  var stages = F.stages.map(function (st, i) {
    return { id: st.id, name: st.name, short: st.short || st.name, color: st.color, index: i };
  });
  var stageById = {};
  stages.forEach(function (st) { stageById[st.id] = st; });

  var sets = F.sets.map(function (s) {
    return {
      id: slug(s.stage + '-' + s.artist),
      stage: s.stage,
      stageObj: stageById[s.stage],
      artist: s.artist,
      photo: s.photo || '',
      s: toMin(s.start),
      e: toMin(s.end)
    };
  }).filter(function (s) { return s.stageObj && s.e > s.s; })
    .sort(function (a, b) { return a.s - b.s || a.stageObj.index - b.stageObj.index; });
  var setById = {};
  sets.forEach(function (s) { setById[s.id] = s; });

  /* ---------- state ---------- */
  var LS_FAVS = 'tgmf-favs', LS_PPM = 'tgmf-ppm', LS_VIEW = 'tgmf-view';
  var PPM_STEPS = [2.0, 2.8, 3.8];
  var state = { view: 'timeline', stage: 'all', mine: false, favs: {}, ppm: 2.8, now: { eventDay: false, mins: 0 } };

  try {
    var raw = store.get(LS_FAVS);
    if (raw) JSON.parse(raw).forEach(function (id) { if (setById[id]) state.favs[id] = true; });
  } catch (e) { /* ignore bad storage */ }
  var savedPpm = parseFloat(store.get(LS_PPM));
  if (PPM_STEPS.indexOf(savedPpm) !== -1) state.ppm = savedPpm;
  var hashView = location.hash.replace('#', '');
  if (hashView === 'list' || hashView === 'timeline') state.view = hashView;
  else { var v = store.get(LS_VIEW); if (v === 'list' || v === 'timeline') state.view = v; }

  var favCount = function () { return Object.keys(state.favs).length; };
  var isFav = function (id) { return state.favs[id] === true; };
  var favList = function () { return sets.filter(function (s) { return isFav(s.id); }); };
  var visibleStages = function () {
    return state.stage === 'all' ? stages : stages.filter(function (s) { return s.id === state.stage; });
  };

  /* Saved sets that overlap another saved set (on any stage). */
  function conflicts() {
    var favs = favList(), out = {};
    for (var i = 0; i < favs.length; i++) {
      for (var j = i + 1; j < favs.length; j++) {
        var a = favs[i], b = favs[j];
        if (a.s < b.e && b.s < a.e) { out[a.id] = true; out[b.id] = true; }
      }
    }
    return out;
  }

  /* ---------- "now" in the festival's time zone ---------- */
  function computeNow() {
    var override = null;
    try { override = new URLSearchParams(location.search).get('now'); } catch (e) { /* old browser */ }
    if (override && /^\d{1,2}:\d{2}$/.test(override)) return { eventDay: true, mins: toMin(override) };
    try {
      var parts = new Intl.DateTimeFormat('en-US', {
        timeZone: F.timeZone, year: 'numeric', month: '2-digit', day: '2-digit',
        hour: '2-digit', minute: '2-digit', hourCycle: 'h23'
      }).formatToParts(new Date());
      var g = function (t) { var p = parts.filter(function (x) { return x.type === t; })[0]; return p ? p.value : ''; };
      var date = g('year') + '-' + g('month') + '-' + g('day');
      var h = parseInt(g('hour'), 10) % 24;
      return { eventDay: date === F.date, mins: h * 60 + parseInt(g('minute'), 10) };
    } catch (e) {
      return { eventDay: false, mins: 0 };
    }
  }
  function statusClass(s) {
    if (!state.now.eventDay) return '';
    var m = state.now.mins;
    if (m >= s.e) return 'is-past';
    if (m >= s.s) return 'is-live';
    return '';
  }

  /* ---------- rendering ---------- */
  function thumb(s) {
    return '<span class="thumb' + (s.photo ? '' : ' no-photo') + '" aria-hidden="true">' +
      (s.photo ? '<img class="photo" src="' + esc(s.photo) + '" alt="" loading="lazy" decoding="async">' : '') +
      '<span class="mono">' + esc(initials(s.artist)) + '</span></span>';
  }
  /* Photos that fail to load fall back to the monogram tile. */
  function watchPhotos(root) {
    $$('img.photo', root).forEach(function (img) {
      if (img.complete && img.naturalWidth === 0) { img.parentNode.classList.add('no-photo'); return; }
      img.addEventListener('error', function () { img.parentNode.classList.add('no-photo'); });
    });
  }

  function setBlock(s, conf) {
    var fav = isFav(s.id);
    var cls = ['set', fav ? 'is-fav' : '', conf[s.id] ? 'is-conflict' : '', statusClass(s)].filter(Boolean).join(' ');
    var top = Math.max(0, s.s - DAY_START);
    var dur = Math.min(s.e, DAY_END) - Math.max(s.s, DAY_START);
    if (dur <= 0) return '';
    return '<button type="button" class="' + cls + '" data-id="' + s.id + '" style="--s:' + top + ';--d:' + dur + '"' +
      ' aria-pressed="' + fav + '" aria-label="' + esc(s.artist) + ', ' + fmtRange(s.s, s.e) + ', ' + esc(s.stageObj.name) + '. Tap to save.">' +
      thumb(s) +
      '<span class="set-inner">' +
        '<span class="set-name"><i class="live-dot" aria-hidden="true"></i>' + esc(s.artist) + '</span>' +
        '<span class="set-time">' + fmtRange(s.s, s.e) + '</span>' +
      '</span>' +
      '<span class="star" aria-hidden="true"></span>' +
      '<span class="flag">Overlap</span>' +
    '</button>';
  }

  function renderTimeline() {
    var vs = visibleStages();
    var conf = conflicts();
    var head = vs.map(function (st) {
      var n = sets.filter(function (s) { return s.stage === st.id; }).length;
      return '<div class="stage-head" style="--c:' + st.color + '"><span class="long">' + esc(st.name) + '</span>' +
        '<span class="short">' + esc(st.short) + '</span><small>' + n + ' sets</small></div>';
    }).join('');
    var hours = [];
    for (var m = Math.ceil(DAY_START / 60) * 60; m <= DAY_END; m += 60) {
      var h = Math.floor(m / 60) % 24, h12 = h % 12 || 12;
      hours.push('<div class="hour" style="--m:' + (m - DAY_START) + '">' + h12 + '<small>' + (h >= 12 ? 'PM' : 'AM') + '</small></div>');
    }
    var cols = vs.map(function (st) {
      var items = sets.filter(function (s) { return s.stage === st.id; }).map(function (s) { return setBlock(s, conf); }).join('');
      return '<div class="col" data-stage="' + st.id + '" style="--c:' + st.color + '">' + items + '</div>';
    }).join('');
    var grid = $('#grid');
    grid.style.setProperty('--cols', vs.length);
    grid.innerHTML =
      '<div class="grid-head"><div class="corner">' + esc(tzAbbr()) + '</div>' + head + '</div>' +
      '<div class="grid-body" style="--day-mins:' + DAY_MINS + '">' +
        '<div class="gutter">' + hours.join('') + '</div>' + cols +
        '<div class="now-line" id="nowLine" hidden><span id="nowLabel"></span></div>' +
      '</div>';
    watchPhotos(grid);
  }

  function card(s, conf) {
    var fav = isFav(s.id);
    var cls = ['card', fav ? 'is-fav' : '', conf[s.id] ? 'is-conflict' : '', statusClass(s)].filter(Boolean).join(' ');
    return '<button type="button" class="' + cls + '" data-id="' + s.id + '" style="--c:' + s.stageObj.color + '" aria-pressed="' + fav + '">' +
      thumb(s) +
      '<span class="card-time"><b>' + fmt(s.s) + '</b><span>to ' + fmt(s.e, true) + '</span></span>' +
      '<span class="card-main">' +
        '<span class="card-name">' + esc(s.artist) + '</span>' +
        '<span class="card-stage"><i class="dot"></i>' + esc(s.stageObj.name) +
          '<span class="tag tag-live">On now</span><span class="tag tag-conflict">Overlaps</span>' +
        '</span>' +
      '</span>' +
      '<span class="star" aria-hidden="true"></span>' +
    '</button>';
  }

  function renderList() {
    var vs = {};
    visibleStages().forEach(function (st) { vs[st.id] = true; });
    var conf = conflicts();
    var items = sets.filter(function (s) { return vs[s.stage]; });
    if (state.mine) items = items.filter(function (s) { return isFav(s.id); });
    var root = $('#listRoot');
    if (!items.length) {
      root.innerHTML = '<p class="empty">' + (state.mine
        ? 'Nothing saved yet. Tap any set to save it.'
        : 'No sets to show.') + '</p>';
      return;
    }
    var groups = [], byHour = {};
    items.forEach(function (s) {
      var h = Math.floor(s.s / 60) * 60;
      if (!byHour[h]) { byHour[h] = []; groups.push(h); }
      byHour[h].push(s);
    });
    root.innerHTML = groups.map(function (h) {
      return '<section class="hour-group"><h2 class="hour-label">' + fmtHour(h) + '</h2><ul class="cards">' +
        byHour[h].map(function (s) { return '<li>' + card(s, conf) + '</li>'; }).join('') +
      '</ul></section>';
    }).join('');
    watchPhotos(root);
  }

  function renderLive() {
    var live = $('#live'), now = state.now, m = now.mins;
    if (!now.eventDay || m < DAY_START - 90 || m > DAY_END) { live.hidden = true; live.innerHTML = ''; return; }
    var items = stages.map(function (st) {
      var on = null, next = null;
      for (var i = 0; i < sets.length; i++) {
        var s = sets[i];
        if (s.stage !== st.id) continue;
        if (!on && s.s <= m && m < s.e) on = s;
        if (!next && s.s > m) next = s;
      }
      var body = on ? '<b>' + esc(on.artist) + '</b><span>until ' + fmt(on.e, true) + '</span>'
        : next ? '<b>' + esc(next.artist) + '</b><span>up next · ' + fmt(next.s, true) + '</span>'
        : '<b>Done for the night</b>';
      return '<div class="live-item" style="--c:' + st.color + '"><i class="dot"></i><span class="live-stage">' + esc(st.short) + '</span>' + body + '</div>';
    }).join('');
    live.innerHTML = '<div class="wrap"><span class="live-tag"><i class="live-dot"></i>Right now</span>' + items + '</div>';
    live.hidden = false;
  }

  /* ---------- countdown to the first note ---------- */
  var START_AT = zonedToUTC(F.date, F.startTime || F.dayStart, F.timeZone);
  var END_AT = zonedToUTC(F.date, F.dayEnd, F.timeZone);
  function tzAbbr() {
    if (tzAbbr.value !== undefined) return tzAbbr.value;
    try {
      var p = new Intl.DateTimeFormat('en-US', { timeZone: F.timeZone, timeZoneName: 'short' })
        .formatToParts(new Date(zonedToUTC(F.date, F.startTime || F.dayStart, F.timeZone)))
        .filter(function (x) { return x.type === 'timeZoneName'; })[0];
      tzAbbr.value = p ? p.value : '';
    } catch (e) { tzAbbr.value = ''; }
    return tzAbbr.value;
  }
  var cdLast = '';
  function renderCountdown() {
    var el = $('#countdown');
    if (!el) return;
    var override = false;
    try { override = /^\d{1,2}:\d{2}$/.test(new URLSearchParams(location.search).get('now') || ''); } catch (e) { /* ignore */ }
    var nowMs = Date.now();
    var diff = override ? -1 : START_AT - nowMs;
    var mode = diff > 0 ? 'before' : (override || nowMs < END_AT) ? 'live' : 'after';
    if (mode !== cdLast) {
      var first = cdLast === '';
      el.setAttribute('data-mode', mode);
      var masthead = $('.masthead');
      if (masthead) masthead.classList.toggle('is-live', mode !== 'before');
      cdLast = mode;
      if (!first) refreshNow();
      if (mode === 'live') {
        el.innerHTML = '<span class="cd-label"><i class="live-dot"></i>Happening now</span>' +
          '<span class="cd-note">Day of show \u00b7 scroll for what\u2019s on</span>';
      } else if (mode === 'after') {
        el.innerHTML = '<span class="cd-label">That\u2019s a wrap</span>' +
          '<span class="cd-note">Thanks for touching grass with us.</span>';
      } else {
        el.innerHTML = '<span class="cd-label">Music starts in</span>' +
          '<span class="cd-units">' + ['Days', 'Hrs', 'Min', 'Sec'].map(function (n) {
            return '<span class="cd-unit"><b class="cd-num" data-unit="' + n + '">00</b><span class="cd-name">' + n + '</span></span>';
          }).join('') + '</span>';
      }
    }
    if (mode !== 'before') return;
    var secs = Math.floor(diff / 1000);
    var d = Math.floor(secs / 86400), h = Math.floor(secs % 86400 / 3600), m = Math.floor(secs % 3600 / 60), sec = secs % 60;
    var vals = { Days: String(d), Hrs: pad(h), Min: pad(m), Sec: pad(sec) };
    $$('.cd-num', el).forEach(function (n) {
      var v = vals[n.getAttribute('data-unit')];
      if (n.textContent !== v) n.textContent = v;
    });
  }

  function renderMineBar() {
    var bar = $('#minebar');
    if (!state.mine) { bar.hidden = true; return; }
    var n = favCount(), c = Object.keys(conflicts()).length;
    $('#mineSummary').innerHTML = n
      ? '<b>' + n + '</b> set' + (n === 1 ? '' : 's') + ' saved' + (c ? ' <span class="warn">' + c + ' overlap</span>' : '')
      : 'Tap any set to save it here';
    $('#copyBtn').hidden = !n;
    $('#clearBtn').hidden = !n;
    bar.hidden = false;
  }

  /* Patch favorite/overlap state in place so scroll position and focus survive. */
  function refreshFavUI() {
    var conf = conflicts();
    $$('[data-id]').forEach(function (el) {
      var id = el.getAttribute('data-id'), fav = isFav(id);
      el.classList.toggle('is-fav', fav);
      el.classList.toggle('is-conflict', !!conf[id]);
      el.setAttribute('aria-pressed', fav);
    });
    $('#mineCount').textContent = favCount();
    renderMineBar();
    if (state.mine && state.view === 'list') renderList();
  }

  function refreshNow() {
    state.now = computeNow();
    var ev = state.now.eventDay, m = state.now.mins;
    $$('[data-id]').forEach(function (el) {
      var s = setById[el.getAttribute('data-id')];
      if (!s) return;
      el.classList.toggle('is-past', ev && m >= s.e);
      el.classList.toggle('is-live', ev && m >= s.s && m < s.e);
    });
    var inDay = ev && m >= DAY_START && m <= DAY_END;
    var line = $('#nowLine');
    if (line) {
      line.hidden = !inDay;
      line.style.setProperty('--t', m - DAY_START);
      $('#nowLabel').textContent = fmt(m, true);
    }
    $('#nowBtn').hidden = !(inDay && state.view === 'timeline');
    renderLive();
  }

  /* ---------- actions ---------- */
  function toggleFav(id) {
    if (isFav(id)) delete state.favs[id]; else state.favs[id] = true;
    store.set(LS_FAVS, JSON.stringify(Object.keys(state.favs)));
    refreshFavUI();
  }

  function setView(view) {
    state.view = view;
    store.set(LS_VIEW, view);
    $$('.seg-btn').forEach(function (b) {
      var on = b.getAttribute('data-view') === view;
      b.classList.toggle('is-active', on);
      b.setAttribute('aria-selected', on);
    });
    $('#timeline').hidden = view !== 'timeline';
    $('#list').hidden = view !== 'list';
    $('#zoomOut').hidden = view !== 'timeline';
    $('#zoomIn').hidden = view !== 'timeline';
    try { history.replaceState(null, '', '#' + view); } catch (e) { /* file:// etc. */ }
    if (view === 'list') renderList();
    refreshNow();
  }

  function setStage(id) {
    state.stage = id;
    $$('.chip[data-stage]').forEach(function (b) {
      var on = b.getAttribute('data-stage') === id;
      b.classList.toggle('is-active', on);
      b.setAttribute('aria-pressed', on);
    });
    renderTimeline();
    renderList();
    refreshNow();
  }

  function setMine(on) {
    state.mine = on;
    document.body.classList.toggle('mine-only', on);
    var btn = $('#mineBtn');
    btn.classList.toggle('is-active', on);
    btn.setAttribute('aria-pressed', on);
    renderMineBar();
    renderList();
    refreshNow();
  }

  function setPpm(ppm) {
    state.ppm = ppm;
    document.documentElement.style.setProperty('--ppm', ppm);
    store.set(LS_PPM, String(ppm));
    $('#zoomOut').disabled = ppm === PPM_STEPS[0];
    $('#zoomIn').disabled = ppm === PPM_STEPS[PPM_STEPS.length - 1];
  }
  function zoom(dir) {
    var i = PPM_STEPS.indexOf(state.ppm) + dir;
    if (i < 0 || i >= PPM_STEPS.length) return;
    /* keep the same minute under the top of the viewport while zooming */
    var body = $('.grid-body'), before = body ? body.getBoundingClientRect().top : 0;
    var minuteAtTop = body ? Math.max(0, -before) / state.ppm : 0;
    setPpm(PPM_STEPS[i]);
    if (body) {
      var after = body.getBoundingClientRect().top + window.pageYOffset;
      window.scrollTo(0, after + minuteAtTop * state.ppm);
    }
  }

  function jumpToNow(smooth) {
    var line = $('#nowLine');
    if (!line || line.hidden) return;
    var toolbar = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--toolbar-h')) || 58;
    var y = line.getBoundingClientRect().top + window.pageYOffset - toolbar - 140;
    try { window.scrollTo({ top: Math.max(0, y), behavior: smooth ? 'smooth' : 'auto' }); }
    catch (e) { window.scrollTo(0, Math.max(0, y)); }
  }

  var toastTimer = null;
  function toast(msg) {
    var el = $('#toast');
    el.textContent = msg;
    el.hidden = false;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { el.hidden = true; }, 2200);
  }

  function copyList() {
    var list = favList();
    if (!list.length) { toast('Nothing saved yet'); return; }
    var lines = ['My ' + F.name + ' sets · ' + F.dateLabel];
    list.forEach(function (s) { lines.push(fmtRange(s.s, s.e) + '  ' + s.artist + ' — ' + s.stageObj.name); });
    var text = lines.join('\n');
    var done = function () { toast('Copied — paste it anywhere'); };
    var fallback = function () {
      var ta = document.createElement('textarea');
      ta.value = text; ta.setAttribute('readonly', '');
      ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy'); done(); } catch (e) { toast('Copy failed on this browser'); }
      document.body.removeChild(ta);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(done, fallback);
    else fallback();
  }

  var clearArmed = null;
  function clearAll() {
    var btn = $('#clearBtn');
    if (!clearArmed) {
      btn.textContent = 'Tap again to clear';
      btn.classList.add('is-danger');
      clearArmed = setTimeout(function () { clearArmed = null; btn.textContent = 'Clear all'; btn.classList.remove('is-danger'); }, 3000);
      return;
    }
    clearTimeout(clearArmed); clearArmed = null;
    btn.textContent = 'Clear all'; btn.classList.remove('is-danger');
    state.favs = {};
    store.set(LS_FAVS, '[]');
    refreshFavUI();
    toast('Saved sets cleared');
  }

  /* ---------- wire up ---------- */
  function init() {
    $('#festName').textContent = F.name;
    $('#festVenue').textContent = F.venue + (F.city ? ', ' + F.city : '');
    $('#festDate').textContent = F.dateShort || F.dateLabel;
    $('#festHours').textContent = fmtHour(DAY_START) + ' \u2013 ' + fmtHour(DAY_END);
    $('#festStages').textContent = stages.length === 1 ? 'One stage' : stages.length === 2 ? 'Two stages' : stages.length + ' stages';
    $('#footNote').textContent = F.note || '';
    document.title = F.name + ' · Set Times';

    var chips = $('#stageChips');
    chips.innerHTML = '<button type="button" class="chip is-active" data-stage="all" style="--c:var(--ink)" aria-pressed="true">All</button>' +
      stages.map(function (st) {
        return '<button type="button" class="chip" data-stage="' + st.id + '" style="--c:' + st.color + '" aria-pressed="false"><i class="dot"></i>' + esc(st.short) + '</button>';
      }).join('');

    setPpm(state.ppm);
    renderTimeline();
    renderList();
    refreshFavUI();
    setView(state.view);

    document.addEventListener('click', function (ev) {
      var t = ev.target.closest ? ev.target.closest('[data-id], [data-view], [data-stage]') : null;
      if (!t) return;
      if (t.hasAttribute('data-id')) toggleFav(t.getAttribute('data-id'));
      else if (t.hasAttribute('data-view')) setView(t.getAttribute('data-view'));
      else if (t.hasAttribute('data-stage')) setStage(t.getAttribute('data-stage'));
    });
    $('#mineBtn').addEventListener('click', function () { setMine(!state.mine); });
    $('#zoomOut').addEventListener('click', function () { zoom(-1); });
    $('#zoomIn').addEventListener('click', function () { zoom(1); });
    $('#nowBtn').addEventListener('click', function () { jumpToNow(true); });
    $('#copyBtn').addEventListener('click', copyList);
    $('#clearBtn').addEventListener('click', clearAll);

    /* keep the sticky stage header just under the toolbar, whatever its height */
    var toolbar = $('#toolbar');
    var measure = function () { document.documentElement.style.setProperty('--toolbar-h', toolbar.offsetHeight + 'px'); };
    measure();
    if (window.ResizeObserver) new ResizeObserver(measure).observe(toolbar);
    else window.addEventListener('resize', measure);

    /* tick on the whole second so the countdown never skips or doubles a digit */
    (function tick() { renderCountdown(); setTimeout(tick, 1000 - (Date.now() % 1000)); })();
    setInterval(refreshNow, 30000);
    document.addEventListener('visibilitychange', function () { if (!document.hidden) { renderCountdown(); refreshNow(); } });

    /* on the festival day, open on what's happening now */
    if (state.now.eventDay && state.view === 'timeline') {
      window.requestAnimationFrame(function () { jumpToNow(false); });
    }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
