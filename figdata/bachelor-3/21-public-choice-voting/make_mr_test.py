"""A cross-country test of the Meltzer-Richard prediction: average central-
government expense (WDI GC.XPN.TOTL.GD.ZS) against the average Gini index
(SI.POV.GINI), 2010--2019, countries with at least three years of each; with and
without log GDP per person (NY.GDP.PCAP.PP.KD) as a control. The WDI Gini is of
disposable income or consumption, after redistribution, so this regression cannot test
the model. The European rows use the Eurostat Gini before social transfers (after
taxes; ilc_di12b, pensions counted as transfers, and ilc_di12c, pensions counted as
income), averaged over 2010--2019, against the same spending measure. Writes
out/mr_test.csv."""
import numpy as np
import pandas as pd
import statsmodels.api as sm
from econdata import eurostat, wdi, wdi_countries
from figout import write_table


def table():
    c = wdi_countries()
    real = set(c.loc[c.Region.notna(), "Country Code"])
    parts = []
    for code, name in (("GC.XPN.TOTL.GD.ZS", "s"), ("SI.POV.GINI", "gini"),
                       ("NY.GDP.PCAP.PP.KD", "y")):
        x = wdi(code, since=2010, until=2019).dropna()
        x = x[x.iso3.isin(real)]
        g = x.groupby("iso3").value.agg(["mean", "size"])
        parts.append(g[g["size"] >= 3]["mean"].rename(name))
    d = pd.concat(parts, axis=1).dropna()
    r1 = sm.OLS(d.s, sm.add_constant(d.gini)).fit()
    r2 = sm.OLS(d.s, sm.add_constant(pd.DataFrame({"gini": d.gini,
                                                    "ly": np.log(d.y)}))).fit()
    rows = {"countries": len(d), "slope": r1.params["gini"], "se": r1.bse["gini"],
            "slope_ctrl": r2.params["gini"], "se_ctrl": r2.bse["gini"]}
    e = europe()
    for col in ("b", "c"):
        r = sm.OLS(e.s, sm.add_constant(e[col])).fit()
        rows[f"eu_slope_{col}"], rows[f"eu_se_{col}"] = r.params[col], r.bse[col]
    rows["eu_countries"] = len(e)
    return pd.DataFrame({"stat": list(rows), "value": list(rows.values())})


FIX = {"EL": "GR", "UK": "GB"}


def pre_transfer_gini(name):
    cc = wdi_countries()[["Country Code", "2-alpha code"]].dropna()
    iso = dict(zip(cc["2-alpha code"], cc["Country Code"]))
    d = eurostat(name)
    d = d[d.time.between(2010, 2019) & (d.statinfo == "GINI_HND")].copy()
    d["iso3"] = [iso.get(FIX.get(g, g)) for g in d.geo]
    return d.dropna(subset=["iso3"]).groupby("iso3").value.mean()


def europe():
    s = wdi("GC.XPN.TOTL.GD.ZS", since=2010, until=2019).dropna()
    s = s.groupby("iso3").value.mean().rename("s")
    return pd.concat([pre_transfer_gini("ilc_di12b").rename("b"),
                      pre_transfer_gini("ilc_di12c").rename("c"), s], axis=1).dropna()


if __name__ == "__main__":
    write_table(table(), __file__, "mr_test")
