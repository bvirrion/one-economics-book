"""Weekend problem of b1 ch. 7: Brenland's basket (invented), 2015-2025. With the 2015
basket and Cobb--Douglas households who keep their 2015 budget shares: the Laspeyres index
(fixed 2015 basket), the Paasche index (2025 basket), the geometric index (the true
cost-of-living index for these preferences) and the chained Laspeyres index with shares
updated every year, all 2015 = 100."""
import numpy as np
import pandas as pd
from figout import write_table

import country

b = country.load("basket")
b = b[b.year.between(2015, 2025)]
p = b.pivot(index="year", columns="good", values="price")
q = b.groupby("good").qty_2015.first()[p.columns]
spend = q * p.loc[2015]
s = spend / spend.sum()
write_table(pd.DataFrame({"good": p.columns, "qty": q.values, "p2015": p.loc[2015].values,
                          "p2025": p.loc[2025].values, "spend2015": spend.values,
                          "share": s.round(4).values,
                          "relative": (p.loc[2025] / p.loc[2015]).round(4).values}),
            __file__, "brenland_basket")
rows = []
chain = 100.0
for y in p.index:
    r = p.loc[y] / p.loc[2015]
    if y > 2015:
        chain *= float((s * p.loc[y] / p.loc[y - 1]).sum())
    rows.append({"year": y, "laspeyres": 100 * float((s * r).sum()),
                 "paasche": 100 / float((s / r).sum()),
                 "geometric": 100 * float(np.exp((s * np.log(r)).sum())),
                 "chained": chain})
d = pd.DataFrame(rows).round(2)
write_table(d, __file__, "brenland_indices")
last = d.iloc[-1]
g = {k: round(100 * ((last[k] / 100) ** 0.1 - 1), 2)
     for k in ["laspeyres", "paasche", "geometric", "chained"]}
write_table(pd.DataFrame([g]), __file__, "brenland_growth")
