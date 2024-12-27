from src.logger import log


class InvestmentCalculator:
    def __init__(self, initial_contribution, yearly_contribution, apy, duration):
        self.initial_contribution = initial_contribution
        self.yearly_contribution = yearly_contribution
        self.apy = apy
        self.duration = duration
        self.totals = []
        self.contributions = []
        self.returns = []

    def calculate_cmpd_int_yearly(self, years=None):
        initial_contribution = self.initial_contribution
        yearly_contribution = self.yearly_contribution
        apy = self.apy
        if years is None:
            years = self.duration
        int_factor = 1 + apy
        if years <= 1:
            log.debug("\nCalculating Compound Interest - Yearly")
            log.debug("  Initial Investment: $%.2f", initial_contribution)
            log.debug("  Yearly Investment: $%.2f", yearly_contribution)
            log.debug("  APY: %.2f%%", apy * 100)
            total = initial_contribution * int_factor
            log.debug("  Year %d Total: $%.2f", years, total)
            return total
        sub_total = self.calculate_cmpd_int_yearly(years - 1)
        total = (sub_total + yearly_contribution) * int_factor
        log.debug("  Year %d Total: $%.2f", years, total)
        return total

    def calculate_cmpd_int_list_yearly(self, years=None):
        initial_contribution = self.initial_contribution
        yearly_contribution = self.yearly_contribution
        apy = self.apy
        totals = self.totals
        contributions = self.contributions
        returns = self.returns
        if years is None:
            years = self.duration
        int_factor = 1 + apy
        if years <= 1:
            log.debug("\nCalculating Compound Interest - Yearly")
            log.debug("  Initial Investment: $%.2f", initial_contribution)
            log.debug("  Yearly Investment: $%.2f", yearly_contribution)
            log.debug("  APY: %.2f%%", apy * 100)
            total = initial_contribution * int_factor
            log.debug("  Year %d Total: $%.2f", years, total)
            totals.append(total)
            contributions.append(initial_contribution)
            returns.append(total - initial_contribution)
            log.debug("  Totals List: " + " ".join(map(str, totals)))
            log.debug("  Contributions List: " + " ".join(map(str, contributions)))
            log.debug("  Returns List: " + " ".join(map(str, returns)))
            return totals, contributions, returns
        sub_totals, sub_contributions, _ = self.calculate_cmpd_int_list_yearly(years - 1)
        total = (sub_totals[-1] + yearly_contribution) * int_factor
        total_contribution = (sub_contributions[-1] + yearly_contribution)
        log.debug("  Year %d Total: $%.2f", years, total)
        totals.append(total)
        contributions.append(total_contribution)
        returns.append(total - contributions[-1])
        log.debug("  Totals List: " + " ".join(map(str, totals)))
        log.debug("  Contributions List: " + " ".join(map(str, contributions)))
        log.debug("  Returns List: " + " ".join(map(str, returns)))
        return totals, contributions, returns
