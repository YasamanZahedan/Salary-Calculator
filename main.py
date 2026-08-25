from decimal import Decimal

from src.models import SalaryInput
from src.services import (
    EmployeeTaxDeductionCalculator,
    IrpefCalculator,
    SocialSecurityCalculator,
)


def main() -> None:
    salary_input = SalaryInput(
        annual_gross_salary=Decimal("35000")
    )

    social_security_calculator = SocialSecurityCalculator()
    irpef_calculator = IrpefCalculator()
    deduction_calculator = EmployeeTaxDeductionCalculator()

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

    print("Jet HR Salary Calculator")
    print(f"RAL: €{salary_input.annual_gross_salary}")
    print(f"Employee INPS: €{social_security}")
    print(f"IRPEF taxable income: €{taxable_income}")
    print(f"Gross IRPEF: €{gross_irpef}")
    print(f"Employee tax deduction: €{employee_tax_deduction}")
    print(f"Net IRPEF: €{net_irpef}")


if __name__ == "__main__":
    main()