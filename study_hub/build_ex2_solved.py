import sys, html as H
from math import erf, sqrt
import figs
FS1 = float(sys.argv[1]) if len(sys.argv) > 1 else 7.0   # side A (solved exam)
FS2 = float(sys.argv[2]) if len(sys.argv) > 2 else 7.0   # side B (reference)
KATEX = sys.argv[3] if len(sys.argv) > 3 else "file:///tmp/claude-0/-home-user-dsdasda/bdc32f87-6f2d-5f62-952a-43c9c6f6142d/scratchpad/ex2/katex/node_modules/katex/dist"
OUT = sys.argv[4] if len(sys.argv) > 4 else "/home/user/dsdasda/STA2023_Exam2_SOLVED_SHEET.html"
FIG = {k: f() for k, f in figs.ALL.items()}
Phi = lambda z: 0.5 * (1 + erf(z / sqrt(2)))

def esc(t): return t.replace("<", "&lt;").replace(">", "&gt;")
def M(tex): return "\\(" + esc(tex) + "\\)"            # inline math
def D(tex): return "<div class='dm'>\\(" + esc(tex.replace("\\frac", "\\dfrac")) + "\\)</div>"   # one equation per line, stacked fractions

rows = []
for i in range(31):
    z0 = i / 10
    cells = "".join(f"<td>{Phi(z0 + j/100):.4f}</td>".replace("<td>0.", "<td>") for j in range(10))
    rows.append(f"<tr><th>{z0:.1f}</th>{cells}</tr>")
ZT = ("<table class='zt'><tr><th>z</th>" + "".join(f"<th>.0{j}</th>" for j in range(10)) + "</tr>" + "".join(rows) + "</table>")

CSS = """
@page { size: letter; margin: 0.2in; }
* { box-sizing: border-box; }
body { margin:0; font-family: Helvetica, Arial, "Liberation Sans", sans-serif; font-size: __FS1__pt; line-height: 1.08; color:#000; background:#fff; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.side { column-count: 3; column-gap: 6pt; column-rule: 0.5pt solid #999; column-fill: auto; }
.s2 { font-size: __FS2__pt; }
.pb { break-after: page; page-break-after: always; }
h1 { column-span: all; font-size: 1.45em; margin: 0 0 2pt 0; padding-bottom: 1.5pt; border-bottom: 1.2pt solid #000; }
h1 .legend { font-size: 0.6em; font-weight: normal; float: right; margin-top: 2.5pt; }
h2 { font-size: 1.18em; margin: 4pt 0 1.5pt 0; padding: 1pt 3pt; background:#000; color:#fff; break-after: avoid; }
h3 { font-size: 1.08em; margin: 3pt 0 1pt 0; border-bottom: 0.7pt solid #000; break-after: avoid; }
ul { margin: 0 0 2pt 0; padding-left: 9pt; } li { margin: 0 0 0.6pt 0; }
ol { margin: 0 0 2pt 0; padding-left: 11pt; } ol li { margin: 0 0 0.6pt 0; }
p { margin: 0 0 2pt 0; }
.d { color:#0033cc; }
.f { color:#cc0000; font-weight: bold; }
.e { color:#007a1f; }
.q { color:#007a1f; font-weight: bold; }
.box { border: 0.9pt solid #cc0000; color:#cc0000; padding: 1.5pt 3pt; margin: 1.5pt 0 2.5pt 0; font-weight: bold; break-inside: avoid; }
.ex { border-left: 2pt solid #007a1f; padding: 0.5pt 0 0.5pt 3.5pt; margin: 1.5pt 0 2.5pt 0; color:#007a1f; }
.qb { border-left: 2.2pt solid #007a1f; padding: 1pt 0 1pt 3.5pt; margin: 2pt 0 2pt 0; }
.part { margin: 0.5pt 0 2pt 0; }
.part .lab { font-weight: bold; }
.rule { color:#cc0000; font-weight: bold; }
.ans { color:#cc0000; font-weight: bold; border: 0.8pt solid #cc0000; padding: 0 2pt; display:inline-block; margin-top: 0.5pt; }
.watch { color:#cc0000; }
.sw { color:#0033cc; border-top: 0.5pt dashed #0033cc; margin: 1.5pt 0 2pt 0; padding-top: 1pt; }
.fig.sm { width: 66%; } .fig.md { width: 84%; } .fig.sm2 { width: 77%; } .fig.xs { width: 58%; } .fig.s70 { width: 70%; } .fig.s77 { width: 77%; }
.sw b { color:#0033cc; }
.warn { color:#cc0000; }
.dm { margin: 0 0 0 6pt; }
.katex { font-size: 0.93em; }
.katex-display { margin: 0 !important; text-align: left !important; }
.katex-display > .katex { text-align: left !important; }
table { border-collapse: collapse; width:100%; margin: 1.5pt 0 2.5pt 0; font-size: 0.95em; break-inside: avoid; }
td, th { border: 0.35pt solid #666; padding: 0.6pt 2.2pt; vertical-align: top; text-align: left; }
th { background:#e8e8e8; }
table.num td, table.num th { text-align: center; }
.zt { font-size: 0.74em; table-layout: fixed; } .zt td, .zt th { padding: 0 0.4pt; text-align: right; border: 0.3pt solid #999; overflow: hidden; } .zt th { text-align: center; }
.small { font-size: 0.93em; }
.fig { break-inside: avoid; margin: 1pt 0 2.5pt 0; } .fig svg { width:100%; height:auto; display:block; }
"""

LEG_A = '<span class="legend"><span class="q">■ GREEN = the question</span> &nbsp; <span class="f">■ RED = rule / answer</span> &nbsp; ■ BLACK = the work &nbsp; <span class="d">■ BLUE = if they switch it up</span></span>'
LEG_B = '<span class="legend"><span class="d">■ BLUE = what it means</span> &nbsp; <span class="f">■ RED = formula / rule</span> &nbsp; <span class="e">■ GREEN = example</span> &nbsp; ■ BLACK = steps</span>'

def part(label, question, body):
    return f'<div class="part"><span class="lab">{label}</span> <span class="q">{question}</span><br>{body}</div>'
