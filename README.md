# Italian Salary Calculator — 2026

A simplified gross-to-net salary calculator for a permanent private-sector employee resident in Milan, Italy.

The application receives an annual gross salary (**RAL — Retribuzione Annua Lorda**) and estimates:

* annual net salary;
* average monthly net salary;
* net amount per salary payment;
* employee social-security contributions;
* national IRPEF;
* employee tax deductions;
* Lombardy regional IRPEF surcharge;
* Milan municipal IRPEF surcharge.

The project was built as a prototype for the Jet HR AI Product Builder technical task.

## Live Demo

**Streamlit app:** https://yasamanzahedan-salary-calculator-streamlit-app-xtefgf.streamlit.app/

## How it works

The simplified calculation flow is:

```text
Annual Gross Salary (RAL)
        ↓
Employee Social Security (INPS)
        ↓
IRPEF Taxable Income
        ↓
Gross National IRPEF
        ↓
Employee Tax Deductions
        ↓
Net IRPEF
        ↓
Lombardy Regional Surcharge
        ↓
Milan Municipal Surcharge
        ↓
Estimated Annual Net Salary
```

The application also calculates:

```text
Average monthly net = annual net / 12
```

and:

```text
Net per salary payment = annual net / selected payments
```

The user can select 12, 13, or 14 salary payments.

## Scope and assumptions

This prototype intentionally models a simple and standard employment case rather than attempting to reproduce a complete Italian payroll system.

The model assumes:

* tax year 2026;
* permanent private-sector employee;
* employee works for the entire calendar year;
* tax residence in Milan, Lombardy;
* no dependants;
* no additional sources of income;
* no special tax regimes;
* no impatriate regime;
* no additional personal deductions;
* no supplementary pension contributions;
* no bonuses subject to special taxation;
* no fringe benefits;
* no overtime;
* no welfare benefits;
* TFR is excluded from take-home salary;
* ordinary employee social-security treatment;
* monthly values are estimates rather than a month-by-month payslip simulation.

The selected number of salary payments affects only the estimated amount per payment. It does not change annual tax liability or annual net salary.

## Tax methodology

### Employee social-security contributions

The prototype assumes an ordinary employee contribution rate of:

```text
9.19%
```

An additional employee contribution of:

```text
1%
```

is applied to remuneration exceeding the applicable 2026 pensionable-income threshold used by the model:

```text
€56,224
```

The implementation is intentionally simplified and does not attempt to reproduce all INPS contribution regimes or monthly contribution reconciliation.

### National IRPEF

The calculator applies progressive 2026 national IRPEF brackets:

| Taxable income  | Rate |
| --------------- | ---: |
| Up to €28,000   |  23% |
| €28,000–€50,000 |  33% |
| Above €50,000   |  43% |

Rates are applied progressively rather than applying a single marginal rate to the entire taxable income.

### Employee tax deduction

The standard employment-income deduction is calculated using the income-dependent formulas defined by Article 13 of the Italian TUIR.

The model also includes the additional €65 deduction applicable in the relevant €25,000–€35,000 income range.

### Additional employment tax relief

The prototype models the additional employment tax deduction applicable to the €20,000–€40,000 income range.

For the purpose of this prototype, taxable employment income is used as a simplified proxy when determining eligibility.

Lower-income relief and interactions with other income or tax benefits are not modeled comprehensively.

### Lombardy regional surcharge

The prototype applies the progressive Lombardy regional IRPEF surcharge:

| Taxable income  |  Rate |
| --------------- | ----: |
| Up to €15,000   | 1.23% |
| €15,000–€28,000 | 1.58% |
| €28,000–€50,000 | 1.72% |
| Above €50,000   | 1.73% |

### Milan municipal surcharge

The model assumes tax residence in Milan.

The municipal IRPEF surcharge is:

```text
0.8%
```

with an exemption for taxable income not exceeding:

```text
€23,000
```

If taxable income exceeds the exemption threshold, the simplified model applies the municipal rate to the full taxable income.

## Architecture

The calculation engine is deliberately separated from the Streamlit user interface.

```text
Streamlit UI
     ↓
SalaryInput
     ↓
SalaryCalculator
     │
     ├── SocialSecurityCalculator
     ├── IrpefCalculator
     ├── EmployeeTaxDeductionCalculator
     ├── AdditionalTaxReliefCalculator
     ├── RegionalTaxCalculator
     └── MunicipalTaxCalculator
     ↓
SalaryResult
```

This means the domain logic is not coupled to Streamlit and could later be reused in an API, another frontend, or a payroll workflow.

Tax parameters are also separated from calculation logic in the `config` package so that regulatory values can be versioned and maintained independently.

## Project structure

```text
jet-hr-salary-calculator/
│
├── src/
│   ├── config/
│   │   └── tax_rules_2026.py
│   │
│   ├── models/
│   │   └── salary.py
│   │
│   └── services/
│       ├── social_security_calculator.py
│       ├── irpef_calculator.py
│       ├── employee_tax_deduction_calculator.py
│       ├── additional_tax_relief_calculator.py
│       ├── regional_tax_calculator.py
│       ├── municipal_tax_calculator.py
│       └── salary_calculator.py
│
├── tests/
├── main.py
├── streamlit_app.py
├── requirements.txt
└── README.md
```

## Running locally

Clone the repository and create a virtual environment.

On Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Run the automated tests:

```powershell
python -m pytest
```

Run the web application:

```powershell
streamlit run streamlit_app.py
```

## Testing strategy

The calculation engine is tested independently from the UI.

Tests focus particularly on regulatory boundaries such as:

```text
€15,000
€20,000
€23,000
€25,000
€28,000
€32,000
€35,000
€40,000
€50,000
€56,224
```

This is intentional because progressive tax systems are especially sensitive to errors around thresholds and transitions between brackets.

## Sources

The prototype prioritizes official institutional sources.

### National taxation

* Italian Ministry of Economy and Finance — TUIR, Article 11: national IRPEF rules.
* Italian Ministry of Economy and Finance — TUIR, Article 13: employment-income deductions.
* Italian Revenue Agency — employment income, tax relief and additional employee deductions.

### Social security

* INPS — employee pension contribution rules and 2026 pensionable-income thresholds.

### Regional taxation

* Regione Lombardia — regional IRPEF surcharge rates.
* Consiglio Regionale della Lombardia — regional legislation defining the applicable brackets and rates.

### Municipal taxation

* Comune di Milano — municipal IRPEF surcharge rate and exemption threshold.

## Limitations

This application is an estimation prototype, not payroll software.

A production payroll implementation would require additional handling for matters including:

* exact INPS classification and contribution regime;
* CCNL-specific rules;
* monthly payroll withholding and year-end reconciliation;
* partial-year employment;
* other taxable income;
* dependants and personal deductions;
* special tax regimes;
* bonuses and substitute taxes;
* fringe benefits;
* supplementary pension contributions;
* TFR;
* municipality and region selection;
* changes to legislation over time.

Because of these simplifications, the result should be interpreted as an estimate rather than an official payslip calculation.

## Possible next iterations

A production-oriented version could add municipality and region selection, versioned rules by tax year, additional employee profiles, employer total-cost calculation, automated regulatory regression cases, and comparison against known payroll examples.

## Disclaimer

This project is provided for demonstration and estimation purposes only. It does not constitute tax, payroll, accounting, or legal advice.
