"""Weekend problem: Kestria's printing press, and the seigniorage curve (chart 5).
Writes out/laffer.csv (mu from 0 to 2.5: seigniorage and balances) and
out/kestria_stats.csv."""
import numpy as np
import pandas as pd
from cagan import A, DEFICIT, annual, balances, financing_rates, peak, seigniorage
from figout import write_table

GRADUAL_TO, RATIO_GRADUAL, RATIO_CREDIBLE = 3.0, 1.5, 0.5


def tables():
    mus = np.linspace(0, 2.5, 101)
    curve = pd.DataFrame({"mu": mus, "s": seigniorage(mus), "m": balances(mus)})
    mu_star, s_max = peak()
    lo, hi = financing_rates()
    infl_lo = annual(lo)
    gain = A - balances(lo)
    fall = infl_lo - GRADUAL_TO
    stats = pd.DataFrame({"stat": ["mu_peak", "s_max", "infl_peak", "mu_low", "mu_high",
                                   "infl_low", "infl_high", "m_low", "m_high",
                                   "remonetisation", "fall_points", "loss_gradual",
                                   "loss_credible", "deficit"],
                          "value": [mu_star, s_max, annual(mu_star), lo, hi, infl_lo,
                                    annual(hi), balances(lo), balances(hi), gain, fall,
                                    RATIO_GRADUAL * fall, RATIO_CREDIBLE * fall,
                                    DEFICIT]})
    return curve, stats


if __name__ == "__main__":
    c, s = tables()
    write_table(c, __file__, "laffer")
    write_table(s, __file__, "kestria_stats")