def ans(t): return f'<span class="ans">{t}</span>'
def watch(t): return f'<div class="watch"><b>Watch out:</b> {t}</div>'
def sw(items): return '<div class="sw"><b>If they switch it up:</b> ' + " &nbsp;·&nbsp; ".join(items) + '</div>'
def rule(t): return f'<div class="rule">{t}</div>'

# ======================= SIDE A: THE PRACTICE EXAM SOLVED =======================
A = []
A.append('<div class="box">Every part: formula → plug in → arithmetic → box it. Probabilities: 4 decimals (0.4 → 0.4000); μ, σ and x values: 2 decimals. No work = no credit.</div>')

# ---- Q1
A.append('<h2>Q1 (6 pts) — Two-way table: or / and / given</h2>')
A.append('<div class="qb"><span class="q">"The table below summarizes the employment status of 78 residents. Answer each question. Show your work."</span></div>')
A.append('''<table class="num"><tr><th>Status</th><th>Males</th><th>Females</th><th class="f">Row total</th></tr>
<tr><td>Full-time</td><td>22</td><td>18</td><td class="f">40</td></tr>
<tr><td>Part-time</td><td>6</td><td>10</td><td class="f">16</td></tr>
<tr><td>Unemployed</td><td>3</td><td>2</td><td class="f">5</td></tr>
<tr><td>Not in labor force</td><td>5</td><td>12</td><td class="f">17</td></tr>
<tr><th>Column total</th><th class="f">36</th><th class="f">42</th><th class="f">78</th></tr></table>''')
A.append('<p><b>First:</b> total each row and column at the table\'s edge (if the counts come in words, draw the table yourself). Every answer is then <span class="rule">a count ÷ the group you are picking from</span>.</p>')
A.append(part("(a)", "probability that a randomly selected resident is male?",
    rule("one category (a row or a column) → its total ÷ grand total (78)") + D(r"P(\text{male})=\frac{36}{78}=0.4615")))
A.append(part("(b)", "…is part-time?",
    rule("same rule: add the row\'s cells, ÷ grand total") + D(r"P(\text{part-time})=\frac{6+10}{78}=\frac{16}{78}=0.2051")))
A.append(part("(c)", "…is male OR unemployed?",
    rule("OR: " + M(r"P(A\text{ or }B)=P(A)+P(B)-P(A\text{ and }B)") + " — adding counts the overlap (male AND unemployed = 3) twice, so take it out once") +
    D(r"P(\text{M or U})=\frac{36}{78}+\frac{5}{78}-\frac{3}{78}=\frac{38}{78}=0.4872") +
    watch("forgetting the overlap gives 41/78 ✗ (check: 36 males + 2 unemployed women = 38 ✓)")))
A.append(part("(d)", "…is female AND not in the labor force (NLF)?",
    rule("AND in a table = the ONE cell where the row and column meet, ÷ grand total") + D(r"P(\text{F and NLF})=\frac{12}{78}=0.1538")))
A.append(part("(e)", "…is part-time GIVEN that the resident is female?",
    rule("GIVEN: " + M(r"P(B\mid A)=\dfrac{\#(A\text{ and }B)}{\#(A)}") + " — the letter after | is the given group (the word after \"given\"): divide by its total, 42, not 78") +
    D(r"P(\text{PT}\mid\text{Female})=\frac{10}{42}=0.2381") +
    watch("10/78 = 0.1282 is the classic error.")))
A.append(sw([
    "<b>NOT male</b> → " + M(r"1-\dfrac{36}{78}=\dfrac{42}{78}=0.5385"),
    "<b>female GIVEN part-time</b> → " + M(r"\dfrac{10}{16}=0.6250") + " (direction matters)",
    "<b>independent?</b> is P(PT | F) = P(PT)? 0.2381 ≠ 0.2051 → dependent (either direction gives the same verdict)",
]))

# ---- Q2
A.append('<h2>Q2 (2 pts) — Valid discrete probability distribution?</h2>')
A.append('<div class="qb"><span class="q">"Determine whether the following distribution represents a valid discrete probability distribution. If not, explain why." x: 0, 1, 2, 3, 4 with P(x): 0.34, 0.21, 0.13, 0.04, 0.01</span></div>')
A.append(rule("Valid only if (1) every " + M(r"0\le P(x)\le 1") + " AND (2) " + M(r"\sum P(x)=1") + ". Write BOTH checks (given decimals must add to exactly 1)."))
A.append('<p>Rule 1: 0.34, 0.21, 0.13, 0.04, 0.01 are all between 0 and 1 ✓ &nbsp; Rule 2: add them:</p>')
A.append(D(r"0.34+0.21+0.13+0.04+0.01=0.73\neq 1\;✗"))
A.append(ans("NOT a valid probability distribution — the probabilities add to 0.73, not 1.") + '<br>')
A.append(sw(["any P(x) below 0 or above 1 → not valid even if the sum is 1", "sum above 1 (e.g. 1.02) → not valid", "<b>\"find the missing probability\"</b> → 1 − (the others): if P(4) were blank, the rest add to 0.34 + 0.21 + 0.13 + 0.04 = 0.72 → P(4) = 1 − 0.72 = 0.28"]))

# ---- Q3
A.append('<h2>Q3 (8 pts) — Stanley Cup: discrete random variable</h2>')
A.append('<div class="qb"><span class="q">"The following data represent the number of games played, X, in the Stanley Cup before a champion was determined." x: 4, 5, 6, 7 with frequency 20, 20, 26, 17.</span></div>')
A.append(part("(a)", "construct the probability distribution",
    rule(M(r"P(x)=\dfrac{\text{frequency}}{\text{total}}") + " (frequency = how many times that x happened) &nbsp; total = 20 + 20 + 26 + 17 = 83") +
    D(r"P(4)=\frac{20}{83}=0.2410\qquad P(5)=\frac{20}{83}=0.2410") + D(r"P(6)=\frac{26}{83}=0.3133\qquad P(7)=\frac{17}{83}=0.2048") +
    'Check: 0.2410 + 0.2410 + 0.3133 + 0.2048 = 1.0001 ≈ 1 ✓ (rounding). '))
