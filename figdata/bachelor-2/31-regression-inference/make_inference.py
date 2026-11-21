"""Classical and robust standard errors in the RAND Health Insurance Experiment, ch. 31.

Data: statsmodels' `randhie` (20,190 person-years): outpatient visits to a doctor
(mdvis) on the plan variables (lncoins, idp, lpi, fmde) and health (physlm, disea,
hlthg, hlthf, hlthp), with a constant.
Writes
  out/se.csv       term, label, b, se, hc1, ratio (robust / classical, 2 d.p.), lo, hi,
                   rlo, rhi (classical and robust 95 % intervals)
  out/spread.csv   bin, fitted (mean fitted value), sd (s.d. of residuals), n:
                   20 bins of equal size by fitted value
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm
from econdata import sm_dataset
from figout import write_table

LABELS = {
    "const": "constant",
    "lncoins": "log coinsurance",
    "idp": "deductible plan",
    "lpi": "log incentive",
    "fmde": "log max. expense",
    "physlm": "phys. limitation",
    "disea": "chronic diseases",
    "hlthg": "health good",
    "hlthf": "health fair",
    "hlthp": "health poor",
}


def fit():
    d = sm_dataset("randhie")
    X = sm.add_constant(d.drop(columns="mdvis"))
    return sm.OLS(d.mdvis, X)


def se_table():
    m = fit()
    c, h = m.fit(), m.fit(cov_type="HC1")
    ci, rci = c.conf_int(), h.conf_int()
    t = pd.DataFrame(
        {
            "term": c.params.index,
            "label": [LABELS[k] for k in c.params.index],
            "b": c.params.values,
            "se": c.bse.values,
            "hc1": h.bse.values,
            "ratio": (h.bse / c.bse).values,
            "lo": ci[0].values,
            "hi": ci[1].values,
            "rlo": rci[0].values,
            "rhi": rci[1].values,
        }
    )
    t = t.round(4)
    t["ratio"] = (h.bse / c.bse).round(2).values  # as printed by robust_se.py
    return t


def spread(bins=20):
    c = fit().fit()
    d = pd.DataFrame({"fitted": c.fittedvalues, "resid": c.resid}).sort_values("fitted")
    d["bin"] = np.arange(len(d)) * bins // len(d)
    g = d.groupby("bin")
    out = pd.DataFrame({"fitted": g.fitted.mean(), "sd": g.resid.std(), "n": g.size()})
    return out.reset_index().round(3)


if __name__ == "__main__":
    write_table(se_table(), __file__, "se")
    write_table(spread(), __file__, "spread")
