"""Exercise 8: research spending and patents across countries, 2019. Regress log10
of resident patent applications per million people on R&D spending as a share of
GDP, then add log10 GDP per person (PPP)."""
import numpy as np
from econdata import wdi

Y = 2019
cols = {"IP.PAT.RESD": "pat", "SP.POP.TOTL": "pop", "GB.XPD.RSDV.GD.ZS": "rnd",
        "NY.GDP.PCAP.PP.KD": "gdp"}
d = None
for code, name in cols.items():
    s = wdi(code, since=Y, until=Y, countries_only=True)[["iso3", "value"]]
    s = s.rename(columns={"value": name})
    d = s if d is None else d.merge(s, on="iso3")
d = d[(d.pat > 0) & (d.rnd > 0)].dropna()
y = np.log10(d.pat / d["pop"] * 1e6)
for label, X in [("R&D only", np.column_stack([np.ones(len(d)), d.rnd])),
                 ("R&D and income", np.column_stack([np.ones(len(d)), d.rnd,
                                                     np.log10(d.gdp)]))]:
    b = np.linalg.lstsq(X, y, rcond=None)[0]
    r2 = 1 - ((y - X @ b) ** 2).sum() / ((y - y.mean()) ** 2).sum()
    print(f"{label}: R&D coefficient {b[1]:.3f}, R2 {r2:.2f}, {len(d)} countries")
