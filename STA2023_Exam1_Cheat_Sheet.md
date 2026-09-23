# STA2023 Exam 1 Cheat Sheet — Chapters 1–3 (Sullivan)

**★ = maps directly to a practice-exam question (the real exam follows the same format).**
**Every numeric answer: formula → substitute → arithmetic → boxed answer with units.** Round probabilities to 4 decimals. Relative frequencies as a decimal (0.3000 / 0.30; 4 decimals when the division does not terminate: 2/30 = 0.0667). Percent only when the question says "percent".

---

# SIDE 1

## CHAPTER 1 – DATA COLLECTION

### 1.1 Statistics, Population vs. Sample ★ (PE Q1)

| Term | Definition |
|---|---|
| **Statistics** | The science of collecting, organizing, summarizing, and analyzing information (data) to draw conclusions or answer questions, AND providing a measure of confidence in those conclusions. Exists because of **variability**. |
| **Data** | The information collected: facts/figures that describe characteristics of individuals. |
| **Population** | The ENTIRE group of individuals to be studied. |
| **Individual** | ONE person or object that is a member of the population. |
| **Sample** | A SUBSET of the population that is actually measured/studied. |
| **Parameter** | A numerical summary of a **P**opulation (usually unknown). |
| **Statistic** | A numerical summary of a **S**ample (computed from the data you have). |
| Descriptive / Inferential | Descriptive = organize & summarize (tables, graphs, numbers; Ch 2–3): "the 80 participants' cholesterol dropped an average of 15 points." Inferential = extend a sample result to the population and state how reliable it is: "the diet lowers cholesterol for all who follow it." |

Process of statistics: (1) Identify the research objective (state the question, define the population). (2) Collect the data (usually a sample; badly collected data → meaningless conclusions). (3) Describe the data (descriptive statistics). (4) Perform inference (extend to the population, report reliability/confidence).

Notation: population size **N**, mean **μ**, SD **σ**, variance **σ²**, proportion **p**. Sample size **n**, mean **x̄**, SD **s**, variance **s²**, proportion **p̂**.

**How to answer a PE Q1-style question:**
1. **Population** = ALL of the group the objective sentence is ABOUT (not just the ones measured). Do not add restrictions the problem never states.
2. **Sample** = the group actually measured; look for the number ("80 participants", "random sample of 165").
3. **Individual** = ONE member of the population, singular.
4. **Parameter** = the same summary for the whole population; usually unknown → describe it in words ("the mean drop for ALL …, μ").
5. **Statistic** = the number computed from the sample = the value that IS given. Exception: a value stated for the whole population (Ex 1: 0.849 for ALL students) IS the parameter.

Ex 1: proportion of ALL campus students with a job = 0.849; a sample of 250 gives 0.864. Population: all students on campus. Sample: the 250 students. Individual: each student. Parameter: p = 0.849. Statistic: p̂ = 0.864.
Ex 2: random sample of 165 US adults with high blood pressure; after 6 months the drug lowered BP an average of 14 points. Population: all US adults with high BP. Sample: the 165. Individual: one US adult with high BP. Parameter: mean drop μ for ALL US adults with high BP (unknown). Statistic: x̄ = 14 points.

### Types of Variables ★ (PE Q2)

**Variable** = a characteristic of the individuals in the population; it varies from individual to individual.

