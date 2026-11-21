"""Opening chart: GDP per person, United Kingdom series of the Maddison Project
2023, 1252--1850 (2011 dollars). Writes out/england.csv and out/england_stats.csv
(levels in chosen years; growth by half-century between decade means, the ten years
from a - 5 to a + 4, because the annual series swings by 10--15 % from one year to the
next and single-year endpoints would measure those swings)."""
import numpy as np
import pandas as pd
from econdata import maddison
from figout import write_table

YEARS = [1300, 1340, 1348, 1351, 1400, 1450, 1500, 1600, 1650, 1700, 1800, 1850]


def table():
    m = maddison(isos=["GBR"], since=1252, until=1850)
    return m[["year", "gdppc"]].dropna().reset_index(drop=True)


def decade_mean(s, a):
    return s.loc[a - 5:a + 4].mean()


def stats(t):
    s = t.set_index("year").gdppc
    rows = [{"stat": f"y{y}", "value": s[y]} for y in YEARS]
    d = {a: decade_mean(s, a) for a in range(1300, 1851, 50)}
    rows += [{"stat": f"d{a}", "value": v} for a, v in d.items()]
    for a in range(1300, 1850, 50):
        rows.append({"stat": f"g{a}", "value": 100 * np.log(d[a + 50] / d[a]) / 50})
    rows.append({"stat": "g1300_1650", "value": 100 * np.log(d[1650] / d[1300]) / 350})
    rows.append({"stat": "rise1650_1700", "value": 100 * (d[1700] / d[1650] - 1)})
    rows.append({"stat": "plague_rise", "value": 100 * (s[1351] / s[1348] - 1)})
    return pd.DataFrame(rows)


if __name__ == "__main__":
    t = table()
    write_table(t, __file__, "england")
    write_table(stats(t), __file__, "england_stats")
