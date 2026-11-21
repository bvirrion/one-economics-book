"""Chart 3: the uncovered-interest-parity regression. For 17 economies against the
United States, 1974--2019: the depreciation of the currency against the dollar over
the next year, 100 x (log xrusd_{t+1} - log xrusd_t), against the short-term interest
differential stir_i - stir_USA in year t (JST annual data). UIP predicts a slope of 1.
Writes out/uip.csv, out/uip_fit.csv and out/uip_stats.csv."""
import numpy as np
import pandas as pd
import statsmodels.api as sm
from econdata import jst
from figout import write_table


def table():
    j = jst(cols=["xrusd", "stir"], since=1974, until=2020)
    j = j.sort_values(["iso3", "year"])
    us = j[j.iso3 == "USA"].set_index("year").stir
    j = j[j.iso3 != "USA"].copy()
    j["dep"] = j.groupby("iso3").xrusd.transform(
        lambda s: 100 * np.log(s).diff().shift(-1))
    j["diff"] = j.stir - j.year.map(us)
    return j[["iso3", "year", "diff", "dep"]].dropna().reset_index(drop=True)


def tables():
    d = table()
    r = sm.OLS(d.dep, sm.add_constant(d["diff"])).fit()
    xs = np.array([d["diff"].min(), d["diff"].max()])
    fit = pd.DataFrame({"diff": xs, "dep": r.params.iloc[0] + r.params.iloc[1] * xs,
                        "uip": xs})
    stats = pd.DataFrame({"stat": ["obs", "economies", "slope", "slope_se", "r2"],
                          "value": [len(d), d.iso3.nunique(), r.params.iloc[1],
                                    r.bse.iloc[1], r.rsquared]})
    return d, fit, stats


if __name__ == "__main__":
    d, fit, stats = tables()
    write_table(d, __file__, "uip")
    write_table(fit, __file__, "uip_fit")
    write_table(stats, __file__, "uip_stats")
