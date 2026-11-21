"""Death rates as the base of a pool; the spread of a pooled average loss (seeded simulation).

Grade 12, chapter 2 (risk and insurance).
World Development Indicators SP.DYN.CDRT.IN (crude death rate, per 1,000 people), FRA, JPN, SWE, USA, 2000-2024.
Pooling (invented): each member loses 1000 with probability 0.05, independently; for pools of n = 10 to 10,000 members,
4,000 seeded draws of the average loss per member; the 5th and 95th percentiles and the theoretical standard deviation
1000 * sqrt(0.05 * 0.95 / n). Seed 20261120.
Writes:
  out/death_rates.csv   year, FRA, JPN, SWE, USA
  out/pool_spread.csv   n, p05, p95, sd_theory
"""
import numpy as np
import pandas as pd

from econdata import wdi
from figout import write_table

ISOS = ["FRA", "JPN", "SWE", "USA"]
LOSS, P, DRAWS, SEED = 1000.0, 0.05, 4000, 20261120
NS = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]


def deaths():
    w = wdi("SP.DYN.CDRT.IN", isos=ISOS, since=2000, until=2024)
    t = w.pivot(index="year", columns="iso3", values="value")[ISOS].round(2).reset_index()
    t.columns.name = None
    return t


def pool():
    rng = np.random.default_rng(SEED)
    rows = []
    for n in NS:
        k = rng.binomial(n, P, size=DRAWS)
        avg = LOSS * k / n
        rows.append({"n": n, "p05": round(float(np.percentile(avg, 5)), 1), "p95": round(float(np.percentile(avg, 95)), 1),
                     "sd_theory": round(LOSS * np.sqrt(P * (1 - P) / n), 2)})
    return pd.DataFrame(rows)


if __name__ == "__main__":
    write_table(deaths(), __file__, "death_rates")
    write_table(pool(), __file__, "pool_spread")
