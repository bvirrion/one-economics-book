"""Chart 2: the trilemma test, 1999--2020: change in the home short-term rate against
the change in the base country's rate, pegs and floats, with fitted lines; and the
slopes by era. Writes out/tri_peg.csv, out/tri_float.csv, out/tri_fit.csv and
out/tri_eras.csv."""
import numpy as np
import pandas as pd
from figout import write_table
from trilemma import ERAS, changes, slope


def tables():
    c = changes()
    recent = c[c.year.between(1999, 2020)]
    xs = np.array([-4.5, 2.5])
    fit = pd.DataFrame({"db": xs})
    for t in ("PEG", "FLOAT"):
        g = recent[recent.peg_type == t]
        b = slope(g)[0]
        a = g.d.mean() - b * g.db.mean()
        fit[t.lower()] = a + b * xs
    rows = []
    for era, (lo, hi) in ERAS.items():
        for t in ("PEG", "FLOAT"):
            b, se, r2, n = slope(c[(c.peg_type == t) & c.year.between(lo, hi)])
            rows.append({"era": era, "regime": t.lower(), "slope": b, "se": se,
                         "r2": r2, "obs": n})
    peg = recent[recent.peg_type == "PEG"][["iso3", "year", "db", "d"]]
    flo = recent[recent.peg_type == "FLOAT"][["iso3", "year", "db", "d"]]
    return peg, flo, fit, pd.DataFrame(rows)


if __name__ == "__main__":
    peg, flo, fit, eras = tables()
    write_table(peg, __file__, "tri_peg")
    write_table(flo, __file__, "tri_float")
    write_table(fit, __file__, "tri_fit")
    write_table(eras, __file__, "tri_eras")
