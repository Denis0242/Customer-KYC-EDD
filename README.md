# Financial Crime Customer Risk & KYC/EDD Analytics

**Financial Crime Analytics Portfolio Project**

An end-to-end KYC/EDD analytics project using **Python, SQL, Tableau,
and Streamlit** to assess customer risk, KYC completeness, Enhanced Due
Diligence requirements, PEP/sanctions/adverse-media exposure,
beneficial-ownership context, and remediation priorities.

> **Portfolio scope:** This project uses synthetic data created for
> analytical and educational purposes. Risk scores, EDD indicators,
> review decisions, and prioritization logic are illustrative and do not
> represent any financial institution's production KYC policy.

------------------------------------------------------------------------

## Project Overview

Effective KYC and Enhanced Due Diligence programs require more than
collecting customer information. Compliance teams must identify
incomplete due-diligence records, recognize elevated customer-risk
indicators, prioritize remediation, and determine which customers
require enhanced review.

This project analyzes **1,200 synthetic customers** using an
analytics-ready customer-risk layer that combines customer profile
information, KYC controls, PEP exposure, sanctions-screening indicators,
adverse media, customer risk scoring, EDD requirements, and primary risk
drivers.

The wider project data model also includes **897 beneficial-owner
records** and **300 KYC/EDD review cases**, supporting customer
due-diligence, beneficial-ownership analysis, remediation monitoring,
and review prioritization.

------------------------------------------------------------------------

## Business & Compliance Problem

The project addresses practical KYC/EDD questions such as:

-   Which customers present elevated financial-crime risk?
-   Which customers require Enhanced Due Diligence?
-   Which KYC controls remain incomplete?
-   Where are PEP, sanctions, and adverse-media indicators concentrated?
-   What are the main drivers of EDD requirements?
-   Which customers should be prioritized for remediation or enhanced
    review?
-   How can customer risk and KYC completeness be summarized for
    compliance decision support?
-   How can review teams rank customers and cases by risk and urgency?

The objective is to support **risk-based KYC/EDD review and
prioritization**, not to automate customer acceptance or regulatory
decisions.

------------------------------------------------------------------------

## Dataset

  ----------------------------------------------------------------------------------
  Dataset                                                 Rows Purpose
  ------------------------------- ---------------------------- ---------------------
  `customers_kyc.csv`                                    1,200 Customer profile, KYC
                                                               controls,
                                                               due-diligence and
                                                               risk attributes

  `beneficial_owners.csv`                                  897 Ownership structure
                                                               and UBO-related
                                                               analysis

  `kyc_review_cases.csv`                                   300 KYC/EDD review,
                                                               remediation and case
                                                               monitoring

  `customer_risk_analytics.csv`                          1,200 Analytics-ready
                                                               customer risk and
                                                               prioritization layer
  ----------------------------------------------------------------------------------

A detailed field-level reference is available in
[`docs/data_dictionary.md`](docs/data_dictionary.md).

------------------------------------------------------------------------

## Exploratory Data Analysis & Data Quality

The analytical workflow includes practical EDA and data-quality
validation across customer-risk and KYC/EDD attributes.

Key activities include:

-   Dataset and schema review
-   Missing-value analysis
-   Duplicate validation
-   Datatype review
-   KYC completeness analysis
-   Customer-risk distribution analysis
-   EDD population analysis
-   PEP, sanctions, and adverse-media indicator review
-   Range and categorical validation
-   Summary statistics
-   Business-rule validation

Missing or unusual values are evaluated according to their KYC/EDD
business meaning rather than being automatically removed.

------------------------------------------------------------------------

## Feature Engineering & Analytical Fields

The project uses customer-level features and derived analytics to
support risk segmentation and review prioritization.

Important fields include:

-   `risk_score` --- customer risk measure
-   `risk_level` --- customer risk segmentation
-   `kyc_complete_pct` --- KYC completion measure
-   `edd_required` --- EDD requirement indicator
-   `primary_risk_driver` --- principal driver of customer risk
-   `pep_flag` --- PEP indicator
-   `sanctions_hit` --- sanctions-screening indicator
-   `adverse_media_flag` --- adverse-media indicator
-   `ubo_complete` --- beneficial-ownership completion control
-   `source_of_wealth_verified` --- source-of-wealth verification
    control

The notebook workflow also demonstrates simple, explainable feature
engineering for KYC gaps, completion status, EDD attention, case aging,
and aged-case prioritization.

------------------------------------------------------------------------

## KYC / EDD Analysis

The project evaluates four connected areas.

**Customer risk:** customer-level risk scores and risk segmentation.

**KYC completeness:** ID, address, tax, beneficial ownership, and
source-of-wealth controls.

**Enhanced Due Diligence:** identification of customers requiring deeper
review based on their risk profile and risk indicators.

**Review prioritization:** ranking customers and KYC/EDD cases so
higher-risk and unresolved records receive attention first.

------------------------------------------------------------------------

## SQL Analysis

The SQL layer supports customer-risk, KYC/EDD, and remediation analysis,
including customer segmentation, KYC completeness, EDD-required
populations, PEP/sanctions/adverse-media exposure, review-case
monitoring, and prioritization.

See [`sql/`](sql/) for the project queries.

------------------------------------------------------------------------

## Key Portfolio KPIs

The following figures are verified from the current
`customer_risk_analytics.csv` dataset:

  KPI                              Result
  --------------------- -----------------
  Total Customers               **1,200**
  High/Critical Risk        **13 (1.1%)**
  EDD Required            **172 (14.3%)**
  Fully KYC Complete      **684 (57.0%)**
  Incomplete KYC                  **516**
  PEP Customers                    **54**
  Sanctions Hits                   **13**
  Adverse-Media Flags             **111**

------------------------------------------------------------------------

## Key Findings

-   The portfolio contains **1,200 customers**, with **13** classified
    as High/Critical risk.

-   **172 customers (14.3%)** require Enhanced Due Diligence.

-   **684 customers (57.0%)** have 100% KYC completion, leaving **516**
    with at least one incomplete KYC control.

-   The current portfolio contains **54 PEP indicators**, **13 sanctions
    hits**, and **111 adverse-media flags**.

-   The risk distribution is concentrated in lower-risk customers: **916
    Low**, **271 Moderate**, **13 High**, and **0 Critical**.

-   Leading EDD drivers in the current analytics layer include **Adverse
    Media (105)**, **PEP (54)**, **Sanctions (13)**.

These findings support targeted remediation and enhanced review rather
than treating the entire customer population as equally risky.

------------------------------------------------------------------------

## Streamlit Decision-Support Application

The Streamlit application provides portfolio-level and customer-level
KYC/EDD decision support.

Users can filter by:

-   Risk level
-   Customer type
-   Country

The application recalculates customer count, High/Critical population,
EDD-required customers, KYC completion, PEP exposure, sanctions hits,
and adverse-media indicators.

### Portfolio Decision Logic

The application summarizes the selected population as:

-   **Generally Stable**
-   **Targeted Review Recommended**
-   **Enhanced Review Required**

This status is based on project-defined signals such as elevated-risk
concentration, EDD requirements, sanctions hits, and incomplete KYC.

### Customer-Level Decision Support

For an individual customer, the application displays:

-   Risk score and risk level
-   KYC completion
-   EDD requirement
-   Primary risk driver
-   Control-review results
-   PEP / sanctions / adverse-media indicators
-   Beneficial-ownership completeness
-   Source-of-wealth verification

It then presents an explainable portfolio decision such as **Sanctions
Review**, **EDD Required**, **KYC Remediation Required**, **Enhanced
Review**, or **Standard KYC Approval / Routine Monitoring**.

------------------------------------------------------------------------

## Tableau Dashboard

The executive dashboard presents:

