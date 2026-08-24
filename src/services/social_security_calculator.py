from decimal import Decimal

from src.config import TaxRules2026


class SocialSecurityCalculator:
    def calculate(self, annual_gross_salary: Decimal) -> Decimal:
        standard_contribution = (
            annual_gross_salary * TaxRules2026.EMPLOYEE_INPS_RATE
        )

        additional_contribution = Decimal("0")

        if annual_gross_salary > TaxRules2026.ADDITIONAL_INPS_THRESHOLD:
            excess_income = (
                annual_gross_salary
                - TaxRules2026.ADDITIONAL_INPS_THRESHOLD
            )

            additional_contribution = (
                excess_income * TaxRules2026.ADDITIONAL_INPS_RATE
            )

        return standard_contribution + additional_contribution