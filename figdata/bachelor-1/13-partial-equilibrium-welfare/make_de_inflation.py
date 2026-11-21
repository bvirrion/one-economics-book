"""Opening chart of b1 ch. 13: Germany, HICP annual rates of change (RCH_A), month by
month, January 2019 - December 2022, all items (CP00) and food and non-alcoholic
beverages (CP01); x is the decimal year of the month's middle. Also the four months
around the start and the end of the 2020 VAT cut.
"""
import pandas as pd
from econdata import eurostat
from figout import write_table

d = eurostat("prc_hicp_manr")
d = d[(d.geo == "DE") & (d.unit == "RCH_A") & d.coicop.isin(["CP00", "CP01"])]
d = d[d.time.between("2019-01", "2022-12")]
w = d.pivot(index="time", columns="coicop", values="value").reset_index()
w.columns = ["month", "all", "food"]
y, m = w.month.str[:4].astype(int), w.month.str[5:].astype(int)
w.insert(1, "x", (y + (m - 0.5) / 12).round(4))
write_table(w, __file__, "de_hicp")
pts = w[w.month.isin(["2020-06", "2020-07", "2020-12", "2021-01", "2021-06", "2021-07"])]
write_table(pts, __file__, "de_hicp_points")
