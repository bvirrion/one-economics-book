"""Exercise 11: estimating a firm-level labour supply elasticity.

Five hundred invented firms face the same supply curve L = 10 w^4 and differ in
productivity: each sets its monopsony wage, w = MRP x eps / (1 + eps) with eps = 4.
Measurement error is added to wages and employment. A regression of log employment
on log wage across firms traces the supply curve; the markdown follows.
"""
import numpy as np

rng = np.random.default_rng(26)
eps = 4.0
mrp = rng.lognormal(np.log(20), 0.3, 500)
w = mrp * eps / (1 + eps)
lab = 10 * w**eps
lw = np.log(w) + rng.normal(0, 0.02, 500)
ll = np.log(lab) + rng.normal(0, 0.05, 500)
slope = np.polyfit(lw, ll, 1)[0]
print(f"estimated supply elasticity: {slope:.2f}")
print(f"implied gap between product and wage: {100 / (1 + slope):.1f} % of MRP")
