from decimal import Decimal

from src.models import SalaryInput
from src.services import SocialSecurityCalculator


def main() -> None:
    salary_input = SalaryInput(
        annual_gross_salary=Decimal("35000")
    )

    social_security_calculator = SocialSecurityCalculator()

    social_security = social_security_calculator.calculate(
        salary_input.annual_gross_salary
    )

    print("Jet HR Salary Calculator")
    print(f"RAL: €{salary_input.annual_gross_salary}")
    print(f"Employee INPS: €{social_security}")


if __name__ == "__main__":
    main()