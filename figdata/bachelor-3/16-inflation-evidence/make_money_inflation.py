"""Chart 2: average broad-money growth against average consumer-price inflation,
1990--2024, countries with at least 20 years of both (WDI FM.LBL.BMNY.ZG,
FP.CPI.TOTL.ZG). Averages are of log growth, 100 x (exp(mean(ln(1 + x/100))) - 1),
so that a few years of very high inflation do not dominate. Writes out/mi.csv,
out/mi_line.csv (two points of the equality line, for the log-log chart) and
out/mi_stats.csv: countries; the slope of average continuously compounded inflation on
average continuously compounded money growth (rates, not logs of rates); the slope of
the log-log regression of the plotted values, over the countries with positive money
growth; and the countries that a log axis cannot show."""
import numpy as np
import pandas as pd
import statsmodels.api as sm
from econdata import wdi, wdi_countries
from figout import write_table


def tables():
    c = wdi_countries()
    real = set(c.loc[c.Region.notna(), "Country Code"])
    m = wdi("FM.LBL.BMNY.ZG", since=1990, until=2024).rename(columns={"value": "m"})
    p = wdi("FP.CPI.TOTL.ZG", since=1990, until=2024).rename(columns={"value": "p"})
    d = m.merge(p[["iso3", "year", "p"]], on=["iso3", "year"]).dropna()
    d = d[d.iso3.isin(real) & (d.m > -100) & (d.p > -100)]
    d["lm"], d["lp"] = np.log1p(d.m / 100), np.log1p(d.p / 100)
    g = d.groupby("iso3").agg(lm=("lm", "mean"), lp=("lp", "mean"),
                              years=("m", "size")).reset_index()
    g = g[g.years >= 20].reset_index(drop=True)
    g["money"], g["infl"] = 100 * np.expm1(g.lm), 100 * np.expm1(g.lp)
    r = sm.OLS(g.lp, sm.add_constant(g.lm)).fit()
    pos = g[(g.money > 0) & (g.infl > 0)]
    ll = sm.OLS(np.log(pos.infl), sm.add_constant(np.log(pos.money))).fit()
    stats = pd.DataFrame({"stat": ["countries", "slope", "slope_se", "r2",
                                   "above_20pct", "loglog_slope", "loglog_r2",
                                   "not_plotted"],
                          "value": [len(g), r.params.iloc[1], r.bse.iloc[1],
                                    r.rsquared, (g.infl > 20).sum(), ll.params.iloc[1],
                                    ll.rsquared, len(g) - len(pos)]})
    return g[["iso3", "money", "infl"]], stats


if __name__ == "__main__":
    g, s = tables()
    write_table(g, __file__, "mi")
    write_table(pd.DataFrame({"x": [1, 200], "y": [1, 200]}), __file__, "mi_line")
    write_table(s, __file__, "mi_stats")
