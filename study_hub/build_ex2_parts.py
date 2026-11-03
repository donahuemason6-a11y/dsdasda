import sys, os, math
from math import erf, sqrt, comb
import figs
FS1 = float(sys.argv[1]) if len(sys.argv) > 1 else 6.4
FS2 = float(sys.argv[2]) if len(sys.argv) > 2 else 6.4
KATEX = sys.argv[3] if len(sys.argv) > 3 else "file:///tmp/claude-0/-home-user-dsdasda/bdc32f87-6f2d-5f62-952a-43c9c6f6142d/scratchpad/ex2/katex/node_modules/katex/dist"
OUT = sys.argv[4] if len(sys.argv) > 4 else "/home/user/dsdasda/STA2023_Exam2_CHEAT_SHEET_FINAL.html"
FIG = {k: f() for k, f in figs.ALL.items()}
FIG["discrete"] = FIG["discrete"].replace("Label both axes (x across, P(x) up). Heights = the P(x) values from (a); tallest bar = most likely x.", "bar heights = the P(x) from (a); tallest bar = the mode")
Phi = lambda z: 0.5 * (1 + erf(z / sqrt(2)))
L = lambda z: round(Phi(z), 4)

def esc(t): return t.replace("<", "&lt;").replace(">", "&gt;")
def M(tex): return "\\(" + esc(tex) + "\\)"
def D(tex): return "<div class='dm'>\\(" + esc(tex.replace("\\frac", "\\dfrac")) + "\\)</div>"
def f4(v): return f"{v:.4f}"
def fx(v, nd=10):
    s = f"{v:.{nd}f}".rstrip('0').rstrip('.')
    return s if s else "0"
def part(label, question, body): return f'<div class="part"><span class="lab">{label}</span> <span class="q">{question}</span><br>{body}</div>'
def ans(t): return f'<span class="ans">{t}</span>'
def wd(t): return f'<div class="w">{t}</div>'
def last(tex, a): return f"<div class='dm'>{M(tex.replace(chr(92)+'frac', chr(92)+'dfrac'))} {ans(a)}</div>"
def recipe(items): return '<div class="rec"><b>RECIPE</b><ol>' + "".join(f"<li>{i}</li>" for i in items) + '</ol></div>'
def quote(t): return f'<div class="qb"><span class="q">{t}</span></div>'
def dots(inc, rng): return '<span class="dots">' + " ".join((f"<b>{k}</b>" if k in inc else str(k)) for k in rng) + '</span>'

CSS = """
@page { size: letter; margin: 0.17in; }
* { box-sizing: border-box; }
body { margin:0; font-family: Helvetica, Arial, "Liberation Sans", sans-serif; font-size: __FS1__pt; line-height: 1.05; color:#000; background:#fff; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.side { column-count: 3; column-gap: 6pt; column-rule: 0.5pt solid #999; column-fill: auto; }
.s2 { font-size: __FS2__pt; }
.pb { break-after: page; page-break-after: always; }
h1 { column-span: all; font-size: 1.45em; margin: 0 0 2pt 0; padding-bottom: 1.5pt; border-bottom: 1.2pt solid #000; }
h1 .legend { font-size: 0.6em; font-weight: normal; float: right; margin-top: 2.5pt; }
h2 { font-size: 1.18em; margin: 3.5pt 0 1.5pt 0; padding: 1pt 3pt; background:#000; color:#fff; break-after: avoid; }
ol { margin: 0 0 1pt 0; padding-left: 10pt; } ol li { margin: 0 0 0.4pt 0; }
ul { margin: 0 0 2pt 0; padding-left: 9pt; } li { margin: 0 0 0.6pt 0; }
p { margin: 0 0 2pt 0; }
.q { color:#007a1f; font-weight: bold; } .f { color:#cc0000; font-weight: bold; } .d { color:#0033cc; }
.box { border: 0.9pt solid #cc0000; color:#cc0000; padding: 1.5pt 3pt; margin: 1.5pt 0 2.5pt 0; font-weight: bold; break-inside: avoid; }
.rec { border: 0.9pt solid #cc0000; padding: 0.8pt 2.5pt; margin: 1.2pt 0 2pt 0; break-inside: avoid; } .rec > b { color:#cc0000; } .rec li b { color:#cc0000; }
.qb { border-left: 2.2pt solid #007a1f; padding: 0.5pt 0 0.5pt 3.5pt; margin: 1.5pt 0 1.5pt 0; }
.part { margin: 0 0 2.2pt 0; break-inside: avoid; } .part .lab { font-weight: bold; }
.w { color:#0033cc; } .w b { color:#0033cc; }
.ans { color:#cc0000; font-weight: bold; border: 0.8pt solid #cc0000; padding: 0 2pt; display:inline-block; margin-left: 3pt; }
.watch { color:#cc0000; }
.bb { border-left: 2pt solid #000; padding: 0.5pt 0 0.5pt 3.5pt; margin: 1.5pt 0 2pt 0; break-inside: avoid; }
.fig.xs { width: 58%; } .fig.s46 { width: 46%; } .fig.s70 { width: 70%; } .fig.s90 { width: 90%; }
.dm { margin: 0 0 0 5pt; }
.katex { font-size: 0.93em; white-space: nowrap; }
table { border-collapse: collapse; width:100%; margin: 1.5pt 0 2pt 0; font-size: 0.95em; break-inside: avoid; }
td, th { border: 0.35pt solid #666; padding: 0.4pt 2pt; vertical-align: top; text-align: left; }
th { background:#e8e8e8; }
table.num td, table.num th { text-align: center; padding: 0.3pt 1.5pt; } table.num td.l, table.num th.l { text-align: left; }
.small { font-size: 0.93em; }
.fig { break-inside: avoid; margin: 1pt 0 2pt 0; } .fig svg { width:100%; height:auto; display:block; }
.dots { font-family: "DejaVu Sans Mono", "Liberation Mono", monospace; font-size: 0.95em; white-space: nowrap; } .dots b { color:#cc0000; }
"""
LEG = '<span class="legend"><span class="q">■ GREEN = the question</span> &nbsp; <span class="d">■ BLUE = the words → what to do</span> &nbsp; ■ BLACK = the math &nbsp; <span class="f">■ RED = recipe / answer</span></span>'

