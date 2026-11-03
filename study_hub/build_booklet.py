import math, re
from math import erf, sqrt, comb
BASE = '/tmp/claude-0/-home-user-dsdasda/bdc32f87-6f2d-5f62-952a-43c9c6f6142d/scratchpad/ex2/'
KATEX = "file://" + BASE + "katex/node_modules/katex/dist"
OUT = "/home/user/dsdasda/STA2023_Exam2_EVERY_SCENARIO_WORKED.html"
ns = {'__file__': BASE + 'make_graphs.py'}
exec(open(BASE + 'make_graphs.py').read().split('\ndef inject(')[0], ns)
discrete_graph, uniform_graph, normal_graph, fig = ns['discrete_graph'], ns['uniform_graph'], ns['normal_graph'], ns['fig']
Phi = lambda z: 0.5 * (1 + erf(z / sqrt(2)))

def esc(t): return t.replace("<", "&lt;").replace(">", "&gt;")
def D(t): return "<div class='dm'>\\[" + esc(t) + "\\]</div>"
def M(t): return "\\(" + esc(t) + "\\)"
def f4(v): return f"{v:.4f}"
def fx(v, nd=10):
    s = f"{v:.{nd}f}".rstrip('0').rstrip('.')
    return s if s else "0"

CSS = r"""
:root { --accent:#cc0000; --muted:#666; --ex:#0033cc; }
@page { size: letter; margin: 0.5in 0.55in; }
body { font-family: Helvetica, Arial, sans-serif; font-size: 10.5pt; line-height: 1.33; color:#000; margin:0; }
h1 { font-size: 19pt; margin: 0 0 4pt; }
h2 { font-size: 15pt; background:#000; color:#fff; padding: 3pt 8pt; margin: 16pt 0 8pt; break-after: avoid; }
.setup { border-left: 4px solid #007a1f; color:#007a1f; padding: 4pt 10pt; margin: 6pt 0 8pt; }
.recipe { border: 1.2pt solid #cc0000; padding: 5pt 9pt; margin: 6pt 0 10pt; }
.recipe b.t { color:#cc0000; }
.recipe ol { margin: 2pt 0 0; padding-left: 20pt; }
.card { break-inside: avoid; border: 0.8pt solid #999; border-radius: 4pt; padding: 7pt 10pt 8pt; margin: 0 0 9pt; display:flex; gap: 12pt; }
.card.blk { display:block; } .card.long { break-inside: auto; }
.st { break-inside: avoid; }
.card .txt { flex: 1 1 62%; min-width: 0; } .card .gfx { flex: 0 0 36%; } .card .gfx svg { width:100%; height:auto; }
.ph { font-size: 13pt; font-weight: bold; color:#0033cc; margin: 0 0 2pt; }
.ask { color:#0033cc; margin: 0 0 5pt; }
.st { margin: 0 0 5pt; padding-left: 4pt; border-left: 2pt solid #ddd; }
.st b.n { color:#007a1f; }
.dm { margin: 1pt 0 1pt 8pt; } .katex-display { margin: 2pt 0 !important; text-align:left !important; } .katex { font-size: 1.05em; }
.katex-display > .katex { white-space: normal; }
.ans { display:inline-block; border: 1.4pt solid #cc0000; color:#cc0000; font-weight:bold; padding: 2pt 8pt; margin: 3pt 6pt 0 0; }
.say { display:block; margin-top: 4pt; font-size: 9.8pt; } .say b { color:#007a1f; }
.why { color:#cc0000; margin: 4pt 0 0; font-size: 9.8pt; }
.dots { font-family: monospace; font-size: 11pt; margin: 3pt 0; letter-spacing: 1px; } .dots b { color:#cc0000; }
figure.fig { margin:0; } figcaption { font-size: 9pt; color:#333; text-align:center; }
.note { font-size: 10pt; color:#333; margin: 0 0 8pt; }
"""
H = []
CARDS = []; SECTION = ["intro"]
import json
def card(phrase, ask, steps, answer, say=None, why=None, gfx=None):
    """steps: list of (label, text, math) ; math may be None, a string, or a list of strings (one display each)."""
    body = ""
    for i, (lab, txt, mth) in enumerate(steps, 1):
        if isinstance(mth, str): mth = [mth]
        body += f'<div class="st"><b class="n">Step {i} · {lab}</b> {txt}' + "".join(D(m) for m in (mth or [])) + '</div>'
    g = f'<div class="gfx">{gfx}</div>' if gfx else ''
    s = f'<span class="say"><b>Write on the exam:</b> {say}</span>' if say else ''
    w = f'<div class="why"><b>Watch out:</b> {why}</div>' if why else ''
    cls = "card" + ("" if gfx else " blk") + (" long" if (not gfx and len(steps) >= 6) else "")
    H.append(f'<div class="{cls}"><div class="txt"><div class="ph">{phrase}</div><div class="ask">{ask}</div>{body}<span class="ans">{answer}</span>{s}{w}</div>{g}</div>')
    CARDS.append({"section": SECTION[0], "phrase": re.sub(r"<[^>]+>", "", phrase), "ask": re.sub(r"<[^>]+>", "", ask),
                  "steps": [{"label": lab, "text": re.sub(r"<[^>]+>", " ", txt).strip(), "math": (mth if isinstance(mth, list) else ([mth] if mth else []))} for lab, txt, mth in steps],
                  "answer": answer, "write": say or "", "watch_out": why or ""})
def recipe(title, items):
    H.append(f'<div class="recipe"><b class="t">{title}</b><ol>' + "".join(f"<li>{i}</li>" for i in items) + '</ol></div>')

# ---------- graph wrappers ----------
def normal(mu, sd, lo=None, hi=None, area=None, unknown=None, xl="x", outside=False):
    zrow = (mu != 0)
    labels = {v: (unknown if unknown else (f"{v:.2f}" if mu == 0 else f"{v:g}")) for v in (lo, hi) if v is not None}
    if not outside:
        return normal_graph(mu, sd, lo=lo, hi=hi, w=360, h=170, xlabel=xl, zrow=zrow, cut_labels=labels, area_text=area)
    mid = normal_graph(mu, sd, lo=lo, hi=hi, w=360, h=170, xlabel=xl, zrow=zrow, cut_labels=labels)
    full = normal_graph(mu, sd, w=360, h=170, xlabel=xl, zrow=zrow)
    poly_full = re.search(r'<polygon[^>]*/>', full).group(0)
    poly_mid = re.search(r'<polygon[^>]*/>', mid).group(0)
    white = poly_mid.replace('fill="var(--accent)" fill-opacity="0.4"', 'fill="#fff" fill-opacity="1"')
    g = mid.replace(poly_mid, poly_full + white)
    px = lambda z: 16 + (z + 3.6) / 7.2 * (360 - 32)
    base = 170 - (52 if zrow else 40)
    za, zb = (lo - mu) / sd, (hi - mu) / sd
    lab = ''.join(f'<text x="{px(z):.1f}" y="{base-18}" text-anchor="middle" fill="#000" font-weight="700" font-size="11">{t}</text>'
                  for z, t in ((max(za - 1.1, -3.2), area[0]), (min(zb + 1.1, 3.2), area[1])))
    return g.replace('</svg>', lab + '</svg>')
