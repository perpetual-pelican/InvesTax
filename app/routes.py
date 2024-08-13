from flask import render_template
from app import app
from app.forms import Form
from tax_calculator import calculate_taxes


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/calculate_tax', methods=['GET', 'POST'])
def calculate_tax():
    form = Form()
    salary = None
    taxes = None
    if form.validate_on_submit():
        salary = form.salary.data
        taxes = calculate_taxes(salary)
    return render_template('calculate_tax.html', title='Calculate Tax', salary=salary, taxes=taxes, form=form)
