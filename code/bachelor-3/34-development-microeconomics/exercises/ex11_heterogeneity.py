"""Exercise 11: heterogeneity across seven invented randomized studies of a training
programme (effect on monthly earnings, dollars, with standard errors). Fixed-effect
(inverse-variance) pooled estimate, Cochran's Q, the DerSimonian--Laird tau^2 and the
random-effects pooled estimate with its 95 % interval."""
import numpy as np

effects = np.array([12.0, 3.0, 25.0, -4.0, 8.0, 15.0, 1.0])
se = np.array([5.0, 4.0, 9.0, 6.0, 3.0, 7.0, 4.0])
w = 1 / se**2
fe = (w * effects).sum() / w.sum()
q = (w * (effects - fe) ** 2).sum()
k = len(effects)
tau2 = max(0.0, (q - (k - 1)) / (w.sum() - (w**2).sum() / w.sum()))
wr = 1 / (se**2 + tau2)
re = (wr * effects).sum() / wr.sum()
se_re = np.sqrt(1 / wr.sum())
print(f"fixed effect {fe:.2f} (se {np.sqrt(1 / w.sum()):.2f})")
print(f"Q = {q:.2f} on {k - 1} degrees of freedom")
print(f"tau^2 = {tau2:.2f} (tau = {np.sqrt(tau2):.2f})")
lo, hi = re - 1.96 * se_re, re + 1.96 * se_re
print(f"random effects {re:.2f}, interval [{lo:.2f}, {hi:.2f}]")
