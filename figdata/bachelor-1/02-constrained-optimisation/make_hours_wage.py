"""Opening chart of b1 ch. 2: hours worked per person employed against labour
compensation per hour, 2019, PWT 11.0.

Compensation per hour = labsh x cgdpo / (emp x avh), in 2021 dollars at purchasing-power
parity (cgdpo is output-side real GDP at current PPPs, in millions; emp in millions).
Venezuela is left out (see below). Writes hours_wage.csv (iso3, wage, hours), hours_wage_stats.csv and hours_wage_tenths.csv
(median wage and median hours in each tenth of the wage distribution).
"""
import numpy as np
import pandas as pd
from econdata import pwt
from figout import write_table

d = pwt(None, 2019, 2019, ["emp", "avh", "labsh", "cgdpo"]).dropna(
    subset=["emp", "avh", "labsh", "cgdpo"])
d = d[(d.emp > 0) & (d.avh > 0)].copy()
# Venezuela's 2019 row gives 5 cents an hour, far below every other country:
# left out, and the caption says so
d = d[d.iso3 != "VEN"]
d["wage"] = d.labsh * d.cgdpo / (d.emp * d.avh)
d = d.sort_values("wage").reset_index(drop=True)
t = d[["iso3", "wage", "avh"]].rename(columns={"avh": "hours"})
t["wage"] = t.wage.round(2)
t["hours"] = t.hours.round(0)
write_table(t, __file__, "hours_wage")

r = np.corrcoef(np.log(t.wage), t.hours)[0, 1]
slope = np.polyfit(np.log(t.wage), t.hours, 1)[0]
usa = t[t.iso3 == "USA"].iloc[0]
write_table(pd.DataFrame({"n": [len(t)], "corr_logwage_hours": [round(r, 2)],
                          "slope_per_log": [round(slope, 0)],
                          "usa_wage": [usa.wage], "usa_hours": [usa.hours]}),
            __file__, "hours_wage_stats")

t["tenth"] = np.arange(len(t)) * 10 // len(t) + 1
g = t.groupby("tenth").agg(n=("wage", "size"), wage=("wage", "median"),
                           hours=("hours", "median")).reset_index()
g["wage"] = g.wage.round(2)
g["hours"] = g.hours.round(0)
write_table(g, __file__, "hours_wage_tenths")
