import sys
from math import erf, sqrt, comb
KATEX = "file:///tmp/claude-0/-home-user-dsdasda/bdc32f87-6f2d-5f62-952a-43c9c6f6142d/scratchpad/ex2/katex/node_modules/katex/dist"
OUT_EXAM = "/home/user/dsdasda/STA2023_Mirror_Exam_2.html"
OUT_KEY  = "/home/user/dsdasda/STA2023_Mirror_Exam_2_KEY.html"
Phi = lambda z: 0.5*(1+erf(z/sqrt(2)))
def z2(x, mu, sd): return round((x-mu)/sd + 1e-12, 2)
def esc(t): return t.replace("<","&lt;").replace(">","&gt;")
def M(t): return "\\(" + esc(t) + "\\)"
def D(t): return "<div class='dm'>\\[" + esc(t) + "\\]</div>"

# ---------- numbers (all computed here so the hints match the questions)
# Q6 hints
h085, hm130, hm025 = Phi(-0.85), Phi(-1.30), Phi(-0.25)
z6c = z2(300, 250, 40); h6c = Phi(z6c)
# Q7 hints
z7a, z7b, z7b1, z7b2 = z2(74,69,2.8), z2(65,69,2.8), z2(66,69,2.8), z2(72,69,2.8)
h7a, h7b, h7b1, h7b2 = Phi(z7a), Phi(z7b), Phi(z7b1), Phi(z7b2)
NW = lambda t: "<span style='white-space:nowrap'>" + t + "</span>"
HINT6 = "Hints: " + NW(f"P(Z &lt; −0.85) = {h085:.4f},") + " &nbsp; " + NW(f"P(Z &lt; −1.30) = {hm130:.4f},") + " &nbsp; " + NW(f"P(Z &lt; −0.25) = {hm025:.4f},") + " &nbsp; " + NW(f"P(Z &lt; {z6c:.2f}) = {h6c:.4f}.")
HINT7 = ("Hints: " + NW(f"P(Z &lt; {z7a:.2f}) = {h7a:.4f},") + " &nbsp; " + NW(f"P(Z &lt; {z7b:.2f}) = {h7b:.4f},") + " &nbsp; " + NW(f"P(Z &lt; {z7b1:.2f}) = {h7b1:.4f},") + " &nbsp; " + NW(f"P(Z &lt; {z7b2:.2f}) = {h7b2:.4f};") + " &nbsp; " + NW("the 10th percentile corresponds to z = −1.28.")).replace(") = -", ") = −").replace("&lt; -", "&lt; −")

