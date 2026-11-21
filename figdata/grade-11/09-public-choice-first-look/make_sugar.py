"""The US sugar programme in 1998: cost per person against benefit per sugar farm.

Grade 11, chapter 9 (public choice, a first look). Cited (src/gao.csv): GAO/RCED-00-126, the programme's cost to US
sweetener users (1.9 billion 1999 dollars) and its benefit to producers (1.0 billion), and the number of farms growing
cane (973) or beets (7097) in the 1997 census. Population: World Bank WDI SP.POP.TOTL, United States, 1998.
The benefit per farm is an upper bound for a grower: it includes the processors' share.
Writes:
  out/sugar.csv   item, x, dollars   (cost per person; benefit per farm)
  out/sugar_key.csv  pop_millions, farms, cost_pp, benefit_pf, ratio
"""
import pandas as pd

from cited import load_cited
from econdata import wdi
from figout import write_table


def compute():
    g = load_cited(__file__, "gao").set_index("item")["value"].astype(str).str.replace(",", "").astype(float)
    pop = float(wdi("SP.POP.TOTL", isos=["USA"]).set_index("year").value.loc[1998])
    farms = int(g["cane_farms"] + g["beet_farms"])
    cost_pp = g["cost_1998_bn"] * 1e9 / pop
    ben_pf = g["benefit_1998_bn"] * 1e9 / farms
    key = pd.DataFrame([{"pop_millions": round(pop / 1e6, 1), "farms": farms, "cost_pp": round(cost_pp, 2),
                         "benefit_pf": round(ben_pf, -2), "ratio": round(ben_pf / cost_pp, -2)}])
    bars = pd.DataFrame({"item": ["cost per person", "benefit per farm"], "x": [0, 1],
                         "dollars": [round(cost_pp, 2), round(ben_pf, -2)]})
    return bars, key


if __name__ == "__main__":
    b, k = compute()
    write_table(b, __file__, "sugar")
    write_table(k, __file__, "sugar_key")
