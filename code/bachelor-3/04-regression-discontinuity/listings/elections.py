"""Simulated close elections, calibrated on a published estimate (a jump of 0.077 in
the next vote share). Imported by the chapter's listings; not run on its own."""
import numpy as np


def draw(n=6000, seed=2024, jump=0.077):
    rng = np.random.default_rng(seed)
    margin = np.clip(rng.normal(0, 0.2, n), -0.5, 0.5)    # vote margin at t
    win = margin >= 0
    past = 0.47 + 0.40 * margin + 1.0 * margin**3 + rng.normal(0, 0.08, n)
    share = (0.46 + 0.45 * margin + 1.2 * margin**3 + jump * win
             + rng.normal(0, 0.08, n))                     # vote share at t + 1
    return margin, share, past