CSS = f"""
@page {{ size: letter; margin: 0; }}
* {{ box-sizing: border-box; }}
html, body {{ margin:0; padding:0; background:#fff; color:#000; }}
body {{ font-family: KaTeX_Main, "Latin Modern Roman", "Times New Roman", serif; font-size: 12pt; line-height: 1.22; }}
.page {{ width: 8.5in; height: 11in; padding: 1.2in 1.5in 0.9in 1.5in; display:flex; flex-direction:column; break-after: page; page-break-after: always; position: relative; }}
.page:last-child {{ break-after: auto; page-break-after: auto; }}
.hdr {{ display:flex; justify-content:space-between; border-bottom: 0.6pt solid #000; padding-bottom: 2pt; margin-bottom: 16pt; font-size: 12pt; }}
.ftr {{ margin-top:auto; text-align:center; font-size: 12pt; padding-top: 10pt; }}
.box {{ border: 0.7pt solid #000; padding: 10pt 14pt 6pt 14pt; margin: 2pt 0 26pt 0; font-size: 11.5pt; }}
.box ul {{ margin:0; padding-left: 14pt; }} .box li {{ margin: 0 0 4pt 0; }}
.red {{ color:#b00000; font-weight:bold; }}
h1 {{ font-size: 17pt; margin: 14pt 0 8pt 0; font-weight: bold; line-height:1.2; }}
h2 {{ font-size: 11.5pt; margin: 6pt 0 2pt 0; font-weight: bold; }}
p {{ margin: 0 0 6pt 0; }}
.parts {{ margin: 6pt 0 0 0; padding: 0; list-style: none; }}
.parts li {{ margin: 0 0 var(--gap, 34pt) 0; padding-left: 26pt; text-indent: -26pt; }}
.parts li b {{ font-weight:bold; }}
table.bt {{ border-collapse: collapse; margin: 6pt auto 8pt auto; font-size: 11pt; }}
table.bt th, table.bt td {{ padding: 1.5pt 12pt; text-align:center; }}
table.bt th {{ border-top: 0.9pt solid #000; border-bottom: 0.6pt solid #000; font-weight: bold; }}
table.bt td.l, table.bt th.l {{ text-align:left; }}
table.bt tr:last-child td {{ border-bottom: 0.9pt solid #000; }}
table.vl {{ border-collapse: collapse; margin: 6pt auto 8pt auto; font-size: 11pt; }}
table.vl th {{ border-bottom: 0.6pt solid #000; padding: 0 8pt; font-weight: normal; }}
table.vl td {{ padding: 0 8pt; text-align:center; }}
table.vl th.l, table.vl td.l {{ border-right: 0.6pt solid #000; }}
.center {{ text-align:center; }}
.sig {{ display:flex; align-items:baseline; margin: 0 0 11pt 0; }} .sig b {{ white-space:nowrap; margin-right: 6pt; }} .line {{ flex:1; border-bottom: 0.6pt solid #000; height: 0.9em; }}
.ack {{ margin: 6pt 0 10pt 28pt; width: 4.6in; }}
.hint {{ margin: 4pt 0 8pt 0; font-size: 10.6pt; }}
.katex {{ font-size: 1.0em; white-space: nowrap; }}
.dm {{ margin: 2pt 0 2pt 14pt; }} .katex-display {{ margin: 0 !important; text-align:left !important; }}
.ans {{ border: 0.9pt solid #000; padding: 1pt 5pt; display:inline-block; margin: 2pt 0 6pt 0; font-weight:bold; }}
.key .q {{ margin: 0 0 14pt 0; }} .key h1 {{ font-size: 14pt; margin: 10pt 0 4pt 0; }} .key p {{ margin: 0 0 3pt 0; }}
.why {{ color:#333; font-style: italic; }}
"""
def hdr(title, date): return f'<div class="hdr"><span>STA2023</span><span>{title}</span><span>{date}</span></div>'
def ftr(n, tot): return f'<div class="ftr">Page {n} of {tot}</div>'
def page(n, tot, body, title="Practice Exam 2 (Mirror)", date="2 November 26"):
    return f'<div class="page">{hdr(title,date)}{body}{ftr(n,tot)}</div>'

