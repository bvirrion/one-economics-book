"""Opening chart of b1 ch. 17: Bresnahan and Reiss (1991), Table 5 part A (cited
numbers): the town population (thousands) needed to support N = 1..5 firms, by
profession; here per firm, S_N / N, and the ratios of successive per-firm thresholds
computed from those printed thresholds. Also the same per-firm thresholds for Cournot
competitors with linear demand, S_N proportional to (N + 1)^2, scaled to S_1 = 1.
"""
import pandas as pd
from cited import load_cited
from figout import write_table

d = load_cited(__file__, "entry_thresholds").drop(columns="ledger")
long = []
for _, r in d.iterrows():
    for n in range(1, 6):
        long.append({"profession": r.profession, "n": n, "S": r[f"s{n}"], "per_firm": round(r[f"s{n}"] / n, 3)})
long = pd.DataFrame(long)
wide = long.pivot(index="n", columns="profession", values="per_firm").reset_index()
wide.columns = ["n"] + [c.lower().replace(" ", "_") for c in wide.columns[1:]]
wide["cournot"] = [round((n + 1) ** 2 / 4 / n, 3) for n in wide.n]
write_table(wide, __file__, "per_firm")
ratios = []
for _, r in d.iterrows():
    s = [r[f"s{n}"] / n for n in range(1, 6)]
    ratios.append({"profession": r.profession, "r21": round(s[1] / s[0], 2), "r32": round(s[2] / s[1], 2),
                   "r43": round(s[3] / s[2], 2), "r54": round(s[4] / s[3], 2)})
c = [(n + 1) ** 2 / n for n in range(1, 6)]
ratios.append({"profession": "Cournot", "r21": round(c[1] / c[0], 2), "r32": round(c[2] / c[1], 2),
               "r43": round(c[3] / c[2], 2), "r54": round(c[4] / c[3], 2)})
write_table(pd.DataFrame(ratios), __file__, "ratios")
