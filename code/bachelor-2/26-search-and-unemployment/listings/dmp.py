"""Equilibrium unemployment in the search-and-matching model, monthly, invented numbers.

Matching m = A * u**0.5 * v**0.5; tightness theta = v / u; Nash wage with bargaining
power B. Tightness solves (1 - B) (p - z) / (r + s + B f) = c / q.
"""

A, B, C, R, S = 0.7, 0.5, 1.0, 0.004, 0.03


def equilibrium(p, z):
    lo, hi = 1e-6, 100.0
    for _ in range(200):
        theta = (lo + hi) / 2
        f, q = A * theta**0.5, A * theta**-0.5
        if (1 - B) * (p - z) / (R + S + B * f) > C / q:
            lo = theta
        else:
            hi = theta
    u = S / (S + f)
    return theta, f, u, (1 - B) * z + B * (p + C * theta)


for p, z in ((1.0, 0.4), (1.0, 0.5), (1.01, 0.4), (1.0, 0.9)):
    theta, f, u, w = equilibrium(p, z)
    print(f"p {p:.2f} z {z:.1f}: tightness {theta:.3f}, job finding {f:.3f}, ", end="")
    print(f"unemployment {100 * u:.2f}%, wage {w:.4f}")

for z in (0.4, 0.9):
    t0, t1 = equilibrium(1.0, z)[0], equilibrium(1.01, z)[0]
    print(f"z {z}: a 1% rise in p raises tightness by {100 * (t1 / t0 - 1):.1f}%")
