from src.logger import log


def calculate_cmpd_int(initial_investment, yearly_investment, apy, years):
    int_factor = 1 + apy
    if years <= 1:
        log.debug("\nCalculating Compound Interest")
        log.debug("  Initial Investment: $%.2f", initial_investment)
        log.debug("  Yearly Investment: $%.2f", yearly_investment)
        log.debug("  APY: %.2f%%", apy * 100)
        total = initial_investment * int_factor
        log.debug("  Year %d Total: $%.2f", years, total)
        return total
    sub_total = calculate_cmpd_int(initial_investment, yearly_investment, apy, years - 1)
    total = (sub_total + yearly_investment) * int_factor
    log.debug("  Year %d Total: $%.2f", years, total)
    return total
