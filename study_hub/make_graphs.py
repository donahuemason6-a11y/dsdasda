"""Inject to-scale SVG graphs into explained.html (reads explained_base.html, writes explained.html)."""
import os, math
D = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(D, "explained_base.html")).read()

ACC = "var(--accent)"; FG = "currentColor"; MUTED = "var(--muted)"; EX = "var(--ex)"
FONT = 'font-family="Public Sans, Helvetica, Arial, sans-serif"'

def fig(svg, caption):
    return f'<figure class="fig">{svg}<figcaption>{caption}</figcaption></figure>'

# ---------------- discrete distribution (Q3b) ----------------
def discrete_graph(xs, ps, ymax=0.35, w=360, h=230):
    L, R, T, B = 50, 20, 20, 50
    px = lambda i: L + (i + 0.5) * (w - L - R) / len(xs)
    py = lambda p: (h - B) - p / ymax * (h - B - T)
    s = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Probability distribution of X" {FONT} font-size="11">']
    # y axis + ticks
    s.append(f'<line x1="{L}" y1="{T}" x2="{L}" y2="{h-B}" stroke="{FG}" stroke-width="1"/>')
    for t in [0, 0.1, 0.2, 0.3]:
        y = py(t)
        s.append(f'<line x1="{L-4}" y1="{y:.1f}" x2="{w-R}" y2="{y:.1f}" stroke="{MUTED}" stroke-width="0.5" stroke-dasharray="2 3"/>')
        s.append(f'<text x="{L-7}" y="{y+4:.1f}" text-anchor="end" fill="{FG}">{t:.2f}</text>')
    # x axis
    s.append(f'<line x1="{L}" y1="{h-B}" x2="{w-R}" y2="{h-B}" stroke="{FG}" stroke-width="1"/>')
    bw = (w - L - R) / len(xs) * 0.5
    for i, (x, p) in enumerate(zip(xs, ps)):
        cx = px(i); y = py(p)
        s.append(f'<rect x="{cx-bw/2:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{(h-B)-y:.1f}" fill="{ACC}" fill-opacity="0.35" stroke="{ACC}" stroke-width="1.2"/>')
        s.append(f'<text x="{cx:.1f}" y="{y-5:.1f}" text-anchor="middle" fill="{FG}" font-weight="700">{p:.4f}</text>')
        s.append(f'<text x="{cx:.1f}" y="{h-B+16}" text-anchor="middle" fill="{FG}">{x}</text>')
    s.append(f'<text x="{(L+w-R)/2:.0f}" y="{h-8}" text-anchor="middle" fill="{FG}">x = number of games</text>')
    s.append(f'<text x="14" y="{(T+h-B)/2:.0f}" text-anchor="middle" fill="{FG}" transform="rotate(-90 14 {(T+h-B)/2:.0f})">P(x)</text>')
    s.append('</svg>')
    return "".join(s)

# ---------------- uniform (Q5) ----------------
def uniform_graph(a, b, shade=None, w=360, h=160, label_h="1/30"):
    L, R, T, B = 50, 20, 28, 46
    rect_h = 70
    px = lambda x: L + (x - a) / (b - a) * (w - L - R)
    top = h - B - rect_h
    s = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Uniform pdf" {FONT} font-size="11">']
    s.append(f'<line x1="{L}" y1="{T-10}" x2="{L}" y2="{h-B}" stroke="{FG}" stroke-width="1"/>')
    s.append(f'<line x1="{L-10}" y1="{h-B}" x2="{w-R}" y2="{h-B}" stroke="{FG}" stroke-width="1"/>')
    if shade:
        c, d = shade
        s.append(f'<rect x="{px(c):.1f}" y="{top}" width="{px(d)-px(c):.1f}" height="{rect_h}" fill="{ACC}" fill-opacity="0.4"/>')
    s.append(f'<rect x="{px(a):.1f}" y="{top}" width="{px(b)-px(a):.1f}" height="{rect_h}" fill="none" stroke="{FG}" stroke-width="1.5"/>')
    s.append(f'<line x1="{L-4}" y1="{top}" x2="{L}" y2="{top}" stroke="{FG}"/>')
    s.append(f'<text x="{L-7}" y="{top+4}" text-anchor="end" fill="{FG}">{label_h}</text>')
    s.append(f'<text x="{L-7}" y="{h-B+4}" text-anchor="end" fill="{FG}">0</text>')
    ticks = sorted(set([a, b] + (list(shade) if shade else [])))
    for t in ticks:
        s.append(f'<line x1="{px(t):.1f}" y1="{h-B}" x2="{px(t):.1f}" y2="{h-B+5}" stroke="{FG}"/>')
        s.append(f'<text x="{px(t):.1f}" y="{h-B+18}" text-anchor="middle" fill="{FG}">{t:g}</text>')
    if shade:
        c, d = shade
        s.append(f'<text x="{(px(c)+px(d))/2:.1f}" y="{top-8:.1f}" text-anchor="middle" fill="{FG}" font-weight="700">shaded area = {d-c:g}/{b-a:g} = {(d-c)/(b-a):.4f}</text>')
    else:
        s.append(f'<text x="{(px(a)+px(b))/2:.1f}" y="{top+rect_h/2+4:.1f}" text-anchor="middle" fill="{FG}" font-weight="700">total area = {b-a:g} × {label_h} = 1</text>')
    s.append(f'<text x="{(L+w-R)/2:.0f}" y="{h-6}" text-anchor="middle" fill="{FG}">x = temperature (°F)</text>')
    s.append('</svg>')
    return "".join(s)

