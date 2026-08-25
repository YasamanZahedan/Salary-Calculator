from decimal import Decimal

from src.config import TaxRules2026


class MunicipalTaxCalculator:
    def calculate(self, taxable_income: Decimal) -> Decimal:
        if taxable_income <= TaxRules2026.MILAN_EXEMPTION_THRESHOLD:
            return Decimal("0")

        return taxable_income * TaxRules2026.MILAN_RATE