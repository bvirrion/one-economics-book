"""Labour compensation per worker against output per worker across countries, 2019 (Penn World Table).

Grade 10, chapter 3 (ricardo-model): wages follow productivity across countries.
Output per worker = rgdpo / emp (output-side real GDP at chained PPPs, 2017 dollars, per person
engaged); labour compensation per worker = labsh * output per worker (labsh, the share of labour
compensation in GDP, includes an estimate for the self-employed). Countries with all three series, except
Venezuela: its 2019 accounts (output per worker 1,140 dollars, labour share 0.09) are unreliable.
Writes:
  out/wages_productivity.csv  iso3, opw, comp (dollars per worker per year, rounded to 10)
  out/wages_selected.csv      iso3, name, opw, comp for six countries quoted in the chapter
  out/wages_marked.csv    the three of them labelled on the chart (USA, IND, KEN)
  out/wages_summary.csv       n, slope (of log10 comp on log10 opw), r (correlation of the logs)
"""
import numpy as np
import pandas as pd

from econdata import pwt
from figout import write_table

YEAR = 2019
MARKED = ["USA", "IND", "KEN"]   # labelled on the chart (the others crowd the cloud)
SELECTED = {"USA": "United States", "DEU": "Germany", "MEX": "Mexico", "CHN": "China",
            "IND": "India", "KEN": "Kenya"}


def tables():
    d = pwt(since=YEAR, until=YEAR).dropna(subset=["labsh", "rgdpo", "emp"])
    d = d[(d.emp > 0) & (d.iso3 != "VEN")]
    opw = d.rgdpo / d.emp
    out = pd.DataFrame({"iso3": d.iso3, "opw": (opw / 10).round() * 10,
                        "comp": (d.labsh * opw / 10).round() * 10}).sort_values("iso3").reset_index(drop=True)
    x, y = np.log10(out.opw), np.log10(out.comp)
    b = np.polyfit(x, y, 1)[0]
    summ = pd.DataFrame({"n": [len(out)], "slope": [round(b, 2)], "r": [round(np.corrcoef(x, y)[0, 1], 2)]})
    sel = out[out.iso3.isin(SELECTED)].copy()
    sel.insert(1, "name", sel.iso3.map(SELECTED))
    order = list(SELECTED)
    sel = sel.set_index("iso3").loc[order].reset_index()
    return out, sel, summ


if __name__ == "__main__":
    out, sel, summ = tables()
    write_table(out, __file__, "wages_productivity")
    write_table(sel, __file__, "wages_selected")
    write_table(sel[sel.iso3.isin(MARKED)][["iso3", "opw", "comp"]], __file__, "wages_marked")
    write_table(summ, __file__, "wages_summary")
