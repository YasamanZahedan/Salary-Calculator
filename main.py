from decimal import Decimal

from src.models import SalaryInput
from src.services import SalaryCalculator


def main() -> None:
    salary_input = SalaryInput(
        annual_gross_salary=Decimal("35000"),
        salary_payments=13,
    )

    calculator = SalaryCalculator()

    result = calculator.calculate(salary_input)

    print("Jet HR Salary Calculator")
    print("------------------------")
    print(f"RAL: €{result.gross_salary:.2f}")
    print(f"Employee INPS: €{result.social_security:.2f}")
    print(f"Taxable income: €{result.taxable_income:.2f}")
    print(f"Gross IRPEF: €{result.gross_irpef:.2f}")
    print(
        "Employee tax deduction: "
        f"€{result.employee_tax_deduction:.2f}"
    )
    print(
        "Additional tax relief: "
        f"€{result.additional_tax_relief:.2f}"
    )
    print(f"Net IRPEF: €{result.net_irpef:.2f}")
    print(f"Lombardy tax: €{result.regional_tax:.2f}")
    print(f"Milan tax: €{result.municipal_tax:.2f}")
    print("------------------------")
    print(f"Annual net: €{result.annual_net_salary:.2f}")
    print(
        f"Average monthly net: "
        f"€{result.average_monthly_net:.2f}"
    )
    print(
        f"Net per salary payment (13): "
        f"€{result.net_per_salary_payment:.2f}"
    )


if __name__ == "__main__":
    main()