def discrete_hl(xs, ps, inc):
    g = discrete_graph(xs, ps)
    rects = re.findall(r'<rect[^>]*/>', g)
    for x, r in zip(xs, rects):
        if x not in inc:
            g = g.replace(r, r.replace('fill="var(--accent)" fill-opacity="0.35" stroke="var(--accent)"', 'fill="#ddd" fill-opacity="1" stroke="#999"'), 1)
    return g

H.append('<h1>STA2023 Exam 2 — every scenario, solved step by step</h1>'
         '<p class="note">Study copy (too long to bring in; the two-sided cheat sheet is the one you bring). One box per way a question can be phrased. '
         'Each box is complete on its own: the words → what they really ask → numbered steps with the real math → the boxed answer → the sentence to write. '
         'Same numbers as the practice exam, so on the real exam you keep the steps and swap the numbers.</p>')

# =====================================================================
# Q1
# =====================================================================
SECTION[0] = 'Question 1'
H.append('<h2>Question 1 — two-way table (or / and / given / not / two picks)</h2>')
H.append('<div class="setup">Employment status of 78 residents.<br>Males / Females — Full-time 22 / 18 (row total 40) · Part-time 6 / 10 (16) · Unemployed 3 / 2 (5) · Not in labor force 5 / 12 (17).<br>Column totals: males 36, females 42. Grand total 78.</div>')
recipe("The recipe for every table question", [
    "Find the numbers: the cell, the row total, the column total, the grand total.",
    "Pick the rule from the key word: <b>is A</b> → A's total ÷ 78 · <b>A or B</b> → add the two totals, subtract the overlap cell once · <b>A and B</b> → the one cell ÷ 78 · <b>A given B</b> → the cell ÷ B's total (not 78) · <b>not A</b> → 1 − P(A).",
    "Write the fraction, then the decimal to 4 places, box it."])
card("is male", "Out of everybody, what fraction are male? One category → its total ÷ grand total.",
     [("Find the numbers", "Male is a column; its total is 36. Grand total 78.", None),
      ("Rule", "P(A) = (number in A) ÷ (total).", r"P(\text{male})=\frac{\text{males}}{\text{total}}"),
      ("Plug in and compute", "", r"P(\text{male})=\frac{36}{78}=0.4615")],
     "0.4615", say="P(male) = 36/78 = 0.4615.")
card("is part-time", "A row: add both cells of the row, then ÷ 78.",
     [("Find the numbers", "Part-time row: 6 males + 10 females.", r"6+10=16"),
      ("Rule", "", r"P(\text{part-time})=\frac{\text{part-time total}}{\text{total}}"),
      ("Plug in and compute", "", r"P(\text{part-time})=\frac{16}{78}=0.2051")],
     "0.2051")
card("is NOT male", "The complement: everything except male.",
     [("Find the numbers", "Males 36, total 78.", None),
      ("Rule", "P(not A) = 1 − P(A).", r"P(\text{not male})=1-P(\text{male})"),
      ("Plug in and compute", "", r"P(\text{not male})=1-\frac{36}{78}=\frac{42}{78}=0.5385")],
     "0.5385", why="Same thing as counting the females directly: 42 ÷ 78.")
card("male OR unemployed", "Either group, or both. Adding the two totals counts the overlap (male AND unemployed) twice, so subtract it once.",
     [("Find the numbers", "Males 36. Unemployed 5. Overlap (unemployed males) 3.", None),
      ("Rule", "", r"P(A\text{ or }B)=P(A)+P(B)-P(A\text{ and }B)"),
      ("Plug in", "", r"P(\text{M or U})=\frac{36}{78}+\frac{5}{78}-\frac{3}{78}"),
      ("Compute", "", r"=\frac{36+5-3}{78}=\frac{38}{78}=0.4872")],
     "0.4872", say="P(M or U) = 36/78 + 5/78 − 3/78 = 38/78 = 0.4872.",
     why="Forgetting the overlap gives 41/78 = 0.5256 ✗. Check: 36 males + the 2 unemployed women = 38 people ✓")
card("full-time OR part-time (two rows of the same variable)", "They can't both happen at once (nobody is in two rows), so the overlap is 0: just add.",
     [("Find the numbers", "Row totals 40 and 16. Overlap 0.", None),
      ("Rule", "", r"P(A\text{ or }B)=P(A)+P(B)-0"),
      ("Plug in and compute", "", r"P(\text{FT or PT})=\frac{40}{78}+\frac{16}{78}=\frac{56}{78}=0.7179")],
     "0.7179")
card("female AND not in the labor force", "Both at once → the single cell where the row and the column meet.",
     [("Find the numbers", "Female column, Not-in-labor-force row: 12.", None),
      ("Rule", "", r"P(A\text{ and }B)=\frac{\text{the one cell}}{\text{total}}"),
      ("Plug in and compute", "", r"P(\text{F and NLF})=\frac{12}{78}=0.1538")],
     "0.1538", why="\"and\" never adds anything — it is one cell.")
card("part-time GIVEN female", "You already know she is female, so the world shrinks to the 42 females. Divide by 42, not 78.",
     [("Find the numbers", "Part-time females: 10. All females: 42.", None),
      ("Rule", "", r"P(A\mid B)=\frac{\text{cell}}{\text{total of the given group }B}"),
      ("Plug in and compute", "", r"P(\text{PT}\mid\text{F})=\frac{10}{42}=0.2381")],
     "0.2381", say="P(PT | F) = 10/42 = 0.2381.", why="10/78 = 0.1282 is the classic error. The word after \"given\" tells you the denominator.")
card("female GIVEN part-time", "Other direction: now the given group is the 16 part-timers.",
     [("Find the numbers", "Part-time females: 10. All part-timers: 16.", None),
      ("Rule", "", r"P(\text{F}\mid\text{PT})=\frac{\text{cell}}{\text{part-time total}}"),
      ("Plug in and compute", "", r"P(\text{F}\mid\text{PT})=\frac{10}{16}=0.6250")],
     "0.6250")
card("unemployed GIVEN male", "Given group = the 36 males.",
     [("Find the numbers", "Unemployed males: 3. All males: 36.", None),
      ("Rule and compute", "", r"P(\text{U}\mid\text{M})=\frac{3}{36}=0.0833")],
     "0.0833")
card("are \"part-time\" and \"female\" independent?", "Independent = knowing one does not change the other. Test: is P(PT | F) the same number as P(PT)?",
     [("Compute the conditional", "", r"P(\text{PT}\mid\text{F})=\frac{10}{42}=0.2381"),
      ("Compute the plain probability", "", r"P(\text{PT})=\frac{16}{78}=0.2051"),
      ("Compare", "", r"0.2381\neq 0.2051\ \Rightarrow\ \text{dependent}")],
     "dependent (not independent)", say="P(PT | F) = 0.2381 ≠ P(PT) = 0.2051, so the events are not independent.", why="Equal → independent. Either direction (P(F | PT) vs P(F)) gives the same verdict.")
