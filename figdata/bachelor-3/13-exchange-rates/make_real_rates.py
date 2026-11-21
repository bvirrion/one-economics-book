"""Chart 2: real exchange rates against the dollar, 1870--2020, for five economies
(log deviation from each country's 1870--2020 mean, in percent); and the half-lives
of the 17 economies' real rates, from an AR(1) on 1870--2020 and on 1974--2020, and
on 1870--2020 without the war years 1914--1919 and 1939--1949 (controlled official
rates and wartime inflation). The chart leaves the war years out.
Writes out/real_rates.csv (wide), out/half_lives.csv and out/half_life_stats.csv."""
import numpy as np
import pandas as pd
from figout import write_table
from jstreal import half_life, real_rates

SHOWN = ["GBR", "JPN", "CHE", "CAN", "AUS"]
PERIODS = {"all": (1870, 2020), "float": (1974, 2020)}
WARS = list(range(1914, 1920)) + list(range(1939, 1950))


def tables():
    r = real_rates()
    w = r.pivot(index="year", columns="iso3", values="q")[SHOWN]
    w = 100 * (w - w.mean())
    w = w.reindex(range(1870, 2021))
    w.loc[w.index.isin(WARS)] = np.nan
    w = w.reset_index()
    rows = []
    for iso, g in r.groupby("iso3"):
        row = {"iso3": iso}
        for name, (a, b) in PERIODS.items():
            row[f"rho_{name}"], row[f"hl_{name}"] = half_life(
                g[g.year.between(a, b)].set_index("year").q)
        row["rho_peace"], row["hl_peace"] = half_life(
            g[~g.year.isin(WARS)].set_index("year").q)
        rows.append(row)
    h = pd.DataFrame(rows)
    stats = pd.DataFrame({"stat": ["economies", "median_hl_all", "median_hl_float",
                                   "min_hl_all", "max_hl_all", "median_hl_peace"],
                          "value": [len(h), h.hl_all.median(), h.hl_float.median(),
                                    h.hl_all.min(), h.hl_all.max(), h.hl_peace.median()]})
    return w, h, stats


if __name__ == "__main__":
    w, h, s = tables()
    write_table(w, __file__, "real_rates")
    write_table(h, __file__, "half_lives")
    write_table(s, __file__, "half_life_stats")
    assert np.isfinite(h.hl_float).all()
