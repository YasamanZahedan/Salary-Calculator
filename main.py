from decimal import Decimal

from src.models import SalaryInput
from src.services import (
    EmployeeTaxDeductionCalculator,
    IrpefCalculator,
    MunicipalTaxCalculator,
    RegionalTaxCalculator,
    SocialSecurityCalculator,
)


def main() -> None:
    salary_input = SalaryInput(
        annual_gross_salary=Decimal("35000")
    )

    social_security_calculator = SocialSecurityCalculator()
    irpef_calculator = IrpefCalculator()
    deduction_calculator = EmployeeTaxDeductionCalculator()
    regional_tax_calculator = RegionalTaxCalculator()
    municipal_tax_calculator = MunicipalTaxCalculator()

    social_security = social_security_calculator.calculate(
        salary_input.annual_gross_salary
    )

    taxable_income = (
        salary_input.annual_gross_salary
        - social_security
    )

    gross_irpef = irpef_calculator.calculate(
        taxable_income
    )

    employee_tax_deduction = deduction_calculator.calculate(
        taxable_income
    )

    net_irpef = max(
        Decimal("0"),
        gross_irpef - employee_tax_deduction,
    )

    regional_tax = regional_tax_calculator.calculate(
        taxable_income
    )

    municipal_tax = municipal_tax_calculator.calculate(
        taxable_income
    )

    annual_net_salary = (
        salary_input.annual_gross_salary
        - social_security
        - net_irpef
        - regional_tax
        - municipal_tax
    )

    print("Jet HR Salary Calculator")
    print(f"RAL: €{salary_input.annual_gross_salary}")
    print(f"Employee INPS: €{social_security}")
    print(f"IRPEF taxable income: €{taxable_income}")
    print(f"Gross IRPEF: €{gross_irpef}")
    print(f"Employee tax deduction: €{employee_tax_deduction}")
    print(f"Net IRPEF: €{net_irpef}")
    print(f"Lombardy regional tax: €{regional_tax}")
    print(f"Milan municipal tax: €{municipal_tax}")
    print(f"Annual net salary: €{annual_net_salary}")


if __name__ == "__main__":
    main()