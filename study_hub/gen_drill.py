"""Generate 50 random Exam 2 drill questions (Ch 4–6, Sullivan conventions) as drill50.json for the study hub."""
import json, random, math, re
from math import comb, erf, sqrt
rng = random.Random(20261103)
Phi = lambda z: 0.5 * (1 + erf(z / sqrt(2)))
L = lambda z: round(Phi(z), 4)                 # table value for a 2-decimal z
def f4(v): return f"{v:.4f}"
def num(v, tol, label=None):
    d = {"type": "number", "value": round(v, 4), "tol": tol}
    if label: d["label"] = label
    return d
def nums(fields): return {"type": "numbers", "fields": [{"label": l, "value": round(v, 4), "tol": t} for l, v, t in fields]}
def choice(options, correct): return {"type": "choice", "options": options, "correct": options[correct]}
Q = []   # each: dict(prompt, question, answer, check, solution)
def add(prompt, question, answer, check, solution): Q.append({"prompt": prompt, "question": question, "answer": answer, "check": check, "solution": solution})
PT = 0.0006   # probability tolerance (accepts the rounded-sum and exact-fraction conventions)

# ------------------------------------------------------------ T1 two-way tables (8)
tables = [
    ("Pet ownership and housing", "Housing", ["Apartment", "House"], ["Dog", "Cat", "No pet"]),
    ("Coffee and shift", "Shift", ["Day", "Night"], ["Coffee", "Tea", "Neither"]),
    ("Major and class standing", "Standing", ["Underclass", "Upperclass"], ["Business", "Science", "Arts"]),
    ("Phone brand and age group", "Age", ["Under 30", "30 or older"], ["Brand A", "Brand B", "Other"]),
]
def table_scenario():
    title, colname, cols, rows = rng.choice(tables)
    cells = [[rng.randint(4, 30) for _ in cols] for _ in rows]
    rt = [sum(r) for r in cells]; ct = [sum(cells[i][j] for i in range(len(rows))) for j in range(len(cols))]; N = sum(rt)
    lines = [f"{title}. The table below summarizes {N} people."] + [f"| {colname} | " + " | ".join(cols) + " | Total |"] + [f"| {rows[i]} | " + " | ".join(str(c) for c in cells[i]) + f" | {rt[i]} |" for i in range(len(rows))] + ["| Total | " + " | ".join(str(c) for c in ct) + f" | {N} |"]
    return "\n".join(lines), cols, rows, cells, rt, ct, N
