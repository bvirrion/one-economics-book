"""100 samples of 30 men, a 95% interval from each: how many miss the truth?"""

import numpy as np
from econdata import nsw
from scipy import stats


def intervals(reps=100, n=30, seed=2026):
    y = nsw("psid_controls").re78.to_numpy()
    rng = np.random.default_rng(seed)
    s = rng.choice(y, size=(reps, n))
    half = stats.t.ppf(0.975, n - 1) * s.std(axis=1, ddof=1) / np.sqrt(n)
    lo, hi = s.mean(axis=1) - half, s.mean(axis=1) + half
    return lo, hi, y.mean()


if __name__ == "__main__":
    lo, hi, mu = intervals()
    miss = (lo > mu) | (hi < mu)
    print(f"true mean {mu:,.0f}; intervals that miss it: {miss.sum()} of 100")
    print(
        "first misses:",
        [f"{a:,.0f}-{b:,.0f}" for a, b in zip(lo[miss][:3], hi[miss][:3])],
    )
