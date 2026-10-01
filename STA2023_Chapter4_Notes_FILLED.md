# STA2023 – Chapter 4: Probability — In-Class Notes, FILLED IN

(Blanks from the notes are filled with the textbook (Sullivan) definitions; every example is worked with all steps. Round probabilities to 4 decimals.)

---

## 4.1 Probability Rules

**Random process** = a situation where the outcome of a single trial cannot be predicted with certainty, but a long-run pattern (proportion) appears after many trials.

Coin flip example: after 100 flips the proportion of heads settles just above 0.50 → the chance of a head on this coin is about **0.5** (the long-run proportion). This is the **Law of Large Numbers**: as the number of repetitions grows, the proportion of times an outcome occurs gets closer to its probability.

**Probability** = a measure of the likelihood of a random event; the long-term proportion of times an outcome is observed if the experiment is repeated many times.

**Experiment** = any process with uncertain results that can be repeated. *Examples:* flipping a coin, rolling a die, drawing a card, picking an M&M from a bag.

**Sample space, S** = the collection of ALL possible outcomes of an experiment. *Example:* rolling a die → S = {1, 2, 3, 4, 5, 6}.

**Event** = any collection (subset) of outcomes from the sample space that we are interested in; written with capital letters (E, F, …). A **simple event** has exactly one outcome.

**Example 1** (roll one fair six-sided die)
- (a) Outcomes: 1, 2, 3, 4, 5, 6
- (b) S = {1, 2, 3, 4, 5, 6}
- (c) E = "roll an even number" = {2, 4, 6}

**Example 2** (one M&M picked at random)
- (a) Outcomes: brown, yellow, red, blue, orange, green
- (b) S = {brown, yellow, red, blue, orange, green}
- (c) E = "red or blue" = {red, blue}

### Basic Rules of Probability

**Notation:** P(E) = the probability that event E occurs. N(E) = number of outcomes in E; N(S) = number of outcomes in the sample space.

1. The probability of any event is between 0 and 1: **0 ≤ P(E) ≤ 1**. (P(E) = 0 → impossible; P(E) = 1 → certain.)
2. The probabilities of all outcomes in the sample space add to 1: **P(e₁) + P(e₂) + … + P(eₙ) = 1**.

**Probability model** = a table listing every possible outcome and its probability (must satisfy rules 1 and 2).

**Unusual event** = an event with a low probability, usually **less than 0.05 (5%)**. (A 3% chance → unusual.)

**Example 3** (die model, each side 1/6): every probability is between 0 and 1 ✓, and 1/6 × 6 = 6/6 = 1 ✓ → **valid**.

**Example 4**
- Model 1 (0.50, 0.50, 0): all between 0 and 1, sum = 1 → **valid** (a probability of 0 is allowed).
- Model 2 (0.40, 0.20): sum = 0.60 ≠ 1 → **not valid**.
- Model 3 (−0.10, 0.40, 0.60, 0.10): −0.10 is negative → **not valid** (even though the sum is 1).

### Methods to Determine Probabilities

**Empirical method** — uses relative frequency from data already collected:
**P(E) ≈ (frequency of E) ÷ (number of trials)**

**Example 6** (200 people, means of travel to work)
(a) Probability model = relative frequencies (frequency ÷ 200):

| Means of travel | Frequency | Probability |
|---|---|---|
| Drive alone | 83 | 83/200 = 0.415 |
| Carpool | 22 | 22/200 = 0.110 |
| Public transportation | 10 | 10/200 = 0.050 |
| Walk | 5 | 5/200 = 0.025 |
| Other means | 3 | 3/200 = 0.015 |
| Work at home | 77 | 77/200 = 0.385 |
| Total | 200 | 1.000 ✓ |

(b) P(carpool) = 22/200 = **0.11**. Interpretation: if we randomly selected many individuals, about 11% of them (about 11 out of every 100) would carpool to work.
(c) P(walk) = 5/200 = 0.025 < 0.05 → **yes, unusual**.

**Example 7** (M&M colors, total = 13 + 14 + 13 + 24 + 20 + 16 = 100)
(a) Brown 13/100 = 0.13; Yellow 0.14; Red 0.13; Blue 0.24; Orange 0.20; Green 0.16 (sum = 1.00 ✓)
(b) P(red) = 13/100 = **0.13**

