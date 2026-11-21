"""Charts of b1 ch. 25.

accel: United States, 1960-2018: inflation is the ordinary percent change of the annual
average BLS CPI-U (all items, U.S. city average, period M13); the change in inflation from
the year before against the JST R6 unemployment rate (unemp); least-squares line and its
zero crossing. JST's 2019 US unemployment rate (2.0) is out of line and the series stops in
2018. (BLS, not JST, for US inflation: the two disagree, 13.5 against 11.2 in 1980.)
accel_post: the same fit for 1996-2018.
euro: euro area, 2009-2024 (Eurostat): HICP annual average rate of change (geo EA) and the
unemployment rate (geo EA21, 15-74, which starts in 2009), connected path.
cpi_peak: BLS CPI-U all items, 12-month change, 2021-2024: the peak month.
"""
import numpy as np
import pandas as pd
from econdata import bls_cpi, eurostat, jst
from figout import write_table

cpi = bls_cpi("CUUR0000SA0")
cpi = cpi[cpi.period == "M13"][["year", "value"]].sort_values("year")
cpi["pi"] = 100 * (cpi.value / cpi.value.shift() - 1)
j = jst(["USA"], 1958, 2018, ["unemp"]).merge(cpi[["year", "pi"]], on="year").sort_values("year")
j["dpi"] = j.pi.diff()
a = j[j.year >= 1960][["year", "unemp", "pi", "dpi"]].round(3)
write_table(a, __file__, "accel")
b, c = np.polyfit(a.unemp, a.dpi, 1)
xs = np.array([2.5, 10.5])
write_table(pd.DataFrame({"u": xs, "fit": (c + b * xs).round(3)}), __file__, "accel_fit")
p = a[a.year >= 1996]
b2, c2 = np.polyfit(p.unemp, p.dpi, 1)
st = {"n": len(a), "slope": round(b, 3), "intercept": round(c, 3), "un": round(-c / b, 2),
      "corr": round(a.unemp.corr(a.dpi), 3), "n_post": len(p), "slope_post": round(b2, 3),
      "corr_post": round(p.unemp.corr(p.dpi), 3)}
write_table(pd.DataFrame([st]), __file__, "accel_stats")
write_table(a[a.year.isin([1969, 1974, 1975, 1980, 1982, 1983, 1986])], __file__, "accel_points")
write_table(a[a.year.isin([1969, 1974, 1980, 1982])], __file__, "accel_labels")

h = eurostat("prc_hicp_aind")
h = h[(h.geo == "EA") & (h.unit == "RCH_A_AVG") & (h.coicop == "CP00")][["time", "value"]]
h = h.rename(columns={"value": "pi"})
u = eurostat("une_rt_a")
u = u[(u.geo == "EA21") & (u.unit == "PC_ACT") & (u.age == "Y15-74") & (u.sex == "T")][["time", "value"]]
u = u.rename(columns={"value": "u"})
h["time"] = h.time.astype(str)
u["time"] = u.time.astype(str)
e = h.merge(u, on="time").rename(columns={"time": "year"})
e["year"] = e.year.astype(int)
e = e[(e.year >= 1999) & (e.year <= 2024)].sort_values("year")
write_table(e[["year", "u", "pi"]], __file__, "euro")
write_table(e[e.year.isin([2009, 2013, 2019, 2022, 2024])][["year", "u", "pi"]], __file__, "euro_points")

c = bls_cpi("CUUR0000SA0")
c = c[c.period.str.match(r"M(0[1-9]|1[0-2])")].copy()
c["m"] = c.period.str[1:].astype(int)
c = c.sort_values(["year", "m"]).reset_index(drop=True)
c["yoy"] = (100 * (c.value / c.value.shift(12) - 1)).round(1)
w = c[(c.year >= 2021) & (c.year <= 2024)]
pk = w.loc[w.yoy.idxmax()]
last = c[(c.year == 2024) & (c.m == 12)].iloc[0]
write_table(pd.DataFrame([{"peak_year": int(pk.year), "peak_month": int(pk.m), "peak": pk.yoy,
                           "dec2024": last.yoy}]), __file__, "cpi_peak")