# ======================================================= SIDE A
A = []
A.append('<div class="box">HOW TO USE: find the question type → read its RECIPE → find the lettered part whose words match your question → copy its steps with your numbers. Probabilities: 4 decimals (0.4 → 0.4000); μ, σ, x: 2 decimals. Show the formula, box the answer.</div>')

# ---------------- Q1
A.append('<h2>Q1 — TWO-WAY TABLE (or / and / given / not / two picks)</h2>')
A.append(quote('"The table below summarizes the employment status of 78 residents."'))
A.append('<table class="num"><tr><th class="l">Status</th><th>Male</th><th>Female</th><th>Total</th></tr>'
         '<tr><td class="l">Full-time</td><td>22</td><td>18</td><td>40</td></tr><tr><td class="l">Part-time</td><td>6</td><td>10</td><td>16</td></tr>'
         '<tr><td class="l">Unemployed</td><td>3</td><td>2</td><td>5</td></tr><tr><td class="l">Not in labor force</td><td>5</td><td>12</td><td>17</td></tr>'
         '<tr><th class="l">Total</th><th>36</th><th>42</th><th>78</th></tr></table>')
A.append(recipe(["<b>Total every row and column</b> first (if the counts come in words, draw the table).",
                 "<b>is A</b> → A's total ÷ 78 · <b>A or B</b> → add both totals, subtract the overlap cell once · <b>A and B</b> (\"a part-time female\") → the one cell ÷ 78 · <b>A given B</b> (\"of the females\", \"among the males\", \"if female\") → the cell ÷ B's total, not 78 · <b>not A</b> → 1 − P(A).",
                 "Fraction → decimal (4 places) → box it."]))
A.append(part("(a)", "probability a randomly selected resident is male", wd("one category → its total ÷ grand total") + last(r"P(\text{male})=\frac{36}{78}=0.4615", "0.4615")))
A.append(part("(b)", "…is part-time", wd("a row → add its cells, ÷ 78") + last(r"P(\text{part-time})=\frac{6+10}{78}=\frac{16}{78}=0.2051", "0.2051")))
A.append(part("(c)", "…is male OR unemployed", wd("OR → add both totals, subtract the overlap (unemployed males = 3) once") + D(r"P(\text{M or U})=P(\text{M})+P(\text{U})-P(\text{M and U})") + last(r"=\frac{36}{78}+\frac{5}{78}-\frac{3}{78}=\frac{38}{78}=0.4872", "0.4872") + '<div class="watch"><b>Watch out:</b> forgetting the overlap gives 41/78 = 0.5256 ✗ (check: 36 males + 2 unemployed women = 38 people ✓)</div>'))
A.append(part("(d)", "…is female AND not in the labor force", wd("AND → the one cell where the row and column meet, ÷ 78") + last(r"P(\text{F and NLF})=\frac{12}{78}=0.1538", "0.1538")))
A.append(part("(e)", "…is part-time GIVEN the resident is female", wd("GIVEN → divide by the given group (the 42 females), not 78") + last(r"P(\text{PT}\mid\text{F})=\frac{\text{part-time females}}{\text{all females}}=\frac{10}{42}=0.2381", "0.2381") + '<div class="watch"><b>Watch out:</b> 10/78 = 0.1282 is the classic error — the word after "given" is the denominator.</div>'))
A.append(part("(f)", "…is NOT male", wd("NOT → 1 − P(male)") + last(r"P(\text{not male})=1-\frac{36}{78}=\frac{42}{78}=0.5385", "0.5385")))
A.append(part("(g)", "…is full-time OR part-time", wd("two rows of the same variable can't overlap → just add") + last(r"P(\text{FT or PT})=\frac{40}{78}+\frac{16}{78}=\frac{56}{78}=0.7179", "0.7179")))
A.append(part("(h)", "…is female GIVEN part-time · unemployed GIVEN male", wd("the given group is now the 16 part-timers · the 36 males") + last(r"P(\text{F}\mid\text{PT})=\frac{10}{16}=0.6250\qquad P(\text{U}\mid\text{M})=\frac{3}{36}=0.0833", "0.6250 · 0.0833")))
A.append(part("(i)", "…is neither male nor unemployed", wd("NOT (M or U) → 1 − the answer to (c)") + last(r"1-\frac{38}{78}=\frac{40}{78}=0.5128", "0.5128")))
A.append(part("(j)", "are \"part-time\" and \"female\" independent?", wd("independent = knowing one doesn't change the other: compare P(PT | F) with P(PT)") + D(r"P(\text{PT}\mid\text{F})=\frac{10}{42}=0.2381\qquad P(\text{PT})=\frac{16}{78}=0.2051") + last(r"0.2381\neq 0.2051", "not independent (dependent)") + wd("equal → independent. Disjoint (mutually exclusive) = no shared cell: full-time &amp; unemployed → disjoint; male &amp; unemployed share the cell 3 → not disjoint.")))
A.append(part("(k)", "two residents picked without replacement: both male · WITH replacement: both male", wd("AND for two picks → multiply; without replacement the 2nd pick has one fewer male and one fewer person; with replacement it is the same fraction twice") + last(r"\frac{36}{78}\cdot\frac{35}{77}=0.2098\qquad \frac{36}{78}\cdot\frac{36}{78}=0.2130", "0.2098 · 0.2130")))
A.append(part("(l)", "two picks: at least one male · at most one male", wd("at least one → 1 − P(none) = 1 − P(both female) · at most one → 1 − P(both male)") + last(r"1-\frac{42}{78}\cdot\frac{41}{77}=1-0.2867=0.7133\qquad 1-0.2098=0.7902", "0.7133 · 0.7902")))
A.append(part("(m)", "two picks: exactly one male", wd("male-then-female OR female-then-male → add the two orders") + D(r"\frac{36}{78}\cdot\frac{42}{77}+\frac{42}{78}\cdot\frac{36}{77}=\frac{1512}{6006}+\frac{1512}{6006}") + last(r"=\frac{3024}{6006}=0.5035", "0.5035")))

