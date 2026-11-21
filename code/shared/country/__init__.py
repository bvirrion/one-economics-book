"""Brenland and Kestria: the invented economies of the series (COUNTRY.md).

    from country import load
    acc = load("accounts")          # a pandas DataFrame
    python -m country               # rewrite data/country/*.csv from the seed
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "data" / "country"
SEED = 2026
YEARS = list(range(2000, 2026))
# Income tax of 2025, on gross household income in dalens per year: (from, rate).
TAX_BANDS = [(0, 0.0), (12_000, 0.20), (40_000, 0.35), (100_000, 0.45)]
GOODS = {  # good: (qty_2015 per household per year, price_2015 in dalens)
    "bread": (300, 2.0), "rent": (12, 700.0), "transport": (100, 3.0),
    "clothing": (20, 40.0), "energy": (3000, 0.25),
}


def _tax(g: float) -> float:
    t = 0.0
    for (lo, r), nxt in zip(TAX_BANDS, TAX_BANDS[1:] + [(float("inf"), 0)]):
        if g > lo:
            t += (min(g, nxt[0]) - lo) * r
    return t


def _accounts(rng):
    growth = {y: 0.021 for y in YEARS}
    growth.update({2001: 0.012, 2008: 0.004, 2009: -0.031, 2010: 0.018, 2020: -0.052,
                   2021: 0.047, 2022: 0.028})
    infl = {y: 0.019 for y in YEARS}
    infl.update({2009: 0.004, 2015: 0.002, 2021: 0.032, 2022: 0.081, 2023: 0.054,
                 2024: 0.027})
    rows, real, defl, pop, debt, rate = [], 0.0, 0.0, 8000.0, 0.0, 3.0
    for y in YEARS:
        if y == 2000:
            real, defl, debt = 200_000.0, 76.0, 90_000.0
        else:
            real *= 1 + growth[y] + rng.normal(0, 0.002)
            defl *= 1 + infl[y] + rng.normal(0, 0.002)
            pop *= 1.006
        gdp = round(real * defl / 100)
        C = round(gdp * (0.58 + rng.normal(0, 0.004)))
        I = round(gdp * (0.21 + (0.03 if growth[y] > 0.02 else -0.02) * 0.5))
        G = round(gdp * (0.20 + (0.03 if growth[y] < 0 else 0)))
        X = round(gdp * (0.32 + 0.002 * (y - 2000) / 5))
        M = C + I + G + X - gdp
        lf = round(pop * 0.50)
        u = 6.0 - 40 * (growth[y] - 0.021) + rng.normal(0, 0.15)
        u = round(min(max(u, 3.5), 11.0), 1)
        emp = round(lf * (1 - u / 100))
        rev = round(gdp * (0.40 + (-0.01 if growth[y] < 0 else 0)))
        spend = round(gdp * (0.42 + (0.04 if growth[y] < 0 else 0)))
        deficit = spend - rev
        debt = debt + deficit if y > 2000 else debt
        # a smoothed Taylor-type rule: 70 % last year's rate, 30 % the rule's value
        rule = 1.0 + infl[y] * 100 + 0.25 * (infl[y] * 100 - 2) + 0.25 * (growth[y] * 100 - 2)
        rate = max(0.0, 0.7 * rate + 0.3 * max(rule, 0.0))
        rows.append(dict(year=y, pop=round(pop), labour_force=lf, employed=emp, unemp_rate=u,
                         real_gdp=round(real), gdp=gdp, deflator=round(defl, 1), C=C, I=I,
                         G=G, X=X, M=M, policy_rate=round(rate, 2), revenue=rev, spending=spend,
                         deficit=deficit, debt=round(debt)))
    acc = pd.DataFrame(rows)
    # rebase the deflator and real GDP to 2015 = 100
    d15 = acc.loc[acc.year == 2015, "deflator"].iloc[0]
    acc["deflator"] = (acc.deflator / d15 * 100).round(1)
    acc["real_gdp"] = (acc.gdp / acc.deflator * 100).round().astype(int)
    return acc, infl


def _basket(rng, infl):
    rows = []
    rel = {"bread": 0.0, "rent": 0.006, "transport": -0.004, "clothing": -0.012, "energy": 0.01}
    for g, (q, p15) in GOODS.items():
        level = {2015: p15}
        for y in range(2016, 2026):
            shock = 0.25 if (g == "energy" and y == 2022) else 0
            level[y] = level[y - 1] * (1 + infl[y] + rel[g] + shock + rng.normal(0, 0.003))
        for y in range(2014, 1999, -1):
            level[y] = level[y + 1] / (1 + infl[y + 1] + rel[g] + rng.normal(0, 0.003))
        for y in YEARS:
            rows.append(dict(year=y, good=g, qty_2015=q, price=round(level[y], 2)))
    b = pd.DataFrame(rows)
    cost = b.assign(c=b.qty_2015 * b.price).groupby("year").c.sum()
    cpi = (cost / cost.loc[2015] * 100).round(1)
    return b, cpi


def _households(rng, n=2000):
    size = rng.choice([1, 2, 3, 4, 5], n, p=[0.28, 0.32, 0.17, 0.16, 0.07])
    age = rng.integers(21, 80, n)
    school = np.clip(np.round(rng.normal(12.5, 2.6, n)), 6, 20).astype(int)
    retired = age >= 65
    hours = np.where(retired, 0, np.clip(np.round(rng.normal(1650, 250, n), -1), 0, 2600)).astype(int)
    hours[rng.random(n) < 0.06] = 0
    wage = np.exp(np.log(11) + 0.08 * (school - 12) + 0.03 * (np.minimum(age, 55) - 21)
                  - 0.0004 * (np.minimum(age, 55) - 21) ** 2 + rng.normal(0, 0.35, n))
    gross = np.round(wage * hours + np.where(retired, rng.normal(19000, 4000, n), 0), -1)
    gross = np.maximum(gross, 0)
    tax = np.round([_tax(g) for g in gross], -1)
    transfers = np.round(np.where(gross < 12000, 6000 + 1500 * (size - 1), 0)
                         + 1200 * np.maximum(size - 2, 0), -1)
    disp = gross - tax + transfers
    cons = np.round(np.minimum(disp, 4000 + 0.80 * disp + rng.normal(0, 1500, n)), -1)
    food = np.round(np.clip(1500 + 900 * size + 0.04 * cons + rng.normal(0, 300, n), 800, None), -1)
    food = np.minimum(food, cons * 0.6)
    owner = (rng.random(n) < 1 / (1 + np.exp(-(disp - 35000) / 12000))).astype(int)
    return pd.DataFrame(dict(hh=np.arange(1, n + 1), size=size, age_head=age, school_years=school,
                             hours=hours, gross_income=gross.astype(int), tax=tax.astype(int),
                             transfers=transfers.astype(int), disposable=disp.astype(int),
                             food=np.round(food, -1).astype(int), consumption=cons.astype(int),
                             owner=owner))


def _firms(rng, n=500):
    sector = rng.choice(["farming", "manufacturing", "services"], n, p=[0.12, 0.23, 0.65])
    workers = np.maximum(1, np.round(np.exp(rng.normal(2.2, 1.1, n)))).astype(int)
    cap = {"farming": 180, "manufacturing": 150, "services": 60}
    capital = np.round([w * cap[s] * np.exp(rng.normal(0, 0.3)) for w, s in zip(workers, sector)]).astype(int)
    out_k = 0.9 * workers ** 0.65 * capital ** 0.35 * np.exp(rng.normal(0, 0.15, n))
    output = np.round(out_k * 18).astype(int)
    wage_bill = np.round(workers * 38 * np.exp(rng.normal(0, 0.1, n))).astype(int)
    other = np.round(output * rng.uniform(0.25, 0.4, n)).astype(int)
    return pd.DataFrame(dict(firm=np.arange(1, n + 1), sector=sector, workers=workers, capital=capital,
                             output=output, wage_bill=wage_bill, other_costs=other,
                             profit=output - wage_bill - other))


def generate() -> dict[str, pd.DataFrame]:
    rng = np.random.default_rng(SEED)
    acc, infl = _accounts(rng)
    basket, cpi = _basket(rng, infl)
    acc["cpi"] = acc.year.map(cpi)
    acc = acc[["year", "pop", "labour_force", "employed", "unemp_rate", "real_gdp", "gdp", "deflator",
               "C", "I", "G", "X", "M", "cpi", "policy_rate", "revenue", "spending", "deficit", "debt"]]
    ric = pd.DataFrame(dict(country=["Brenland", "Brenland", "Kestria", "Kestria"],
                            good=["cloth", "grain", "cloth", "grain"],
                            hours_per_unit=[4, 2, 6, 12]))
    rate = [round(1.25 + 0.15 * np.sin((y - 2000) / 4) + rng.normal(0, 0.01), 3) for y in YEARS]
    trade = pd.DataFrame(dict(year=YEARS,
                              exports_to_kestria=(acc.X * 0.31).round().astype(int).values,
                              imports_from_kestria=(acc.M * 0.27).round().astype(int).values,
                              rate=rate))
    return dict(accounts=acc, basket=basket, households=_households(rng), firms=_firms(rng),
                ricardo=ric, trade=trade)


def write() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, df in generate().items():
        df.to_csv(OUT / f"{name}.csv", index=False, lineterminator="\n")


def load(name: str) -> pd.DataFrame:
    return pd.read_csv(OUT / f"{name}.csv")
