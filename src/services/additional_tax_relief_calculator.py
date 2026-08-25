from decimal import Decimal

from src.config import TaxRules2026


class AdditionalTaxReliefCalculator:
    def calculate(self, taxable_income: Decimal) -> Decimal:
        if (
            taxable_income
            <= TaxRules2026.ADDITIONAL_RELIEF_FIRST_THRESHOLD
        ):
            return Decimal("0")

        if (
            taxable_income
            <= TaxRules2026.ADDITIONAL_RELIEF_SECOND_THRESHOLD
        ):
            return TaxRules2026.ADDITIONAL_RELIEF_MAX_AMOUNT

        if (
            taxable_income
            <= TaxRules2026.ADDITIONAL_RELIEF_THIRD_THRESHOLD
        ):
            return (
                TaxRules2026.ADDITIONAL_RELIEF_MAX_AMOUNT
                * (
                    TaxRules2026.ADDITIONAL_RELIEF_THIRD_THRESHOLD
                    - taxable_income
                )
                / TaxRules2026.ADDITIONAL_RELIEF_TAPER_RANGE
            )

        return Decimal("0")