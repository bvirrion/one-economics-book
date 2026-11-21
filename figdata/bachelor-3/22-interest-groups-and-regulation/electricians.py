"""Brenland licenses its electricians (weekend problem). Assumptions: inverse demand
for electricians' hours P = 100 - 0.05 Q, supply P = 20 + 0.03 Q (Q in thousands of
hours a year, P in dalens an hour); the licence caps hours at 800 thousand; the
trade association's stake is the producers' gain, the consumer group's the
consumers' loss, in a two-player Tullock contest. After the licence, four of
Brenland's eight regions repeal it; mean prices (dalens an hour) before and after:
repealing regions 60 and 53, the others 58 and 57."""
from tullock import two_player


def demand(q):
    return 100 - 0.05 * q


def supply(q):
    return 20 + 0.03 * q


def competitive():
    q = 80 / 0.08
    return q, demand(q)


def licensed(cap=800.0):
    return cap, demand(cap), supply(cap)


def stats(cap=800.0):
    qc, pc = competitive()
    q, p, w = licensed(cap)
    rent = (p - w) * q / 1000
    harberger = 0.5 * (p - w) * (qc - q) / 1000
    cs_loss = ((p - pc) * q + 0.5 * (p - pc) * (qc - q)) / 1000
    ps_gain = rent - ((pc - 20) * qc / 2 - (w - 20) * q / 2) / 1000
    b1, b2 = two_player(ps_gain, cs_loss)
    did = (53 - 60) - (57 - 58)
    return {"q_c": qc, "p_c": pc, "q_l": q, "p_l": p, "w_l": w,
            "premium": 100 * (p - pc) / pc, "rent_per_hour": p - w,
            "rent": rent, "harberger": harberger, "cs_loss": cs_loss,
            "ps_gain": ps_gain,
            "bid_assoc": b1, "bid_cons": b2, "rent_seeking": b1 + b2,
            "p_pass": ps_gain / (ps_gain + cs_loss), "total_cost": harberger + b1 + b2,
            "did": did}
