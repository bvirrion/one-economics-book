"""Charts of b1 ch. 23.

velocity: JST R6 nominal GDP / broad money, United States, United Kingdom, Germany, Japan,
1950-2020.
qt_decades: JST R6, 18 economies, decade averages 1870-2019 of broad-money growth and CPI
inflation (log differences, per cent a year), decades with both complete; fit and correlation.
fisher: the same decades, short-term interest rate (stir) against inflation; slope, for all
decades and for those from 1960.
bolivia: WDI broad money (% of GDP) and CPI inflation, Bolivia and Peru, 1980-1996.
"""
import numpy as np
import pandas as pd
from econdata import jst, wdi
from figout import write_table

j = jst(["USA", "GBR", "DEU", "JPN"], 1950, 2020, ["gdp", "money"])
j["v"] = (j.gdp / j.money).round(3)
v = j.pivot(index="year", columns="iso3", values="v")
v.columns = [c.lower() for c in v.columns]
write_table(v.reset_index(), __file__, "velocity")
write_table(j[(j.iso3 == "USA") & j.year.isin([1960, 1980, 1990, 2000, 2019, 2020])][["year", "v"]], __file__,
            "velocity_us")

a = jst(None, 1869, 2019, ["money", "cpi", "stir"]).sort_values(["iso3", "year"])
a["gm"] = 100 * np.log(a.money).groupby(a.iso3).diff()
a["pi"] = 100 * np.log(a.cpi).groupby(a.iso3).diff()
a = a[a.year >= 1870]
a["decade"] = (a.year // 10) * 10
rows = []
for (iso, dec), g in a.groupby(["iso3", "decade"]):
    if g.gm.notna().sum() == 10 and g.pi.notna().sum() == 10:
        rows.append({"iso3": iso, "decade": dec, "gm": round(g.gm.mean(), 2), "pi": round(g.pi.mean(), 2),
                     "stir": round(g.stir.mean(), 2) if g.stir.notna().sum() == 10 else np.nan})
d = pd.DataFrame(rows)
qt = d[(d.pi > -10) & (d.pi < 60)]
write_table(qt[["iso3", "decade", "gm", "pi"]], __file__, "qt_decades")
b, c = np.polyfit(qt.gm, qt.pi, 1)
fx = np.array([-5, 40])
write_table(pd.DataFrame({"gm": fx, "fit": (c + b * fx).round(2)}), __file__, "qt_fit")
f = qt.dropna(subset=["stir"])
fb, fc = np.polyfit(f.pi, f.stir, 1)
st = {"n": len(qt), "excluded": len(d) - len(qt), "corr": round(qt.gm.corr(qt.pi), 3), "slope": round(b, 3),
      "intercept": round(c, 2), "fisher_n": len(f), "fisher_slope": round(fb, 3), "fisher_int": round(fc, 2),
      "fisher_corr": round(f.pi.corr(f.stir), 3)}
f2 = f[f.decade >= 1960]
gb, gc = np.polyfit(f2.pi, f2.stir, 1)
st.update({"fisher60_n": len(f2), "fisher60_slope": round(gb, 3), "fisher60_int": round(gc, 2),
           "fisher60_corr": round(f2.pi.corr(f2.stir), 3)})
# The slope with and without the high-inflation decades (two wartime decades above 30%).
for key, sub in {"low30": qt[qt.pi <= 30], "gm15": qt[qt.gm < 15], "since1950": qt[qt.decade >= 1950]}.items():
    sb, _ = np.polyfit(sub.gm, sub.pi, 1)
    st.update({f"{key}_n": len(sub), f"{key}_slope": round(sb, 3), f"{key}_corr": round(sub.gm.corr(sub.pi), 3)})
write_table(pd.DataFrame([st]), __file__, "qt_stats")
write_table(d[d.pi >= 60][["iso3", "decade", "gm", "pi"]], __file__, "qt_excluded")

m = wdi("FM.LBL.BMNY.GD.ZS", ["BOL", "PER"], 1980, 1996)
p = wdi("FP.CPI.TOTL.ZG", ["BOL", "PER"], 1980, 1996)
x = m.merge(p, on=["iso3", "country", "year"], suffixes=("_m", "_p")).dropna()
x = x.rename(columns={"value_m": "money", "value_p": "infl"})[["iso3", "year", "money", "infl"]].round(1)
for iso in ["BOL", "PER"]:
    write_table(x[x.iso3 == iso], __file__, f"hyper_{iso.lower()}")
