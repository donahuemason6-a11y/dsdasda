"""New Q4–Q7 for the full practice exam in the hub (same structure and points as the posted exam, new contexts and numbers)."""
import json, math
from math import comb, erf, sqrt
Phi = lambda z: 0.5 * (1 + erf(z / sqrt(2)))
L = lambda z: round(Phi(z), 4)
f4 = lambda v: f"{v:.4f}"
def num(v, tol, label=None):
    d = {"type": "number", "value": round(v, 4), "tol": tol}
    if label: d["label"] = label
    return d
def nums(fields): return {"type": "numbers", "fields": [{"label": l, "value": round(v, 4), "tol": t} for l, v, t in fields]}

# ---------------- Q4 binomial: n = 9, p = 0.25
n, p = 9, 0.25; q = 1 - p
B = {k: round(comb(n, k) * p ** k * q ** (n - k), 4) for k in range(n + 1)}
def bshow(k): return f"P({k}) = {n}C{k}·(0.25)^{k}·(0.75)^{n - k} = {comb(n, k)}({p ** k:.6g})({q ** (n - k):.6g}) = {B[k]:.4f}"
s012 = round(B[0] + B[1] + B[2], 4); more2 = round(1 - s012, 4); b24 = round(B[2] + B[3] + B[4], 4)
N2 = 300; mu4 = N2 * p; sd4 = round(math.sqrt(N2 * p * q), 2)
Q4 = {"points": 8, "prompt": "According to a safety survey, 25% of drivers admit to texting while driving. In a random sample of 9 drivers, find the probability that:",
      "parts": [
          {"label": "(a) 2 pt", "question": "Exactly 3 admit to texting while driving.", "answer": f4(B[3]), "check": num(B[3], 0.0006), "solution": f"Binomial: n = 9, p = 0.25, 1 − p = 0.75\n₉C₃ = 9!/(3!·6!) = (9·8·7)/(3·2·1) = 84\n{bshow(3)}"},
          {"label": "(b) 2 pt", "question": "More than 2 admit to texting while driving.", "answer": f4(more2), "check": num(more2, 0.0006), "solution": f"\"more than 2\" → 2 is OUT → x = 3, 4, …, 9 is a long list → 1 − P(X ≤ 2)\n{bshow(0)}\n{bshow(1)}\n{bshow(2)}\nP(X ≤ 2) = {B[0]:.4f} + {B[1]:.4f} + {B[2]:.4f} = {s012:.4f}\nP(X > 2) = 1 − {s012:.4f} = {more2:.4f}"},
          {"label": "(c) 2 pt", "question": "Between 2 and 4 (inclusive) admit to texting while driving.", "answer": f4(b24), "check": num(b24, 0.0006), "solution": f"inclusive → x = 2, 3, 4 → add\n{bshow(2)}\n{bshow(3)}\n{bshow(4)}\nP(2 ≤ X ≤ 4) = {B[2]:.4f} + {B[3]:.4f} + {B[4]:.4f} = {b24:.4f}"},
          {"label": "(d) 2 pt", "question": "For a random sample of 300 drivers, find the expected number and the standard deviation of the number who admit to texting while driving.", "answer": f"μ = {mu4:g}, σ = {sd4:.2f}", "check": nums([("μ", mu4, 0.011), ("σ", sd4, 0.011)]), "solution": f"μ = np = 300(0.25) = {mu4:g}\nσ = √(np(1 − p)) = √(300(0.25)(0.75)) = √{N2 * p * q:g} = {sd4:.2f}"}]}

# ---------------- Q5 uniform on [2, 12]
a, b = 2, 12; w = b - a
Q5 = {"points": 5, "prompt": "The time X (minutes) a customer waits at a drive-through is uniformly distributed between 2 and 12 minutes.",
      "parts": [
          {"label": "(a) 1 pt", "question": "Sketch the probability density function and state its height.", "answer": "a flat line from 2 to 12 at height 1/10 = 0.1000 (zero elsewhere)", "check": num(1 / w, 0.0006, "height"), "solution": "height = 1/(b − a) = 1/(12 − 2) = 1/10 = 0.1000; the rectangle's area is 10 × 1/10 = 1"},
          {"label": "(b) 2 pt", "question": "Find the probability that a customer waits between 4 and 7 minutes.", "answer": f4(3 / w), "check": num(3 / w, 0.0006), "solution": "P(4 ≤ X ≤ 7) = (d − c)/(b − a) = (7 − 4)/(12 − 2) = 3/10 = 0.3000"},
          {"label": "(c) 2 pt", "question": "Find the probability that a customer waits more than 8.5 minutes.", "answer": f4(3.5 / w), "check": num(3.5 / w, 0.0006), "solution": "\"more than 8.5\" → the piece from 8.5 to 12\nP(X > 8.5) = (12 − 8.5)/(12 − 2) = 3.5/10 = 0.3500"}]}

