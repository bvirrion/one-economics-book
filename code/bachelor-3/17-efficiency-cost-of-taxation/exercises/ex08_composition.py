"""Exercise 8: how the mix of central-government revenue changed, 1990 to 2024.

WDI shares of revenue: income, profits and capital gains; goods and services;
social contributions; international trade. Five economies. A value missing in
either year leaves the change missing.
"""
from econdata import wdi

CODES = {"income": "GC.TAX.YPKG.RV.ZS", "goods": "GC.TAX.GSRV.RV.ZS",
         "social": "GC.REV.SOCL.ZS", "trade": "GC.TAX.INTT.RV.ZS"}
SHOWN = ["USA", "GBR", "FRA", "DEU", "KOR"]

d = None
for k, c in CODES.items():
    x = wdi(c, since=1990, until=2024).rename(columns={"value": k})
    x = x[x.iso3.isin(SHOWN) & x.year.isin([1990, 2024])][["iso3", "year", k]]
    d = x if d is None else d.merge(x, on=["iso3", "year"], how="outer")
d = d.set_index(["iso3", "year"])  # a missing value stays missing (NaN)
change = d.xs(2024, level="year") - d.xs(1990, level="year")
print("change in share of revenue, 1990 to 2024 (points)")
print(change.loc[SHOWN].round(1).to_string())
best = change.stack().dropna().idxmax()
print(f"largest gain: {best[1]} in {best[0]}, {change.loc[best]:+.1f} points")
