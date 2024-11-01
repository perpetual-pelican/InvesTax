from flask import render_template
from app import app
from app.forms import TaxForm, InvestForm
from src.tax.tax_calculator import calculate_taxes
from src.invest.investment_calculator import calculate_cmpd_int


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/calculate_tax', methods=['GET', 'POST'])
def calculate_tax():
    form = TaxForm()
    salary = None
    taxes = None
    if form.validate_on_submit():
        salary = form.salary.data
        taxes = calculate_taxes(salary)
    return render_template('calculate_tax.html', title='Calculate Tax', salary=salary, taxes=taxes, form=form)


@app.route('/calculate_interest', methods=['GET', 'POST'])
def calculate_interest():
    form = InvestForm()
    initial = None
    yearly = None
    apy = None
    years = None
    total = None
    if form.validate_on_submit():
        initial = form.initial_contribution.data
        yearly = form.yearly_contribution.data
        apy = form.apy.data / 100
        years = form.years.data
        total = calculate_cmpd_int(initial, yearly, apy, years)
        total = "{amount:.2f}".format(amount=total)
    return render_template('calculate_interest.html', title='Calculate Interest', total=total, form=form)