# ---------------- Q6 standard normal with hints
z1, z2, z3 = 1.23, -1.75, 0.40
mu6, sd6, x6 = 45, 6, 36; z6 = round((x6 - mu6) / sd6, 2)
hints6 = f"Hints (as printed on the exam): area to the left of z = 1.23 is {L(z1):.4f}; left of z = −1.75 is {L(z2):.4f}; left of z = 0.40 is {L(z3):.4f}; left of z = −1.50 is {L(z6):.4f}."
Q6 = {"points": 6, "prompt": "Use the standard normal distribution. Round final answers to four decimal places. " + hints6,
      "parts": [
          {"label": "(a) 2 pt", "question": "Find the area under the standard normal curve to the RIGHT of z = 1.23.", "answer": f4(1 - L(z1)), "check": num(1 - L(z1), 0.0006), "solution": f"RIGHT → 1 − (area to the left) = 1 − {L(z1):.4f} = {1 - L(z1):.4f}"},
          {"label": "(b) 2 pt", "question": "Find the area between z = −1.75 and z = 0.40.", "answer": f4(L(z3) - L(z2)), "check": num(L(z3) - L(z2), 0.0006), "solution": f"BETWEEN → (left of the bigger z) − (left of the smaller z) = {L(z3):.4f} − {L(z2):.4f} = {L(z3) - L(z2):.4f}"},
          {"label": "(c) 2 pt", "question": "X is normally distributed with μ = 45 and σ = 6. Find P(X < 36).", "answer": f4(L(z6)), "check": num(L(z6), 0.0006), "solution": f"z = (36 − 45)/6 = {z6:.2f} → area to the left = {L(z6):.4f}\nBELOW → the hint itself: P(X < 36) = {L(z6):.4f}"}]}

# ---------------- Q7 normal in context: homework time μ = 55, σ = 12
mu7, sd7 = 55, 12
za = round((70 - mu7) / sd7, 2); zb = round((45 - mu7) / sd7, 2); zc1 = round((48 - mu7) / sd7, 2); zc2 = round((72 - mu7) / sd7, 2); zd = 1.28
xa = round(1 - L(za), 4); xb = L(zb); xc = round(L(zc2) - L(zc1), 4); xd = round(mu7 + zd * sd7, 2)
hints7 = f"Hints: area to the left of z = {za:.2f} is {L(za):.4f}; left of z = {zb:.2f} is {L(zb):.4f}; left of z = {zc1:.2f} is {L(zc1):.4f}; left of z = {zc2:.2f} is {L(zc2):.4f}; the z-score with area 0.90 to its left is 1.28."
Q7 = {"points": 8, "prompt": f"The time students spend on a statistics homework assignment is approximately normally distributed with mean μ = {mu7} minutes and standard deviation σ = {sd7} minutes. " + hints7,
      "parts": [
          {"label": "(a) 2 pt", "question": "Find the probability that a randomly selected student spends more than 70 minutes.", "answer": f4(xa), "check": num(xa, 0.0006), "solution": f"z = (70 − 55)/12 = {za:.2f} → left area {L(za):.4f}\nABOVE → 1 − {L(za):.4f} = {xa:.4f}"},
          {"label": "(b) 2 pt", "question": "Find the probability that a randomly selected student spends less than 45 minutes.", "answer": f4(xb), "check": num(xb, 0.0006), "solution": f"z = (45 − 55)/12 = {zb:.2f} → left area {L(zb):.4f}\nBELOW → the hint itself: {xb:.4f}"},
          {"label": "(c) 2 pt", "question": "Find the proportion of students who spend between 48 and 72 minutes.", "answer": f4(xc), "check": num(xc, 0.0006), "solution": f"z = (48 − 55)/12 = {zc1:.2f} → {L(zc1):.4f};  z = (72 − 55)/12 = {zc2:.2f} → {L(zc2):.4f}\nBETWEEN → {L(zc2):.4f} − {L(zc1):.4f} = {xc:.4f}"},
          {"label": "(d) 2 pt", "question": "How many minutes must a student spend to be in the top 10%?", "answer": f"{xd:.1f} minutes (≈ {round(xd)})", "check": num(xd, 0.5, "minutes"), "solution": f"top 10% → 90% below → area to the left = 0.90 → z = 1.28\nx = μ + zσ = 55 + 1.28(12) = 55 + {zd * sd7:.2f} = {xd:.2f} ≈ {xd:.1f} minutes"}]}

json.dump([Q4, Q5, Q6, Q7], open("/tmp/claude-0/-home-user-dsdasda/bdc32f87-6f2d-5f62-952a-43c9c6f6142d/scratchpad/ex2/examB_q4to7.json", "w"), ensure_ascii=False, indent=1)
for qq in (Q4, Q5, Q6, Q7):
    for pp in qq["parts"]: print(pp["label"], pp["answer"])
