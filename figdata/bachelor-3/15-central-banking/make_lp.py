"""Chart: the estimated responses of U.S. real GDP and the consumer price level to a
one-point Treasury-bill shock, 1960--2007, with 90 % bands (statsmodels macrodata, the
listing's method in lp.py). Writes out/lp.csv (h; output and price responses, bands)
and out/lp_stats.csv."""
import pandas as pd
from econdata import sm_dataset
from figout import write_table
from lp import irf, prepare, shock


def tables():
    d, lags = prepare(sm_dataset("macrodata"))
    d["shock"] = shock(d, lags)
    y, p = irf(d, lags, "y"), irf(d, lags, "p")
    t = pd.DataFrame({"h": y.h, "y": y.b, "y_lo": y.lo, "y_hi": y.hi,
                      "p": p.b, "p_lo": p.lo, "p_hi": p.hi})
    s = pd.DataFrame({"item": ["quarters", "shock_sd", "y_min", "y_min_h", "p_16"],
                      "value": [len(d), d.shock.std(), y.b.min(), int(y.b.idxmin()),
                                p.b.iloc[16]]})
    return t, s


if __name__ == "__main__":
    t, s = tables()
    write_table(t, __file__, "lp")
    write_table(s, __file__, "lp_stats")
