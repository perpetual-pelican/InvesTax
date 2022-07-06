from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
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

class Form(FlaskForm):
  salary = DecimalField('Salary', validators=[InputRequired(), SalaryPositive()])
  submit = SubmitField('Calculate Income Tax')