card("two residents picked WITHOUT replacement: both male", "\"Both\" = AND for two picks → multiply. The second pick has one fewer male and one fewer person.",
     [("First pick", "", r"P(\text{1st male})=\frac{36}{78}"),
      ("Second pick, given the first was male", "35 males left out of 77 people.", r"P(\text{2nd male}\mid\text{1st male})=\frac{35}{77}"),
      ("Multiply", "", r"P(\text{both male})=\frac{36}{78}\cdot\frac{35}{77}=0.2098")],
     "0.2098")
card("two residents picked WITH replacement (or a tiny sample from a huge population): both male", "Independent picks: the same probability twice.",
     [("Rule", "", r"P(\text{both})=P(\text{male})\cdot P(\text{male})"),
      ("Plug in and compute", "", r"P(\text{both male})=\frac{36}{78}\cdot\frac{36}{78}=0.2130")],
     "0.2130")
card("two residents, at least one male", "\"At least one\" = 1 − P(none). None male = both female.",
     [("P(none) = both female (without replacement)", "", r"P(\text{both F})=\frac{42}{78}\cdot\frac{41}{77}=0.2867"),
      ("Subtract from 1", "", r"P(\text{at least one male})=1-0.2867=0.7133")],
     "0.7133", why="Keep full decimals until the end; rounding each fraction first gives 0.7132.")
card("two residents, exactly one male", "Male-then-female OR female-then-male: two orders, add them.",
     [("Order 1: M then F", "", r"\frac{36}{78}\cdot\frac{42}{77}=0.2517"),
      ("Order 2: F then M", "", r"\frac{42}{78}\cdot\frac{36}{77}=0.2517"),
      ("Add", "", r"P(\text{exactly one male})=0.2517+0.2517=0.5035")],
     "0.5035")

# =====================================================================
# Q2
# =====================================================================
SECTION[0] = 'Question 2'
H.append('<h2>Question 2 — is it a valid probability distribution?</h2>')
recipe("The recipe (write both checks every time)", [
    "Rule 1: every P(x) is between 0 and 1 (0 and 1 themselves are allowed).",
    "Rule 2: add all the P(x); the sum must be exactly 1.",
    "Verdict in a sentence: valid, or not valid and WHICH rule fails."])
card("the probabilities add to less than 1 (the practice exam)", "x: 0, 1, 2, 3, 4 with P(x): 0.34, 0.21, 0.13, 0.04, 0.01.",
     [("Rule 1", "Every P(x) is between 0 and 1 ✓", None),
      ("Rule 2: add", "", r"0.34+0.21+0.13+0.04+0.01=0.73"),
      ("Compare with 1", "", r"0.73\neq 1\ \Rightarrow\ \text{rule 2 fails}")],
     "NOT valid — the probabilities add to 0.73, not 1", say="Not a valid distribution: ΣP(x) = 0.73 ≠ 1.")
card("the probabilities add to more than 1", "x: 1–5 with P(x): 0.15, 0.25, 0.30, 0.20, 0.12.",
     [("Rule 1", "All between 0 and 1 ✓", None),
      ("Rule 2: add", "", r"0.15+0.25+0.30+0.20+0.12=1.02"),
      ("Compare with 1", "", r"1.02\neq 1\ \Rightarrow\ \text{rule 2 fails}")],
     "NOT valid — they add to 1.02, not 1")
card("one probability is negative (or above 1)", "x: 1–4 with P(x): 0.5, 0.4, 0.2, −0.1 (notice they add to 1).",
     [("Rule 1", "P(4) = −0.1 is below 0 ✗ — rule 1 fails.", None),
      ("Rule 2: add", "", r"0.5+0.4+0.2+(-0.1)=1\ \text{✓ (passes, but rule 1 already failed)}")],
     "NOT valid — a probability can never be negative", why="A sum of 1 does not rescue a negative entry (and an entry like 1.3 fails rule 1 the same way).")
card("everything checks out", "x: 1–4 with P(x): 0.2, 0.4, 0.3, 0.1.",
     [("Rule 1", "All between 0 and 1 ✓", None),
      ("Rule 2: add", "", r"0.2+0.4+0.3+0.1=1\ \text{✓}")],
     "valid — each P(x) is between 0 and 1 and they add to 1", say="Valid: 0 ≤ P(x) ≤ 1 for every x and ΣP(x) = 1.")
card("find the missing probability", "x: 0–4 with P(x): 0.34, 0.21, 0.13, 0.04, ? — the blank must make the total exactly 1.",
     [("Add the known ones", "", r"0.34+0.21+0.13+0.04=0.72"),
      ("Subtract from 1", "", r"P(4)=1-0.72=0.28"),
      ("Check rule 1", "0.28 is between 0 and 1 ✓", None)],
     "0.28")

# =====================================================================
# Q3
# =====================================================================
FREQ = {4: 20, 5: 20, 6: 26, 7: 17}; N3 = 83
P3 = {x: round(f / N3, 4) for x, f in FREQ.items()}
mu3 = round(sum(x * P3[x] for x in P3), 2)                       # 5.48
var_terms = {x: round((x - mu3) ** 2 * P3[x], 4) for x in P3}
var3 = round(sum(var_terms.values()), 4); sd3 = round(math.sqrt(var3), 2)
SECTION[0] = 'Question 3'
H.append('<h2>Question 3 — discrete probability distribution (Stanley Cup games)</h2>')
H.append(f'<div class="setup">x = number of games in the series: 4, 5, 6, 7 happened 20, 20, 26, 17 times (total 83).<br>P(x) = frequency ÷ 83: P(4) = {P3[4]:.4f}, P(5) = {P3[5]:.4f}, P(6) = {P3[6]:.4f}, P(7) = {P3[7]:.4f}. μ = {mu3}, σ² = {var3}, σ = {sd3}.</div>')
recipe("The recipe for every probability here", [
    "Words → the list of x values. <b>at least / at most / \"or more\" / \"or less\"</b> keep the number IN; <b>more than / fewer than</b> leave it OUT.",
    "Write P(x) = frequency ÷ 83 for each x on the list.",
    "Add them (or, if the list is most of the table, 1 − the leftovers). 4 decimals, box it."])
BAR = lambda inc: fig(discrete_hl([4, 5, 6, 7], [P3[x] for x in [4, 5, 6, 7]], inc), "red bars = the ones you add")
card("build the probability distribution (part a)", "Each probability = how often it happened ÷ total.",
     [("Rule", "", r"P(x)=\frac{\text{frequency}}{\text{total}}=\frac{\text{frequency}}{83}"),
      ("Each x", "", [r"P(4)=\frac{20}{83}=0.2410\qquad P(5)=\frac{20}{83}=0.2410", r"P(6)=\frac{26}{83}=0.3133\qquad P(7)=\frac{17}{83}=0.2048"]),
      ("Check", "", r"0.2410+0.2410+0.3133+0.2048=1.0001\approx 1\ \text{(rounding)}")],
     "the table of x and P(x) above", gfx=BAR([4, 5, 6, 7]))
card("the graph (part b)", "x across, P(x) up, one bar above each x with height P(x); label both axes. The tallest bar is the mode.",
     [("Draw", "Axis x: 4, 5, 6, 7. Axis P(x): 0 to 0.35. Bars of height 0.2410, 0.2410, 0.3133, 0.2048.", None)],
     "a bar for each x, labels on both axes", gfx=BAR([4, 5, 6, 7]))