# ---------------- normal curve ----------------
def normal_graph(mu, sigma, lo=None, hi=None, w=400, h=180, xlabel="x", zrow=True, cut_labels=None, area_text=None, unknown_cut=None):
    """Shade from lo to hi (None = tail). Axis ticks at mu ± kσ. cut_labels: dict value->label text."""
    L, R, T, B = 16, 16, 18, 52 if zrow else 40
    zmin, zmax = -3.6, 3.6
    px = lambda z: L + (z - zmin) / (zmax - zmin) * (w - L - R)
    base = h - B
    peak = base - T - 70
    py = lambda z: base - (base - peak) * math.exp(-z * z / 2)
    pts = [(px(z), py(z)) for z in [zmin + i * (zmax - zmin) / 160 for i in range(161)]]
    s = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Normal curve with shaded area" {FONT} font-size="11">']
    # shaded region
    zlo = zmin if lo is None else (lo - mu) / sigma
    zhi = zmax if hi is None else (hi - mu) / sigma
    zlo, zhi = max(zlo, zmin), min(zhi, zmax)
    n = 80
    poly = [f"{px(zlo):.1f},{base:.1f}"] + [f"{px(z):.1f},{py(z):.1f}" for z in [zlo + i * (zhi - zlo) / n for i in range(n + 1)]] + [f"{px(zhi):.1f},{base:.1f}"]
    s.append(f'<polygon points="{" ".join(poly)}" fill="{ACC}" fill-opacity="0.4"/>')
    # curve
    s.append('<polyline points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + f'" fill="none" stroke="{FG}" stroke-width="1.6"/>')
    # baseline
    s.append(f'<line x1="{L}" y1="{base}" x2="{w-R}" y2="{base}" stroke="{FG}" stroke-width="1"/>')
    # ticks at mu ± kσ
    for k in range(-3, 4):
        x = px(k)
        s.append(f'<line x1="{x:.1f}" y1="{base}" x2="{x:.1f}" y2="{base+4}" stroke="{FG}"/>')
        val = mu + k * sigma
        lab = f"{val:g}" if abs(val - round(val)) < 1e-9 else f"{val:.1f}"
        s.append(f'<text x="{x:.1f}" y="{base+15}" text-anchor="middle" fill="{FG}" font-size="10">{lab}</text>')
        if zrow:
            s.append(f'<text x="{x:.1f}" y="{base+28}" text-anchor="middle" fill="{MUTED}" font-size="9">z={k}</text>')
    s.append(f'<text x="{px(0):.1f}" y="{base+ (40 if zrow else 28)}" text-anchor="middle" fill="{FG}" font-size="10">{xlabel}</text>')
    # cut lines + labels
    for v in [v for v in (lo, hi) if v is not None]:
        z = (v - mu) / sigma; x = px(z)
        s.append(f'<line x1="{x:.1f}" y1="{T+12}" x2="{x:.1f}" y2="{base}" stroke="{EX}" stroke-width="1.5" stroke-dasharray="4 3"/>')
        lab = (cut_labels or {}).get(v, f"{v:g}")
        anchor_ = "middle" if 60 < x < w - 60 else ("start" if x <= 60 else "end")
        s.append(f'<text x="{x:.1f}" y="{T+6}" text-anchor="{anchor_}" fill="{EX}" font-weight="700" font-size="11">{lab}</text>')
    if unknown_cut is not None:
        z = (unknown_cut - mu) / sigma; x = px(z)
        s.append(f'<line x1="{x:.1f}" y1="{T+12}" x2="{x:.1f}" y2="{base}" stroke="{EX}" stroke-width="1.5" stroke-dasharray="4 3"/>')
        s.append(f'<text x="{x:.1f}" y="{T+6}" text-anchor="middle" fill="{EX}" font-weight="700" font-size="11">x = ?</text>')
    if area_text:
        # place the area label inside the shaded region
        zc = (zlo + zhi) / 2
        if lo is None and hi is not None and zhi < -1.2: zc = max(zhi - 1.2, zmin + 0.4)
        if hi is None and lo is not None and zlo > 1.2: zc = min(zlo + 1.2, zmax - 0.4)
        yc = base - 18
        s.append(f'<text x="{px(zc):.1f}" y="{yc:.1f}" text-anchor="middle" fill="{FG}" font-weight="700" font-size="11">{area_text}</text>')
    s.append('</svg>')
    return "".join(s)

out = base
def inject(anchor, html):
    global out
    assert out.count(anchor) == 1, anchor[:60]
    out = out.replace(anchor, anchor + html)

# Q3(b)
inject('Answer: four vertical lines/bars at 4, 5, 6, 7 with those heights; the tallest is at x = 6.</p>',
       fig(discrete_graph([4, 5, 6, 7], [0.2410, 0.2410, 0.3133, 0.2048]), "Q3(b): the probability distribution of X. One bar per value; height = P(x). Drawn to scale."))
# Q5
inject('Answer: a rectangle from 70 to 100 with height 1/30.</p>',
       fig(uniform_graph(70, 100), "Q5(a): the uniform pdf. Width 30, height 1/30, so the area is 1."))
inject('P(75 ≤ X ≤ 85) = (85 − 75)/(100 − 70) = 10/30 = 0.3333</pre>',
       fig(uniform_graph(70, 100, (75, 85)), "Q5(b): the shaded piece is 10 wide and 1/30 tall → area 0.3333."))
inject('P(X < 80) = (80 − 70)/(100 − 70) = 10/30 = 0.3333</pre>',
       fig(uniform_graph(70, 100, (70, 80)), "Q5(c): everything below 80 — a 10-wide piece → area 0.3333."))
# Q6
inject('Area left of z = −1.10 → table (row −1.1, column .00) = 0.1357</pre>',
       fig(normal_graph(0, 1, hi=-1.10, xlabel="z", zrow=False, cut_labels={-1.10: "z = −1.10"}, area_text="0.1357"), "Q6(a): standard normal; the shaded area to the left of z = −1.10 is what the table gives."))
inject('between = 0.9265 − 0.2743 = 0.6522</pre>',
       fig(normal_graph(0, 1, lo=-0.60, hi=1.45, xlabel="z", zrow=False, cut_labels={-0.60: "−0.60", 1.45: "1.45"}, area_text="0.6522"), "Q6(b): the strip between z = −0.60 and z = 1.45 = (left of 1.45) − (left of −0.60)."))
inject('P(70 < X < 95) = 0.9332 − 0.1587 = 0.7745</pre>',
       fig(normal_graph(80, 10, lo=70, hi=95, xlabel="x  (μ = 80, σ = 10)", cut_labels={70: "70 (z −1.00)", 95: "95 (z 1.50)"}, area_text="0.7745"), "Q6(c): X ~ N(80, 10). Shade 70 to 95; convert each endpoint to z; subtract the two left-areas."))
# Q7
inject('P(X > 125) = 1 − 0.9525 = 0.0475</pre>',
       fig(normal_graph(100, 15, lo=125, xlabel="IQ score  (μ = 100, σ = 15)", cut_labels={125: "125 (z 1.67)"}, area_text="0.0475"), "Q7(a): the right tail above 125. The table gives the unshaded left part (0.9525); the shaded tail is 1 − 0.9525."))
inject('P(X < 90) = area left of −0.67 = 0.2514</pre>',
       fig(normal_graph(100, 15, hi=90, xlabel="IQ score  (μ = 100, σ = 15)", cut_labels={90: "90 (z −0.67)"}, area_text="0.2514"), "Q7(b): the left tail below 90 — exactly the table value for z = −0.67."))
inject('P(110 < X < 140) = 0.9962 − 0.7486 = 0.2476</pre>',
       fig(normal_graph(100, 15, lo=110, hi=140, xlabel="IQ score  (μ = 100, σ = 15)", cut_labels={110: "110 (z 0.67)", 140: "140 (z 2.67)"}, area_text="0.2476"), "Q7(c): the strip from 110 to 140 = (left of 2.67) − (left of 0.67)."))
inject('x = μ + z·σ = 100 + 2.05(15) = 100 + 30.75 = 130.75 ≈ 131</pre>',
       fig(normal_graph(100, 15, hi=130.75, xlabel="IQ score  (μ = 100, σ = 15)", cut_labels={130.75: "x = 130.75 (z 2.05)"}, area_text="0.98"), "Q7(d): backwards — the shaded area 0.98 is given; find the z that leaves 0.98 to its left (2.05), then convert: 100 + 2.05(15) = 130.75."))

open(os.path.join(D, "explained.html"), "w").write(out)
print("graphs injected:", out.count('<figure class="fig">'))
