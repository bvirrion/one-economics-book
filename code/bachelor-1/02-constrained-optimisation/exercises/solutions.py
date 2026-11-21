"""Worked numbers of the exercises and weekend problem of b1 ch. 2 (constrained
optimisation), checked against a numerical optimiser where one applies."""

import math

from scipy.optimize import minimize


def numeric_max(f, cons, x0, bounds=None):
    """Maximise f under constraints (scipy SLSQP); returns the maximiser."""
    r = minimize(
        lambda v: -f(v),
        x0,
        constraints=cons,
        bounds=bounds,
        method="SLSQP",
        options={"ftol": 1e-12, "maxiter": 500},
    )
    return r.x


def worked_example():
    """Text: max sqrt(xy) s.t. x + 2y = 12, and the multiplier."""
    x, y = 6.0, 3.0
    lam = 0.5 * math.sqrt(y / x)  # f_x / p_x with p_x = 1
    return {
        "x": x,
        "y": y,
        "f": math.sqrt(x * y),
        "lam": lam,
        "f_14": 14 / (2 * math.sqrt(2)),
        "approx_14": math.sqrt(18) + 2 * lam,
    }


def ex_substitution():
    """Exercise 2: max xy s.t. 2x + 3y = 24."""
    x = 24 / 4
    y = (24 - 2 * x) / 3
    return {"x": x, "y": y, "f": x * y}


def ex_level_slope(x=1.0, y=2.0):
    """Exercise 3: slope of the level curve of x^2 y at (x, y): -f_x/f_y."""
    return -(2 * x * y) / (x**2)


def ex_lagrange_log(p1=1.0, p2=2.0, m=30.0):
    """Exercises 5-6: max ln x + 2 ln y s.t. p1 x + p2 y = m."""
    x, y = m / (3 * p1), 2 * m / (3 * p2)

    def v(mm):
        return math.log(mm / (3 * p1)) + 2 * math.log(2 * mm / (3 * p2))

    return {
        "x": x,
        "y": y,
        "lam": 3 / m,
        "v": v(m),
        "dv_exact": v(m + 10) - v(m),
        "dv_approx": 10 * 3 / m,
    }


def ex_corner(m=0.5):
    """Exercise 7: max x + ln y s.t. x + y = m, x >= 0, y >= 0."""
    if m >= 1:
        return {"x": m - 1, "y": 1.0, "lam": 1.0}
    return {"x": 0.0, "y": m, "lam": 1 / m, "x_interior": m - 1}


def student_income(h, wage=15.0, grant=200.0, free=100.0, rate=0.5):
    """Hook and exercises 8-9: weekly income from h hours of paid work; the grant
    is withdrawn at `rate` per dalen earned above `free`, down to zero."""
    earn = wage * h
    return earn + max(0.0, grant - rate * max(0.0, earn - free))


def student_kinks(wage=15.0, grant=200.0, free=100.0, rate=0.5):
    h1 = free / wage
    h2 = (free + grant / rate) / wage
    return {
        "h1": h1,
        "h2": h2,
        "slopes": (wage, wage * (1 - rate), wage),
        "y1": student_income(h1),
        "y2": student_income(h2),
    }


U0 = math.sqrt(18)


def ex_dual(u0=U0):
    """Exercise 11: min x + 2y s.t. sqrt(xy) = u0; cost and multiplier."""
    x, y = math.sqrt(2) * u0, u0 / math.sqrt(2)
    return {
        "x": x,
        "y": y,
        "cost": x + 2 * y,
        "mu": 2 * math.sqrt(2),
        "lam_primal": 1 / (2 * math.sqrt(2)),
    }


def farm(land=20.0, a=2400.0, b=1200.0, water=None, wp=500.0, wb=100.0):
    """Weekend problem: max a sqrt(x) + b sqrt(y) s.t. x + y = land
    (and wp x + wb y <= water if given). Returns the plan and the multipliers."""
    # land only: a/(2 sqrt x) = b/(2 sqrt y) = lam  =>  x/y = (a/b)^2
    k = (a / b) ** 2
    y = land / (1 + k)
    x = land - y
    lam = a / (2 * math.sqrt(x))
    out = {
        "x": x,
        "y": y,
        "profit": a * math.sqrt(x) + b * math.sqrt(y),
        "lam": lam,
        "water_used": wp * x + wb * y,
        "mu": 0.0,
    }
    if water is not None and out["water_used"] > water:
        x = (water - wb * land) / (wp - wb)
        y = land - x
        fx, fy = a / (2 * math.sqrt(x)), b / (2 * math.sqrt(y))
        mu = (fx - fy) / (wp - wb)
        out = {
            "x": x,
            "y": y,
            "profit": a * math.sqrt(x) + b * math.sqrt(y),
            "lam": fy - wb * mu,
            "water_used": water,
            "mu": mu,
        }
    return out


def farm_value(land):
    """Value function of the land-only farm: 6000 sqrt(land / 5)."""
    return farm(land)["profit"]


if __name__ == "__main__":
    for f in (
        worked_example,
        ex_substitution,
        ex_lagrange_log,
        ex_corner,
        student_kinks,
        ex_dual,
    ):
        print(f.__name__, f())
    print("ex3", ex_level_slope())
    print("farm", farm())
    print("farm 21", farm_value(21) - farm_value(20))
    print("farm water 9000", farm(water=9000))
    print("farm water 6000", farm(water=6000))
