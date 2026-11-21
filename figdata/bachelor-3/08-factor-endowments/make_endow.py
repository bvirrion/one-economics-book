"""Opening chart: shares of world capital, workers and output, 2019, for the twelve
largest economies by output (PWT 11.0: rnna capital stock at constant 2021 national
prices, emp persons engaged, rgdpo output-side real GDP at 2021 PPPs). "World" is the
countries with all three series in 2019. Writes out/endow.csv (country, capital,
workers, output, rank; shares in percent; rank 1 = twelfth largest, first row) and
out/endow_meta.csv."""
import pandas as pd
from econdata import pwt
from figout import write_table

COLS = ["rnna", "emp", "rgdpo"]
SHORT = {"United States": "United States", "Russian Federation": "Russia",
         "Republic of Korea": "South Korea", "United Kingdom": "United Kingdom"}


def tables():
    d = pwt(since=2019, until=2019, cols=COLS).dropna(subset=COLS)
    tot = d[COLS].sum()
    s = d.assign(**{c: 100 * d[c] / tot[c] for c in COLS})
    top = s.sort_values("rgdpo", ascending=False).head(12).reset_index(drop=True)
    out = pd.DataFrame({"country": top.country.map(lambda c: SHORT.get(c, c)),
                        "capital": top.rnna, "workers": top.emp, "output": top.rgdpo,
                        "rank": range(12, 0, -1)}).iloc[::-1].reset_index(drop=True)
    meta = pd.DataFrame({"stat": ["countries", "year"], "value": [len(d), 2019]})
    return out, meta


if __name__ == "__main__":
    o, m = tables()
    o["country"] = o.country.str.replace(",", "", regex=False)
    write_table(o, __file__, "endow")
    write_table(m, __file__, "endow_meta")
