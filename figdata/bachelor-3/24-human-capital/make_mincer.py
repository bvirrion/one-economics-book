"""Charts 2 and 3: the Mincer equation in the CPS comparison sample of the NSW
data (men, earnings in 1978, dollars, top-coded at 25,564.7). Log earnings of those
with positive earnings on years of schooling, experience (age - schooling - 6) and
its square. Writes out/mincer_means.csv (mean log earnings by schooling, 6-18 years,
raw and adjusted to mean experience with the fitted experience terms, so that they
are comparable with the line), out/mincer_fit.csv (fitted line at mean
experience), out/profiles.csv (mean log earnings by age group and schooling group)
and out/mincer_stats.csv (with an F test of one dummy per year of schooling against
the linear term, and the jump at 12 years in the adjusted means)."""
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from econdata import nsw
from figout import write_table


def sample():
    d = nsw("cps_controls")
    d = d[d.re78 > 0].copy()
    d["lw"] = np.log(d.re78)
    d["exp"] = (d.age - d.education - 6).clip(lower=0)
    return d


def tables():
    d = sample()
    m = smf.ols("lw ~ education + exp + I(exp**2)", d).fit(cov_type="HC1")
    s = smf.ols("lw ~ education", d).fit(cov_type="HC1")
    me = d.exp.mean()
    d["adj"] = (d.lw - m.params["exp"] * (d.exp - me)
                - m.params["I(exp ** 2)"] * (d.exp**2 - me**2))
    means = (d[d.education.between(6, 18)].groupby("education")
             .agg(lw=("lw", "mean"), adj=("adj", "mean"), n=("lw", "size")).reset_index())
    dum = smf.ols("lw ~ C(education) + exp + I(exp**2)", d).fit()
    lin = smf.ols("lw ~ education + exp + I(exp**2)", d).fit()
    f, p, _ = dum.compare_f_test(lin)
    a = means.set_index("education").adj
    steps = a.diff().drop(12).dropna()
    grid = np.arange(6, 19)
    fit = pd.DataFrame({"education": grid,
                        "lw": m.params["Intercept"] + m.params["education"] * grid
                        + m.params["exp"] * me + m.params["I(exp ** 2)"] * me**2})
    top = 100 * (d.re78 >= d.re78.max() - 0.01).mean()
    peak = -m.params["exp"] / (2 * m.params["I(exp ** 2)"])
    st = pd.DataFrame({"stat": ["n", "b_school", "se_school", "b_exp", "b_exp2",
                                "peak_exp", "b_simple", "top_share", "r2",
                                "f_linear", "p_linear", "jump12", "median_step"],
                       "value": [len(d), m.params["education"],
                                 m.bse["education"], m.params["exp"],
                                 m.params["I(exp ** 2)"], peak,
                                 s.params["education"], top, m.rsquared,
                                 f, p, a[12] - a[11], steps.median()]})
    return means, fit, st


if __name__ == "__main__":
    means, fit, st = tables()
    write_table(means, __file__, "mincer_means")
    write_table(fit, __file__, "mincer_fit")
    write_table(st, __file__, "mincer_stats")
