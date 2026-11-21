"""Chart 4: exam scores with a pass mark of 70, after a marker moves half of the scripts
on 66-69 up to 70 (the chapter's listing density_test.py: seed 70, 20,000 scripts,
N(58, 12) rounded to whole marks). Writes out/scores.csv (score, clean, remarked):
the number of scripts on each mark from 30 to 95. Book 5, chapter 4, chart 4.
"""
import numpy as np
import pandas as pd
from figout import write_table


def table():
    rng = np.random.default_rng(70)
    clean = np.clip(np.round(rng.normal(58, 12, 20000)), 0, 100)
    moved = clean.copy()
    pick = (moved >= 66) & (moved <= 69) & (rng.uniform(size=moved.size) < 0.5)
    moved[pick] = 70
    s = np.arange(30, 96)
    return pd.DataFrame({"score": s,
                         "clean": [(clean == v).sum() for v in s],
                         "remarked": [(moved == v).sum() for v in s]})


if __name__ == "__main__":
    write_table(table(), __file__, "scores")
