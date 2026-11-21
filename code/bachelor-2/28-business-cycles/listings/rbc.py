"""The real-business-cycle model with log utility and full depreciation.

y = a * k**ALPHA, k' = ALPHA * BETA * y, c = (1 - ALPHA * BETA) * y; log technology
follows log a' = RHO * log a + shock. All variables in per cent deviations.
"""

import numpy as np

ALPHA, BETA = 1 / 3, 0.96


def impulse(rho, periods=8):
    a, k, out = 1.0, 0.0, []
    for _ in range(periods):
        y = a + ALPHA * k  # log output
        out.append(y)
        a, k = rho * a, y  # next period's capital moves with this period's output
    return out


for rho in (0.0, 0.9):
    print(f"rho {rho}: output", " ".join(f"{y:.2f}" for y in impulse(rho)))

rng = np.random.default_rng(28)
a, k, ys = 0.0, 0.0, []
for shock in rng.normal(0, 1, 20000):
    a = 0.9 * a + shock
    y = a + ALPHA * k
    ys.append(y)
    k = y
y = np.array(ys)
c, i = y.copy(), y.copy()  # constant shares: log c and log k' move one for one with y
rel_c, rel_i = c.std() / y.std(), i.std() / y.std()
print(f"sd of c / sd of y {rel_c:.2f}, sd of i / sd of y {rel_i:.2f}")
print(f"first-order autocorrelation of output {np.corrcoef(y[1:], y[:-1])[0, 1]:.2f}")
