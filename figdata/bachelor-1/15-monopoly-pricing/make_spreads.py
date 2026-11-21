"""Opening chart of b1 ch. 15: banks' lending rate minus deposit rate (WDI FR.INR.LNDP,
percentage points) against GDP per person at purchasing-power parity (WDI
NY.GDP.PCAP.PP.KD, constant 2021 international dollars), countries only, 2019.
"""
import numpy as np
import pandas as pd
from econdata import wdi
from figout import write_table

s = wdi("FR.INR.LNDP", since=2019, until=2019, countries_only=True)
g = wdi("NY.GDP.PCAP.PP.KD", since=2019, until=2019, countries_only=True)
d = s.merge(g[["iso3", "value"]], on="iso3", suffixes=("_spread", "_gdp")).dropna()
d = d.rename(columns={"value_spread": "spread", "value_gdp": "gdp"})
d["country"] = d.country.str.replace(",", "", regex=False)
d = d[["iso3", "country", "gdp", "spread"]].round({"gdp": 0, "spread": 2})
write_table(d, __file__, "spreads_2019")
fit = np.polyfit(np.log10(d.gdp), d.spread, 1)
q = d.spread.quantile([0.1, 0.5, 0.9]).round(2).tolist()
lo, hi = d.gdp.median(), d.gdp.median()
rich = d[d.gdp > hi].spread.median()
poor = d[d.gdp <= lo].spread.median()
stats = pd.DataFrame([{"n": len(d), "p10": q[0], "median": q[1], "p90": q[2],
                       "median_poor_half": round(poor, 2), "median_rich_half": round(rich, 2),
                       "slope_per_decade": round(fit[0], 2), "corr_log": round(np.corrcoef(np.log10(d.gdp), d.spread)[0, 1], 2)}])
write_table(stats, __file__, "spreads_stats")
xs = np.array([700, 130000])
write_table(pd.DataFrame({"gdp": xs, "fit": (fit[1] + fit[0] * np.log10(xs)).round(2)}), __file__, "spreads_fit")
pts = d[d.iso3.isin(["BRA", "CHE", "KEN", "MDG", "PER"])]
write_table(pts, __file__, "spreads_points")
