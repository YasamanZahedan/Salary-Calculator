from decimal import Decimal

from src.models import SalaryInput, SalaryResult

from .additional_tax_relief_calculator import AdditionalTaxReliefCalculator
from .employee_tax_deduction_calculator import (
    EmployeeTaxDeductionCalculator,
)
from .irpef_calculator import IrpefCalculator
from .municipal_tax_calculator import MunicipalTaxCalculator
from .regional_tax_calculator import RegionalTaxCalculator
from .social_security_calculator import SocialSecurityCalculator


class SalaryCalculator:
    def __init__(self) -> None:
        self.social_security_calculator = SocialSecurityCalculator()
        self.irpef_calculator = IrpefCalculator()
        self.employee_deduction_calculator = (
            EmployeeTaxDeductionCalculator()
        )
        self.additional_relief_calculator = (
            AdditionalTaxReliefCalculator()
        )
        self.regional_tax_calculator = RegionalTaxCalculator()
        self.municipal_tax_calculator = MunicipalTaxCalculator()

    def calculate(self, salary_input: SalaryInput) -> SalaryResult:
        gross_salary = salary_input.annual_gross_salary

        social_security = (
            self.social_security_calculator.calculate(
                gross_salary
            )
        )

        taxable_income = gross_salary - social_security

        gross_irpef = self.irpef_calculator.calculate(
            taxable_income
        )

        employee_tax_deduction = (
            self.employee_deduction_calculator.calculate(
                taxable_income
            )
        )

        additional_tax_relief = (
            self.additional_relief_calculator.calculate(
                taxable_income
            )
        )

        net_irpef = max(
            Decimal("0"),
            gross_irpef
            - employee_tax_deduction
            - additional_tax_relief,
        )

        regional_tax = self.regional_tax_calculator.calculate(
            taxable_income
        )

        municipal_tax = (
            self.municipal_tax_calculator.calculate(
                taxable_income
            )
        )

        annual_net_salary = (
            gross_salary
            - social_security
            - net_irpef
            - regional_tax
            - municipal_tax
        )

        average_monthly_net = (
            annual_net_salary / Decimal("12")
        )

        net_per_salary_payment = (
            annual_net_salary
            / Decimal(str(salary_input.salary_payments))
        )

        return SalaryResult(
            gross_salary=gross_salary,
            social_security=social_security,
            taxable_income=taxable_income,
            gross_irpef=gross_irpef,
            employee_tax_deduction=employee_tax_deduction,
            additional_tax_relief=additional_tax_relief,
            net_irpef=net_irpef,
            regional_tax=regional_tax,
            municipal_tax=municipal_tax,
            annual_net_salary=annual_net_salary,
            average_monthly_net=average_monthly_net,
            net_per_salary_payment=net_per_salary_payment,
        )