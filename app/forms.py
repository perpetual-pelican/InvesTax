from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from src.tax.tax_constants import FILING_STATUS_CHOICES


class TaxForm(FlaskForm):
    salary = DecimalField('Salary', validators=[NumberRange(min=1)])
    filing_status = SelectField('Filing Status', choices=FILING_STATUS_CHOICES, validators=[DataRequired()])
    submit_tax = SubmitField('Calculate Income Tax')


class InvestForm(FlaskForm):
    initial_contribution = DecimalField('Initial Contribution',
                                        validators=[NumberRange(min=0)])
    yearly_contribution = DecimalField('Yearly Contribution',
                                        validators=[NumberRange(min=0)])
    apy = DecimalField('APY', validators=[NumberRange(min=0)])
    years = IntegerField('Years', validators=[NumberRange(min=1)])
    submit_invest = SubmitField('Calculate Compound Interest')


class InvesTaxForm(FlaskForm):
    initial_contribution = DecimalField('Initial Contribution',
                                        validators=[NumberRange(min=0)])
    yearly_contribution = DecimalField('Yearly Contribution',
                                        validators=[NumberRange(min=0)])
    apy = DecimalField('APY', validators=[NumberRange(min=0)])
    years = IntegerField('Years', validators=[NumberRange(min=1)])
    salary = DecimalField('Salary', validators=[NumberRange(min=1)])
    filing_status = SelectField('Filing Status', choices=FILING_STATUS_CHOICES, validators=[DataRequired()])
    submit = SubmitField('Calculate')
