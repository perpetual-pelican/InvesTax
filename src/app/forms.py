from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, SubmitField
from wtforms.validators import InputRequired, ValidationError


class SalaryPositive(object):
    def __init__(self, message=None):
        if not message:
            message = 'Salary must be greater than zero'
        self.message = message

    def __call__(self, form, field):
        value = field.data or 0
        if value <= 0:
            raise ValidationError(self.message)


class InitialContributionPositive(object):
    def __init__(self, message=None):
        if not message:
            message = 'Initial Contribution must be greater than zero'
        self.message = message

    def __call__(self, form, field):
        value = field.data or 0
        if value <= 0:
            raise ValidationError(self.message)


class YearlyContributionPositive(object):
    def __init__(self, message=None):
        if not message:
            message = 'Yearly Contribution must be positive'
        self.message = message

    def __call__(self, form, field):
        value = field.data or 0
        if value < 0:
            raise ValidationError(self.message)


class YearsPositive(object):
    def __init__(self, message=None):
        if not message:
            message = 'Years must be greater than zero'
        self.message = message

    def __call__(self, form, field):
        value = field.data or 0
        if value <= 0:
            raise ValidationError(self.message)


class TaxForm(FlaskForm):
    salary = DecimalField('Salary', validators=[InputRequired(), SalaryPositive()])
    submit = SubmitField('Calculate Income Tax')


class InvestForm(FlaskForm):
    initial_contribution = DecimalField('Initial Contribution',
                                        validators=[InputRequired(), InitialContributionPositive()])
    yearly_contribution = DecimalField('Yearly Contribution',
                                        validators=[InputRequired(), YearlyContributionPositive()])
    apy = DecimalField('APY', validators=[InputRequired()])
    years = IntegerField('Years', validators=[InputRequired(), YearsPositive()])
    submit = SubmitField('Calculate Compound Interest')
