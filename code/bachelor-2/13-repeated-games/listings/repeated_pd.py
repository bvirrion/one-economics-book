"""Discounted average payoffs of four strategies in the repeated prisoner's dilemma."""

PAYOFF = {("C", "C"): 3, ("C", "D"): 0, ("D", "C"): 5, ("D", "D"): 1}
STRATEGIES = {
    "always C": lambda mine, theirs: "C",
    "always D": lambda mine, theirs: "D",
    "grim": lambda mine, theirs: "D" if "D" in theirs else "C",
    "tit for tat": lambda mine, theirs: theirs[-1] if theirs else "C",
}


def average(first, second, beta, rounds=400):
    """Row player's (1 - beta) * sum of beta**t * payoff over the play of the pair."""
    mine, theirs, total = [], [], 0.0
    for t in range(rounds):  # beta**400 is negligible for beta <= 0.9
        a, b = first(mine, theirs), second(theirs, mine)
        total += (1 - beta) * beta**t * PAYOFF[(a, b)]
        mine.append(a)
        theirs.append(b)
    return total


for beta in (0.4, 0.9):
    print(f"beta = {beta}: row player's average payoff against each column")
    print(" " * 12 + "".join(f"{name:>12}" for name in STRATEGIES))
    for name, row in STRATEGIES.items():
        cells = [average(row, col, beta) for col in STRATEGIES.values()]
        print(f"{name:>12}" + "".join(f"{x:12.3f}" for x in cells))
