"""Opening chart: share of men in the survey sample of the NSW files (CPS controls, 15,992)
with earnings in 1978, against earnings in 1975 (thousands of dollars). Dots: shares in bins
(0 exactly, then 0-1, 1-2, 2-4, ..., 26-30, above 30), at the bin's mean 1975 earnings.
Lines: linear probability model, logit and probit of the 1978 indicator on 1975 earnings
alone, evaluated on a grid 0-26 (1975 earnings are top-coded near 25). Writes out/work_bins.csv (earn75, share, n) and
out/work_fits.csv (earn75, lpm, logit, probit). Book 5, chapter 5, opening chart.
"""
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from econdata import nsw
from figout import write_table

EDGES = [-1, 0, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 30, 1e9]


def data():
    d = nsw("cps_controls")
    return pd.DataFrame({"work": (d.re78 > 0).astype(int), "earn75": d.re75 / 1000})


def tables():
    d = data()
    d["bin"] = pd.cut(d.earn75, EDGES)
    bins = (d.groupby("bin", observed=True)
            .agg(earn75=("earn75", "mean"), share=("work", "mean"), n=("work", "size"))
            .reset_index(drop=True))
    grid = pd.DataFrame({"earn75": np.linspace(0, 26, 53)})
    fits = grid.copy()
    for name, model in (("lpm", smf.ols), ("logit", smf.logit), ("probit", smf.probit)):
        m = model("work ~ earn75", d)
        f = m.fit() if name == "lpm" else m.fit(disp=0)
        fits[name] = f.predict(grid)
    return bins, fits


if __name__ == "__main__":
    bins, fits = tables()
    write_table(bins, __file__, "work_bins")
    write_table(fits, __file__, "work_fits")
