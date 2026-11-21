"""How often is there no Condorcet winner? Random against single-peaked preferences."""

import numpy as np

rng = np.random.default_rng(909)
elections, voters = 4000, 501


def has_winner(ranks):
    """ranks[e, v, c] = place of candidate c on voter v's ballot (0 = top)."""
    m = ranks.shape[2]
    beats = np.ones((ranks.shape[0], m), dtype=bool)
    for i in range(m):
        for j in range(m):
            if i != j:
                wins = (ranks[:, :, i] < ranks[:, :, j]).sum(axis=1) > voters / 2
                beats[:, i] &= wins
    return beats.any(axis=1)


for m in (3, 4, 5):
    random = rng.random((elections, voters, m)).argsort(axis=2).argsort(axis=2)
    spots = np.sort(rng.random((elections, 1, m)), axis=2)  # candidates on a line
    ideal = rng.random((elections, voters, 1))  # each voter's favourite point
    peaked = np.abs(spots - ideal).argsort(axis=2).argsort(axis=2)
    no_r, no_p = 1 - has_winner(random).mean(), 1 - has_winner(peaked).mean()
    print(f"{m} candidates, no winner: random {no_r:.3f}, single-peaked {no_p:.3f}")
