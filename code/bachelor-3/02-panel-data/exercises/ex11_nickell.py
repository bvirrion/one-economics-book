"""Exercise 11: dynamic panel bias at T = 5, 10, 20 against -(1 + rho)/(T - 1)."""
import numpy as np

rng = np.random.default_rng(11)
rho, n, reps = 0.5, 500, 200
print(" T   mean estimate   bias   -(1+rho)/(T-1)")
for T in (5, 10, 20):
    est = []
    for _ in range(reps):
        a = rng.normal(size=n)
        y = a / (1 - rho) + rng.normal(size=n) / np.sqrt(1 - rho**2)
        path = []
        for s in range(50 + T + 1):
            y = a + rho * y + rng.normal(size=n)
            if s >= 50:
                path.append(y)
        Y = np.array(path).T
        yt = Y[:, 1:] - Y[:, 1:].mean(1, keepdims=True)
        yl = Y[:, :-1] - Y[:, :-1].mean(1, keepdims=True)
        est.append((yl * yt).sum() / (yl * yl).sum())
    b = np.mean(est) - rho
    print(f"{T:2d}   {np.mean(est):13.3f}   {b:6.3f}   {-(1 + rho) / (T - 1):14.3f}")
