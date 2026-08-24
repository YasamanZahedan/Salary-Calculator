from decimal import Decimal

from src.services import SocialSecurityCalculator


def test_standard_employee_inps_contribution() -> None:
    calculator = SocialSecurityCalculator()

    contribution = calculator.calculate(
        Decimal("35000")
    )

    assert contribution == Decimal("3216.5000")


def test_additional_one_percent_is_not_applied_at_threshold() -> None:
    calculator = SocialSecurityCalculator()

    contribution = calculator.calculate(
        Decimal("56224")
    )

    expected = Decimal("56224") * Decimal("0.0919")

    assert contribution == expected


def test_additional_one_percent_is_applied_above_threshold() -> None:
    calculator = SocialSecurityCalculator()

    contribution = calculator.calculate(
        Decimal("60000")
    )

    standard = Decimal("60000") * Decimal("0.0919")

    additional = (
        Decimal("60000") - Decimal("56224")
    ) * Decimal("0.01")

    expected = standard + additional

    assert contribution == expected


def test_zero_salary_has_zero_contribution() -> None:
    calculator = SocialSecurityCalculator()

    contribution = calculator.calculate(
        Decimal("0")
    )

    assert contribution == Decimal("0")    