A.append(part("(b)", "graph the discrete probability distribution",
    "x across, P(x) up; a bar above each x with height P(x); label both axes. In words: \"bars at 4, 5, 6, 7 with heights 0.2410, 0.2410, 0.3133, 0.2048; tallest at x = 6.\"" + FIG["discrete"].replace('class="fig"','class="fig xs"')))
A.append(part("(c)", "compute and interpret the mean of X",
    rule(M(r"\mu=\sum x\cdot P(x)") + " — a weighted average: each x counts as much as its probability") +
    D(r"\mu=4(0.2410)+5(0.2410)+6(0.3133)+7(0.2048)") + D(r"=0.9640+1.2050+1.8798+1.4336=5.48\text{ games}") +
    ans("μ ≈ 5.48 games") + ' <b>Interpretation (part of the points):</b> over many Stanley Cup series, the average length is about 5.48 games.'))
A.append(part("(d)", "compute the standard deviation of X",
    rule(M(r"\sigma=\sqrt{\sum (x-\mu)^2\cdot P(x)}") + " with μ = 5.48: subtract, square, × P(x), add, √") +
    '''<table class="num"><tr><th>x</th><th>x − μ</th><th>(x − μ)²</th><th>(x − μ)² · P(x)</th></tr>
<tr><td>4</td><td>−1.48</td><td>2.1904</td><td>2.1904(0.2410) = 0.5279</td></tr>
<tr><td>5</td><td>−0.48</td><td>0.2304</td><td>0.2304(0.2410) = 0.0555</td></tr>
<tr><td>6</td><td>0.52</td><td>0.2704</td><td>0.2704(0.3133) = 0.0847</td></tr>
<tr><td>7</td><td>1.52</td><td>2.3104</td><td>2.3104(0.2048) = 0.4732</td></tr></table>''' +
    D(r"\sigma^2=0.5279+0.0555+0.0847+0.4732=1.1413") + D(r"\sigma=\sqrt{1.1413}=1.07\text{ games}") +
    ans("σ ≈ 1.07 games") + watch("don't stop at the variance 1.1413; no ÷ 4 or ÷ 83 — the P(x) do the averaging. Write each product to 4 decimals and add those.")))
A.append(sw(["<b>P(at least 6 games)</b> = P(6) + P(7) = 0.3133 + 0.2048 = 0.5181", "<b>P(fewer than 6)</b> = P(4) + P(5) = 0.4820", "<b>variance</b> = σ² = 1.1413 (stop before the √)", "<b>expected value E(X)</b> = the mean"]))

# ---- Q4
A.append('<h2>Q4 (8 pts) — Driving age: binomial</h2>')
A.append('<div class="qb"><span class="q">"According to a Gallup poll, 60% of U.S. women 18 years old or older stated that the minimum driving age should be 18. In a random sample of 10 U.S. women 18 years old or older, find the probability that:"</span></div>')
A.append('<p><b>Binomial:</b> n = the sample size (10 yes/no trials); p = the percent in the question as a decimal (the thing being counted = \"success\"). <span class="rule">n = 10, p = 0.60, 1 − p = 0.40, X = number who say yes.</span></p>')
A.append(D(r"P(x)={}_{n}C_{x}\;p^{x}\,(1-p)^{\,n-x}\qquad {}_{n}C_{x}=\frac{n!}{x!\,(n-x)!}"))
A.append(part("(a)", "exactly 3 believe the minimum driving age should be 18",
    D(r"{}_{10}C_{3}=\frac{10!}{3!\,7!}=\frac{10\cdot 9\cdot 8}{3\cdot 2\cdot 1}=120") + D(r"P(3)={}_{10}C_{3}\,(0.60)^{3}(0.40)^{7}=120(0.216)(0.0016384)=0.0425") +
    ans("0.0425") + watch("the power on 0.40 is n − x = 7, not 3. ₁₀C₃: 10! = 10·9·8·7!, the 7! cancels → 10·9·8 ÷ (3·2·1), or press the nCr key.")))
A.append(part("(b)", "fewer than 3 believe…",
    rule("\"fewer than 3\" = 0, 1, 2 — the 3 is OUT. Add the three (₁₀C₀ = 1, 0.6⁰ = 1); round each to 4 decimals, then add those.") +
    D(r"P(0)={}_{10}C_{0}(0.6)^{0}(0.4)^{10}=1(1)(0.0001049)=0.0001") +
    D(r"P(1)={}_{10}C_{1}(0.6)^{1}(0.4)^{9}=10(0.6)(0.0002621)=0.0016") +
    D(r"P(2)={}_{10}C_{2}(0.6)^{2}(0.4)^{8}=45(0.36)(0.0006554)=0.0106") +
    D(r"P(X<3)=0.0001+0.0016+0.0106=0.0123") + ans("0.0123")))
A.append(part("(c)", "between 1 and 3 (inclusive) believe…",
    rule("inclusive → x = 1, 2, 3. Reuse (a) and (b) — write \"from part (a)\".") +
    D(r"P(1\le X\le 3)=P(1)+P(2)+P(3)=0.0016+0.0106+0.0425=0.0547") + ans("0.0547")))
A.append(part("(d)", "sample of 200: expected number and standard deviation",
    rule("binomial shortcuts: " + M(r"\mu=np,\qquad \sigma=\sqrt{np(1-p)}")) +
    D(r"\mu=np=200(0.60)=120") + D(r"\sigma=\sqrt{np(1-p)}=\sqrt{200(0.60)(0.40)}=\sqrt{48}=6.93") + ans("μ = 120, σ ≈ 6.93 (48 is the variance — take the √)")))
A.append(sw(["<b>at least 3</b> = 1 − P(X < 3) = 1 − 0.0123 = 0.9877", "<b>at most 3</b> (3 is IN) = P(X < 3) + P(3) = 0.0123 + 0.0425 = 0.0548", "<b>more than 3</b> = 1 − 0.0548 = 0.9452", "<b>at least 1</b> = 1 − P(0) = 1 − (0.4)¹⁰ = 0.9999",
    "<b>\"would 130 of 200 be unusual?\"</b> np(1 − p) = 48 ≥ 10 ✓ so the μ ± 2σ rule applies: 120 ± 2(6.93) = 106.1 to 133.9 → 130 inside → not unusual"]))