def q3(phrase, ask, xs, why=None):
    inc = sorted(xs)
    terms = "+".join(f"{P3[x]:.4f}" for x in inc)
    total = round(sum(P3[x] for x in inc), 4)
    steps = [("Words → list", f"The x values that fit: <b>{', '.join(map(str, inc))}</b>." + ('<div class="dots">x = ' + " ".join((f"<b>{k}</b>" if k in inc else str(k)) for k in [4, 5, 6, 7]) + '</div>'), None),
             ("Write each P(x)", "", r"\qquad ".join(rf"P({x})=\frac{{{FREQ[x]}}}{{83}}={P3[x]:.4f}" for x in inc))]
    if len(inc) > 1:
        steps.append(("Add", "", rf"P={terms}={total:.4f}"))
    if len(inc) == 3:
        other = [x for x in [4, 5, 6, 7] if x not in inc][0]
        steps.append(("Shortcut (same answer)", f"The list is everything except {other}:", rf"P=1-P({other})=1-{P3[other]:.4f}={round(1-P3[other],4):.4f}"))
    card(phrase, ask, steps, f"{total:.4f}", why=why, gfx=BAR(inc))
q3("exactly 6", "Just one value.", [6])
q3("at least 6 (6 or more)", "6 is IN → 6 and 7.", [6, 7])
q3("more than 6 (over 6)", "6 is OUT → only 7.", [7])
q3("fewer than 6 (under 6, less than 6)", "6 is OUT → 4 and 5.", [4, 5])
q3("at most 5 (5 or fewer, no more than 5)", "5 is IN → 4 and 5 (same list as \"fewer than 6\").", [4, 5])
q3("at most 6 (= fewer than 7 = not 7)", "6 is IN → 4, 5, 6.", [4, 5, 6])
q3("at least 5 (= more than 4 = not 4)", "5 is IN → 5, 6, 7.", [5, 6, 7])
q3("between 5 and 6 inclusive", "Both ends count → 5 and 6.", [5, 6])
q3("between 4 and 7 NOT inclusive (strictly between)", "Ends are out → 5 and 6.", [5, 6])
q3("5 or 7", "Two separate values → add them.", [5, 7])
card("mean / expected value E(X) (part c)", "Weighted average: each x times its probability, then add.",
     [("Rule", "", r"\mu=E(X)=\sum x\cdot P(x)"),
      ("Plug in", "", r"\mu=4(0.2410)+5(0.2410)+6(0.3133)+7(0.2048)"),
      ("Multiply each", "", r"=0.9640+1.2050+1.8798+1.4336"),
      ("Add", "", rf"\mu={mu3}")],
     f"μ = E(X) = {mu3} games", say="Over many series, the average length is about 5.48 games.")
card("variance and standard deviation (part d)", "Subtract the mean, square, multiply by P(x), add (= variance), take √ (= SD).",
     [("Rule", "", r"\sigma^2=\sum (x-\mu)^2\cdot P(x)\qquad \sigma=\sqrt{\sigma^2}"),
      ("Each term (μ = 5.48)", "", [r"(4-5.48)^2(0.2410)=(-1.48)^2(0.2410)=2.1904(0.2410)=0.5279",
                                   r"(5-5.48)^2(0.2410)=(-0.48)^2(0.2410)=0.2304(0.2410)=0.0555",
                                   r"(6-5.48)^2(0.3133)=(0.52)^2(0.3133)=0.2704(0.3133)=0.0847",
                                   r"(7-5.48)^2(0.2048)=(1.52)^2(0.2048)=2.3104(0.2048)=0.4732"]),
      ("Add → variance", "", rf"\sigma^2=0.5279+0.0555+0.0847+0.4732={var3}"),
      ("Square root → SD", "", rf"\sigma=\sqrt{{{var3}}}={sd3}")],
     f"σ² = {var3}, σ = {sd3} games", why="If the question says variance, stop before the √. No ÷ 4 and no ÷ 83 here — the P(x) do the averaging.")
card("most likely number of games (the mode)", "The x with the biggest P(x).",
     [("Compare the P(x)", "0.2410, 0.2410, 0.3133, 0.2048 → the biggest is 0.3133 at x = 6.", None)],
     "6 games", gfx=BAR([6]))
card("is a 7-game series unusual?", "Two accepted tests: probability below 0.05, or x outside μ ± 2σ.",
     [("Probability test", "", r"P(7)=0.2048\ \text{ is not below }0.05"),
      ("Range test", "", rf"\mu\pm 2\sigma={mu3}\pm 2({sd3})={round(mu3-2*sd3,2)}\ \text{{to}}\ {round(mu3+2*sd3,2)}"),
      ("Decide", "7 is inside 3.34 to 7.62 and 0.2048 ≥ 0.05.", None)],
     "not unusual", say="P(7) = 0.2048 > 0.05, so a 7-game series is not unusual.")

# =====================================================================
# Q4
# =====================================================================
n4, p4 = 10, 0.6
q4v = 1 - p4
def bterm(k, n=n4, p=p4):
    q = 1 - p; c = comb(n, k); pk = p ** k; qk = q ** (n - k); val = c * pk * qk
    m = min(k, n - k)
    if m == 0:
        cexp = r"\frac{%d!}{%d!\,%d!}=1" % (n, k, n - k)
    else:
        num = r"\cdot ".join(str(n - i) for i in range(m)); den = r"\cdot ".join(str(m - i) for i in range(m))
        cexp = r"\frac{%d!}{%d!\,%d!}=\frac{%s}{%s}=%d" % (n, k, n - k, num, den, c)
    assert round(c * float(fx(pk)) * float(fx(qk)), 4) == round(val, 4)
    tex = (r"\begin{aligned}"
           + r"P(%d)&={}_{%d}C_{%d}\,(%s)^{%d}\,(%s)^{%d}\\" % (k, n, k, fx(p), k, fx(q), n - k)
           + r"{}_{%d}C_{%d}&=%s\\" % (n, k, cexp)
           + r"(%s)^{%d}&=%s\qquad (%s)^{%d}=%s\\" % (fx(p), k, fx(pk), fx(q), n - k, fx(qk))
           + r"P(%d)&=%d\times %s\times %s=%s" % (k, c, fx(pk), fx(qk), f4(val))
           + r"\end{aligned}")
    return tex, round(val, 4)
P4 = {k: bterm(k)[1] for k in range(11)}
SECTION[0] = 'Question 4'
H.append('<h2>Question 4 — binomial (60% of women say yes; a sample of 10)</h2>')
H.append('<div class="setup">n = 10 trials (the 10 women), p = 0.60 (a "yes"), 1 − p = 0.40. X = how many of the 10 say yes. '
         'Formula: P(x) = ₙCₓ · pˣ · (1 − p)ⁿ⁻ˣ.<br>All eleven values, for checking: ' + ", ".join(f"P({k}) = {P4[k]:.4f}" for k in range(11)) + '.</div>')