kinds1 = ["is", "or", "and", "given_col", "given_row", "not", "two_no_rep", "atleast_one"]
rng.shuffle(kinds1)
for kind in kinds1:
    prompt, cols, rows, cells, rt, ct, N = table_scenario()
    i = rng.randrange(len(rows)); j = rng.randrange(len(cols))
    r, c, cell = rows[i], cols[j], cells[i][j]
    if kind == "is":
        v = rt[i] / N
        add(prompt, f"What is the probability that a randomly selected person is in the \"{r}\" row?", f4(v), num(v, PT), f"one category → its total ÷ grand total\nP({r}) = {rt[i]}/{N} = {f4(v)}")
    elif kind == "or":
        v = (rt[i] + ct[j] - cell) / N
        add(prompt, f"What is the probability that a randomly selected person is \"{r}\" OR \"{c}\"?", f4(v), num(v, PT), f"OR → add both totals, subtract the overlap cell ({r} and {c} = {cell}) once\nP = {rt[i]}/{N} + {ct[j]}/{N} − {cell}/{N} = {rt[i] + ct[j] - cell}/{N} = {f4(v)}")
    elif kind == "and":
        v = cell / N
        add(prompt, f"What is the probability that a randomly selected person is \"{r}\" AND \"{c}\"?", f4(v), num(v, PT), f"AND → the one cell ÷ grand total\nP = {cell}/{N} = {f4(v)}")
    elif kind == "given_col":
        v = cell / ct[j]
        add(prompt, f"What is the probability that a person is \"{r}\" GIVEN that the person is \"{c}\"?", f4(v), num(v, PT), f"GIVEN → divide by the given group's total ({c} = {ct[j]}), not {N}\nP({r} | {c}) = {cell}/{ct[j]} = {f4(v)}")
    elif kind == "given_row":
        v = cell / rt[i]
        add(prompt, f"Of the people in the \"{r}\" row, what proportion are \"{c}\"? (This is a GIVEN question.)", f4(v), num(v, PT), f"\"of the {r} people\" = GIVEN {r} → divide by that row's total {rt[i]}\nP({c} | {r}) = {cell}/{rt[i]} = {f4(v)}")
    elif kind == "not":
        v = 1 - ct[j] / N
        add(prompt, f"What is the probability that a randomly selected person is NOT \"{c}\"?", f4(v), num(v, PT), f"NOT → 1 − P({c})\nP(not {c}) = 1 − {ct[j]}/{N} = {N - ct[j]}/{N} = {f4(v)}")
    elif kind == "two_no_rep":
        v = ct[j] / N * (ct[j] - 1) / (N - 1)
        add(prompt, f"Two people are selected without replacement. What is the probability that both are \"{c}\"?", f4(v), num(v, PT), f"AND for two picks → multiply; the 2nd pick has one fewer {c} and one fewer person\nP(both) = {ct[j]}/{N} · {ct[j] - 1}/{N - 1} = {f4(v)}")
    else:
        v = 1 - (N - ct[j]) / N * (N - ct[j] - 1) / (N - 1)
        add(prompt, f"Two people are selected without replacement. What is the probability that at least one is \"{c}\"?", f4(v), num(v, PT), f"at least one → 1 − P(none) = 1 − P(both NOT {c})\nP = 1 − {N - ct[j]}/{N} · {N - ct[j] - 1}/{N - 1} = 1 − {f4((N - ct[j]) / N * (N - ct[j] - 1) / (N - 1))} = {f4(v)}")

# ------------------------------------------------------------ T2 validity (4)
def dist_prompt(xs, ps): return "Consider the following table.\n| x | " + " | ".join(str(x) for x in xs) + " |\n| P(x) | " + " | ".join(ps) + " |"
# valid
xs = [0, 1, 2, 3]; ps = ["0.15", "0.35", "0.30", "0.20"]
add(dist_prompt(xs, ps), "Is this a valid discrete probability distribution?", "Valid", choice(["Valid", "Not valid"], 0), "Rule 1: every P(x) is between 0 and 1 ✓\nRule 2: 0.15 + 0.35 + 0.30 + 0.20 = 1.00 ✓ → valid")
xs = [1, 2, 3, 4, 5]; ps = ["0.10", "0.25", "0.30", "0.25", "0.15"]
add(dist_prompt(xs, ps), "Is this a valid discrete probability distribution?", "Not valid", choice(["Valid", "Not valid"], 1), "Rule 1 ✓ · Rule 2: 0.10 + 0.25 + 0.30 + 0.25 + 0.15 = 1.05 ≠ 1 → NOT valid (the probabilities add to 1.05)")
xs = [0, 1, 2, 3]; ps = ["0.45", "0.40", "0.25", "−0.10"]
add(dist_prompt(xs, ps), "Is this a valid discrete probability distribution?", "Not valid", choice(["Valid", "Not valid"], 1), "Rule 1 fails: P(3) = −0.10 is below 0 → NOT valid (a probability can never be negative), even though the sum is 1")
xs = [0, 1, 2, 3, 4]; ps = ["0.22", "0.31", "0.19", "?", "0.08"]
add(dist_prompt(xs, ps), "Find the value of P(3) that makes this a valid probability distribution.", "0.20", num(0.20, 0.0006), "The probabilities must add to exactly 1\nP(3) = 1 − (0.22 + 0.31 + 0.19 + 0.08) = 1 − 0.80 = 0.20")

