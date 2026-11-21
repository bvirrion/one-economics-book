"""The best linear contract w = a + b y when y = e + noise, found by search.

The agent's effort e costs c e**2 / 2 and she chooses e = b / c; her risk premium is
r b**2 var / 2. The fixed part a only shares the surplus, so the best b maximises
  surplus(b) = e - c e**2 / 2 - r b**2 var / 2.
"""

r, c = 2.0, 1.0


def surplus(b, var):
    e = b / c
    return e - c * e * e / 2 - r * b * b * var / 2


print("variance   best b   formula   effort   surplus   agency cost")
for var in [0.0, 0.25, 0.5, 1.0, 2.0, 4.0]:
    b = max((i / 1000 for i in range(1001)), key=lambda b: surplus(b, var))
    formula = 1 / (1 + r * c * var)
    s = surplus(b, var)
    first_best = 1 / (2 * c)
    print(
        f"{var:8.2f} {b:8.3f} {formula:9.3f} {b / c:8.3f}"
        f" {s:9.3f} {first_best - s:12.3f}"
    )
