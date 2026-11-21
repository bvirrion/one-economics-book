"""Chart 2: Oaxaca-Blinder decomposition of the gap in log 1978 earnings between
white and black men in the CPS comparison sample of the NSW data (positive earnings;
white = neither black nor Hispanic). Characteristics: schooling, age, age squared,
married. Reports the decomposition with white and with black coefficients as the
reference. Writes out/oaxaca.csv and out/oaxaca_stats.csv."""
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from econdata import nsw
from figout import write_table

F = "lw ~ education + age + I(age**2) + married"


def groups():
    d = nsw("cps_controls")
    d = d[(d.re78 > 0) & (d.hispanic == 0)].copy()
    d["lw"] = np.log(d.re78)
    return d[d.black == 0], d[d.black == 1]


def decompose(a, b, ref):
    """Gap mean(a) - mean(b) = explained + unexplained, coefficients of `ref`."""
    ra, rb = smf.ols(F, a).fit(), smf.ols(F, b).fit()
    xa = ra.model.exog.mean(axis=0)
    xb = rb.model.exog.mean(axis=0)
    beta = ra.params.values if ref == "a" else rb.params.values
    explained = float((xa - xb) @ beta)
    gap = a.lw.mean() - b.lw.mean()
    return gap, explained, gap - explained


def tables():
    w, b = groups()
    rows = []
    for ref, name in (("a", "white"), ("b", "black")):
        gap, ex, un = decompose(w, b, ref)
        rows.append((name, gap, ex, un))
    t = pd.DataFrame(rows, columns=["reference", "gap", "explained", "unexplained"])
    t["pos"] = [0, 1]
    st = pd.DataFrame({"stat": ["n_white", "n_black", "gap", "school_white",
                                "school_black"],
                       "value": [len(w), len(b), t.gap[0], w.education.mean(),
                                 b.education.mean()]})
    return t, st


if __name__ == "__main__":
    t, st = tables()
    write_table(t, __file__, "oaxaca")
    write_table(st, __file__, "oaxaca_stats")
