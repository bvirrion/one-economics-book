"""Exercise 8: which countries aged fastest, 2000 to 2025?

Old-age dependency ratio (65+ per 100 aged 15-64), WDI SP.POP.DPND.OL, countries
only (aggregates removed) with at least one million people in 2025 (SP.POP.TOTL).
"""
from econdata import wdi, wdi_countries

c = wdi_countries()
names = c.loc[c.Region.notna()].set_index("Country Code")["Table Name"]
x = wdi("SP.POP.DPND.OL", since=2000, until=2025)
pop = wdi("SP.POP.TOTL", since=2025, until=2025).set_index("iso3").value
big = pop[pop >= 1e6].index
x = x[x.iso3.isin(names.index) & x.iso3.isin(big) & x.year.isin([2000, 2025])]
w = x.pivot(index="iso3", columns="year", values="value").dropna()
w["rise"] = w[2025] - w[2000]
top = w.sort_values("rise", ascending=False).head(5)
print(f"countries with both years: {len(w)}")
for iso, r in top.iterrows():
    print(f"{names[iso]:<24} {r[2000]:5.1f} -> {r[2025]:5.1f}  (+{r['rise']:.1f})")
