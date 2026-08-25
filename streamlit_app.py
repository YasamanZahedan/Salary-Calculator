from decimal import Decimal

import streamlit as st

from src.models import SalaryInput
from src.services import SalaryCalculator


st.set_page_config(
    page_title="Italian Salary Calculator",
    page_icon="💶",
    layout="centered",
)


def format_euro(value: Decimal) -> str:
    return f"€{value:,.2f}"


st.title("Italian Salary Calculator")

st.caption(
    "Estimate your 2026 net salary from your annual gross salary (RAL). "
    "Standard permanent employee resident in Milan."
)

st.divider()

st.subheader("Salary details")

gross_salary = st.number_input(
    "Annual gross salary (RAL)",
    min_value=0.0,
    value=35000.0,
    step=1000.0,
    format="%.2f",
)

salary_payments = st.selectbox(
    "Number of salary payments",
    options=[12, 13, 14],
    index=1,
)

calculate_clicked = st.button(
    "Calculate",
    type="primary",
    use_container_width=True,
)

if calculate_clicked:
    if gross_salary <= 0:
        st.error(
            "Please enter an annual gross salary greater than €0."
        )

    else:
        salary_input = SalaryInput(
            annual_gross_salary=Decimal(str(gross_salary)),
            salary_payments=salary_payments,
        )

        calculator = SalaryCalculator()

        result = calculator.calculate(
            salary_input
        )

        total_deductions = (
            result.gross_salary
            - result.annual_net_salary
        )

        effective_deduction_rate = (
            total_deductions
            / result.gross_salary
            * Decimal("100")
        )

        st.divider()

        st.subheader("Estimated net salary")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Annual net salary",
                format_euro(
                    result.annual_net_salary
                ),
            )

        with col2:
            st.metric(
                "Average monthly net",
                format_euro(
                    result.average_monthly_net
                ),
            )

        with col3:
            st.metric(
                "Effective deductions",
                f"{effective_deduction_rate:.1f}%",
            )

        st.metric(
            f"Net per salary payment "
            f"({salary_payments} payments)",
            format_euro(
                result.net_per_salary_payment
            ),
        )

        st.divider()

        st.subheader("From gross to net")

        st.write(
            f"**Gross annual salary:** "
            f"{format_euro(result.gross_salary)}"
        )

        st.write(
            f"**Employee social security (INPS):** "
            f"-{format_euro(result.social_security)}"
        )

        st.write(
            f"**IRPEF taxable income:** "
            f"{format_euro(result.taxable_income)}"
        )

        st.write(
            f"**Gross IRPEF:** "
            f"-{format_euro(result.gross_irpef)}"
        )

        st.write(
            f"**Employee tax deduction:** "
            f"+{format_euro(result.employee_tax_deduction)}"
        )

        st.write(
            f"**Additional employment tax relief:** "
            f"+{format_euro(result.additional_tax_relief)}"
        )

        st.write(
            f"**Net IRPEF:** "
            f"-{format_euro(result.net_irpef)}"
        )

        st.write(
            f"**Lombardy regional surcharge:** "
            f"-{format_euro(result.regional_tax)}"
        )

        st.write(
            f"**Milan municipal surcharge:** "
            f"-{format_euro(result.municipal_tax)}"
        )

        st.divider()

        st.success(
            f"Estimated annual net salary: "
            f"{format_euro(result.annual_net_salary)}"
        )

st.divider()

with st.expander("Assumptions and methodology"):
    st.markdown(
        """
This prototype estimates the annual gross-to-net salary for a simplified
standard Italian employment scenario.

**Assumptions**

- Tax year: 2026
- Permanent private-sector employee
- Employee works for the full calendar year
- Resident in Milan, Lombardy
- No dependants
- No additional income
- No special tax regimes or tax benefits
- No deductible expenses
- Standard employee social-security contribution assumptions
- TFR is excluded
- Bonuses, fringe benefits and overtime are excluded
- Monthly values are estimates rather than an exact payroll simulation
- The user can select 12, 13 or 14 salary payments

**Calculation flow**

RAL → employee social security → IRPEF taxable income → gross IRPEF →
employee deductions → regional surcharge → municipal surcharge →
net annual salary
"""
    )

st.caption(
    "Prototype for estimation purposes only. "
    "It is not an official payroll calculation."
)