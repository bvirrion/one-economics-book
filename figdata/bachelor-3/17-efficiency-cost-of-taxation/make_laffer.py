"""Chart 3: revenue from the top bracket against its rate, for a Pareto tail with
a = 1.5 and two elasticities of taxable income (0.25, 0.5). Every top income scales
with (1 - tau)^e, so the Pareto scale does too; the income above the threshold zbar
is then proportional to (1 - tau)^(a e), and revenue to tau (1 - tau)^(a e).
Revenue is normalised to its maximum for e = 0.25.
Writes out/laffer.csv and out/laffer_peaks.csv."""
import numpy as np
import pandas as pd
from figout import write_table

A = 1.5


def revenue(tau, e, a=A):
    """Top-bracket revenue, relative to the excess income at tau = 0."""
    return tau * (1 - tau) ** (a * e)


def peak(e, a=A):
    return 1 / (1 + a * e)


def tables():
    tau = np.linspace(0, 1, 101)
    norm = revenue(peak(0.25), 0.25)
    curve = pd.DataFrame({"tau": 100 * tau, "e25": revenue(tau, 0.25) / norm,
                          "e50": revenue(tau, 0.5) / norm})
    peaks = pd.DataFrame({"e": [0.25, 0.5], "tau_star": [100 * peak(0.25),
                                                         100 * peak(0.5)]})
    return curve, peaks


if __name__ == "__main__":
    c, p = tables()
    write_table(c, __file__, "laffer")
    write_table(p, __file__, "laffer_peaks")
