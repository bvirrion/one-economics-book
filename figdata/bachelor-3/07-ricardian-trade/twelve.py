"""Helper for the weekend problem (Brenland and Kestria with twelve goods): equilibrium of
a Ricardian model with discrete goods, equal expenditure shares and an iceberg factor
kappa >= 1. Goods are ranked by A_i = a_K,i / a_B,i. omega = w_B / w_K, r = L_K / L_B.

Brenland sells good i in Kestria when kappa w_B a_B,i <= w_K a_K,i (A_i >= kappa omega);
Kestria sells good i in Brenland when A_i <= omega / kappa. With equal shares, trade
balances when omega * (goods Brenland imports) = r * (goods Brenland exports), counting a
good at a threshold fractionally. f(omega) = r E(omega) - omega M(omega) falls with
omega, so the equilibrium is unique; it is found among the thresholds and the interior
solutions r e / m.
"""


def classify(A, omega, kappa, tol=1e-9):
    E = sum(a > kappa * omega + tol for a in A)
    M = sum(a < omega / kappa - tol for a in A)
    mE = sum(abs(a - kappa * omega) <= tol for a in A)
    mM = sum(abs(a - omega / kappa) <= tol for a in A)
    return E, M, mE, mM


def equilibrium(A, r, kappa=1.0):
    """(omega, exported, imported, nontraded); exported/imported may be fractional."""
    n = len(A)
    cands = {a / kappa for a in A} | {kappa * a for a in A}
    cands |= {r * e / m for e in range(1, n) for m in range(1, n)}
    for w in sorted(cands):
        E, M, mE, mM = classify(A, w, kappa)
        if kappa == 1.0 and mE:            # one good, made by both countries
            # Brenland makes share s of the marginal good's world supply
            s = (w * (M + 1) - r * E) / (r + w)
            if -1e-12 <= s <= 1 + 1e-12:
                return w, E + s, M + 1 - s, 0
            continue
        lo = r * E - w * (M + mM)
        hi = r * (E + mE) - w * M
        if lo <= 1e-12 and hi >= -1e-12:
            if mE:
                x = (w * M - r * E) / r
                return w, E + x, M, n - E - M - x
            if mM:
                y = (r * E - w * M) / w
                return w, E, M + y, n - E - M - y
            return w, E, M, n - E - M
    raise ValueError("no equilibrium")


def real_gain(A, omega, kappa=1.0):
    """Brenland's real-wage gain over autarky, equal shares: the product over goods it
    imports of (omega / (kappa A_i))^(1/n), minus one (a split good counts as made at
    home, where its price is unchanged)."""
    g = 1.0
    for a in A:
        if a < omega / kappa - 1e-9:
            g *= (omega / (kappa * a)) ** (1 / len(A))
    return g - 1


def real_gain_foreign(A, omega, kappa=1.0):
    """Kestria's real-wage gain over its autarky: the product over goods it imports from
    Brenland (A_i > kappa omega) of (A_i / (kappa omega))^(1/n), minus one."""
    g = 1.0
    for a in A:
        if a > kappa * omega + 1e-9:
            g *= (a / (kappa * omega)) ** (1 / len(A))
    return g - 1
