"""Gravity fits shared by this chapter's charts (same specifications as the listings
gravity_fe.py and gravity_ppml.py in code/bachelor-3/10-gravity)."""
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from econdata import gravity

COLS = ["year", "iso3_o", "iso3_d", "tradeflow_baci", "dist", "contig",
        "comlang_off", "col45", "fta_wto"]
RHS = "ln_dist + contig + comlang_off + col45 + fta_wto + C(iso3_o) + C(iso3_d)"


def load(year):
    """One year of positive flows with the pair variables (rows with gaps dropped)."""
    d = gravity(since=year, until=year, columns=COLS).dropna()
    d["ln_dist"] = np.log(d.dist)
    d["ln_x"] = np.log(d.tradeflow_baci)
    d["x"] = d.tradeflow_baci / 1e3
    return d


def ols_fe(d):
    """OLS on log flows with exporter and importer dummies, robust errors."""
    return smf.ols("ln_x ~ " + RHS, data=d).fit(cov_type="HC1")


def ppml_fe(d):
    """Poisson pseudo-maximum likelihood with the same dummies, robust errors."""
    return smf.glm("x ~ " + RHS, data=d, family=sm.families.Poisson()).fit(cov_type="HC1")
