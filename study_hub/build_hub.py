"""Build the Exam 2 study hub page. Usage: python3 build_hub.py <tests.json> <out.html>"""
import json, sys, html

tests_path, out_path = sys.argv[1], sys.argv[2]
generated = json.load(open(tests_path))          # {"tests":[{"key","test":{title,intro,questions:[...]},"issues":[...]}]}
by_key = {t["key"]: t["test"] for t in generated["tests"]}

# ---------- Official practice exam with full worked solutions (verified earlier in Python) ----------
OFFICIAL = {
 "title": "Official Practice Exam 2 (with full solutions)",
 "intro": "The exact practice exam Dr. Amir posted. The real exam follows this format. Do it timed (50 minutes) with only your cheat sheet and calculator, then grade yourself.",
 "questions": [
  {"points": 6, "prompt": "Employment status of 78 residents.\nStatus | Males | Females\nFull-time | 22 | 18\nPart-time | 6 | 10\nUnemployed | 3 | 2\nNot in labor force | 5 | 12\nTotal Males = 36, Total Females = 42, Overall Total = 78.",
   "parts": [
    {"label": "(a)", "question": "What is the probability that a randomly selected resident is male?", "answer": "0.4615", "solution": "P(male) = (males) / (total) = 36/78 = 0.4615"},
    {"label": "(b)", "question": "What is the probability that a randomly selected resident is part-time?", "answer": "0.2051", "solution": "Part-time row total = 6 + 10 = 16\nP(part-time) = 16/78 = 0.2051"},
    {"label": "(c)", "question": "What is the probability that a randomly selected resident is male OR unemployed?", "answer": "0.4872", "solution": "Unemployed row total = 3 + 2 = 5. The overlap (male AND unemployed) = 3.\nP(male or unemployed) = P(male) + P(unemployed) − P(both)\n= 36/78 + 5/78 − 3/78 = 38/78 = 0.4872"},
    {"label": "(d)", "question": "What is the probability that a randomly selected resident is female AND not in the labor force?", "answer": "0.1538", "solution": "That is one cell: 12.\nP(female and not in labor force) = 12/78 = 0.1538"},
    {"label": "(e)", "question": "What is the probability that a randomly selected resident is part-time given that the resident is female?", "answer": "0.2381", "solution": "\"Given female\" → divide by the females total only.\nP(part-time | female) = (part-time females) / (females) = 10/42 = 0.2381"}]},
  {"points": 2, "prompt": "Determine whether the following distribution represents a valid discrete probability distribution. If not, explain why.\nx: 0, 1, 2, 3, 4\nP(x): 0.34, 0.21, 0.13, 0.04, 0.01",
   "parts": [{"label": "", "question": "Valid or not?", "answer": "NOT valid — the probabilities add to 0.73, not 1.", "solution": "Rule 1: each P(x) is between 0 and 1 ✓\nRule 2: 0.34 + 0.21 + 0.13 + 0.04 + 0.01 = 0.73 ≠ 1 ✗\nNot a valid distribution (the probabilities must sum to 1)."}]},
  {"points": 8, "prompt": "Stanley Cup: number of games played, X, before a champion was determined.\nx: 4, 5, 6, 7\nFrequency: 20, 20, 26, 17",
   "parts": [
    {"label": "(a)", "question": "Construct a probability distribution for X.", "answer": "P(4) = 0.2410, P(5) = 0.2410, P(6) = 0.3133, P(7) = 0.2048", "check": {"type":"numbers","fields":[{"label":"P(4)","value":0.2410,"tol":0.0002},{"label":"P(5)","value":0.2410,"tol":0.0002},{"label":"P(6)","value":0.3133,"tol":0.0002},{"label":"P(7)","value":0.2048,"tol":0.0002}]}, "solution": "Total = 20 + 20 + 26 + 17 = 83\nP(4) = 20/83 = 0.2410\nP(5) = 20/83 = 0.2410\nP(6) = 26/83 = 0.3133\nP(7) = 17/83 = 0.2048\nCheck: sum ≈ 1.0001 ≈ 1 ✓"},
    {"label": "(b)", "question": "Graph the discrete probability distribution.", "answer": "Vertical lines/bars at x = 4, 5, 6, 7 with heights 0.2410, 0.2410, 0.3133, 0.2048", "solution": "Horizontal axis: x (4, 5, 6, 7). Vertical axis: P(x).\nDraw a vertical line (or bar) above each x with height equal to its probability. The tallest is at x = 6."},
    {"label": "(c)", "question": "Compute and interpret the mean of X.", "answer": "μ = 5.48 games", "solution": "μ = Σ x·P(x)\n= 4(0.2410) + 5(0.2410) + 6(0.3133) + 7(0.2048)\n= 0.9640 + 1.2050 + 1.8798 + 1.4336\n= 5.48 games\nInterpretation: over many Stanley Cup series, the series lasts about 5.48 games on average."},
    {"label": "(d)", "question": "Compute the standard deviation of X.", "answer": "σ ≈ 1.07 games", "solution": "σ = sqrt( Σ (x − μ)²·P(x) ), μ = 5.48\n(4 − 5.48)²(0.2410) = 2.1904(0.2410) = 0.5279\n(5 − 5.48)²(0.2410) = 0.2304(0.2410) = 0.0555\n(6 − 5.48)²(0.3133) = 0.2704(0.3133) = 0.0847\n(7 − 5.48)²(0.2048) = 2.3104(0.2048) = 0.4732\nσ² = 0.5279 + 0.0555 + 0.0847 + 0.4732 = 1.1413\nσ = sqrt(1.1413) ≈ 1.07 games"}]},
  {"points": 8, "prompt": "According to a Gallup poll, 60% of U.S. women 18 years old or older stated that the minimum driving age should be 18. In a random sample of 10 U.S. women 18 years old or older, find the probability that:",
   "parts": [
    {"label": "(a)", "question": "Exactly 3 believe the minimum driving age should be 18.", "answer": "0.0425", "solution": "Binomial: n = 10, p = 0.60, 1 − p = 0.40\nP(3) = C(10,3) (0.60)^3 (0.40)^7\n= 120 · 0.216 · 0.0016384\n= 0.0425"},
    {"label": "(b)", "question": "Fewer than 3 believe the minimum driving age should be 18.", "answer": "0.0123", "solution": "Fewer than 3 → P(0) + P(1) + P(2)\nP(0) = C(10,0)(0.6)^0(0.4)^10 = 1 · 1 · 0.0001049 = 0.0001\nP(1) = C(10,1)(0.6)^1(0.4)^9 = 10 · 0.6 · 0.0002621 = 0.0016\nP(2) = C(10,2)(0.6)^2(0.4)^8 = 45 · 0.36 · 0.0006554 = 0.0106\nP(X < 3) = 0.0001 + 0.0016 + 0.0106 = 0.0123"},
    {"label": "(c)", "question": "Between 1 and 3 (inclusive) believe the minimum driving age should be 18.", "answer": "0.0547", "solution": "P(1 ≤ X ≤ 3) = P(1) + P(2) + P(3)\n= 0.0016 + 0.0106 + 0.0425\n= 0.0547"},
    {"label": "(d)", "question": "For a random sample of 200 U.S. women 18 years or older, find the expected number and standard deviation of those who believe the minimum driving age should be 18.", "answer": "μ = 120, σ ≈ 6.93", "check": {"type":"numbers","fields":[{"label":"μ","value":120,"tol":0.011},{"label":"σ","value":6.93,"tol":0.011}]}, "solution": "μ = n·p = 200(0.60) = 120\nσ = sqrt(n·p·(1 − p)) = sqrt(200 · 0.60 · 0.40) = sqrt(48) ≈ 6.93"}]},
  {"points": 5, "prompt": "Suppose the daytime temperature X (°F) in a coastal city during summer is uniformly distributed between 70°F and 100°F.",
   "parts": [
    {"label": "(a)", "question": "Sketch or describe the graph of the uniform probability density function (pdf).", "answer": "A flat rectangle from 70 to 100 with height 1/30", "solution": "Height = 1/(b − a) = 1/(100 − 70) = 1/30\nThe pdf is a horizontal line at 1/30 from x = 70 to x = 100 (and 0 elsewhere). Area = 30 · (1/30) = 1 ✓"},
    {"label": "(b)", "question": "Find P(75 ≤ X ≤ 85).", "answer": "0.3333", "solution": "P(75 ≤ X ≤ 85) = (85 − 75)/(100 − 70) = 10/30 = 0.3333"},
    {"label": "(c)", "question": "Find P(X < 80).", "answer": "0.3333", "solution": "P(X < 80) = (80 − 70)/(100 − 70) = 10/30 = 0.3333"}]},
  {"points": 6, "prompt": "Use the standard normal table. Round final answers to four decimal places.",
   "parts": [
    {"label": "(a)", "question": "Find the area to the left of z = −1.10.", "answer": "0.1357", "solution": "Table V, row −1.1, column .00 → 0.1357"},
    {"label": "(b)", "question": "Find the area between z = −0.60 and z = 1.45.", "answer": "0.6522", "solution": "Area left of 1.45 = 0.9265\nArea left of −0.60 = 0.2743\nBetween = 0.9265 − 0.2743 = 0.6522"},
    {"label": "(c)", "question": "X is normally distributed with μ = 80 and σ = 10. Find P(70 < X < 95).", "answer": "0.7745", "solution": "z₁ = (70 − 80)/10 = −1.00 → area left = 0.1587\nz₂ = (95 − 80)/10 = 1.50 → area left = 0.9332\nP(70 < X < 95) = 0.9332 − 0.1587 = 0.7745"}]},
  {"points": 8, "prompt": "The Wechsler Intelligence Scale for Children is approximately normally distributed with mean μ = 100 and standard deviation σ = 15.",
   "parts": [
    {"label": "(a)", "question": "What is the probability that a randomly selected test taker will score above 125?", "answer": "0.0475", "solution": "z = (125 − 100)/15 = 1.67\nArea left of 1.67 = 0.9525\nP(X > 125) = 1 − 0.9525 = 0.0475"},
    {"label": "(b)", "question": "What is the probability that a randomly selected test taker will score below 90?", "answer": "0.2514", "solution": "z = (90 − 100)/15 = −0.67\nP(X < 90) = area left of −0.67 = 0.2514"},
    {"label": "(c)", "question": "What proportion of test takers will score between 110 and 140?", "answer": "0.2476", "solution": "z₁ = (110 − 100)/15 = 0.67 → 0.7486\nz₂ = (140 − 100)/15 = 2.67 → 0.9962\nP(110 < X < 140) = 0.9962 − 0.7486 = 0.2476"},
    {"label": "(d)", "question": "What intelligence score will place a child in the 98th percentile?", "answer": "≈ 131 (130.75)", "check": {"type":"number","value":130.75,"tol":0.5,"label":"score"}, "solution": "98th percentile → area to the left = 0.98\nClosest table entry 0.9798 → z = 2.05\nx = μ + z·σ = 100 + 2.05(15) = 130.75 ≈ 131"}]}
 ]
}