1.  Customer Risk Mix
2.  KYC Completeness
3.  Top EDD Drivers
4.  Review Case Aging
5.  Top High-Risk Countries
6.  KYC Case Status

### Dashboard Preview

![Financial Crime Customer Risk & KYC/EDD Analytics Dashboard](images/02_executive_dashboard.png)

> **Dashboard status:** The Executive Dashboard is synchronized to the current portfolio metrics used in this project. Customer-level KPIs are verified against `customer_risk_analytics.csv`; the dashboard also presents the project’s 300-case KYC/EDD review layer for case-status and aging analysis.

------------------------------------------------------------------------

## Analytical Workflow

``` text
Customer Profile
        ↓
KYC Control Validation
        ↓
Beneficial Ownership Review
        ↓
Customer Risk Assessment
        ↓
EDA + Feature Engineering
        ↓
EDD / Remediation Prioritization
        ↓
SQL + Python Analysis
        ↓
Tableau + Streamlit Reporting
        ↓
KYC / EDD Decision Support
```

------------------------------------------------------------------------

## Tools & Technologies

  -----------------------------------------------------------------------
  Tool                                Use
  ----------------------------------- -----------------------------------
  **Python / Pandas**                 EDA, validation, feature
                                      engineering and customer-risk
                                      analysis

  **SQL**                             KYC, EDD, risk, exposure and
                                      remediation analysis

  **Tableau**                         Executive KYC/EDD dashboard

  **Streamlit**                       Interactive customer review and
                                      decision support

  **Jupyter Notebook**                Reproducible analytical workflow

  **Git / GitHub**                    Version control and portfolio
                                      documentation
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Repository Structure

``` text
Customer-KYC-EDD/
├── app/             # Streamlit application
├── data/            # Raw and processed synthetic datasets
├── docs/            # Data dictionary and documentation
├── images/          # Dashboard images
├── notebooks/       # Python EDA and feature engineering
├── sql/             # KYC/EDD analytics queries
├── tableau/         # Tableau workbook
├── .gitignore
├── .python-version
├── pyproject.toml
├── requirements.txt
├── uv.lock
└── README.md
```


------------------------------------------------------------------------

## How to Run

Clone the repository and install dependencies:

``` bash
git clone https://github.com/Denis0242/Customer-KYC-EDD.git
cd Customer-KYC-EDD
pip install -r requirements.txt
```

Run the Streamlit application:

``` bash
streamlit run app/streamlit_app.py
```

------------------------------------------------------------------------

## Skills Demonstrated

### AML / KYC / Financial Crime

-   Know Your Customer (KYC)
-   Customer Due Diligence (CDD)
-   Enhanced Due Diligence (EDD)
-   Customer Risk Assessment
-   KYC Remediation
-   PEP Review
-   Sanctions Screening Analysis
-   Adverse-Media Analysis
-   Beneficial Ownership / UBO Review
-   Source-of-Wealth Controls
-   Risk-Based Review Prioritization

### Data & Analytics

-   Exploratory Data Analysis
-   Data Quality Validation
-   Feature Engineering
-   SQL Analysis
-   Python / Pandas
-   Customer Risk Segmentation
-   KPI Development
-   Business-Rule Validation
-   Decision-Support Analytics

### Reporting & Visualization

-   Tableau
-   Streamlit
-   Customer 360 Reporting
-   Executive KPI Reporting
-   Interactive Analytics
-   Data Storytelling

------------------------------------------------------------------------

## Disclaimer

This project uses **synthetic data** created for educational and
portfolio purposes. No real customer, beneficial owner, account,
financial institution, or confidential compliance data is included.

Risk scores, KYC controls, EDD requirements, PEP/sanctions/adverse-media
indicators, review priorities, and decision logic are illustrative. They
demonstrate KYC/EDD and financial-crime analytics workflows and should
not be interpreted as actual bank policy, customer acceptance criteria,
sanctions adjudication, or regulatory guidance.
