"""Exercise 8: entry thresholds from an invented table of isolated towns.

Each of 400 towns has a population (thousands) and a number of dentists. A town
supports N dentists if population x v_N / N covers a fixed cost F, where v_N is the
variable profit per thousand residents in a market with N dentists. The script
estimates each threshold S_N as the midpoint between the median population of the
ten largest towns with fewer than N dentists and that of the ten smallest towns with
at least N, then prints the threshold per dentist, S_N / N.
"""
import numpy as np

rng = np.random.default_rng(27)
v = np.array([10.0, 7.0, 6.0, 5.8, 5.7])
pop = rng.uniform(0.1, 6.0, 400)
fixed = 5.0 * rng.lognormal(0, 0.05, 400)
dentists = np.array([sum(p * v[n - 1] / n >= f for n in range(1, 6))
                     for p, f in zip(pop, fixed)])
for n in range(1, 6):
    below, above = np.sort(pop[dentists < n]), np.sort(pop[dentists >= n])
    s_n = (np.median(below[-10:]) + np.median(above[:10])) / 2
    print(f"N = {n}: threshold {s_n:5.2f} thousand, per dentist {s_n / n:4.2f}")