# ---- Q5
A.append('<h2>Q5 (5 pts) — Daily temperature: uniform</h2>')
A.append('<div class="qb"><span class="q">"The daytime temperature X (°F) in a coastal city during summer is uniformly distributed between 70°F and 100°F."</span></div>')
A.append(rule("a = smaller end 70, b = bigger end 100, width 30. &nbsp;" + M(r"\text{height}=\dfrac{1}{b-a}\qquad P(c\le X\le d)=\dfrac{d-c}{b-a}") + " = the piece's share of the width. \"more than c\" → (b − c)/(b − a); \"less than d\" → (d − a)/(b − a). No z (that's Q6)."))
A.append(part("(a)", "sketch / describe the pdf (= the probability graph)",
    D(r"\text{height}=\frac{1}{b-a}=\frac{1}{100-70}=\frac{1}{30}\qquad \text{area}=30\cdot\frac{1}{30}=1\;✓") +
    ans("a flat line (rectangle) at height 1/30 from 70 to 100, and 0 everywhere else") + FIG["uniform"].replace('class="fig"','class="fig xs"')))
A.append(part("(b)", "P(75 ≤ X ≤ 85)", D(r"P(75\le X\le 85)=\frac{85-75}{100-70}=\frac{10}{30}=0.3333") + ans("0.3333")))
A.append(part("(c)", "P(X &lt; 80)", D(r"P(X<80)=\frac{80-70}{100-70}=\frac{10}{30}=0.3333") + ans("0.3333") + watch("P(X ≤ 80) is the same number — one point has no width, P(X = 80) = 0.")))
A.append(sw(["<b>P(X > 90)</b> = " + M(r"\dfrac{100-90}{30}=0.3333"), "<b>P(X ≥ 95)</b> = 5/30 = 0.1667", "<b>\"20% of days are cooler than what temperature?\"</b> → the 20% goes in as 0.20: " + M(r"x=a+0.20(b-a)=70+0.20(30)=76^\circ\text{F}") + " (no z)"]))

# ---- Q6
A.append('<h2>Q6 (6 pts) — Standard normal: the exam\'s z hint (= the table entry) is the area to the LEFT</h2>')
A.append('<div class="qb"><span class="q">"Use the standard normal table (on the real exam: the printed z hints). Round final answers to four decimal places."</span></div>')
A.append(rule("No table on this sheet: the exam prints the values as hints. LEFT (below) = the hint · RIGHT (above) = 1 − hint · BETWEEN = (left of the bigger z) − (left of the smaller z); bigger = further right, so −0.25 is bigger than −1.30 · " + M(r"z=\dfrac{x-\mu}{\sigma}") + " to 2 decimals"))
A.append(part("(a)", "area to the left of z = −1.10", "the hint (or table row −1.1, column .00): " + ans("0.1357") + watch("a hint P(Z < −1.10) = 0.1357 is already the left area — use it as is (only with no negative z given: 1 − 0.8643 = 0.1357).")))
A.append(part("(b)", "area between z = −0.60 and z = 1.45", "hints: left of 1.45 = 0.9265; left of −0.60 = 0.2743." + D(r"\text{between}=0.9265-0.2743=0.6522") + ans("0.6522") + watch("subtract the AREAS, never the z's; a negative answer means you subtracted the wrong way.")))
A.append(part("(c)", "μ = 80, σ = 10: P(70 &lt; X &lt; 95)",
    D(r"z_1=\frac{70-80}{10}=-1.00\ \to\ \text{left}=0.1587") + D(r"z_2=\frac{95-80}{10}=1.50\ \to\ \text{left}=0.9332") + D(r"P(70<X<95)=0.9332-0.1587=0.7745") + ans("0.7745")))
A.append(sw(["<b>right of z = 1.45</b> = 1 − 0.9265 = 0.0735", "<b>P(X > 95)</b> = 1 − 0.9332 = 0.0668", "<b>z with area 0.10 to its LEFT</b> → closest entry 0.1003 → z = −1.28", "<b>z with area 0.025 to its RIGHT</b> → left area 0.975 → z = 1.96"]))

# ---- Q7
A.append('<h2>Q7 (8 pts) — Wechsler IQ: normal with μ = 100, σ = 15</h2>')
A.append('<div class="qb"><span class="q">"The Wechsler Intelligence Scale for Children is approximately normally distributed with mean μ = 100 and standard deviation σ = 15."</span></div>')
A.append(rule("Forward (a)–(c): " + M(r"z=\dfrac{x-100}{15}") + " → hint → below: left · above: 1 − left · between: bigger left − smaller left. &nbsp; Backward (d): percent → left area → the hint's z → " + M(r"x=\mu+z\sigma") + " (x to 1 decimal; 130.75 ≈ 131 is fine). Unusual: |z| > 2 or tail area < 0.05 — no hint needed."))
A.append(part("(a)", "probability a test taker scores above 125",
    D(r"z=\frac{125-100}{15}=1.67\ \to\ \text{left}=0.9525") + D(r"P(X>125)=1-0.9525=0.0475") + ans("0.0475") + watch("0.9525 is the #1 error; fewer than half score above 125 → the answer must be below 0.5.")))
A.append(part("(b)", "probability a test taker scores below 90",
    D(r"z=\frac{90-100}{15}=-0.67") + D(r"P(X<90)=\text{left of }-0.67=0.2514") + ans("0.2514") + " (keep the minus sign on z)"))
A.append(part("(c)", "proportion scoring between 110 and 140",
    D(r"z_1=\frac{110-100}{15}=0.67\ \to\ \text{left}=0.7486") + D(r"z_2=\frac{140-100}{15}=2.67\ \to\ \text{left}=0.9962") + D(r"P(110<X<140)=0.9962-0.7486=0.2476") + ans("0.2476") + " (proportion = probability; 4 decimals)"))
