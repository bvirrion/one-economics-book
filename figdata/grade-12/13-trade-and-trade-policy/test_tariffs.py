import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_tariffs_fell():
    k = pd.read_csv(OUT / "tariff_key.csv").iloc[0]
    assert k.chn1992 > 30 and k.chn2022 < 3 and k.ind1990 > 50 and k.ind2022 < 6
    assert k.usa2019 > 3 * k.usa_other_max


def test_kestria_accounts():
    k = pd.read_csv(OUT / "kestria_key.csv").iloc[0]
    assert abs(k.cs_loss - k.ps_gain - k.rev - k.dwl) < 1e-9
    assert abs(k.dwl - k.dwl_prod - k.dwl_cons) < 1e-9
    assert k.dwl == 64 and k.net_loss == 106
