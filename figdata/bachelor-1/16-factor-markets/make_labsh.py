"""Charts of b1 ch. 16.

labsh_2019: PWT labour share of GDP (labsh) against output-side real GDP per person
(rgdpe/pop, PPP dollars), 2019. labsh_self: the same share against the self-employed
share of employment (WDI SL.EMP.SELF.ZS, per cent), 2019.
"""
import numpy as np
import pandas as pd
from econdata import pwt, wdi
from figout import write_table

p = pwt(since=2019, until=2019, cols=["labsh", "rgdpe", "pop"]).dropna()
p["gdp"] = (p.rgdpe / p["pop"]).round(0)
p["country"] = p.country.str.replace(",", "", regex=False)
d = p[["iso3", "country", "gdp", "labsh"]].round({"labsh": 3})
write_table(d, __file__, "labsh_2019")
q = d.labsh.quantile([0.1, 0.5, 0.9]).round(3).tolist()
corr_y = round(np.corrcoef(np.log10(d.gdp), d.labsh)[0, 1], 2)
s = wdi("SL.EMP.SELF.ZS", since=2019, until=2019, countries_only=True).dropna()
m = d.merge(s[["iso3", "value"]], on="iso3").rename(columns={"value": "self"})
m["self"] = m["self"].round(1)
write_table(m, __file__, "labsh_self")
stats = pd.DataFrame([{"n": len(d), "p10": q[0], "median": q[1], "p90": q[2], "corr_log_gdp": corr_y,
                       "n_self": len(m), "corr_self": round(m.labsh.corr(m["self"]), 2)}])
write_table(stats, __file__, "labsh_stats")
pts = m[m.iso3.isin(["USA", "FRA", "IND", "QAT", "RWA", "NGA"])]
write_table(pts, __file__, "labsh_points")
write_table(pts[~pts.iso3.isin(["FRA", "USA"])], __file__, "labsh_labels")
