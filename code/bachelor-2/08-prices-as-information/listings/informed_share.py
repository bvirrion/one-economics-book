"""A market where some traders pay for information and the rest learn from the price."""

import numpy as np

a, c, s_z = 1.0, 0.1116, 0.25  # risk aversion, cost of the signal, noise in supply
phi = 0.433  # share of informed traders (the equilibrium share at this cost)
rng = np.random.default_rng(808)
n = 400_000
theta, eps, z = rng.normal(0, 1, n), rng.normal(0, 1, n), rng.normal(0, s_z, n)
v = theta + eps  # the asset's value; the informed see theta

xi = theta - (a / phi) * z  # what the price reveals
kappa = 1 / (1 + (s_z / phi) ** 2)  # E[theta | xi] = kappa xi
var_u = 1 + (1 - kappa)  # Var(v | xi) for the uninformed
b = (phi + (1 - phi) * kappa / var_u) / (phi + (1 - phi) / var_u)
p = b * xi  # the equilibrium price

x_inf = (theta - p) / a  # demand of an informed trader (Var(v | theta) = 1)
x_un = (kappa * p / b - p) / (a * var_u)  # demand of an uninformed trader
clear = phi * x_inf + (1 - phi) * x_un - z
fit = np.polyfit(p, theta, 1)
u_inf = -np.exp(-a * (x_inf * (v - p) - c)).mean()
u_un = -np.exp(-a * x_un * (v - p)).mean()
print(f"every market clears           {bool(np.allclose(clear, 0))}")
print(
    f"theta given the price: slope {fit[0]:.3f}, error variance "
    f"{np.var(theta - np.polyval(fit, p)):.3f}"
)
print(f"expected utility, informed   {u_inf:.4f}")
print(f"expected utility, uninformed {u_un:.4f}")
