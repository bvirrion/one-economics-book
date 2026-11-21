"""Germany: 12-month change in consumer prices, all items and food, monthly 2019-2021, around the VAT cut
of 1 July - 31 December 2020.

Grade 10, chapter 10 (tax-incidence). Eurostat HICP, prc_hicp_manr (annual rate of change, %), Germany,
COICOP CP00 (all items) and CP011 (food).
Writes:
  out/vat_de.csv      t (decimal year, mid-month), month (YYYY-MM), all, food
  out/vat_steps.csv   step (cut: June -> July 2020; end: December 2020 -> January 2021), all_before, all_after,
                      food_before, food_after, d_all, d_food (percentage points)
"""
import pandas as pd

from econdata import eurostat
from figout import write_table

CODES = {"all": "CP00", "food": "CP011"}


def tables():
    m = eurostat("prc_hicp_manr")
    m = m[(m.unit == "RCH_A") & (m.geo == "DE") & (m.time >= "2019-01") & (m.time <= "2021-12")]
    w = m[m.coicop.isin(CODES.values())].pivot(index="time", columns="coicop", values="value")
    w = w.rename(columns={v: k for k, v in CODES.items()})[list(CODES)].sort_index()
    d = w.reset_index().rename(columns={"time": "month"})
    d.insert(0, "t", [round(int(s[:4]) + (int(s[5:7]) - 0.5) / 12, 3) for s in d.month])
    g = d.set_index("month")
    rows = []
    for step, a, b in [("cut", "2020-06", "2020-07"), ("end", "2020-12", "2021-01")]:
        rows.append({"step": step, "all_before": g.loc[a, "all"], "all_after": g.loc[b, "all"],
                     "food_before": g.loc[a, "food"], "food_after": g.loc[b, "food"],
                     "d_all": round(g.loc[b, "all"] - g.loc[a, "all"], 1),
                     "d_food": round(g.loc[b, "food"] - g.loc[a, "food"], 1)})
    return d, pd.DataFrame(rows)


if __name__ == "__main__":
    d, s = tables()
    write_table(d, __file__, "vat_de")
    write_table(s, __file__, "vat_steps")