# ---------------- Q2
A.append('<h2>Q2 — VALID PROBABILITY DISTRIBUTION?</h2>')
A.append(quote('"Determine whether the following distribution represents a valid discrete probability distribution. If not, explain why." x: 0, 1, 2, 3, 4 with P(x): 0.34, 0.21, 0.13, 0.04, 0.01'))
A.append(recipe(["<b>Rule 1:</b> every P(x) between 0 and 1 (0 and 1 allowed). <b>Rule 2:</b> the P(x) add to exactly 1 (fractions or percents → decimals first; 0.9999 from rounding counts).", "Write BOTH checks and a sentence: valid, or NOT valid and which rule fails."]))
A.append(part("(a)", "the exam's table", wd("rule 1: 0.34, 0.21, 0.13, 0.04, 0.01 are all between 0 and 1 ✓ · rule 2: add them") + last(r"0.34+0.21+0.13+0.04+0.01=0.73\neq 1", "NOT valid — adds to 0.73, not 1")))
A.append(part("(b)", "if the sum is more than 1 (e.g. 0.15, 0.25, 0.30, 0.20, 0.12)", wd("rule 1 ✓ · rule 2:") + last(r"0.15+0.25+0.30+0.20+0.12=1.02\neq 1", "NOT valid — adds to 1.02")))
A.append(part("(c)", "if one entry is negative (e.g. 0.5, 0.4, 0.2, −0.1)", wd("rule 1 fails: −0.1 &lt; 0, even though the sum is 1") + last(r"0.5+0.4+0.2+(-0.1)=1\ \text{but the last entry }-0.1<0", "NOT valid — a probability can't be negative")))
A.append(part("(d)", "if everything checks out (e.g. 0.2, 0.4, 0.3, 0.1)", wd("rule 1 ✓ · rule 2:") + last(r"0.2+0.4+0.3+0.1=1", "valid — each P(x) is 0–1 and they add to 1")))
A.append(part("(e)", "find the missing probability (0.34, 0.21, 0.13, 0.04, ?)", wd("the blank must make the total exactly 1") + last(r"P(4)=1-(0.34+0.21+0.13+0.04)=1-0.72=0.28", "0.28")))

# ---------------- Q3
FREQ = {4: 20, 5: 20, 6: 26, 7: 17}; N3 = 83
P3 = {x: round(f / N3, 4) for x, f in FREQ.items()}
A.append('<h2>Q3 — DISCRETE DISTRIBUTION (Stanley Cup games)</h2>')
A.append(quote('"The following data represent the number of games played, X, in the Stanley Cup before a champion was determined." x: 4, 5, 6, 7 with frequency 20, 20, 26, 17.'))
A.append(recipe(["<b>P(x) = frequency ÷ total.</b> Mean μ = Σ x·P(x). SD: (x − μ)²·P(x) for each x, add (= variance), √.",
                 "<b>Any probability:</b> words → the list of x. <b>at least / at most / \"or more\" / \"or less\" keep the number IN; more than / fewer than leave it OUT</b> (P(X ≤ 5) = at most 5, P(X ≥ 6) = at least 6, P(X &lt; 6) = fewer than 6, P(X &gt; 6) = more than 6). Then add their P(x)."]))
A.append(part("(a)", "construct the probability distribution", wd("total = 20 + 20 + 26 + 17 = 83; each P(x) = its count ÷ 83") + D(r"P(4)=\frac{20}{83}=0.2410\qquad P(5)=\frac{20}{83}=0.2410") + D(r"P(6)=\frac{26}{83}=0.3133\qquad P(7)=\frac{17}{83}=0.2048") + wd("check: 0.2410 + 0.2410 + 0.3133 + 0.2048 = 1.0001 ≈ 1 (rounding) ✓")))
A.append(part("(b)", "graph the distribution", wd("x across, P(x) up, a bar above each x with height P(x), label both axes (tallest bar = x = 6)") + FIG["discrete"].replace('class="fig"', 'class="fig s46"')))
A.append(part("(c)", "compute and interpret the mean", wd("each x times its P(x), then add") + D(r"\mu=\sum x\cdot P(x)=4(0.2410)+5(0.2410)+6(0.3133)+7(0.2048)") + last(r"=0.9640+1.2050+1.8798+1.4336=5.48", "μ = 5.48 games") + wd("interpret: \"over many series, the average length is about 5.48 games.\"")))
A.append(part("(d)", "compute the standard deviation", wd("subtract μ = 5.48, square, × P(x), add, √") + D(r"(4-5.48)^2(0.2410)=2.1904(0.2410)=0.5279") + D(r"(5-5.48)^2(0.2410)=0.2304(0.2410)=0.0555") + D(r"(6-5.48)^2(0.3133)=0.2704(0.3133)=0.0847") + D(r"(7-5.48)^2(0.2048)=2.3104(0.2048)=0.4732") + D(r"\sigma^2=0.5279+0.0555+0.0847+0.4732=1.1413") + last(r"\sigma=\sqrt{1.1413}=1.07", "σ = 1.07 games") + '<div class="watch"><b>Watch out:</b> if they ask for the variance, stop at 1.1413. No ÷ 4 and no ÷ 83 here.</div>'))
def q3t(xs, sym):
    inc = sorted(xs); tot = round(sum(P3[x] for x in inc), 4)
    return (sym + "=" + "+".join(f4(P3[x]) for x in inc) + "=" + f4(tot)) if len(inc) > 1 else (sym + "=" + f4(tot)), f4(tot)
def q3p2(lab, q1, w1, xs1, s1, q2, w2, xs2, s2):
    t1, v1 = q3t(xs1, s1); t2, v2 = q3t(xs2, s2)
    return part(lab, q1 + " · " + q2, wd(w1 + " → x = " + dots(sorted(xs1), [4, 5, 6, 7]) + " &nbsp;·&nbsp; " + w2 + " → x = " + dots(sorted(xs2), [4, 5, 6, 7])) + last(t1, v1) + last(t2, v2))