recipe("The recipe for every binomial probability (do these 5 steps every time)", [
    "<b>Words → list of x.</b> at most / at least / \"or fewer\" / \"or more\" keep the number IN; fewer than / more than leave it OUT; exactly = one value; at least one = 1 − P(0).",
    "<b>Short list (1–4 values) → compute each and add. Long list → compute the OTHER side and do 1 − (that).</b>",
    "<b>Each P(x) with the formula:</b> ₙCₓ = n! ÷ (x!(n − x)!) → pˣ → (1 − p)ⁿ⁻ˣ → multiply the three.",
    "<b>Add</b> the terms; if you used the other side, <b>subtract from 1</b>.",
    "4 decimals, box it, write the sentence."])
def dots(inc):
    return '<div class="dots">x = ' + " ".join((f"<b>{k}</b>" if k in inc else str(k)) for k in range(11)) + '</div>'
def q4(phrase, ask, inc, why=None, say=None, sym=None):
    inc = sorted(inc)
    sym = sym or ("P(X=%d)" % inc[0] if len(inc) == 1 else r"P(\text{asked})")
    long = len(inc) > 4
    direct = [k for k in range(11) if k not in inc] if long else inc
    steps = [("Words → list", f"{ask} The x values that fit: <b>{', '.join(map(str, inc))}</b>." + dots(inc), None)]
    if long:
        steps.append(("Short or long?", f"{len(inc)} values is a long list. Compute the other side (x = {', '.join(map(str, direct))}) and subtract from 1.", None))
    else:
        steps.append(("Short or long?", (f"{len(inc)} values — short list: compute each one and add." if len(inc) > 1 else "1 value — just compute it with the formula."), None))
    steps.append(("Set up", "", r"n=10,\quad p=0.6,\quad 1-p=0.4,\qquad P(x)={}_{n}C_{x}\,p^{x}(1-p)^{n-x}"))
    for k in direct:
        steps.append((f"Compute P({k})", "", bterm(k)[0]))
    total = round(sum(P4[k] for k in direct), 4)
    if len(direct) > 1:
        steps.append(("Add", "", r"%s=%s" % ("+".join(f4(P4[k]) for k in direct), f4(total)) if long else r"%s=%s=%s" % (sym, "+".join(f4(P4[k]) for k in direct), f4(total))))
    if long:
        ans = round(1 - total, 4)
        steps.append(("Subtract from 1", "", r"%s=1-%s=%s" % (sym, f4(total), f4(ans))))
    else:
        ans = total
    card(phrase, ask, steps, f4(ans), say=say, why=why)
q4("exactly 3", "One value.", [3], say="P(3) = ₁₀C₃(0.6)³(0.4)⁷ = 0.0425.", why="The power on 0.4 is n − x = 7, not 3. Calculator check: nCr(10,3) × 0.6^3 × 0.4^7.")
q4("fewer than 3 (under 3, less than 3)", "3 is OUT.", [0, 1, 2], sym=r"P(X<3)", say="P(X < 3) = P(0) + P(1) + P(2) = 0.0123.")
q4("at most 3 (3 or fewer, no more than 3, up to 3)", "3 is IN.", [0, 1, 2, 3], sym=r"P(X\le 3)", say="P(X ≤ 3) = P(0) + P(1) + P(2) + P(3) = 0.0548.")
q4("more than 3 (over 3)", "3 is OUT, so the list is 4 through 10.", [4, 5, 6, 7, 8, 9, 10], sym=r"P(X>3)", say="P(X > 3) = 1 − P(X ≤ 3) = 1 − 0.0548 = 0.9452.", why="1 − 0.0123 would be \"at least 3\". Decide IN or OUT first.")
q4("at least 3 (3 or more, no fewer than 3)", "3 is IN, so the list is 3 through 10.", [3, 4, 5, 6, 7, 8, 9, 10], sym=r"P(X\ge 3)", say="P(X ≥ 3) = 1 − P(X ≤ 2) = 1 − 0.0123 = 0.9877.", why="The other side of \"at least 3\" is 0, 1, 2 — it does NOT include 3.")
q4("between 1 and 3 inclusive (from 1 to 3)", "Both ends count.", [1, 2, 3], sym=r"P(1\le X\le 3)")
q4("between 1 and 3 NOT inclusive (strictly between)", "Ends are out.", [2])
q4("at least 1 (at least one says yes)", "1 is IN, so the list is 1 through 10 — the other side is just x = 0.", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], sym=r"P(X\ge 1)", say="P(X ≥ 1) = 1 − P(0) = 1 − 0.0001 = 0.9999.")
q4("none (nobody says yes, zero)", "Just x = 0.", [0])
q4("all 10 say yes", "Just x = 10.", [10])
q4("at most 8 (a long list on the low side)", "8 is IN, so the list is 0 through 8 — the other side is 9 and 10.", [0, 1, 2, 3, 4, 5, 6, 7, 8], sym=r"P(X\le 8)")
q4("more than 8", "8 is OUT → 9 and 10.", [9, 10], sym=r"P(X>8)")
card("expected number (mean) and standard deviation for the sample of 10", "Binomial shortcuts — no table needed.",
     [("Rule", "", r"\mu=np\qquad \sigma=\sqrt{np(1-p)}"),
      ("Plug in", "", r"\mu=10(0.6)=6\qquad \sigma=\sqrt{10(0.6)(0.4)}=\sqrt{2.4}"),
      ("Compute", "", r"\sigma=1.55")],
     "μ = 6, σ = 1.55", say="We expect 6 of the 10 to say yes, give or take about 1.55.")
card("expected number and SD for a sample of 200", "Same shortcuts with n = 200.",
     [("Rule", "", r"\mu=np\qquad \sigma=\sqrt{np(1-p)}"),
      ("Plug in", "", r"\mu=200(0.6)=120\qquad \sigma=\sqrt{200(0.6)(0.4)}=\sqrt{48}"),
      ("Compute", "", r"\sigma=6.93")],
     "μ = 120, σ = 6.93", why="48 is the variance — take the square root for σ.")
card("would 130 of 200 be unusual?", "Usual range = μ ± 2σ (allowed when np(1 − p) ≥ 10).",
     [("Check the condition", "", r"np(1-p)=200(0.6)(0.4)=48\ge 10\ \text{✓}"),
      ("Usual range", "", r"\mu\pm 2\sigma=120\pm 2(6.93)=120\pm 13.86=106.14\ \text{to}\ 133.86"),
      ("Decide", "130 is inside the range.", None)],
     "not unusual", say="130 is inside μ ± 2σ = 106.1 to 133.9, so it is not unusual.")
card("would only 2 of the 10 saying yes be unusual?", "Unusual = the probability of that or something more extreme is below 0.05. \"2 or fewer\" = x = 0, 1, 2.",
     [("Words → list", "2 or fewer → 0, 1, 2." + dots([0, 1, 2]), None),
      ("Add their probabilities (each worked in the \"fewer than 3\" box)", "", r"P(X\le 2)=0.0001+0.0016+0.0106=0.0123"),
      ("Compare with 0.05", "", r"0.0123<0.05")],
     "yes, unusual", say="P(X ≤ 2) = 0.0123 < 0.05, so it would be unusual.")
