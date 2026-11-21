"""Annuity features and death within five years, chapter 15 opening chart.

Reads src/fp2004.csv, columns 3 and 4 of Table 2 of Finkelstein and Poterba
(2004): the change in the probability of dying within five years of buying an
annuity associated with each feature, in the compulsory and the voluntary
market (ledger b2:fp2004-t2; capital-protected annuities exist only in the
voluntary market). Writes
  out/annuities.csv          pos, feature, compulsory, voluntary in percentage
                             points (nan where the feature does not exist)
  out/annuities_summary.csv  the voluntary-market effects of escalating and
                             index-linked annuities as multiples of the male
                             effect
"""

import pandas as pd
from cited import load_cited
from figout import write_table


def table():
    d = load_cited(__file__, "fp2004")
    out = pd.DataFrame(
        {
            "pos": range(len(d), 0, -1),
            "feature": d.feature,
            "compulsory": (pd.to_numeric(d.compulsory, errors="coerce") * 100).round(1),
            "voluntary": (d.voluntary.astype(float) * 100).round(1),
        }
    )
    out["compulsory"] = out.compulsory.astype(object).fillna("nan")
    return out


def summary():
    d = load_cited(__file__, "fp2004").set_index("feature")
    v = d.voluntary.astype(float)
    return pd.DataFrame(
        [
            {
                "escalating_vs_male": round(-v["Escalating"] / v["Male"], 1),
                "indexed_vs_male": round(-v["Index-linked"] / v["Male"], 1),
            }
        ]
    )


if __name__ == "__main__":
    write_table(table(), __file__, "annuities")
    write_table(summary(), __file__, "annuities_summary")
