"""Exercise 8: inflation in Greece and Germany inside the euro, 1999--2008.

HICP annual average rates of change (Eurostat prc_hicp_aind, all items).
"""
from econdata import eurostat

e = eurostat("prc_hicp_aind")
e = e[(e.unit == "RCH_A_AVG") & (e.coicop == "CP00") & e.geo.isin(["EL", "DE"])]
w = e.pivot(index="time", columns="geo", values="value").loc[1999:2008]
for year, row in w.iterrows():
    print(f"{year}: Greece {row.EL:4.1f} %, Germany {row.DE:4.1f} %, "
          f"gap {row.EL - row.DE:4.1f} points")
gap = (w.EL - w.DE).mean()
rel = ((1 + w.EL / 100).prod() / (1 + w.DE / 100).prod() - 1) * 100
print(f"mean gap {gap:.2f} points; Greek prices rose {rel:.1f} % relative to German")