# ============================ EXAM ============================
P = []
P.append(page(1, 6, '''
<div class="box"><ul>
<li>The <b>Mid Term Exam 2</b> for <b>STA 2023</b> will be held in class on <b>November 3, 2026</b> (this mirror: time yourself, <b>50 minutes</b>).</li>
<li>The exam will cover Chapters 4-6.</li>
<li>The exam is <b>closed-book and closed-notes</b>.</li>
<li>You may use a <b>calculator</b> and <b>one double-page cheat sheet</b>.</li>
<li class="red">You must bring your physical UCF ID card. Your exam will not be graded if you fail to present your physical UCF ID card.</li>
<li>You are <b>not allowed</b> to use laptops, cellphones, tablets, or any other electronic devices.</li>
<li>All cellphones must be <b>turned off</b> before the exam begins.</li>
<li>Show all necessary steps for full credit.</li>
<li><b>Write all work clearly.</b> Answers without supporting steps may not receive credit and Round all probabilities to <b>four decimal places</b>.</li>
<li><b>Write answers in the spaces provided.</b> If you need additional space, clearly label the continuation.</li>
<li>All needed z-scores and standard normal areas are given as <b>hints</b> on the exam paper.</li>
<li><b>Total points: 50.</b></li></ul></div>
<h1>Question 0: Academic Integrity Acknowledgment (Required)</h1>
<p>As your first task, please <b>handwrite the acknowledgment statement below</b> on your answer sheet. Then write your <b>full name</b>, <b>signature</b>, and <b>UCF ID number (in digits)</b> below it.</p>'''))
P.append(page(2, 6, '''
<p><i>Acknowledgment Statement:</i></p>
<p class="ack">“I acknowledge that I have read and understood all exam instructions and that I have fully complied, and will continue to comply, with the university’s policies on Academic Integrity in completing and submitting this exam.”</p>
<div class="sig"><b>Name (print clearly):</b> <span class="line"></span></div>
<div class="sig"><b>Signature:</b> <span class="line"></span></div>
<div class="sig"><b>UCF ID Number:</b> <span class="line"></span></div>
<h1>Question 1 (6 points)</h1>
<h2>Commuting and Housing</h2>
<p style="margin-left:12pt">The table below summarizes how 110 students at a university commute and where they live.</p>
<table class="bt"><tr><th class="l">Commute</th><th>Lives on campus</th><th>Lives off campus</th></tr>
<tr><td class="l">Drive</td><td>8</td><td>34</td></tr><tr><td class="l">Bus</td><td>10</td><td>16</td></tr><tr><td class="l">Walk</td><td>22</td><td>4</td></tr><tr><td class="l">Bike</td><td>9</td><td>7</td></tr></table>
<p class="center">Total on campus = 49, &nbsp;&nbsp;&nbsp;&nbsp; Total off campus = 61, &nbsp;&nbsp;&nbsp;&nbsp; Overall Total = 110</p>
<p style="margin-left:12pt">Answer each question. Show your work when appropriate.</p>
<ul class="parts">
<li>(a) <b>(1 points)</b> What is the probability that a randomly selected student lives off campus?</li>
<li>(b) <b>(1 points)</b> What is the probability that a randomly selected student walks to campus?</li></ul>'''))
P.append(page(3, 6, '''
<ul class="parts">
<li>(c) <b>(1 point)</b> What is the probability that a randomly selected student drives OR lives on campus?</li>
<li>(d) <b>(1 points)</b> What is the probability that a randomly selected student bikes AND lives off campus?</li>
<li>(e) <b>(2 points)</b> What is the probability that a randomly selected student takes the bus given that the student lives off campus?</li></ul>
<h1>Question 2 (2 points): Discrete Probability Distribution</h1>
<p>Determine whether the following distribution represents a valid <b>discrete probability distribution</b>. If not, explain why.</p>
<table class="vl"><tr><th class="l">''' + M("x") + '''</th><th>''' + M("P(x)") + '''</th></tr>
<tr><td class="l">1</td><td>0.15</td></tr><tr><td class="l">2</td><td>0.25</td></tr><tr><td class="l">3</td><td>0.30</td></tr><tr><td class="l">4</td><td>0.20</td></tr><tr><td class="l">5</td><td>0.12</td></tr></table>'''))
P.append(page(4, 6, '''
<h1>Question 3 (8 points): Cars per Household</h1>
<p>A city planner records the number of cars, ''' + M("X") + ''', owned by each household in a random sample of 85 households in one neighborhood. The following data represent the number of cars per household. <i>Note: no household in the sample owned more than 3 cars.</i></p>
<table class="vl"><tr><th class="l">''' + M("x") + '''</th><th>Frequency</th></tr>
<tr><td class="l">0</td><td>13</td></tr><tr><td class="l">1</td><td>29</td></tr><tr><td class="l">2</td><td>33</td></tr><tr><td class="l">3</td><td>10</td></tr></table>
<ul class="parts" style="--gap:12pt">
<li><b>(a)</b> (2 pt) Construct a probability distribution for the random variable ''' + M("X") + ''', the number of cars per household.</li>
<li><b>(b)</b> (2 pt) Graph the discrete probability distribution.</li>
<li><b>(c)</b> (2 pt) Compute and interpret the mean of ''' + M("X") + '''.</li>
<li><b>(d)</b> (2 pt) Compute the standard deviation of ''' + M("X") + '''.</li></ul>
<h1>Question 4 (8 points): Reading Habits</h1>
<p>According to a national survey, 35% of U.S. adults read at least one book last month. In a random sample of 8 U.S. adults, find the probability that:</p>
<ul class="parts" style="--gap:12pt">
<li><b>(a)</b> (2 pt) Exactly 2 read at least one book last month.</li>
<li><b>(b)</b> (2 pt) At most 2 read at least one book last month.</li>
<li><b>(c)</b> (2 pt) At least 1 read at least one book last month.</li>
<li><b>(d)</b> (2 pt) For a random sample of 300 U.S. adults, find the expected number and standard deviation of those who read at least one book last month.</li></ul>'''))
P.append(page(5, 6, '''
<h1>Question 5 (5 points): Shuttle Wait Time</h1>
<p>Suppose the waiting time ''' + M("X") + ''' (in minutes) for a campus shuttle is uniformly distributed between 0 and 25 minutes.</p>
<ul class="parts" style="--gap:12pt">
<li><b>(a)</b> (1 pt) Sketch or describe the graph of the uniform probability density function (pdf).</li>
<li><b>(b)</b> (2 pt) Find the probability that the wait is between 5 and 15 minutes, i.e., ''' + M(r"P(5 \le X \le 15)") + '''.</li>
<li><b>(c)</b> (2 pt) Find the probability that the wait is more than 18 minutes, i.e., ''' + M("P(X > 18)") + '''.</li></ul>
<h1>Question 6 (6 points): Normal Distribution and z‑Scores</h1>
<p><b>Instructions:</b> Use the hints below (or the standard normal table) to find each probability. Show work and round final answers to four decimal places.</p>
<p class="hint"><b>''' + HINT6 + '''</b></p>
<ul class="parts" style="--gap:12pt">
<li><b>(a)</b> Find the area to the left of ''' + M("z = -0.85") + '''.</li>
<li><b>(b)</b> Find the area between ''' + M("z = -1.30") + ''' and ''' + M("z = -0.25") + '''.</li>
<li><b>(c)</b> The random variable ''' + M("X") + ''' is normally distributed with ''' + M(r"\mu = 250") + ''' and ''' + M(r"\sigma = 40") + '''. Find ''' + M("P(X > 300)") + '''.</li></ul>
<h1>Question 7 (8 points): Heights of Adult Men</h1>
<p>The heights of adult men in the U.S. are approximately normally distributed with mean ''' + M(r"\mu = 69") + ''' inches and standard deviation ''' + M(r"\sigma = 2.8") + ''' inches.</p>
<p class="hint"><b>''' + HINT7 + '''</b></p>
<ul class="parts" style="--gap:12pt">
<li><b>(a)</b> (2 pt) What is the probability that a randomly selected man is taller than 74 inches?</li></ul>'''))
P.append(page(6, 6, '''
<ul class="parts">
<li><b>(b)</b> (2 pt) What is the probability that a randomly selected man is shorter than 65 inches?</li>
<li><b>(c)</b> (2 pt) What proportion of men are between 66 and 72 inches tall?</li>
<li><b>(d)</b> (2 pt) What height places a man at the 10th percentile?</li></ul>'''))

