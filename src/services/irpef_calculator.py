from decimal import Decimal

from src.config import TaxRules2026


class IrpefCalculator:
    def calculate(self, taxable_income: Decimal) -> Decimal:
        if taxable_income <= Decimal("0"):
            return Decimal("0")

        first_threshold = TaxRules2026.IRPEF_FIRST_THRESHOLD
        second_threshold = TaxRules2026.IRPEF_SECOND_THRESHOLD

        first_rate = TaxRules2026.IRPEF_FIRST_RATE
        second_rate = TaxRules2026.IRPEF_SECOND_RATE
        third_rate = TaxRules2026.IRPEF_THIRD_RATE

        if taxable_income <= first_threshold:
            return taxable_income * first_rate

        if taxable_income <= second_threshold:
            first_band_tax = first_threshold * first_rate
            second_band_tax = (
                taxable_income - first_threshold
            ) * second_rate

            return first_band_tax + second_band_tax

        first_band_tax = first_threshold * first_rate

        second_band_tax = (
            second_threshold - first_threshold
        ) * second_rate

        third_band_tax = (
            taxable_income - second_threshold
        ) * third_rate

        return (
            first_band_tax
            + second_band_tax
            + third_band_tax
        )