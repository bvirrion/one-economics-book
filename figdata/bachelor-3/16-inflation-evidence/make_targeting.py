"""Chart 3: median consumer-price inflation (WDI FP.CPI.TOTL.ZG) of the 26 inflation
targeters of Roger (2010), by years from adoption (-5 to +8), against the median of
all other countries in the same calendar years. Writes out/it_event.csv."""
import pandas as pd
from cited import load_cited
from econdata import wdi, wdi_countries
from figout import write_table


def table():
    t = load_cited(__file__, "targeters").drop(columns="ledger")
    c = wdi_countries()
    real = set(c.loc[c.Region.notna(), "Country Code"])
    p = wdi("FP.CPI.TOTL.ZG", since=1980, until=2024).dropna()
    p = p[p.iso3.isin(real)]
    others = p[~p.iso3.isin(t.iso3)].groupby("year").value.median()
    rows = []
    for k in range(-5, 9):
        it, ot = [], []
        for _, r in t.iterrows():
            v = p[(p.iso3 == r.iso3) & (p.year == r.adoption + k)].value
            if len(v):
                it.append(v.iloc[0])
                ot.append(others.get(r.adoption + k))
        rows.append({"k": k, "targeters": pd.Series(it).median(),
                     "others": pd.Series(ot).median(), "n": len(it)})
    return pd.DataFrame(rows)


if __name__ == "__main__":
    write_table(table(), __file__, "it_event")
