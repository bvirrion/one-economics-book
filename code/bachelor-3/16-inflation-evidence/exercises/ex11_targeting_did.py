"""Exercise 11: inflation before and after the adoption of a target.

The 26 targeters and their adoption years (Roger 2010, cited table of the chapter's
chart data); WDI consumer-price inflation. Before: years -5 to -1; after: years 3 to
7. Other countries: the median of all non-targeters in the same calendar years.
"""
import pandas as pd
from econdata import wdi, wdi_countries

from pathlib import Path

SRC = Path(__file__).resolve().parents[4] / "figdata" / "bachelor-3" / \
    "16-inflation-evidence" / "src" / "targeters.csv"
t = pd.read_csv(SRC)
c = wdi_countries()
real = set(c.loc[c.Region.notna(), "Country Code"])
p = wdi("FP.CPI.TOTL.ZG", since=1980, until=2024).dropna()
p = p[p.iso3.isin(real)]
others = p[~p.iso3.isin(t.iso3)].groupby("year").value.median()

rows = []
for _, r in t.iterrows():
    own = p[p.iso3 == r.iso3].set_index("year").value
    before = [y for y in range(r.adoption - 5, r.adoption)]
    after = [y for y in range(r.adoption + 3, r.adoption + 8)]
    rows.append({"iso3": r.iso3,
                 "it_before": own.reindex(before).mean(),
                 "it_after": own.reindex(after).mean(),
                 "oth_before": others.reindex(before).mean(),
                 "oth_after": others.reindex(after).mean()})
d = pd.DataFrame(rows)
m = d.drop(columns="iso3").median()
print(f"targeters: {m.it_before:.1f} % before, {m.it_after:.1f} % after")
print(f"others, same years: {m.oth_before:.1f} % before, {m.oth_after:.1f} % after")
did = (m.it_after - m.it_before) - (m.oth_after - m.oth_before)
print(f"difference-in-differences (medians): {did:.1f} points")
