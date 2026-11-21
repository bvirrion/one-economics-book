"""Exercise 8: peak inflation in the United States and the euro area, 2019--2025.

U.S. CPI-U (BLS CUUR0000SA0, twelve-month change computed from the index); euro area
HICP twelve-month rate (Eurostat prc_hicp_manr, all items, EA).
"""
from econdata import bls_cpi, eurostat

c = bls_cpi()
c = c[c.period.str.match(r"M(0[1-9]|1[0-2])")].copy()
c["month"] = c.period.str[1:].astype(int)
c = c.sort_values(["year", "month"]).reset_index(drop=True)
c["rate"] = 100 * (c.value / c.value.shift(12) - 1)
h = eurostat("prc_hicp_manr")
h = h[(h.unit == "RCH_A") & (h.coicop == "CP00") & (h.geo == "EA")].copy()
h["year"], h["month"] = h.time.str[:4].astype(int), h.time.str[5:7].astype(int)
h = h.rename(columns={"value": "rate"}).sort_values(["year", "month"])

for name, d in (("United States", c), ("Euro area", h)):
    d = d[d.year.between(2019, 2025)].reset_index(drop=True)
    i = d.rate.idxmax()
    peak = d.loc[i]
    after = d.loc[i:]
    below = after[after.rate < 3].iloc[0]
    print(f"{name}: peak {peak.rate:.1f} % in {int(peak.month):02d}/{int(peak.year)}; "
          f"first below 3 % in {int(below.month):02d}/{int(below.year)} "
          f"({below.rate:.2f} %)")
