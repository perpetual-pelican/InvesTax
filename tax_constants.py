from collections import OrderedDict
from math import inf

# 2022 Tax Brackets
TAX_BRACKETS = OrderedDict()
TAX_BRACKETS[0.1] = 10275
TAX_BRACKETS[0.12] = 41775
TAX_BRACKETS[0.22] = 89075
TAX_BRACKETS[0.24] = 170050
TAX_BRACKETS[0.32] = 215950
TAX_BRACKETS[0.35] = 539900
TAX_BRACKETS[0.37] = inf

STANDARD_DEDUCTION = 12950
SOCIAL_SECURITY_TAX_RATE = 0.062
MEDICARE_TAX_RATE = 0.0145
PERSONAL_EXEMPTION = 2225
IL_TAX_RATE = 0.0495
