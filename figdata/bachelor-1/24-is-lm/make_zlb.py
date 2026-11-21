"""Opening chart of b1 ch. 24.

fedzlb: the effective federal funds rate (H.15, monthly, per cent) and the Federal
Reserve's total assets (H.4.1, Wednesday level, the last Wednesday of each month, trillions
of dollars), 2003-2025. zlb_stats: months with the rate below 0.25 between December 2008
and November 2015, and total assets at chosen dates.
jst_rates: JST short-term rates of Japan, United States, United Kingdom, Germany, 1995-2020.
"""
import pandas as pd
from econdata import fed_series, jst
from figout import write_table

ff = fed_series("h15", "RIFSPFF_N.M")
ff["date"] = pd.to_datetime(ff.date)
ff = ff[(ff.date >= "2003-01-01") & (ff.date <= "2025-12-31")].copy()
ff["t"] = (ff.date.dt.year + (ff.date.dt.month - 0.5) / 12).round(3)
ta = fed_series("h41", "RESPPMA_N.WW")
ta["date"] = pd.to_datetime(ta.date)
ta["ym"] = ta.date.dt.to_period("M")
ta = ta.groupby("ym").last().reset_index()
ta = ta[(ta.ym >= pd.Period("2003-01", "M")) & (ta.ym <= pd.Period("2025-12", "M"))].copy()
ta["t"] = (ta.ym.dt.year + (ta.ym.dt.month - 0.5) / 12).round(3)
ta["assets"] = (ta.value / 1e6).round(3)
out = ff[["t", "value"]].rename(columns={"value": "ffr"}).merge(ta[["t", "assets"]], on="t", how="inner")
write_table(out, __file__, "fedzlb")
z = ff[(ff.date >= "2008-12-01") & (ff.date <= "2015-11-30")]
pts = ta[ta.ym.astype(str).isin(["2007-12", "2008-12", "2014-12", "2015-12", "2022-04", "2025-12"])]
st = {"zlb_months": len(z), "zlb_max": z.value.max(), "zlb_min": z.value.min()}
write_table(pd.DataFrame([st]), __file__, "zlb_stats")
write_table(pts[["t", "assets"]].assign(month=pts.ym.astype(str)), __file__, "assets_points")

j = jst(["JPN", "USA", "GBR", "DEU"], 1995, 2020, ["stir"])
w = j.pivot(index="year", columns="iso3", values="stir").round(3)
w.columns = [c.lower() for c in w.columns]
write_table(w.reset_index(), __file__, "jst_rates")
