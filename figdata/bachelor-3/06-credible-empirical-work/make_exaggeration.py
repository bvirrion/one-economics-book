"""Exaggeration ratio against power (analytic, normal approximation, one-sided filter at
1.96): with the effect in units of its standard error, b = 1.96 + Phi^-1(power), the mean
published z is b + phi(1.96 - b) / (1 - Phi(1.96 - b)); the ratio is that over b.
Writes out/exaggeration.csv (power, ratio) for power 0.06 to 0.95."""
import numpy as np
import pandas as pd
from figout import write_table
from scipy.stats import norm


def ratio(pw):
    b = 1.96 + norm.ppf(pw)
    a = 1.96 - b
    return (b + norm.pdf(a) / norm.sf(a)) / b


def table():
    pw = np.round(np.arange(0.06, 0.9501, 0.01), 2)
    return pd.DataFrame({"power": pw, "ratio": ratio(pw)})


if __name__ == "__main__":
    write_table(table(), __file__, "exaggeration")