A.append(part("(d)", "score at the 98th percentile",
    "98th percentile = 98% score below it → area to the LEFT = 0.98 → the exam's hint gives z = 2.05 (from a table: 0.9798 is the entry closest to 0.98)." +
    D(r"x=\mu+z\sigma=100+2.05(15)") + D(r"=100+30.75=130.75\approx 131") + ans("≈ 131 (130.75)") + watch("never put 0.98 into the z formula — it is an area, not a score.")))
A.append(sw(["<b>top 5%</b> → left 0.95 → z = 1.645 (halfway between 1.64 and 1.65) → 100 + 1.645(15) = 124.7", "<b>bottom 10%</b> → left 0.10 → z = −1.28 → 100 − 1.28(15) = 80.8", "<b>middle 95%</b> → 0.025 in each tail → z = ±1.96 → 70.6 to 129.4", "<b>is 70 unusual?</b> z = −2.00 → left area 0.0228 &lt; 0.05 → yes (|z| > 2 also says unusual)"]))


# ======================= SIDE B: REFERENCE =======================
B = []
B.append('<h2>SYMBOLS — what they mean</h2><table>'
 '<tr><th>Symbol</th><th>Plain English</th></tr>'
 '<tr><td>Σ</td><td class="d">"add them all up"</td></tr>'
 '<tr><td>N / n</td><td class="d">how many values (N population, n sample)</td></tr>'
 '<tr><td>μ ("mu") / x̄ ("x-bar")</td><td class="d">the mean (average): μ population, x̄ sample</td></tr>'
 '<tr><td>σ ("sigma") / s</td><td class="d">standard deviation (SD) = typical gap from the mean; σ², s² = variance = SD²</td></tr>'
 '<tr><td>z</td><td class="d">z-score = how many SDs a value sits above (+) or below (−) the mean</td></tr>'
 '<tr><td>P(E), E<sup>c</sup>, N(E)</td><td class="d">probability of event E (0 = impossible … 1 = certain); E<sup>c</sup> = "not E"; N(E) = # of outcomes in E, N(S) = # of all outcomes</td></tr>'
 '<tr><td>P(F | E)</td><td class="d">probability of F <b>given</b> you already know E happened</td></tr>'
 '<tr><td>X / x, P(x)</td><td class="d">X = the random variable (the number an experiment produces); x = one value; P(x) = the chance X comes out equal to x; μ<sub>X</sub>, σ<sub>X</sub> = its mean and SD; E(X) = expected value = μ<sub>X</sub></td></tr>'
 '<tr><td>n, p, 1 − p; <sub>n</sub>C<sub>r</sub>, <sub>n</sub>P<sub>r</sub>, n!</td><td class="d">binomial: # of trials, P(success), P(failure); C = pick r of n, order ignored; P = order counts; n! = n·(n−1)·…·1</td></tr></table>'
 '<div class="box">μ, σ or capital N → whole population; x̄, s or small n → a sample. ≤ / ≥ = at most / at least (the end number counts); ≠ = not equal. Probabilities: 4 decimals (0.4 → 0.4000); μ, σ, x: 2.</div>')

B.append('<h2>WHICH TOOL? — read the question first (★Qn = solved on side A)</h2><table>'
 '<tr><th>Question says…</th><th>Use</th></tr>'
 '<tr><td>table of counts + "or / and / given"</td><td>Ch 4 rules on the two-way table <b>★Q1</b></td></tr>'
 '<tr><td>"how many ways"</td><td>counting: multiply / <sub>n</sub>P<sub>r</sub> / <sub>n</sub>C<sub>r</sub></td></tr>'
 '<tr><td>x with its P(x), or x with its frequency count</td><td>Ch 5: validity check, μ, σ <b>★Q2 ★Q3</b></td></tr>'
 '<tr><td>n trials, probability p, "how many successes"</td><td>binomial; μ = np, σ = √(np(1−p)) <b>★Q4</b></td></tr>'
 '<tr><td>"uniformly distributed between a and b"</td><td>uniform: (d − c)/(b − a), never z <b>★Q5</b></td></tr>'
 '<tr><td>"normally distributed, mean μ, SD σ"</td><td>z → table → left / right / between <b>★Q6 ★Q7</b></td></tr>'
 '<tr><td>"what value is the __th percentile / top 10%"</td><td>backwards: area → z → x = μ + zσ <b>★Q7(d)</b></td></tr></table>')

B.append('<h2>EXAM 1 SKILLS THAT COME BACK</h2><ul class="small">'
 '<li><b>Mean</b> ' + M(r"\mu=\dfrac{\sum x}{N}") + ' <span class="d">(balance point); <b>median</b> = middle of the sorted list; <b>mode</b> = most frequent. <b>SD</b> = typical distance from the mean:</span> ' + M(r"\sigma=\sqrt{\dfrac{\sum (x-\mu)^2}{N}}") + ' <span class="d">(sample s: ÷ (n − 1); calculator σx = population, Sx = sample).</span></li>'
 '<li><b>z-score</b> ' + M(r"z=\dfrac{x-\mu}{\sigma}") + ' <span class="d">= how many SDs above (+) or below (−) the mean; beyond ±2 → unusual.</span> <b>Empirical Rule</b> <span class="d">68–95–99.7 (picture in the normal section).</span> <b>Quartiles:</b> <span class="f">Q₁, Q₃ = the 25th, 75th percentile values; IQR = Q₃ − Q₁; outlier if below Q₁ − 1.5·IQR or above Q₃ + 1.5·IQR</span></li></ul>')

