"""The Wald ratio and two-stage least squares, by hand, on the simulated town."""
import numpy as np
from schooling_data import draw

d = draw(n=10_000, seed=1)
y, x, z = d["log_wage"], d["school"], d["near"]
n = len(y)

first = x[z == 1].mean() - x[z == 0].mean()        # first stage
reduced = y[z == 1].mean() - y[z == 0].mean()      # reduced form
print(f"first stage     {first:.4f}")
print(f"reduced form    {reduced:.4f}")
print(f"Wald ratio      {reduced / first:.4f}")

X = np.column_stack([np.ones(n), x])               # regressors
Z = np.column_stack([np.ones(n), z])               # instruments
X_hat = Z @ np.linalg.solve(Z.T @ Z, Z.T @ X)      # fitted first stage
beta = np.linalg.solve(X_hat.T @ X, X_hat.T @ y)
print(f"2SLS slope      {beta[1]:.4f}")

A_inv = np.linalg.inv(X_hat.T @ X_hat)
u = y - X @ beta                                   # residual with actual x
u_naive = y - X_hat @ beta                         # residual with fitted x
se = np.sqrt(u @ u / (n - 2) * A_inv[1, 1])
se_naive = np.sqrt(u_naive @ u_naive / (n - 2) * A_inv[1, 1])
print(f"2SLS s.e.       {se:.4f}")
print(f"naive s.e.      {se_naive:.4f}   (OLS on the fitted x)")

pi = np.linalg.lstsq(Z, x, rcond=None)[0]          # first-stage coefficients
v = x - Z @ pi
se_pi = np.sqrt(v @ v / (n - 2) * np.linalg.inv(Z.T @ Z)[1, 1])
print(f"first-stage F   {(pi[1] / se_pi) ** 2:.1f}")
