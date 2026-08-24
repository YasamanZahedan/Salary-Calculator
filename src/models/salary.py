from dataclasses import dataclass
from decimal import Decimal


@dataclass
class SalaryInput:
    annual_gross_salary: Decimal
    salary_payments: int = 13


@dataclass
class SalaryResult:
    gross_salary: Decimal
    social_security: Decimal
    taxable_income: Decimal
    gross_irpef: Decimal
    employee_tax_deduction: Decimal
    net_irpef: Decimal
    regional_tax: Decimal
    municipal_tax: Decimal
    annual_net_salary: Decimal
    average_monthly_net: Decimal
    net_per_salary_payment: Decimal