# ------------------------------------------------------------ T3 discrete distribution (8)
def discrete_scenario():
    ctx = rng.choice([("number of cars in a household", [0, 1, 2, 3]), ("number of goals in a soccer match", [0, 1, 2, 3, 4]), ("number of siblings a student has", [0, 1, 2, 3]), ("number of overtime periods in a game", [0, 1, 2, 3])])
    name, xs = ctx
    f = [rng.randint(5, 40) for _ in xs]; N = sum(f)
    P = {x: round(fi / N, 4) for x, fi in zip(xs, f)}
    prompt = f"The {name} (x) was recorded for {N} cases:\n| x | " + " | ".join(str(x) for x in xs) + " |\n| frequency | " + " | ".join(str(v) for v in f) + " |\nFirst build the probability distribution: P(x) = frequency ÷ " + str(N) + " (4 decimals): " + ", ".join(f"P({x}) = {P[x]:.4f}" for x in xs) + "."
    return name, xs, f, N, P, prompt
kinds3 = ["exact", "atleast", "atmost", "more", "fewer", "between", "mean", "sd"]
rng.shuffle(kinds3)
for kind in kinds3:
    name, xs, f, N, P, prompt = discrete_scenario()
    k = rng.choice(xs[1:-1])
    if kind == "exact":
        add(prompt, f"Find P(X = {k}).", f4(P[k]), num(P[k], PT), f"one value → P({k}) = {f[xs.index(k)]}/{N} = {f4(P[k])}")
    elif kind == "atleast":
        lst = [x for x in xs if x >= k]; v = round(sum(P[x] for x in lst), 4)
        add(prompt, f"Find the probability that X is at least {k}.", f4(v), num(v, PT), f"at least {k} → {k} is IN → x = {', '.join(map(str, lst))}\nP = " + " + ".join(f4(P[x]) for x in lst) + f" = {f4(v)}")
    elif kind == "atmost":
        lst = [x for x in xs if x <= k]; v = round(sum(P[x] for x in lst), 4)
        add(prompt, f"Find the probability that X is at most {k}.", f4(v), num(v, PT), f"at most {k} → {k} is IN → x = {', '.join(map(str, lst))}\nP = " + " + ".join(f4(P[x]) for x in lst) + f" = {f4(v)}")
    elif kind == "more":
        lst = [x for x in xs if x > k]; v = round(sum(P[x] for x in lst), 4)
        add(prompt, f"Find the probability that X is more than {k}.", f4(v), num(v, PT), f"more than {k} → {k} is OUT → x = {', '.join(map(str, lst))}\nP = " + " + ".join(f4(P[x]) for x in lst) + f" = {f4(v)}")
    elif kind == "fewer":
        lst = [x for x in xs if x < k]; v = round(sum(P[x] for x in lst), 4)
        add(prompt, f"Find the probability that X is fewer than {k}.", f4(v), num(v, PT), f"fewer than {k} → {k} is OUT → x = {', '.join(map(str, lst))}\nP = " + " + ".join(f4(P[x]) for x in lst) + f" = {f4(v)}")
    elif kind == "between":
        a, b = xs[1], xs[-1]; lst = [x for x in xs if a <= x <= b]; v = round(sum(P[x] for x in lst), 4)
        add(prompt, f"Find the probability that X is between {a} and {b}, inclusive.", f4(v), num(v, PT), f"inclusive → both ends IN → x = {', '.join(map(str, lst))}\nP = " + " + ".join(f4(P[x]) for x in lst) + f" = {f4(v)}")
    elif kind == "mean":
        mu = round(sum(x * P[x] for x in xs), 2)
        add(prompt, "Compute the mean (expected value) of X. Round to 2 decimals.", f"{mu:.2f}", num(mu, 0.011), "μ = Σ x·P(x) = " + " + ".join(f"{x}({P[x]:.4f})" for x in xs) + " = " + " + ".join(f"{x * P[x]:.4f}" for x in xs) + f" = {mu:.2f}")
    else:
        mu = round(sum(x * P[x] for x in xs), 2); terms = {x: round((x - mu) ** 2 * P[x], 4) for x in xs}; var = round(sum(terms.values()), 4); sd = round(math.sqrt(var), 2)
        add(prompt, f"The mean is μ = {mu:.2f}. Compute the standard deviation of X. Round to 2 decimals.", f"{sd:.2f}", num(sd, 0.011), "σ² = Σ (x − μ)²·P(x) = " + " + ".join(f"({x} − {mu:.2f})²({P[x]:.4f})" for x in xs) + "\n= " + " + ".join(f"{terms[x]:.4f}" for x in xs) + f" = {var:.4f}\nσ = √{var:.4f} = {sd:.2f}")

