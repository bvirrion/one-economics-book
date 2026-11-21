"""Brenland's household survey: mean disposable income and consumption by age band.

Brenland is invented (code/shared/country, survey of 2025, 2,000 households). Writes
  out/brenland_age.csv  band, mid, n, disposable, consumption (means, thousands of
                        dalens), ratio = consumption / disposable
for the age bands of the head 21-29, 30-39, ..., 70-79, and
  out/brenland_fit.csv  one row: slope and intercept (thousands of dalens) of the
                        least-squares line of consumption on disposable income
                        across households, and the slope across the six band means.
Book 4, chapter 3: second chart and exercise 8.
"""

import numpy as np
import pandas as pd
from country import load
from figout import write_table

EDGES = [21, 30, 40, 50, 60, 70, 80]


def bands():
    h = load("households")
    labels = [f"{a}-{b - 1}" for a, b in zip(EDGES[:-1], EDGES[1:])]
    h["band"] = pd.cut(h.age_head, EDGES, right=False, labels=labels)
    g = h.groupby("band", observed=True)
    out = pd.DataFrame(
        {
            "n": g.size(),
            "disposable": (g.disposable.mean() / 1000).round(3),
            "consumption": (g.consumption.mean() / 1000).round(3),
        }
    ).reset_index()
    out.insert(1, "mid", [(a + b - 1) / 2 for a, b in zip(EDGES[:-1], EDGES[1:])])
    out["ratio"] = (out.consumption / out.disposable).round(3)
    return out


def fit():
    h = load("households")
    b, a = np.polyfit(h.disposable / 1000, h.consumption / 1000, 1)
    t = bands()
    bb, _ = np.polyfit(t.disposable, t.consumption, 1)
    return pd.DataFrame(
        [{"slope": round(b, 3), "intercept": round(a, 3), "band_slope": round(bb, 3)}]
    )


if __name__ == "__main__":
    write_table(bands(), __file__, "brenland_age")
    write_table(fit(), __file__, "brenland_fit")
