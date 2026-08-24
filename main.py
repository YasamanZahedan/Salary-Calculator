from decimal import Decimal

from src.models import SalaryInput


def main() -> None:
    salary_input = SalaryInput(
        annual_gross_salary=Decimal("35000")
    )

    print("Jet HR Salary Calculator")
    print(f"RAL: €{salary_input.annual_gross_salary}")
    print(f"Salary payments: {salary_input.salary_payments}")


if __name__ == "__main__":
    main()