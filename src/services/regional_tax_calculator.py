from decimal import Decimal

from src.config import TaxRules2026


class RegionalTaxCalculator:
    def calculate(self, taxable_income: Decimal) -> Decimal:
        if taxable_income <= Decimal("0"):
            return Decimal("0")

        first_threshold = TaxRules2026.LOMBARDY_FIRST_THRESHOLD
        second_threshold = TaxRules2026.LOMBARDY_SECOND_THRESHOLD
        third_threshold = TaxRules2026.LOMBARDY_THIRD_THRESHOLD

        if taxable_income <= first_threshold:
            return taxable_income * TaxRules2026.LOMBARDY_FIRST_RATE

        if taxable_income <= second_threshold:
            first_band = (
                first_threshold
                * TaxRules2026.LOMBARDY_FIRST_RATE
            )

            second_band = (
                taxable_income - first_threshold
            ) * TaxRules2026.LOMBARDY_SECOND_RATE

            return first_band + second_band

        if taxable_income <= third_threshold:
            first_band = (
                first_threshold
                * TaxRules2026.LOMBARDY_FIRST_RATE
            )

            second_band = (
                second_threshold - first_threshold
            ) * TaxRules2026.LOMBARDY_SECOND_RATE

            third_band = (
                taxable_income - second_threshold
            ) * TaxRules2026.LOMBARDY_THIRD_RATE

            return first_band + second_band + third_band

        first_band = (
            first_threshold
            * TaxRules2026.LOMBARDY_FIRST_RATE
        )

        second_band = (
            second_threshold - first_threshold
        ) * TaxRules2026.LOMBARDY_SECOND_RATE

        third_band = (
            third_threshold - second_threshold
        ) * TaxRules2026.LOMBARDY_THIRD_RATE

        fourth_band = (
            taxable_income - third_threshold
        ) * TaxRules2026.LOMBARDY_FOURTH_RATE

        return (
            first_band
            + second_band
            + third_band
            + fourth_band
        )