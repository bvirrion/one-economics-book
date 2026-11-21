"""Card and Krueger (1994), Table 3: mean full-time-equivalent employment per store in
New Jersey and eastern Pennsylvania, February and November 1992 (cited numbers, ledger
b3did:ck94.t3). Also the dashed counterfactual: New Jersey's February level moved by
Pennsylvania's change (our arithmetic on the printed means).
Writes out/ck.csv (x, pa, nj, cf; x = 0 February, 1 November) and out/ck_stats.csv.
Book 5, chapter 3, opening chart.
"""
import pandas as pd
from cited import load_cited
from figout import write_table


def tables():
    d = load_cited(__file__, "ck").set_index(["state", "month"]).fte
    pa = [d["Pennsylvania", "February"], d["Pennsylvania", "November"]]
    nj = [d["New Jersey", "February"], d["New Jersey", "November"]]
    cf = [nj[0], round(nj[0] + pa[1] - pa[0], 2)]
    chart = pd.DataFrame({"x": [0, 1], "pa": pa, "nj": nj, "cf": cf})
    did = round((nj[1] - nj[0]) - (pa[1] - pa[0]), 2)
    stats = pd.DataFrame({"stat": ["change_pa", "change_nj", "did", "cf_nov"],
                          "value": [round(pa[1] - pa[0], 2), round(nj[1] - nj[0], 2),
                                    did, cf[1]]})
    return chart, stats


if __name__ == "__main__":
    chart, stats = tables()
    write_table(chart, __file__, "ck")
    write_table(stats, __file__, "ck_stats")
