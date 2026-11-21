"""Equilibrium play of the penalty-kick game, simulated: what minimax data look like."""

import numpy as np

score = np.array([[0.60, 0.95], [0.90, 0.70]])  # kicker L/R (rows), goalie L/R (cols)
den = score[0, 0] - score[0, 1] - score[1, 0] + score[1, 1]
p = (score[1, 1] - score[1, 0]) / den  # kicker's probability of kicking left
q = (score[1, 1] - score[0, 1]) / den  # goalie's probability of covering left
value = score[0, 0] * q + score[0, 1] * (1 - q)
print(f"kick left {p:.4f}, cover left {q:.4f}, scoring rate {value:.4f}")

rng = np.random.default_rng(1111)
pairs, rounds, rejected = 20, 150, 0
for _ in range(pairs):
    kick = rng.random(rounds) < p  # True = left
    cover = rng.random(rounds) < q
    goal = rng.random(rounds) < score[np.where(kick, 0, 1), np.where(cover, 0, 1)]
    n_l, n_r = kick.sum(), (~kick).sum()
    g_l, g_r = goal[kick].sum(), goal[~kick].sum()
    pooled = (g_l + g_r) / rounds
    chi2 = sum(
        (g - n * pooled) ** 2 / (n * pooled * (1 - pooled))
        for g, n in [(g_l, n_l), (g_r, n_r)]
    )
    rejected += chi2 > 3.841  # 5 per cent critical value, one degree of freedom
print(f"pairs whose scoring rates differ at the 5% level: {rejected} of {pairs}")