card("is this a binomial experiment? (why the formula is allowed)", "Four conditions — write all four.",
     [("Fixed number of trials", "n = 10 women.", None),
      ("Each trial has two outcomes", "yes / no.", None),
      ("Same probability every trial", "p = 0.60 for each woman.", None),
      ("Independent trials", "one woman's answer does not change another's (random sample).", None)],
     "yes — all four conditions hold", why="A \"not binomial\" example: drawing cards without replacement from a small deck (p changes each draw).")

# =====================================================================
# Q5
# =====================================================================
a5, b5 = 70, 100
SECTION[0] = 'Question 5'
H.append('<h2>Question 5 — uniform distribution (temperature from 70°F to 100°F)</h2>')
H.append('<div class="setup">a = 70, b = 100, width b − a = 30. The graph is a flat rectangle of height 1/(b − a) = 1/30, so the total area is 30 × 1/30 = 1. Probability of any piece = (length of the piece) ÷ 30. No z-scores anywhere in this question.</div>')
recipe("The recipe for every uniform question", [
    "Write a, b and the width b − a.",
    "Words → the piece: from c to d. \"below 80\" means 70 to 80; \"above 90\" means 90 to 100; anything outside 70–100 is cut off at 70 or 100.",
    "P = (d − c) ÷ (b − a). 4 decimals, box it. (Backwards: x = a + area × (b − a).)"])
UG = lambda shade: fig(uniform_graph(a5, b5, shade=shade), "shaded area = the probability")
card("sketch / describe the pdf and give its height", "A flat line from 70 to 100; zero everywhere else.",
     [("Set up", "", r"a=70,\quad b=100,\quad b-a=30"),
      ("Height", "", r"\text{height}=\frac{1}{b-a}=\frac{1}{100-70}=\frac{1}{30}=0.0333"),
      ("Check the area", "", r"\text{area}=\text{width}\times\text{height}=30\times\frac{1}{30}=1\ \text{✓}")],
     "rectangle from 70 to 100 with height 1/30", say="f(x) = 1/30 for 70 ≤ x ≤ 100, and 0 otherwise.", gfx=UG(None))
def q5(phrase, ask, c, d, why=None, say=None):
    val = round((d - c) / (b5 - a5), 4)
    card(phrase, ask,
         [("Set up", "", r"a=70,\quad b=100,\quad b-a=30"),
          ("Words → piece", f"From <b>{c:g}</b> to <b>{d:g}</b>; its length is {d:g} − {c:g} = {d-c:g}.", None),
          ("Rule", "", r"P(c\le X\le d)=\frac{d-c}{b-a}"),
          ("Plug in and compute", "", rf"P({c:g}\le X\le {d:g})=\frac{{{d:g}-{c:g}}}{{100-70}}=\frac{{{d-c:g}}}{{30}}={val:.4f}")],
         f"{val:.4f}", say=say, why=why, gfx=UG((c, d)))
q5("between 75 and 85", "A piece in the middle.", 75, 85, say="P(75 ≤ X ≤ 85) = (85 − 75)/(100 − 70) = 10/30 = 0.3333.")
q5("below 80 (less than 80, at most 80, cooler than 80)", "From the left end 70 up to 80.", 70, 80, why="P(X ≤ 80) is the identical number — one single point has no width, so P(X = 80) = 0.")
q5("above 90 (more than 90, at least 90, hotter than 90)", "From 90 up to the right end 100.", 90, 100)
q5("at least 95", "From 95 to 100.", 95, 100)
q5("between 60 and 75 (60 is outside the range)", "Only the part inside 70–100 counts, so the piece is 70 to 75.", 70, 75, why="Using 75 − 60 = 15 is wrong: nothing lives below 70.")
card("exactly 80", "A single point has no width, so no area.",
     [("Rule", "", r"P(X=\text{one value})=\frac{80-80}{30}=\frac{0}{30}=0")],
     "0", gfx=UG(None))
card("20% of days are cooler than what temperature?", "Backwards: the area to the LEFT is given (0.20); find the cut x.",
     [("Set up", "", r"a=70,\quad b=100,\quad b-a=30,\quad \text{area to the left}=0.20"),
      ("Rule (area = length ÷ 30, so length = area × 30)", "", r"x=a+(\text{area})(b-a)"),
      ("Plug in and compute", "", r"x=70+0.20(30)=70+6=76"),
      ("Check", "", r"P(X<76)=\frac{76-70}{30}=\frac{6}{30}=0.20\ \text{✓}")],
     "76°F", why="The 20% goes in as 0.20 — no z, no table, no hint.", gfx=UG((70, 76)))
card("the hottest 10% of days start at what temperature?", "Top 10% means 90% are below it → area to the LEFT = 0.90.",
     [("Set up", "", r"\text{area to the left}=1-0.10=0.90"),
      ("Rule", "", r"x=a+(\text{area})(b-a)"),
      ("Plug in and compute", "", r"x=70+0.90(30)=70+27=97"),
      ("Check", "", r"P(X>97)=\frac{100-97}{30}=\frac{3}{30}=0.10\ \text{✓}")],
     "97°F", gfx=UG((97, 100)))
card("the mean and standard deviation of the uniform (if asked)", "Mean = the midpoint. SD = width ÷ √12.",
     [("Rule", "", r"\mu=\frac{a+b}{2}\qquad \sigma=\frac{b-a}{\sqrt{12}}"),
      ("Plug in and compute", "", r"\mu=\frac{70+100}{2}=85\qquad \sigma=\frac{30}{\sqrt{12}}=8.66")],
     "μ = 85, σ = 8.66")

# =====================================================================
# Q6
# =====================================================================
SECTION[0] = 'Question 6'
H.append('<h2>Question 6 — standard normal z (the hints give the area to the LEFT)</h2>')
H.append('<div class="setup">Hints as printed on the exam: left of −1.10 = 0.1357 · left of −0.60 = 0.2743 · left of 0.60 = 0.7257 · left of 1.45 = 0.9265 · (for the N(80, 10) part) left of −1.00 = 0.1587, left of 1.50 = 0.9332.</div>')
recipe("The recipe for every z question", [
    "Words → which area: LEFT of z (below, less than) · RIGHT of z (above, more than) · BETWEEN two z's · OUTSIDE two z's.",
    "Read the hint(s). A hint is ALWAYS the area to the LEFT of that z.",
    "LEFT → the hint itself · RIGHT → 1 − hint · BETWEEN → (left of the bigger z) − (left of the smaller z); bigger = further right, so −0.60 is bigger than −1.10 · OUTSIDE → left tail + right tail.",
    "4 decimals, box it. Backwards (area given, find z): make it a LEFT area, find the closest hint/table entry, read its z."])
ZG = lambda lo=None, hi=None, area=None, unknown=None, outside=False: fig(normal(0, 1, lo, hi, area, unknown, xl="z", outside=outside), "shaded = the area asked for")
card("area to the LEFT of z = −1.10 (below −1.10)", "Exactly what a hint gives.",
     [("Words → area", "\"left of\" → the hint is the answer.", None),
      ("Read the hint", "", r"\text{left of }-1.10=0.1357"),
      ("Rule and answer", "", r"P(Z<-1.10)=0.1357")],
     "0.1357", why="A hint for a negative z is already the left area — do not subtract it from 1.", gfx=ZG(hi=-1.10, area="0.1357"))
