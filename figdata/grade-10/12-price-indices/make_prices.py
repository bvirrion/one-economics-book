"""US consumer prices of selected items, 2000-2025 (2000 = 100), and Brenland's basket prices (2015 = 100).

Grade 10, chapter 12 (price-indices). BLS CPI-U, U.S. city average, not seasonally adjusted, annual averages
(period M13): all items (SA0), computers, peripherals and smart home assistants (SEEE01), college tuition and
fees (SEEB01), apparel (SAA); each rebased to 2000 = 100. Brenland: code/shared/country basket.csv (invented).
Writes:
  out/us_items.csv     year, all, computers, tuition, apparel (2000 = 100)
  out/us_summary.csv   item, idx2025 (2000 = 100)
  out/bren_goods.csv   year, bread, rent, transport, clothing, energy (each 2015 = 100)
  out/bren_laspeyres.csv year, cost (dalens, the 2015 basket at that year's prices), cpi (2015 = 100)
"""
import pandas as pd

import country
from econdata import bls_cpi
from figout import write_table

ITEMS = {"all": "CUUR0000SA0", "computers": "CUUR0000SEEE01", "tuition": "CUUR0000SEEB01", "apparel": "CUUR0000SAA"}
BASE, LAST = 2000, 2025


def us():
    d = pd.DataFrame({"year": range(BASE, LAST + 1)})
    for k, sid in ITEMS.items():
        c = bls_cpi(sid)
        a = c[c.period == "M13"].set_index("year").value
        d[k] = (100 * a.loc[d.year].values / a.loc[BASE]).round(1)
    s = pd.DataFrame({"item": list(ITEMS), "idx2025": [d[k].iloc[-1] for k in ITEMS]})
    return d, s


def brenland():
    b = country.load("basket")
    w = b.pivot(index="year", columns="good", values="price")
    goods = ["bread", "rent", "transport", "clothing", "energy"]
    rel = (100 * w[goods] / w.loc[2015, goods]).round(1).reset_index()
    q = b.drop_duplicates("good").set_index("good").qty_2015
    cost = (w[goods] * q[goods]).sum(axis=1).round(2)
    las = pd.DataFrame({"year": cost.index, "cost": cost.values, "cpi": (100 * cost / cost.loc[2015]).round(2).values})
    return rel, las


if __name__ == "__main__":
    d, s = us()
    write_table(d, __file__, "us_items")
    write_table(s, __file__, "us_summary")
    rel, las = brenland()
    write_table(rel, __file__, "bren_goods")
    write_table(las, __file__, "bren_laspeyres")
