"""The pivot mechanism for a bridge that costs 300, shared equally by three residents.

Each reports a value; the bridge is built if the reported net values (value minus a
share of 100) sum to zero or more. A resident whose report changes the decision pays
the net loss that the change imposes on the other two.
"""

share = 100


def outcome(reports):
    net = [v - share for v in reports]
    build = sum(net) >= 0
    taxes = []
    for i in range(len(net)):
        others = sum(net) - net[i]
        pivotal = build != (others >= 0)
        taxes.append(abs(others) if pivotal else 0)
    return build, taxes


def payoff(i, true_value, reports):
    build, taxes = outcome(reports)
    return (true_value - share if build else 0) - taxes[i]


values = [250, 60, 40]
build, taxes = outcome(values)
print(f"truthful reports {values}: build {build}, taxes {taxes}")
for i, v in enumerate(values):
    truthful = payoff(i, v, values)
    best = max(payoff(i, v, values[:i] + [r] + values[i + 1 :]) for r in range(401))
    print(f"resident {i + 1}: truthful {truthful}, best of 401 reports {best}")
