"""Worked numbers for the exercises and the problem of Book 4, chapter 15."""


def lemons(price, top=10_000.0, buyer_factor=1.2):
    """Uniform quality on [0, top]; sellers sell when quality <= price."""
    share = min(price / top, 1.0)
    average = min(price, top) / 2
    return share, average, buyer_factor * average


def two_types(
    cost_low=1000.0, wtp_low=1500.0, cost_high=3000.0, wtp_high=3500.0, low=0.5
):
    pooled = low * cost_low + (1 - low) * cost_high
    low_buys = wtp_low >= pooled
    price = pooled if low_buys else cost_high
    return pooled, low_buys, price, wtp_high >= price


def pooling_threshold(cost_low=1000.0, wtp_low=1500.0, cost_high=3000.0):
    """Smallest share of low risks at which the pooled price is <= wtp_low."""
    return (cost_high - wtp_low) / (cost_high - cost_low)


def linear_market(d0, d1, m0, m1):
    """wtp(q) = d0 - d1 q, MC(q) = m0 - m1 q, AC(q) = m0 - m1 q / 2.

    Returns equilibrium share, premium, efficient share and the welfare loss
    per person, from too little cover or too much."""
    q = (d0 - m0) / (d1 - m1 / 2)
    q = min(max(q, 0.0), 1.0)
    premium = m0 - m1 * q / 2
    # efficient share: wtp = MC, capped to [0, 1]
    q_eff = 1.0 if d1 == m1 else min(max((d0 - m0) / (d1 - m1), 0.0), 1.0)
    if d0 - d1 * 1.0 >= m0 - m1 * 1.0:
        q_eff = 1.0

    def gap(x):  # integral of wtp - MC
        return (d0 - m0) * x - (d1 - m1) * x * x / 2

    loss = gap(q_eff) - gap(q)
    return q, premium, q_eff, loss


def spiral(d0, d1, m0, m1, steps):
    price, out = m0 - m1 / 2, []
    for _ in range(steps):
        share = min(max((d0 - price) / d1, 0.0), 1.0)
        out.append((price, share))
        price = m0 - m1 * share / 2
    return out


def coop():
    """Kestria's health cooperative, 1,000 members (kests a year)."""
    members = 1000
    healthy, sick = 600, 400
    avg = (healthy * 400 + sick * 1600) / members
    surplus = healthy * (600 - 400) + sick * (1900 - 1600)
    q, premium, q_eff, loss = linear_market(1800, 1000, 1500, 1200)
    steps = spiral(1800, 1000, 1500, 1200, 3)
    return {
        "avg": avg,
        "surplus": surplus,
        "healthy_lost": healthy * (600 - 400),
        "sick_surplus": sick * (1900 - 1600),
        "q": q,
        "premium": premium,
        "loss_total": loss * members,
        "steps": steps,
        "mandate_premium": 1500 - 1200 / 2,
        "loser_rank": (1800 - (1500 - 600)) / 1000,  # wtp below 900 above it
        "penalty": (1500 - 600) - (1800 - 1000),
    }
