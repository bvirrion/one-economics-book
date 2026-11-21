"""Charts of b1 ch. 20.

invest_income: GDP per person 2019 (PWT rgdpe/pop, PPP dollars) against the average
investment share (csh_i) over the years 1960-2019 available for the country (at least 30);
Bermuda, whose recorded average share exceeds 100%, is left out.
mrw: the augmented Solow regression, ln y_2019 = a + b [ln s - ln(n + 0.05)] + c ln hc_2019,
with n the average growth rate of population over the same years and 0.05 for g + delta
(the convention of the cited paper); fitted values against actual; implied capital share
alpha = b / (1 + b). Least squares with numpy.
"""
import numpy as np
import pandas as pd
from econdata import pwt
from figout import write_table

p = pwt(None, 1960, 2019, ["csh_i", "hc", "pop", "rgdpe"])
rows = []
for iso, g in p.groupby("iso3"):
    g = g.dropna(subset=["csh_i", "pop"]).sort_values("year")
    last = p[(p.iso3 == iso) & (p.year == 2019)]
    if len(g) < 30 or last.empty or last.rgdpe.isna().any():
        continue
    y0, y1 = g.year.iloc[0], g.year.iloc[-1]
    n = np.log(g["pop"].iloc[-1] / g["pop"].iloc[0]) / (y1 - y0)
    rows.append({"iso3": iso, "country": g.country.iloc[0].replace(",", ""), "s": g.csh_i.mean(), "n": n,
                 "hc": last.hc.iloc[0], "y": last.rgdpe.iloc[0] / last["pop"].iloc[0], "years": len(g)})
d = pd.DataFrame(rows)
d = d[d.s < 1]  # one territory records an average investment share above 100%: left out
out = d[["iso3", "country", "s", "y"]].copy()
out["s"] = (100 * out.s).round(2)
out["y"] = out.y.round(0)
write_table(out, __file__, "invest_income")
st = {"n": len(d), "corr_lny_s": round(np.corrcoef(np.log(d.y), d.s)[0, 1], 2)}
q = d.s.quantile([0.25, 0.75])
st["y_low_quart"] = round(d[d.s <= q.iloc[0]].y.median(), 0)
st["y_high_quart"] = round(d[d.s >= q.iloc[1]].y.median(), 0)
st["s_low_quart"] = round(100 * q.iloc[0], 1)
st["s_high_quart"] = round(100 * q.iloc[1], 1)

m = d.dropna(subset=["hc"]).copy()
m = m[(m.s > 0) & (m.n + 0.05 > 0)]
X = np.column_stack([np.ones(len(m)), np.log(m.s) - np.log(m.n + 0.05), np.log(m.hc)])
yv = np.log(m.y.values)
beta, *_ = np.linalg.lstsq(X, yv, rcond=None)
fit = X @ beta
r2 = 1 - ((yv - fit) ** 2).sum() / ((yv - yv.mean()) ** 2).sum()
m["fitted"] = np.exp(fit).round(0)
m["y"] = m.y.round(0)
write_table(m[["iso3", "country", "y", "fitted"]], __file__, "mrw_fit")
b = beta[1]
st.update({"mrw_n": len(m), "b": round(b, 3), "c": round(beta[2], 3), "r2": round(r2, 3),
           "alpha": round(b / (1 + b), 3)})
X0 = np.column_stack([np.ones(len(m)), np.log(m.s) - np.log(m.n + 0.05)])
b0, *_ = np.linalg.lstsq(X0, yv, rcond=None)
f0 = X0 @ b0
st.update({"basic_b": round(b0[1], 3), "basic_alpha": round(b0[1] / (1 + b0[1]), 3),
           "basic_r2": round(1 - ((yv - f0) ** 2).sum() / ((yv - yv.mean()) ** 2).sum(), 3)})
write_table(pd.DataFrame([st]), __file__, "solow_stats")
write_table(out[out.iso3.isin(["SGP", "CHN", "IND", "NER", "NOR"])], __file__, "invest_points")

# postwar recoveries: average growth of real GDP per person (rgdpna/pop), 1950-1973
q = pwt(["DEU", "JPN", "FRA", "GBR", "USA"], 1950, 1973, ["rgdpna", "pop"])
rec = []
for iso, g in q.groupby("iso3"):
    g = g.sort_values("year")
    y = g.rgdpna / g["pop"]
    rec.append({"iso3": iso, "growth": round(100 * np.log(y.iloc[-1] / y.iloc[0]) / 23, 2),
                "ratio_usa_1950": None})
r = pd.DataFrame(rec)
q50 = q[q.year == 1950].set_index("iso3")
yp = (q50.rgdpna / q50["pop"])
r["ratio_usa_1950"] = [round(yp[i] / yp["USA"], 3) for i in r.iso3]
write_table(r, __file__, "postwar")
mf = m[m.iso3.isin(["IND", "NER", "USA", "CHN"])][["iso3", "country", "y", "fitted"]]
write_table(mf, __file__, "mrw_points")
