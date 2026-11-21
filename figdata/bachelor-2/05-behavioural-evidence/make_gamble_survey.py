"""Brenmoor's survey of mixed gambles (invented), Book 4, chapter 5 weekend problem.

300 Brenmoor residents (seed 4505) are each offered a 50-50 gamble that loses 100
dalens or gains G, for G = 100, 125, ..., 400, and say yes or no. Each has a
loss-aversion coefficient drawn from a lognormal with median 2 and log-sd 0.35, and
accepts when G >= lambda * 100 (linear value, no probability weighting).
Writes
  out/gamble_survey.csv   G, accept (per cent of the 300 who accept)
  out/gamble_summary.csv  one row: n; median_switch (the smallest G at which at
                          least half accept); lambda_median (median_switch / 100);
                          share_reject_125 (per cent rejecting at G = 125).
"""

import numpy as np
import pandas as pd
from figout import write_table

SEED, N = 4505, 300
GRID = list(range(100, 425, 25))


def survey():
    rng = np.random.default_rng(SEED)
    lam = np.exp(np.log(2.0) + 0.35 * rng.normal(size=N))
    rows = [{"G": g, "accept": round(100 * np.mean(g >= 100 * lam), 1)} for g in GRID]
    return pd.DataFrame(rows)


def summary():
    s = survey()
    switch = int(s[s.accept >= 50].G.iloc[0])
    return pd.DataFrame(
        [
            {
                "n": N,
                "median_switch": switch,
                "lambda_median": switch / 100,
                "share_reject_125": round(100 - s.set_index("G").accept[125], 1),
            }
        ]
    )


if __name__ == "__main__":
    write_table(survey(), __file__, "gamble_survey")
    write_table(summary(), __file__, "gamble_summary")
