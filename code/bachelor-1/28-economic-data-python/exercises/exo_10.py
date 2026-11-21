"""Exercise 10: seasonal adjustment of quarterly data, tested on a known season."""

import numpy as np
import pandas as pd


def adjust_q(x):
    """x: quarterly Series indexed by (year, quarter). Returns (factors, adjusted)."""
    m4 = x.rolling(4).mean()
    trend = (m4.shift(-2) + m4.shift(-1)) / 2  # centred: 1/8, 1/4, 1/4, 1/4, 1/8
    ratio = (x / trend).dropna()
    factors = ratio.groupby(level="quarter").mean()
    factors = factors / factors.mean()
    q = x.index.get_level_values("quarter")
    return factors, x / factors.loc[q].to_numpy()


def known_series(years=8):
    season = {1: 0.98, 2: 1.01, 3: 1.03, 4: 0.98}
    idx = pd.MultiIndex.from_product(
        [range(2010, 2010 + years), range(1, 5)], names=["year", "quarter"]
    )
    t = np.arange(len(idx))
    x = 100 * 1.005**t * np.array([season[q] for q in idx.get_level_values("quarter")])
    return pd.Series(x, index=idx), season


if __name__ == "__main__":
    x, season = known_series()
    f, _ = adjust_q(x)
    print(f.round(4).to_dict())
    print({q: round(v / np.mean(list(season.values())), 4) for q, v in season.items()})
