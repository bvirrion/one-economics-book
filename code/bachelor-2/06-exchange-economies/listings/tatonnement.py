"""Tatonnement in an exchange economy with three equilibria (p = 1/2, 1, 2)."""

r = 2 ** (8 / 9) - 2 ** (1 / 9)  # good 2 held by consumer A, good 1 by consumer B


def excess_demand(p):
    """Excess demand for good 1 at the relative price p = p1 / p2."""
    x1_a = 2 + (r - p ** (1 / 9)) / p  # A spends what is left on good 1
    x1_b = p ** (-1 / 9)  # B's demand for good 1
    return x1_a + x1_b - (2 + r)


def tatonnement(p, speed=50, rounds=2000):
    """Raise the price of good 1 when it is in excess demand, lower it if not."""
    for _ in range(rounds):
        p = p * (1 + speed * excess_demand(p))
    return p


for start in [0.3, 0.9, 0.99, 1.0, 1.01, 1.1, 3.0]:
    print(f"start {start:4.2f}  ->  price {tatonnement(start):.4f}")
