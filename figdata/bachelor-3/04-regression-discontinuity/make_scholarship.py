"""The Brenmoor scholarship (invented), for the chapter's weekend problem.

6,000 school-leavers of Brenmoor; exam score in whole marks, N(60, 13) clipped to 0-100;
a scholarship is offered from 70. 72 % of those offered take it up, and 6 % of the others
obtain an equivalent award elsewhere. Parents' log income 10 + 0.01 score + N(0, 0.4)
(a predetermined covariate). Log earnings at 30:
    9.8 + 0.012 score + 0.15 award + 0.3 (parents - 10) + N(0, 0.35).
One school (8 % of pupils, chosen at random) has a teacher who re-marks every script on
67-69 to 70; the re-marked pupils keep their true score in the earnings equation.
Local linear fits, triangular weights, cutoff 69.5 (scores are whole marks), with the
heteroskedasticity-robust standard error of the chapter's helper (inlined).
Writes out/scholarship.csv (quantity, window, est_all, se_all, est_wo, se_wo: all pupils,
and without the re-marking school; `all` and `without` print them as 'est (se)') and
out/scholarship_density.csv (sample, theta, se). Seed 70. Book 5, chapter 4, weekend problem.
"""
import numpy as np
import pandas as pd
from figout import write_table


def side(x, y, h):
    w = np.clip(1 - np.abs(x) / h, 0, None)
    k = w > 0
    x, y, w = x[k], y[k], w[k]
    X = np.column_stack([np.ones_like(x), x])
    A = np.linalg.inv((X.T * w) @ X)
    b = A @ ((X.T * w) @ y)
    e = y - X @ b
    n = len(x)
    V = A @ (X.T * (w**2 * e**2)) @ X @ A * n / (n - 2)
    return b[0], V[0, 0]


def rd(x, y, c, h):
    x, y = np.asarray(x, float) - c, np.asarray(y, float)
    r, left = x >= 0, x < 0
    a1, v1 = side(x[r], y[r], h)
    a0, v0 = side(x[left], y[left], h)
    return a1 - a0, np.sqrt(v1 + v0)


def density(x, c, h):
    n = len(x)
    edges = np.arange(-0.5, 101.5, 1.0)
    counts, _ = np.histogram(x, edges)
    mids = np.arange(0, 101) - c
    f = counts / n
    fr = side(mids[mids > 0], f[mids > 0], h)[0]
    fl = side(mids[mids < 0], f[mids < 0], h)[0]
    return np.log(fr / fl), np.sqrt(24 / 5 * (1 / fr + 1 / fl) / (n * h))


def data():
    rng = np.random.default_rng(70)
    n = 6000
    true = np.clip(np.round(rng.normal(60, 13, n)), 0, 100)
    teacher = rng.uniform(size=n) < 0.08
    score = np.where(teacher & (true >= 67) & (true <= 69), 70, true)
    offer = score >= 70
    award = np.where(offer, rng.uniform(size=n) < 0.72, rng.uniform(size=n) < 0.06)
    parents = 10 + 0.01 * true + rng.normal(0, 0.4, n)
    earn = (9.8 + 0.012 * true + 0.15 * award + 0.3 * (parents - 10)
            + rng.normal(0, 0.35, n))
    return pd.DataFrame({"score": score, "true": true, "teacher": teacher,
                         "award": award.astype(float), "parents": parents, "earn": earn})


def tables():
    d = data()
    rows = []
    samples = {"all": d, "without the school": d[~d.teacher]}
    for sname, s in samples.items():
        for h in (5, 10, 20):
            for q, col in (("earnings", "earn"), ("award", "award")):
                rows.append((q, sname, h, *rd(s.score, s[col], 69.5, h)))
        rows.append(("parents' income", sname, 10, *rd(s.score, s.parents, 69.5, 10)))
        rows.append(("earnings at 60", sname, 10, *rd(s.score, s.earn, 59.5, 10)))
    long = pd.DataFrame(rows, columns=["quantity", "sample", "window", "est", "se"])
    a = long[long["sample"] == "all"].drop(columns="sample").reset_index(drop=True)
    b = long[long["sample"] != "all"].reset_index(drop=True)
    est = a.rename(columns={"est": "est_all", "se": "se_all"}).assign(
        est_wo=b.est, se_wo=b.se)
    def cell(e, v):
        return f"{e:.4f} ({v:.4f})".replace("-", "$-$")

    est["all"] = [cell(e, v) for e, v in zip(est.est_all, est.se_all)]
    est["without"] = [cell(e, v) for e, v in zip(est.est_wo, est.se_wo)]
    dens = pd.DataFrame([(sname, *density(s.score.values, 69.5, 10))
                         for sname, s in samples.items()], columns=["sample", "theta", "se"])
    return est, dens


if __name__ == "__main__":
    est, dens = tables()
    write_table(est, __file__, "scholarship")
    write_table(dens, __file__, "scholarship_density")
