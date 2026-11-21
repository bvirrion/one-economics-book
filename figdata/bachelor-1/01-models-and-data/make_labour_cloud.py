"""Opening chart of b1 ch. 1: the US labour market as one price and one quantity.

Yearly log changes (per cent) in total hours worked (emp x avh) and in real labour
compensation per hour (labsh x rgdpna / hours), United States, 1981-2023, PWT 11.0.
"""
import numpy as np
import pandas as pd
from econdata import pwt
from figout import write_table

d = pwt(["USA"], 1980, 2023, ["emp", "avh", "labsh", "rgdpna"]).sort_values("year")
hours = d["emp"] * d["avh"]
wage = d["labsh"] * d["rgdpna"] / hours
t = pd.DataFrame({
    "year": d["year"].to_numpy()[1:],
    "dhours": 100 * np.diff(np.log(hours.to_numpy())),
    "dwage": 100 * np.diff(np.log(wage.to_numpy())),
})
write_table(t.round(3), __file__, "labour_cloud")

r = np.corrcoef(t["dwage"], t["dhours"])[0, 1]
slope = np.polyfit(t["dwage"], t["dhours"], 1)[0]
s = pd.DataFrame({"n": [len(t)], "corr": [round(r, 2)], "slope": [round(slope, 2)],
                  "sd_dhours": [round(t["dhours"].std(), 2)],
                  "sd_dwage": [round(t["dwage"].std(), 2)]})
write_table(s, __file__, "labour_cloud_stats")
