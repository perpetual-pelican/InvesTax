
def calculate_cmpd_int (yearly_investment, apy, years):
  int_factor = 1 + apy
  if years < 1:
    return 0
  sub_total = calculate_cmpd_int(yearly_investment, apy, years - 1)
  return (sub_total + yearly_investment) * int_factor
