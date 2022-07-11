from decimal import getcontext, ROUND_HALF_UP
import tax_constants
from logger import log

getcontext().rounding = ROUND_HALF_UP

def calculate_taxes (salary, pre_tax_investments=0):
  fed_tax = calculate_fed_tax(salary, pre_tax_investments)
  ss_tax = calculate_ss_tax(salary)
  medicare_tax = calculate_medicare_tax(salary)
  state_tax = calculate_state_tax(salary, pre_tax_investments)
  total = fed_tax + ss_tax + medicare_tax + state_tax
  return { "federal": fed_tax, "social_security": ss_tax, "medicare": medicare_tax, "state": state_tax, "total": total }

def calculate_fed_tax (salary, pre_tax_investments=0):
  taxable_income = calculate_taxable_income(salary, tax_constants.STANDARD_DEDUCTION, pre_tax_investments)
  total_tax = 0
  lower_limit = 0

  log.debug("\nCalculating Federal Tax")
  log.debug("  Base Salary: $%.2f", salary)
  log.debug("  Federal Taxable Income: $%.2f", taxable_income)
  log.debug("  Tax Brackets")
  
  for rate, upper_limit in tax_constants.TAX_BRACKETS.items():
    bracket_tax = 0
    if taxable_income > upper_limit:
      bracket_tax = rate * (upper_limit - lower_limit)
    elif taxable_income > lower_limit:
      bracket_tax = rate * (taxable_income - lower_limit)
    else:
      break

    log.debug("  %d%%: $%d - $%d", rate*100, lower_limit, upper_limit)
    log.debug("   bracket tax: $%.2f", bracket_tax)
    log.debug("   total tax: $%.2f", total_tax)

    total_tax += bracket_tax
    lower_limit = upper_limit
  
  return round(total_tax, 2)

def calculate_ss_tax (salary):
  ss_tax = salary * tax_constants.SOCIAL_SECURITY_TAX_RATE
  return round(ss_tax, 2)

def calculate_medicare_tax (salary):
  medicare_tax = salary * tax_constants.MEDICARE_TAX_RATE
  return round(medicare_tax, 2)

def calculate_state_tax (salary, pre_tax_investments=0):
  taxable_income = calculate_taxable_income(salary, tax_constants.PERSONAL_EXEMPTION, pre_tax_investments)
  log.debug("Calculating State Tax")
  log.debug("  Base Salary: $%.2f", salary)
  log.debug("  State Taxable Income: $%.2f", taxable_income)
  state_tax = taxable_income * tax_constants.IL_TAX_RATE
  return round(state_tax, 2)

def calculate_taxable_income (salary, deductions, pre_tax_investments=0):
  return salary - deductions - pre_tax_investments
