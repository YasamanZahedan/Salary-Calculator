from decimal import Decimal

from src.services import AdditionalTaxReliefCalculator


def test_relief_is_1000_between_20000_and_32000() -> None:
    calculator = AdditionalTaxReliefCalculator()

    result = calculator.calculate(Decimal("25000"))

    assert result == Decimal("1000")


def test_relief_tapers_between_32000_and_40000() -> None:
    calculator = AdditionalTaxReliefCalculator()

    result = calculator.calculate(Decimal("36000"))

    assert result == Decimal("500")


def test_relief_is_zero_above_40000() -> None:
    calculator = AdditionalTaxReliefCalculator()

    result = calculator.calculate(Decimal("45000"))

    assert result == Decimal("0")