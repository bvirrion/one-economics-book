"""A firm with labour supply w = A + B L and marginal revenue product R - C L (the
weekend problem: A = 6, B = 0.1, R = 20, C = 0.1, wages in dalens an hour, L
workers). Monopsony, competitive and floor outcomes."""

A, B, R, C = 6.0, 0.1, 20.0, 0.1


def monopsony():
    lab = (R - A) / (2 * B + C)
    return lab, A + B * lab


def competitive():
    lab = (R - A) / (B + C)
    return lab, A + B * lab


def employment(floor):
    """Employment under a wage floor: the smaller of supply and demand at the floor,
    or the monopsony level if the floor does not bind."""
    lm, wm = monopsony()
    if floor <= wm:
        return lm
    return min((floor - A) / B, (R - floor) / C)


def supply_elasticity(lab):
    w = A + B * lab
    return w / (B * lab)
