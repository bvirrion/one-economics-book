"""Seasonal adjustment by the ratio to a centred moving average."""

import pandas as pd
from cpi_tools import monthly


def adjust(x):
    """x: monthly Series indexed by (year, month). Returns (factors, adjusted)."""
    m12 = x.rolling(12).mean()
    trend = (m12.shift(-6) + m12.shift(-5)) / 2  # centred: 1/24, 1/12 x 11, 1/24
    ratio = (x / trend).dropna()
    factors = ratio.groupby(level="month").mean()
    factors = factors / factors.mean()  # average 1 over the year
    months = x.index.get_level_values("month")
    return factors, x / factors.loc[months].to_numpy()


if __name__ == "__main__":
    nsa = monthly("CUUR0000SA0")
    factors, adj = adjust(nsa)
    print("seasonal factors by month:")
    print(factors.round(4).to_string())
    sa = monthly("CUSR0000SA0")
    d = pd.DataFrame({"hand": adj.pct_change(), "official": sa.pct_change()})
    d = d.loc[2015:2024]
    print("months:", len(d))
    print("correlation of monthly changes:", round(d.hand.corr(d.official), 3))
