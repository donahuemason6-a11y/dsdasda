# STA2023 Exam 1 Cheat Sheet — PRINT EDITION (fits 2 sides)

**★ = maps to a practice-exam question.** Every numeric answer: **formula → substitute → arithmetic → boxed answer + units**. Probabilities to 4 decimals; relative frequency as a decimal (0.3000; 2/30 = 0.0667). Percent only when asked.

---

# SIDE 1

## CH 1 – DATA COLLECTION

### 1.1 Definitions ★ (Q1)

| Term | Definition |
|---|---|
| **Statistics** | Science of collecting, organizing, summarizing, analyzing data to draw conclusions, with a measure of confidence. Exists because of **variability**. |
| **Data** | Facts/figures collected that describe characteristics of individuals. |
| **Population** | The ENTIRE group of individuals to be studied. |
| **Individual** | ONE member (person/object) of the population. |
| **Sample** | A SUBSET of the population that is actually measured. |
| **Parameter** | Numerical summary of a **P**opulation (usually unknown). |
| **Statistic** | Numerical summary of a **S**ample (computed from the data). |

Notation: population **N, μ, σ, σ², p**; sample **n, x̄, s, s², p̂**. Process: (1) identify the research objective; (2) collect data; (3) describe the data (descriptive); (4) perform inference (extend to the population + reliability).
**Q1 method:** Population = ALL of the group the sentence is about (don't add restrictions). Sample = the group actually measured (the given count). Individual = ONE member. Parameter = the same summary for the whole population (unknown → describe in words). Statistic = the number computed from the sample (the value given). A value stated for ALL (Ex 1: 0.849 of all students) IS the parameter.
Ex 2: sample of 165 US adults with high BP; drug lowered BP an average of 14 pts → Pop: all US adults with high BP. Sample: the 165. Individual: one such adult. Parameter: mean drop μ for all (unknown). Statistic: x̄ = 14.

### Types of Variables ★ (Q2) — answer all 3: (1) Qual/Quant (2) Discrete/Continuous (3) Level

- **Qualitative (categorical):** names/labels/categories; averaging is meaningless — still qualitative when coded with numbers (ZIP, ID, jersey #) or **ranked (1st, 2nd…)**. Discrete/continuous → write **"Not applicable (not quantitative)"**.
- **Quantitative:** numeric measures; adding/subtracting is meaningful. **Discrete** = COUNTED, a list of values with gaps ("number of…", "how many"). **Continuous** = MEASURED, any value in an interval (time, hours, age, weight, height, temperature, distance, grams, dollars, % grade).

| Level | Definition | Ask |
|---|---|---|
| **Nominal** | names/categories, no order | Meaningful order? NO |
| **Ordinal** | categories CAN be ordered; differences not meaningful | Order yes; equal-size differences? NO |
| **Interval** | ordered + differences meaningful, but **no true zero** (0 ≠ "none", ratios meaningless) | Differences yes; true zero? NO |
| **Ratio** | interval + **true zero** (0 = none; 20 is twice 10) | True zero? YES |

Qualitative → Nominal or Ordinal only. Quantitative → Interval or Ratio only. **Interval:** temperature °F/°C (0° ≠ no heat; 80° is not twice 40°), calendar year/dates, clock time, SAT/IQ. **Ratio:** any count, money, time, age, weight, height, distance, % grade. **Ordinal:** rankings, Likert (strongly agree…disagree), letter grade, S/M/L, star rating, class standing, education level, age (young/middle/old), generation. **Nominal:** provider, phone type, transmission, yes/no, gender, ZIP/ID.

| Variable | Q/Q | D/C | Level |
|---|---|---|---|
| Education level; Likert response; age (young/middle/old); generation | Qual | N/A | Ordinal |
| Internet provider; phone type; prepared for class (yes/no); student ID | Qual | N/A | Nominal |
| Temperature (°F or °C) ★Q2c | Quant | Continuous | Interval |
| Whole grains (g/day); income ($); algebra grade (%); age (yrs); sleep/exercise (hrs) | Quant | Continuous | Ratio |
| # vending machines; # students; # newly admitted; # pets ★Q2b | Quant | Discrete | Ratio |
| Car transmission (manual/automatic/CVT) ★Q2a | Qual | N/A | Nominal |
| Ranking of top 5 tennis players ★Q2d | Qual | N/A | Ordinal |

### 1.2 Observational vs. Experiment ★ (Q3)

- **Explanatory variable** = may explain/cause a change (input, x: screen time, the drug). **Response variable** = the measured outcome (y: GPA, blood pressure).
- **Observational study:** measures explanatory & response WITHOUT influencing either (survey, ask, record, track, compare existing groups). → **ASSOCIATION only — NO causation** (**lurking variable** = not in the study but affects the response, e.g., sleep, study habits).
- **Designed experiment:** researcher ASSIGNS treatments / controls the explanatory variable (randomly assigned, given a drug/placebo, control group). → CAN claim **CAUSATION**. **Confounding** = two explanatory variables in the study whose effects can't be separated.
- Notes: kindergartners randomly assigned to xylophone/singing/listening → **experiment** (instruction type → IQ). Music-program kids vs neighboring daycare → **observational**. 279 new mothers surveyed (PPD) → **observational**. 75 children GIVEN milk with/without xylitol, rated taste → **experiment**. Faculty/students surveyed on online instruction → **observational**. 1006 prehypertensive teens tracked for years → **observational**.
- **Census** = every individual in the population is measured. **Web scraping** = software pulls existing data from websites (not random).

### 1.3 Simple Random Sample
**SRS** of size n: every possible sample of size n is equally likely. Steps: (1) get a **frame** (list of ALL N individuals), number them 1–N; (2) generate n random numbers (table/calculator/software), skipping repeats; those individuals are the sample. Ex: 435 House members → number 1–435, generate 5 distinct random numbers. Literary Digest 1936 was NOT an SRS: frame = own readers + car + phone owners (no complete frame; poor had zero chance → undercoverage).

### 1.5 Bias ★ (Q4) — sample is not representative

| Bias | Definition | Keywords |
|---|---|---|
| **Sampling** | The TECHNIQUE favors part of the population: incomplete frame, **undercoverage**, convenience, voluntary response (call-in/online poll) | "only sent to HQ", "its own readers", "mall", "call-in" |
| **Nonresponse** | Selected individuals don't respond (can't be reached / refuse) and differ from responders | "only 20% responded", "refused", "hung up" |
| **Response** | Answers don't reflect the truth: leading/loaded wording, interviewer effect, lying, unbalanced choices, data-entry errors | "safe answers", "what management wants", "embarrassing" |

Test: WHO was asked wrong → Sampling; chosen people didn't ANSWER → Nonresponse; answers not TRUE → Response. **Nonsampling error** = the biases above (possible even in a census). **Sampling error** = natural statistic-vs-parameter difference just because a sample was used (shrinks as n grows). Literary Digest: sampling (undercoverage) + nonresponse (only 2.38 of 10 million replied). Robocalls/internet polls: undercoverage of cell-only/no-internet + voluntary response + nonresponse (hang-ups). "How satisfied?" with 3 positive choices of 4 → response bias (unbalanced wording).

## CH 2 – ORGANIZING DATA

### 2.1 Qualitative data ★ (Q5)
**Frequency** = count per category (sums to n). **Relative frequency RF = f / n** (sums to 1). **Pie degrees = RF × 360°** (sums to 360°). Conversions: f = RF × n (round to whole); missing RF = 1 − (others); missing f = n − (others); n = f/RF from any complete row; RF = degrees/360; % = RF × 100. Check every table: Σf = n, ΣRF = 1, Σ° = 360.
Ex (rehab, n = 30): Wrist RF 0.0667 → f = 0.0667 × 30 = 2.001 → **2**; Knee 0.1667 × 30 → **5**; Back 12 → 12/30 = 0.4000. Ex (Slashdot, n = 40): Sat = 40 − (5+2+2+2+4+10) = **15**; 15/40 = 0.3750 ✓.
- **Bar graph:** categories on one axis, frequency/RF on the other, gaps between bars. **Rules ★: axis starts at 0, equal bar widths, 2-D.** Construct: (1) categories on x; (2) y = f or RF from 0, even scale; (3) equal-width bars, height = f; (4) label + title. **Pareto** = bars in decreasing order. **Pie:** (1) RF; (2) ° = RF × 360; (3) draw sectors; (4) label with category + %.
- **Pie vs bar:** pie = parts of a whole; bar = comparing specific categories (angles hard to judge) or only some categories shown. **Comparing two data sets → use RELATIVE frequency, never counts** (different totals).

### 2.2 Quantitative data: histograms ★ (Q6)
**Classes** = intervals. **Lower/upper class limit** = smallest/largest value in the class (60–69 → 60, 69). **★ Class width = difference of consecutive LOWER limits** (40–49, 50–59 → 50 − 40 = **10**, NOT 49 − 40). Classes don't overlap, equal widths; **open-ended** = first has no lower limit ("< $75") or last no upper ("$300 or more"). Continuous classes 50–74.99 = 50 up to < 75 (width 25). Build classes: next lower = lower + width; upper = next lower − 1 (Ch 3 Ex 6: 55–69, 70–84, 85–99 …).
**Histogram:** bars touch; height = frequency (or RF; same shape). Reading: freq vs RF → is the y-axis counts or proportions? Most frequent class → tallest bar, answer with the interval. Count in a range → add frequencies; % → (sum ÷ total) × 100; count from an RF histogram → RF × n.
**Shape ★ (Q7):** **Symmetric** (mirror halves): **uniform** (flat) or **bell-shaped** (peak in the middle). **Skewed = named for the TAIL:** skewed **right** = long tail to the right (a few very LARGE values; mean > median); skewed **left** = tail left (a few very SMALL values; mean < median).

| Situation | Shape |
|---|---|
| Salaries/income (a few earn millions), house prices, waiting times (most short, few long), hospital stays | **Skewed right** |
| Easy exam (most high, a few very low), age at death, product lifetimes | **Skewed left** |
| Heights, weights, IQ, test scores in general | **Bell-shaped** |
| Fair die rolls, random digits, birthdays | **Uniform** |

### 2.3–2.4 Other displays; misleading graphs
**Stem-and-leaf:** stem = all digits but the last, leaf = last digit; list every stem (even empty), leaves in order, legend (5 | 6 = 56); # leaves = n. Ex 56, 60, 66, 68, 80, 82, 82, 84, 88, 90, 92, 94, 98, 98 → `5|6  6|0 6 8  7|  8|0 2 2 4 8  9|0 2 4 8 8` (skewed left). **Time-series plot:** time on x, value on y, points connected; "highest year" = highest point.
**Misleading ★:** vertical axis not starting at 0 (tax-rate 39.6% → 37% looks huge) → start at 0; unequal bar widths → equal widths; also 3-D, inverted axis, odd colors. Answer = name the flaw AND the fix.

## ★ PRACTICE EXAM KEY Q1–Q7

**Q1** (diet, 80 participants, avg drop 15): (a) Pop = all people who could follow the diet. (b) Sample = the 80 participants. (c) Individual = each participant. (d) Parameter = mean cholesterol drop for the whole population, μ (unknown). (e) Statistic = the sample mean drop, x̄ = 15 pts.
**Q2** (a) transmission → Qualitative; Not applicable; Nominal. (b) # pets → Quantitative; Discrete; Ratio (count; 0 = none). (c) temperature °F → Quantitative; Continuous; Interval (0° ≠ no temperature; 80° not twice 40°). (d) ranking top 5 → Qualitative; Not applicable; Ordinal (order, but gaps not equal).
**Q3** (screen time vs GPA survey): (a) Observational (only surveyed; nothing assigned). (b) Explanatory = daily screen time. (c) Response = GPA. (d) Causation? **No** — observational → association only (lurking: sleep, study habits). [If an experiment: researcher assigned the treatment → causation Yes.]
**Q4** (1) sent only to HQ → **Sampling bias** (undercoverage). (2) 20% respond, mostly unhappy → **Nonresponse bias**. (3) "safe" answers → **Response bias**.
**Q5** (n = 60+50+40+30+20 = 200): Sports 60/200 = **0.3000**, 0.3000 × 360° = **108°**; Movies 50/200 = **0.2500**, 90°; Shopping 0.2000 × 360° = **72°**; Reading 0.1500, 54°; Other 0.1000, 36°. Checks: RF sum = 1.0000; 108+90+72+54+36 = 360 ✓. (b) most popular = largest f → **Sports**. (c) Reading 30/200 = 0.15 → **15%**. (d) Sports or Movies = (60+50)/200 = 110/200 = 0.55 = 55% > 50% → **True**.
**Q6** (40 students): (a) 3rd class 60–69 → lower limit **60**, upper **69**. (b) width = 50 − 40 = **10**. (c) ≥ 70: 12 + 8 = 20 → 20/40 = **50%**. (d) < 60: 4 + 6 = **10**. (e) highest frequency 12 → **70–79**.
**Q7** (a) salaries, few executives earn millions → **Skewed right**. (b) heights of 10-yr-old boys → **Bell-shaped**. (c) fair die 200 times → **Uniform**. (d) waiting times, most short, few very long → **Skewed right**.

---

# SIDE 2

## CH 3 – NUMERICALLY SUMMARIZING DATA (shape, center, spread)

### 3.1 Center
**★ Mean** = sum ÷ count. Population **μ = Σx/N** (ALL members, "population mean"); sample **x̄ = Σx/n** ("a sample of…"). Ex 1: 76+80+84+86+90+92+94 = 602; μ = 602/7 = **86**; sample 76, 84, 92 → x̄ = 252/3 = 84 (different samples → different x̄).
**★ Median M** = middle of SORTED data. (1) Sort. (2) Count n. (3) n **odd** → value at position (n+1)/2; n **even** → average of positions n/2 and n/2+1. Ex: 76, 80, 84, **86**, 90, 92, 94 → M = 86; with 32 added (n = 8) → (84+86)/2 = **85**.
**Mode** = most frequent value: one mode / several ("bimodal": 7, 12, 12, 20, 20, 25 → 12 and 20) / **no mode** if nothing repeats (5, 10, 15, 20, 27, 44). Works for qualitative data.
**Resistant** = not much affected by extreme values: **median (and IQR) resistant; mean, range, SD NOT.** Ex 3: 5, 18, 23, 23, 26, 36, 43 → μ = 174/7 = 24.857, M = 23, mode 23, range 43 − 5 = **38**; add 70 → μ = 244/8 = **30.5** (+5.6), M = (23+26)/2 = **24.5** (+1.5) → median more resistant.

| **★ Shape from mean vs median** | Report |
|---|---|
| mean **<** median → **skewed LEFT** (mean pulled to the low tail) | median & IQR |
| mean **≈** median → **symmetric** | mean & SD |
| mean **>** median → **skewed RIGHT** | median & IQR |

Ex 4: mean 65 < median 75 → skewed left; $172,950 ≈ $173,000 → symmetric; 1300 > 1150 → skewed right.

### 3.2 Spread ★ (Q8, Q9)
**Range** = max − min (easy; not resistant). **Deviation** x − μ (sum = 0), so square, average, then √.

| | Population (÷N) | Sample (÷(n − 1)) |
|---|---|---|
| Variance | σ² = Σ(x − μ)²/N = [Σx² − (Σx)²/N]/N | s² = Σ(x − x̄)²/(n − 1) = [Σx² − (Σx)²/n]/(n − 1) |
| SD | σ = √σ² (calculator **σx**) | s = √s² (calculator **Sx**) |

**Deviation-table method:** (1) mean; (2) column x − mean; (3) square each; (4) add = Σ(x − mean)²; (5) ÷ N or ÷ (n − 1) = variance (units²); (6) √ = SD (data units). Check: deviations sum to 0 (≈ 0 if the mean was rounded). Full models: **Q8(b)** (population) and **Q9(b)** (sample) below.
Non-terminating mean → carry 4 decimals, or use the computational form: Ex 3 data: Σx = 174, Σx² = 25+324+529+529+676+1296+1849 = 5228; σ² = [5228 − 174²/7]/7 = [5228 − 4325.1429]/7 = 902.8571/7 = **128.98**; σ = √128.98 = **11.36**.
Ex 7 (notes, μ = 79): squares 9, 4, 121, 81, 289, 121, 25, 25, 225, 81 → Σ = 981; σ² = 981/10 = 98.1; σ = √98.1 = **9.90**. Ex 8 sample 62, 88, 77, 68: x̄ = 73.75; squares 138.0625 + 203.0625 + 10.5625 + 33.0625 = 384.75; s² = 384.75/3 = **128.25**; s = **11.32**.
"How far": (value − mean)/SD. 31 vs 25 with σ = 6 → 1 SD (typical); σ = 0.5 → 12 SDs (very unusual).

### ★ Empirical Rule (bell-shaped ONLY) (Q11)
≈ **68%** within 1σ (μ ± 1σ), ≈ **95%** within 2σ, ≈ **99.7%** within 3σ. Bands: μ→μ+1σ **34%**; +1σ→+2σ **13.5%**; +2σ→+3σ **2.35%**; beyond 3σ **0.15%** each side (mirror on the left).

```
μ-3σ    μ-2σ    μ-1σ     μ     μ+1σ    μ+2σ    μ+3σ
  |2.35%|13.5%| 34%  | 34%  |13.5%|2.35%|
```

**Method:** (1) write μ, σ (round σ to 1 decimal if the question's numbers only match a rounded σ; say which you use); (2) compute all 6 landmarks μ ± 1σ, 2σ, 3σ; (3) match the question's numbers to landmarks; (4) add the bands between.

| Question | Answer |
|---|---|
| 68% / 95% / 99.7% lie between? | μ ± 1σ / μ ± 2σ / μ ± 3σ (compute both ends) |
| between μ − kσ and μ + kσ | k = 1: 68%; k = 2: 95%; k = 3: 99.7% |
| μ to μ + 1σ (or μ − 1σ to μ) | 34% |
| μ + 1σ to μ + 2σ (or −2σ to −1σ) | (95 − 68)/2 = 13.5% |
| μ + 2σ to μ + 3σ | (99.7 − 95)/2 = 2.35% |
| μ + 1σ to μ + 3σ | 13.5 + 2.35 = 15.85% |
| above μ + 1σ (or below μ − 1σ) | 50 − 34 = 16% |
| above μ + 2σ (or below μ − 2σ) | (100 − 95)/2 = 2.5% |
| outside μ ± 2σ (both tails) | 100 − 95 = 5% |
| below μ − 3σ (or above μ + 3σ) | (100 − 99.7)/2 = 0.15% |
| above μ (or below μ) | 50% |
| μ − 1σ to μ + 2σ | 34 + 34 + 13.5 = 81.5% |
Ex 9 (waist μ = 48.5, σ = 4.8): landmarks 43.7/53.3, 38.9/58.1, 34.1/62.9. (a) 95% → 48.5 ± 9.6 → **38.9 to 58.1**. (b) 34.1 to 62.9 = ±3σ → **99.7%**. (c) 53.3 to 62.9 = +1σ to +3σ → **15.85%**. Ex 10 (μ = 65, σ = 17): use the Empirical Rule IF bell-shaped; 31 to 99 = ±2σ → 95%. (Chebyshev: not tested.)

### 3.4 Position & outliers ★ (Q10)
**z-score = (x − μ)/σ** or (x − x̄)/s = # of SDs from the mean (no units; bigger z = relatively higher; usual −2 to 2). Ex 11: ACT 27: z = (27 − 18)/6 = **1.50**; SAT 1200: z = (1200 − 1000)/200 = **1.00** → ACT student relatively higher.
**kth percentile Pₖ:** k% of the data ≤ that value ("95th percentile" = at or above 95% of takers, top 5%; stricter than the 70th). Median = 50th percentile = Q₂; Q₁ = P₂₅; Q₃ = P₇₅.
**★ Quartiles:** (1) sort; (2) **Q₂ = median**; (3) **Q₁ = median of the lower half, Q₃ = median of the upper half; n odd → the median is NOT in either half**; n even → two halves of n/2. Ex 14 (n = 7): 76, 80, 84 | 86 | 90, 92, 94 → Q₁ = **80**, Q₂ = 86, Q₃ = **92**. n = 8: 32, 76, 80, 84 | 86, 90, 92, 94 → Q₁ = (76+80)/2 = **78**, Q₂ = 85, Q₃ = (90+92)/2 = **91**. Ex 15: 5, 18, 23, 23 | 26, 36, 43, 70 → 20.5, 24.5, 39.5.
**IQR = Q₃ − Q₁** (middle 50%; resistant): 92 − 80 = 12; 91 − 78 = 13; 39.5 − 20.5 = 19.
**★ Outliers:** (1) Q₁, Q₃; (2) IQR; (3) **LF = Q₁ − 1.5·IQR, UF = Q₃ + 1.5·IQR**; (4) outlier = any value **< LF or > UF**. Ex 18: 7 scores → 1.5(12) = 18; LF = 80 − 18 = 62, UF = 92 + 18 = 110 → none. 8 scores → 1.5(13) = 19.5; LF = 78 − 19.5 = **58.5**, UF = 91 + 19.5 = 110.5 → **32 < 58.5 is an outlier**. Travel times: 1.5(19) = 28.5; LF = −8, UF = 68 → **70 is an outlier**.

### 3.5 Five-number summary & boxplot ★ (Q10)
**Min, Q₁, M, Q₃, Max** (Min/Max are the actual data values even if outliers). Ex 19: 32, 78, 85, 91, 94.
**Boxplot:** (1) five-number summary + fences; (2) number line; box from Q₁ to Q₃ with a line at M; (3) **whiskers to the smallest and largest values INSIDE the fences** (not to the fences, not to outliers); (4) each outlier = **\***. Not to scale:

```
 *       |----[====|=====]---|
32      76   78   85    91  94    (32 outlier; whisker
                                   stops at 76, not 32)
```

Ex 20 (0.4, 2.2, 4.85, 9.4, 42.3): IQR = 7.2; 1.5(7.2) = 10.8; LF = −8.6, UF = **20.2** → every value > 20.2 is an outlier (42.3); right whisker ends at the largest value ≤ 20.2.
**Read shape:** median centered, equal whiskers → symmetric; median left in box, long right whisker/right outliers → **skewed right**; mirror → skewed left. **Read a five-number summary off a boxplot (Ex 21a):** Min = leftmost mark (lowest \* if any, else left whisker end); Q₁, M, Q₃ = box edges and line; Max = rightmost mark. Each of whisker / half-box / half-box / whisker holds ≈ 25% of the data. Compare two boxplots (Ex 21b): (1) center = medians; (2) spread = box (IQR) and whisker span; (3) shape/outliers; conclude which group tends higher.

## CALCULATOR (1-Var Stats) — σx = population SD (÷N); Sx = sample SD (÷(n−1)); variance = (UNROUNDED SD)²
TI-30XS/36X: [data] → values in L1 → [2nd][data] → 1-Var Stats → L1, FRQ ONE → CALC → n, x̄, Sx, σx, Q1, Med, Q3. Casio fx-991EX: MENU → Statistics → 1-Variable → values → [OPTN] → 1-Variable Calc. Casio fx-300ES PLUS: MODE → STAT → 1-VAR → values → AC → SHIFT 1 → Var → σx / sx. TI-84: STAT → Edit → L1; STAT → CALC → 1-Var Stats. Clear old data first; check n. Still write the table — the exam requires steps; quartiles by hand.

## ★ PRACTICE EXAM Q8–Q11 (commute times, POPULATION): 18, 22, 25, 28, 30, 31, 33, 35, 36, 40 (N = 10)

**Q8(a)** μ = Σx/N: 18+22+25+28+30+31+33+35+36+40 = 298 → **μ = 298/10 = 29.8 min**.
**Q8(b)** σ² = Σ(x − μ)²/N:

| x | x − μ | (x − μ)² |
|---|---|---|
| 18 | −11.8 | 139.24 |
| 22 | −7.8 | 60.84 |
| 25 | −4.8 | 23.04 |
| 28 | −1.8 | 3.24 |
| 30 | 0.2 | 0.04 |
| 31 | 1.2 | 1.44 |
| 33 | 3.2 | 10.24 |
| 35 | 5.2 | 27.04 |
| 36 | 6.2 | 38.44 |
| 40 | 10.2 | 104.04 |
| Σ | 0 ✓ | **407.60** |

**σ² = 407.60/10 = 40.76 min²; σ = √40.76 = 6.3844 ≈ 6.38 min** (calculator σx; Sx = 6.73 is the sample SD — wrong here). Check: Σx² = 9288; [9288 − 298²/10]/10 = [9288 − 8880.4]/10 = 40.76 ✓. (If called a sample: s² = 407.60/9 = 45.29; s = 6.73.)
**Q8(c)** n = 10 even → positions 5, 6 → **M = (30 + 31)/2 = 30.5 min**. **Q8(d)** no value repeats → **no mode**. **Q8(e)** mean 29.8 < median 30.5 → **skewed left (slightly)** (state the rule).
**Q9** sample 18, 22, 25, 28, 30 (n = 5): **(a)** x̄ = (18+22+25+28+30)/5 = **123/5 = 24.6 min**. **(b)** s² = Σ(x − x̄)²/(n − 1):

| x | x − x̄ | (x − x̄)² |
|---|---|---|
| 18 | −6.6 | 43.56 |
| 22 | −2.6 | 6.76 |
| 25 | 0.4 | 0.16 |
| 28 | 3.4 | 11.56 |
| 30 | 5.4 | 29.16 |
| Σ | 0 ✓ | **91.20** |

**s² = 91.20/(5 − 1) = 91.20/4 = 22.8 min²** (÷4, NOT ÷5); s = √22.8 = 4.77 if asked. Check: Σx² = 3117; [3117 − 123²/5]/4 = [3117 − 3025.8]/4 = 22.8 ✓.
**Q10(a)** n = 10 even → halves of 5: lower 18, 22, **25**, 28, 30 → Q₁ = **25**; upper 31, 33, **35**, 36, 40 → Q₃ = **35**; M = 30.5. **Five-number summary: 18, 25, 30.5, 35, 40.** **(b)** IQR = 35 − 25 = **10**. **(c)** 1.5(10) = 15 → **LF = 25 − 15 = 10; UF = 35 + 15 = 50**; 18 > 10 and 40 < 50 → **no outliers**. Boxplot (to scale, 1 char = 1 min):

```
18            25        30.5      35        40
|-------------[==========|========]---------|
Min           Q1         M        Q3       Max
```

z-score of the 40-min commute: z = (40 − 29.8)/6.38 = 10.2/6.38 = **1.60** (1.60 SDs above the mean; within ±2 → not unusual).
**Q11** μ = 29.8; σ ≈ **6.4** (the instructor rounds σ to 1 decimal: 23.4 = 29.8 − 6.4). Landmarks: 1σ → 23.4 / 36.2; 2σ (12.8) → 17.0 / 42.6; 3σ (19.2) → 10.6 / 49.0.

```
10.6   17.0   23.4   29.8   36.2   42.6   49.0
  |2.35%|13.5%| 34% | 34% |13.5%|2.35%|
```

**(a)** 95% ↔ μ ± 2σ = 29.8 ± 2(6.4) = 29.8 ± 12.8 → **17.0 to 42.6 min**. **(b)** 23.4 = μ − 1σ, 36.2 = μ + 1σ → **68%**. **(c)** 36.2 = μ + 1σ, 42.6 = μ + 2σ → (95 − 68)/2 = **13.5%**.

## ★ POINT-LOSERS
Sort before median/quartiles · "sample" → ÷(n − 1), "population/all" → ÷N · take √ for SD and write units (variance = min²) · σx vs Sx; never square a rounded SD · odd n: leave the median OUT of both halves · RF as a decimal, degrees with ° · class width = next lower − lower (not 49 − 40) · observational → no causation · skew is named for the TAIL (mean > median → right) · "no mode" / "not applicable" are real answers · whiskers end at the last value inside the fences, outliers get \*.
