"""The Bank of Brenland (weekend problem). Policy rate and CPI from the country
tables; the balance sheet, reserve demand and yields are the problem's assumptions
(billions of dalens, end of 2019).

Assets: government bonds 60 at 3.0 %, loans to banks 10 at the policy rate, foreign
reserves 30 in kest bonds at 3.0 %. Liabilities: currency 50, bank reserves 40,
government deposits 10 (no interest on currency or government deposits).
Corridor: deposit rate i - 0.5, lending rate i + 0.5; reserve demand
R(r) = 20 + 40 (i_L - r) / (i_L - i_D) between the two rates.
In 2020 the bank buys 40 of long bonds yielding 2.0 % from banks, paid in reserves,
and moves to a floor: the deposit rate is set equal to the policy rate.
"""
from country import load

BONDS, BOND_Y, LOANS, FX, FX_Y = 60.0, 3.0, 10.0, 30.0, 3.0
CURRENCY, RESERVES, GOV = 50.0, 40.0, 10.0
QE, QE_Y = 40.0, 2.0
R_MIN, R_SPAN = 20.0, 40.0
R_STAR, PI_STAR, PHI = 1.0, 2.0, 0.5


def overnight(i, supply):
    """Overnight rate in the corridor (i - 0.5, i + 0.5) given reserve supply."""
    lo, hi = i - 0.5, i + 0.5
    if supply >= R_MIN + R_SPAN:
        return lo
    if supply <= R_MIN:
        return hi
    return hi - (supply - R_MIN) / R_SPAN * (hi - lo)


def income_corridor(i, reserves=RESERVES):
    """Net interest income (billions) with reserves paid the deposit rate i - 0.5."""
    return (BONDS * BOND_Y + FX * FX_Y + LOANS * i - reserves * (i - 0.5)) / 100


def income_floor(i, reserves=RESERVES + QE):
    """Net interest income after the purchase, reserves paid the policy rate."""
    return (BONDS * BOND_Y + QE * QE_Y + FX * FX_Y + LOANS * i - reserves * i) / 100


def rule(pi, gap=0.0):
    """The Year 2 volume's rule: i = r* + pi + 0.5 (pi - pi*) + 0.5 gap."""
    return R_STAR + pi + PHI * (pi - PI_STAR) + PHI * gap


def data():
    a = load("accounts")[["year", "cpi", "policy_rate", "gdp"]].copy()
    a["infl"] = 100 * a.cpi.pct_change()
    return a[a.year.between(2019, 2025)].reset_index(drop=True)
