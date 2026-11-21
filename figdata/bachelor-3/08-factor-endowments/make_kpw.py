"""Capital per worker against output per worker, 2019, all countries with both in PWT
11.0 (rnna / emp and rgdpo / emp, thousands of 2021 dollars per person engaged), with
the least-squares line of log output per worker on log capital per worker; also the
median capital share of income (1 - labsh) over the countries with labsh in 2019.
Writes out/kpw.csv (country, k, y), out/kpw_fit.csv, out/kpw_stats.csv."""
import numpy as np
import pandas as pd
from econdata import pwt
from figout import write_table


def tables():
    d = pwt(since=2019, until=2019, cols=["rnna", "emp", "rgdpo"]).dropna()
    d = d[d.emp > 0]
    k, y = d.rnna / d.emp / 1000, d.rgdpo / d.emp / 1000
    b, a = np.polyfit(np.log(k), np.log(y), 1)
    ks = np.exp(np.linspace(np.log(k.min()), np.log(k.max()), 30))
    fit = pd.DataFrame({"k": ks, "y": np.exp(a + b * np.log(ks))})
    labsh = pwt(since=2019, until=2019, cols=["labsh"]).labsh.dropna()
    stats = pd.DataFrame({"stat": ["countries", "slope", "k_ratio_90_10",
                                   "median_capital_share", "countries_labsh"],
                          "value": [len(d), b, k.quantile(0.9) / k.quantile(0.1),
                                    (1 - labsh).median(), len(labsh)]})
    pts = pd.DataFrame({"country": d.country.str.replace(",", "", regex=False),
                        "k": k.values, "y": y.values})
    return pts, fit, stats


if __name__ == "__main__":
    p, f, s = tables()
    write_table(p, __file__, "kpw")
    write_table(f, __file__, "kpw_fit")
    write_table(s, __file__, "kpw_stats")
