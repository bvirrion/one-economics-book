"""Month-on-month, twelve-month and annualised changes of consumer prices."""

from cpi_tools import monthly

for sid, name in [("CUUR0000SA0", "not adjusted"), ("CUSR0000SA0", "adjusted")]:
    cpi = monthly(sid)
    mom = 100 * (cpi / cpi.shift(1) - 1)
    yoy = 100 * (cpi / cpi.shift(12) - 1)
    ann = 100 * ((cpi / cpi.shift(1)) ** 12 - 1)  # one month's change, compounded
    print(f"June 2022, {name}:")
    print(f"  month on month   {mom.loc[(2022, 6)]:6.2f}")
    print(f"  twelve months    {yoy.loc[(2022, 6)]:6.2f}")
    print(f"  annualised       {ann.loc[(2022, 6)]:6.2f}")