HEAD = (f"<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'><title>STA2023 Mirror Exam 2</title>"
 f"<link rel='stylesheet' href='{KATEX}/katex.min.css'><script src='{KATEX}/katex.min.js'></script><script src='{KATEX}/contrib/auto-render.min.js'></script><style>{CSS}</style></head><body>")
TAIL = "<script>renderMathInElement(document.body,{delimiters:[{left:'\\\\[',right:'\\\\]',display:true},{left:'\\\\(',right:'\\\\)',display:false}],throwOnError:false});</script></body></html>"
open(OUT_EXAM, "w").write(HEAD + "".join(P) + TAIL)

# ============================ KEY ============================
F3 = [13, 29, 33, 10]; N3 = sum(F3); xs=[0,1,2,3]
pr = [round(f/N3, 4) for f in F3]                      # course method: P(x) to 4 decimals
mu3 = round(sum(x*pi for x,pi in zip(xs,pr)), 2)       # mean to 2 decimals (5.48-style)
terms = [round((x-mu3)**2, 4) for x in xs]
prods = [round(t*pi, 4) for t,pi in zip(terms, pr)]
var3 = round(sum(prods), 4); sd3 = sqrt(var3)
mu_exact = sum(x*f for x,f in zip(xs,F3))/N3; var_exact = sum(x*x*f for x,f in zip(xs,F3))/N3 - mu_exact**2
n4,p4 = 8,0.35; B=lambda k: comb(n4,k)*p4**k*(1-p4)**(n4-k)
K = []
def q(title, body): K.append(f'<div class="q"><h1>{title}</h1>{body}</div>')
def part(lab, txt): return f'<p><b>{lab}</b> {txt}</p>'
def ans(t): return f'<span class="ans">{t}</span>'
q("Question 1 (6 points) — Commuting and Housing",
  '<p>First add the margins: Drive 42, Bus 26, Walk 26, Bike 16 (row totals); on campus 49, off campus 61; overall 110.</p>' +
  part("(a)", "one category → its total ÷ grand total") + D(r"P(\text{off campus})=\frac{61}{110}=0.5545") + ans("0.5545") +
  part("(b)", "a row → add its cells, ÷ 110") + D(r"P(\text{walk})=\frac{22+4}{110}=\frac{26}{110}=0.2364") + ans("0.2364") +
  part("(c)", "OR → add, subtract the overlap (drive AND on campus = 8) once") + D(r"P(\text{drive or on})=\frac{42}{110}+\frac{49}{110}-\frac{8}{110}=\frac{83}{110}=0.7545") + ans("0.7545") +
  part("(d)", "AND → the one cell ÷ 110") + D(r"P(\text{bike and off})=\frac{7}{110}=0.0636") + ans("0.0636") +
  part("(e)", "GIVEN off campus → divide by the off-campus total (61), not 110") + D(r"P(\text{bus}\mid\text{off})=\frac{16}{61}=0.2623") + ans("0.2623") +
  '<p class="why">Common errors: (c) forgetting the overlap gives 91/110 = 0.8273; (e) 16/110 = 0.1455 uses the wrong denominator.</p>')
