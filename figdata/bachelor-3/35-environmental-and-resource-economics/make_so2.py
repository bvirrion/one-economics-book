"""Opening chart: sulphur dioxide emissions per person against GDP per person,
1850--2019, six economies, every fifth year (CEDS emissions in kt; Maddison Project
2023 population and GDP per person, 2011 dollars). Writes out/so2_<iso3>.csv (lx =
log10 GDP per person, kg = kilograms of SO2 per person) and out/so2_stats.csv (the
peak year, its income and level, and the 2019 level)."""
import numpy as np
import pandas as pd
from econdata import ceds, maddison
from figout import write_table

SHOWN = ["GBR", "USA", "DEU", "JPN", "KOR", "CHN"]


def paths():
    s = ceds("so2", isos=SHOWN, since=1850, until=2019)[["iso3", "year", "value"]]
    m = maddison(isos=SHOWN, since=1850, until=2019)[["iso3", "year", "gdppc", "pop"]]
    d = s.merge(m, on=["iso3", "year"]).dropna()
    d["kg"] = 1000 * d.value / d["pop"]
    d["lx"] = np.log10(d.gdppc)
    return d


def stats(d):
    rows = []
    for c in SHOWN:
        x = d[d.iso3 == c].set_index("year")
        t = x.kg.idxmax()
        rows.append({"iso3": c, "first": x.index.min(), "peak_year": t,
                     "peak_kg": x.kg[t], "peak_gdppc": x.gdppc[t], "kg2019": x.kg[2019],
                     "gdppc2019": x.gdppc[2019]})
    return pd.DataFrame(rows)


if __name__ == "__main__":
    d = paths()
    for c in SHOWN:
        x = d[(d.iso3 == c) & ((d.year % 5 == 0) | (d.year == 2019))]
        write_table(x[["year", "lx", "kg"]], __file__, f"so2_{c}")
    write_table(stats(d), __file__, "so2_stats")
