from decimal import getcontext, ROUND_HALF_UP
from logger import log
from tax_constants import *

getcontext().rounding = ROUND_HALF_UP


def calculate_taxes(salary, pre_tax_investments=0):
    fed_tax = calculate_fed_tax(salary, pre_tax_investments)
    ss_tax = calculate_ss_tax(salary)
    medicare_tax = calculate_medicare_tax(salary)
    state_tax = calculate_state_tax(salary, pre_tax_investments)
    total = fed_tax + ss_tax + medicare_tax + state_tax
    return {"federal": fed_tax, "social_security": ss_tax, "medicare": medicare_tax, "state": state_tax, "total": total}


def calculate_fed_tax(salary, pre_tax_investments=0):
    taxable_income = calculate_taxable_income(salary, STANDARD_DEDUCTION, pre_tax_investments)
    total_tax = 0
    lower_limit = 0

    log.debug("\nCalculating Federal Tax")
    log.debug("  Base Salary: $%.2f", salary)
    log.debug("  Federal Taxable Income: $%.2f", taxable_income)
    log.debug("  Tax Brackets")

    for rate, upper_limit in TAX_BRACKETS.items():
        bracket_tax = 0
        if taxable_income > upper_limit:
            bracket_tax = rate * (upper_limit - lower_limit)
        elif taxable_income > lower_limit:
            bracket_tax = rate * (taxable_income - lower_limit)
        else:
            break

        total_tax += bracket_tax
        log.debug("  %d%%: $%d - $%d", rate * 100, lower_limit, upper_limit)
        log.debug("   Bracket Tax: $%.2f", bracket_tax)
        log.debug("   Total Tax: $%.2f", total_tax)
        lower_limit = upper_limit

    effective_tax_rate = total_tax / salary
    log.debug("  Effective Tax Rate: $%.2f", effective_tax_rate)

    return round(total_tax, 2)


def calculate_ss_tax(salary):
    ss_tax = salary * SOCIAL_SECURITY_TAX_RATE
    return round(ss_tax, 2)


def calculate_medicare_tax(salary):
    medicare_tax = salary * MEDICARE_TAX_RATE
    return round(medicare_tax, 2)


def calculate_state_tax(salary, pre_tax_investments=0):
    taxable_income = calculate_taxable_income(salary, PERSONAL_EXEMPTION, pre_tax_investments)
    log.debug("Calculating State Tax")
    log.debug("  Base Salary: $%.2f", salary)
    log.debug("  State Taxable Income: $%.2f", taxable_income)
    state_tax = taxable_income * IL_TAX_RATE
    return round(state_tax, 2)


def calculate_taxable_income(salary, deductions, pre_tax_investments=0):
    return salary - deductions - pre_tax_investments