q("Question 2 (2 points) — Valid distribution?",
  '<p>Rule 1: 0.15, 0.25, 0.30, 0.20, 0.12 are all between 0 and 1 ✓. &nbsp; Rule 2: add them.</p>' + D(r"0.15+0.25+0.30+0.20+0.12=1.02\neq 1") +
  ans("NOT a valid probability distribution — the probabilities add to 1.02, not 1.") + '<p class="why">Write both checks; the question says “explain why.”</p>')
q("Question 3 (8 points) — Cars per Household",
  part("(a)", f"P(x) = frequency ÷ total; total = 13 + 29 + 33 + 10 = {N3}") +
  D(rf"P(0)=\frac{{13}}{{{N3}}}={pr[0]:.4f}\qquad P(1)=\frac{{29}}{{{N3}}}={pr[1]:.4f}\qquad P(2)=\frac{{33}}{{{N3}}}={pr[2]:.4f}\qquad P(3)=\frac{{10}}{{{N3}}}={pr[3]:.4f}") +
  f'<p>Check: {pr[0]:.4f} + {pr[1]:.4f} + {pr[2]:.4f} + {pr[3]:.4f} = {sum(pr):.4f} ≈ 1 ✓ (rounding)</p>' +
  part("(b)", f"x across (0, 1, 2, 3), P(x) up; a vertical bar above each x with heights {pr[0]:.4f}, {pr[1]:.4f}, {pr[2]:.4f}, {pr[3]:.4f}; tallest at x = 2; label both axes.") +
  part("(c)", "") + D(rf"\mu=\sum x\,P(x)=0({pr[0]:.4f})+1({pr[1]:.4f})+2({pr[2]:.4f})+3({pr[3]:.4f})") + D(rf"=0+{pr[1]:.4f}+{2*pr[2]:.4f}+{3*pr[3]:.4f}={sum(x*pi for x,pi in zip(xs,pr)):.4f}\approx {mu3:.2f}") + ans(f"μ ≈ {mu3:.2f} cars") +
  f'<p>Interpretation: over many households in this neighborhood, the average number of cars per household is about {mu3:.2f}.</p>' +
  part("(d)", f"σ = √Σ(x − μ)²·P(x) with μ = {mu3:.2f}") +
  D(rf"(0-{mu3:.2f})^2({pr[0]:.4f})={terms[0]:.4f}({pr[0]:.4f})={prods[0]:.4f}\qquad (1-{mu3:.2f})^2({pr[1]:.4f})={terms[1]:.4f}({pr[1]:.4f})={prods[1]:.4f}") +
  D(rf"(2-{mu3:.2f})^2({pr[2]:.4f})={terms[2]:.4f}({pr[2]:.4f})={prods[2]:.4f}\qquad (3-{mu3:.2f})^2({pr[3]:.4f})={terms[3]:.4f}({pr[3]:.4f})={prods[3]:.4f}") +
  D(rf"\sigma^2={prods[0]:.4f}+{prods[1]:.4f}+{prods[2]:.4f}+{prods[3]:.4f}={var3:.4f}\qquad \sigma=\sqrt{{{var3:.4f}}}={sd3:.2f}") + ans(f"σ ≈ {sd3:.2f} cars") +
  f'<p class="why">(Unrounded from the raw counts: μ = {mu_exact:.4f}, σ² = {var_exact:.4f}, σ = {sqrt(var_exact):.4f}; the same to 2 decimals.)</p>')
