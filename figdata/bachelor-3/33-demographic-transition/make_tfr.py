"""Chart 2: total fertility rate, 1800--2024, six countries. Gapminder Fast Track for
1800--1949 and World Bank WDI SP.DYN.TFRT.IN from 1960 (the two sources are not
joined across the 1950s). Before its first estimate for a country, Gapminder repeats that
estimate back to 1800; `first_estimate` finds the end of such a flat run (ten years or
more at one value), and the years before it are left out (South Korea before 1901, India
before 1880, Nigeria before 1925). Writes out/tfr_<iso3>_early.csv, out/tfr_<iso3>_late.csv,
out/tfr_stats.csv and out/tfr_fill.csv (first year kept per country)."""
import pandas as pd
from econdata import gapminder, wdi
from figout import write_table

SHOWN = ["GBR", "FRA", "JPN", "KOR", "IND", "NGA"]


def first_estimate(s, tol=0.005, run=10):
    """Last year of a leading run of at least `run` years equal to the first value
    (within `tol`), or the first year if there is no such run."""
    same = (s - s.iloc[0]).abs() <= tol
    k = int(same.cumprod().sum())
    return s.index[k - 1] if k >= run else s.index[0]


def tables():
    g = gapminder("children_per_woman_total_fertility", isos=SHOWN, since=1800)
    w = wdi("SP.DYN.TFRT.IN", isos=SHOWN, since=1960).dropna(subset=["value"])
    out, rows = {}, []
    for c in SHOWN:
        e = g[g.iso3 == c][["year", "value"]].rename(columns={"value": "tfr"})
        y0 = first_estimate(e.set_index("year").tfr)
        e = e[e.year >= y0]
        late = w[w.iso3 == c][["year", "value"]].rename(columns={"value": "tfr"})
        out[c] = (e.reset_index(drop=True), late.reset_index(drop=True))
        se, sl = e.set_index("year").tfr, late.set_index("year").tfr
        rows.append({"iso3": c, "first": se.index.min(), "y_first": se.iloc[0],
                     "y1800": se.get(1800, float("nan")),
                     "y1900": se.get(1900, float("nan")),
                     "y1960": sl[1960], "y2024": sl[sl.index.max()],
                     "last": sl.index.max(),
                     "below21": sl[sl < 2.1].index.min() if (sl < 2.1).any() else 0})
    return out, pd.DataFrame(rows)


if __name__ == "__main__":
    out, st = tables()
    for c, (e, late) in out.items():
        write_table(e, __file__, f"tfr_{c}_early")
        write_table(late, __file__, f"tfr_{c}_late")
    write_table(st, __file__, "tfr_stats")
