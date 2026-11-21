"""Strategic trade policy: a Home and a Foreign firm sell only in a third market.
Home's government pays its firm s per unit (s < 0 is an export tax). Home's welfare
is its firm's profit minus the subsidy bill."""
import numpy as np

A, C = 10.0, 2.0                      # Cournot: price A - (q_h + q_f), unit cost C


def cournot(s):
    q_h, q_f = (A - C + 2 * s) / 3, (A - C - s) / 3
    p = A - q_h - q_f
    return {"q_h": q_h, "q_f": q_f, "home": (p - C) * q_h, "foreign": (p - C) * q_f}


def bertrand(s):
    # differentiated goods: q_i = 10 - 2 p_i + p_j; Home's cost is C - s
    c_h, c_f = C - s, C
    # best responses p_i = (10 + p_j + 2 c_i) / 4, solved together
    p_h = (50 + 8 * c_h + 2 * c_f) / 15
    p_f = (10 + p_h + 2 * c_f) / 4
    q_h, q_f = 10 - 2 * p_h + p_f, 10 - 2 * p_f + p_h
    return {"p_h": p_h, "home": (p_h - C) * q_h, "foreign": (p_f - C) * q_f}


grid = np.round(np.linspace(-3, 3, 6001), 3)
for name, game in (("Cournot", cournot), ("Bertrand", bertrand)):
    w = [game(s)["home"] for s in grid]
    best = grid[int(np.argmax(w))]
    f, o = game(0.0), game(best)
    print(f"{name}: best s = {best:+.3f}; Home welfare {f['home']:.3f} -> "
          f"{o['home']:.3f}; Foreign profit {f['foreign']:.3f} -> {o['foreign']:.3f}")
c = cournot(2.0)
print(f"Cournot at s = 2: Home sells {c['q_h']:.3f}, Foreign {c['q_f']:.3f}")