card("area to the RIGHT of z = −1.10 (above −1.10)", "Right = 1 − left.",
     [("Words → area", "\"right of\" → 1 − hint.", None),
      ("Read the hint", "", r"\text{left of }-1.10=0.1357"),
      ("Rule and compute", "", r"P(Z>-1.10)=1-0.1357=0.8643")],
     "0.8643", gfx=ZG(lo=-1.10, area="0.8643"))
card("area to the RIGHT of z = 1.45", "Right = 1 − left.",
     [("Words → area", "\"right of\" → 1 − hint.", None),
      ("Read the hint", "", r"\text{left of }1.45=0.9265"),
      ("Rule and compute", "", r"P(Z>1.45)=1-0.9265=0.0735")],
     "0.0735", gfx=ZG(lo=1.45, area="0.0735"))
card("area BETWEEN z = −0.60 and z = 1.45", "Bigger left area minus smaller left area.",
     [("Words → area", "\"between\" → (left of the bigger z) − (left of the smaller z). Bigger z = 1.45, smaller z = −0.60.", None),
      ("Read both hints", "", r"\text{left of }1.45=0.9265\qquad \text{left of }-0.60=0.2743"),
      ("Rule and compute", "", r"P(-0.60<Z<1.45)=0.9265-0.2743=0.6522")],
     "0.6522", why="Subtract the areas, never the z-values.", gfx=ZG(lo=-0.60, hi=1.45, area="0.6522"))
card("between z = −1.10 and z = −0.60 (both negative)", "Same rule; the bigger z is −0.60 (further right).",
     [("Read both hints", "", r"\text{left of }-0.60=0.2743\qquad \text{left of }-1.10=0.1357"),
      ("Rule and compute", "", r"P(-1.10<Z<-0.60)=0.2743-0.1357=0.1386")],
     "0.1386", gfx=ZG(lo=-1.10, hi=-0.60, area="0.1386"))
card("between z = 0.60 and z = 1.45 (both positive)", "Same rule.",
     [("Read both hints", "", r"\text{left of }1.45=0.9265\qquad \text{left of }0.60=0.7257"),
      ("Rule and compute", "", r"P(0.60<Z<1.45)=0.9265-0.7257=0.2008")],
     "0.2008", gfx=ZG(lo=0.60, hi=1.45, area="0.2008"))
card("OUTSIDE z = −1.10 and z = 1.45 (less than −1.10 OR more than 1.45; the two tails)", "Left tail + right tail.",
     [("Left tail", "", r"P(Z<-1.10)=0.1357"),
      ("Right tail", "", r"P(Z>1.45)=1-0.9265=0.0735"),
      ("Add", "", r"P(\text{outside})=0.1357+0.0735=0.2092"),
      ("Same answer the other way", "", r"1-P(\text{between})=1-(0.9265-0.1357)=1-0.7908=0.2092")],
     "0.2092", gfx=ZG(lo=-1.10, hi=1.45, area=("0.1357", "0.0735"), outside=True))
card("find the z with area 0.10 to its LEFT (the 10th percentile of z)", "Backwards: the area is given; find the hint/table entry closest to 0.10 and read its z.",
     [("Words → left area", "", r"\text{area to the left}=0.10"),
      ("Find the closest entry", "0.1003 is the closest (0.0985 is further).", r"0.1003\ \to\ z=-1.28")],
     "z = −1.28", why="Left area below 0.5 → z is negative.", gfx=ZG(hi=-1.28, area="0.10", unknown="z = ?"))
card("find the z with area 0.025 to its RIGHT", "Convert to a LEFT area first.",
     [("Words → left area", "", r"\text{area to the left}=1-0.025=0.975"),
      ("Find the entry", "", r"0.9750\ \to\ z=1.96")],
     "z = 1.96", gfx=ZG(lo=1.96, area="0.025", unknown="z = ?"))
card("the two z's that cut off the middle 90%", "0.05 left over in each tail.",
     [("Words → left areas", "", r"\text{tails}=\frac{1-0.90}{2}=0.05\ \text{each}\quad\Rightarrow\quad \text{left areas }0.05\text{ and }0.95"),
      ("Find the entries", "0.95 sits exactly halfway between 0.9495 (z = 1.64) and 0.9505 (z = 1.65) → average 1.645; symmetry gives the other.", r"z=-1.645\ \text{and}\ z=1.645")],
     "z = ±1.645", gfx=ZG(lo=-1.645, hi=1.645, area="0.90"))
XG = lambda lo=None, hi=None, area=None, unknown=None: fig(normal(80, 10, lo, hi, area, unknown), "x scale; z underneath")
card("X ~ N(μ = 80, σ = 10): P(70 < X < 95)", "Not standard: convert each x to z first, then BETWEEN.",
     [("Words → area", "\"between\" → bigger left − smaller left.", None),
      ("z for each end", "", r"z_1=\frac{x-\mu}{\sigma}=\frac{70-80}{10}=-1.00\qquad z_2=\frac{95-80}{10}=1.50"),
      ("Read the hints", "", r"\text{left of }-1.00=0.1587\qquad \text{left of }1.50=0.9332"),
      ("Rule and compute", "", r"P(70<X<95)=0.9332-0.1587=0.7745")],
     "0.7745", gfx=XG(lo=70, hi=95, area="0.7745"))
card("X ~ N(80, 10): P(X > 95)", "Convert, then RIGHT = 1 − left.",
     [("z", "", r"z=\frac{95-80}{10}=1.50"),
      ("Read the hint", "", r"\text{left of }1.50=0.9332"),
      ("Rule and compute", "", r"P(X>95)=1-0.9332=0.0668")],
     "0.0668", gfx=XG(lo=95, area="0.0668"))
card("X ~ N(80, 10): P(X ≤ 70)", "Convert, then LEFT = the hint.",
     [("z", "", r"z=\frac{70-80}{10}=-1.00"),
      ("Read the hint", "", r"\text{left of }-1.00=0.1587"),
      ("Rule and answer", "", r"P(X\le 70)=0.1587")],
     "0.1587", gfx=XG(hi=70, area="0.1587"))

# =====================================================================
# Q7
# =====================================================================
mu7, sd7 = 100, 15
SECTION[0] = 'Question 7'
H.append('<h2>Question 7 — normal distribution in context (IQ scores: μ = 100, σ = 15)</h2>')
H.append('<div class="setup">Forward (x given, area wanted): z = (x − μ)/σ to 2 decimals → the hint gives the area to the LEFT → left / 1 − left / subtract.<br>Backward (percent given, x wanted): percent → area to the LEFT → the hint\'s z → x = μ + zσ.</div>')
recipe("The recipe for every normal word problem", [
    "Words → which area (below / above / between / outside), or backwards (a percent or percentile is given → find x).",
    "Forward: z = (x − μ)/σ for each x, 2 decimals. Read the hint = area to the LEFT.",
    "below → the hint · above → 1 − hint · between → bigger left − smaller left · outside → left tail + right tail. 4 decimals.",
    "Backward: turn the percent into a LEFT area → the hint's z → x = μ + zσ (1 decimal).",
    "Write the sentence in context (\"…% of children score…\")."])
