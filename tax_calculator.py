import tax_constants
from logger import log

def salary_after_tax(salary, pre_tax_investments=0):
  return salary - calculate_total_tax(salary, pre_tax_investments)

def calculate_total_tax (salary, pre_tax_investments=0):
  fed_tax = calculate_fed_tax(salary, pre_tax_investments)
  ss_tax = calculate_ss_tax(salary)
  medicare_tax = calculate_medicare_tax(salary)
  state_tax = calculate_state_tax(salary, pre_tax_investments)
  return fed_tax + ss_tax + medicare_tax + state_tax

def calculate_fed_tax (salary, pre_tax_investments=0):
  taxable_income = calculate_taxable_income(salary, tax_constants.STANDARD_DEDUCTION, pre_tax_investments)
  total_tax = 0
  lower_limit = 0

  log.debug("\nBase Salary: $%.2f, Federal Taxable Income: $%.2f", salary, taxable_income)
  log.debug("Tax Brackets")
  
  for rate, upper_limit in tax_constants.TAX_BRACKETS.items():
    bracket_tax = 0
    if taxable_income > upper_limit:
      bracket_tax = rate * (upper_limit - lower_limit)
    elif taxable_income > lower_limit:
      bracket_tax = rate * (taxable_income - lower_limit)
    else:
      break

    log.debug("%d%%: $%d - $%d", rate*100, lower_limit, upper_limit)
    log.debug(" bracket tax: $%.2f", bracket_tax)
    log.debug(" total tax: $%.2f", total_tax)

    total_tax += bracket_tax
    lower_limit = upper_limit
  
  return total_tax

def calculate_ss_tax (salary):
  return salary * tax_constants.SOCIAL_SECURITY_TAX_RATE

def calculate_medicare_tax (salary):
  return salary * tax_constants.MEDICARE_TAX_RATE

def calculate_state_tax (salary, pre_tax_investments=0):
  taxable_income = calculate_taxable_income(salary, tax_constants.PERSONAL_EXEMPTION, pre_tax_investments)
  log.debug("\nBase Salary: $%.2f, State Taxable Income: $%.2f", salary, taxable_income)
  return taxable_income * tax_constants.IL_TAX_RATE

def calculate_taxable_income (salary, deductions, pre_tax_investments=0):
  return salary - deductions - pre_tax_investments
