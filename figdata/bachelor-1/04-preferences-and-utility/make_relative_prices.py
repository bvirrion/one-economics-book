"""Opening chart of b1 ch. 4: euro-area consumer prices of six categories and of all
items, 1996-2024, annual average indices 2015 = 100 (Eurostat prc_hicp_aind, geo EA).

Also writes the ratio 2024/1996 of each index, and of each index to all items.
"""
import pandas as pd
from econdata import eurostat
from figout import write_table

CATS = {"CP00": "all", "CP0111": "bread", "CP041": "rent", "CP0451": "electricity",
        "CP073": "transport", "CP0911": "audiovisual"}
d = eurostat("prc_hicp_aind")
d = d[(d.geo == "EA") & (d.unit == "INX_A_AVG") & d.coicop.isin(CATS)]
d = d[(d.time >= 1996) & (d.time <= 2024)]
w = d.pivot_table(index="time", columns="coicop", values="value").rename(columns=CATS)
w = w[list(CATS.values())].reset_index().rename(columns={"time": "year"})
write_table(w.round(2), __file__, "hicp_categories")

r = pd.DataFrame({
    "category": list(CATS.values()),
    "i1996": [w.loc[w.year == 1996, c].iloc[0] for c in CATS.values()],
    "i2024": [w.loc[w.year == 2024, c].iloc[0] for c in CATS.values()],
})
r["ratio"] = (r.i2024 / r.i1996).round(3)
r["relative"] = (r.ratio / r.ratio.iloc[0]).round(3)
write_table(r, __file__, "hicp_ratios")
