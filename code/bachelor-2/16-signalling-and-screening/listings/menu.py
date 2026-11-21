"""The best two-plan menu for a seller who cannot tell light from heavy users.

A user of type theta values q units at theta * q - q**2 / 2; a unit costs 2.
Two thirds of users are light (theta = 6), one third heavy (theta = 10).
"""

light, heavy, cost, share_light = 6.0, 10.0, 2.0, 2 / 3


def value(theta, q):
    return theta * q - q * q / 2


best = None
for i in range(0, 601):  # light plan: 0 to 6 units in steps of 0.01
    for j in range(0, 1001):  # heavy plan: 0 to 10 units
        q_l, q_h = i / 100, j / 100
        fee_l = value(light, q_l)  # light users just willing to buy
        fee_h = value(heavy, q_h) - (value(heavy, q_l) - fee_l)  # heavy: no envy
        profit = share_light * (fee_l - cost * q_l) + (1 - share_light) * (
            fee_h - cost * q_h
        )
        if best is None or profit > best[0] + 1e-12:
            best = (profit, q_l, fee_l, q_h, fee_h)
profit, q_l, fee_l, q_h, fee_h = best
print(f"light plan: {q_l:.2f} units for {fee_l:.2f}")
print(f"heavy plan: {q_h:.2f} units for {fee_h:.2f}")
print(
    f"heavy user's rent {value(heavy, q_h) - fee_h:.2f}; profit per user {profit:.2f}"
)
print(f"with full information: units {light - cost:.0f} and {heavy - cost:.0f}")
