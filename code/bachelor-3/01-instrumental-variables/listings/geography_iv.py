"""Does trade raise output per worker? Geography as an instrument, 2019."""
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
g["share"] = (g.tradeflow_baci + g.back) / g.gdp_o      # pair trade / GDP
g = g.dropna(subset=["share", "pop_o", "pop_d", "distw_harmonic"])
g = g[g.share > 0]

# 1. A gravity fit that sees only geography and size
G = np.column_stack([np.ones(len(g)), np.log(g.distw_harmonic),
                     np.log(g.pop_o), np.log(g.pop_d), g.contig])
g["fit"] = np.exp(G @ ols(np.log(g.share), G)["beta"])
built = g.groupby("iso3_o").fit.sum().mul(100).rename("built")

# 2. Actual trade share, output per worker, population
w = wdi("NE.TRD.GNFS.ZS", since=2019, until=2019, countries_only=True)
p = pwt(since=2019, until=2019, cols=["rgdpo", "emp", "pop"]).set_index("iso3")
d = pd.concat([built, w.set_index("iso3").value.rename("trade"), p], axis=1,
              join="inner").dropna()
y = np.log(d.rgdpo / d.emp)
one, lpop = np.ones(len(d)), np.log(d["pop"])
X = np.column_stack([one, lpop, np.log(d.trade)])
Z = np.column_stack([one, lpop, np.log(d.built)])

print(f"countries                 {len(d)}")
print(f"first-stage F             {first_stage_f(X[:, 2], Z[:, 2], Z[:, :2]):.1f}")
for name, r in (("OLS ", ols(y, X, se="HC1")), ("2SLS", tsls(y, X, Z, se="HC1"))):
    b, s = r["beta"][2], r["se"][2]
    print(f"{name} elasticity          {b:.3f}  (s.e. {s:.3f})")
