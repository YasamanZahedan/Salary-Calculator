from decimal import Decimal

from src.services import RegionalTaxCalculator


def test_regional_tax_is_zero_for_zero_income() -> None:
    calculator = RegionalTaxCalculator()

    result = calculator.calculate(Decimal("0"))

    assert result == Decimal("0")


def test_regional_tax_first_band() -> None:
    calculator = RegionalTaxCalculator()

    result = calculator.calculate(Decimal("10000"))

    expected = Decimal("10000") * Decimal("0.0123")

    assert result == expected


def test_regional_tax_second_band() -> None:
    calculator = RegionalTaxCalculator()

    result = calculator.calculate(Decimal("20000"))

    expected = (
        Decimal("15000") * Decimal("0.0123")
        + Decimal("5000") * Decimal("0.0158")
    )

    assert result == expected


def test_regional_tax_third_band() -> None:
    calculator = RegionalTaxCalculator()

    result = calculator.calculate(Decimal("35000"))

    expected = (
        Decimal("15000") * Decimal("0.0123")
        + Decimal("13000") * Decimal("0.0158")
        + Decimal("7000") * Decimal("0.0172")
    )

    assert result == expected


def test_regional_tax_fourth_band() -> None:
    calculator = RegionalTaxCalculator()

    result = calculator.calculate(Decimal("60000"))

    expected = (
        Decimal("15000") * Decimal("0.0123")
        + Decimal("13000") * Decimal("0.0158")
        + Decimal("22000") * Decimal("0.0172")
        + Decimal("10000") * Decimal("0.0173")
    )

    assert result == expected