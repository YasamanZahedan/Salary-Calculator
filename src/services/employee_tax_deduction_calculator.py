from decimal import Decimal

from src.config import TaxRules2026


class EmployeeTaxDeductionCalculator:
    def calculate(self, taxable_income: Decimal) -> Decimal:
        if taxable_income <= Decimal("0"):
            return Decimal("0")

        deduction = Decimal("0")

        if taxable_income <= TaxRules2026.EMPLOYEE_DEDUCTION_FIRST_THRESHOLD:
            deduction = TaxRules2026.EMPLOYEE_DEDUCTION_FIRST_AMOUNT

        elif taxable_income <= TaxRules2026.EMPLOYEE_DEDUCTION_SECOND_THRESHOLD:
            deduction = (
                TaxRules2026.EMPLOYEE_DEDUCTION_SECOND_BASE
                + TaxRules2026.EMPLOYEE_DEDUCTION_SECOND_VARIABLE
                * (
                    (
                        TaxRules2026.EMPLOYEE_DEDUCTION_SECOND_THRESHOLD
                        - taxable_income
                    )
                    / TaxRules2026.EMPLOYEE_DEDUCTION_SECOND_DENOMINATOR
                )
            )

        elif taxable_income <= TaxRules2026.EMPLOYEE_DEDUCTION_THIRD_THRESHOLD:
            deduction = (
                TaxRules2026.EMPLOYEE_DEDUCTION_THIRD_BASE
                * (
                    (
                        TaxRules2026.EMPLOYEE_DEDUCTION_THIRD_THRESHOLD
                        - taxable_income
                    )
                    / TaxRules2026.EMPLOYEE_DEDUCTION_THIRD_DENOMINATOR
                )
            )

        if (
            taxable_income
            > TaxRules2026.EMPLOYEE_DEDUCTION_BONUS_LOWER_BOUND
            and taxable_income
            <= TaxRules2026.EMPLOYEE_DEDUCTION_BONUS_UPPER_BOUND
        ):
            deduction += TaxRules2026.EMPLOYEE_DEDUCTION_BONUS_AMOUNT

        return deduction