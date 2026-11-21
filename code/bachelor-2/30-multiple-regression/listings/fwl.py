"""Frisch-Waugh-Lovell: the education coefficient by partialling out the controls."""

import numpy as np
from econdata import nsw

d = nsw("cps_controls")
d = d[(d.re78 > 0) & (d.re75 > 0)]
y = np.log(d.re78).to_numpy()
x = d.education.to_numpy(dtype=float)
W = np.column_stack([np.ones(len(d)), d.age, d.age**2, d.black, d.hispanic, d.married])


def resid(v, M):
    """Residual of v after least squares on the columns of M."""
    return v - M @ np.linalg.lstsq(M, v, rcond=None)[0]


b_long = np.linalg.lstsq(np.column_stack([x, W]), y, rcond=None)[0][0]
rx = resid(x, W)
ry = resid(y, W)
b_fwl = (rx @ ry) / (rx @ rx)
b_half = (rx @ y) / (rx @ rx)
b_short = np.linalg.lstsq(np.column_stack([np.ones(len(d)), x]), y, rcond=None)[0][1]

print(f"long regression:               {b_long:.6f}")
print(f"residual on residual:          {b_fwl:.6f}")
print(f"y on residualised x:           {b_half:.6f}")
print(f"education alone (no controls): {b_short:.6f}")
print(f"variance of x {x.var():.3f}; of its residual {rx.var():.3f}")
