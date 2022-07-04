from logger import log
import tax_calculator as tax
import investment_calculator as invest

log.setLevel("INFO")

SALARY = 100000
PRE_TAX_INVESTMENTS=5000
PRE_TAX_APY = 0.05
PRE_TAX_YEARS = 40
POST_TAX_INVESTMENTS=3000
POST_TAX_APY = 0.1
POST_TAX_YEARS = 15

fed_tax = tax.calculate_fed_tax(SALARY, PRE_TAX_INVESTMENTS)
ss_tax = tax.calculate_ss_tax(SALARY)
medicare_tax = tax.calculate_medicare_tax(SALARY)
state_tax = tax.calculate_state_tax(SALARY, PRE_TAX_INVESTMENTS)
total_tax = fed_tax + ss_tax + medicare_tax + state_tax
salary_after_tax = SALARY - total_tax
salary_after_investments = salary_after_tax - PRE_TAX_INVESTMENTS - POST_TAX_INVESTMENTS

log.info("\nBase Salary: $%.2f", SALARY)
log.info("\nPre-tax Investments: $%.2f at %.2f%% for %d years", PRE_TAX_INVESTMENTS, PRE_TAX_APY*100, PRE_TAX_YEARS)
log.info("Post-tax Investments: $%.2f at %.2f%% for %d years", POST_TAX_INVESTMENTS, POST_TAX_APY*100, POST_TAX_YEARS)

log.debug("\nFederal Tax: $%.2f", fed_tax)
log.debug("Social Security Tax: $%.2f", ss_tax)
log.debug("Medicare Tax: $%.2f", medicare_tax)
log.debug("State Tax: $%.2f", state_tax)

log.info("\nTotal Income Tax: $%.2f", total_tax)
log.info("Salary after tax: $%.2f", salary_after_tax)
log.info("Salary after tax and investments: $%.2f", salary_after_investments)

pre_tax_total = invest.calculate_cmpd_int(PRE_TAX_INVESTMENTS, PRE_TAX_APY, PRE_TAX_YEARS)
log.info("\nTotal pre-tax contributions: $%.2f", PRE_TAX_INVESTMENTS * PRE_TAX_YEARS)
log.info("Total pre-tax earnings: $%.2f", pre_tax_total - (PRE_TAX_INVESTMENTS * PRE_TAX_YEARS))
log.info("Total pre-tax savings: $%.2f", pre_tax_total)

pre_tax_total = invest.calculate_cmpd_int(POST_TAX_INVESTMENTS, POST_TAX_APY, POST_TAX_YEARS)
log.info("\nTotal post-tax contributions: $%.2f", POST_TAX_INVESTMENTS * POST_TAX_YEARS)
log.info("Total post-tax earnings: $%.2f", pre_tax_total - (POST_TAX_INVESTMENTS * POST_TAX_YEARS))
log.info("Total post-tax savings: $%.2f", pre_tax_total)
