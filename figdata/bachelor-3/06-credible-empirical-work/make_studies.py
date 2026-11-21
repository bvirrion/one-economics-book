"""Twenty studies of a training programme (invented, Brenland): the weekend problem.

The programme's true effect on earnings is 2.0 percent. Candidate evaluations have
log-uniform sizes from 100 to 3,000 trainees per arm; the standard error of the estimated
effect, in percent, is 60 sqrt(2/n). A candidate is published when its z exceeds 1.96,
otherwise with probability 0.15; the first twenty published form the literature. Then a
pre-registered trial with 20,000 trainees per arm reports its estimate. Seed 2027.
Writes out/studies.csv (study, n, est, se), out/studies_summary.csv (stat, est, se).
"""
import numpy as np
import pandas as pd
from figout import write_table
from scipy.stats import norm


def literature():
    rng = np.random.default_rng(2027)
    rows = []
    while len(rows) < 20:
        n = int(round(np.exp(rng.uniform(np.log(100), np.log(3000)))))
        se = 60 * np.sqrt(2 / n)
        est = rng.normal(2.0, se)
        if est / se > 1.96 or rng.uniform() < 0.15:
            rows.append((n, round(est, 1), round(se, 2)))
    d = pd.DataFrame(rows, columns=["n", "est", "se"])
    d.insert(0, "study", [f"S{i:02d}" for i in range(1, 21)])
    trial_se = round(60 * np.sqrt(2 / 20000), 2)
    trial = round(rng.normal(2.0, trial_se), 1)
    return d, trial, trial_se


def summary(d, trial, trial_se):
    est, se = d.est.to_numpy(), d.se.to_numpy()
    w = 1 / se**2
    fe = (w @ est) / w.sum()
    X = np.column_stack([np.ones(20), se])
    XtW = X.T * w
    b = np.linalg.solve(XtW @ X, XtW @ est)
    r = est - X @ b
    cov = (w @ r**2) / 18 * np.linalg.inv(XtW @ X)
    rows = [("simple mean", est.mean(), est.std(ddof=1) / np.sqrt(20)),
            ("inverse-variance mean", fe, 1 / np.sqrt(w.sum())),
            ("FAT (slope on s.e.)", b[1], np.sqrt(cov[1, 1])),
            ("PET (effect at s.e. 0)", b[0], np.sqrt(cov[0, 0])),
            ("share significant", np.mean(est / se > 1.96), np.nan),
            ("pre-registered trial", trial, trial_se)]
    out = pd.DataFrame(rows, columns=["stat", "est", "se"])
    return out


def tables():
    d, trial, trial_se = literature()
    return d, summary(d, trial, trial_se)


def power(beta, se):
    return norm.sf(1.96 - beta / se)


if __name__ == "__main__":
    d, s = tables()
    write_table(d, __file__, "studies")
    write_table(s, __file__, "studies_summary")
