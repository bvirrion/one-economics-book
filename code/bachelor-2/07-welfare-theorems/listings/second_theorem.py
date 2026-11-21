"""The second welfare theorem at work: a transfer that delivers a chosen allocation."""

a, b = 1 / 2, 2 / 3  # shares of income spent on good 1 by A and by B
w_a, w_b = (8, 2), (2, 8)  # endowments; good 2 is the numeraire
t1, t2 = w_a[0] + w_b[0], w_a[1] + w_b[1]


def contract(x1):
    """A's good 2 on the contract curve, given A's good 1."""
    return b * (1 - a) * t2 * x1 / (a * (1 - b) * (t1 - x1) + b * (1 - a) * x1)


def equilibrium(w_a, w_b):
    p = (a * w_a[1] + b * w_b[1]) / ((1 - a) * w_a[0] + (1 - b) * w_b[0])
    m_a = p * w_a[0] + w_a[1]
    return p, (a * m_a / p, (1 - a) * m_a)


target = (4, contract(4))  # the planner wants A to consume 4 units of good 1
p = (a / (1 - a)) * target[1] / target[0]  # the price that supports it: A's MRS
transfer = (p * w_a[0] + w_a[1]) - (p * target[0] + target[1])
print(f"target for A       ({target[0]:.3f}, {target[1]:.3f})")
print(f"supporting price   {p:.4f}")
print(f"transfer A -> B    {transfer:.3f} units of good 2")
new_a = (w_a[0], w_a[1] - transfer)
new_b = (w_b[0], w_b[1] + transfer)
p_new, x_a = equilibrium(new_a, new_b)
print(f"equilibrium after  p = {p_new:.4f}, A gets ({x_a[0]:.3f}, {x_a[1]:.3f})")
print(f"no transfer        p = {equilibrium(w_a, w_b)[0]:.4f}")
