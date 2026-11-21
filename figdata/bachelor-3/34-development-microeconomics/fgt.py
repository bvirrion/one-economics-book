"""Foster--Greer--Thorbecke poverty measures."""
import numpy as np


def fgt(y, z, alpha, w=None):
    """P_alpha = sum of w * ((z - y) / z) ** alpha over y < z, divided by sum w."""
    y = np.asarray(y, dtype=float)
    w = np.ones_like(y) if w is None else np.asarray(w, dtype=float)
    poor = y < z
    g = np.where(poor, (z - y) / z, 0.0)
    return float((w * poor * g ** alpha).sum() / w.sum())
