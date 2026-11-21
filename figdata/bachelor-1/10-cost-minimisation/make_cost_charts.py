"""Charts and tables of b1 ch. 10.

pv_costs: Kavlak, McNerney and Trancik (2018), Table 2 (cited numbers): PV module cost
per watt by component, 1980, 2001, 2012, 2015 dollars; plus the total fall and the
yearly rate of fall over each period.
census_extremes: Brenland's census of firms (invented): the smallest and largest firm of
each sector by output, with cost per dalen of output ((wage_bill + other_costs) / output).
"""
import country
import pandas as pd
from cited import load_cited
from figout import write_table

d = load_cited(__file__, "pv_costs").drop(columns="ledger")
for c in ["silicon", "nonsilicon", "scale"]:
    d[f"{c}_pct"] = (100 * d[c] / d.total).round(1)
write_table(d, __file__, "pv_costs")
rows = []
for a, b in [(0, 1), (1, 2), (0, 2)]:
    ra, rb = d.iloc[a], d.iloc[b]
    n = rb.year - ra.year
    rows.append({"from": int(ra.year), "to": int(rb.year), "ratio": round(rb.total / ra.total, 4),
                 "fall_pct": round(100 * (1 - rb.total / ra.total), 1),
                 "per_year_pct": round(100 * (1 - (rb.total / ra.total) ** (1 / n)), 1)})
write_table(pd.DataFrame(rows), __file__, "pv_falls")

f = country.load("firms")
f["cost"] = f.wage_bill + f.other_costs
f["ac"] = (f.cost / f.output).round(3)
out = []
for s, g in f.groupby("sector"):
    for tag, r in [("smallest", g.loc[g.output.idxmin()]), ("largest", g.loc[g.output.idxmax()])]:
        out.append({"sector": s, "which": tag, "firm": int(r.firm), "output": int(r.output),
                    "cost": int(r.cost), "ac": r.ac})
write_table(pd.DataFrame(out), __file__, "census_extremes")