B.append('<h2>CH 4 — PROBABILITY</h2><ul>'
 '<li><b>Probability</b> <span class="d">= the long-run fraction of times something happens (Law of Large Numbers: more trials → the fraction settles at the probability).</span> <span class="f">0 ≤ P(E) ≤ 1; all outcomes together add to 1.</span> <b>Unusual event</b> <span class="d">= probability below 0.05</span>.</li>'
 '<li><b>Sample space S</b> <span class="d">= everything that could happen; an <b>event</b> = any part of it.</span></li>'
 '<li><b>Classical</b> <span class="d">(equally likely outcomes — dice, cards, coins): count.</span> ' + M(r"P(E)=\dfrac{N(E)}{N(S)}") + ' <span class="e">P(two heads) = 1/4; P(at least one tail) = 3/4.</span></li>'
 '<li><b>Empirical</b> <span class="d">(from data):</span> ' + M(r"P(E)\approx\dfrac{\text{frequency of }E}{\text{number of trials}}") + ' <span class="e">22 of 200 carpool → 0.11 (interpret: "if many people were selected, about 11 of every 100 would carpool"); 5 walk → 5/200 = 0.025 &lt; 0.05 → unusual.</span> <b>Subjective</b> <span class="d">= educated guess.</span></li>'
 '<li><b>Disjoint</b> (mutually exclusive) <span class="d">= can\'t both happen (one card: king AND queen), so P(E and F) = 0.</span> <b>Independent</b> <span class="d">= E happening doesn\'t change P(F) (two coin flips).</span> <span class="f">Disjoint is NOT independent:</span> <span class="d">if they are disjoint, knowing E happened means F didn\'t.</span></li></ul>'
 '<h3>The rules — spot the keyword</h3><div class="box">'
 'NOT: ' + M(r"P(E^{c})=1-P(E)") + ' &nbsp;·&nbsp; AT LEAST ONE: ' + M(r"P(\text{at least 1})=1-P(\text{none})") + '<br>'
 'OR: ' + M(r"P(E\text{ or }F)=P(E)+P(F)-P(E\text{ and }F)") + ' &nbsp;(disjoint → the overlap is 0, just add)<br>'
 'AND, independent: ' + M(r"P(E\text{ and }F)=P(E)\cdot P(F)") + ' &nbsp;·&nbsp; AND, always: ' + M(r"P(E\text{ and }F)=P(E)\cdot P(F\mid E)") + '<br>'
 'GIVEN: ' + M(r"P(F\mid E)=\dfrac{P(E\text{ and }F)}{P(E)}=\dfrac{N(E\text{ and }F)}{N(E)}") + ' &nbsp;·&nbsp; Independent? check ' + M(r"P(F\mid E)=P(F)") + ': equal → independent, different → dependent</div>' + FIG["venn"].replace('class="fig"','class="fig sm2"') +
 '<div class="ex"><b>Cards:</b> 52 = 4 suits × 13 ranks (4 per rank, 13 per suit, 12 face cards J/Q/K). P(king or ♦) = 4/52 + 13/52 − 1/52 = 16/52 = <b>0.3077</b>. Two picks, no replacement: P(2 kings) = 4/52 · 3/51 = <b>0.0045</b> (the 1st card stays out, so the 2nd pick is 3 kings of 51 cards).</div>'
 '<ul class="small"><li><span class="d"><b>"At least one":</b> compute the one case you don\'t want (none) and subtract from 1.</span> <span class="e">P(survive) = 0.9986: P(both of 2 survive) = 0.9986² = 0.9972; P(at least one of 1000 dies) = 1 − 0.9986<sup>1000</sup> = 0.7536.</span></li></ul>'
 '<h3>Counting — "how many ways"</h3><ul class="small">'
 '<li><span class="d">A <b>sequence of choices</b>: multiply the options at each step.</span> <span class="e">3-letter codes: 26·26·26 = 17,576; chair, vice-chair, secretary from 14: 14·13·12 = 2,184.</span></li>'
 '<li><span class="d"><b>Permutation</b> = pick r of n, ORDER MATTERS (1st/2nd/3rd).</span> ' + M(r"{}_{n}P_{r}=\dfrac{n!}{(n-r)!}") + ' <span class="e">₇P₅ = 7·6·5·4·3 = 2,520 (r numbers counting down); ₁₀P₃ = 720; 7 in order: 7! = 5,040; note 0! = 1: ₅P₅ = 5! = 120; ₙC₀ = ₙCₙ = 1.</span></li>'
 '<li><span class="d"><b>Combination</b> = pick r of n, order DOESN\'T matter (committee, poker hand, sample).</span> ' + M(r"{}_{n}C_{r}=\dfrac{n!}{r!\,(n-r)!}") + ' <span class="e">₄C₂ = 4!/(2!·2!) = 24/(2·2) = 6; ₂₀C₄ = 4,845. Probability by counting: P(4 cards all the same rank) = 13 ranks ÷ ₅₂C₄ = 13/270,725 ≈ 0.00005.</span></li></ul>')

B.append('<h2>CH 5 — DISCRETE RANDOM VARIABLES ★Q2 ★Q3</h2><ul>'
 '<li><b>Random variable X</b> <span class="d">= the number that comes out of a chance experiment. <b>Discrete</b> = you count it; its possible values are a list (x = 0, 1, 2, …). <b>Continuous</b> = you measure it; its possible values are an interval (time t ≥ 0, mass 0 &lt; m ≤ 16 oz).</span> <b>Probability distribution</b> <span class="d">= every value X can take with its probability.</span></li></ul>'
 '<div class="box">VALID only if (1) every ' + M(r"0\le P(x)\le 1") + ' AND (2) ' + M(r"\sum P(x)=1") + D(r"\mu_X=E(X)=\sum\big[x\cdot P(x)\big]") + D(r"\sigma_X=\sqrt{\sum\big[(x-\mu)^2\cdot P(x)\big]}") + '</div>'
 '<p class="small d"><b>Mean of a distribution</b> = weighted average (each value counts as much as its probability) = the long-run average per trial. <b>SD</b> = typical distance from the mean, each squared gap weighted by its probability.</p>'
 '<div class="ex"><b>Q:</b> "Insurance: premium $100, pays $10,000 if the client dies, P(dies) = 0.0014. Expected profit?" <b>A:</b> build X = profit from the words: lives → +$100, P = 1 − 0.0014 = 0.9986; dies → 100 − 10,000 = −$9,900, P = 0.0014 (sum = 1 ✓). E(X) = 100(0.9986) − 9900(0.0014) = 99.86 − 13.86 = <b>$86</b> per policy (positive → keep selling).</div>')