ORDER = ["mini1", "mini2", "mini3", "mini4", "mini5", "mini6", "mini7", "mini0"]
QUIZ_NO = {"mini1": 1, "mini2": 2, "mini3": 3, "mini4": 4, "mini5": 5, "mini6": 6, "mini7": 7, "mini0": 8}
mini_tests = []
for k in ORDER:
    if k in by_key:
        t = dict(by_key[k], key=k)
        t["title"] = f"Quiz {QUIZ_NO[k]} · " + t["title"].replace("MINI TEST", "").replace("Mini Test", "").lstrip(" 0123456789—–-:·")
        mini_tests.append(t)
import os
EXB = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "examB_q4to7.json")))
OFFICIAL["questions"][3:7] = EXB
OFFICIAL["title"] = "Full Practice Exam 2 — Q1–Q3 as posted, Q4–Q7 switched up"
OFFICIAL["intro"] = "Same format and point values as the posted practice exam. Q1–Q3 are the posted questions; Q4–Q7 use new contexts and numbers (the posted Q4–Q7 are solved on your cheat sheet and in the Practice exam explained tab). Do it timed (50 minutes) with only your cheat sheet and calculator, then grade yourself."
big_tests = [dict(OFFICIAL, key="official")]
import os
M2 = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mirror2.json")))
mirror_tests = [dict(M2["test"], key="mirror2")]
D50 = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "drill50.json")))
drill_tests = [dict(D50["test"], key="drill50")]
DATA = json.dumps({"mini": mini_tests, "big": big_tests, "mirror": mirror_tests, "drill": drill_tests}, ensure_ascii=False)

