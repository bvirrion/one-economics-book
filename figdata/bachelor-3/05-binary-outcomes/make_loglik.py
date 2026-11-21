"""Chart 2: the log-likelihood of the simplest logit, P(work) = 1/(1 + exp(-b)), for the
15,992 men of the opening chart, as a function of b; and the Newton steps from b = 0.
Writes out/loglik.csv (b, ll) and out/newton.csv (step, b, ll).
Book 5, chapter 5, chart 2.
"""
import numpy as np
import pandas as pd
from econdata import nsw
from figout import write_table


def counts():
    d = nsw("cps_controls")
    return int((d.re78 > 0).sum()), len(d)


def ll(b, n1, n):
    return n1 * b - n * np.logaddexp(0, b)


def tables():
    n1, n = counts()
    grid = np.linspace(-0.5, 3.5, 81)
    curve = pd.DataFrame({"b": grid, "ll": ll(grid, n1, n)})
    b, rows = 0.0, []
    for k in range(5):
        rows.append((k, b, ll(b, n1, n)))
        p = 1 / (1 + np.exp(-b))
        b = b + (n1 - n * p) / (n * p * (1 - p))
    return curve, pd.DataFrame(rows, columns=["step", "b", "ll"])


if __name__ == "__main__":
    curve, steps = tables()
    write_table(curve, __file__, "loglik")
    write_table(steps, __file__, "newton")