| Type | One-line test | Examples |
|---|---|---|
| **Qualitative (categorical)** | Values are names/labels/categories; averaging them is meaningless. Still qualitative when coded with numbers (ZIP code, ID, jersey #, phone #) or ranked (1st, 2nd, …). | gender, education level, phone type, yes/no, Likert response, transmission type, ranking |
| **Quantitative** | Numerical measures; adding/subtracting gives a meaningful result. | temperature, income, number of pets, hours of sleep, grams |

| Quantitative subtype | One-line test | Tell-tale words |
|---|---|---|
| **Discrete** | Result of COUNTING; a finite or countable list of values (0, 1, 2, …); nothing possible in between. | "number of …", "how many …" |
| **Continuous** | Result of MEASURING; can take ANY value in an interval; limited only by the precision of the instrument. | time, hours, age, weight, height, distance, temperature, volume |

- If the variable is **qualitative**, write **"Not applicable (not quantitative)"** for discrete/continuous — the expected exam answer (PE Q2a).
- Income in dollars, grade as a percentage, age in years → **Continuous** (a measured amount; rounding to cents / whole years is only measurement precision). Write that reason.

### Levels of Measurement ★ (PE Q2) — applies to BOTH qualitative and quantitative variables

| Level | Definition | Question to ask |
|---|---|---|
| **Nominal** | Names, labels, or categories that CANNOT be ranked or put in a specific order. | Meaningful ORDER? No → Nominal |
| **Ordinal** | Names/labels/categories that CAN be ranked/ordered, but DIFFERENCES between values are not meaningful. | Order = yes. Meaningful (equal-size) differences? No → Ordinal |
| **Interval** | Ordinal + differences ARE meaningful (add/subtract OK), but NO true zero: 0 does not mean "none", so ratios are meaningless. | Differences = yes. Does 0 = absence? Is "twice as much" meaningful? No → Interval |
| **Ratio** | Interval + a TRUE ZERO (0 = none of the quantity); ratios meaningful (20 is twice 10). | True zero = yes → Ratio |

Decision path: **Order?** No → Nominal. Yes → **Meaningful differences?** No → Ordinal. Yes → **True zero?** No → Interval. Yes → Ratio.
Qualitative → ALWAYS Nominal or Ordinal. Quantitative → ALWAYS Interval or Ratio.
Interval usual suspects: **temperature in °F or °C** (0° is not "no heat"; 80° is not twice as hot as 40°), calendar year / year of birth / dates, time of day on a clock, SAT/IQ score, pH. Ratio: any COUNT, money, time/hours, age, weight, height, distance, grams, percent grade, speed.
**Ordinal** (Qualitative, N/A): **rankings** (1st, 2nd, …), **Likert responses** (strongly agree … strongly disagree), letter grade A–F, T-shirt size S/M/L, star rating 1–5, class standing (freshman … senior), income bracket (low/middle/high). **Nominal** (Qualitative, N/A): numbers used as labels (ZIP, ID, jersey #, phone #), gender, color, brand, yes/no, major.

Master classification table (Notes Ex 3–7, EXAMPLE page, PE Q2):

| Variable | Qual / Quant | Discrete / Continuous | Level |
|---|---|---|---|
| Education level (< HS, HS diploma, some college, bachelor's, advanced) | Qualitative | Not applicable | Ordinal |
| Today's high temperature (°F) / Temperature in Celsius / **PE Q2c** Temperature in °F on a given day | Quantitative | Continuous | Interval |
| Daily intake of whole grains (grams per day) | Quantitative | Continuous | Ratio |
| Number of vending machines at a school | Quantitative | Discrete | Ratio |
| Whether or not a student is prepared for class (yes/no) | Qualitative | Not applicable | Nominal |
| Age (in years) | Quantitative | Continuous (age is a time measurement) | Ratio |
| Age (Young, Middle, Old) | Qualitative | Not applicable | Ordinal |
| Generation (Boomer, Gen X, Millennial, Gen Z) | Qualitative | Not applicable | Ordinal (ordered by birth year) |
| Student (name / ID) | Qualitative | Not applicable | Nominal |
| Sleep (hours) / Time exercised in a day / Number of hours exercised | Quantitative | Continuous | Ratio |
| Internet provider / Phone type (iPhone, Samsung Galaxy, …) | Qualitative | Not applicable | Nominal |
| Income (in dollars) | Quantitative | Continuous (see note above) | Ratio |
| Grade earned in Algebra (as a percentage) | Quantitative | Continuous | Ratio |
| Response to "Working with numbers upsets me" (strongly agree … strongly disagree) | Qualitative | Not applicable | Ordinal |
| Number of students in a classroom / Number of newly admitted students to UCF | Quantitative | Discrete | Ratio |
| **PE Q2a** Type of car transmission (manual, automatic, CVT) | Qualitative | Not applicable | Nominal |
| **PE Q2b** Number of pets owned | Quantitative | Discrete | Ratio |
| **PE Q2d** Ranking of the top 5 tennis players | Qualitative | Not applicable | Ordinal |
| ZIP code / student ID / jersey number | Qualitative | Not applicable | Nominal |

### 1.2 Observational Studies vs. Designed Experiments ★ (PE Q3)

| Term | Definition |
|---|---|
| **Explanatory variable** | The variable that may explain or cause a change in the other (input / treatment / x): screen time, type of music instruction, the drug. |
| **Response variable** | The outcome that is measured (effect / y): GPA, IQ score, blood pressure. |
| **Observational study** | The researcher measures the explanatory and response variables WITHOUT attempting to influence either one; just observes, surveys, records, or follows. |
| **Designed experiment** | The researcher ASSIGNS individuals to groups and intentionally CONTROLS/CHANGES the explanatory variable (the treatment), then records the response for each group. |

Cue words. Observational: "surveyed", "asked", "questionnaire", "observed", "recorded", "tracked/followed over years", "compared existing groups", "correlated", "prevalence". Experiment: "randomly assigned", "given/administered a TREATMENT (drug, diet, product) by the researcher", "placebo", "control group", "the researcher set/varied …". (Being "given a survey/questionnaire" is still observational.)

**Causation rule ★:** Observational study → only **ASSOCIATION**, NEVER causation. Designed experiment → CAN claim **CAUSATION** (when well designed: control group, randomization, replication).
- **Lurking variable** (problem of observational studies): a variable NOT considered in the study that affects the response (screen time vs GPA → sleep, study habits, job hours).
- **Confounding** (problem of experiments): two explanatory variables that WERE in the study whose effects cannot be separated.

Notes studies classified (with explanatory → response, the PE Q3(b)(c) skill):

| Study | Type | Reason; explanatory → response |
|---|---|---|
| Music 1: 68 kindergartners randomly assigned to xylophone / singing / listening groups; IQ tested after 4 months | **Designed experiment** | Researcher assigned the groups (controlled the treatment). Type of music instruction → IQ score. Can claim cause. |
| Music 2: children already in an after-school music enrichment program compared with a neighboring daycare | **Observational** | Existing groups compared; nothing assigned. Participation in the music program → cognitive-ability score. Association only (lurking: family income, parent involvement). |
| 1. 279 new mothers (19–45) surveyed within the two months immediately after giving birth; unemployment, education, C-section correlated with PPD | **Observational** | Only surveyed; "correlated". Unemployment / education status / C-section → postpartum depression. |
| 2. 75 Peruvian children given milk with and without xylitol and asked to rate the taste of each | **Designed experiment** | Researchers gave the treatment (which milk each child drank). Milk with vs without xylitol → taste rating. |
| 3. 110 faculty + 627 students surveyed about difficulties during online instruction | **Observational** | Survey of past experiences; no treatment imposed. Online-instruction conditions → difficulties reported. |
| 4. 1006 adolescents with prehypertension tracked over several years | **Observational** | Only followed and recorded; nothing assigned. Health factors → development of hypertension. |

Other data collection: **Census** = a list of ALL individuals in the population together with certain characteristics of each (whole population measured; costly; can still have nonsampling error). **Web scraping (data mining)** = software automatically extracts large amounts of EXISTING data from websites; observational, no random selection → representativeness must be questioned.

### 1.3 Simple Random Sampling ★

- **Random sampling** = using CHANCE (not the researcher's judgment) to select individuals. **Simple random sample (SRS)** of size n from a population of size N: **every possible sample of size n has an equally likely chance of being selected.** The gold standard. **Frame** = a list of ALL individuals in the population. Sampling is without replacement (an individual is picked at most once).
- **Steps:** (1) Obtain a frame listing ALL N individuals; number them 1 to N. (2) Use a random number table, calculator, or software to randomly generate n numbers from 1 to N (skip repeats). The individuals with those numbers form the sample.
- Worked (House of Representatives, 435 members, choose 5): Frame = the list of all 435 members numbered 1–435. Generate 5 DIFFERENT random integers from 1 to 435 (discard repeats). The 5 members whose numbers came up attend. Every possible group of 5 had the same chance → SRS.
- Worked (why Literary Digest 1936 was NOT an SRS): There was no frame of ALL voters. The lists (own readers, registered car owners, phone users) were an incomplete frame that undercovered lower-income voters, so many voters had ZERO chance of selection and no chance mechanism was used → not every sample of voters was equally likely → not an SRS (sampling bias from undercoverage).

### 1.5 Bias in Sampling ★ (PE Q4)

Bias = the sample results are NOT representative of the population. Three sources:

| Bias | Definition | Tell-tale keywords |
|---|---|---|
| **Sampling bias** | The TECHNIQUE used to select the sample favors one part of the population over another: incomplete frame, **undercoverage** (a group left out or under-represented), convenience sample, voluntary-response (self-selected) sample such as a call-in/online poll. | "only sent to …", "only headquarters", "surveyed people at the mall", "its own readers", "left out", "call-in/online poll" |
| **Nonresponse bias** | Individuals SELECTED for the sample do not respond (cannot be contacted or refuse), and their opinions differ from those who do respond. | "only 20% responded", "refused", "did not return the survey", "could not be reached", "hung up" |
| **Response bias** | The ANSWERS given do not reflect the respondents' true feelings: interviewer influence, misrepresented answers (lying about weight, income, drug use), poorly worded / leading / loaded questions, question order, unbalanced answer choices, data-entry (keying) errors. | "safe answers", "what management wants", "leading question", "embarrassing question", "interviewer present", "lied", "mistyped" |

Quick test: **WHO got asked?** wrong/partial group → Sampling. **Did the chosen people ANSWER?** no → Nonresponse. **Are the answers TRUE?** no → Response.
- **Nonsampling error** = any error from the data-collection process: sampling bias/undercoverage, nonresponse bias, response bias, data-entry error (Sullivan files data-entry error under response bias — if forced to pick Sampling / Nonresponse / Response, answer Response). Can occur even in a **census**.
- **Sampling error** = the natural difference between a sample statistic and the population parameter simply because a SAMPLE, not the whole population, was measured. Not a mistake; shrinks as n grows; zero in a census.

| Notes scenario | Bias | Reason |
|---|---|---|
| Literary Digest 1936: 10 million polled, 2.38 million responded; predicted Landon 57.08%; Roosevelt won by 24.92 points | **Sampling bias (undercoverage) + Nonresponse bias** | Frame = own readers + car owners + phone owners → wealthier, Republican-leaning voters over-represented, the poor left out. Only 2.38/10 = 0.238 ≈ 23.8% responded, and those with strong (anti-Roosevelt) feelings were more likely to mail the ballot back. |
| Robocalls and internet polling (ICM: 3,000–4,000 calls for n = 2000 in 1995, over 30,000 today; robocalls to cell phones illegal under the TCPA) | **Nonsampling error: sampling bias (undercoverage + voluntary response) + nonresponse bias** | Cell-phone-only households cannot be robocalled and people without internet cannot take web polls → undercoverage (sampling bias). Internet polls are voluntary-response / self-selected (a convenience sample) → sampling bias. Most people hang up on or ignore robocalls, so many selected individuals never answer → nonresponse bias. |
| Product survey "How satisfied were you with the product?" choices: Highly satisfied / satisfied / somewhat satisfied / not satisfied | **Response bias (question wording) + Nonresponse bias** | Three of the four choices are positive → unbalanced, leading answer set pushes answers toward "satisfied". Only customers who bother to reply (very happy or very angry) return it. |


## CHAPTER 2 – ORGANIZING AND SUMMARIZING DATA

Which display for which data: Qualitative → frequency / relative-frequency table, bar graph, Pareto chart, pie chart. Quantitative → class frequency table, histogram, stem-and-leaf, time-series plot. **Raw data** = data as collected, not yet organized.

### 2.1 Organizing Qualitative Data ★ (PE Q5)

- ★ **Frequency distribution** = table listing each category of the variable and its **frequency** (number of times it occurs). Frequencies add to the total n.
- ★ **Relative frequency** = proportion of all observations in a category: **RF = frequency / total**. RFs add to 1 (0.9999–1.0001 is fine with rounding). A relative frequency distribution lists each category with its RF.
- ★ **Pie-chart degree measure = RF × 360°**; degrees add to 360°.

Conversions in every direction:

| Have | Want | Formula |
|---|---|---|
| frequency f, total n | RF | RF = f / n |
| RF, total n | f | f = RF × n (round to a whole number) |
| every other RF | one missing RF | RF = 1 − (sum of the other RFs) |
| every other frequency, total | one missing frequency | f = n − (sum of the others) |
| RF (or f and n) | degree measure | degrees = RF × 360° = (f / n) × 360° |
| every other degree | ONE missing degree (only when exactly one is missing) | 360° − (sum of the others) |
| degree measure | RF | RF = degrees / 360 |
| RF | percent | % = RF × 100 |

Steps: (1) Find total n: given, or add the frequencies, or n = f / RF from any row that has both. (2) Convert row by row. (3) Check: frequencies sum to n, RFs sum to 1 (0.9999–1.0001 OK), degrees sum to 360°.

**Ex 1 (Slashdot "best day of the week", 40 people).** Given: Sun 5, Mon 2, Tue 2, Wed 2, Thu 4, Fri 10, Sat ?, Sat RF = 0.375.
Saturday = 40 − (5 + 2 + 2 + 2 + 4 + 10) = 40 − 25 = **15**; check 15/40 = 0.375 ✓. RFs: Sun 5/40 = 0.1250; Mon, Tue, Wed 2/40 = 0.0500 each; Thu 4/40 = 0.1000; Fri 10/40 = 0.2500; Sat 15/40 = 0.3750. Sum 0.1250 + 0.0500 + 0.0500 + 0.0500 + 0.1000 + 0.2500 + 0.3750 = 1.0000 ✓. Other route for Sat: 1 − 0.625 = 0.375 ✓.

**Ex 2 (rehab body part, SRS of n = 30; frequency = RF × 30, round to a whole number).** Back 12 → 12/30 = 0.4000; Wrist 0.0667 × 30 = 2.001 → **2**; Elbow 0.0333 × 30 = 0.999 → **1**; Hip → 2; Shoulder 0.1333 × 30 = 3.999 → **4**; Knee 0.1667 × 30 = 5.001 → **5**; Hand → 2; Groin → 1; Neck 1 → 1/30 = 0.0333. Check: 12 + 2 + 1 + 2 + 4 + 5 + 2 + 1 + 1 = 30 ✓.

**Qualitative graphs**
- **Bar graph**: categories on one axis, frequency (or RF) on the other; bar height = frequency; bars separated by gaps. A relative frequency bar graph uses RF heights (same shape). ★ Rules: vertical axis **starts at 0**, all bars **equal width**, graph is **2-D** — otherwise misleading (2.4). **Construct:** (1) categories on the horizontal axis; (2) vertical axis = frequency or RF, evenly scaled, starting at 0; (3) one bar per category, equal widths, gaps between bars, height = its frequency/RF; (4) label both axes + title.
- **Pareto chart** = bar graph whose bars are in **decreasing order** of frequency (tallest on the left). Construct: sort the table by frequency first, then draw the bar graph.
- ★ **Comparing two data sets** (educational attainment 1990 vs 2021): side-by-side bar graph using **relative frequency, never counts** (the two sets have different totals). RF = f / that set's own total. Model conclusion: "Comparing RFs category by category, from 1990 to 2021 the share of adults who are not high-school graduates fell and the share with a bachelor's or graduate degree rose."
- **Pie chart** = circle divided into sectors, one per category; sector angle = RF × 360°. **Construct:** (1) RF = f/n for each category; (2) degrees = RF × 360°; (3) draw each sector with its angle (check they total 360°); (4) label each sector with category and percent (RF × 100). ★ **Pie vs bar**: pie → showing **parts of a whole** (each category's share of 100%). Bar → **comparing specific categories** (angles are hard to judge by eye), or when only **a few categories** are shown (not the whole) → must use a bar graph.
- Reading an RF graph (Ex 4): "True/False: more than 50% have some college experience?" → add the RFs of every qualifying category (some college no degree + associate + bachelor's + graduate) and compare with 0.50. "About what % have a HS diploma or below?" → RF(not a HS graduate) + RF(HS graduate), × 100.

### 2.2 Organizing Quantitative Data: Histograms ★ (PE Q6)

- **Classes** = the intervals into which quantitative data are grouped. **Lower class limit** = smallest value in the class; **upper class limit** = largest value in the class. Class 60–69 → lower 60, upper 69.
- ★ **Class width = difference between consecutive LOWER class limits**: 40–49, 50–59 → 50 − 40 = **10** (NOT 49 − 40 = 9).
- Classes do not overlap; all have equal width. Only exception: **open-ended** tables — first class has no lower limit ("< $75") or last class has no upper limit ("$300 or more").
- Continuous-data classes: 50–74.99 means 50 up to anything less than 75; width = next lower limit − this lower limit = 75 − 50 = 25.
- **Building classes from a first lower limit and a width:** next lower limit = previous lower limit + width; upper limit = next lower limit − 1 (integer data). Worked (Ch 3 Ex 6: first lower limit 55, width 15): lower limits 55, 70, 85, 100, 115, 130 → classes **55–69, 70–84, 85–99, 100–114, 115–129, 130–144**. Tally each value into its class; frequencies must sum to n; check width 70 − 55 = 15 ✓.
- **Frequency histogram**: one bar per class, height = frequency, bars **touch** (no gaps), classes on the horizontal axis. **Relative frequency histogram**: same picture, heights = RF (vertical axis 0–1 or %); same shape.

★ Reading a histogram or class table:

| Question | How to answer |
|---|---|
| Frequency or relative frequency histogram? | Vertical axis: whole-number counts → frequency; proportions 0–1 (or %) → relative frequency |
| Class width? | 2nd lower limit − 1st lower limit |
| Most frequent class? | Tallest bar / largest frequency; answer with the interval (70–79), not the count |
| How many in a range? | Add the frequencies of every class inside the range |
| What percent in a range? | (sum of those frequencies ÷ total) × 100 |
| About how many in one class of an RF histogram? | RF × total |

Notes Ex 5 (graduation-rate histogram): (a) axis in counts → frequency histogram (proportions → relative frequency); (b) width = 2nd lower limit − 1st lower limit; (c) most frequent class = the tallest bar's interval; (d) 90–100% count = that bar's height (or RF × total). Ex 6 (four histograms): name the shape by where the TAIL is; graduation rate ≈ bell-shaped (Ch 3 Ex 10 applies the Empirical Rule to it).

**Describing shape**
- **Symmetric**: split down the middle, the halves are (almost) mirror images. Two kinds: **uniform** (all bars about the same height) and **bell-shaped** (highest in the middle, tapering equally on both sides).
- **Skewed** = not symmetric. ★ **The direction of the TAIL is the direction of the skew.** Skewed **right** → long tail to the right (a few unusually LARGE values). Skewed **left** → long tail to the left (a few unusually SMALL values).

```
 BELL-SHAPED (symmetric)   UNIFORM (symmetric)      SKEWED RIGHT (tail -->)    SKEWED LEFT (<-- tail)
          #                 # # # # # # #            #                                        #
        # # #               # # # # # # #            # #                                    # #
      # # # # #             # # # # # # #            # # #                                # # #
    # # # # # # #           # # # # # # #            # # # # #                        # # # # #
  # # # # # # # # #         # # # # # # #            # # # # # # # # #            # # # # # # # # #
 -------------------       ---------------          -------------------          -------------------
     mean = median           mean = median           median < mean                mean < median
                                                     (mean pulled toward tail)    (mean pulled toward tail)
```

★ Link to Ch 3: symmetric → mean ≈ median; skewed right → **mean > median**; skewed left → **mean < median**.

★ Real-world cues for shape (PE Q7):

| Situation | Shape | Reason |
|---|---|---|
| Salaries/income (a few executives earn millions), house prices, waiting times (most short, a few very long), hospital stays, number of children, ages of college students | **Skewed right** | Values can't go below 0; a few very LARGE values stretch the tail to the right (mean > median) |
| Scores on an easy exam (most score high, a few very low), age at death of adults, lifetimes of products that mostly last long | **Skewed left** | A few very SMALL values stretch the tail to the left (mean < median) |
| Heights, weights, IQ scores, standardized test scores, measurement errors, shoe sizes | **Bell-shaped** | Values cluster around a center with symmetric tails |
| Rolling a fair die, random digits 0–9, lottery numbers, birthdays by day of year | **Uniform** | Every outcome equally likely → all bars about the same height |

### 2.3 Additional Displays of Quantitative Data

**Stem-and-leaf plot**: each value is split into a **stem** (all digits except the last) and a **leaf** (the last digit). Keeps the raw data and shows the shape like a histogram. Steps: (1) Stems = leading digit(s), listed in increasing order INCLUDING stems with no data. (2) Write each value's last digit as a leaf on its stem's row (repeated values → repeated leaves). (3) Order the leaves. (4) Legend (5 | 6 = 56). (5) Check: number of leaves = n.

Notes example, exam scores: 56, 60, 66, 68, 80, 82, 82, 84, 88, 90, 92, 94, 98, 98 (n = 14)

```
5 | 6
6 | 0 6 8
7 |
8 | 0 2 2 4 8
9 | 0 2 4 8 8        Legend: 5 | 6 = 56
```

Leaf count 1 + 3 + 0 + 5 + 5 = 14 ✓; stem 7 kept even though empty. Turned 90° it is a histogram with class width 10. Shape: peak at stems 8–9, single low values 56–68 form a left tail → **skewed left**; check: mean = 1138/14 = 81.3 < median = (82 + 84)/2 = 83 ✓.

**Time-series plot**: time on the horizontal axis, the value of the variable at each time on the vertical axis; consecutive points connected by line segments. Ex 7 (Partisan Conflict Index, Dec 2004–2022) "In what year was the index highest?" → find the highest point, read its year off the horizontal axis. Shows trends over time.

### 2.4 Graphical Misrepresentations of Data

Two main ways graphs mislead (unintentionally) or deceive (intentionally): manipulating the **vertical axis** (not starting at 0) and changing the **width of the bars**.

| Trick | Why it misleads | Fix |
|---|---|---|
| ★ Vertical axis does not start at 0 (truncated/broken axis) | Small differences look huge. Ex 8: top marginal tax rate 39.6% → 37% drawn on a vertical axis that starts well above 0 (near the two values), so a 2.6-point drop looks like a collapse | Start the vertical axis at 0 |
| ★ Unequal bar widths | A wider bar looks like "more" although the frequency is the same (area is compared, not just height) | Make all bars the same width |
| 3-D bars/pies; inverted axis (higher on the y-axis = smaller value); unexpected colors (people read darker = more); pictographs scaled in two dimensions | Hard to read / perspective and area distort the comparison | Draw 2-D, values increasing upward, darker = larger, plain equal-width bars |

Exam-style answer: name the flaw AND the fix — "The vertical axis starts at about [read the actual value off the graph] instead of 0, which exaggerates the change; redraw with the vertical axis starting at 0." Check any given graph (Ex 9, highway accidents) against: starts at 0? equal bar widths? 2-D? axis increasing upward?

## ★ PRACTICE EXAM KEY — Q1 TO Q7

**Q1 (5 pts).** Nutritionist studies whether a new diet reduces cholesterol; selects 80 participants; measures before/after; after 12 weeks the average drop is 15 points.
- (a) **Population:** all people who could follow the new diet (everyone the nutritionist wants to draw a conclusion about).
- (b) **Sample:** the 80 participants selected.
- (c) **Individuals:** each person (one member of the population, e.g., one person whose cholesterol is measured).
- (d) **Parameter:** the mean drop in cholesterol after 12 weeks on the diet for the ENTIRE population, μ — unknown.
- (e) **Statistic:** the mean drop of 15 points for the 80 participants, x̄ = 15.

**Q2 (12 pts, 3 each).** (1) Qual/Quant, (2) Discrete/Continuous, (3) Level — write the reason.
- (a) Type of car transmission (manual, automatic, CVT) → **Qualitative; Not applicable (not quantitative); Nominal** — names/categories with no order.
- (b) Number of pets owned → **Quantitative; Discrete; Ratio** — a count 0, 1, 2, …; 0 pets = none; 4 pets is twice 2.
- (c) Temperature in Fahrenheit on a given day → **Quantitative; Continuous; Interval** — any value (72.4°F); differences meaningful, but 0°F ≠ "no temperature" and 80°F is not twice 40°F.
- (d) Ranking of the top 5 tennis players → **Qualitative; Not applicable; Ordinal** — 1st…5th have a meaningful order, but the gap between ranks is not a measurable equal amount.

**Q3 (4 pts).** Survey responses from college students about daily screen time and GPA.
- (a) **Observational study** — researchers only collected survey responses; they did not assign or control anyone's screen time.
- (b) **Explanatory variable = daily screen time.** (c) **Response variable = GPA.**
- (d) **Causation? No** — observational study → association only; lurking variables (sleep, study habits, job hours) could explain it.
- If the real exam gives an EXPERIMENT instead (Music Study 1 above): (a) designed experiment — researcher randomly ASSIGNED the treatment; (b) explanatory = type of music instruction; (c) response = IQ score; (d) causation: **Yes** (well-designed experiment).

**Q4 (3 pts).** Remote-work survey.
- (1) Sent only to employees at headquarters → **Sampling bias** (technique excludes all non-HQ employees → undercoverage).
- (2) Only 20% respond, mostly those unhappy with remote work → **Nonresponse bias** (non-responders' opinions differ from responders').
- (3) Employees give "safe" answers they think management wants → **Response bias** (answers do not reflect true opinions).

**Q5 (8 pts).** 200 households, favorite weekend activity. n = 60 + 50 + 40 + 30 + 20 = 200 ✓. RF = f/200; degrees = RF × 360°.

| Activity | Frequency | Relative frequency (show the division) | Degree measure (show the product) |
|---|---|---|---|
| Sports | 60 | 60/200 = **0.3000** | 0.3000 × 360° = **108°** |
| Movies | 50 | 50/200 = **0.2500** | 0.2500 × 360° = 90° (given ✓) |
| Shopping | 40 | 40/200 = 0.2000 (given ✓) | 0.2000 × 360° = **72°** |
| Reading | 30 | 30/200 = 0.1500 (given ✓) | 0.1500 × 360° = 54° (given ✓) |
| Other | 20 | 20/200 = 0.1000 (given ✓) | 0.1000 × 360° = 36° (given ✓) |
| Total | 200 | 1.0000 | 360° |

Checks: 0.3000 + 0.2500 + 0.2000 + 0.1500 + 0.1000 = 1.0000 ✓; 108 + 90 + 72 + 54 + 36 = 360 ✓. Two degrees are missing here, so compute Shopping = 0.2000 × 360° = 72° first; then Sports = 0.3000 × 360° = 108° directly, or as a check Sports = 360 − (90 + 72 + 54 + 36) = 360 − 252 = 108° (the subtraction shortcut works only when exactly ONE degree is missing).
- (b) Most popular = largest frequency (60) → **Sports**. (c) Reading: 30/200 = 0.15 → 0.15 × 100 = **15%**.
- (d) Sports or Movies: (60 + 50)/200 = 110/200 = 0.55 = 55% > 50% → **True** (or 0.3000 + 0.2500 = 0.55).

**Q6 (5 pts).** Quiz scores of 40 students: 40–49 (4), 50–59 (6), 60–69 (10), 70–79 (12), 80–89 (8). Total 4 + 6 + 10 + 12 + 8 = 40 ✓.
- (a) 3rd class = 60–69 → **lower class limit = 60, upper class limit = 69**.
- (b) Class width = consecutive lower limits: 50 − 40 = **10** (not 49 − 40 = 9).
- (c) 70 or higher = 70–79 and 80–89: 12 + 8 = 20 → 20/40 = 0.50 → **50%**.
- (d) Below 60 = 40–49 and 50–59: 4 + 6 = **10 students**.
- (e) Highest frequency = 12 → class **70–79**.

**Q7 (4 pts).** (a) Salaries, a few executives earn millions → **Skewed right** (a few very large values → long right tail). (b) Heights of 10-year-old boys → **Bell-shaped** (cluster near the middle, symmetric tails). (c) Rolling a fair die 200 times → **Uniform** (each face equally likely → all six bars about 33 tall). (d) Waiting times, most short but a few very long → **Skewed right** (tail toward the large values). Skewed-LEFT model answer: "an easy exam where most score high and a few score very low → skewed left (a few very small values stretch the tail left; mean < median)".

---

# SIDE 2

## CHAPTER 3 – NUMERICALLY SUMMARIZING DATA

Describe a distribution with 3 things: **SHAPE** (Ch 2), **CENTER** (3.1: mean/median/mode), **SPREAD** (3.2: range/SD; 3.4: IQR). Σ = "add them all up".

### 3.1 Measures of Central Tendency

**★ Mean** = add all values, divide by the number of observations.

| Data is… | Symbol | Formula | Divide by |
|---|---|---|---|
| ALL individuals (population) → parameter | **μ** | μ = Σx / N | N |
| SOME individuals (sample) → statistic | **x̄** | x̄ = Σx / n | n |

Cues for POPULATION (μ, σ, ÷N): the question says "population mean/variance/SD", or the data are ALL members ("all 7 students"). Cues for SAMPLE (x̄, s, ÷(n − 1)): "a sample of …", "select the first 5 observations as a sample" (PE Q9).
Ex 1 (all 7 students): 76, 80, 84, 86, 90, 92, 94 → Σx = 76 + 80 + 84 + 86 + 90 + 92 + 94 = 602; μ = 602/7 = **86**. Sample of 1st, 3rd, 6th (76, 84, 92): x̄ = 252/3 = **84**; sample of 2nd, 3rd, 7th (80, 84, 94): x̄ = 258/3 = **86**. Different samples → different x̄ (sampling error). ★ Population mean fully worked: PE Q8(a); sample mean: PE Q9(a).

**★ Median (M)** = middle value of ORDERED data; 50% below, 50% above. Steps: (1) Sort ascending. (2) Count n (or N). (3) **n odd** → M = value in position (n + 1)/2. **n even** → M = average of the values in positions n/2 and n/2 + 1.
Ex 2(a) 76, 80, 84, 86, 90, 92, 94: n = 7 odd → position (7 + 1)/2 = 4 → **M = 86**. Ex 2(b) 32, 76, 80, 84, 86, 90, 92, 94: n = 8 even → positions 4 and 5 → (84 + 86)/2 = **85**.

**Resistance**: a numerical summary is **resistant** if extreme values do not substantially change it. **Median = resistant; mean = NOT resistant** (also not resistant: range, SD; resistant: IQR).
Ex 3 (travel times, all 7 employees) 5, 18, 23, 23, 26, 36, 43: (a) Σx = 5 + 18 + 23 + 23 + 26 + 36 + 43 = 174; μ = 174/7 ≈ **24.857** min; (b) n = 7 odd → 4th value → **M = 23**. (c) Add a 70-min employee: 5, 18, 23, 23, 26, 36, 43, 70 → μ = 244/8 = **30.5**; n = 8 even → (23 + 26)/2 = **M = 24.5**. (d) Mean jumped 24.857 → 30.5 (+5.6); median moved 23 → 24.5 (+1.5) → **median is more resistant**.

**★ Mean vs. median → shape** (guideline; can fail for discrete data)

| Compare | Shape | Why |
|---|---|---|
| mean **<** median | **Skewed LEFT** | small values in the left tail pull the mean down |
| mean **≈** median | **Symmetric** | |
| mean **>** median | **Skewed RIGHT** | large values in the right tail pull the mean up |

Memory: the mean is dragged toward the tail. Ex 4: (a) mean 65 < median 75 → skewed left. (b) mean $172,950 ≈ median $173,000 → symmetric. (c) mean 1300 > median 1150 → skewed right. (d) mean 69 = median 69 → symmetric. ★ PE Q8(e) below.

**Mode** = the value that occurs most often (tally each value). One value occurs most → it is the mode; two or more tie → all are modes ("bimodal"); no repeats → **"no mode"**. Works for qualitative data too.
Ex 5: (a) 5, 18, 23, **23**, 26, 36, 43 → mode = **23**. (b) Company A: 7, 12, 12, 20, 20, 25 → modes **12 and 20** (bimodal). Company B: 5, 10, 15, 20, 27, 44 → **no mode**. ★ PE Q8(d): no mode.

### 3.2 Measures of Dispersion

**Dispersion** = how spread out the data are; center alone is not enough (Ex 6: two universities with the same mean IQ but very different spread → describe shape, center, AND spread).

**Range** R = largest − smallest. Ex: 5, 18, 23, 23, 26, 36, 43 → R = 43 − 5 = **38** min. Pro: easy. Con: uses only 2 values; not resistant. ★ Commute data: R = 40 − 18 = 22 min.

**Deviation about the mean**: population xᵢ − μ; sample xᵢ − x̄. With the exact mean, Σ(xᵢ − μ) = 0 (negatives cancel), so we SQUARE the deviations, average them (variance), then take the square root to undo the squaring (standard deviation).

**★ Standard deviation and variance**

| | Population | Sample |
|---|---|---|
| Variance (definition) | σ² = Σ(x − μ)² / **N** | s² = Σ(x − x̄)² / **(n − 1)** |
| Variance (computational, same answer) | σ² = [Σx² − (Σx)²/N] / N | s² = [Σx² − (Σx)²/n] / (n − 1) |
| Standard deviation | σ = √σ² | s = √s² |
| Calculator label | **σx** | **Sx** (or sx) |

**RULE: population → divide by N; sample → divide by n − 1.** Variance = (SD)². SD has the data's units; variance has units². Neither is resistant. SD ≥ 0; SD = 0 only if all values are equal.

**★ Deviation-table method (write this on the exam):** (1) Find the mean. (2) Column x − mean for every value. (3) Square each. (4) Add the squares = Σ(x − mean)². (5) Divide by N (population) or n − 1 (sample) = variance. (6) √variance = SD. Check: with the EXACT mean the deviation column sums to 0; with a rounded mean it is close to 0 but not exactly (Ex 7 with μ = 79 gives −1).
**If the mean does not terminate** (e.g., 174/7 = 24.857…): either carry the mean to 4 decimals in the table (deviations sum ≈ 0), or use the **computational formula**, which needs only Σx and Σx² and no rounded mean. Ex 3 data 5, 18, 23, 23, 26, 36, 43 (N = 7): Σx = 174; Σx² = 25 + 324 + 529 + 529 + 676 + 1296 + 1849 = 5228; σ² = [5228 − 174²/7]/7 = [5228 − 30276/7]/7 = [5228 − 4325.1429]/7 = 902.8571/7 = **128.98**; σ = √128.98 ≈ **11.36** min. (Sample version: divide the bracket by n − 1 = 6 instead → s² = 150.48, s ≈ 12.27.)

**Ex 7 – Population SD.** Scores 82, 77, 90, 70, 62, 68, 74, 84, 94, 88; N = 10; the notes give μ = 79 (exact mean 789/10 = 78.9 — on the exam use the exact mean unless one is given).

| x | μ | x − μ | (x − μ)² |
|---|---|---|---|
| 82 | 79 | 3 | 9 |
| 77 | 79 | −2 | 4 |
| 90 | 79 | 11 | 121 |
| 70 | 79 | −9 | 81 |
| 62 | 79 | −17 | 289 |
| 68 | 79 | −11 | 121 |
| 74 | 79 | −5 | 25 |
| 84 | 79 | 5 | 25 |
| 94 | 79 | 15 | 225 |
| 88 | 79 | 9 | 81 |
| | | Σ = −1 (≈ 0; not exactly 0 because μ = 79 is rounded from 78.9) | **Σ = 981** |

σ² = 981/10 = **98.1**; σ = √98.1 ≈ **9.90**. (With the exact mean 78.9: Σ(x − μ)² = 980.9, σ² = 980.9/10 = 98.09, σ = √98.09 ≈ 9.90 — same to two decimals.)

**Ex 8 – Sample SD.** Sample 62, 88, 77, 68; n = 4; x̄ = 295/4 = 73.75

| x | x̄ | x − x̄ | (x − x̄)² |
|---|---|---|---|
| 62 | 73.75 | −11.75 | 138.0625 |
| 88 | 73.75 | 14.25 | 203.0625 |
| 77 | 73.75 | 3.25 | 10.5625 |
| 68 | 73.75 | −5.75 | 33.0625 |
| | | Σ = 0 ✓ | **Σ = 384.75** |

s² = 384.75/(4 − 1) = 384.75/3 = **128.25**; s = √128.25 ≈ **11.32**. ★ Population variance/SD fully worked: PE Q8(b); sample variance: PE Q9(b).

"Is 31 cm far from a mean of 25 cm?" distance in SDs = (value − mean)/SD. σ = 6: (31 − 25)/6 = 1 SD → typical. σ = 0.5: (31 − 25)/0.5 = 12 SDs → very unusual.

### ★ Empirical Rule (68–95–99.7) — ONLY for bell-shaped data (PE Q11)

- ≈ **68%** of data within **1** SD: μ − 1σ to μ + 1σ
- ≈ **95%** within **2** SDs: μ − 2σ to μ + 2σ
- ≈ **99.7%** within **3** SDs: μ − 3σ to μ + 3σ

```
 μ−3σ     μ−2σ     μ−1σ      μ      μ+1σ     μ+2σ     μ+3σ
   |  2.35% |  13.5% |  34%   |  34%   |  13.5% |  2.35% |
 0.15% below μ−3σ                          0.15% above μ+3σ
```

How to answer any Empirical Rule question: (1) Write μ and σ (round σ to 1 decimal if the question's numbers only match a rounded σ, and SAY which σ you use). (2) Compute the 6 landmarks μ ± 1σ, μ ± 2σ, μ ± 3σ. (3) Match the numbers in the question to landmarks (z = (x − μ)/σ tells you which). (4) Add the band percentages between them.

| Question type | Answer |
|---|---|
| "68% / 95% / 99.7% lie between what values?" | μ ± 1σ / μ ± 2σ / μ ± 3σ (compute both endpoints) |
| between μ − kσ and μ + kσ | k = 1: 68%; k = 2: 95%; k = 3: 99.7% |
| between μ and μ + 1σ (or μ − 1σ and μ) | 34% |
| between μ + 1σ and μ + 2σ (or −2σ to −1σ) | 13.5% = (95 − 68)/2 |
| between μ + 2σ and μ + 3σ | 2.35% = (99.7 − 95)/2 |
| between μ + 1σ and μ + 3σ | 13.5 + 2.35 = 15.85% |
| above μ + 1σ (or below μ − 1σ) | 100 − 50 − 34 = 16% |
| above μ + 2σ (or below μ − 2σ) | (100 − 95)/2 = 2.5% |
| outside μ ± 2σ (both tails) | 100 − 95 = 5% |
| below μ − 3σ (or above μ + 3σ) | (100 − 99.7)/2 = 0.15% |
| above μ (or below μ) | 50% |
| between μ − 1σ and μ + 2σ | 34 + 34 + 13.5 = 81.5% |

Ex 9 (waist, bell-shaped, μ = 48.5 cm, σ = 4.8 cm): landmarks 1σ: 48.5 − 4.8 = 43.7, 48.5 + 4.8 = 53.3; 2σ: 48.5 ± 9.6 → 38.9 / 58.1; 3σ: 48.5 ± 14.4 → 34.1 / 62.9.
(a) 95% → μ ± 2σ = 48.5 ± 2(4.8) = 48.5 ± 9.6 → **38.9 cm to 58.1 cm**. (b) 34.1 = 48.5 − 3(4.8) = μ − 3σ and 62.9 = μ + 3σ → **99.7%**. (c) 53.3 = 48.5 + 4.8 = μ + 1σ; 62.9 = μ + 3σ → 13.5% + 2.35% = **15.85%**.
Ex 10 (graduation rate, μ = 65, σ = 17): (a) "**Empirical Rule** — IF the histogram is roughly bell-shaped (single central peak, symmetric tails)"; if not bell-shaped the Empirical Rule cannot be used (Chebyshev — not tested). (b) 31 = 65 − 2(17) = μ − 2σ; 99 = 65 + 2(17) = μ + 2σ → **≈ 95%**.
*[Not Tested] Chebyshev's inequality (any shape): at least (1 − 1/k²)·100% of data lie within k SDs of the mean (k > 1).*

### 3.4 Measures of Position and Outliers

**★ z-score** = number of standard deviations a value is from the mean. **Population: z = (x − μ)/σ. Sample: z = (x − x̄)/s.** No units. z > 0 above the mean, z < 0 below, z = 0 at the mean; most observations have −2 ≤ z ≤ 2. **Bigger z = relatively higher** → use z to compare values from different scales. Round z to 2 decimals.
Ex 11: ACT μ = 18, σ = 6, Student A scored 27 → z = (27 − 18)/6 = 9/6 = **1.50**. SAT μ = 1000, σ = 200, Student B scored 1200 → z = (1200 − 1000)/200 = 200/200 = **1.00**. 1.50 > 1.00 → **Student A** scored relatively higher.
Commute data (μ = 29.8, σ = 6.3844): the 40-min commute has z = (40 − 29.8)/6.3844 = 10.2/6.3844 = **1.60** (1.60 SDs above the mean; not unusual since it is within ±2).

**Percentiles**: the **kth percentile, Pₖ**, is the value such that **k% of the observations are ≤ Pₖ** (and (100 − k)% ≥ Pₖ). Percentile ≠ percent correct. Ex 12: "95th percentile" → scored at or above 95% of all test takers (top 5%); "70th percentile" → at or above 70% (top 30%); the full scholarship is stricter. Ex 13: the median is the **50th percentile** (P₅₀ = M = Q₂).

**★ Quartiles** divide ordered data into 4 equal parts: **Q₁ = P₂₅**, **Q₂ = P₅₀ = median**, **Q₃ = P₇₅**.
Steps: (1) Sort ascending. (2) **Q₂** = median of the whole data set. (3) **Q₁** = median of the LOWER half; **Q₃** = median of the UPPER half. **If n is odd, the overall median is NOT put in either half.** If n is even, the halves are the first n/2 and last n/2 values.
Ex 14 (n = 7, odd): 76, 80, 84 | **86** | 90, 92, 94 → Q₂ = 86 (4th). Lower half 76, 80, 84 → **Q₁ = 80**; upper half 90, 92, 94 → **Q₃ = 92**.
Ex 14 with 8th student (n = 8, even): 32, 76, 80, 84 | 86, 90, 92, 94 → Q₂ = (84 + 86)/2 = **85**; Q₁ = (76 + 80)/2 = **78**; Q₃ = (90 + 92)/2 = **91**.
Ex 15 (n = 8): 5, 18, 23, 23 | 26, 36, 43, 70 → Q₂ = (23 + 26)/2 = **24.5**; Q₁ = (18 + 23)/2 = **20.5**; Q₃ = (36 + 43)/2 = **39.5**. ★ Even n with odd halves (n = 10): PE Q10.

**Interquartile range IQR = Q₃ − Q₁** = spread of the middle 50%; resistant. Ex 16: 7 scores 92 − 80 = **12**; 8 scores 91 − 78 = **13**. Ex 17: travel times 39.5 − 20.5 = **19**.

**★ Which measures to report**

| Shape of distribution | Center | Spread |
|---|---|---|
| Symmetric | Mean | Standard deviation |
| Skewed left or skewed right | Median | IQR |

(Reason: mean & SD are not resistant; median & IQR are.)

**★ Outliers (formal rule)** — extreme observations (chance, measurement error, data-entry error, sampling error).
Steps: (1) Find Q₁ and Q₃. (2) IQR = Q₃ − Q₁. (3) **Lower fence = Q₁ − 1.5(IQR)**, **Upper fence = Q₃ + 1.5(IQR)**. (4) Any value **< lower fence or > upper fence is an outlier** (a value exactly on a fence is not).
Ex 18, 7 scores: Q₁ = 80, Q₃ = 92, IQR = 12, 1.5(12) = 18 → LF = 80 − 18 = **62**, UF = 92 + 18 = **110**. Min 76 > 62 and max 94 < 110 → **no outliers**.
Ex 18, 8 scores: Q₁ = 78, Q₃ = 91, IQR = 13, 1.5(13) = 19.5 → LF = 78 − 19.5 = **58.5**, UF = 91 + 19.5 = **110.5**. 32 < 58.5 → **32 IS an outlier**; 94 < 110.5 → no upper outliers.
Travel times (n = 8): Q₁ = 20.5, Q₃ = 39.5, IQR = 19, 1.5(19) = 28.5 → LF = 20.5 − 28.5 = **−8**, UF = 39.5 + 28.5 = **68**. 70 > 68 → **70 is an outlier**; 5 > −8 → no lower outliers.

### 3.5 Five-Number Summary and Boxplots ★ (PE Q10)

**Five-number summary = Minimum, Q₁, Median (Q₂), Q₃, Maximum** — in this order (Min and Max are the actual smallest/largest data values, even if they are outliers). Resistant → good for any shape.
Ex 19 (32, 76, 80, 84, 86, 90, 92, 94): **32, 78, 85, 91, 94**.

**★ Drawing a boxplot (5 steps):** (1) Compute the five-number summary AND the fences (LF = Q₁ − 1.5·IQR, UF = Q₃ + 1.5·IQR). (2) Draw a number line covering the data; mark Q₁, M, Q₃ with vertical lines and connect into a **box** (box = Q₁ to Q₃, line inside = median). (3) Lightly mark the fences (guides only). (4) Draw **whiskers** from the box to the **smallest and largest data values that are NOT outliers** (inside the fences) — NOT to the fences and NOT to an outlier. (5) Plot each **outlier as an asterisk (*)** beyond the whisker; erase the fence marks.

Ex 19 boxplot (fences 58.5 and 110.5; 32 is an outlier; smallest non-outlier = 76):

```
30        40        50        60        70        80        90        100
  *                                           |-[======|=====]--|
  32                                          76       85    91 94
                                                78 (Q1)
```
(box 78–91 with the line at the median 85; left whisker stops at 76 = smallest NON-outlier, NOT at 32; 32 is plotted as *)

Ex 20 (ride distances, n = 50; five-number summary 0.4, 2.2, 4.85, 9.4, 42.3): IQR = 9.4 − 2.2 = 7.2; 1.5(7.2) = 10.8; LF = 2.2 − 10.8 = **−8.6**; UF = 9.4 + 10.8 = **20.2**. Min 0.4 > −8.6 → left whisker ends at 0.4. UF = 20.2, so EVERY data value > 20.2 is an outlier and gets its own * (42.3 is certainly one; check the data table for others between 20.2 and 42.3). Right whisker stops at the largest data value ≤ 20.2. Box 2.2 to 9.4 with the line at 4.85.

**★ Reading a boxplot**
- Left box edge = Q₁; line in box = M; right box edge = Q₃; box length = IQR; about 25% of the data in each of: left whisker, left half of box, right half of box, right whisker; * = outliers.
- To READ a five-number summary off a boxplot (Ex 21a): Min = the leftmost mark on the plot (the smallest * if there are low outliers, otherwise the left whisker end); Max = the rightmost mark (the largest * if there are high outliers, otherwise the right whisker end). Whisker ends are the min/max of the NON-outliers only.

| Boxplot looks like | Shape |
|---|---|
| Median near the center of the box; whiskers about equal | **Symmetric** |
| Median closer to Q₁ (left of box); right whisker longer; outliers on the right | **Skewed right** |
| Median closer to Q₃ (right of box); left whisker longer; outliers on the left | **Skewed left** |

Ex 20/22: median 4.85 sits left of center in the box 2.2–9.4, long right whisker and high outliers → **skewed right**.
Comparing two boxplots (Ex 21b) — write 3 sentences: (1) CENTER: which median is larger; (2) SPREAD: which box (IQR) / whisker span is wider; (3) SHAPE/OUTLIERS: skew direction and which group has more/larger outliers. Conclude: "Yes/No, group X tends to have longer rides because its median (and Q₁, Q₃) are higher."

## CALCULATOR GUIDE (1-variable statistics) — VERIFY ON YOUR OWN MODEL BEFORE EXAM DAY

Calculator = a CHECK; the exam requires shown steps, so still write the deviation table. **σx = population SD (÷N). Sx / sx = sample SD (÷(n − 1)).** Variance = (SD)² — square the UNROUNDED SD (or read σ²x / s²x if your model shows them). Always clear the old list first.

| Model | Enter data | Get results | What you read |
|---|---|---|---|
| **TI-30XS MultiView / TI-34 MultiView / TI-36X Pro** | [data] → type each value in L1, [enter] after each. Clear old data: [data] [data] → Clear L1. | [2nd] [data] (stat-reg/distr) → 1-Var Stats → DATA: L1, FRQ: ONE → CALC | n, x̄, **Sx**, **σx**, Σx, Σx², minX, Q1, Med, Q3, maxX (scroll ▼) |
| **TI-30X IIS** | [2nd] [STAT] → 1-VAR → [ENTER] → [DATA] → X1 = value, ▼ FRQ = 1, ▼ X2 = … | [STATVAR] → arrow across | n, x̄, **Sx**, **σx**, Σx, Σx². Clear: [2nd] [STAT] → CLRDATA |
| **Casio fx-991EX ClassWiz** | [MENU] → 6:Statistics → 1:1-Variable → type value, [=] after each. If a FREQ column appears: [SHIFT] [MENU] (SETUP) → ▼ → Statistics → Frequency → Off. | [AC] → [OPTN] → 1-Variable Calc | x̄, Σx, Σx², **σ²x** (pop. variance), **σx**, **s²x** (sample variance), **sx**, n, min, Q1, Med, Q3, max |
| **Casio fx-300ES PLUS / fx-991ES PLUS / fx-115ES PLUS** | [MODE] → 3:STAT → 1:1-VAR → values, [=] after each → [AC]. Clear: re-enter [MODE] → 3:STAT → 1:1-VAR (re-selecting wipes the list), or [SHIFT] [9] (CLR) → All. | [SHIFT] [1] (STAT) → Var → 1:n, 2:x̄, 3:σx, 4:sx (one at a time, then [=]) | MinMax menu gives minX, maxX; quartiles by hand |
| **Casio fx-300MS / fx-991MS** | fx-300MS: [MODE] → 2:SD. fx-991MS: [MODE] [MODE] → 1:SD. Then each value followed by [M+] (DT). Clear: [SHIFT] [CLR] → 1:Scl → [=]. | [SHIFT] [2] (S-VAR) → 1:x̄, 2:xσn (population), 3:xσn−1 (sample) → [=] | x̄, **xσn** = σ, **xσn−1** = s |
| **TI-84 (graphing — only if allowed; the announcement says "scientific")** | [STAT] → 1:Edit → values in L1. Clear: cursor on the L1 header → [CLEAR] [ENTER]. | [STAT] → CALC → 1:1-Var Stats → List: L1, FreqList blank → Calculate | x̄, Σx, Σx², **Sx**, **σx**, n, minX, Q1, Med, Q3, maxX |

(Copy only YOUR model's row onto the physical sheet.) Checks: n must equal your count; x̄ must match Σx/n by hand; population variance = (σx)², sample variance = (Sx)². Some models compute Q1/Q3 with a different convention — on the exam compute quartiles BY HAND with the halves method and show the steps.

## ★ PRACTICE EXAM Q8–Q11, FULLY WORKED (commute times of 10 employees → POPULATION)

Data (already sorted): **18, 22, 25, 28, 30, 31, 33, 35, 36, 40**; N = 10. The questions say "population mean/variance" → μ, σ, divide by N.

### Q8 (a) Population mean (2 pts) — μ = Σx / N
Σx = 18 + 22 + 25 + 28 + 30 + 31 + 33 + 35 + 36 + 40 = 298 → **μ = 298/10 = 29.8 minutes**

### Q8 (b) Population variance and standard deviation (3 pts) — σ² = Σ(x − μ)² / N; σ = √σ²

| x | x − μ | (x − μ)² |
|---|---|---|
| 18 | 18 − 29.8 = −11.8 | 139.24 |
| 22 | 22 − 29.8 = −7.8 | 60.84 |
| 25 | 25 − 29.8 = −4.8 | 23.04 |
| 28 | 28 − 29.8 = −1.8 | 3.24 |
| 30 | 30 − 29.8 = 0.2 | 0.04 |
| 31 | 31 − 29.8 = 1.2 | 1.44 |
| 33 | 33 − 29.8 = 3.2 | 10.24 |
| 35 | 35 − 29.8 = 5.2 | 27.04 |
| 36 | 36 − 29.8 = 6.2 | 38.44 |
| 40 | 40 − 29.8 = 10.2 | 104.04 |
| Σ | 0 ✓ (exact mean → deviations sum to 0) | **407.60** |

Running sum: 139.24 + 60.84 = 200.08; + 23.04 = 223.12; + 3.24 = 226.36; + 0.04 = 226.40; + 1.44 = 227.84; + 10.24 = 238.08; + 27.04 = 265.12; + 38.44 = 303.56; + 104.04 = **407.60**
**σ² = 407.60/10 = 40.76 min²**; **σ = √40.76 = 6.3844 ≈ 6.38 minutes** (the instructor's Q11 bounds use 6.4 — reason stated at Q11).
Computational check: Σx² = 324 + 484 + 625 + 784 + 900 + 961 + 1089 + 1225 + 1296 + 1600 = 9288; σ² = [9288 − 298²/10]/10 = [9288 − 88804/10]/10 = [9288 − 8880.4]/10 = 407.6/10 = 40.76 ✓.
Calculator: 1-Var Stats → **σx = 6.3844** (use this); Sx = 6.7297 is the SAMPLE SD (÷9) — wrong here. Variance = (6.3844)² = 40.76 using the UNROUNDED σ (or the σ²x entry). Never square the rounded 6.4 (6.4² = 40.96 ≠ 40.76).
If the same 10 values were called a **SAMPLE**: s² = 407.60/(10 − 1) = 407.60/9 = **45.29 min²**; s = √45.29 ≈ **6.73 minutes** (calculator Sx).
Range (if asked): R = 40 − 18 = 22 minutes (not resistant).

### Q8 (c) Median (1 pt)
n = 10 even → average positions 10/2 = 5 and 6 → values 30 and 31 → **M = (30 + 31)/2 = 61/2 = 30.5 minutes**

### Q8 (d) Mode (1 pt)
Every value occurs exactly once → **no mode**.

### Q8 (e) Shape from mean vs. median (1 pt)
Mean 29.8 **<** median 30.5 → **Skewed left (slightly)** — rule: mean < median ⇒ skewed left; the mean is pulled toward the low tail. Write the comparison and the rule; do not just write "symmetric". Skewed → report median & IQR (3.4 table).

### Q9 Sample = first 5 observations: 18, 22, 25, 28, 30; n = 5
**(a) Sample mean (2 pts)** — x̄ = Σx / n: Σx = 18 + 22 + 25 + 28 + 30 = 123 → **x̄ = 123/5 = 24.6 minutes**
**(b) Sample variance (2 pts)** — s² = Σ(x − x̄)² / (n − 1)

| x | x − x̄ | (x − x̄)² |
|---|---|---|
| 18 | 18 − 24.6 = −6.6 | 43.56 |
| 22 | 22 − 24.6 = −2.6 | 6.76 |
| 25 | 25 − 24.6 = 0.4 | 0.16 |
| 28 | 28 − 24.6 = 3.4 | 11.56 |
| 30 | 30 − 24.6 = 5.4 | 29.16 |
| Σ | 0 ✓ | **91.20** |

43.56 + 6.76 = 50.32; + 0.16 = 50.48; + 11.56 = 62.04; + 29.16 = **91.20**
**s² = 91.20/(5 − 1) = 91.20/4 = 22.8 min²** (if s is asked: s = √22.8 ≈ 4.77 minutes; calculator Sx = 4.7749)
★ Divide by **n − 1 = 4**, NOT 5 (÷5 gives 18.24 → loses the points). The word "sample" is the trigger for n − 1.
Computational check: Σx² = 324 + 484 + 625 + 784 + 900 = 3117; s² = [3117 − 123²/5]/4 = [3117 − 15129/5]/4 = [3117 − 3025.8]/4 = 91.2/4 = 22.8 ✓.

### Q10 (a) Five-number summary (3 pts) — all 10 values
Sorted; n = 10 even → two halves of 5, nothing left out:

```
Lower half:  18, 22, [25], 28, 30   |   Upper half:  31, 33, [35], 36, 40
                     Q1 = 25        M = (30 + 31)/2 = 30.5       Q3 = 35
```

Min = **18**; Q₁ = median of {18, 22, **25**, 28, 30} = **25**; M = (30 + 31)/2 = **30.5**; Q₃ = median of {31, 33, **35**, 36, 40} = **35**; Max = **40**.
**Five-number summary: 18, 25, 30.5, 35, 40**

### Q10 (b) IQR (1 pt) = Q₃ − Q₁ = 35 − 25 = **10 minutes**

### Q10 (c) Fences and outliers (2 pts)
1.5(IQR) = 1.5(10) = 15. **Lower fence = Q₁ − 15 = 25 − 15 = 10; Upper fence = Q₃ + 15 = 35 + 15 = 50.**
Outlier = any value < 10 or > 50. Smallest 18 > 10 and largest 40 < 50 → **no outliers**.
(Boxplot: box 25 to 35 with line at 30.5; whiskers to 18 and 40; no asterisks. For the outlier case with whisker/asterisk placement see Ex 19 above.)

### Q11 Empirical Rule (6 pts) with μ = 29.8 and σ from Q8
σ = √40.76 = 6.3844 ≈ 6.38; the instructor's landmarks 23.4 / 36.2 / 42.6 come out exactly with **σ = 6.4** — he rounds σ to ONE decimal before building μ ± kσ. **General rule:** for Empirical Rule parts, round σ to 1 decimal, write "using σ ≈ 6.4", then compute the landmarks; if the question's numbers still don't match exactly, match each to the NEAREST landmark and say which k it is. (With 6.38: 29.8 ± 12.76 → 17.04 and 42.56, which round to the same 17.0 and 42.6.)

| k | kσ | μ − kσ | μ + kσ | % inside |
|---|---|---|---|---|
| 1 | 1(6.4) = 6.4 | 29.8 − 6.4 = **23.4** | 29.8 + 6.4 = **36.2** | 68% |
| 2 | 2(6.4) = 12.8 | 29.8 − 12.8 = **17.0** | 29.8 + 12.8 = **42.6** | 95% |
| 3 | 3(6.4) = 19.2 | 29.8 − 19.2 = **10.6** | 29.8 + 19.2 = **49.0** | 99.7% |

```
 10.6     17.0     23.4     29.8     36.2     42.6     49.0
   |  2.35% |  13.5% |  34%   |  34%   |  13.5% |  2.35% |
 0.15% below 10.6                              0.15% above 49.0
```

- **(a)** 95% ↔ within 2 SDs: μ − 2σ = 29.8 − 2(6.4) = 29.8 − 12.8 = 17.0; μ + 2σ = 29.8 + 12.8 = 42.6 → **between 17.0 and 42.6 minutes**.
- **(b)** 23.4 = 29.8 − 6.4 = μ − 1σ and 36.2 = 29.8 + 6.4 = μ + 1σ → within 1 SD → **≈ 68%**.
- **(c)** 36.2 = μ + 1σ and 42.6 = μ + 2σ → band from +1σ to +2σ → (95% − 68%)/2 = 27%/2 = **13.5%**.
- Any other band: match the endpoints to the landmark table, then use the question-type table in the Empirical Rule section.

## ★ EXAM-DAY CHECKLIST — the common ways to lose points on THIS exam

| Trap | Do this instead |
|---|---|
| Median/quartiles on UNSORTED data | Sort ascending first, count n |
| Using N for a SAMPLE variance; stopping at the variance when SD is asked | "Sample" → ÷(n − 1) (Q9: ÷4, not ÷5); "population"/"all" → ÷N. Then √ for the SD, with units (variance is in min²) |
| Calculator Sx when σx is asked (or vice versa); squaring a ROUNDED SD | σx = population SD (Q8); Sx = sample SD. Variance = (unrounded SD)² |
| Odd n: putting the median into the halves for Q₁/Q₃ | Odd n → leave the middle value OUT of both halves. Even n → two full halves |
| RF written as a percent (30%); degrees without ° or computed from frequency | RF = decimal (0.3000); degrees = RF × 360°, write the ° |
| Class width = upper − lower of one class (49 − 40 = 9) | Width = next lower limit − this lower limit (50 − 40 = 10) |
| Claiming causation from an observational study | Observational → "association only, No"; only a designed experiment supports causation |
| Skew direction / mean-vs-median backwards | Skew is named for the TAIL: tail right = skewed right (mean > median); tail left = skewed left (mean < median) |
| Forgetting "no mode" / "not applicable" | No repeated value → "no mode"; qualitative variable → discrete/continuous = "not applicable" |
| Outlier check without fences; whisker drawn to an outlier | Write both fences, compare min and max; whiskers end at the last value INSIDE the fences, outliers get * |
