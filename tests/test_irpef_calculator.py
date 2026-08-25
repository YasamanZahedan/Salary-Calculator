from decimal import Decimal

from src.services import IrpefCalculator


def test_irpef_is_zero_for_zero_income() -> None:
    calculator = IrpefCalculator()

    result = calculator.calculate(Decimal("0"))

    assert result == Decimal("0")


def test_irpef_first_bracket() -> None:
    calculator = IrpefCalculator()

    result = calculator.calculate(Decimal("20000"))

    expected = Decimal("20000") * Decimal("0.23")

    assert result == expected


def test_irpef_at_first_threshold() -> None:
    calculator = IrpefCalculator()

    result = calculator.calculate(Decimal("28000"))

    expected = Decimal("28000") * Decimal("0.23")

    assert result == expected


def test_irpef_second_bracket() -> None:
    calculator = IrpefCalculator()

    result = calculator.calculate(Decimal("30000"))

    expected = (
        Decimal("28000") * Decimal("0.23")
        + Decimal("2000") * Decimal("0.33")
    )

    assert result == expected


def test_irpef_third_bracket() -> None:
    calculator = IrpefCalculator()

    result = calculator.calculate(Decimal("60000"))

    expected = (
        Decimal("28000") * Decimal("0.23")
        + Decimal("22000") * Decimal("0.33")
        + Decimal("10000") * Decimal("0.43")
    )

    assert result == expected