A.append(q3p2("(e)", "P(exactly 6)", "one value", [6], "P(6)", "P(at least 6) = 6 or more", "6 is IN", [6, 7], r"P(X\ge 6)"))
A.append(q3p2("(f)", "P(more than 6)", "6 is OUT", [7], "P(X>6)", "P(fewer than 6) = under 6", "6 is OUT", [4, 5], "P(X<6)"))
A.append(q3p2("(g)", "P(at most 5) = 5 or fewer", "5 is IN (same list as fewer than 6)", [4, 5], r"P(X\le 5)", "P(at most 6) = fewer than 7", "6 is IN", [4, 5, 6], r"P(X\le 6)"))
A.append(q3p2("(h)", "P(at least 5) = more than 4", "5 is IN", [5, 6, 7], r"P(X\ge 5)", "P(between 5 and 6 inclusive)", "both ends IN", [5, 6], r"P(5\le X\le 6)"))
A.append(q3p2("(i)", "P(between 4 and 7, NOT inclusive)", "ends OUT", [5, 6], r"P(4<X<7)", "P(5 or 7)", "two values", [5, 7], r"P(5\text{ or }7)"))
A.append(part("(j)", "P(not 4) · P(not 6)", wd("NOT → 1 − that value") + last(r"1-P(4)=1-0.2410=0.7590", "0.7590") + last(r"1-P(6)=1-0.3133=0.6867", "0.6867") + wd("adding the leftovers instead (0.2410 + 0.3133 + 0.2048 = 0.7591) is 0.0001 off only from rounding — both accepted.")))
A.append(part("(k)", "most likely number of games · is 7 games unusual? · in 50 series, how many go 7?", wd("mode = the biggest P(x) = 0.3133 → <b>6 games</b> · unusual: P(7) = 0.2048 is not below 0.05, and μ ± 2σ = 5.48 ± 2(1.07) = 3.34 to 7.62 holds 7 → <b>not unusual</b> · expected count = 50 × 0.2048 = 10.24 ≈ <b>10</b>")))

# ---------------- Q4
def bt(k):
    c = comb(10, k); pk = 0.6 ** k; qk = 0.4 ** (10 - k); val = c * pk * qk
    assert round(c * float(fx(pk)) * float(fx(qk)), 4) == round(val, 4)
    return c, fx(pk), fx(qk), round(val, 4)
P4 = {k: bt(k)[3] for k in range(11)}
def pline(k):
    c, pk, qk, v = bt(k)
    return r"P(%d)={}_{10}C_{%d}(0.6)^{%d}(0.4)^{%d}=%d(%s)(%s)=%s" % (k, k, k, 10 - k, c, pk, qk, f4(v))
A.append('<h2>Q4 — BINOMIAL (60% say yes; sample of 10)</h2>')
A.append(quote('"According to a Gallup poll, 60% of U.S. women 18 years old or older stated that the minimum driving age should be 18. In a random sample of 10 U.S. women 18 years old or older, find the probability that:"'))
A.append(recipe(["<b>Set up:</b> n = sample size = 10, p = the percent as a decimal = 0.6, 1 − p = 0.4, X = number who say yes.",
                 "<b>Words → list of x:</b> at most / at least / \"or fewer\" / \"or more\" keep the number IN; fewer than / more than leave it OUT; exactly = one value; at least one = 1 − P(0); \"3 say NO\" = 7 say yes.",
                 "<b>Short list (1–4 values) → compute each P(x) and add. Long list → compute the OTHER side and do 1 − (that).</b>",
                 "<b>Each P(x):</b> " + M(r"P(x)={}_{n}C_{x}\,p^{x}(1-p)^{n-x},\ {}_{n}C_{x}=\frac{n!}{x!\,(n-x)!}") + " (TI-89: 2nd MATH → Probability → nCr(10,3) = 120). 4 decimals, box it."]))
