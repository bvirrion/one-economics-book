"""Charts of b1 ch. 26.

budget: 27 EU countries (Eurostat): change in the general-government balance (B9, S13,
per cent of GDP) from 2007 to 2009, against the change in real GDP growth (B1GQ,
CLV_PCH_PRE) from 2007 to 2009; least-squares slope.
cpi: United States, BLS CPI-U all items, 12-month change, monthly, 2019-2024.
"""
import numpy as np
import pandas as pd
from econdata import bls_cpi, eurostat
from figout import write_table

AGG = {"EA19", "EA20", "EA21", "EU27_2020"}
g = eurostat("gov_10dd_edpt1")
g = g[(g.unit == "PC_GDP") & (g.sector == "S13") & (g.na_item == "B9") & ~g.geo.isin(AGG)]
g = g.assign(time=g.time.astype(int)).pivot(index="geo", columns="time", values="value")
n = eurostat("nama_10_gdp")
n = n[(n.unit == "CLV_PCH_PRE") & (n.na_item == "B1GQ")]
n = n.assign(time=n.time.astype(int)).pivot(index="geo", columns="time", values="value")
d = pd.DataFrame({"bal07": g[2007], "bal09": g[2009], "gr07": n[2007], "gr09": n[2009]}).dropna()
d = d[d.index.isin(g.index)]
d["dbal"] = (d.bal09 - d.bal07).round(1)
d["dgr"] = (d.gr09 - d.gr07).round(1)
d = d.reset_index().rename(columns={"index": "geo"}).sort_values("geo")
write_table(d[["geo", "bal07", "bal09", "gr07", "gr09", "dbal", "dgr"]], __file__, "budget")
LAB = ["DE", "EE", "EL", "ES", "HU", "IE", "LV", "PL", "SK", "FI"]
write_table(d[d.geo.isin(LAB)][["geo", "dbal", "dgr"]], __file__, "budget_labels")
b, c = np.polyfit(d.dgr, d.dbal, 1)
xs = np.array([d.dgr.min() - 1, d.dgr.max() + 1])
write_table(pd.DataFrame({"x": xs.round(1), "fit": (c + b * xs).round(3)}), __file__, "budget_fit")
st = {"n": len(d), "slope": round(b, 3), "intercept": round(c, 3),
      "corr": round(d.dgr.corr(d.dbal), 3), "fell": int((d.dbal < 0).sum())}
write_table(pd.DataFrame([st]), __file__, "budget_stats")

c = bls_cpi("CUUR0000SA0")
c = c[c.period.str.match(r"M(0[1-9]|1[0-2])")].copy()
c["m"] = c.period.str[1:].astype(int)
c = c.sort_values(["year", "m"]).reset_index(drop=True)
c["yoy"] = (100 * (c.value / c.value.shift(12) - 1)).round(1)
c["t"] = (c.year + (c.m - 0.5) / 12).round(3)
w = c[(c.year >= 2019) & (c.year <= 2024)]
write_table(w[["t", "year", "m", "yoy"]], __file__, "cpi")
