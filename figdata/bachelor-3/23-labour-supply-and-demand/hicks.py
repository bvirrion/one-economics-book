"""Hicks-Marshall own-wage elasticity of labour demand, -(1 - s) sigma - s eta, and
the incidence and employment effect of a cut in a payroll tax wedge."""


def hicks_marshall(s, sigma, eta):
    return -(1 - s) * sigma - s * eta


def wedge_cut(cut, e_supply, e_demand):
    """A cut in the wedge between labour cost and take-home pay, as a share of the
    wage: returns the rise in take-home pay, the fall in labour cost and the rise in
    hours (all proportional)."""
    take_home = cut * e_demand / (e_supply + e_demand)
    cost = cut - take_home
    hours = e_supply * take_home
    return take_home, cost, hours
