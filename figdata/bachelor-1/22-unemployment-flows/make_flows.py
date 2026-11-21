"""Charts of b1 ch. 22.

jolts_flows: JOLTS hires and total separations, total nonfarm, seasonally adjusted,
monthly levels (millions), 2001-2025; jolts_stats: yearly averages for 2019 and 2009.
us_unemp: JST R6 unemployment rate, United States, 1890-2018. The release records 2.0 for
2019, far from the neighbouring years (3.9 in 2018, 8.05 in 2020): the chart stops in 2018.
beveridge: EU27 (2020), quarterly, seasonally adjusted, 2010-2025: job vacancy rate
(industry, construction and services, B-S) against the unemployment rate (15-74).
youth: une_rt_a 2023, unemployment rate of 15-24 against 15-74 by country.
"""
import pandas as pd
from econdata import eurostat, jolts, jst
from figout import write_table

f = {}
for e in ["HI", "TS", "QU", "LD", "JO"]:
    d = jolts(e, rate=False)
    d = d[(d.year >= 2001) & (d.year <= 2025)]
    f[e] = d.set_index(["year", "month"]).value / 1000
fl = pd.DataFrame(f).reset_index()
fl["t"] = (fl.year + (fl.month - 0.5) / 12).round(3)
write_table(fl[["t", "HI", "TS"]].round(3), __file__, "jolts_flows")
yr = fl.groupby("year")[["HI", "TS", "QU", "LD", "JO"]].mean().round(2).reset_index()
write_table(yr[yr.year.isin([2007, 2009, 2018, 2019, 2022, 2025])], __file__, "jolts_stats")
apr = fl[(fl.year == 2020) & (fl.month == 4)][["year", "month", "HI", "TS", "LD"]].round(2)
write_table(apr, __file__, "jolts_2020")

u = jst(["USA"], 1890, 2018, ["unemp"])[["year", "unemp"]].round(2)
write_table(u, __file__, "us_unemp")
write_table(u[u.year.isin([1933, 1944, 1982, 2009, 2017, 2018])], __file__, "us_unemp_points")

v = eurostat("jvs_q_nace2")
v = v[(v.geo == "EU27_2020") & (v.indic_em == "JVR") & (v.nace_r2 == "B-S") & (v.sizeclas == "TOTAL")
      & (v.s_adj == "SA")][["time", "value"]].rename(columns={"value": "vac"})
q = eurostat("une_rt_q")
q = q[(q.geo == "EU27_2020") & (q.s_adj == "SA") & (q.age == "Y15-74") & (q.sex == "T")
      & (q.unit == "PC_ACT")][["time", "value"]].rename(columns={"value": "u"})
b = v.merge(q, on="time").sort_values("time")
b = b[b.time >= "2010-Q1"].dropna()
write_table(b, __file__, "beveridge")
write_table(b[b.time.isin(["2010-Q1", "2013-Q1", "2019-Q4", "2020-Q2", "2022-Q2", "2025-Q4"])], __file__,
            "beveridge_points")
write_table(b[b.time.isin(["2013-Q1", "2019-Q4", "2022-Q2"])], __file__, "beveridge_labels")

a = eurostat("une_rt_a")
a = a[(a.time.astype(str) == "2023") & (a.sex == "T") & (a.unit == "PC_ACT") & a.age.isin(["Y15-24", "Y15-74"])]
w = a.pivot_table(index="geo", columns="age", values="value").dropna().reset_index()
w.columns = ["geo", "youth", "all"]
w = w[w.geo.str.len() == 2]
w["ratio"] = (w.youth / w["all"]).round(2)
write_table(w[w.geo.isin(["DE", "FR", "ES", "IT", "NL", "SE", "PL", "EL"])], __file__, "youth")