A.append(part("(a)", "exactly 3 believe the minimum driving age should be 18", wd("one value → the formula once") + D(r"{}_{10}C_{3}=\frac{10!}{3!\,7!}=\frac{10\cdot 9\cdot 8}{3\cdot 2\cdot 1}=120") + D(r"(0.6)^3=0.216\qquad (0.4)^7=0.0016384") + last(pline(3), "0.0425") + '<div class="watch"><b>Watch out:</b> the power on 0.4 is n − x = 7, not 3.</div>'))
A.append(part("(b)", "fewer than 3 believe…", wd("\"fewer than 3\" leaves 3 OUT → x = " + dots([0, 1, 2], range(11)) + " → short list → add the three") + D(r"{}_{10}C_{0}=\frac{10!}{0!\,10!}=1\qquad {}_{10}C_{1}=\frac{10!}{1!\,9!}=10") + D(r"{}_{10}C_{2}=\frac{10!}{2!\,8!}=\frac{10\cdot 9}{2\cdot 1}=45") + D(pline(0)) + D(pline(1)) + D(pline(2)) + last(r"P(X<3)=0.0001+0.0016+0.0106=0.0123", "0.0123")))
A.append(part("(c)", "between 1 and 3 (inclusive) believe…", wd("both ends IN → x = " + dots([1, 2, 3], range(11)) + " → add P(1), P(2) from (b) and P(3) from (a)") + last(r"P(1\le X\le 3)=0.0016+0.0106+0.0425=0.0547", "0.0547")))
A.append(part("(d)", "sample of 200: expected number and standard deviation", wd("binomial shortcuts (no table): μ = np, σ = √(np(1 − p))") + D(r"\mu=np=200(0.6)=120") + last(r"\sigma=\sqrt{np(1-p)}=\sqrt{200(0.6)(0.4)}=\sqrt{48}=6.93", "μ = 120, σ = 6.93") + '<div class="watch"><b>Watch out:</b> 48 is the variance — take the √. For the 10: μ = 10(0.6) = 6, σ = √2.4 = 1.55.</div>'))
A.append(part("(e)", "at most 3 = 3 or fewer = no more than 3", wd("3 is IN → x = " + dots([0, 1, 2, 3], range(11)) + " → add (b)'s three and (a)") + last(r"P(X\le 3)=0.0001+0.0016+0.0106+0.0425=0.0548", "0.0548")))
A.append(part("(f)", "more than 3 = over 3", wd("3 is OUT → x = " + dots(range(4, 11), range(11)) + " → long list → 1 − the other side (x = 0, 1, 2, 3 = part e)") + last(r"P(X>3)=1-P(X\le 3)=1-0.0548=0.9452", "0.9452")))
A.append(part("(g)", "at least 3 = 3 or more", wd("3 is IN → x = " + dots(range(3, 11), range(11)) + " → long list → 1 − the other side (x = 0, 1, 2 = part b)") + last(r"P(X\ge 3)=1-P(X\le 2)=1-0.0123=0.9877", "0.9877") + '<div class="watch"><b>Watch out:</b> \"more than 3\" subtracts 0.0548 (3 goes to the other side); \"at least 3\" subtracts 0.0123.</div>'))
A.append(part("(h)", "between 1 and 3 NOT inclusive", wd("ends OUT → only x = 2") + last(r"P(2)=0.0106", "0.0106")))
A.append(part("(i)", "at least one · none · all 10", wd("at least one → 1 − P(0) · none → P(0) · all → P(10) = (0.6)¹⁰") + D(r"P(X\ge 1)=1-P(0)=1-0.0001=0.9999") + last(r"P(0)=(0.4)^{10}=0.0001\qquad P(10)=(0.6)^{10}=0.0060", "0.9999 · 0.0001 · 0.0060")))
A.append(part("(j)", "at most 8 · more than 8", wd("at most 8: 8 is IN → x = 0 … 8 is long → 1 − P(9) − P(10). more than 8: x = 9, 10 → add") + D(pline(9)) + D(pline(10)) + D(r"P(X>8)=0.0403+0.0060=0.0463") + last(r"P(X\le 8)=1-0.0463=0.9537", "0.0463 · 0.9537")))
A.append(part("(k)", "exactly 6 · at least 8 (middle values)", wd("the other values, same formula: P(4) = 0.1115, P(5) = 0.2007, P(6) = 0.2508, P(7) = 0.2150, P(8) = 0.1209") + last(r"P(6)=0.2508\qquad P(X\ge 8)=0.1209+0.0403+0.0060=0.1672", "0.2508 · 0.1672")))
A.append(part("(l)", "not all say yes · exactly 3 say NO", wd("NOT → 1 − P(10) · 3 \"no\" = 7 \"yes\" → P(7) (same as switching to p = 0.4)") + D(r"P(\text{not all})=1-P(10)=1-0.0060=0.9940") + last(r"{}_{10}C_{3}(0.4)^3(0.6)^7=120(0.064)(0.0279936)=0.2150", "0.9940 · 0.2150")))
A.append(part("(m)", "is 130 of 200 unusual? · would only 2 of 10 be unusual?", wd("count: usual range μ ± 2σ (needs np(1 − p) = 48 ≥ 10 ✓) · probability: \"2 or fewer\" below 0.05?") + D(r"\mu\pm 2\sigma=120\pm 2(6.93)=106.1\ \text{to}\ 133.9\ \text{(130 is inside)}") + last(r"P(X\le 2)=0.0001+0.0016+0.0106=0.0123<0.05", "130 not unusual · 2 of 10 unusual") + wd("(100 of 200 would be below 106.1 → unusual; 9 of 10: P(X ≥ 9) = 0.0463 &lt; 0.05 → unusual)")))
A.append(part("(n)", "explain why this is a binomial experiment", wd("1) fixed n = 10 trials · 2) each trial yes/no · 3) same p = 0.6 each trial · 4) independent (random sample). Not binomial: n not fixed (\"until…\") or no-replacement picks over 5% of the group.")))

# ======================================================= SIDE B
B = []
# ---------------- Q5
B.append('<h2>Q5 — UNIFORM (temperature 70°F to 100°F)</h2>')
B.append(quote('"The daytime temperature X (°F) in a coastal city during summer is uniformly distributed between 70°F and 100°F."'))
B.append(recipe(["<b>Set up:</b> a = smaller end 70, b = bigger end 100, width b − a = 30, height 1/(b − a) = 1/30 (area = 30 × 1/30 = 1).",
                 "<b>Words → the piece from c to d:</b> \"below 80\" = 70 to 80 · \"above 90\" = 90 to 100 · outside 70–100 is cut off at 70 or 100 · one exact value → 0. <b>P = (d − c) ÷ (b − a)</b>, 4 decimals.",
                 "<b>Backwards</b> (a percent is given): x = a + (area to the LEFT)(b − a). No z, no hints in this question."]))
B.append(part("(a)", "sketch / describe the pdf", wd("a flat line from 70 to 100 at height 1/30, zero elsewhere") + last(r"\text{height}=\frac{1}{b-a}=\frac{1}{100-70}=\frac{1}{30}=0.0333\qquad \text{area}=30\times\frac{1}{30}=1", "height 1/30") + FIG["uniform"].replace('class="fig"', 'class="fig s46"')))
def q5p(lab, question, words, c, d):
    v = round((d - c) / 30, 4)
    return part(lab, question, wd(f"{words} → piece from {c:g} to {d:g}") + last(r"P(%g\le X\le %g)=\frac{%g-%g}{100-70}=\frac{%g}{30}=%s" % (c, d, d, c, d - c, f4(v)), f4(v)))
B.append(q5p("(b)", "P(75 ≤ X ≤ 85)", "a middle piece", 75, 85))
B.append(q5p("(c)", "P(X &lt; 80) = below 80 = at most 80", "the left end up to 80", 70, 80))
B.append(q5p("(d)", "P(X &gt; 90) = above 90 = at least 90", "90 up to the right end", 90, 100))
B.append(q5p("(e)", "P(X ≥ 95)", "95 to 100", 95, 100))
B.append(q5p("(f)", "P(60 ≤ X ≤ 75) — 60 is outside the range", "only 70 to 75 exists", 70, 75))
B.append(part("(g)", "P(X = 80) exactly · P(X &lt; 60) · P(50 &lt; X &lt; 110)", wd("one point has no width → 0 · entirely outside → 0 · the whole range → 1") + D(r"P(X=80)=\frac{80-80}{30}=0") + last(r"P(X<60)=0\qquad P(50<X<110)=1", "0 · 0 · 1")))
B.append(part("(h)", "NOT between 75 and 85 · below 75 OR above 95", wd("NOT → 1 − (b) · OR of two pieces → add them") + D(r"1-\frac{10}{30}=0.6667") + last(r"\frac{75-70}{30}+\frac{100-95}{30}=\frac{5}{30}+\frac{5}{30}=0.3333", "0.6667 · 0.3333")))
B.append(part("(i)", "P(X &gt; 90 GIVEN X &gt; 80)", wd("GIVEN → divide by the given piece") + last(r"\frac{P(X>90)}{P(X>80)}=\frac{10/30}{20/30}=\frac{10}{20}=0.5000", "0.5000")))
B.append(part("(j)", "20% of days are cooler than what temperature?", wd("backwards: area to the LEFT = 0.20 → x = a + (area)(b − a)") + last(r"x=70+0.20(30)=70+6=76\qquad\text{check: }\frac{76-70}{30}=0.20\ ✓", "76°F")))
B.append(part("(k)", "the hottest 10% start at what temperature?", wd("top 10% → 90% below it → left area 0.90") + last(r"x=70+0.90(30)=70+27=97\qquad\text{check: }\frac{100-97}{30}=0.10\ ✓", "97°F")))
B.append(part("(l)", "median, quartiles, mean, SD", wd("any percentile: x = 70 + (percent)(30)") + D(r"\text{median}=70+0.5(30)=85\qquad Q_1=70+0.25(30)=77.5") + D(r"Q_3=70+0.75(30)=92.5") + last(r"\mu=\frac{a+b}{2}=85\qquad \sigma=\frac{b-a}{\sqrt{12}}=\frac{30}{\sqrt{12}}=8.66", "85 · 77.5 · 92.5 · 8.66")))