**Classical method** — requires **equally likely outcomes**; count instead of experiment:
**P(E) = N(E) ÷ N(S)** = (number of ways E can happen) ÷ (total number of possible outcomes)

**Example 8** (fair coin flipped twice)
- (a) S = {HH, HT, TH, TT} → N(S) = 4
- (b) P(two heads) = P(HH) = **1/4 = 0.25**
- (c) "At least 1 tails" = {HT, TH, TT} → **3/4 = 0.75** (or 1 − P(HH) = 1 − 1/4 = 3/4)

**Example 9** (pick 2 of Adam, Ben, Sam, Dustin)
- (a) S = {AB, AS, AD, BS, BD, SD} → N(S) = 6 (order doesn't matter)
- (b) P(Adam and Ben) = **1/6 ≈ 0.1667**
- (c) P(Ben goes) = {AB, BS, BD} → **3/6 = 1/2 = 0.5**

**Subjective method** — a probability based on personal judgment, experience, or opinion (an educated guess), used when an experiment cannot be repeated and no data exist (e.g., "chance of a recession next year").

---

## 4.2 The Addition Rule and Complements

**Disjoint (mutually exclusive) events** = two events that have NO outcomes in common; they cannot both happen at the same time. In a Venn diagram the circles do not overlap.

**Example 10** (chips 0–9; E = "≤ 2" = {0, 1, 2}; F = "≥ 8" = {8, 9}): no outcome in common → **E and F are disjoint**. P(E) = 3/10, P(F) = 2/10.

### Addition Rule for Disjoint Events
If E and F are disjoint: **P(E or F) = P(E) + P(F)** (extends to any number of disjoint events: P(E or F or G) = P(E) + P(F) + P(G)).
(Example 10: P(E or F) = 3/10 + 2/10 = 5/10 = 0.5.)

**Example 11** (one card from a 52-card deck)
- (a) P(king) = 4/52 = **1/13 ≈ 0.0769**
- (b) P(king or queen or jack) = 4/52 + 4/52 + 4/52 = 12/52 = **3/13 ≈ 0.2308** (disjoint: a card can't be two ranks)
- (c) P(heart or diamond) = 13/52 + 13/52 = 26/52 = **1/2 = 0.5**

### The General Addition Rule
Chips 0–9; E = "odd" = {1, 3, 5, 7, 9}; F = "≤ 4" = {0, 1, 2, 3, 4}. Outcomes 1 and 3 are in BOTH, so adding P(E) + P(F) would count them twice. Count directly: E or F = {0, 1, 2, 3, 4, 5, 7, 9} → 8/10. Check: 5/10 + 5/10 − 2/10 = 8/10 ✓.

**General Addition Rule** — for ANY two events E and F:
**P(E or F) = P(E) + P(F) − P(E and F)**
(subtract the overlap so it isn't counted twice; if the events are disjoint, P(E and F) = 0 and this becomes the disjoint rule).

**Example 12** (one card; E = king, F = diamond; overlap = king of diamonds)
P(king or diamond) = 4/52 + 13/52 − 1/52 = 16/52 = **4/13 ≈ 0.3077**

**Contingency table** = a table that relates two categorical variables: a row variable and a column variable; each cell is a count.

**Example 13** (marital status, millions, US 2021)

| | Males | Females | Row total |
|---|---|---|---|
| Never married | 49.5 | 43.2 | 92.7 |
| Married | 66.3 | 64.2 | 130.5 |
| Widowed | 3.5 | 11.5 | 15.0 |
| Divorced | 12.3 | 16.6 | 28.9 |
| Separated | 2.0 | 2.6 | 4.6 |
| Column total | 133.6 | 138.1 | **271.7** |

- (a) P(male) = 133.6/271.7 ≈ **0.4917**
- (b) P(widowed) = 15.0/271.7 ≈ **0.0552**
- (c) P(widowed or divorced) = 15.0/271.7 + 28.9/271.7 = 43.9/271.7 ≈ **0.1616** (disjoint: a person has one status)
- (d) P(male or widowed) = P(male) + P(widowed) − P(male and widowed) = 133.6/271.7 + 15.0/271.7 − 3.5/271.7 = 145.1/271.7 ≈ **0.5340**

### Complement of an Event
**Complement of E, written Eᶜ (or E′ or "not E")** = all outcomes in the sample space that are NOT in E.
**Complement Rule: P(Eᶜ) = 1 − P(E)** (so P(E) + P(Eᶜ) = 1).
Illustration: a Venn diagram with the circle E inside the rectangle S; everything in the rectangle outside the circle is Eᶜ.

**Example 14:** P(has played) = 0.52 → P(has NOT played) = 1 − 0.52 = **0.48**

---

## 4.3 Independence and the Multiplication Rule

**Independent events** = two events E and F are independent if the occurrence of E does NOT affect the probability of F (and vice versa). Otherwise they are **dependent**.
- Coin flipped twice: first result doesn't change the second → independent.
- Die: P(6) = 1/6; but if told it was even, P(6) = 1/3 — the probability changed → "roll a 6" and "roll an even number" are dependent.

**Example 15**
- (a) Coin flip and die roll → **independent** (the coin can't affect the die).
- (b) Bachelor's degree and earning over $100,000 → **dependent** (having a degree changes the chance of a high income).
- (c) Two randomly selected 24-year-old males' accidents → **independent** (one driver's accident doesn't affect the other's).

### Multiplication Rule for Independent Events
Coin flipped twice: S = {HH, HT, TH, TT} → P(HH) = 1/4. Separately: P(H on 1st) × P(H on 2nd) = 1/2 × 1/2 = 1/4 — same answer.
If E and F are independent: **P(E and F) = P(E) · P(F)** (extends: P(E and F and G) = P(E)·P(F)·P(G), …).

**Example 16** (P(a 24-year-old male survives the year) = 0.9986)
- (a) Two survive: 0.9986 × 0.9986 = 0.9986² ≈ **0.9972**
- (b) Three survive: 0.9986³ ≈ **0.9958**
- (c) Twenty survive: 0.9986²⁰ ≈ **0.9724**

### Computing At-Least Probabilities
"At least one" = 1 or more. **P(at least 1) = 1 − P(none)**.

**Example 17** (at least one of 1000 males dies; P(survive) = 0.9986)
P(none die) = P(all 1000 survive) = 0.9986¹⁰⁰⁰ ≈ 0.2464
P(at least one dies) = 1 − 0.9986¹⁰⁰⁰ ≈ 1 − 0.2464 = **0.7536**

---

## 4.4 Conditional Probability and the General Multiplication Rule

**Conditional probability, P(F | E)** = the probability that F occurs GIVEN that E has already occurred (read "probability of F given E"). The "given" information shrinks the sample space to only the outcomes where E happened.

**Example 18:** P(six) = **1/6**. Given the roll was even, the sample space is {2, 4, 6} → P(six | even) = **1/3**.

**Conditional Probability Rule** (marital example): P(widowed) = 15.0/271.7 ≈ 0.0552. If we know the person is female, only the 138.1 million females are the sample space: P(widowed | female) = 11.5/138.1 ≈ **0.0833**.

**Rule:** for any two events E and F:
**P(F | E) = P(E and F) ÷ P(E) = N(E and F) ÷ N(E)**
(In a table: the cell count divided by the total of the row or column named after "given".)

**Example 19**
- (a) P(never married | male) = 49.5/133.6 ≈ **0.3705** (divide by the male column total)
- (b) P(male | never married) = 49.5/92.7 ≈ **0.5340** (divide by the never-married row total)

### General Multiplication Rule
**P(E and F) = P(E) · P(F | E)** (works whether or not the events are independent).

**Example 20:** P(pulled over and ticket) = P(pulled over) × P(ticket | pulled over) = 0.8 × 0.9 = **0.72**

### Determining Independence
Rule of thumb: when sampling without replacement from a large population, if the sample is **less than 5% of the population**, treat the selections as independent.

**E and F are independent if P(F | E) = P(F)** (equivalently P(E | F) = P(E), or P(E and F) = P(E)·P(F)). If the probabilities are different, the events are dependent.

**Example 21:** P(widowed) = 15.0/271.7 ≈ 0.0552, but P(widowed | female) = 11.5/138.1 ≈ 0.0833. 0.0833 ≠ 0.0552 → **not independent (dependent)**: knowing the person is female raises the chance of being widowed.

---

## 4.5 Counting Techniques

### General Counting Principle
Restaurant: 2 appetizers × 3 entrées × 2 desserts = **12** different meals (list: soup/salad × chicken/beef au jus/beef patty × ice cream/cheesecake).

**Multiplication Rule of Counting:** if a task is a sequence of choices with p options for the first, q for the second, r for the third, …, the total number of ways is **p · q · r · …**

**Example 22** (3-letter airport codes, repeats allowed): 26 × 26 × 26 = 26³ = **17,576**

**Example 23** (chair, vice-chair, secretary from 14 people): 14 × 13 × 12 = **2,184** (no repeats: one fewer choice each time)

**Factorial:** **n! = n · (n − 1) · (n − 2) · … · 3 · 2 · 1**, and **0! = 1**. (5! = 120.)

**Example 24** (visit 7 schools in some order): 7! = 7·6·5·4·3·2·1 = **5,040** routes

### Permutations
**Permutation** = an ordered arrangement of r objects chosen from n distinct objects, no repeats. **ORDER MATTERS.**
**ₙPᵣ = n! ÷ (n − r)!**

**Example 25:** ₇P₅ = 7!/(7−5)! = 7!/2! = 5040/2 = **2,520**. ₅P₅ = 5!/0! = 120/1 = **120**.
Excel: =PERMUT(7,5), =PERMUT(5,5).

**Example 26** (10 runners; 1st, 2nd, 3rd): ₁₀P₃ = 10!/7! = 10 × 9 × 8 = **720**

### Combinations
**Combination** = a selection of r objects from n distinct objects where **ORDER DOES NOT MATTER** (ABC is the same as BAC).
**ₙCᵣ = n! ÷ [r! (n − r)!]**

**Example 27** (teams of 2 from Roger, Ken, Tom, Jay): list: RK, RT, RJ, KT, KJ, TJ → 6. Formula: ₄C₂ = 4!/(2!·2!) = 24/(2·2) = **6**. Excel: =COMBIN(4,2).

**Example 28** (SRS of size 4 from 20): ₂₀C₄ = 20!/(4!·16!) = (20·19·18·17)/(4·3·2·1) = 116,280/24 = **4,845**

### Using Counting Methods in Probability
P(E) = (number of outcomes in E) ÷ (total number of outcomes), both found by counting.

**Example 29** (dealt 4 cards; all 4 match = four of a kind)
- (a) ₅₂C₄ = 52!/(4!·48!) = (52·51·50·49)/24 = **270,725** possible hands
- (b) One four-of-a-kind for each of the 13 ranks → **13** hands
- (c) P(all 4 match) = 13/270,725 ≈ **0.00005** (≈ 0.0000480)

**Which counting method?**
- Sequence of choices → Multiplication Rule of Counting (p · q · r …)
- Choosing r of n objects, **order matters** → permutation ₙPᵣ
- Choosing r of n objects, **order doesn't matter** → combination ₙCᵣ

---

## 4.7 Determining Which Method to Use (the flow chart in words)

**Single event?**
- Outcomes equally likely → classical: P(E) = N(E)/N(S)
- Not equally likely but data available → empirical: P(E) ≈ frequency of E / number of trials
- No data → subjective probability

**Two events — what word is in the question?**
- **"OR"** → disjoint? Yes: P(E or F) = P(E) + P(F). No: P(E or F) = P(E) + P(F) − P(E and F)
- **"AND"** → independent? Yes: P(E and F) = P(E)·P(F). No: P(E and F) = P(E)·P(F | E)
- **"AT LEAST one"** → P(at least 1) = 1 − P(none)
- **"GIVEN"** → conditional: P(F | E) = P(E and F)/P(E) = N(E and F)/N(E)
- **"NOT"** → complement: P(not E) = 1 − P(E)

**Counting:** sequence of choices → multiply (p·q·r…; tree diagram if choices depend on earlier ones). Selecting r of n → order matters: ₙPᵣ = n!/(n−r)!; order doesn't matter: ₙCᵣ = n!/[r!(n−r)!]. Excel: =PERMUT(n, r), =COMBIN(n, r).
