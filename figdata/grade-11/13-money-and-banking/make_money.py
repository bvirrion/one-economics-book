"""Narrow and broad money in the United States, 2000-2020 (Jorda-Schularick-Taylor Macrohistory Database).

Grade 11, chapter 13 (money and banking). `narrowm` (narrow money as JST defines it; for the US it follows the
monetary base) and `money` (broad money), billions of dollars; index 2000 = 100 and the ratio money / narrowm.
Writes:
  out/usa_money.csv   year, narrowm, money, narrow_idx, broad_idx, ratio
  out/usa_ratio_long.csv  year, ratio (money / narrowm), every fifth year 1950-2020 (quoted in the opening text)
"""
import pandas as pd

from econdata import jst
from figout import write_table


def compute():
    j = jst(isos=["USA"])
    x = j[(j.year >= 2000) & (j.year <= 2020)][["year", "narrowm", "money"]].reset_index(drop=True)
    base = x.iloc[0]
    x["narrow_idx"] = (100 * x.narrowm / base.narrowm).round(0)
    x["broad_idx"] = (100 * x.money / base.money).round(0)
    x["ratio"] = (x.money / x.narrowm).round(1)
    x["narrowm"] = x.narrowm.round(0).astype(int)
    x["money"] = x.money.round(0).astype(int)
    return x


def ratio_long():
    j = jst(isos=["USA"])
    x = j[(j.year >= 1950) & (j.year <= 2020) & (j.year % 5 == 0)][["year", "narrowm", "money"]]
    return pd.DataFrame({"year": x.year, "ratio": (x.money / x.narrowm).round(1)}).reset_index(drop=True)


if __name__ == "__main__":
    write_table(compute(), __file__, "usa_money")
    write_table(ratio_long(), __file__, "usa_ratio_long")
