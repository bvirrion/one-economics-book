"""Win rates of first serves to the left and to the right, chapter 11 opening chart.

Reads src/ww2001.csv, Table 1 of Walker and Wooders (2001): for 40 point games (a
server on one court in one of ten finals), the first serves to the left and right
and the points won after each (ledger b2:ww2001-t1). Writes
  out/serves.csv          game, rate_l, rate_r (points won per serve, recomputed
                          from the counts), serves (total), smaller and larger rate
  out/serves_summary.csv  number of games, overall rates left and right, mean
                          absolute gap between the two rates, number of games with
                          p-values below 0.05 and 0.10, largest gap between a
                          recomputed and a printed rate
"""

import pandas as pd
from cited import load_cited
from figout import write_table


def raw():
    d = load_cited(__file__, "ww2001").drop(columns="ledger")
    for c in ["serves_l", "serves_r", "won_l", "won_r"]:
        d[c] = d[c].astype(int)
    for c in ["rate_l", "rate_r", "p_value"]:
        d[c] = d[c].astype(float)
    return d


def table():
    d = raw()
    out = pd.DataFrame(
        {
            "game": d.game,
            "rate_l": (d.won_l / d.serves_l).round(3),
            "rate_r": (d.won_r / d.serves_r).round(3),
            "serves": d.serves_l + d.serves_r,
        }
    )
    return out


def summary():
    d, t = raw(), table()
    printed_gap = max(
        (t.rate_l - d.rate_l).abs().max(), (t.rate_r - d.rate_r).abs().max()
    )
    return pd.DataFrame(
        [
            {
                "games": len(d),
                "overall_l": round(d.won_l.sum() / d.serves_l.sum(), 3),
                "overall_r": round(d.won_r.sum() / d.serves_r.sum(), 3),
                "mean_abs_gap": round((t.rate_l - t.rate_r).abs().mean(), 3),
                "p05": int((d.p_value < 0.05).sum()),
                "p10": int((d.p_value < 0.10).sum()),
                "max_printed_gap": round(printed_gap, 3),
            }
        ]
    )


if __name__ == "__main__":
    write_table(table(), __file__, "serves")
    write_table(summary(), __file__, "serves_summary")