q("Question 4 (8 points) — Reading Habits (binomial, n = 8, p = 0.35, 1 − p = 0.65)",
  D(r"P(x)={}_{8}C_{x}\,(0.35)^{x}(0.65)^{8-x}") +
  part("(a)", "exactly 2") + D(r"{}_{8}C_{2}=\frac{8\cdot 7}{2\cdot 1}=28\qquad P(2)=28(0.35)^2(0.65)^6=28(0.1225)(0.075419)=0.2587") + ans("0.2587") +
  part("(b)", "at most 2 → x = 0, 1, 2 (the 2 is IN)") +
  D(r"P(0)=(0.65)^8=0.0319\qquad P(1)=8(0.35)(0.65)^7=0.1373\qquad P(2)=0.2587") + D(r"P(X\le 2)=0.0319+0.1373+0.2587=0.4279\approx 0.4278") +
  ans("0.4278 (0.4279 if you add the rounded values — both accepted)") +
  part("(c)", "at least 1 → 1 − P(0)") + D(r"P(X\ge 1)=1-(0.65)^8=1-0.0319=0.9681") + ans("0.9681") +
  part("(d)", "n = 300") + D(r"\mu=np=300(0.35)=105\qquad \sigma=\sqrt{np(1-p)}=\sqrt{300(0.35)(0.65)}=\sqrt{68.25}=8.26") + ans("μ = 105, σ ≈ 8.26") +
  f'<p class="why">Exact values: P(2) = {B(2):.4f}, P(0) = {B(0):.4f}, P(1) = {B(1):.4f}, P(X ≤ 2) = {B(0)+B(1)+B(2):.4f}.</p>')
