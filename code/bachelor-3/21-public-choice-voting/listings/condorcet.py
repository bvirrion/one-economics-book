"""How often does majority rule cycle over three alternatives A, B, C?
Each voter has a strict ranking; a cycle means every alternative loses to another."""
import numpy as np

rng = np.random.default_rng(21)
RANKINGS = np.array([[0, 1, 2], [0, 2, 1], [1, 0, 2],
                     [1, 2, 0], [2, 0, 1], [2, 1, 0]])  # best first


def has_cycle(ranks):
    # pos[v, a] is the place voter v gives alternative a
    pos = np.argsort(ranks, axis=1)
    wins = {(a, b): (pos[:, a] < pos[:, b]).sum() * 2 > len(ranks)
            for a in range(3) for b in range(3) if a != b}
    return not any(all(wins[a, b] for b in range(3) if b != a) for a in range(3))


def spatial(n, dims):
    """Voters and alternatives are points; voters rank by distance."""
    alts = rng.normal(size=(3, dims))
    voters = rng.normal(size=(n, dims))
    return np.argsort(((voters[:, None, :] - alts[None]) ** 2).sum(axis=2), axis=1)


for n in (3, 25, 301):
    trials = 20_000
    any_ranking = np.mean([has_cycle(RANKINGS[rng.integers(0, 6, n)])
                           for _ in range(trials)])
    one_dim = np.mean([has_cycle(spatial(n, 1)) for _ in range(2_000)])
    two_dim = np.mean([has_cycle(spatial(n, 2)) for _ in range(2_000)])
    print(f"{n:3d} voters: any ranking {any_ranking:.3f}, "
          f"one dimension {one_dim:.3f}, two dimensions {two_dim:.3f}")
