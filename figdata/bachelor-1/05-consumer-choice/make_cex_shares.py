"""Opening chart of b1 ch. 5: budget shares by fifth of income before taxes, United States,
Consumer Expenditure Surveys of 2012, 2015 and 2025 (BLS tables of mean, share and standard
error). Also the dollar means and the slope of log spending on log total spending between the
bottom and the top fifth (an arc elasticity of each item to total spending)."""
import math

import pandas as pd
from econdata import cex_table
from figout import write_table

TABLE = "mean-item-share-average-standard-error"
ITEMS = {"Food at home": "food_home", "Food away from home": "food_away",
         "Shelter": "shelter", "Entertainment": "entertainment"}


def block(t, label):
    """The Mean and Share rows under an item label (the first block with that label)."""
    c0 = t.iloc[:, 0].fillna("").str.strip()
    i = c0[c0 == label].index[0]
    rows = {}
    for k in range(i + 1, i + 5):
        rows[str(t.iloc[k, 0]).strip()] = pd.to_numeric(t.iloc[k, 2:7]).to_numpy()
    return rows


out, slopes = [], []
for year in (2012, 2015, 2025):
    t = cex_table(TABLE, year)
    inc = block(t, "Income before taxes")["Mean"]
    tot = block(t, "Average annual expenditures")["Mean"]
    for f in range(5):
        row = {"year": year, "fifth": f + 1, "income": inc[f], "spending": tot[f]}
        for lab, key in ITEMS.items():
            b = block(t, lab)
            row[key] = b["Share"][f]
            row[key + "_usd"] = b["Mean"][f]
        out.append(row)
    for lab, key in ITEMS.items():
        m = block(t, lab)["Mean"]
        s = math.log(m[4] / m[0]) / math.log(tot[4] / tot[0])
        slopes.append({"year": year, "item": key, "slope": round(s, 2)})
d = pd.DataFrame(out)
write_table(d, __file__, "cex_shares")
write_table(pd.DataFrame(slopes), __file__, "cex_slopes")
