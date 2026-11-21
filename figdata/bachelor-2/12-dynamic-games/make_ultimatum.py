"""Ultimatum offers and rejections in seventeen groups, chapter 12 opening chart.

Reads src/henrich2001.csv, Table 1 of Henrich et al. (2001): for each group, the
mean offer and the rejection rate, both as proportions of the stake (ledger
b2:henrich2001-t1; two groups have no usable rejection rate, written nan).
Writes
  out/ultimatum.csv          pos, group, offer and rejection in per cent, sorted
                             by the mean offer
  out/ultimatum_summary.csv  lowest and highest mean offer, the median of the
                             mean offers, and the number of groups with no
                             rejections
"""

import pandas as pd
from cited import load_cited
from figout import write_table


def table():
    d = load_cited(__file__, "henrich2001").drop(columns="ledger")
    d["offer"] = (100 * d.mean_offer.astype(float)).round(1)
    d["rejection"] = pd.to_numeric(d.rejection, errors="coerce") * 100
    d = d.sort_values("offer", kind="stable").reset_index(drop=True)
    out = d[["group", "offer", "rejection"]].copy()
    out["rejection"] = out.rejection.round(1).astype(object).fillna("nan")
    out.insert(0, "pos", range(1, len(out) + 1))
    return out


def summary():
    d = table()
    rej = pd.to_numeric(d.rejection, errors="coerce")
    return pd.DataFrame(
        [
            {
                "lowest": d.offer.min(),
                "highest": d.offer.max(),
                "median": d.offer.median(),
                "zero_rejection": int((rej == 0).sum()),
                "groups": len(d),
            }
        ]
    )


if __name__ == "__main__":
    write_table(table(), __file__, "ultimatum")
    write_table(summary(), __file__, "ultimatum_summary")
