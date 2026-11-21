"""g7-04 Money.

accounts.csv    label, iso3, y2011, y2024: share of adults (15 and over) with an account at a bank or other financial
                institution or with a mobile-money provider, 2011 and 2024 (WDI FX.OWN.TOTL.ZS, from the Global Findex
                survey); ten countries and the world, sorted by the 2011 value; pos is the bar position
barter.csv      goods, rates: number of barter exchange rates n(n-1)/2 against n money prices, n = 2..10
"""
import pandas as pd

from econdata import wdi
from figout import write_table

COUNTRIES = {"PAK": "Pakistan", "EGY": "Egypt", "IDN": "Indonesia", "NGA": "Nigeria", "VNM": "Viet Nam",
             "GHA": "Ghana", "KEN": "Kenya", "IND": "India", "BRA": "Brazil", "CHN": "China", "WLD": "World"}


def accounts():
    w = wdi("FX.OWN.TOTL.ZS", isos=list(COUNTRIES), since=2011, until=2024).dropna()
    p = w.pivot(index="iso3", columns="year", values="value")[[2011, 2024]].round(1)
    p.columns = ["y2011", "y2024"]
    p = p.sort_values("y2011").reset_index()
    p.insert(0, "label", p.iso3.map(COUNTRIES))
    p["pos"] = range(1, len(p) + 1)
    return p


def barter():
    n = pd.Series(range(2, 11), name="goods")
    return pd.DataFrame({"goods": n, "rates": n * (n - 1) // 2, "prices": n})


if __name__ == "__main__":
    write_table(accounts(), __file__, "accounts")
    write_table(barter(), __file__, "barter")