PAGE = r"""<title>Exam 2 Study Hub</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bitter:wght@600;700&family=Public+Sans:ital,wght@0,400;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;600&display=swap">
<style>
/* Layout: a notebook — fixed top tab bar, one reading column, cards only for questions. Colors reuse the student's own cheat-sheet code: blue = meaning, red = rule, green = worked. */
:root{
  --bg:#f6f7f9; --paper:#ffffff; --fg:#17202a; --muted:#5b6672; --line:#d9dee5;
  --accent:#0d6b6b; --accent-ink:#ffffff;
  --def:#1646c2; --rule:#b4181f; --rule-bg:#fff3f3; --ex:#157236; --ex-bg:#f0f8f2;
  --ok:#1b7f3b; --bad:#b4181f; --warn-bg:#fff7e0; --warn:#8a5a00;
  --display:"Bitter", Georgia, "Times New Roman", serif;
  --body:"Public Sans", "Helvetica Neue", Arial, sans-serif;
  --mono:"JetBrains Mono", Menlo, Consolas, monospace;
}
@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){
  --bg:#13181e; --paper:#1b222a; --fg:#e8edf2; --muted:#9aa6b2; --line:#303a45;
  --accent:#3fb5b0; --accent-ink:#0d1418;
  --def:#8fb0ff; --rule:#ff8a90; --rule-bg:#2a1a1c; --ex:#7fd49a; --ex-bg:#172820;
  --ok:#6fd38f; --bad:#ff8a90; --warn-bg:#2b2410; --warn:#f1c76a; color-scheme:dark } }
:root[data-theme="dark"]{
  --bg:#13181e; --paper:#1b222a; --fg:#e8edf2; --muted:#9aa6b2; --line:#303a45;
  --accent:#3fb5b0; --accent-ink:#0d1418;
  --def:#8fb0ff; --rule:#ff8a90; --rule-bg:#2a1a1c; --ex:#7fd49a; --ex-bg:#172820;
  --ok:#6fd38f; --bad:#ff8a90; --warn-bg:#2b2410; --warn:#f1c76a; color-scheme:dark }

*{box-sizing:border-box}
body{background:var(--bg); color:var(--fg); font-family:var(--body); font-size:16px; line-height:1.5; margin:0}
body::before{content:""; position:fixed; inset:0 0 auto; height:env(safe-area-inset-top,0px); z-index:10; background:var(--paper)}
.wrap{max-width:860px; margin:0 auto; padding-left:max(16px, env(safe-area-inset-left,0px)); padding-right:max(16px, env(safe-area-inset-right,0px)); padding-block:0 48px}
header.top{position:sticky; top:env(safe-area-inset-top,0px); z-index:9; background:var(--paper); border-bottom:1px solid var(--line)}
header.top .wrap{padding-block:10px 0}
h1{font-family:var(--display); font-size:1.55rem; margin:0 0 6px; text-wrap:balance}
.sub{color:var(--muted); font-size:.92rem; margin:0 0 8px}
nav.tabs{display:flex; gap:4px; overflow-x:auto; padding-bottom:0}
nav.tabs button{appearance:none; border:0; border-bottom:3px solid transparent; background:none; color:var(--muted); font:600 .95rem var(--body); padding:8px 12px; cursor:pointer; white-space:nowrap}
nav.tabs button[aria-selected="true"]{color:var(--accent); border-bottom-color:var(--accent)}
nav.tabs button:focus-visible{outline:2px solid var(--accent); outline-offset:-2px; border-radius:4px}
section.view{padding-top:18px}
h2{font-family:var(--display); font-size:1.3rem; margin:26px 0 8px; text-wrap:balance}
h3{font-family:var(--display); font-size:1.08rem; margin:18px 0 6px}
p{margin:0 0 10px; max-width:68ch}
ul,ol{margin:0 0 10px; padding-left:22px; max-width:68ch}
li{margin:0 0 4px}
.def{color:var(--def)}
.rule{display:block; color:var(--rule); background:var(--rule-bg); border:1px solid var(--rule); border-radius:6px; padding:8px 12px; margin:8px 0 12px; font-weight:600; font-family:var(--mono); font-size:.9rem; white-space:pre-wrap}
.ex{display:block; color:var(--ex); background:var(--ex-bg); border-left:4px solid var(--ex); padding:8px 12px; margin:8px 0 12px; white-space:pre-wrap; font-size:.95rem}
.eyebrow{font-size:.75rem; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); font-weight:700}
.note{background:var(--warn-bg); color:var(--warn); border-radius:6px; padding:10px 12px; margin:10px 0 14px; max-width:68ch}
.grid{display:grid; grid-template-columns:repeat(auto-fit, minmax(240px,1fr)); gap:12px}
.card{background:var(--paper); border:1px solid var(--line); border-radius:8px; padding:12px 14px; min-width:0}
.card h3{margin-top:0}
.plan li{display:flex; gap:10px; align-items:flex-start; margin:0 0 8px}
.plan input{margin-top:4px; width:18px; height:18px; flex:0 0 auto; accent-color:var(--accent)}
.plan .t{color:var(--muted); font-size:.85rem; font-variant-numeric:tabular-nums}
.bar{height:8px; background:var(--line); border-radius:4px; overflow:hidden; margin:6px 0 12px}
.bar i{display:block; height:100%; background:var(--accent); width:0}
.pill{display:inline-block; font-size:.78rem; font-weight:700; padding:2px 8px; border-radius:999px; background:var(--line); color:var(--fg); margin-left:6px; font-variant-numeric:tabular-nums}
details.lesson{border:1px solid var(--line); border-radius:8px; background:var(--paper); padding:0 14px; margin:0 0 10px}
details.lesson summary{cursor:pointer; padding:12px 0; font-weight:700; font-family:var(--display); font-size:1.02rem; list-style:none; display:flex; justify-content:space-between; gap:10px}
details.lesson summary::-webkit-details-marker{display:none}
details.lesson summary .t{font:600 .8rem var(--body); color:var(--muted)}
details.lesson > div{padding:0 0 14px}
.q{background:var(--paper); border:1px solid var(--line); border-radius:8px; padding:14px; margin:0 0 14px; min-width:0}
.q .pts{float:right; color:var(--muted); font-size:.82rem; font-variant-numeric:tabular-nums}
.q .prompt{white-space:pre-wrap; font-weight:600; margin:0 0 8px}
.part{border-top:1px dashed var(--line); padding:10px 0 4px; min-width:0}
.part .qt{margin:0 0 8px; white-space:pre-wrap}
.part .lab{font-weight:700; margin-right:6px}
.btns{display:flex; flex-wrap:wrap; gap:8px; align-items:center}
button.b{appearance:none; border:1px solid var(--line); background:var(--paper); color:var(--fg); border-radius:6px; padding:6px 12px; font:600 .88rem var(--body); cursor:pointer}
button.b:focus-visible{outline:2px solid var(--accent); outline-offset:2px}
button.b.primary{background:var(--accent); color:var(--accent-ink); border-color:var(--accent)}
button.b.ok[aria-pressed="true"]{background:var(--ok); color:#fff; border-color:var(--ok)}
button.b.bad[aria-pressed="true"]{background:var(--bad); color:#fff; border-color:var(--bad)}
.ans{margin-top:10px}
.ans .final{font-weight:700; color:var(--ex)}
.ans pre{font-family:var(--mono); font-size:.86rem; white-space:pre-wrap; word-break:break-word; background:var(--ex-bg); border-left:4px solid var(--ex); color:var(--fg); padding:8px 10px; border-radius:4px; margin:6px 0 0; overflow-x:auto}
table.t{border-collapse:collapse; margin:6px 0 12px; font-size:.92rem}
table.t th, table.t td{border:1px solid var(--line); padding:4px 10px; text-align:left; vertical-align:top}
table.t th{background:var(--bg)}
.tscroll{overflow-x:auto; max-width:100%}
.score{font-variant-numeric:tabular-nums; color:var(--muted); font-size:.9rem; margin:0 0 10px}
.small{font-size:.88rem; color:var(--muted)}
kbd{font-family:var(--mono); font-size:.85em; background:var(--bg); border:1px solid var(--line); border-radius:4px; padding:0 4px}
.exp .qhead{margin-top:26px; padding-top:10px; border-top:2px solid var(--accent)}
.exp .part{background:var(--paper); border:1px solid var(--line); border-radius:8px; padding:12px 14px; margin:0 0 12px; min-width:0}
.exp .part > p:first-child{margin:0 0 8px}
.exp .ask{color:var(--def); margin:0 0 6px}
.exp .why, .rule-inline{color:var(--rule); font-weight:600; margin:0 0 6px}
.exp ol.steps{margin:0 0 8px}
.exp pre.work{font-family:var(--mono); font-size:.86rem; white-space:pre-wrap; word-break:break-word; background:var(--ex-bg); border-left:4px solid var(--ex); color:var(--fg); padding:8px 10px; border-radius:4px; margin:6px 0 8px; overflow-x:auto}
.exp .final{font-weight:700; color:var(--ex); margin:0 0 8px}
.exp .watch{background:var(--warn-bg); color:var(--warn); padding:6px 10px; border-radius:6px; font-size:.92rem; margin:0}
.fig{margin:10px 0 12px; max-width:440px} .fig svg{width:100%; height:auto; display:block; color:var(--fg)} .fig figcaption{font-size:.85rem; color:var(--muted); margin-top:4px}
@media (prefers-reduced-motion: no-preference){ .bar i{transition:width .25s} }
@media (max-width:480px){ body{font-size:15px} .q .pts{float:none; display:block} }
.chkrow{display:flex; flex-direction:column; gap:8px; align-items:flex-start; margin:6px 0}
.fields{display:flex; flex-wrap:wrap; gap:8px; align-items:center}
.fields.labeled{display:grid; grid-template-columns:minmax(0,max-content) minmax(8em,14em); gap:8px 10px; align-items:center}
.fields.labeled label{justify-self:end; text-align:right}
.fields.labeled .inp{width:100%}
.chkrow label{font-size:.9rem; color:var(--muted); max-width:11em; overflow-wrap:anywhere}
.inp::placeholder{color:var(--muted); opacity:1}
.inp.good{box-shadow:inset 0 0 0 1px var(--ok); background:color-mix(in srgb, var(--ok) 12%, var(--bg))}
.inp.wrong{box-shadow:inset 0 0 0 1px var(--bad); background:color-mix(in srgb, var(--bad) 10%, var(--bg))}
button.b.ok[aria-pressed="true"], button.b.bad[aria-pressed="true"]{color:var(--bg)}
.q .prompt .tscroll{overflow-x:auto}
@media (pointer:coarse), (max-width:480px){ button.b{min-height:44px; padding:8px 12px} .inp{min-height:44px; padding:8px 10px} .btns, .fields{gap:10px 8px} }
@media (max-width:480px){ header.top{position:static} nav.tabs{position:sticky; top:0; z-index:5; background:var(--bg); flex-wrap:wrap; gap:4px; padding-bottom:4px} }
.inp{font-family:var(--mono); font-size:1rem; padding:6px 10px; border:1px solid var(--line); border-radius:6px; background:var(--bg); color:var(--fg); width:9.5em; max-width:100%}
.inp:focus{outline:2px solid var(--accent); outline-offset:1px}
.inp.good{border-color:var(--ok)} .inp.wrong{border-color:var(--bad)}
.fb{margin:6px 0 4px; font-weight:700; min-height:1.2em}
.fb.ok{color:var(--ok)} .fb.bad{color:var(--bad)}
.b.choice[aria-pressed=true]{outline:2px solid var(--accent)}
.timer{display:inline-flex; gap:10px; align-items:center; flex-wrap:wrap; font-family:var(--mono); font-weight:700; font-size:1.05rem; padding:6px 10px; border:1px solid var(--line); border-radius:8px; margin:6px 0 10px}
.timer.over{color:var(--bad); border-color:var(--bad)}
.ptable{border-collapse:collapse; margin:6px 0 8px; font-size:.95rem} .ptable td, .ptable th{border:1px solid color-mix(in srgb, var(--line) 70%, var(--fg)); padding:3px 10px; text-align:center} .ptable th{background:var(--bg)}
.prompt{white-space:normal}
</style>

<header class="top"><div class="wrap">
<h1>Exam 2 Study Hub — Chapters 4–6</h1>
<p class="sub">Exam tomorrow 1:00 PM. Plan → learn → practice → full exams. Progress saves in this browser.</p>
<nav class="tabs" role="tablist">
<button role="tab" aria-selected="true" data-tab="plan">Plan</button>
<button role="tab" aria-selected="false" data-tab="learn">Learn</button>
<button role="tab" aria-selected="false" data-tab="mini">Quizzes</button>
<button role="tab" aria-selected="false" data-tab="exam">Full exams</button>
<button role="tab" aria-selected="false" data-tab="explained">Practice exam explained</button>
<button role="tab" aria-selected="false" data-tab="ref">Formulas</button>
<button role="tab" aria-selected="false" data-tab="mirror">Mirror exam</button>
<button role="tab" aria-selected="false" data-tab="drill">50 drill</button>
</nav></div></header>

<main class="wrap">

<!-- ================= PLAN ================= -->
<section class="view" id="view-plan">
<h2>How long will this take?</h2>
<p>From zero, this material takes most people about <b>8–12 focused hours</b> to pass solidly and <b>15–20</b> to feel confident. Everything on this exam is a recipe: the same seven question types as the practice exam, with different numbers. You don't need to understand statistics deeply — you need to recognize the question type and run the steps.</p>
<div class="note"><b>Exam: tomorrow, 1:00 PM.</b> You have tonight and tomorrow morning — about 8 hours if you use both. That is enough. Bring your <b>physical UCF ID card</b> (the exam is not graded without it), a calculator, and the cheat sheet. Show every step; round probabilities to 4 decimals.</div>

<h2>Example-first track — tonight, about 4 hours (recommended)</h2>
<p class="small">Start from the worked exam instead of the lessons. For each question: read it on the <b>Practice exam explained</b> tab, close it, redo it from the question alone, then do the matching quiz items. Open a lesson only if an explanation doesn't click.</p>
<div class="bar"><i id="bar-ex"></i></div>
<ol class="plan" data-plan="ex">
<li><input type="checkbox" id="e1"><label for="e1"><b>Lesson 0 only</b> — the symbols key and "how to read a question." <span class="t">10 min</span></label></li>
<li><input type="checkbox" id="e2"><label for="e2"><b>Explained Q1</b> (two-way table: or / and / given) → redo it cold → <b>Quiz 2, Q5</b>. <span class="t">30 min</span></label></li>
<li><input type="checkbox" id="e3"><label for="e3"><b>Explained Q2 and Q3</b> (valid? then distribution, mean, SD) → redo cold → <b>Quiz 4, Q2–Q3</b>. <span class="t">40 min</span></label></li>
<li><input type="checkbox" id="e4"><label for="e4"><b>Explained Q4</b> (binomial, all four parts) → redo cold → <b>Quiz 5, Q4</b>. <span class="t">40 min</span></label></li>
<li><input type="checkbox" id="e5"><label for="e5"><b>Break.</b> <span class="t">10 min</span></label></li>
<li><input type="checkbox" id="e6"><label for="e6"><b>Explained Q5 and Q6</b> (uniform; z-table left / between / in context) → redo cold → <b>Quiz 6, Q1, Q3, Q4</b>. <span class="t">45 min</span></label></li>
<li><input type="checkbox" id="e7"><label for="e7"><b>Explained Q7</b> (above / below / between / 98th percentile) → redo cold → <b>Quiz 7, Q5 then Q2</b>. <span class="t">40 min</span></label></li>
<li><input type="checkbox" id="e8"><label for="e8"><b>Quick pass:</b> Quiz 2 Q1–Q3 (and / at least one) and Quiz 3 Q5 (permutation vs combination) — these appear inside other questions. <span class="t">20 min</span></label></li>
<li><input type="checkbox" id="e9"><label for="e9"><b>Sleep 7+ hours.</b> Tomorrow morning's track (below) is the timed practice. <span class="t">—</span></label></li>
</ol>

<h2>Lesson-first track — tonight, about 4½ hours (alternative)</h2>
<p class="small">Ordered by points on the exam. Do the lesson, then its quiz. Check the box when the quiz is done.</p>
<div class="bar"><i id="bar-crash"></i></div>
<ol class="plan" data-plan="crash">
<li><input type="checkbox" id="c1"><label for="c1"><b>Lesson 0 — how to read a question + the symbols.</b> <span class="t">15 min</span></label></li>
<li><input type="checkbox" id="c2"><label for="c2"><b>Lesson 6 — uniform and normal (z, the table, left/right/between)</b>, then Quiz 6. This is the biggest block on the exam (Q5 + Q6 = 11 pts, plus most of Q7). <span class="t">60 min</span></label></li>
<li><input type="checkbox" id="c3"><label for="c3"><b>Lesson 7 — backwards (percentiles, top 10%, middle 80%)</b>, then Quiz 7. Finishes Q7 (8 pts). <span class="t">40 min</span></label></li>
<li><input type="checkbox" id="c4"><label for="c4"><b>Break.</b> Walk, water, 10 minutes. <span class="t">10 min</span></label></li>
<li><input type="checkbox" id="c5"><label for="c5"><b>Lesson 5 — binomial</b>, then Quiz 5. Q4 (8 pts). <span class="t">45 min</span></label></li>
<li><input type="checkbox" id="c6"><label for="c6"><b>Lesson 4 — distributions: valid? mean, SD</b>, then Quiz 4. Q2 + Q3 (10 pts). <span class="t">40 min</span></label></li>
<li><input type="checkbox" id="c7"><label for="c7"><b>Lesson 2 — two-way tables, AND / GIVEN / at least one</b>, then Quiz 2. Q1 (6 pts). <span class="t">35 min</span></label></li>
<li><input type="checkbox" id="c8"><label for="c8"><b>Lessons 1 and 3 — OR/NOT rules and counting</b>, then Quiz 1 Q5–Q6 and Quiz 3 Q5. <span class="t">25 min</span></label></li>
<li><input type="checkbox" id="c9"><label for="c9"><b>Sleep.</b> At least 7 hours. A rested brain recalls recipes; a tired one doesn't. One more hour tonight is worth less than the sleep. <span class="t">—</span></label></li>
</ol>

<h2>Tomorrow morning — about 3½ hours (prove it under time)</h2>
<p class="small">Finish by noon. Eat. Leave early.</p>
<div class="bar"><i id="bar-full"></i></div>
<ol class="plan" data-plan="full">
<li><input type="checkbox" id="f1"><label for="f1"><b>Re-read the cheat sheet</b> start to finish, slowly. <span class="t">15 min</span></label></li>
<li><input type="checkbox" id="f2"><label for="f2"><b>Official practice exam, timed 50 minutes</b> — cheat sheet and calculator only, no lessons, no solutions. Write every step as if it were graded. <span class="t">50 min</span></label></li>
<li><input type="checkbox" id="f3"><label for="f3"><b>Grade it.</b> Read the matching part on the <b>Practice exam explained</b> tab for anything you missed, then redo two questions of that type from its quiz. <span class="t">35 min</span></label></li>
<li><input type="checkbox" id="f4"><label for="f4"><b>Mirror exam, timed 50 minutes.</b> Same rules. <span class="t">50 min</span></label></li>
<li><input type="checkbox" id="f5"><label for="f5"><b>Grade it; read every solution you missed</b> line by line. Skim Lesson 8 (Exam 1 skills) if any of mean/SD/z felt shaky. <span class="t">30 min</span></label></li>
<li><input type="checkbox" id="f6"><label for="f6"><b>Pack:</b> physical UCF ID card, calculator (fresh batteries), the cheat sheet, pencils. Read "Don't lose points" on the Formulas tab one last time. <span class="t">10 min</span></label></li>
</ol>

<h2>If you only have 3 hours total</h2>
<p>Do tonight's items 1, 2, 3, 5 and 6 (symbols, normal both directions, binomial, distributions) and tomorrow's item 2 (the official practice exam timed). That covers about 37 of the 50 points.</p>

<h2>How to use a practice question</h2>
<ol>
<li>Cover the answer. Write the formula first, then plug in, then arithmetic, then box the answer — exactly like the exam wants.</li>
<li>Press <b>Show answer</b>. Compare your work line by line, not just the final number.</li>
<li>Press <b>Got it</b> or <b>Missed it</b>. Missed ones are the ones to redo tomorrow.</li>
</ol>
</section>

<!-- ================= LEARN ================= -->
<section class="view" id="view-learn" hidden>
<h2>Lessons — plain English first, formula second, example third</h2>
<p class="small">Blue = what it means. Red = the rule. Green = a worked example. Each lesson is 10–20 minutes.</p>

<details class="lesson" open><summary>Lesson 0 · How to read any question (start here) <span class="t">10 min</span></summary><div>
<p class="def">Every exam question hides a keyword that tells you which recipe to run. Find the keyword before you touch the calculator.</p>
<div class="tscroll"><table class="t"><tr><th>The question says…</th><th>Run this</th></tr>
<tr><td>a table of counts and "or / and / given"</td><td>Chapter 4 rules on the two-way table (Lesson 2)</td></tr>
<tr><td>"how many ways"</td><td>counting (Lesson 3)</td></tr>
<tr><td>"at least one"</td><td>1 − P(none)</td></tr>
<tr><td>a table of x and P(x), or counts of outcomes</td><td>distribution: valid? mean = Σx·P(x), SD (Lesson 4)</td></tr>
<tr><td>n trials, probability p, "how many successes"</td><td>binomial (Lesson 5)</td></tr>
<tr><td>"uniformly distributed between a and b"</td><td>rectangle: fraction of the width (Lesson 6)</td></tr>
<tr><td>"normally distributed, mean μ, SD σ"</td><td>z = (x − μ)/σ → table → left / right / between (Lesson 6)</td></tr>
<tr><td>"what value is the __th percentile / top 10%"</td><td>backwards: area → z → x = μ + zσ (Lesson 7)</td></tr></table></div>
<h3>The symbols</h3>
<ul>
<li><b>Σ</b> "sigma" (big) <span class="def">— add them all up.</span></li>
<li><b>N / n</b> <span class="def">— how many values: N = everyone (population), n = a sample.</span></li>
<li><b>μ "mu" / x̄ "x-bar"</b> <span class="def">— the mean: μ population, x̄ sample.</span></li>
<li><b>σ "sigma" / s</b> <span class="def">— standard deviation: σ population, s sample. σ², s² = variance = SD squared.</span></li>
<li><b>z</b> <span class="def">— how many SDs a value is above (+) or below (−) the mean.</span></li>
<li><b>P(E)</b> <span class="def">— probability of event E, from 0 to 1. E<sup>c</sup> = "not E". P(F | E) = probability of F <i>given</i> E happened.</span></li>
<li><b>X / x</b> <span class="def">— X = the random variable (the number the experiment produces), x = one specific value. P(x) = probability X equals x.</span></li>
<li><b>μ<sub>X</sub>, σ<sub>X</sub>, E(X)</b> <span class="def">— mean and SD of a random variable; E(X) = expected value = the same as μ<sub>X</sub>.</span></li>
<li><b>n, p</b> <span class="def">— binomial: number of trials and probability of success on one trial.</span></li>
<li><b><sub>n</sub>C<sub>r</sub>, <sub>n</sub>P<sub>r</sub>, n!</b> <span class="def">— combinations, permutations, factorial.</span></li>
</ul>
<p class="def">Rule of thumb: Greek letters and capital N = the whole population; plain letters and small n = a sample.</p>
</div></details>

<details class="lesson"><summary>Lesson 1 · What probability is; the OR and NOT rules <span class="t">20 min</span></summary><div>
<p class="def"><b>Probability</b> is the long-run fraction of times something happens. Flip a fair coin a million times, about half are heads, so P(heads) = 0.5. It is always between 0 (impossible) and 1 (certain), and all the possible outcomes together add to 1. Below 0.05 counts as "unusual."</p>
<p class="def">The <b>sample space</b> is the list of everything that could happen. An <b>event</b> is any part of that list.</p>
<p class="def">Three ways to get a probability: <b>classical</b> (every outcome equally likely — dice, cards, coins: just count), <b>empirical</b> (from data: how often it happened ÷ total), <b>subjective</b> (an educated guess when there is no data).</p>
<span class="rule">Classical: P(E) = N(E) ÷ N(S)     Empirical: P(E) ≈ frequency ÷ total
NOT: P(not E) = 1 − P(E)
OR:  P(E or F) = P(E) + P(F) − P(E and F)   (disjoint → the overlap is 0, just add)</span>
<p class="def">Why you subtract in OR: adding P(E) + P(F) counts the overlap twice, so take it out once. <b>Disjoint</b> (mutually exclusive) means they can't both happen. Careful: disjoint is <i>not</i> the same as independent — disjoint events are dependent, because knowing one happened tells you the other didn't.</p>
<span class="ex">Two coin flips: S = {HH, HT, TH, TT}. P(two heads) = 1/4 = 0.25. P(at least one tail) = 3/4 = 0.75.
One card: P(king or diamond) = 4/52 + 13/52 − 1/52 = 16/52 = 0.3077 (the king of diamonds was counted twice).
52% played the lottery → P(has not) = 1 − 0.52 = 0.48.
Is {A 0.40, B 0.20} a valid model? No: 0.40 + 0.20 = 0.60 ≠ 1.</span>
<p><a class="b primary" href="#mini" data-quiz="mini1" style="display:inline-block;text-decoration:none">Take Quiz 1 for this lesson →</a></p>
</div></details>

<details class="lesson"><summary>Lesson 2 · AND, GIVEN, independence, "at least one", two-way tables <span class="t">30 min</span></summary><div>
<p class="def"><b>Independent</b> means one event happening doesn't change the probability of the other (two coin flips; two different drivers). Then P(both) is just the product.</p>
<p class="def"><b>Given</b> (conditional probability) means you already know something. Knowing E shrinks your world to only the cases where E happened, so you divide by E's total instead of the grand total. P(roll a 6) = 1/6, but P(6 | the roll was even) = 1/3, because only {2, 4, 6} remain.</p>
<span class="rule">AND (independent):  P(E and F) = P(E) · P(F)
AND (general):      P(E and F) = P(E) · P(F | E)
GIVEN:              P(F | E) = P(E and F) ÷ P(E) = N(E and F) ÷ N(E)
AT LEAST ONE:       P(at least 1) = 1 − P(none)
Independent?        check whether P(F | E) = P(F). Equal → independent. Different → dependent.</span>
<p class="def">"At least one" has many cases (one, two, three…), so compute the one case you don't want — none — and subtract from 1.</p>
<h3>Two-way tables (exam Question 1)</h3>
<ol>
<li>Add the row totals and the column totals; the grand total is N.</li>
<li>"is A" → A's total ÷ N.</li>
<li>"A <b>or</b> B" → P(A) + P(B) − P(both) — subtract the one overlapping cell.</li>
<li>"A <b>and</b> B" → that single cell ÷ N.</li>
<li>"A <b>given</b> B" → the cell ÷ B's total. Divide by the given group only.</li>
</ol>
<span class="ex">78 residents (36 men, 42 women). P(male) = 36/78 = 0.4615. P(male or unemployed) = 36/78 + 5/78 − 3/78 = 0.4872. P(female and not in labor force) = 12/78 = 0.1538. P(part-time | female) = 10/42 = 0.2381.
Speeder: P(pulled over) = 0.8, P(ticket | pulled over) = 0.9 → P(pulled over and ticket) = 0.72.
P(at least one of 1000 men dies) = 1 − 0.9986^1000 = 1 − 0.2464 = 0.7536.</span>
<p><a class="b primary" href="#mini" data-quiz="mini2" style="display:inline-block;text-decoration:none">Take Quiz 2 for this lesson →</a></p>
</div></details>

<details class="lesson"><summary>Lesson 3 · Counting <span class="t">15 min</span></summary><div>
<p class="def">A <b>sequence of choices</b> (first this, then that): multiply the number of options at each step. 3-letter codes: 26 · 26 · 26 = 17,576.</p>
<p class="def"><b>Permutation</b> = pick r of n where ORDER MATTERS (1st/2nd/3rd place, officers, arranging in a line). <b>Combination</b> = pick r of n where order DOESN'T matter (a committee, a hand of cards, a sample). Ask: if I swap two of the chosen things, is it a different outcome? Yes → permutation. No → combination.</p>
<span class="rule">n! = n(n−1)(n−2)···1,  0! = 1
ₙPᵣ = n! ÷ (n − r)!          ₙCᵣ = n! ÷ [ r! (n − r)! ]
Probability by counting: (ways to get what you want) ÷ (total ways)</span>
<span class="ex">Chair, vice-chair, secretary from 14: 14 · 13 · 12 = 2,184 (order matters).
₁₀P₃ = 10 · 9 · 8 = 720.   ₄C₂ = 4!/(2!·2!) = 6.   ₂₀C₄ = (20·19·18·17)/(4·3·2·1) = 4,845.
P(4 cards all the same rank) = 13 / ₅₂C₄ = 13/270,725 ≈ 0.00005.</span>
<p><a class="b primary" href="#mini" data-quiz="mini3" style="display:inline-block;text-decoration:none">Take Quiz 3 for this lesson →</a></p>
</div></details>

<details class="lesson"><summary>Lesson 4 · Random variables, distributions, mean and SD <span class="t">30 min</span></summary><div>
<p class="def">A <b>random variable X</b> is just "the number that comes out of a chance experiment": games in a series, profit from a bet, number of people who say yes. <b>Discrete</b> = you count it (0, 1, 2…). <b>Continuous</b> = you measure it (time, weight, temperature).</p>
<p class="def">A <b>probability distribution</b> is a table of every value X can take and its probability. It is <b>valid</b> only if every P(x) is between 0 and 1 <i>and</i> they add to exactly 1.</p>
<p class="def">The <b>mean</b> of a random variable (also called the <b>expected value</b>, E(X)) is a weighted average: each value counts as much as its probability. It is the long-run average per trial. The <b>standard deviation</b> is the typical distance from that mean, with each squared gap weighted by its probability.</p>
<span class="rule">Valid: each 0 ≤ P(x) ≤ 1  and  Σ P(x) = 1
From counts: P(x) = count ÷ total
Mean:  μ = Σ [ x · P(x) ]
SD:    σ = √( Σ [ (x − μ)² · P(x) ] )</span>
<ol>
<li>P(x) = count ÷ total for each x. Check they add to 1.</li>
<li>Mean: multiply each x by its P(x), add.</li>
<li>SD: for each x, (x − μ)², times P(x); add them up; square root.</li>
<li>Graph: a vertical line or bar above each x, height P(x).</li>
</ol>
<span class="ex">Stanley Cup (83 series): P(4) = 20/83 = 0.2410, P(5) = 0.2410, P(6) = 0.3133, P(7) = 0.2048.
μ = 4(0.2410) + 5(0.2410) + 6(0.3133) + 7(0.2048) = 5.48 games → a series lasts about 5.48 games on average.
σ² = 2.1904(0.2410) + 0.2304(0.2410) + 0.2704(0.3133) + 2.3104(0.2048) = 1.1413 → σ = 1.07 games.
Insurance: $100(0.9986) + (−$9,900)(0.0014) = $86 expected profit per policy → keep selling.</span>
<p><a class="b primary" href="#mini" data-quiz="mini4" style="display:inline-block;text-decoration:none">Take Quiz 4 for this lesson →</a></p>
</div></details>

<details class="lesson"><summary>Lesson 5 · Binomial <span class="t">30 min</span></summary><div>
<p class="def">A <b>binomial experiment</b> is the same yes/no trial repeated: a fixed number of trials n, each independent, each with only two outcomes (success/failure), and the same success probability p every time. X = the number of successes. It is <i>not</i> binomial if n isn't fixed ("keep going until…") or the picks are without replacement from a small group (p changes).</p>
<span class="rule">P(x) = ₙCₓ · pˣ · (1 − p)ⁿ⁻ˣ        ₙCₓ = n! ÷ [ x! (n − x)! ]
μ = n·p          σ = √( n·p·(1 − p) )
Unusual count (when np(1−p) ≥ 10): x below μ − 2σ or above μ + 2σ</span>
<p class="def">Read the formula as: (number of ways to place the x successes among the n trials) × (probability of the successes) × (probability of the failures).</p>
<div class="tscroll"><table class="t"><tr><th>Words</th><th>Compute</th></tr>
<tr><td>exactly x</td><td>P(x)</td></tr><tr><td>fewer than k / less than k</td><td>P(0) + … + P(k − 1)</td></tr>
<tr><td>at most k / no more than k</td><td>P(0) + … + P(k)</td></tr><tr><td>more than k</td><td>1 − [P(0) + … + P(k)]</td></tr>
<tr><td>at least k</td><td>1 − [P(0) + … + P(k − 1)]</td></tr><tr><td>between a and b inclusive</td><td>P(a) + … + P(b)</td></tr></table></div>
<span class="ex">60% agree, n = 10. P(exactly 3) = ₁₀C₃(0.6)³(0.4)⁷ = 120 · 0.216 · 0.0016384 = 0.0425.
Fewer than 3 = P(0) + P(1) + P(2) = 0.0001 + 0.0016 + 0.0106 = 0.0123.
n = 200: μ = 200(0.6) = 120, σ = √(200 · 0.6 · 0.4) = √48 = 6.93. Would 130 be unusual? 120 ± 2(6.93) = 106.1 to 133.9 → no.</span>
<p><a class="b primary" href="#mini" data-quiz="mini5" style="display:inline-block;text-decoration:none">Take Quiz 5 for this lesson →</a></p>
</div></details>

<details class="lesson"><summary>Lesson 6 · Uniform and normal: area = probability, z-scores, the table <span class="t">40 min</span></summary><div>
<p class="def">A continuous variable has infinitely many values, so you can't list them. Instead, probability = <b>area under a curve</b> over an interval. The total area is 1, and the probability of one exact value is 0 (a point has no width).</p>
<h3>Uniform</h3>
<p class="def">A <b>uniform</b> distribution is a flat rectangle: every stretch of the same length is equally likely. Height = 1/(b − a) so the area is 1. The probability of an interval is its share of the total width.</p>
<span class="rule">height = 1 ÷ (b − a)       P(c ≤ X ≤ d) = (d − c) ÷ (b − a)
value with area P to its left: x = a + P·(b − a)</span>
<span class="ex">Temperature uniform on 70–100: P(75 ≤ X ≤ 85) = 10/30 = 0.3333. P(X < 80) = 10/30 = 0.3333. Coolest 20%: 70 + 0.20(30) = 76°F.</span>
<h3>Normal</h3>
<p class="def">The <b>normal</b> curve is the bell: symmetric around μ, most values near the middle, fewer far out. Every normal curve has the same shape; μ slides it, σ widens or narrows it. Properties: symmetric about μ; mean = median = mode = μ; inflection points at μ ± σ; total area 1; tails never touch the axis; the Empirical Rule holds; half the area is on each side of μ.</p>
<p class="def"><b>The trick of the chapter:</b> you can't have a table for every μ and σ, so convert your value to a z-score and use one table (Table V), which gives the area to the LEFT of z.</p>
<span class="rule">z = (x − μ) ÷ σ   (round z to 2 decimals)
LEFT of x ("less than", "below"):   table value
RIGHT of x ("more than", "above", "at least"):   1 − table value
BETWEEN x₁ and x₂:   (left of z₂) − (left of z₁)
Negative z:  left of −z = 1 − (left of +z)</span>
<ol>
<li>Draw a bell, write μ under the peak, mark the x value(s), shade what is asked.</li>
<li>z = (x − μ)/σ for each x, two decimals.</li>
<li>Table: row = first two digits (1.6), column = last digit (.07) → area to the LEFT.</li>
<li>Left → done. Right → 1 − area. Between → subtract the two lefts.</li>
</ol>
<span class="ex">IQ μ = 100, σ = 15. P(above 125): z = 25/15 = 1.67 → 0.9525 → 1 − 0.9525 = 0.0475.
P(below 90): z = −0.67 → 0.2514.
P(between 110 and 140): z = 0.67 → 0.7486 and z = 2.67 → 0.9962 → 0.9962 − 0.7486 = 0.2476.
Area between z = −0.60 and 1.45: 0.9265 − 0.2743 = 0.6522.</span>
<p><a class="b primary" href="#mini" data-quiz="mini6" style="display:inline-block;text-decoration:none">Take Quiz 6 for this lesson →</a></p>
</div></details>

<details class="lesson"><summary>Lesson 7 · Backwards: percentiles, cutoffs, middle %; is the data normal? <span class="t">25 min</span></summary><div>
<p class="def">Now the area is given and you want the value. Reverse the steps: area → z (found <i>inside</i> the table) → x = μ + zσ. The k-th percentile is the value with k% of the data below it, so the area to the left is k/100 (5th → 0.05, 98th → 0.98). "Top 10%" means the area to the left is 0.90. "Middle 80%" leaves 10% in each tail → areas 0.10 and 0.90.</p>
<span class="rule">area to the left → closest table entry → z → x = μ + z·σ
Exactly halfway between two entries → average the two z's (0.95 → 1.645, 0.995 → 2.575)</span>
<div class="tscroll"><table class="t"><tr><th>Percentile</th><th>z</th><th>Percentile</th><th>z</th></tr>
<tr><td>1st</td><td>−2.33</td><td>99th</td><td>2.33</td></tr><tr><td>2nd</td><td>−2.05</td><td>98th</td><td>2.05</td></tr>
<tr><td>2.5th</td><td>−1.96</td><td>97.5th</td><td>1.96</td></tr><tr><td>5th</td><td>−1.645</td><td>95th</td><td>1.645</td></tr>
<tr><td>10th</td><td>−1.28</td><td>90th</td><td>1.28</td></tr><tr><td>20th</td><td>−0.84</td><td>80th</td><td>0.84</td></tr>
<tr><td>25th</td><td>−0.67</td><td>75th</td><td>0.67</td></tr></table></div>
<span class="ex">98th percentile IQ: area 0.98 → closest 0.9798 → z = 2.05 → x = 100 + 2.05(15) = 130.75 ≈ 131.
Height at the 20th percentile (μ 38.72, σ 3.17): z = −0.84 → 38.72 + (−0.84)(3.17) = 36.06 in.
Middle 80% of heights: z = ±1.28 → 34.66 to 42.78 in.</span>
<p class="def"><b>Interpreting an area:</b> "the area to the right of 200 is 0.29" means both that 29% of the population is above 200 and that a randomly chosen person has a 0.29 chance of being above 200.</p>
<p class="def"><b>Is the data normal?</b> Histogram: bell-shaped, one peak, roughly symmetric, few outliers. Normal probability plot: points close to a straight line.</p>
<p><a class="b primary" href="#mini" data-quiz="mini7" style="display:inline-block;text-decoration:none">Take Quiz 7 for this lesson →</a></p>
</div></details>

<details class="lesson"><summary>Lesson 8 · Exam 1 skills that come back (mean, SD, z, Empirical Rule, quartiles) <span class="t">20 min</span></summary><div>
<p class="def"><b>Mean</b> = add everything, divide by how many. <b>Median</b> = sort, take the middle (average the two middles if the count is even); resistant to outliers, the mean is not. <b>Mode</b> = most frequent value(s); none if nothing repeats.</p>
<p class="def"><b>Standard deviation</b> = on average, how far values are from the mean. Why the recipe: the gaps (x − mean) always add to 0, so square them (all positive), average the squares (that is the variance), then take the square root to get back to normal units (that is the SD). The one trap: the word <b>sample</b> means divide by n − 1. Your calculator shows both: σx = population, Sx = sample.</p>
<span class="rule">σ² = Σ(x − μ)² ÷ N   (population)      s² = Σ(x − x̄)² ÷ (n − 1)   (sample)      SD = √variance
z = (x − μ) ÷ σ   — bigger z = relatively higher (if lower is better, the smaller z did better); beyond ±2 = unusual
Empirical Rule (bell-shaped): 68% within 1σ, 95% within 2σ, 99.7% within 3σ; pieces 34 | 13.5 | 2.35 | 0.15 each side
Quartiles: Q₂ = median; Q₁/Q₃ = medians of the halves (odd n → leave the median out). IQR = Q₃ − Q₁; fences Q₁ − 1.5·IQR and Q₃ + 1.5·IQR; outside = outlier</span>
<span class="ex">Sample 18, 22, 25, 28, 30: x̄ = 123/5 = 24.6; squares 43.56 + 6.76 + 0.16 + 11.56 + 29.16 = 91.20; s² = 91.20/4 = 22.8; s = 4.77.
ACT 27 (μ 18, σ 6): z = 1.50 beats SAT 1200 (μ 1000, σ 200): z = 1.00.
μ = 29.8, σ = 6.4: 95% of values between 29.8 ± 12.8 = 17.0 and 42.6.</span>
<p><a class="b primary" href="#mini" data-quiz="mini0" style="display:inline-block;text-decoration:none">Take Quiz 8 for this lesson →</a></p>
</div></details>
</section>

<!-- ================= MINI TESTS ================= -->
<section class="view" id="view-mini" hidden>
<h2>Quizzes — one per lesson</h2>
<p class="small">Quiz 1 goes with Lesson 1, Quiz 2 with Lesson 2, and so on (Quiz 8 is the Exam 1 refresher, Lesson 8). Do each quiz right after its lesson. Work the part on paper, type the final answer, press <b>Check answer</b>; parts that ask for words or a sketch use <b>Show answer</b> and your own honest Got it / Missed it.</p>
<div id="mini-root"></div>
</section>

<!-- ================= FULL EXAMS ================= -->
<section class="view" id="view-exam" hidden>
<h2>Full exams — 50 points, 50 minutes each</h2>
<p class="small">Press <b>Start 50 min</b>, use only the cheat sheet and a calculator, type each final answer and press <b>Check answer</b>. Read the full solution for every part you miss.</p>
<div id="exam-root"></div>
</section>

__EXPLAINED__

<!-- ================= FORMULAS ================= -->
<section class="view" id="view-ref" hidden>
<h2>Formula card</h2>
<p class="small">The same rules as the cheat sheet, in one place.</p>
<span class="rule">NOT   P(Eᶜ) = 1 − P(E)
OR    P(E or F) = P(E) + P(F) − P(E and F)        disjoint → just add
AND   independent: P(E)·P(F)        general: P(E)·P(F | E)
GIVEN P(F | E) = P(E and F) ÷ P(E) = N(E and F) ÷ N(E)
AT LEAST ONE   1 − P(none)
Counting   sequence: multiply    ₙPᵣ = n!/(n−r)!  (order)    ₙCᵣ = n!/[r!(n−r)!]  (no order)</span>
<span class="rule">Discrete RV   valid: each 0–1 and Σ P(x) = 1
μ = Σ x·P(x)        σ = √( Σ (x − μ)²·P(x) )
Binomial   P(x) = ₙCₓ pˣ (1−p)ⁿ⁻ˣ      μ = np      σ = √(np(1−p))</span>
<span class="rule">Uniform [a,b]   height 1/(b−a)      P(c ≤ X ≤ d) = (d − c)/(b − a)      x = a + P·(b − a)
Normal   z = (x − μ)/σ  (2 decimals)   table = area to the LEFT
   left: table    right: 1 − table    between: left(z₂) − left(z₁)    negative z: 1 − (positive entry)
Backwards   area → z (inside the table) → x = μ + zσ
   1.28 ↔ 90%/10%   1.645 ↔ 95%/5%   1.96 ↔ 97.5%/2.5%   2.05 ↔ 98%   2.33 ↔ 99%</span>
<span class="rule">Exam 1   x̄ = Σx/n     s² = Σ(x − x̄)²/(n−1)     σ² = Σ(x − μ)²/N     z = (x − μ)/σ
Empirical Rule 68 / 95 / 99.7     IQR = Q₃ − Q₁, fences Q₁ − 1.5·IQR, Q₃ + 1.5·IQR</span>
<h3>Don't lose points</h3>
<ul>
<li>"Or" → subtract the overlap once. "And" → the one cell. "Given" → divide by the given group.</li>
<li>Check Σ P(x) = 1 before calling a distribution valid.</li>
<li>Binomial σ needs the square root. "Fewer than 3" stops at 2; "at least 3" = 1 − P(≤ 2).</li>
<li>Uniform: length ÷ width, never z. Normal: always z first, two decimals, table = left.</li>
<li>"Above" → 1 − left. "Between" → big minus small. Percentile → area → z → x = μ + zσ.</li>
<li>Round probabilities to 4 decimals and write the formula every time.</li>
</ul>
</section>

<!-- ================= MIRROR EXAM ================= -->
<section class="view" id="view-mirror" hidden>
<h2>Mirror exam — models the practice exam, switched up</h2>
<p class="small">Same seven question types and point values as the official practice exam, in the same order, with new numbers and a few twists (it is the same exam as the Mirror Exam PDF). Start the timer, work each part on paper with only the cheat sheet and a calculator, type the final answer, and press <b>Check answer</b>. A wrong answer opens the worked solution; a right one lets you move on. The z-hints are printed in each question, as they will be on the real exam.</p>
<div class="tscroll"><table class="t"><tr><th>#</th><th>Type</th><th>What's switched</th></tr>
<tr><td>1</td><td>Two-way table</td><td>"given" conditions on the column variable instead of the row</td></tr>
<tr><td>2</td><td>Valid distribution?</td><td>sums to more than 1 instead of less</td></tr>
<tr><td>3</td><td>Distribution, mean, SD</td><td>x starts at 0; counts that do not divide evenly, so you must round</td></tr>
<tr><td>4</td><td>Binomial</td><td>"at most" and "at least 1" instead of "fewer than" / "between"</td></tr>
<tr><td>5</td><td>Uniform</td><td>a "more than" question instead of "below"</td></tr>
<tr><td>6</td><td>z areas from hints</td><td>left of a negative z; both-negative between; right tail in context</td></tr>
<tr><td>7</td><td>Normal in context</td><td>a LOW percentile (negative z)</td></tr></table></div>
<div id="mirror-root"></div>
</section>

<!-- ================= 50 DRILL ================= -->
<section class="view" id="view-drill" hidden>
<h2>50-question drill — every type, new numbers</h2>
<p class="small">Fifty random questions mixed across all seven types (table, valid?, discrete, binomial, uniform, z, normal). Each one stands alone. Solve on paper with only the cheat sheet and calculator, type the answer, press <b>Check answer</b>. Wrong → the worked solution opens. Probabilities to 4 decimals; μ, σ to 2; x values to 1 decimal. z hints are printed in the question like the real exam.</p>
<div id="drill-root"></div>
</section>
</main>

<script id="data" type="application/json">__DATA__</script>
<script>
(function(){
  var DATA = JSON.parse(document.getElementById('data').textContent);
  function store(k, v){ try{ if(v===undefined){ return localStorage.getItem(k); } localStorage.setItem(k, v); }catch(e){ return null; } }
  function esc(s){ return String(s==null?'':s).replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }

  /* tabs */
  var tabs = document.querySelectorAll('nav.tabs button');
  function show(name){
    tabs.forEach(function(b){ b.setAttribute('aria-selected', b.dataset.tab===name ? 'true':'false'); });
    document.querySelectorAll('section.view').forEach(function(s){ s.hidden = (s.id !== 'view-'+name); });
    store('tab', name);
    window.scrollTo({top:0});
  }
  tabs.forEach(function(b){ b.addEventListener('click', function(){ show(b.dataset.tab); }); });
  var h = (location.hash||'').replace('#',''); var saved = store('tab');
  show(['plan','learn','mini','exam','explained','ref','mirror','drill'].indexOf(h)>=0 ? h : (saved || 'plan'));
  window.addEventListener('hashchange', function(){ var x=(location.hash||'').replace('#',''); if(['plan','learn','mini','exam','explained','ref','mirror','drill'].indexOf(x)>=0) show(x); });

  /* plan checkboxes */
  document.querySelectorAll('ol.plan').forEach(function(ol){
    var key = 'plan-'+ol.dataset.plan, bar = document.getElementById('bar-'+ol.dataset.plan);
    var boxes = ol.querySelectorAll('input[type=checkbox]');
    var saved = {}; try{ saved = JSON.parse(store(key)||'{}'); }catch(e){}
    function upd(){ var n=0; boxes.forEach(function(b){ if(b.checked) n++; }); if(bar) bar.style.width = Math.round(100*n/boxes.length)+'%'; }
    boxes.forEach(function(b){ b.checked = !!saved[b.id]; b.addEventListener('change', function(){ saved[b.id]=b.checked; store(key, JSON.stringify(saved)); upd(); }); });
    upd();
  });

  /* tests */
  function numsIn(str){ var out=[]; var t=String(str||'').replace(/[−–]/g,'-'); var re=/-?\d*\.?\d+/g; var m; while((m=re.exec(t))){ var v=parseFloat(m[0]); if(!isNaN(v)) out.push(v); } return out; }
  function parseUser(str){ if(str==null) return NaN; var t=String(str).trim().replace(/[−–]/g,'-').replace(/\$/g,'').replace(/(\d),(?=\d{3}(?!\d))/g,'$1').replace(/\s+/g,'').replace(/^[≈~=]+/,'').replace(/[a-zA-Z°]+$/,''); if(!t) return NaN; var pct=/%$/.test(t); t=t.replace(/%$/,''); var v; var f=t.match(/^(-?\d*\.?\d+)\/(-?\d*\.?\d+)$/); if(f){ v=parseFloat(f[1])/parseFloat(f[2]); } else { v=parseFloat(t); } if(pct) v=v/100; return v; }
  function deriveCheck(p){
    if(p.check) return p.check;
    var a=String(p.answer||'').replace(/(\d),(\d{3})\b/g,'$1$2');
    if(/\bnot valid\b/i.test(a)) return {type:'choice', options:['Valid','Not valid'], correct:'Not valid'};
    if(/\bvalid\b/i.test(a)) return {type:'choice', options:['Valid','Not valid'], correct:'Valid'};
    if(/^\s*(not\s+binomial|binomial)\b/i.test(a)) return {type:'choice', options:['Binomial','Not binomial'], correct: /^\s*not/i.test(a)?'Not binomial':'Binomial'};
    if(/^\s*(discrete|continuous)\b/i.test(a)) return {type:'choice', options:['Discrete','Continuous'], correct: /^\s*discrete/i.test(a)?'Discrete':'Continuous'};
    if(/\bnot independent\b/i.test(a)) return {type:'choice', options:['Independent','Not independent'], correct:'Not independent'};
    if(/\bindependent\b/i.test(a) && !/\bdependent\b/i.test(a.replace(/independent/ig,''))) return {type:'choice', options:['Independent','Not independent'], correct:'Independent'};
    if(/^\s*(yes|no)\b/i.test(a) && !/\d\.\d{3,4}/.test(a)) return {type:'choice', options:['Yes','No'], correct: /^\s*yes/i.test(a)?'Yes':'No'};
    if(/\b(bar|bars|sketch|rectangle|graph|axis|axes|flat line|line\/bar|lines\/bars|interpretation)\b/i.test(a)) return {type:'self'};
    var segs=a.split(/;|\sand\s/); var fields=[];
    segs.forEach(function(sg){ var ns=numsIn(sg); if(ns.length>=1){ var lab=''; var eq=sg.search(/[=≈:]/); if(eq>0){ lab=sg.slice(0,eq).trim(); if(lab.length>22) lab=''; } fields.push({label:lab, value:ns[ns.length-1]}); } });
    if(fields.length===0 || fields.length>4) return {type:'self'};
    fields.forEach(function(f){ var v=f.value; f.tol = Number.isInteger(v) ? 0.5 : (Math.abs(v)<1 ? 0.0006 : 0.011); });
    if(fields.length===1) return {type:'number', value:fields[0].value, tol:fields[0].tol, label:fields[0].label};
    return {type:'numbers', fields:fields};
  }
  function fmt(v){ return (Math.abs(v)<1 && v!==0) ? v.toFixed(4) : String(v); }
  function renderPrompt(txt){ var lines=String(txt).split('\n'); var html=''; var rows=[];
    function flush(){ if(!rows.length) return; var counts={}; rows.forEach(function(r){ counts[r.split('|').length]=1; }); if(rows.length<2 || Object.keys(counts).length>1){ rows.forEach(function(r){ html+='<div>'+esc(r)+'</div>'; }); rows=[]; return; } html+='<div class="tscroll"><table class="ptable">'+rows.map(function(r,i){ var cells=r.split('|').map(function(c){return c.trim();}); return '<tr>'+cells.map(function(c){ return i===0?'<th>'+esc(c)+'</th>':'<td>'+esc(c)+'</td>'; }).join('')+'</tr>'; }).join('')+'</table></div>'; rows=[]; }
    lines.forEach(function(ln){ if(ln.indexOf('|')>=0){ rows.push(ln); } else { flush(); if(ln.trim()) html+='<div>'+esc(ln)+'</div>'; } }); flush(); return html; }
  function renderTest(t, root, kind){
    var box = document.createElement('div'); box.id = 'quiz-'+t.key;
    var total = 0; t.questions.forEach(function(q){ q.parts.forEach(function(){ total++; }); });
    var head = document.createElement('div');
    head.innerHTML = '<h3>'+esc(t.title)+' <span class="pill" id="pill-'+t.key+'">0 / '+total+'</span></h3><p class="small">'+esc(t.intro)+'</p><div class="score" id="score-'+t.key+'"></div>';
    box.appendChild(head);
    if(kind==='big'){
      var tm = document.createElement('div'); tm.className='timer'; tm.setAttribute('role','timer');
      tm.innerHTML = '⏱ <span id="tmv-'+t.key+'">50:00</span><button class="b primary" data-act="start">Start 50 min</button><button class="b" data-act="treset">Reset timer</button>';
      head.appendChild(tm);
      var tkey='timer-'+t.key;
      function tick(){ var end=parseInt(store(tkey)||'0',10); var v=document.getElementById('tmv-'+t.key); if(!v) return; if(!end){ v.textContent='50:00'; tm.classList.remove('over'); return; } var rem=Math.round((end-Date.now())/1000); if(rem<=0){ v.textContent='Time!'; tm.classList.add('over'); return; } tm.classList.remove('over'); var m=Math.floor(rem/60), sc=rem%60; v.textContent=(m<10?'0':'')+m+':'+(sc<10?'0':'')+sc; }
      tm.addEventListener('click', function(ev){ var b=ev.target.closest('button'); if(!b) return; if(b.dataset.act==='start'){ store(tkey, String(Date.now()+50*60*1000)); } else { store(tkey, '0'); } tick(); });
      setInterval(tick, 1000); box._tick = tick;
    }
    var state = {}; try{ state = JSON.parse(store('test-'+t.key)||'{}'); }catch(e){}
    function save(){ store('test-'+t.key, JSON.stringify(state)); var got=0, missed=0; Object.keys(state).forEach(function(k){ if(state[k]==='ok') got++; else if(state[k]==='bad') missed++; }); document.getElementById('pill-'+t.key).textContent = got+' / '+total; document.getElementById('score-'+t.key).textContent = got+' right, '+missed+' missed, '+(total-got-missed)+' not yet checked'; }
    t.questions.forEach(function(q, qi){
      var qd = document.createElement('div'); qd.className='q';
      var ptxt = q.prompt ? '<div class="prompt">'+renderPrompt(q.prompt)+'</div>' : '';
      qd.innerHTML = '<span class="pts">Question '+(qi+1)+(q.points?' · '+q.points+' pts':'')+'</span>'+ptxt;
      q.parts.forEach(function(p, pi){
        var id = t.key+'-'+qi+'-'+pi; var chk = deriveCheck(p);
        var pd = document.createElement('div'); pd.className='part';
        var ctl='';
        var flds = chk.type==='number' ? [{label:chk.label, value:chk.value}] : (chk.type==='numbers' ? chk.fields : []);
        var im = flds.every(function(f){ return f.value>=0; }) ? ' inputmode="decimal"' : ' inputmode="text"';
        var inputsHtml = flds.map(function(f,i){ var lab = f.label || (flds.length>1 ? 'value '+(i+1) : ''); return (lab?'<label for="in-'+id+'-'+i+'">'+esc(lab)+' =</label>':'')+'<input class="inp"'+im+' enterkeyhint="go" autocomplete="off" placeholder="your answer" id="in-'+id+'-'+i+'" aria-label="'+esc(lab||'your answer')+'">'; }).join('');
        if(chk.type==='number' || chk.type==='numbers'){ ctl='<div class="chkrow"><div class="fields'+(flds.some(function(f){return f.label;})||flds.length>1?' labeled':'')+'">'+inputsHtml+'</div><div class="btns"><button class="b primary" data-act="check">Check answer</button><button class="b" data-act="show">Show solution</button></div></div>'; }
        else if(chk.type==='choice'){ ctl='<div class="chkrow">'+chk.options.map(function(o){ return '<button class="b choice" data-act="choose" data-val="'+esc(o)+'" aria-pressed="false">'+esc(o)+'</button>'; }).join('')+'<button class="b" data-act="show">Show solution</button></div>'; }
        else { ctl='<div class="btns"><button class="b primary" data-act="show">Show answer</button><button class="b ok" data-act="ok" aria-pressed="'+(state[id]==='ok')+'">Got it</button><button class="b bad" data-act="bad" aria-pressed="'+(state[id]==='bad')+'">Missed it</button></div>'; }
        pd.innerHTML = '<p class="qt"><span class="lab">'+esc(p.label)+'</span>'+esc(p.question)+'</p>' + ctl + '<div class="fb" id="fb-'+id+'"></div>'
          + '<div class="ans" hidden id="ans-'+id+'"><div class="final">Answer: '+esc(p.answer)+'</div><pre>'+esc(p.solution)+'</pre></div>';
        var fb = pd.querySelector('#fb-'+CSS.escape(id));
        if(chk.type!=='self' && state[id]==='ok'){ fb.className='fb ok'; fb.textContent='✓ Checked earlier: correct'; }
        if(chk.type!=='self' && state[id]==='bad'){ fb.className='fb bad'; fb.textContent='✗ Checked earlier: missed — try again'; }
        function setResult(ok, correctText){ state[id]= ok?'ok':'bad'; fb.className='fb '+(ok?'ok':'bad'); fb.textContent = ok ? '✓ Correct' : ('✗ Not quite — correct: '+correctText+'. Read the solution, then redo it on paper.'); var a=pd.querySelector('.ans'); if(!ok){ a.hidden=false; pd.querySelector('[data-act=show]').textContent='Hide solution'; } save(); }
        pd.addEventListener('click', function(ev){
          var b = ev.target.closest('button'); if(!b) return; var act=b.dataset.act;
          if(act==='show'){ var a=pd.querySelector('.ans'); a.hidden=!a.hidden; b.textContent = a.hidden ? (chk.type==='self'?'Show answer':'Show solution') : (chk.type==='self'?'Hide answer':'Hide solution'); }
          else if(act==='check'){
            var fields = chk.type==='number' ? [{value:chk.value, tol:chk.tol}] : chk.fields; var allok=true, any=false;
            fields.forEach(function(f,i){ var inp=pd.querySelector('#in-'+CSS.escape(id+'-'+i)); var v=parseUser(inp.value); if(inp.value.trim()) any=true; var ok = !isNaN(v) && (Math.abs(v-f.value)<=f.tol || (/%\s*$/.test(inp.value) && Math.abs(v*100-f.value)<=f.tol)); inp.className='inp '+(ok?'good':'wrong'); if(!ok) allok=false; });
            if(!any){ fb.className='fb bad'; fb.textContent='Type your answer first.'; return; }
            setResult(allok, fields.map(function(f){ return (f.label? f.label+' = ' : '') + fmt(f.value); }).join(', '));
          }
          else if(act==='choose'){ pd.querySelectorAll('[data-act=choose]').forEach(function(x){ x.setAttribute('aria-pressed', x===b); }); setResult(b.dataset.val===chk.correct, chk.correct); }
          else { state[id] = (state[id]===act) ? '' : act; pd.querySelector('[data-act=ok]').setAttribute('aria-pressed', state[id]==='ok'); pd.querySelector('[data-act=bad]').setAttribute('aria-pressed', state[id]==='bad'); save(); }
        });
        pd.addEventListener('keydown', function(ev){ if(ev.key==='Enter' && ev.target.classList.contains('inp')){ ev.preventDefault(); var cb=pd.querySelector('[data-act=check]'); if(cb) cb.click(); } });
        qd.appendChild(pd);
      });
      box.appendChild(qd);
    });
    var tools = document.createElement('div'); tools.className='btns'; tools.style.margin='0 0 28px';
    tools.innerHTML = '<button class="b" data-act="all">Show all solutions</button><button class="b" data-act="reset">Reset this test</button>';
    tools.addEventListener('click', function(ev){ var b=ev.target.closest('button'); if(!b) return;
      if(b.dataset.act==='all'){ var any=false; box.querySelectorAll('.ans').forEach(function(a){ if(a.hidden) any=true; }); box.querySelectorAll('.ans').forEach(function(a){ a.hidden=!any; }); b.textContent = any?'Hide all solutions':'Show all solutions'; }
      else { state={}; save(); box.querySelectorAll('[aria-pressed]').forEach(function(x){ x.setAttribute('aria-pressed','false'); }); box.querySelectorAll('.inp').forEach(function(x){ x.value=''; x.className='inp'; }); box.querySelectorAll('.fb').forEach(function(x){ x.className='fb'; x.textContent=''; }); box.querySelectorAll('.ans').forEach(function(a){ a.hidden=true; }); }
    });
    box.appendChild(tools);
    root.appendChild(box);
    save(); if(box._tick) box._tick();
  }
  document.querySelectorAll('[data-quiz]').forEach(function(a){ a.addEventListener('click', function(ev){ ev.preventDefault(); show('mini'); var el=document.getElementById('quiz-'+a.dataset.quiz); if(el){ el.scrollIntoView(); } else { window.scrollTo({top:0}); } }); });
  var mr = document.getElementById('mini-root'); DATA.mini.forEach(function(t){ renderTest(t, mr, 'mini'); });
  var er = document.getElementById('exam-root'); DATA.big.forEach(function(t){ renderTest(t, er, 'big'); });
  var xr = document.getElementById('mirror-root'); (DATA.mirror||[]).forEach(function(t){ renderTest(t, xr, 'big'); });
  var dr = document.getElementById('drill-root'); (DATA.drill||[]).forEach(function(t){ renderTest(t, dr, 'mini'); });
})();
</script>
"""
EXPL = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "explained.html")).read()
open(out_path, "w").write(PAGE.replace("__EXPLAINED__", EXPL).replace("__DATA__", DATA.replace("</", "<\\/")))
print("wrote", out_path, "minis:", [t["key"] for t in mini_tests], "bigs:", [t["key"] for t in big_tests])