B.append('<h2>CH 5 (cont.) — BINOMIAL ★Q4</h2>'
 '<p><b>Binomial experiment</b> <span class="d">= the same yes/no trial repeated: (1) FIXED number of trials n, (2) independent, (3) two outcomes (success / failure), (4) SAME p each time. X = number of successes. Not binomial if n isn\'t fixed ("until…") or picks without replacement are more than 5% of the group.</span></p>'
 '<div class="box">' + D(r"P(x)={}_{n}C_{x}\;p^{x}(1-p)^{\,n-x}\qquad {}_{n}C_{x}=\frac{n!}{x!\,(n-x)!}") + D(r"\mu=np\qquad \sigma=\sqrt{np(1-p)}") + 'Unusual count (needs np(1 − p) ≥ 10): below μ − 2σ or above μ + 2σ &nbsp;·&nbsp; Excel: BINOM.DIST(x, n, p, FALSE) = P(x); TRUE = P(X ≤ x)</div>'
 + FIG["binom"].replace('class="fig"','class="fig md"') +
 '<div class="ex"><b>Q:</b> "Binomial or not? (1) Roll a pair of dice 10 times, count sums of 7. (2) Select flights until 10 late ones. (3) Pick 4 of 30 students, count females." <b>A:</b> (1) YES: n = 10, p = 6/36 (6 of the 36 sums are 7), x = 0, 1, …, 10 (x always runs 0 … n). (2) NO: n not fixed. (3) NO: no replacement, and 4 of 30 = 13% &gt; 5% of the group → p changes.</div>')

B.append('<h2>CH 6 — CONTINUOUS &amp; NORMAL</h2><ul>'
 '<li><span class="d">A continuous variable has infinitely many values, so probability = <b>AREA under the curve</b> (pdf = the probability curve: never below 0, total area 1).</span> <span class="f">P(X = one exact value) = 0</span> <span class="d">so P(a &lt; X &lt; b) = P(a ≤ X ≤ b).</span></li></ul>'
 '<h3>Uniform ★Q5</h3><p><b>Uniform from a to b</b> <span class="d">= a flat rectangle: every stretch of the same length is equally likely. Probability of an interval = its share of the total width.</span></p>'
 '<div class="box">' + D(r"\text{height}=\frac{1}{b-a}\qquad P(c\le X\le d)=\frac{d-c}{b-a}") + D(r"\text{value with share }P\text{ below it: } x=a+P\,(b-a)") + '</div>'
 '<h3>Normal ★Q6 ★Q7</h3><p><b>Normal</b> <span class="d">= the bell curve: symmetric around μ, most values near the middle. μ slides it left/right, σ makes it wider or narrower.</span> <span class="small d"><b>Properties:</b> symmetric about μ; mean = median = mode = μ (the peak); bends (inflection points) at μ ± σ; total area 1; tails never touch the axis; Empirical Rule; half the area on each side of μ.</span></p>' + FIG["emp"].replace('class="fig"','class="fig s70"') +
 '<p><b>Standard normal Z:</b> <span class="d">μ = 0, σ = 1. <b>The trick:</b> convert any value to a z-score and use ONE table (or the exam\'s hint): it gives the area to the LEFT of z.</span></p>'
 '<div class="box">' + D(r"z=\frac{x-\mu}{\sigma}\ \ (\text{round to 2 decimals})\qquad x=\mu+z\sigma") + 'LEFT ("less than / below"): table value &nbsp;·&nbsp; RIGHT ("more than / above"): 1 − table value<br>BETWEEN: (left of the bigger z) − (left of the smaller z) &nbsp;·&nbsp; no −z row in the table? left of −z = 1 − (left of +z)</div>' + FIG["bells"].replace('class="fig"','class="fig s77"') +
 '<p><b>Steps:</b> draw the bell, mark μ and x, shade → z = (x − μ)/σ to 2 decimals → hint or table (z = 1.67: row 1.6, column .07) = area to the LEFT → left: done · right: 1 − it · between: big left − small left.</p>'
 '<h3>USING THE z HINTS ON THE EXAM (no table needed)</h3><p class="d">Dr. Amir: every z-score you need is printed as a hint on the exam paper; a hint is a table value, so use it exactly like the table. Still compute your own z = (x − μ)/σ to 2 decimals and match it to a hint — no match means your arithmetic is wrong.</p>'
 '<div class="box">"P(Z &lt; 1.67) = 0.9525" / "area to the left of 1.67 is 0.9525" → the LEFT area: below → write it · above → 1 − it · between → bigger − smaller<br>"P(Z &gt; 1.67) = 0.0475" (a right tail) → that IS the "above" answer; "below" = 1 − 0.0475<br>"z = 2.05 for the 98th percentile" / "z = 1.28 for the top 10%" → x = μ + z·σ; bottom 10% → negative z (z = −1.28 → x = μ − 1.28σ)<br>"P(Z &lt; −1.43) = 0.0764" is already a LEFT area — write it as is &nbsp;·&nbsp; "is it unusual?" has no hint: |z| &gt; 2 (x beyond μ ± 2σ) → unusual</div>'
 '<h3>Backwards — find x from a percent / percentile ★Q7(d)</h3><p class="d">The area is GIVEN; run the steps backwards: words → area to the LEFT ("top 10%" → 0.90, "bottom 5%" → 0.05, "k-th percentile" → k/100, "middle 80%" → 0.10 and 0.90) → find it INSIDE the table (closest entry; 0.95 sits halfway between 1.64 and 1.65 → 1.645; 0.995 → 2.575) → read z from its row + column → x = μ + zσ.</p>'
 + FIG["back"].replace('class="fig"','class="fig s70"') +
 '<div class="box">Percentile → z: 1st −2.33 · 5th −1.645 · 10th −1.28 · 20th −0.84 · 25th −0.67 · 75th 0.67 · 80th 0.84 · 90th 1.28 · 95th 1.645 · 97.5th 1.96 · 98th 2.05 · 99th 2.33 · middle 80 / 90 / 95 / 99% ↔ ±1.28 / ±1.645 / ±1.96 / ±2.575</div>'
 '<ul class="small"><li><span class="d"><b>"Give two interpretations" of an area:</b> "the area to the right of 200 is 0.2903" means (1) the <b>proportion</b> of the population above 200 is 0.2903 (29.03%) AND (2) the <b>probability</b> that one randomly selected person is above 200 is 0.2903.</span></li>'
 '<li><span class="d"><b>Is it normal?</b> histogram bell-shaped, one peak, symmetric, few outliers → yes; a <b>normal probability plot</b> (observed values vs the z-scores expected if normal) close to a straight line → yes; a long tail or a bent plot → not normal.</span></li></ul>')

