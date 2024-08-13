from collections import OrderedDict
from decimal import Decimal
from math import inf

TAX_YEAR = 2024

# 2022 Tax Brackets
# TAX_BRACKETS = OrderedDict()
# TAX_BRACKETS[Decimal("0.1")] = 10275
# TAX_BRACKETS[Decimal("0.12")] = 41775
# TAX_BRACKETS[Decimal("0.22")] = 89075
# TAX_BRACKETS[Decimal("0.24")] = 170050
# TAX_BRACKETS[Decimal("0.32")] = 215950
# TAX_BRACKETS[Decimal("0.35")] = 539900
# TAX_BRACKETS[Decimal("0.37")] = inf

# 2024 Tax Brackets
TAX_BRACKETS = OrderedDict()
TAX_BRACKETS[Decimal("0.1")] = 11600
TAX_BRACKETS[Decimal("0.12")] = 47150
TAX_BRACKETS[Decimal("0.22")] = 100525
TAX_BRACKETS[Decimal("0.24")] = 191950
TAX_BRACKETS[Decimal("0.32")] = 243725
TAX_BRACKETS[Decimal("0.35")] = 609350
TAX_BRACKETS[Decimal("0.37")] = inf

STANDARD_DEDUCTION = 12950
SOCIAL_SECURITY_TAX_RATE = Decimal("0.062")
MEDICARE_TAX_RATE = Decimal("0.0145")
PERSONAL_EXEMPTION = 2225
IL_TAX_RATE = Decimal("0.0495")
