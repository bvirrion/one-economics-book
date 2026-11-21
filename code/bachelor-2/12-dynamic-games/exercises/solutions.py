"""Worked numbers for the exercises and the problem of Book 4, chapter 12."""

from math import sqrt


def rubinstein(beta_1, beta_2):
    """Share of the first proposer in the infinite-horizon alternating-offers game."""
    return (1 - beta_2) / (1 - beta_1 * beta_2)


def finite(beta_1, beta_2, rounds):
    """First proposer's share when the game ends after `rounds` rounds."""
    share = 1.0
    for t in range(rounds - 1, 0, -1):
        share = 1 - (beta_2 if t % 2 == 1 else beta_1) * share
    return share


def backward_three():
    """Exercise 1: a three-stage tree solved backwards (payoffs player 1, player 2).

    Player 1 chooses Out (2, 2) or In; then player 2 chooses Low (1, 3) or High;
    then player 1 chooses a (4, 1) or b (0, 5). Returns the outcome reached.
    """
    after_high = max([(4, 1), (0, 5)], key=lambda x: x[0])
    after_in = max([(1, 3), after_high], key=lambda x: x[1])
    return max([(2, 2), after_in], key=lambda x: x[0])


def entry_game():
    """Payoffs (entrant, incumbent): out (0, 9); accommodate (2, 4); fight (-1, 1)."""
    respond = "accommodate" if 4 > 1 else "fight"
    enter = 2 > 0
    return enter, respond


def ultimatum_coins(coins=10):
    """Subgame-perfect equilibria with whole coins: offers the responder accepts."""
    # responder accepts every positive offer; at 0 she is indifferent
    return [(coins, 0), (coins - 1, 1)]


ENTRY = {"a_minus_c": 12.0}


def follower(q1, fixed, a_minus_c=12.0):
    """Entrant's best response and profit to the incumbent's committed output q1."""
    q2 = max((a_minus_c - q1) / 2, 0.0)
    profit = q2 * q2 - fixed
    return (q2, profit) if profit > 0 else (0.0, 0.0)


def deterrence(fixed, a_minus_c=12.0):
    """Incumbent's choice: deter (output that leaves the entrant no profit) or
    accommodate as a Stackelberg leader. Entrant stays out when indifferent."""
    q_deter = max(a_minus_c - 2 * sqrt(fixed), a_minus_c / 2)
    deter_profit = (a_minus_c - q_deter) * q_deter
    q_acc = a_minus_c / 2
    acc_profit = (a_minus_c - q_acc - (a_minus_c - q_acc) / 2) * q_acc
    blockaded = q_deter == a_minus_c / 2
    return {
        "q_deter": q_deter,
        "deter": deter_profit,
        "accommodate": acc_profit,
        "blockaded": blockaded,
        "choice": "deter" if deter_profit >= acc_profit else "accommodate",
    }


def deterrence_threshold(a_minus_c=12.0):
    """Fixed cost above which deterring beats accommodating: 2s(12 - 2s) = 18."""
    acc = a_minus_c**2 / 8
    # 4 s^2 - 2 a s + acc = 0, smaller root
    s = (2 * a_minus_c - sqrt(4 * a_minus_c**2 - 16 * acc)) / 8
    return s * s


def chain_store(markets=20):
    """Finite chain store: backward induction gives accommodation everywhere."""
    return ["enter/accommodate"] * markets


def andersen():
    """Rejection rates by stakes (percent), Andersen et al. (2011) Table 2."""
    return {20: 36.32, 200: 42.74, 2000: 27.52, 20000: 4.17}


HARBOUR = {"pie": 1000.0, "beta_e": 0.98, "beta_u": 0.95}


def harbour(beta_e=0.98, beta_u=0.95, pie=1000.0, outside=None):
    """Brenmoor harbour: the employer proposes first; shares of the monthly premium."""
    employer = rubinstein(beta_e, beta_u)
    union = 1 - employer
    if outside is not None and outside > union * pie:
        union = outside / pie
        employer = 1 - union
    return {"employer": employer * pie, "union": union * pie}


def harbour_two_rounds(beta_e=0.98, beta_u=0.95, pie=1000.0):
    """Day 1 the employer proposes; day 2 the union proposes and takes all."""
    union = beta_u * pie
    return {"employer": pie - union, "union": union}


def harbour_union_first(beta_e=0.98, beta_u=0.95, pie=1000.0):
    union = rubinstein(beta_u, beta_e)
    return {"union": union * pie, "employer": (1 - union) * pie}
