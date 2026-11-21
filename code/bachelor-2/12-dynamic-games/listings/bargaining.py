"""Alternating offers over a pie of 1, solved by backward induction for T rounds."""

beta_1, beta_2 = 0.95, 0.90  # discount factors: player 1 proposes in round 1


def first_share(rounds):
    """Player 1's share in the subgame-perfect equilibrium of the T-round game."""
    share = 1.0  # in the last round the proposer takes everything
    for t in range(rounds - 1, 0, -1):
        # in round t the proposer must give the responder, who proposes in
        # round t + 1, what waiting is worth to her: her beta times that share
        beta_waiting = beta_2 if t % 2 == 1 else beta_1
        share = 1 - beta_waiting * share
    return share


for rounds in (1, 2, 3, 4, 10, 50, 200):
    print(f"{rounds:>3} rounds: player 1 gets {first_share(rounds):.4f}")
limit = (1 - beta_2) / (1 - beta_1 * beta_2)
print(f"infinite horizon:  {limit:.4f}")