# ------------------------------------------------------------ T4 binomial (10)
contexts4 = [("adults who own a smart speaker", 0.35), ("students who commute by bus", 0.25), ("customers who use a coupon", 0.4), ("voters who support the measure", 0.55), ("flights that arrive late", 0.2), ("households with a pet", 0.6), ("people who are left-handed", 0.1), ("employees who work remotely", 0.3), ("teens who prefer texting", 0.7), ("drivers who speed", 0.45)]
rng.shuffle(contexts4)
def binom(n, p): return {k: round(comb(n, k) * p ** k * (1 - p) ** (n - k), 4) for k in range(n + 1)}
def bshow(n, p, k): return f"P({k}) = {n}C{k}·({p})^{k}·({round(1 - p, 2)})^{n - k} = {comb(n, k)}({p ** k:.6g})({(1 - p) ** (n - k):.6g}) = {round(comb(n, k) * p ** k * (1 - p) ** (n - k), 4):.4f}"
kinds4 = ["exact", "fewer", "atmost", "more", "atleast", "between", "atleastone", "none", "meansd", "unusual"]
rng.shuffle(kinds4)
for kind, (ctx, p) in zip(kinds4, contexts4):
    n = rng.choice([6, 7, 8, 9, 10, 12]); B = binom(n, p); q = round(1 - p, 2)
    prompt = f"According to a survey, {int(p * 100)}% of {ctx}. A random sample of {n} is selected. Let X = the number in the sample who do."
    k = rng.randint(2, min(4, n - 2))
    if kind == "exact":
        add(prompt, f"Find the probability that exactly {k} do.", f4(B[k]), num(B[k], PT), f"Binomial: n = {n}, p = {p}, 1 − p = {q}\n{bshow(n, p, k)}")
    elif kind == "fewer":
        lst = list(range(0, k)); v = round(sum(B[x] for x in lst), 4)
        add(prompt, f"Find the probability that fewer than {k} do.", f4(v), num(v, PT), f"fewer than {k} → {k} is OUT → x = {', '.join(map(str, lst))} → add\n" + "\n".join(bshow(n, p, x) for x in lst) + f"\nP(X < {k}) = " + " + ".join(f4(B[x]) for x in lst) + f" = {f4(v)}")
    elif kind == "atmost":
        lst = list(range(0, k + 1)); v = round(sum(B[x] for x in lst), 4)
        add(prompt, f"Find the probability that at most {k} do.", f4(v), num(v, PT), f"at most {k} → {k} is IN → x = {', '.join(map(str, lst))} → add\n" + "\n".join(bshow(n, p, x) for x in lst) + f"\nP(X ≤ {k}) = " + " + ".join(f4(B[x]) for x in lst) + f" = {f4(v)}")
    elif kind == "more":
        other = list(range(0, k + 1)); s = round(sum(B[x] for x in other), 4); v = round(1 - s, 4)
        add(prompt, f"Find the probability that more than {k} do.", f4(v), num(v, PT), f"more than {k} → {k} is OUT → x = {k + 1} … {n} is a long list → 1 − P(X ≤ {k})\n" + "\n".join(bshow(n, p, x) for x in other) + f"\nP(X ≤ {k}) = " + " + ".join(f4(B[x]) for x in other) + f" = {f4(s)}\nP(X > {k}) = 1 − {f4(s)} = {f4(v)}")
    elif kind == "atleast":
        other = list(range(0, k)); s = round(sum(B[x] for x in other), 4); v = round(1 - s, 4)
        add(prompt, f"Find the probability that at least {k} do.", f4(v), num(v, PT), f"at least {k} → {k} is IN → x = {k} … {n} is a long list → 1 − P(X ≤ {k - 1})\n" + "\n".join(bshow(n, p, x) for x in other) + f"\nP(X ≤ {k - 1}) = " + " + ".join(f4(B[x]) for x in other) + f" = {f4(s)}\nP(X ≥ {k}) = 1 − {f4(s)} = {f4(v)}")
    elif kind == "between":
        a, b = k - 1, k + 1; lst = list(range(a, b + 1)); v = round(sum(B[x] for x in lst), 4)
        add(prompt, f"Find the probability that between {a} and {b} (inclusive) do.", f4(v), num(v, PT), f"inclusive → x = {', '.join(map(str, lst))} → add\n" + "\n".join(bshow(n, p, x) for x in lst) + f"\nP({a} ≤ X ≤ {b}) = " + " + ".join(f4(B[x]) for x in lst) + f" = {f4(v)}")
    elif kind == "atleastone":
        v = round(1 - B[0], 4)
        add(prompt, "Find the probability that at least one does.", f4(v), num(v, PT), f"at least one → 1 − P(0)\n{bshow(n, p, 0)}\nP(X ≥ 1) = 1 − {f4(B[0])} = {f4(v)}")
    elif kind == "none":
        add(prompt, "Find the probability that none do.", f4(B[0]), num(B[0], PT), f"none → P(0) = ({q})^{n}\n{bshow(n, p, 0)}")
    elif kind == "meansd":
        N2 = rng.choice([100, 150, 200, 250, 400]); mu = N2 * p; sd = round(math.sqrt(N2 * p * q), 2)
        add(f"According to a survey, {int(p * 100)}% of {ctx}. A random sample of {N2} is selected.", f"Find the expected number (mean) and the standard deviation of the number in the sample who do. (μ exact, σ to 2 decimals)", f"μ = {mu:g}, σ = {sd:.2f}", nums([("μ", mu, 0.011), ("σ", sd, 0.011)]), f"μ = np = {N2}({p}) = {mu:g}\nσ = √(np(1 − p)) = √({N2}({p})({q})) = √{N2 * p * q:.4g} = {sd:.2f}")
    else:
        N2 = rng.choice([100, 150, 200, 250, 400]); mu = N2 * p; sd = round(math.sqrt(N2 * p * q), 2); lo, hi = round(mu - 2 * sd, 2), round(mu + 2 * sd, 2)
        xo = rng.choice([int(hi) + rng.randint(3, 12), int(mu) + rng.randint(-5, 5)]); unusual = xo < lo or xo > hi
        add(f"According to a survey, {int(p * 100)}% of {ctx}. A random sample of {N2} is selected. (μ = {mu:g}, σ = {sd:.2f}, and np(1 − p) = {N2 * p * q:.4g} ≥ 10.)", f"Would it be unusual to find {xo} in the sample who do?", "Unusual" if unusual else "Not unusual", choice(["Unusual", "Not unusual"], 0 if unusual else 1), f"usual range = μ ± 2σ = {mu:g} ± 2({sd:.2f}) = {lo} to {hi}\n{xo} is {'outside' if unusual else 'inside'} the range → {'unusual' if unusual else 'not unusual'}")

