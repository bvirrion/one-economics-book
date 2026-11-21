"""The Brenmoor pension fund: 60 years of invented real returns (Book 4, ch. 4 problem).

Brenland is invented. Equity and bond real returns are drawn independently across
years (seed 4404) from a bivariate normal: equity mean 7 %, sd 18 %; bonds mean 3 %,
sd 6 %; correlation 0.2. Since the draws are independent, past returns predict nothing.
Writes
  out/brenland_returns.csv  year (1965-2024), equity, bond (per cent, 2 decimals)
  out/brenland_predict.csv  one row: n, mean_eq, sd_eq, rho1 (first-order
                            autocorrelation of equity returns), se (1/sqrt(n)), t,
                            mean_after_up and mean_after_down (mean equity return in
                            years after a rise and after a fall), n_up, n_down.
"""

import numpy as np
import pandas as pd
from figout import write_table

SEED, N = 4404, 60
MU = np.array([0.07, 0.03])
SD = np.array([0.18, 0.06])
CORR = 0.2


def returns():
    rng = np.random.default_rng(SEED)
    cov = np.outer(SD, SD) * np.array([[1, CORR], [CORR, 1]])
    x = rng.multivariate_normal(MU, cov, N)
    return pd.DataFrame(
        {
            "year": range(1965, 1965 + N),
            "equity": np.round(100 * x[:, 0], 2),
            "bond": np.round(100 * x[:, 1], 2),
        }
    )


def predict():
    e = returns().equity
    rho = e.autocorr(1)
    prev = e.shift(1)
    up, down = e[prev > 0], e[prev <= 0]
    return pd.DataFrame(
        [
            {
                "n": N,
                "mean_eq": round(e.mean(), 2),
                "sd_eq": round(e.std(), 2),
                "rho1": round(rho, 3),
                "se": round(1 / np.sqrt(N), 3),
                "t": round(rho * np.sqrt(N), 2),
                "mean_after_up": round(up.mean(), 2),
                "mean_after_down": round(down.mean(), 2),
                "n_up": len(up),
                "n_down": len(down),
            }
        ]
    )


if __name__ == "__main__":
    write_table(returns(), __file__, "brenland_returns")
    write_table(predict(), __file__, "brenland_predict")
