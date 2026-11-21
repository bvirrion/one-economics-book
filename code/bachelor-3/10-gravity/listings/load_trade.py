"""Load one year of bilateral trade (BACI flows in the CEPII Gravity database)."""
from econdata import gravity

COLS = ["year", "iso3_o", "iso3_d", "tradeflow_baci", "gdp_o", "gdp_d", "dist"]
d = gravity(since=2019, until=2019, columns=COLS)  # one year only: the file is large
d["flow"] = d.tradeflow_baci / 1e6  # thousands of dollars -> billions

countries = sorted(set(d.iso3_o) | set(d.iso3_d))
possible = len(countries) * (len(countries) - 1)  # ordered pairs, no self-trade
print(f"countries {len(countries)}, ordered pairs with positive trade {len(d):,}")
print(f"pairs with no recorded trade: {1 - len(d) / possible:.1%} of {possible:,}")
print(f"total trade {d.flow.sum():,.0f} billion dollars")
top = d.nlargest(5, "flow")[["iso3_o", "iso3_d", "flow", "dist"]]
print(top.to_string(index=False, float_format="{:,.0f}".format))
share = top.flow.sum() / d.flow.sum()
print(f"the 5 largest flows: {share:.1%} of world trade")
