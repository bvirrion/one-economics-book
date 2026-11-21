"""Brenland: food spending against disposable income, one point per household (invented data).

Grade 10, chapter 7 (elasticities): the income elasticity of food spending is below one.
Reads code/shared/country households.csv. The slope of log(food) on log(disposable) is the elasticity;
the poorest and richest fifths give an arc elasticity by hand.
Writes:
  out/food.csv       hh, disposable, food (dalens a year)
  out/food_fit.csv   n, slope (log-log), share_low, share_high (food share of the poorest and richest fifth, %),
                     inc_low, inc_high, food_low, food_high (fifth means, dalens), arc (midpoint arc elasticity
                     from the two fifth means)
"""
import numpy as np
import pandas as pd

import country
from figout import write_table


def tables():
    h = country.load("households")
    d = h[["hh", "disposable", "food"]].copy()
    d = d[(d.disposable > 0) & (d.food > 0)].sort_values("hh").reset_index(drop=True)
    slope = np.polyfit(np.log(d.disposable), np.log(d.food), 1)[0]
    q = pd.qcut(d.disposable, 5, labels=False)
    lo, hi = d[q == 0], d[q == 4]
    il, ih = round(lo.disposable.mean(), -1), round(hi.disposable.mean(), -1)
    fl, fh = round(lo.food.mean(), -1), round(hi.food.mean(), -1)
    arc = ((fh - fl) / ((fh + fl) / 2)) / ((ih - il) / ((ih + il) / 2))
    fit = pd.DataFrame({"n": [len(d)], "slope": [round(slope, 2)],
                        "share_low": [round(100 * fl / il, 1)], "share_high": [round(100 * fh / ih, 1)],
                        "inc_low": [il], "inc_high": [ih], "food_low": [fl], "food_high": [fh],
                        "arc": [round(arc, 2)]})
    return d, fit


if __name__ == "__main__":
    d, fit = tables()
    write_table(d, __file__, "food")
    write_table(fit, __file__, "food_fit")
