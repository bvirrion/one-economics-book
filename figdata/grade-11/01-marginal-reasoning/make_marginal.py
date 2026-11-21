"""Life expectancy against health spending per person (2019), and Brenland's marginal and average income tax rates.

Grade 11, chapter 1 (marginal-reasoning). World Bank WDI SP.DYN.LE00.IN (life expectancy at birth, years) and
SH.XPD.CHEX.PP.CD (current health expenditure per person, PPP dollars), 2019, countries only. The fitted curve
is life = a + b log10(health); its slope gives the years gained per extra 100 dollars at each level of spending.
Brenland: code/shared/country TAX_BANDS (invented).
Writes:
  out/life.csv        iso3, health, life
  out/life_fit.csv    n, a, b (years per tenfold spending), gain100_at100, gain100_at1000, gain100_at5000
                      (years gained from 100 more dollars, at spending of 100, 1000 and 5000 dollars)
  out/life_curve.csv  health, life (the fitted curve, for the chart)
  out/tax_rates.csv   income (dalens a year, step 1000), marginal, average (percent)
"""
import numpy as np
import pandas as pd

import country
from econdata import wdi
from figout import write_table

YEAR = 2019


def life():
    a = wdi("SP.DYN.LE00.IN", countries_only=True)
    h = wdi("SH.XPD.CHEX.PP.CD", countries_only=True)
    d = (h[h.year == YEAR][["iso3", "value"]].rename(columns={"value": "health"})
         .merge(a[a.year == YEAR][["iso3", "value"]].rename(columns={"value": "life"}), on="iso3").dropna())
    d = d.sort_values("iso3").reset_index(drop=True)
    d["health"] = d.health.round(1)
    d["life"] = d.life.round(1)
    b, a0 = np.polyfit(np.log10(d.health), d.life, 1)

    def gain(x):
        return round(float(a0 + b * np.log10(x + 100) - (a0 + b * np.log10(x))), 2)

    fit = pd.DataFrame({"n": [len(d)], "a": [round(a0, 2)], "b": [round(b, 2)], "gain100_at100": [gain(100)],
                        "gain100_at1000": [gain(1000)], "gain100_at5000": [gain(5000)]})
    xs = np.round(np.logspace(np.log10(20), np.log10(12000), 40), 1)
    curve = pd.DataFrame({"health": xs, "life": np.round(a0 + b * np.log10(xs), 2)})
    return d, fit, curve


def tax_rates():
    bands = country.TAX_BANDS
    inc = np.arange(1000, 150001, 1000)
    rows = []
    for g in inc:
        t = sum((min(g, hi) - lo) * r for (lo, r), (hi, _) in zip(bands, bands[1:] + [(float("inf"), 0)]) if g > lo)
        m = [r for lo, r in bands if g >= lo][-1]
        rows.append({"income": int(g), "marginal": round(100 * m, 1), "average": round(100 * t / g, 2)})
    return pd.DataFrame(rows)


if __name__ == "__main__":
    d, fit, curve = life()
    write_table(d, __file__, "life")
    write_table(fit, __file__, "life_fit")
    write_table(curve, __file__, "life_curve")
    write_table(tax_rates(), __file__, "tax_rates")