# ---------------- Q6
B.append('<h2>Q6 — STANDARD NORMAL z (the exam\'s hint = the table value = area to the LEFT)</h2>')
B.append(quote('"Use the standard normal table (on the real exam: the printed z hints). Round to four decimal places." Hints: left of −1.10 = 0.1357 · left of −0.60 = 0.2743 · left of 0.60 = 0.7257 · left of 1.45 = 0.9265 · left of −1.00 = 0.1587 · left of 1.50 = 0.9332'))
B.append(recipe(["<b>Words → which area:</b> LEFT of z (below, less than, at most) · RIGHT of z (above, more than, at least, exceeds) · BETWEEN (within) · OUTSIDE (two tails).",
                 "<b>Read the hint:</b> ALWAYS the area to the LEFT of that z, even for a negative z. <b>LEFT → the hint · RIGHT → 1 − hint · BETWEEN → (left of the bigger z) − (left of the smaller z)</b>, bigger = further right (−0.60 is bigger than −1.10) · <b>OUTSIDE → left tail + right tail.</b>",
                 "<b>μ, σ given:</b> first " + M(r"z=\frac{x-\mu}{\sigma}") + " to 2 decimals for each x (variance given → σ = √variance), then the same rules. <b>Backwards</b> (area given): make it a LEFT area → the closest hint/table entry → its z."]))
B.append('<div class="box">READING A PRINTED HINT: "P(Z &lt; 1.67) = 0.9525" or "area to the left of 1.67 is 0.9525" → a LEFT area (below → write it; above → 1 − it) · "P(Z &gt; 1.67) = 0.0475" → already the RIGHT tail (below = 1 − 0.0475) · "P(Z &lt; −1.43) = 0.0764" → already a left area, use as is · "z = 2.05 for the 98th percentile" / "z = 1.28 for the top 10%" → put it in x = μ + zσ (bottom 10% → z = −1.28). Your z not among the hints? Recompute it — a hint exists for every z the exam needs.</div>')
B.append(FIG["bells"].replace('class="fig"', 'class="fig s90"'))
B.append(part("(a)", "area to the left of z = −1.10", wd("LEFT → the hint is the answer (a hint for a negative z is already the left area)") + last(r"P(Z<-1.10)=0.1357", "0.1357")))
B.append(part("(b)", "area between z = −0.60 and z = 1.45", wd("BETWEEN → bigger z is 1.45 (left 0.9265), smaller is −0.60 (left 0.2743)") + last(r"P(-0.60<Z<1.45)=0.9265-0.2743=0.6522", "0.6522") + '<div class="watch"><b>Watch out:</b> subtract the AREAS, never the z\'s; a negative answer means you subtracted the wrong way.</div>'))
B.append(part("(c)", "μ = 80, σ = 10: P(70 &lt; X &lt; 95)", wd("convert each end to z, then BETWEEN") + D(r"z=\frac{70-80}{10}=-1.00\to 0.1587\qquad z=\frac{95-80}{10}=1.50\to 0.9332") + last(r"P(70<X<95)=0.9332-0.1587=0.7745", "0.7745")))
B.append(part("(d)", "right of −1.10 · right of 1.45 · left of 1.45", wd("RIGHT → 1 − hint · LEFT of a positive z → still just the hint") + D(r"P(Z>-1.10)=1-0.1357=0.8643") + D(r"P(Z>1.45)=1-0.9265=0.0735") + last(r"P(Z<1.45)=0.9265", "0.8643 · 0.0735 · 0.9265")))
B.append(part("(e)", "between −1.10 and −0.60 (both negative) · between 0.60 and 1.45 (both positive)", wd("same rule: bigger z's left area minus smaller z's") + last(r"0.2743-0.1357=0.1386\qquad 0.9265-0.7257=0.2008", "0.1386 · 0.2008")))
B.append(part("(f)", "outside −1.10 and 1.45 (less than −1.10 OR more than 1.45)", wd("two tails → left tail + right tail") + last(r"0.1357+(1-0.9265)=0.1357+0.0735=0.2092", "0.2092")))
B.append(part("(g)", "μ = 80, σ = 10: P(X &gt; 95) · P(X ≤ 70)", wd("z = 1.50 → 0.9332 → RIGHT · z = −1.00 → LEFT → the hint") + last(r"P(X>95)=1-0.9332=0.0668\qquad P(X\le 70)=0.1587", "0.0668 · 0.1587")))
B.append(part("(h)", "find z with area 0.10 to its LEFT · with 0.025 to its RIGHT", wd("backwards: LEFT area given → closest entry (0.1003) → z · RIGHT given → left = 1 − 0.025 = 0.975 → z") + last(r"z=-1.28\qquad z=1.96", "−1.28 · 1.96")))
B.append(part("(i)", "the two z's that cut off the middle 90%", wd("0.05 in each tail → left areas 0.05 and 0.95 (0.95 is halfway between 1.64 and 1.65 → 1.645)") + last(r"z=\pm 1.645", "±1.645")))
B.append(part("(j)", "μ = 80, σ = 10: bottom 10% cutoff · top 5% · middle 90%", wd("backwards for x: left area → z → x = μ + zσ") + D(r"80+(-1.28)(10)=67.2\qquad 80+1.645(10)=96.45") + last(r"80\pm 1.645(10)=63.55\ \text{to}\ 96.45", "67.2 · 96.45 · 63.55–96.45")))
B.append(part("(k)", "symmetry · within 1 SD of the mean", wd("P(Z &gt; 1.10) = P(Z &lt; −1.10) = 0.1357 · P(Z &lt; 0) = 0.5000 · left of −z = 1 − (left of z)") + last(r"P(-1<Z<1)=0.8413-0.1587=0.6826", "0.6826 (the 68%)")))

