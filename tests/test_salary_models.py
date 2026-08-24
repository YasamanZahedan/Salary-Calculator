from decimal import Decimal

from src.models import SalaryInput


def test_salary_input_uses_thirteen_payments_by_default() -> None:
    salary_input = SalaryInput(
        annual_gross_salary=Decimal("35000")
    )

    assert salary_input.annual_gross_salary == Decimal("35000")
    assert salary_input.salary_payments == 13