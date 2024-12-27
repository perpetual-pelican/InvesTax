import base64
import io

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from src.tax.tax_constants import TAX_YEAR

matplotlib.use('agg')


def plot_as_line_graph(num_years, totals=None, contributions=None):
    years = [year for year in range(1, num_years + 1)]
    fig, ax = plt.subplots()
    if totals is not None:
        plt.plot(years, totals, label="total", marker='o')
    if contributions is not None:
        plt.plot(years, contributions, label="contributions", marker='x')
    plt.legend()
    plt.grid(True)
    plt.xlabel("Years")
    plt.ylabel("Investment Total ($M)")
    fig.tight_layout()
    bytes_io = io.BytesIO()
    fig.savefig(bytes_io, format='png')
    bytes_io.seek(0)
    base64_data = base64.b64encode(bytes_io.read()).decode()
    plt.close()
    return base64_data


def plot_as_stack_graph(num_years, contributions, returns):
    years = [year for year in range(1, num_years + 1)]
    data = np.vstack([contributions, returns])

    fig, ax = plt.subplots()
    plt.stackplot(years, data, labels=["Contributions - ${0:.2f}".format(contributions[-1]), "Returns - ${0:.2f}".format(returns[-1])], colors=['#0485d1', '#02ab2e'])
    plt.legend(reverse=True)
    plt.grid(True)
    plt.title("Total Returns Over Time")
    plt.xlabel("Years")
    plt.ylabel("Investment Total ($)")
    fig.tight_layout()
    bytes_io = io.BytesIO()
    fig.savefig(bytes_io, format='png')
    bytes_io.seek(0)
    base64_data = base64.b64encode(bytes_io.read()).decode()
    plt.close()
    return base64_data


def plot_as_pie_chart(base_salary, taxes):
    sizes = [base_salary - taxes['total'], taxes['federal'], taxes['social_security'], taxes['medicare'], taxes['state']]
    labels = ['net income - $' + str(sizes[0]), 'federal - $' + str(sizes[1]), 'social security - $' + str(sizes[2]), 'medicare - $' + str(sizes[3]), 'state - $' + str(sizes[4])]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'}, textprops={'fontsize': 8, 'weight': 'bold'})
    plt.title('{0} Income Tax Breakdown for Yearly Income of ${1:.2f}'.format(TAX_YEAR, base_salary))
    fig.tight_layout()
    bytes_io = io.BytesIO()
    fig.savefig(bytes_io, format='png')
    bytes_io.seek(0)
    base64_data = base64.b64encode(bytes_io.read()).decode()
    plt.close()
    return base64_data