# ---------------- Q7
B.append('<h2>Q7 — NORMAL IN CONTEXT (IQ: μ = 100, σ = 15)</h2>')
B.append(quote('"The Wechsler Intelligence Scale for Children is approximately normally distributed with mean μ = 100 and standard deviation σ = 15."'))
B.append(recipe(["<b>Forward (an x is given):</b> " + M(r"z=\frac{x-\mu}{\sigma}") + " to 2 decimals → the hint = area to the LEFT → below: the hint · above: 1 − hint · between: bigger left − smaller left · outside: both tails added.",
                 "<b>Backward (a percent / percentile is given):</b> turn it into the area to the LEFT (\"top 10%\" → 0.90, \"bottom 5%\" → 0.05, \"k-th percentile\" → k/100, \"middle 95%\" → 0.025 and 0.975) → the hint's z → " + M(r"x=\mu+z\sigma") + " (1 decimal).",
                 "<b>Unusual?</b> tail area &lt; 0.05 or |z| &gt; 2. <b>Sentence:</b> \"__% of children score …\" / \"a random child has a 0.__ chance of …\"."]))
B.append(FIG["back"].replace('class="fig"', 'class="fig s70"'))
B.append(part("(a)", "probability a test taker scores above 125", wd("ABOVE → 1 − (left of z)") + D(r"z=\frac{125-100}{15}=1.67\ \to\ \text{hint: left of }1.67=0.9525") + last(r"P(X>125)=1-0.9525=0.0475", "0.0475") + '<div class="watch"><b>Watch out:</b> 0.9525 is the #1 wrong answer — fewer than half score above 125, so the answer must be below 0.5.</div>'))
B.append(part("(b)", "probability a test taker scores below 90", wd("BELOW → the hint itself") + last(r"z=\frac{90-100}{15}=-0.67\ \to\ P(X<90)=0.2514", "0.2514")))
B.append(part("(c)", "proportion scoring between 110 and 140", wd("BETWEEN → two z's, bigger left − smaller left") + D(r"z=\frac{110-100}{15}=0.67\to 0.7486\qquad z=\frac{140-100}{15}=2.67\to 0.9962") + last(r"P(110<X<140)=0.9962-0.7486=0.2476", "0.2476")))
B.append(part("(d)", "score at the 98th percentile", wd("98% below it → area to the LEFT = 0.98 → hint z = 2.05 → x = μ + zσ") + last(r"x=100+2.05(15)=100+30.75=130.75", "130.75 ≈ 131") + '<div class="watch"><b>Watch out:</b> never put 0.98 into the z formula — it is an area, not a score.</div>'))
B.append(part("(e)", "outside 70 to 130 (below 70 OR above 130)", wd("two tails → add them") + D(r"z=\frac{70-100}{15}=-2.00\to 0.0228\qquad z=\frac{130-100}{15}=2.00\to 0.9772") + last(r"0.0228+(1-0.9772)=0.0456", "0.0456")))
B.append(part("(f)", "exactly 100 · at most 100 · above 100", wd("one value has no area → 0 · z = 0 → left of 0 = 0.5000 either way") + last(r"P(X=100)=0\qquad P(X\le 100)=P(X>100)=0.5000", "0 · 0.5000")))
B.append(part("(g)", "the top 5% cutoff (minimum score for the top 5%)", wd("95% below → left area 0.95 → z = 1.645") + last(r"x=100+1.645(15)=124.675\approx 124.7", "124.7")))
B.append(part("(h)", "the bottom 10% cutoff (10th percentile)", wd("left area 0.10 → z = −1.28 (keep the minus)") + last(r"x=100+(-1.28)(15)=100-19.2=80.8", "80.8")))
B.append(part("(i)", "the two scores holding the middle 95% · quartiles (middle 50%)", wd("2.5% in each tail → left areas 0.025, 0.975 → z = ±1.96 · quartiles: left 0.25, 0.75 → z = ±0.67") + D(r"100\pm 1.96(15)=100\pm 29.4\to 70.6\ \text{and}\ 129.4") + last(r"100\pm 0.67(15)=100\pm 10.05\to 89.95\ \text{and}\ 110.05", "70.6–129.4 · 89.95–110.05")))
B.append(part("(j)", "the score with 30% above it", wd("30% above → 70% below → left area 0.70 → z = 0.52") + last(r"x=100+0.52(15)=100+7.8=107.8", "107.8")))
B.append(part("(k)", "a score of 115 is what percentile? · between 85 and 115", wd("forward then read the left area · within 1 SD: z = ±1.00") + D(r"z=\frac{115-100}{15}=1.00\to \text{left }0.8413\to 84\text{th percentile}") + last(r"P(85<X<115)=0.8413-0.1587=0.6826", "84th · 0.6826")))
B.append(part("(l)", "is a score of 65 unusual? · is 140?", wd("tail area below 0.05 (or |z| &gt; 2) → unusual") + D(r"z=\frac{65-100}{15}=-2.33\to \text{left }0.0099<0.05") + last(r"z=\frac{140-100}{15}=2.67\to 1-0.9962=0.0038<0.05", "both unusual")))
B.append(part("(m)", "NOT between 110 and 140 · above 125 GIVEN above 100 · 3 children, at least one above 125", wd("NOT → 1 − (c) · GIVEN → divide · at least one → 1 − P(none)") + D(r"1-0.2476=0.7524\qquad \frac{0.0475}{0.5000}=0.0950") + last(r"1-(0.9525)^3=1-0.8642=0.1358", "0.7524 · 0.0950 · 0.1358")))
B.append(part("(n)", "interpret \"the area above 125 is 0.0475\" · a z-score", wd("(1) 4.75% of all children score above 125; (2) a randomly selected child has a 0.0475 chance of scoring above 125 · \"z = −2.33\" = 2.33 SDs below the mean · \"131 is the 98th percentile\" = 98% score below 131 · the score 1.5 SDs above the mean = 100 + 1.5(15) = 122.5")))
B.append('<div class="box">Percentile → z: 1st −2.33 · 5th −1.645 · 10th −1.28 · 20th −0.84 · 25th −0.67 · 75th 0.67 · 80th 0.84 · 90th 1.28 · 95th 1.645 · 97.5th 1.96 · 98th 2.05 · 99th 2.33 · middle 80 / 90 / 95 / 99% ↔ ±1.28 / ±1.645 / ±1.96 / ±2.575</div>')