NG = lambda lo=None, hi=None, area=None, unknown=None, outside=False: fig(normal(mu7, sd7, lo, hi, area, unknown, outside=outside), "IQ scale; z underneath")
card("above 125 (more than 125, at least 125, higher than 125)", "Right tail.",
     [("Words → area", "\"above\" → 1 − (left of z).", None),
      ("z-score", "", r"z=\frac{x-\mu}{\sigma}=\frac{125-100}{15}=\frac{25}{15}=1.67"),
      ("Read the hint", "", r"\text{left of }1.67=0.9525"),
      ("Rule and compute", "", r"P(X>125)=1-0.9525=0.0475")],
     "0.0475", say="About 4.75% of children have an IQ above 125.", why="0.9525 is the number-one wrong answer. Fewer than half score above 125, so the answer must be below 0.5.", gfx=NG(lo=125, area="0.0475"))
card("below 90 (less than 90, at most 90, under 90)", "Left area = the hint.",
     [("Words → area", "\"below\" → the hint itself.", None),
      ("z-score", "", r"z=\frac{90-100}{15}=\frac{-10}{15}=-0.67"),
      ("Read the hint", "", r"\text{left of }-0.67=0.2514"),
      ("Rule and answer", "", r"P(X<90)=0.2514")],
     "0.2514", say="About 25.14% of children have an IQ below 90.", gfx=NG(hi=90, area="0.2514"))
card("between 110 and 140", "Two z's, two left areas, bigger minus smaller.",
     [("Words → area", "\"between\" → (left of bigger z) − (left of smaller z).", None),
      ("z for each end", "", r"z_1=\frac{110-100}{15}=0.67\qquad z_2=\frac{140-100}{15}=2.67"),
      ("Read the hints", "", r"\text{left of }0.67=0.7486\qquad \text{left of }2.67=0.9962"),
      ("Rule and compute", "", r"P(110<X<140)=0.9962-0.7486=0.2476")],
     "0.2476", say="About 24.76% of children score between 110 and 140.", gfx=NG(lo=110, hi=140, area="0.2476"))
card("outside 70 to 130 (below 70 OR above 130)", "Two tails: left tail + right tail.",
     [("z for each end", "", r"z_1=\frac{70-100}{15}=-2.00\qquad z_2=\frac{130-100}{15}=2.00"),
      ("Read the hints", "", r"\text{left of }-2.00=0.0228\qquad \text{left of }2.00=0.9772"),
      ("Left tail + right tail", "", r"P=0.0228+(1-0.9772)=0.0228+0.0228=0.0456")],
     "0.0456", gfx=NG(lo=70, hi=130, area=("0.0228", "0.0228"), outside=True))
card("exactly 100", "One single value has no area under a curve.",
     [("Rule", "", r"P(X=100)=0")],
     "0", why="Any \"exactly\" with a continuous variable is 0; \"at most 100\" would be 0.5000.", gfx=NG(hi=100, area="no width → 0"))
card("the 98th percentile (98% score below it)", "Backwards: left area 0.98 → the hint gives z → x = μ + zσ.",
     [("Words → left area", "", r"\text{area to the left}=0.98"),
      ("Hint → z", "closest entry 0.9798", r"z=2.05"),
      ("Rule", "", r"x=\mu+z\sigma"),
      ("Plug in and compute", "", r"x=100+2.05(15)=100+30.75=130.75")],
     "130.75 ≈ 131", say="An IQ of about 131 is the 98th percentile.", why="Never put 0.98 into the z formula — it is an area, not a score.", gfx=NG(hi=130.75, area="0.98", unknown="x = ?"))
card("the top 5% cutoff (minimum score to be in the top 5%)", "Top 5% → 95% below it → left area 0.95.",
     [("Words → left area", "", r"\text{area to the left}=1-0.05=0.95"),
      ("Hint → z", "0.95 is halfway between 1.64 and 1.65", r"z=1.645"),
      ("Rule, plug in, compute", "", r"x=100+1.645(15)=100+24.675=124.675\approx 124.7")],
     "124.7", gfx=NG(lo=124.7, area="0.05", unknown="x = ?"))
card("the bottom 10% cutoff (10th percentile)", "Left area 0.10 → z is negative.",
     [("Words → left area", "", r"\text{area to the left}=0.10"),
      ("Hint → z", "closest entry 0.1003", r"z=-1.28"),
      ("Rule, plug in, compute", "", r"x=100+(-1.28)(15)=100-19.2=80.8")],
     "80.8", why="Keep the minus sign: the answer must be below the mean.", gfx=NG(hi=80.8, area="0.10", unknown="x = ?"))
card("the two scores holding the middle 95%", "2.5% in each tail → left areas 0.025 and 0.975.",
     [("Words → left areas", "", r"\text{tails}=\frac{1-0.95}{2}=0.025\quad\Rightarrow\quad 0.025\ \text{and}\ 0.975"),
      ("Hints → z", "", r"z=-1.96\ \text{and}\ z=1.96"),
      ("Rule, plug in, compute", "", r"x=100\pm 1.96(15)=100\pm 29.4\quad\Rightarrow\quad 70.6\ \text{and}\ 129.4")],
     "70.6 to 129.4", gfx=NG(lo=70.6, hi=129.4, area="0.95"))
card("the score with 30% above it (70th percentile)", "30% above → 70% below → left area 0.70.",
     [("Words → left area", "", r"\text{area to the left}=1-0.30=0.70"),
      ("Hint → z", "closest entry 0.6985", r"z=0.52"),
      ("Rule, plug in, compute", "", r"x=100+0.52(15)=100+7.8=107.8")],
     "107.8", gfx=NG(lo=107.8, area="0.30", unknown="x = ?"))
card("is a score of 65 unusual?", "Unusual = probability below 0.05 (or z beyond ±2).",
     [("z-score", "", r"z=\frac{65-100}{15}=\frac{-35}{15}=-2.33"),
      ("Read the hint", "", r"\text{left of }-2.33=0.0099"),
      ("Compare", "", r"0.0099<0.05\ \text{(and }|{-2.33}|>2\text{)}")],
     "yes, unusual", say="P(X ≤ 65) = 0.0099 < 0.05, so a score of 65 is unusual.", gfx=NG(hi=65, area="0.0099"))
card("interpret \"the area above 125 is 0.0475\" (two ways)", "An area under the curve is both a proportion and a probability.",
     [("Proportion", "4.75% of all children score above 125.", None),
      ("Probability", "A randomly selected child has a 0.0475 chance of scoring above 125.", None)],
     "write both sentences")

HTML = (f"<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'><title>STA2023 Exam 2 — every scenario worked</title>"
        f"<link rel='stylesheet' href='{KATEX}/katex.min.css'><script src='{KATEX}/katex.min.js'></script><script src='{KATEX}/contrib/auto-render.min.js'></script><style>{CSS}</style></head><body>"
        + "".join(H) + "<script>renderMathInElement(document.body,{delimiters:[{left:'\\\\[',right:'\\\\]',display:true},{left:'\\\\(',right:'\\\\)',display:false}],throwOnError:false});</script></body></html>")
open(OUT, "w").write(HTML)
json.dump(CARDS, open(BASE + "cards.json", "w"), indent=1, ensure_ascii=False)
print("booklet written, cards:", HTML.count('class="card"'))