B.append('<h2>DON\'T LOSE POINTS</h2><ul class="warn">'
 '<li>"Or" → subtract the overlap once. "And" → the one table cell. "Given" → divide by the given group, not the grand total. Σ P(x) = 1 and each P(x) 0–1 before calling a distribution valid.</li>'
 '<li>Binomial counts: "fewer than 3" = 0, 1, 2; "at least 3" = 1 − P(X ≤ 2); "at most 3" = 0, 1, 2, 3. Binomial σ needs the √. Uniform: length ÷ total width, never z.</li>'
 '<li>Normal: z to 2 decimals; the hint or table value = area to the LEFT; "above" → 1 − left; "between" → big − small. Percentile → area → z (inside the table) → x = μ + zσ. 4 decimals; formula every time.</li></ul>')
B.append('<h2>WRITE THIS SENTENCE — answer templates</h2><ul class="small">'
 '<li><b>Interpret the mean / expected value:</b> "Over many [series], the average [games per series] is about [5.48]." Insurance: "$86 profit per policy on average → positive → keep selling."</li>'
 '<li><b>Valid distribution? (Q2):</b> "Not valid: the probabilities add to 0.73, not 1" / "not valid: P(2) = −0.1 is negative" / "each P(x) is 0–1 and they add to 1 → valid."</li>'
 '<li><b>Binomial or not:</b> "Yes: fixed n = 10, independent, two outcomes, same p = 0.60; x = 0, 1, …, 10." / "No: n not fixed." / "No: no replacement; the sample is 4/30 = 13% &gt; 5% of the group, so p changes."</li>'
 '<li><b>Two interpretations of an area</b> (0.2903 right of 200): "(1) 29.03% of males are above 200. (2) The probability a randomly selected male is above 200 is 0.2903."</li>'
 '<li><b>Unusual?</b> "P = 0.025 &lt; 0.05 → unusual" / "count 130 is inside μ ± 2σ = 106.1 to 133.9 → not unusual." <b>Independent?</b> "P(A | B) = 0.2381 ≠ P(A) = 0.2051 → dependent." <b>Sketch:</b> uniform = "flat line at height 1/30 from 70 to 100, 0 elsewhere, area 1"; normal = bell at μ, ticks μ ± σ, 2σ, 3σ, shade, write the area.</li></ul>'
 '<p class="small"><b>Calculator:</b> 36 ÷ 78 = 0.4615 · 0.4 ^ 7 = 0.0016384 · 10 [nCr] 3 = 120 (TI-84: MATH → PRB; TI-89: 2nd MATH → Probability → nCr(10,3); no key: 10! ÷ (3!·7!)) · √48 = 6.93 · keep decimals (round only z, to 2). <b>Order (minutes):</b> Q1 6 · Q2 2 · Q5 5 · Q6 6 · Q7 9 · Q3 10 · Q4 10. Formula first, box every answer.</p>')



HTML = ("<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'><title>STA2023 Exam 2 Cheat Sheet — solved + reference</title>"
 f"<link rel='stylesheet' href='{KATEX}/katex.min.css'><script src='{KATEX}/katex.min.js'></script><script src='{KATEX}/contrib/auto-render.min.js'></script>"
 "<style>" + CSS.replace("__FS1__", str(FS1)).replace("__FS2__", str(FS2)) + "</style></head><body>"
 '<div class="side pb"><h1>STA2023 Exam 2 — SIDE A — THE PRACTICE EXAM, SOLVED (the real exam copies it) ' + LEG_A + '</h1>' + "\n".join(A) + '</div>'
 '<div class="side s2"><h1>STA2023 Exam 2 — SIDE B — RULES, FORMULAS, PICTURES ' + LEG_B + '</h1>' + "\n".join(B) + '</div>'
 "<script>renderMathInElement(document.body,{delimiters:[{left:'\\\\[',right:'\\\\]',display:true},{left:'\\\\(',right:'\\\\)',display:false}],throwOnError:false});</script>"
 + ("<script>var out=[];var cw=document.querySelector('.side').getBoundingClientRect().width/3-6;document.querySelectorAll('.katex').forEach(function(e){var w=e.getBoundingClientRect().width;if(w>cw){out.push(Math.round(w)+'px > '+Math.round(cw)+' : '+e.textContent.slice(0,70));}});var pageH=(11-0.44)*96;document.querySelectorAll('.side').forEach(function(sd,i){var h1=sd.querySelector('h1');var hh=h1?h1.getBoundingClientRect().height:0;var cwpx=(8.5-0.44)*96;var colw=(cwpx-2*(7*96/72))/3;var cl=sd.cloneNode(true);cl.style.columnCount='1';cl.style.width=colw+'px';cl.style.position='absolute';cl.style.left='-99999px';cl.querySelector('h1').remove();document.body.appendChild(cl);var ch=(pageH-hh-4);var need=cl.getBoundingClientRect().height/ch;out.push('SIDE'+(i+1)+' needs '+need.toFixed(2)+' columns');var mathH=0;cl.querySelectorAll('.katex-display').forEach(function(k){mathH+=k.getBoundingClientRect().height;});out.push('  display-math height = '+(mathH/ch).toFixed(2)+' columns');var secs=cl.querySelectorAll('h2');secs.forEach(function(h,k){var hh2=h.getBoundingClientRect().top;var nxt=secs[k+1];var bot=nxt?nxt.getBoundingClientRect().top:cl.getBoundingClientRect().bottom;out.push('  '+h.textContent.slice(0,40)+' : '+((bot-hh2)/ch).toFixed(2));});cl.remove();});var p=document.createElement('pre');p.id='dbg';p.textContent=out.length?out.join('\\n'):'NO-OVERFLOW';document.body.appendChild(p);</script>" if __import__('os').environ.get('DEBUG') else "")
 + "</body></html>")
open(OUT, "w").write(HTML)
print("written", OUT, len(HTML), "FS", FS1, FS2)
