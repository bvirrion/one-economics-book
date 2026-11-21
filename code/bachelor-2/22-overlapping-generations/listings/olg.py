"""Overlapping generations, log utility, Cobb-Douglas, with a pay-as-you-go pension d.
One period is a generation; capital lasts one period; thousands of dalens per young.
"""

ALPHA, BETA, N, A = 0.3, 0.6, 0.2, 10.0


def wage(k):
    return (1 - ALPHA) * A * k**ALPHA


def gross_return(k):
    return ALPHA * A * k ** (ALPHA - 1)


def next_k(k, d=0.0):
    """k' must equal s / (1 + n), where saving s depends on R(k'): bisect on k'."""
    w = wage(k)
    lo, hi = 1e-9, w
    for _ in range(100):
        k1 = (lo + hi) / 2
        s = BETA / (1 + BETA) * (w - d) - (1 + N) * d / ((1 + BETA) * gross_return(k1))
        lo, hi = (k1, hi) if s / (1 + N) > k1 else (lo, k1)
    return (lo + hi) / 2


def steady(d=0.0, k=1.0):
    for _ in range(500):
        k = next_k(k, d)
    return k


for d in (0.0, 1.0):
    k = steady(d)
    print(
        f"contribution {d:.1f}: k = {k:.3f}, wage {wage(k):.3f},"
        f" gross return {gross_return(k):.3f} (1 + n = {1 + N:.1f})"
    )
