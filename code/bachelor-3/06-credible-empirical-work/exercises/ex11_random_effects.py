"""Exercise 11: a random-effects mean by DerSimonian--Laird for eight studies."""
import numpy as np
from metatools import dersimonian_laird, fixed_effect

est = np.array([0.12, 0.05, 0.30, 0.18, -0.02, 0.22, 0.09, 0.15])
se = np.array([0.05, 0.04, 0.10, 0.06, 0.05, 0.08, 0.03, 0.07])
m, m_se = fixed_effect(est, se)
r, r_se, tau2, q = dersimonian_laird(est, se)
print(f"fixed effect: {m:.4f} (s.e. {m_se:.4f})")
print(f"Q = {q:.2f} on {len(est) - 1} degrees of freedom; tau^2 = {tau2:.5f},"
      f" tau = {np.sqrt(tau2):.4f}")
print(f"random effects: {r:.4f} (s.e. {r_se:.4f})")
