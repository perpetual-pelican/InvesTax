from flask import render_template
from app import app
from app.forms import TaxForm, InvestForm
from src.tax.tax_calculator import calculate_taxes
from src.invest.investment_calculator import InvestmentCalculator
from src.visuals.plotting import plot_as_pie_chart, plot_as_stack_graph


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    invest_form = InvestForm()
    total = None
    effective_rate = None
    base64_invest_figure = None

    tax_form = TaxForm()
    salary = None
    taxes = None
    base64_tax_figure = None

    if invest_form.submit_invest.data and invest_form.validate_on_submit():
        initial = invest_form.initial_contribution.data
        yearly = invest_form.yearly_contribution.data
        apy = invest_form.apy.data / 100
        years = invest_form.years.data
        calc = InvestmentCalculator(initial, yearly, apy, years)
        totals, contributions, returns = calc.calculate_cmpd_int_list_yearly()
        total = round(totals[-1], 2)
        if contributions[-1] > 0:
            effective_rate = round((returns[-1] / contributions[-1]) * 100, 1)
        else:
            effective_rate = 0
        base64_invest_figure = plot_as_stack_graph(years, contributions, returns)

    if tax_form.submit_tax.data and tax_form.validate_on_submit():
        salary = tax_form.salary.data
        filing_status = tax_form.filing_status.data
        taxes = calculate_taxes(salary, filing_status=filing_status)
        base64_tax_figure = plot_as_pie_chart(salary, taxes)
        salary = round(salary, 2)

    return render_template('index.html', title='Calculate Interest and Tax', invest_form=invest_form, tax_form=tax_form,
                           total=total, effective_rate=effective_rate, salary=salary, taxes=taxes, base64_invest_figure=base64_invest_figure, base64_tax_figure=base64_tax_figure)


@app.route('/calculate_interest', methods=['GET', 'POST'])
def calculate_interest():
    invest_form = InvestForm()
    total = None
    effective_rate = None
    base64_figure = None
    if invest_form.validate_on_submit():
        initial = invest_form.initial_contribution.data
        yearly = invest_form.yearly_contribution.data
        apy = invest_form.apy.data / 100
        years = invest_form.years.data
        calc = InvestmentCalculator(initial, yearly, apy, years)
        totals, contributions, returns = calc.calculate_cmpd_int_list_yearly()
        total = round(totals[-1], 2)
        if contributions[-1] > 0:
            effective_rate = round((returns[-1] / contributions[-1]) * 100, 1)
        else:
            effective_rate = 0
        base64_figure = plot_as_stack_graph(years, contributions, returns)
    return render_template('calculate_interest.html', title='Calculate Interest', invest_form=invest_form, total=total,
                           effective_rate=effective_rate, base64_figure=base64_figure)


@app.route('/calculate_tax', methods=['GET', 'POST'])
def calculate_tax():
    tax_form = TaxForm()
    salary = None
    taxes = None
    base64_figure = None
    if tax_form.validate_on_submit():
        salary = tax_form.salary.data
        filing_status = tax_form.filing_status.data
        taxes = calculate_taxes(salary, filing_status=filing_status)
        salary = round(salary, 2)
        base64_figure = plot_as_pie_chart(salary, taxes)
    return render_template('calculate_tax.html', title='Calculate Tax', tax_form=tax_form, salary=salary, taxes=taxes, base64_figure=base64_figure)
