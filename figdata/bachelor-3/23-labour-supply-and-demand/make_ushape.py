"""Chart 3: ratio of female to male labour-force participation (WDI
SL.TLF.CACT.FM.ZS, percent) against GDP per person (NY.GDP.PCAP.PP.KD), countries,
2019, with a fitted quadratic in log income. Writes out/ushape.csv, out/ushape_fit.csv
and out/ushape_stats.csv (coefficients, minimum)."""
import numpy as np
import pandas as pd
import statsmodels.api as sm
from econdata import wdi, wdi_countries
from figout import write_table


def tables(year=2019):
    c = wdi_countries()
    real = set(c.loc[c.Region.notna(), "Country Code"])
    r = wdi("SL.TLF.CACT.FM.ZS", since=year, until=year).rename(columns={"value": "r"})
    y = wdi("NY.GDP.PCAP.PP.KD", since=year, until=year).rename(columns={"value": "y"})
    d = r.merge(y[["iso3", "y"]], on="iso3").dropna()
    d = d[d.iso3.isin(real)].reset_index(drop=True)
    x = np.log(d.y)
    m = sm.OLS(d.r, sm.add_constant(pd.DataFrame({"x": x, "x2": x**2}))).fit()
    b0, b1, b2 = m.params
    grid = np.linspace(x.min(), x.max(), 60)
    fit = pd.DataFrame({"y": np.exp(grid), "r": b0 + b1 * grid + b2 * grid**2})
    xmin = -b1 / (2 * b2)
    st = pd.DataFrame({"stat": ["countries", "b1", "b2", "b2_se", "y_min", "r_min",
                                "r2"],
                       "value": [len(d), b1, b2, m.bse["x2"], np.exp(xmin),
                                 b0 + b1 * xmin + b2 * xmin**2, m.rsquared]})
    return d[["iso3", "y", "r"]], fit, st


if __name__ == "__main__":
    d, fit, st = tables()
    write_table(d, __file__, "ushape")
    write_table(fit, __file__, "ushape_fit")
    write_table(st, __file__, "ushape_stats")
