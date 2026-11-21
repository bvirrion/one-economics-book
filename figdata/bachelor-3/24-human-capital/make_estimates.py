"""Opening chart: OLS and IV estimates of the return to a year of schooling, ten
studies using features of the school system as instruments (Card 2000, Table 2;
first model of each study, cited numbers). Writes out/estimates.csv (with a row
position and the IV 95 % interval) and out/estimates_stats.csv."""
import pandas as pd
from cited import load_cited
from figout import write_table


def tables():
    d = load_cited(__file__, "estimates").drop(columns="ledger")
    d = d.iloc[::-1].reset_index(drop=True)
    d["pos"] = range(1, len(d) + 1)
    for c in ("ols", "iv", "iv_se"):
        d[c] = 100 * d[c]
    d["lo"], d["hi"] = d.iv - 1.96 * d.iv_se, d.iv + 1.96 * d.iv_se
    st = pd.DataFrame({"stat": ["studies", "iv_above", "ols_mean", "iv_mean",
                                "ols_median", "iv_median"],
                       "value": [len(d), int((d.iv > d.ols).sum()), d.ols.mean(),
                                 d.iv.mean(), d.ols.median(), d.iv.median()]})
    return d, st


if __name__ == "__main__":
    d, st = tables()
    write_table(d, __file__, "estimates")
    write_table(st, __file__, "estimates_stats")
