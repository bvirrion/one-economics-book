"""Opening chart: five published estimates of the elasticity of employment with
respect to the minimum wage, each as stated by its authors (cited numbers): the New
Jersey fast-food data of Card and Krueger and the payroll data of Neumark and
Wascher (both elasticities as computed by Neumark and Wascher), the traditional
state-panel and the contiguous-county estimates of Dube, Lester and Reich (the panel
value is the smallest magnitude they report), and the teen estimate of Neumark,
Salas and Wascher. Writes out/elasticities.csv with a row position."""
from cited import load_cited
from figout import write_table


def table():
    d = load_cited(__file__, "elasticities").drop(columns="ledger")
    d = d.iloc[::-1].reset_index(drop=True)
    d["pos"] = range(1, len(d) + 1)
    return d


if __name__ == "__main__":
    write_table(table(), __file__, "elasticities")