q("Question 5 (5 points) — Shuttle Wait Time (uniform, a = 0, b = 25)",
  part("(a)", "") + D(r"\text{height}=\frac{1}{b-a}=\frac{1}{25-0}=\frac{1}{25}=0.04") +
  ans("a flat line (rectangle) at height 1/25 from 0 to 25 minutes, and 0 elsewhere; area = 25 × 1/25 = 1") +
  part("(b)", "") + D(r"P(5\le X\le 15)=\frac{15-5}{25-0}=\frac{10}{25}=0.4000") + ans("0.4000") +
  part("(c)", "“more than 18” → from 18 up to the top end 25") + D(r"P(X>18)=\frac{25-18}{25-0}=\frac{7}{25}=0.2800") + ans("0.2800"))
q("Question 6 (6 points) — Normal Distribution and z-Scores",
  part("(a)", f"area to the LEFT of a negative z: the hint P(Z &lt; −0.85) = {h085:.4f} is already the answer (no 1 − needed)") + D(rf"P(Z<-0.85)={h085:.4f}") + ans(f"{h085:.4f}") +
  part("(b)", f"between = (left of the bigger z) − (left of the smaller z); −0.25 is bigger than −1.30") + D(rf"{hm025:.4f}-{hm130:.4f}={hm025-hm130:.4f}") + ans(f"{hm025-hm130:.4f}") +
  part("(c)", "") + D(rf"z=\frac{{300-250}}{{40}}={z6c:.2f}\ \to\ \text{{left}}={h6c:.4f}\qquad P(X>300)=1-{h6c:.4f}={1-h6c:.4f}") + ans(f"{1-h6c:.4f}"))
q("Question 7 (8 points) — Heights of Adult Men (μ = 69, σ = 2.8)",
  part("(a)", "taller than 74 → right tail") + D(rf"z=\frac{{74-69}}{{2.8}}={z7a:.2f}\ \to\ \text{{left}}={h7a:.4f}\qquad P(X>74)=1-{h7a:.4f}={1-h7a:.4f}") + ans(f"{1-h7a:.4f}") +
  part("(b)", "shorter than 65 → left area (the hint is already the left area)") + D(rf"z=\frac{{65-69}}{{2.8}}={z7b:.2f}\qquad P(X<65)={h7b:.4f}") + ans(f"{h7b:.4f}") +
  part("(c)", "between 66 and 72") + D(rf"z_1=\frac{{66-69}}{{2.8}}={z7b1:.2f}\to {h7b1:.4f}\qquad z_2=\frac{{72-69}}{{2.8}}={z7b2:.2f}\to {h7b2:.4f}") + D(rf"P(66<X<72)={h7b2:.4f}-{h7b1:.4f}={h7b2-h7b1:.4f}") + ans(f"{h7b2-h7b1:.4f}") +
  part("(d)", "10th percentile → area to the LEFT = 0.10 → hint z = −1.28 (negative: lower tail)") + D(r"x=\mu+z\sigma=69+(-1.28)(2.8)=69-3.584=65.416\approx 65.4") + ans("≈ 65.4 inches") +
  '<p class="why">Sanity checks: (a) must be below 0.5 (74 is above average); (d) must be below 69.</p>')
KHEAD = HEAD.replace("<title>STA2023 Mirror Exam 2</title>", "<title>STA2023 Mirror Exam 2 — Answer Key</title>").replace("</style>", ".page{height:auto;min-height:11in}</style>")
KEYHTML = KHEAD + '<div class="page key">' + hdr("Practice Exam 2 (Mirror) — ANSWER KEY", "2 November 26") + '<p class="why">Grade yourself: formula written? numbers substituted? arithmetic shown? answer boxed to 4 decimals? interpretation sentence where asked? Each part on the real exam is scored on those steps, not only the final number.</p>' + "".join(K) + '</div>' + TAIL
open(OUT_KEY, "w").write(KEYHTML)
print("written", OUT_EXAM, OUT_KEY)
print("HINT6:", HINT6); print("HINT7:", HINT7)
