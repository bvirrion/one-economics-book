"""Weekend problem and chart 2: Brenland's furniture makers (invented). Melitz model
with sigma = 3, Pareto shape k = 4 (minimum productivity 1), fixed cost f = 40, entry cost
f_e = 2.5 (thousand dalens a year); with trade tau = 1.2 and fixed export cost 90, then
45 after the agreement. Writes out/furn_params.csv, out/furn_results.csv (one row per
regime) and out/furn_firms.csv: revenue of 10,000 simulated entrants (seed 2003) that
produce, closed and open (empty cells when the firm does not produce)."""
import numpy as np
import pandas as pd
from figout import write_table
from melitz import cutoffs, revenue

SIGMA, K, F, F_E, TAU = 3.0, 4.0, 40.0, 2.5, 1.2
REGIMES = [("closed", None), ("open", 90.0), ("agreement", 45.0)]


def results():
    rows = []
    for name, fx in REGIMES:
        d, x = cutoffs(SIGMA, K, F, F_E, None if fx is None else TAU, fx)
        rows.append({"regime": name, "f_x": fx if fx else 0.0, "cutoff": d,
                     "export_cutoff": x if x else 0.0, "produce": d ** -K,
                     "export_share": (d / x) ** K if x else 0.0,
                     "avg_phi": K / (K - 1) * d})
    r = pd.DataFrame(rows)
    r["exit_vs_previous"] = 1 - (r.cutoff.shift(1) / r.cutoff) ** K
    r["phi_change"] = r.cutoff / r.cutoff.shift(1) - 1
    return r


def firms():
    phi = np.sort(np.random.default_rng(2003).pareto(K, 10_000) + 1.0)
    r = results().set_index("regime")
    dc = r.cutoff["closed"]
    do, xo = r.cutoff["open"], r.export_cutoff["open"]
    phi = phi[(phi >= dc) & (phi <= 6)]
    closed = [revenue(p, SIGMA, F, dc) for p in phi]
    opened = [revenue(p, SIGMA, F, do, TAU, xo) if p >= do else np.nan for p in phi]
    return pd.DataFrame({"phi": phi, "closed": closed, "open": opened})


if __name__ == "__main__":
    params = pd.DataFrame({"item": ["sigma", "k", "f", "f_e", "tau"],
                           "value": [SIGMA, K, F, F_E, TAU]})
    write_table(params, __file__, "furn_params")
    write_table(results(), __file__, "furn_results")
    write_table(firms(), __file__, "furn_firms")
