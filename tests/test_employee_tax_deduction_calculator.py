from decimal import Decimal

from src.services import EmployeeTaxDeductionCalculator


def test_deduction_is_zero_for_zero_income() -> None:
    calculator = EmployeeTaxDeductionCalculator()

    result = calculator.calculate(Decimal("0"))

    assert result == Decimal("0")


def test_deduction_first_band() -> None:
    calculator = EmployeeTaxDeductionCalculator()

    result = calculator.calculate(Decimal("12000"))

    assert result == Decimal("1955")


def test_deduction_second_band() -> None:
    calculator = EmployeeTaxDeductionCalculator()

    income = Decimal("20000")

    result = calculator.calculate(income)

    expected = (
        Decimal("1910")
        + Decimal("1190")
        * ((Decimal("28000") - income) / Decimal("13000"))
    )

    assert result == expected


def test_deduction_third_band() -> None:
    calculator = EmployeeTaxDeductionCalculator()

    income = Decimal("40000")

    result = calculator.calculate(income)

    expected = (
        Decimal("1910")
        * ((Decimal("50000") - income) / Decimal("22000"))
    )

    assert result == expected


def test_additional_65_euro_deduction() -> None:
    calculator = EmployeeTaxDeductionCalculator()

    income = Decimal("30000")

    result = calculator.calculate(income)

    expected = (
        Decimal("1910")
        * ((Decimal("50000") - income) / Decimal("22000"))
        + Decimal("65")
    )

    assert result == expected


def test_deduction_is_zero_above_50000() -> None:
    calculator = EmployeeTaxDeductionCalculator()

    result = calculator.calculate(Decimal("60000"))

    assert result == Decimal("0")

def test_additional_65_euro_deduction_between_25000_and_28000() -> None:
    calculator = EmployeeTaxDeductionCalculator()

    income = Decimal("26000")

    result = calculator.calculate(income)

    expected = (
        Decimal("1910")
        + Decimal("1190")
        * ((Decimal("28000") - income) / Decimal("13000"))
        + Decimal("65")
    )

    assert result == expected        