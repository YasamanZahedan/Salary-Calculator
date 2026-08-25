from decimal import Decimal

from src.services import MunicipalTaxCalculator


def test_milan_tax_is_zero_below_exemption() -> None:
    calculator = MunicipalTaxCalculator()

    result = calculator.calculate(Decimal("20000"))

    assert result == Decimal("0")


def test_milan_tax_is_zero_at_exemption_threshold() -> None:
    calculator = MunicipalTaxCalculator()

    result = calculator.calculate(Decimal("23000"))

    assert result == Decimal("0")


def test_milan_tax_applies_above_exemption_threshold() -> None:
    calculator = MunicipalTaxCalculator()

    result = calculator.calculate(Decimal("25000"))

    expected = Decimal("25000") * Decimal("0.008")

    assert result == expected