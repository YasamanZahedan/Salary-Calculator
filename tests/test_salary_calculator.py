from decimal import Decimal

from src.models import SalaryInput
from src.services import SalaryCalculator


def test_salary_calculator_returns_positive_net_salary() -> None:
    calculator = SalaryCalculator()

    salary_input = SalaryInput(
        annual_gross_salary=Decimal("35000"),
        salary_payments=13,
    )

    result = calculator.calculate(salary_input)

    assert result.gross_salary == Decimal("35000")
    assert result.social_security > Decimal("0")
    assert result.taxable_income < result.gross_salary
    assert result.gross_irpef > Decimal("0")
    assert result.net_irpef < result.gross_irpef

    assert (
        Decimal("0")
        < result.annual_net_salary
        < result.gross_salary
    )


def test_monthly_values_are_derived_from_annual_net() -> None:
    calculator = SalaryCalculator()

    salary_input = SalaryInput(
        annual_gross_salary=Decimal("35000"),
        salary_payments=13,
    )

    result = calculator.calculate(salary_input)

    assert (
        result.average_monthly_net
        == result.annual_net_salary / Decimal("12")
    )

    assert (
        result.net_per_salary_payment
        == result.annual_net_salary / Decimal("13")
    )