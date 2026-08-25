from decimal import Decimal

from src.models import SalaryInput
from src.services import (
    SocialSecurityCalculator,
    IrpefCalculator,
)


def main() -> None:
    salary_input = SalaryInput(
        annual_gross_salary=Decimal("35000")
    )

    social_security_calculator = SocialSecurityCalculator()
    irpef_calculator = IrpefCalculator()

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

    print("Jet HR Salary Calculator")
    print(f"RAL: €{salary_input.annual_gross_salary}")
    print(f"Employee INPS: €{social_security}")
    print(f"IRPEF taxable income: €{taxable_income}")
    print(f"Gross IRPEF: €{gross_irpef}")


if __name__ == "__main__":
    main()