"""g8-06 Banks, Saving and Interest.

long_rates.csv  year, usa, gbr, fra, deu, ita: long-term government bond rate, percent, 1870-2020 (JST ltrate).
                Japan is left out: its JST long rate jumps between about 6 and 15 % from one year to the next in
                1953-1963, a series break rather than a market movement.
spread.csv      year, spread: United States, long rate minus short rate, percentage points, 1870-2020 (JST)
us_real.csv     year, stir, inflation, real: United States short rate, consumer-price inflation (JST cpi) and their
                difference, selected years
brenland.csv    year, policy_rate, cpi, inflation, rate_minus_inflation: Brenland 2000-2025 (invented)
facts.csv       name, value
"""
import pandas as pd

from country import load
from econdata import jst
from figout import write_table

L5 = {"USA": "usa", "GBR": "gbr", "FRA": "fra", "DEU": "deu", "ITA": "ita"}
YEARS = [1975, 1981]


def _p(col):
    return jst(cols=[col]).pivot(index="year", columns="iso3", values=col)


def long_rates():
    return _p("ltrate").loc[1870:2020, list(L5)].round(2).rename(columns=L5).rename_axis("year").reset_index()


def spread():
    s = (_p("ltrate").USA - _p("stir").USA).loc[1870:2020].round(2)
    return pd.DataFrame({"year": s.index, "spread": s.values})


def us_real():
    stir = _p("stir").USA
    inf = (_p("cpi").USA.pct_change() * 100).round(2)
    out = pd.DataFrame({"stir": stir.round(2), "inflation": inf}).loc[YEARS]
    out["real"] = (out.stir - out.inflation).round(2)
    return out.rename_axis("year").reset_index()


def brenland():
    a = load("accounts").set_index("year")[["policy_rate", "cpi"]]
    a["inflation"] = (100 * (a.cpi / a.cpi.shift(1) - 1)).round(1)
    a["rate_minus_inflation"] = (a.policy_rate - a.inflation).round(2)
    return a.reset_index()


def facts():
    lr = long_rates().set_index("year")
    sp = spread().set_index("year").spread
    rows = []
    for c in L5.values():
        rows += [(f"{c}_max", lr[c].max()), (f"{c}_max_year", int(lr[c].idxmax())), (f"{c}_2020", lr[c][2020])]
    rows += [("spread_years", int(sp.notna().sum())), ("spread_positive", int((sp > 0).sum())),
             ("spread_min_year", int(sp.idxmin())), ("spread_min", sp.min()),
             ("spread_1929", sp[1929]), ("spread_1979", sp[1979]), ("spread_1980", sp[1980]),
             ("spread_1981", sp[1981])]
    return pd.DataFrame(rows, columns=["name", "value"])


if __name__ == "__main__":
    write_table(long_rates(), __file__, "long_rates")
    write_table(spread(), __file__, "spread")
    write_table(us_real(), __file__, "us_real")
    write_table(brenland(), __file__, "brenland")
    write_table(facts(), __file__, "facts")
