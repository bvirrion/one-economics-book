"""The funnel plot of the chapter's simulated literature (the same draws as the listing
funnel.py, seed 400): 400 studies of a true effect of 0.1, per-arm sizes log-uniform from
25 to 2,000; significant positive results always published, others one time in ten.
Writes out/funnel.csv (est, precision, published 0/1)."""
import numpy as np
import pandas as pd
from figout import write_table


def table():
    rng = np.random.default_rng(400)
    n = np.exp(rng.uniform(np.log(25), np.log(2000), 400)).round()
    se = np.sqrt(2 / n)
    est = rng.normal(0.1, se)
    published = (est / se > 1.96) | (rng.uniform(size=400) < 0.1)
    return pd.DataFrame({"est": est, "precision": 1 / se, "published": published.astype(int)})


if __name__ == "__main__":
    write_table(table(), __file__, "funnel")