# ---------------- concepts
B.append('<h2>CONCEPTS THEY CAN ASK IN WORDS</h2><ul class="small">'
 '<li><b>Probability</b> = long-run fraction of times something happens; 0 ≤ P ≤ 1; <b>unusual</b> = below 0.05. <b>Classical</b> (equally likely: dice, cards, coins) P = N(E)/N(S), e.g. P(two heads) = 1/4. <b>Empirical</b> (from data) P ≈ frequency ÷ trials. <b>Subjective</b> = educated guess. <b>Disjoint</b> = can\'t both happen (P(E and F) = 0). <b>Independent</b> = one doesn\'t change the other\'s probability. Disjoint is NOT independent.</li>'
 '<li><b>Rules:</b> ' + M(r"P(E^c)=1-P(E)") + ' · at least one = 1 − P(none), e.g. 1 − 0.9986<sup>1000</sup> = 0.7536 · ' + M(r"P(E\text{ or }F)=P(E)+P(F)-P(E\text{ and }F)") + ' · ' + M(r"P(E\text{ and }F)=P(E)\,P(F\mid E)") + ' · ' + M(r"P(F\mid E)=\tfrac{N(E\text{ and }F)}{N(E)}") + '. <b>Counting:</b> choices in sequence → multiply (26·26·26 = 17,576) · permutation (order matters) ' + M(r"{}_{n}P_{r}=\tfrac{n!}{(n-r)!}") + ', ₇P₅ = 2,520 · combination (order doesn\'t) ' + M(r"{}_{n}C_{r}=\tfrac{n!}{r!(n-r)!}") + ', ₄C₂ = 6 · 0! = 1.</li>'
 '<li><b>Discrete</b> = counted (0, 1, 2, …); <b>continuous</b> = measured (time, weight) → probability = area, P(one exact value) = 0. E(X) = Σ x·P(x) = long-run average; insurance: premium $100, pays $10,000 with P = 0.0014 → E = 100(0.9986) − 9900(0.0014) = $86 per policy. <b>Normal:</b> bell, symmetric about μ, mean = median = mode, bends at μ ± σ, area 1; <b>Empirical rule</b> 68 / 95 / 99.7% within 1 / 2 / 3 σ. <b>Is it normal?</b> bell-shaped histogram or a straight normal probability plot → yes. Symbols: μ, σ population; x̄, s sample; σ² variance.</li></ul>')

HTML = ("<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'><title>STA2023 Exam 2 Cheat Sheet — every scenario solved</title>"
 f"<link rel='stylesheet' href='{KATEX}/katex.min.css'><script src='{KATEX}/katex.min.js'></script><script src='{KATEX}/contrib/auto-render.min.js'></script>"
 "<style>" + CSS.replace("__FS1__", str(FS1)).replace("__FS2__", str(FS2)) + "</style></head><body>"
 '<div class="side pb"><h1>STA2023 Exam 2 — SIDE A — Q1 TABLE · Q2 VALID? · Q3 DISCRETE · Q4 BINOMIAL — every scenario solved ' + LEG + '</h1>' + "\n".join(A) + '</div>'
 '<div class="side s2"><h1>STA2023 Exam 2 — SIDE B — Q5 UNIFORM · Q6 z · Q7 NORMAL — every scenario solved ' + LEG + '</h1>' + "\n".join(B) + '</div>'
 "<script>renderMathInElement(document.body,{delimiters:[{left:'\\\\[',right:'\\\\]',display:true},{left:'\\\\(',right:'\\\\)',display:false}],throwOnError:false});</script>"
 + ("<script>var out=[];var cw=((8.5-0.34)*96-2*8)/3;document.querySelectorAll('.katex').forEach(function(e){var w=e.getBoundingClientRect().width;if(w>cw){out.push(Math.round(w)+'px > '+Math.round(cw)+' : '+e.textContent.slice(0,70));}});var pageH=(11-0.34)*96;document.querySelectorAll('.side').forEach(function(sd,i){var h1=sd.querySelector('h1');var hh=h1?h1.getBoundingClientRect().height:0;var cwpx=(8.5-0.34)*96;var colw=(cwpx-2*(6*96/72))/3;var cl=sd.cloneNode(true);cl.style.columnCount='1';cl.style.width=colw+'px';cl.style.position='absolute';cl.style.left='-99999px';cl.querySelector('h1').remove();document.body.appendChild(cl);var ch=(pageH-hh-4);var need=cl.getBoundingClientRect().height/ch;out.push('SIDE'+(i+1)+' needs '+need.toFixed(2)+' columns');var secs=cl.querySelectorAll('h2');secs.forEach(function(h,k){var hh2=h.getBoundingClientRect().top;var nxt=secs[k+1];var bot=nxt?nxt.getBoundingClientRect().top:cl.getBoundingClientRect().bottom;out.push('  '+h.textContent.slice(0,40)+' : '+((bot-hh2)/ch).toFixed(2));});cl.remove();});var p=document.createElement('pre');p.id='dbg';p.textContent=out.length?out.join('\\n'):'NO-OVERFLOW';document.body.appendChild(p);</script>" if os.environ.get('DEBUG') else "")
 + "</body></html>")
open(OUT, "w").write(HTML)
print("written", OUT, len(HTML), "FS", FS1, FS2)
