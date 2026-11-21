"""Worked numbers for the exercises and the problem of Book 4, chapter 11."""


def mixed_2x2(a, b):
    """Mixed equilibrium of a 2x2 game without pure equilibria.

    a, b: row and column payoffs as [[a11, a12], [a21, a22]]. Returns (p, q): the
    row player's probability of row 1, the column player's probability of column 1.
    """
    p = (b[1][1] - b[1][0]) / (b[0][0] - b[0][1] - b[1][0] + b[1][1])
    q = (a[1][1] - a[0][1]) / (a[0][0] - a[0][1] - a[1][0] + a[1][1])
    return p, q


PK = [[0.60, 0.95], [0.90, 0.70]]


def zero_sum_value(a):
    p, q = mixed_2x2(a, [[-x for x in r] for r in a])
    return p, q, a[0][0] * q + a[0][1] * (1 - q)


def better_goalie():
    """Goalie gets better at saving kicks to the left when covering left."""
    before = zero_sum_value(PK)
    after = zero_sum_value([[0.50, 0.95], [0.90, 0.70]])
    return before, after


def battle():
    """Battle of the sexes: (2, 1) / (0, 0) / (0, 0) / (1, 2)."""
    a = [[2, 0], [0, 1]]
    b = [[1, 0], [0, 2]]
    p, q = mixed_2x2(a, b)
    return p, q, 2 * q, p * 1


def serve_game():
    """Server L/R against receiver L/R: the server wins with these chances."""
    a = [[0.58, 0.79], [0.73, 0.49]]
    return zero_sum_value(a)


def inspection(due=1000, fine=1500, cost=200, commit_cost=100):
    """Brenland's tax inspectors: mixed equilibrium and commitment."""
    audit = due / (due + fine)  # makes the taxpayer indifferent
    evade = cost / due  # makes the inspector indifferent
    payoff_mixed = (1 - evade) * due  # the inspector's payoff from not auditing
    payoff_commit = due - cost * audit - commit_cost
    fine_threshold = cost * due / (cost - commit_cost) - due
    tax_payer = -due  # the taxpayer's expected payment either way
    return {
        "audit": audit,
        "evade": evade,
        "mixed": payoff_mixed,
        "commit": payoff_commit,
        "threshold": fine_threshold,
        "taxpayer": tax_payer,
        "revenue": (1 - evade) * due + evade * audit * (due + fine),
    }


def pure_check():
    """Inspection game: no pure equilibrium (cycle of best responses)."""
    return [
        "audit -> honest",
        "honest -> no audit",
        "no audit -> evade",
        "evade -> audit",
    ]


if __name__ == "__main__":
    print(zero_sum_value(PK), better_goalie(), battle(), serve_game())
    for f in (1500, 4000):
        print(inspection(fine=f))
    print(inspection(fine=500))


def pearson(n_l, n_r, g_l, g_r):
    """Pearson statistic for equal win rates after serves left and right."""
    pooled = (g_l + g_r) / (n_l + n_r)
    return sum(
        (g - n * pooled) ** 2 / (n * pooled * (1 - pooled))
        for g, n in [(g_l, n_l), (g_r, n_r)]
    )