# ------------------------------------------------------------ T5 uniform (6)
ctx5 = [("The waiting time (minutes) for a bus", 5, 25, "minutes"), ("The daytime temperature (°F) in a desert town in July", 85, 115, "°F"), ("The length (cm) of a machine-cut rod", 20, 32, "cm"), ("The amount of soda (oz) dispensed by a machine", 10, 16, "oz"), ("The time (seconds) a traffic light stays red", 30, 90, "seconds"), ("The weight (lb) of a bag of apples", 2, 6, "lb")]
rng.shuffle(ctx5)
kinds5 = ["height", "between", "below", "above", "back", "exact"]
for kind, (name, a, b, unit) in zip(kinds5, ctx5):
    w = b - a; prompt = f"{name} is uniformly distributed between {a} and {b} {unit}."
    if kind == "height":
        v = 1 / w
        add(prompt, "What is the height of the probability density function (the rectangle)?", f"1/{w} = {f4(v)}", num(v, 0.0006), f"height = 1/(b − a) = 1/({b} − {a}) = 1/{w} = {f4(v)} (so the area is {w} × 1/{w} = 1)")
    elif kind == "between":
        c = a + rng.randint(1, w // 3); d = c + rng.randint(1, w // 2); v = (d - c) / w
        add(prompt, f"Find the probability that the value is between {c} and {d} {unit}.", f4(v), num(v, PT), f"P({c} ≤ X ≤ {d}) = (d − c)/(b − a) = ({d} − {c})/({b} − {a}) = {d - c}/{w} = {f4(v)}")
    elif kind == "below":
        d = a + rng.randint(1, w - 1); v = (d - a) / w
        add(prompt, f"Find the probability that the value is less than {d} {unit}.", f4(v), num(v, PT), f"\"less than {d}\" → the piece from {a} to {d}\nP(X < {d}) = ({d} − {a})/({b} − {a}) = {d - a}/{w} = {f4(v)}")
    elif kind == "above":
        c = a + rng.randint(1, w - 1); v = (b - c) / w
        add(prompt, f"Find the probability that the value is more than {c} {unit}.", f4(v), num(v, PT), f"\"more than {c}\" → the piece from {c} to {b}\nP(X > {c}) = ({b} − {c})/({b} − {a}) = {b - c}/{w} = {f4(v)}")
    elif kind == "back":
        pct = rng.choice([10, 20, 25, 30, 40, 75, 80]); x = a + pct / 100 * w
        add(prompt, f"{pct}% of the values are below what number? (Backwards: the area to the left is given.)", f"{x:g}", num(x, 0.06), f"x = a + (area to the left)(b − a) = {a} + {pct / 100}({w}) = {a} + {pct / 100 * w:g} = {x:g} {unit}")
    else:
        d = a + rng.randint(1, w - 1)
        add(prompt, f"Find the probability that the value is exactly {d} {unit}.", "0", num(0.0, 0.0001), "A single value has no width under a continuous curve → P(X = one value) = 0")

# ------------------------------------------------------------ T6 standard normal (7)
def zpick(lo=-2.3, hi=2.3): return round(rng.uniform(lo, hi), 2)
def hint(z): return f"area to the left of z = {z:.2f} is {L(z):.4f}"
kinds6 = ["left", "right", "between", "outside", "backleft", "backright", "nonstd"]
rng.shuffle(kinds6)
for kind in kinds6:
    if kind == "left":
        z = zpick(); v = L(z)
        add(f"Standard normal. Hint: {hint(z)}.", f"Find the area to the left of z = {z:.2f}.", f4(v), num(v, PT), f"LEFT → the hint is the answer: P(Z < {z:.2f}) = {f4(v)}")
    elif kind == "right":
        z = zpick(); v = round(1 - L(z), 4)
        add(f"Standard normal. Hint: {hint(z)}.", f"Find the area to the right of z = {z:.2f}.", f4(v), num(v, PT), f"RIGHT → 1 − (left area) = 1 − {L(z):.4f} = {f4(v)}")
    elif kind == "between":
        z1 = zpick(-2.2, 0.3); z2 = round(z1 + rng.uniform(0.6, 2.4), 2); v = round(L(z2) - L(z1), 4)
        add(f"Standard normal. Hints: {hint(z1)}; {hint(z2)}.", f"Find the area between z = {z1:.2f} and z = {z2:.2f}.", f4(v), num(v, PT), f"BETWEEN → (left of the bigger z) − (left of the smaller z) = {L(z2):.4f} − {L(z1):.4f} = {f4(v)}")
    elif kind == "outside":
        z1 = zpick(-2.2, -0.3); z2 = zpick(0.3, 2.2); v = round(L(z1) + 1 - L(z2), 4)
        add(f"Standard normal. Hints: {hint(z1)}; {hint(z2)}.", f"Find the area to the left of z = {z1:.2f} OR to the right of z = {z2:.2f} (the two tails).", f4(v), num(v, PT), f"two tails → left tail + right tail = {L(z1):.4f} + (1 − {L(z2):.4f}) = {L(z1):.4f} + {1 - L(z2):.4f} = {f4(v)}")
    elif kind == "backleft":
        z = rng.choice([-1.28, -0.84, -0.52, 0.67, 1.04, 1.28, 1.96]); area = L(z)
        add(f"Standard normal. Hints: area to the left of z = {z:.2f} is {area:.4f}; area to the left of z = {z + 0.10:.2f} is {L(z + 0.10):.4f}; area to the left of z = {z - 0.10:.2f} is {L(z - 0.10):.4f}.", f"Find the z-score that has area {area:.4f} to its LEFT.", f"{z:g}", num(z, 0.011), f"backwards: the area is given → find the hint closest to {area:.4f} → z = {z:g}")
    elif kind == "backright":
        z = rng.choice([0.84, 1.28, 1.96, 2.05, 2.33]); area_left = L(z); area_right = round(1 - area_left, 4)
        add(f"Standard normal. Hints: area to the left of z = {z:.2f} is {area_left:.4f}; area to the left of z = {-z:.2f} is {round(1 - area_left, 4):.4f}.", f"Find the z-score that has area {area_right:.4f} to its RIGHT.", f"{z:g}", num(z, 0.011), f"RIGHT area given → convert: left area = 1 − {area_right:.4f} = {area_left:.4f} → the hint says z = {z:g}")
    else:
        mu = rng.choice([50, 60, 75, 80, 120]); sd = rng.choice([5, 8, 10, 12]); x1 = mu - rng.choice([3, 5, 7, 10]); x2 = mu + rng.choice([4, 6, 9, 12])
        z1 = round((x1 - mu) / sd, 2); z2 = round((x2 - mu) / sd, 2); v = round(L(z2) - L(z1), 4)
        add(f"X is normal with μ = {mu} and σ = {sd}. Hints: {hint(z1)}; {hint(z2)}.", f"Find P({x1} < X < {x2}).", f4(v), num(v, PT), f"z = ({x1} − {mu})/{sd} = {z1:.2f} → {L(z1):.4f};  z = ({x2} − {mu})/{sd} = {z2:.2f} → {L(z2):.4f}\nBETWEEN → {L(z2):.4f} − {L(z1):.4f} = {f4(v)}")

# ------------------------------------------------------------ T7 normal in context (7)
ctx7 = [("Adult male heights (inches)", 69.5, 2.8), ("SAT math scores", 520, 110), ("Battery life of a laptop (hours)", 9.2, 1.4), ("Weights of newborns (lb)", 7.5, 1.1), ("Systolic blood pressure of adults (mmHg)", 122, 14), ("Finish times in a 5K race (minutes)", 28, 4.5), ("Monthly cell-phone bills ($)", 72, 11)]
rng.shuffle(ctx7)
kinds7 = ["above", "below", "between", "percentile", "top", "bottom", "unusual"]
for kind, (name, mu, sd) in zip(kinds7, ctx7):
    base = f"{name} are approximately normally distributed with mean μ = {mu:g} and standard deviation σ = {sd:g}."
    if kind == "above":
        x = round(mu + rng.uniform(0.6, 1.9) * sd, 1); z = round((x - mu) / sd, 2); v = round(1 - L(z), 4)
        add(base + f" Hint: {hint(z)}.", f"Find the probability that a randomly selected value is above {x:g}.", f4(v), num(v, PT), f"z = ({x:g} − {mu:g})/{sd:g} = {z:.2f} → left area {L(z):.4f}\nABOVE → 1 − {L(z):.4f} = {f4(v)}")
    elif kind == "below":
        x = round(mu - rng.uniform(0.4, 1.8) * sd, 1); z = round((x - mu) / sd, 2); v = L(z)
        add(base + f" Hint: {hint(z)}.", f"Find the probability that a randomly selected value is below {x:g}.", f4(v), num(v, PT), f"z = ({x:g} − {mu:g})/{sd:g} = {z:.2f} → left area {L(z):.4f}\nBELOW → the hint itself = {f4(v)}")
    elif kind == "between":
        x1 = round(mu - rng.uniform(0.3, 1.5) * sd, 1); x2 = round(mu + rng.uniform(0.3, 1.8) * sd, 1); z1 = round((x1 - mu) / sd, 2); z2 = round((x2 - mu) / sd, 2); v = round(L(z2) - L(z1), 4)
        add(base + f" Hints: {hint(z1)}; {hint(z2)}.", f"Find the proportion of values between {x1:g} and {x2:g}.", f4(v), num(v, PT), f"z = ({x1:g} − {mu:g})/{sd:g} = {z1:.2f} → {L(z1):.4f};  z = ({x2:g} − {mu:g})/{sd:g} = {z2:.2f} → {L(z2):.4f}\nBETWEEN → {L(z2):.4f} − {L(z1):.4f} = {f4(v)}")
    elif kind == "percentile":
        k, z = rng.choice([(90, 1.28), (95, 1.645), (80, 0.84), (75, 0.67), (25, -0.67), (10, -1.28), (97.5, 1.96), (98, 2.05)]); x = round(mu + z * sd, 1)
        add(base + f" Hint: the z-score for the {k:g}th percentile is {z:g}.", f"Find the value at the {k:g}th percentile. Round to 1 decimal.", f"{x:g}", num(x, 0.06), f"{k:g}% below it → left area {k / 100} → z = {z:g}\nx = μ + zσ = {mu:g} + ({z:g})({sd:g}) = {x:g}")
    elif kind == "top":
        pct, z = rng.choice([(10, 1.28), (5, 1.645), (2.5, 1.96), (20, 0.84)]); x = round(mu + z * sd, 1)
        add(base + f" Hint: the z-score with area {1 - pct / 100:g} to its left is {z:g}.", f"What is the minimum value needed to be in the top {pct:g}%? Round to 1 decimal.", f"{x:g}", num(x, 0.06), f"top {pct:g}% → {100 - pct:g}% below → left area {1 - pct / 100:g} → z = {z:g}\nx = μ + zσ = {mu:g} + {z:g}({sd:g}) = {x:g}")
    elif kind == "bottom":
        pct, z = rng.choice([(10, -1.28), (5, -1.645), (20, -0.84), (25, -0.67)]); x = round(mu + z * sd, 1)
        add(base + f" Hint: the z-score with area {pct / 100:g} to its left is {z:g}.", f"What value separates the bottom {pct:g}% from the rest? Round to 1 decimal.", f"{x:g}", num(x, 0.06), f"bottom {pct:g}% → left area {pct / 100:g} → z = {z:g} (negative: below the mean)\nx = μ + zσ = {mu:g} + ({z:g})({sd:g}) = {x:g}")
    else:
        dz = rng.choice([-2.6, -2.2, 2.4, 1.3, -1.1]); x = round(mu + dz * sd, 1); z = round((x - mu) / sd, 2); tail = round(L(z) if z < 0 else 1 - L(z), 4); unusual = tail < 0.05
        add(base + f" Hint: {hint(z)}.", f"Is a value of {x:g} unusual? (Unusual = tail probability below 0.05, or |z| > 2.)", "Unusual" if unusual else "Not unusual", choice(["Unusual", "Not unusual"], 0 if unusual else 1), f"z = ({x:g} − {mu:g})/{sd:g} = {z:.2f} → tail area {tail:.4f} {'<' if unusual else '≥'} 0.05 → {'unusual' if unusual else 'not unusual'}")

assert len(Q) == 50, len(Q)
neg = lambda t: re.sub(r'(?<=[=\s(])-(?=\d)', '−', t)
for q in Q:
    for k in ("prompt", "question", "answer", "solution"): q[k] = neg(q[k])
    if q["check"]["type"] == "choice": q["check"]["correct"] = neg(q["check"]["correct"])
rng.shuffle(Q)
questions = []
for i, q in enumerate(Q, 1):
    questions.append({"points": 1, "prompt": f"Q{i}. " + q["prompt"], "parts": [{"label": "", "question": q["question"], "answer": q["answer"], "check": q["check"], "solution": q["solution"]}]})
test = {"key": "drill50", "title": "50-question drill · every type, new numbers", "intro": "Fifty random questions covering Q1–Q7 (tables, validity, discrete, binomial, uniform, z, normal). Each stands alone: read it, solve on paper, type the answer, Check. Probabilities to 4 decimals; μ, σ to 2; x values to 1. z hints are printed like the real exam.", "questions": questions}
json.dump({"key": "drill50", "test": test}, open("/tmp/claude-0/-home-user-dsdasda/bdc32f87-6f2d-5f62-952a-43c9c6f6142d/scratchpad/ex2/drill50.json", "w"), ensure_ascii=False, indent=1)
from collections import Counter
print("written 50 questions; checks:", Counter(q["check"]["type"] for q in Q))
