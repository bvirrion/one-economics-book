"""Exercise 8: the geography instrument without the population control."""
import numpy as np
import pandas as pd
from econdata import gravity, pwt, wdi
from ivtools import first_stage_f, ols, tsls

cols = ["year", "iso3_o", "iso3_d", "tradeflow_baci", "distw_harmonic",
        "contig", "pop_o", "pop_d", "gdp_o"]
g = gravity(2019, 2019, columns=cols)
back = g.rename(columns={"iso3_o": "iso3_d", "iso3_d": "iso3_o",
                         "tradeflow_baci": "back"})[["iso3_o", "iso3_d", "back"]]
g = g.merge(back, on=["iso3_o", "iso3_d"], how="left").fillna({"back": 0})
g["share"] = (g.tradeflow_baci + g.back) / g.gdp_o
g = g.dropna(subset=["share", "pop_o", "pop_d", "distw_harmonic"])
g = g[g.share > 0]
G = np.column_stack([np.ones(len(g)), np.log(g.distw_harmonic),
                     np.log(g.pop_o), np.log(g.pop_d), g.contig])
g["fit"] = np.exp(G @ ols(np.log(g.share), G)["beta"])
built = g.groupby("iso3_o").fit.sum().mul(100).rename("built")
w = wdi("NE.TRD.GNFS.ZS", since=2019, until=2019, countries_only=True)
p = pwt(since=2019, until=2019, cols=["rgdpo", "emp", "pop"]).set_index("iso3")
d = pd.concat([built, w.set_index("iso3").value.rename("trade"), p], axis=1,
              join="inner").dropna()
y = np.log(d.rgdpo / d.emp)
one = np.ones(len(d))
X = np.column_stack([one, np.log(d.trade)])
Z = np.column_stack([one, np.log(d.built)])
print(f"first-stage F             {first_stage_f(X[:, 1], Z[:, 1], Z[:, :1]):.1f}")
for name, r in (("OLS ", ols(y, X, se="HC1")), ("2SLS", tsls(y, X, Z, se="HC1"))):
    print(f"{name} elasticity          {r['beta'][1]:.3f}  (s.e. {r['se'][1]:.3f})")
lpop = np.log(d["pop"])
print(f"corr(log built, log pop)  {np.corrcoef(np.log(d.built), lpop)[0, 1]:.3f}")
print(f"corr(log trade, log pop)  {np.corrcoef(np.log(d.trade), lpop)[0, 1]:.3f}")
