from decimal import Decimal


class TaxRules2026:
    EMPLOYEE_INPS_RATE = Decimal("0.0919")
    ADDITIONAL_INPS_RATE = Decimal("0.01")
    ADDITIONAL_INPS_THRESHOLD = Decimal("56224")

    IRPEF_FIRST_THRESHOLD = Decimal("28000")
    IRPEF_SECOND_THRESHOLD = Decimal("50000")

    IRPEF_FIRST_RATE = Decimal("0.23")
    IRPEF_SECOND_RATE = Decimal("0.33")
    IRPEF_THIRD_RATE = Decimal("0.43")