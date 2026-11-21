"""The equity premium and the risk aversion it needs: United States, 1950-2020."""

import numpy as np
from econdata import jst

d = jst(
    isos=["USA"],
    since=1949,
    until=2020,
    cols=["eq_tr", "bill_rate", "cpi", "rconsbarro"],
)
infl = d.cpi.pct_change()
equity = (1 + d.eq_tr) / (1 + infl) - 1  # real returns
bill = (1 + d.bill_rate) / (1 + infl) - 1
growth = d.rconsbarro.pct_change()  # real consumption per person
keep = d.year >= 1950
equity, bill, growth = equity[keep], bill[keep], growth[keep]

premium = (equity - bill).mean()
sharpe = premium / equity.std()
corr = np.corrcoef(growth, equity)[0, 1]
print(f"years                     {keep.sum()}")
print(f"equity premium            {premium:.4f}")
print(f"sd of equity return       {equity.std():.4f}")
print(f"sd of consumption growth  {growth.std():.4f}")
print(f"correlation               {corr:.3f}")
# premium = gamma * cov(growth, equity): solve for gamma
print(f"gamma needed              {premium / np.cov(growth, equity)[0, 1]:.1f}")
# with a perfect correlation, the smallest gamma that fits
print(f"gamma if corr = 1         {sharpe / growth.std():.1f}")
