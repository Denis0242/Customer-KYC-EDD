# Data Dictionary

## Financial Crime Customer Risk & KYC/EDD Analytics

This data dictionary documents the customer KYC, beneficial-ownership, KYC review-case, and customer-risk analytics datasets used in this portfolio project. It distinguishes operational/source fields from derived analytical features so reviewers can clearly see the data model and feature-engineering components.

> **Portfolio note:** The datasets are structured for analytical demonstration. Definitions describe their use within this project and do not represent any specific financial institution's production data standards.

## Dataset Overview

| Dataset | Rows | Columns | Purpose |
|---|---:|---:|---|
| `beneficial_owners.csv` | 897 | 6 | Beneficial-ownership dataset used to analyze ownership structure and UBO-related risk. |
| `customers_kyc.csv` | 1,200 | 19 | Customer-level KYC dataset containing profile, due-diligence, and risk attributes. |
| `kyc_review_cases.csv` | 300 | 9 | KYC/EDD review-case dataset used to analyze review activity, remediation, and case outcomes. |
| `customer_risk_analytics.csv` | 1,200 | 20 | Analytics-ready customer-risk dataset containing derived measures used for segmentation and risk prioritization. |

## `beneficial_owners.csv`

Beneficial-ownership dataset used to analyze ownership structure and UBO-related risk.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `customer_id` | String | Source / Operational | Unique identifier assigned to the customer. | `CUST10001` |
| `beneficial_owner_id` | String | Source / Operational | Unique identifier for the beneficial owner. | `CUST10001-BO1` |
| `ownership_pct` | Float | Source / Operational | Field representing ownership pct within the KYC/EDD analytics workflow. | `45.2` |
| `ubo_25pct_flag` | Integer | Source / Operational | Indicator identifying whether ubo 25pct applies. | `1` |
| `pep_flag` | Integer | Source / Operational | Indicator showing whether the customer is identified as a politically exposed person. | `0` |
| `adverse_media_flag` | Integer | Source / Operational | Indicator showing whether relevant adverse-media information was identified. | `1` |

## `customers_kyc.csv`

Customer-level KYC dataset containing profile, due-diligence, and risk attributes.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `customer_id` | String | Source / Operational | Unique identifier assigned to the customer. | `CUST10000` |
| `customer_type` | String | Source / Operational | Classification of the customer, such as individual or business/entity. | `Individual` |
| `country` | String | Derived / Analytical | Country associated with the customer or entity. | `United Arab Emirates` |
| `occupation_industry` | String | Source / Operational | Field representing occupation industry within the KYC/EDD analytics workflow. | `Finance` |
| `pep_flag` | Integer | Source / Operational | Indicator showing whether the customer is identified as a politically exposed person. | `0` |
| `sanctions_hit` | Integer | Source / Operational | Field representing sanctions hit within the KYC/EDD analytics workflow. | `0` |
| `adverse_media_flag` | Integer | Source / Operational | Indicator showing whether relevant adverse-media information was identified. | `0` |
| `source_of_wealth_verified` | Integer | Source / Operational | Field representing source of wealth verified within the KYC/EDD analytics workflow. | `1` |
| `ubo_complete` | Integer | Source / Operational | Field representing ubo complete within the KYC/EDD analytics workflow. | `1` |
| `id_verified` | Integer | Source / Operational | Field representing id verified within the KYC/EDD analytics workflow. | `0` |
| `address_verified` | Integer | Source / Operational | Field representing address verified within the KYC/EDD analytics workflow. | `1` |
| `tax_verified` | Integer | Source / Operational | Field representing tax verified within the KYC/EDD analytics workflow. | `1` |
| `kyc_complete_pct` | Float | Source / Operational | Field representing kyc complete pct within the KYC/EDD analytics workflow. | `80` |
| `risk_score` | Integer | Source / Operational | Numeric measure representing assessed customer risk. | `40` |
| `risk_level` | String | Source / Operational | Attribute used in assessing risk level. | `Moderate` |
| `edd_required` | Integer | Source / Operational | Field representing edd required within the KYC/EDD analytics workflow. | `0` |
| `customer_status` | String | Source / Operational | Field representing customer status within the KYC/EDD analytics workflow. | `Approved` |
| `last_review_date` | String | Source / Operational | Date of the customer's most recent KYC review. | `2026-04-03` |
| `next_review_date` | String | Source / Operational | Scheduled date for the next KYC review. | `2027-04-03` |

## `kyc_review_cases.csv`

KYC/EDD review-case dataset used to analyze review activity, remediation, and case outcomes.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `case_id` | String | Source / Operational | Unique identifier assigned to a KYC/EDD review case. | `KYC00001` |
| `customer_id` | String | Source / Operational | Unique identifier assigned to the customer. | `CUST10001` |
| `review_reason` | String | Source / Operational | Field representing review reason within the KYC/EDD analytics workflow. | `Source of Wealth` |
| `created_date` | String | Source / Operational | Date associated with created. | `2026-03-07` |
| `age_days` | Integer | Derived / Analytical | Field representing age days within the KYC/EDD analytics workflow. | `188` |
| `case_status` | String | Source / Operational | Field representing case status within the KYC/EDD analytics workflow. | `In Review` |
| `risk_score` | Integer | Source / Operational | Numeric measure representing assessed customer risk. | `23` |
| `risk_level` | String | Source / Operational | Attribute used in assessing risk level. | `Low` |
| `priority` | String | Derived / Analytical | Field representing priority within the KYC/EDD analytics workflow. | `High` |

## `customer_risk_analytics.csv`

Analytics-ready customer-risk dataset containing derived measures used for segmentation and risk prioritization.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `customer_id` | String | Derived / Analytical | Unique identifier assigned to the customer. | `CUST10000` |
| `customer_type` | String | Derived / Analytical | Classification of the customer, such as individual or business/entity. | `Individual` |
| `country` | String | Derived / Analytical | Country associated with the customer or entity. | `United Arab Emirates` |
| `occupation_industry` | String | Derived / Analytical | Field representing occupation industry within the KYC/EDD analytics workflow. | `Finance` |
| `pep_flag` | Integer | Derived / Analytical | Indicator showing whether the customer is identified as a politically exposed person. | `0` |
| `sanctions_hit` | Integer | Derived / Analytical | Field representing sanctions hit within the KYC/EDD analytics workflow. | `0` |
| `adverse_media_flag` | Integer | Derived / Analytical | Indicator showing whether relevant adverse-media information was identified. | `0` |
| `source_of_wealth_verified` | Integer | Derived / Analytical | Field representing source of wealth verified within the KYC/EDD analytics workflow. | `1` |
| `ubo_complete` | Integer | Derived / Analytical | Field representing ubo complete within the KYC/EDD analytics workflow. | `1` |
| `id_verified` | Integer | Derived / Analytical | Field representing id verified within the KYC/EDD analytics workflow. | `0` |
| `address_verified` | Integer | Derived / Analytical | Field representing address verified within the KYC/EDD analytics workflow. | `1` |
| `tax_verified` | Integer | Derived / Analytical | Field representing tax verified within the KYC/EDD analytics workflow. | `1` |
| `kyc_complete_pct` | Float | Derived / Analytical | Field representing kyc complete pct within the KYC/EDD analytics workflow. | `80` |
| `risk_score` | Integer | Derived / Analytical | Numeric measure representing assessed customer risk. | `40` |
| `risk_level` | String | Derived / Analytical | Attribute used in assessing risk level. | `Moderate` |
| `edd_required` | Integer | Derived / Analytical | Field representing edd required within the KYC/EDD analytics workflow. | `0` |
| `customer_status` | String | Derived / Analytical | Field representing customer status within the KYC/EDD analytics workflow. | `Approved` |
| `last_review_date` | String | Derived / Analytical | Date of the customer's most recent KYC review. | `2026-04-03` |
| `next_review_date` | String | Derived / Analytical | Scheduled date for the next KYC review. | `2027-04-03` |
| `primary_risk_driver` | String | Derived / Analytical | Attribute used in assessing primary risk driver. | `High-Risk Geography` |

## Dataset Relationships

- `beneficial_owners.csv.customer_id` ↔ `customers_kyc.csv.customer_id` links records across the two datasets.
- `beneficial_owners.csv.customer_id` ↔ `kyc_review_cases.csv.customer_id` links records across the two datasets.
- `beneficial_owners.csv.customer_id` ↔ `customer_risk_analytics.csv.customer_id` links records across the two datasets.
- `customers_kyc.csv.customer_id` ↔ `kyc_review_cases.csv.customer_id` links records across the two datasets.
- `customers_kyc.csv.customer_id` ↔ `customer_risk_analytics.csv.customer_id` links records across the two datasets.
- `kyc_review_cases.csv.customer_id` ↔ `customer_risk_analytics.csv.customer_id` links records across the two datasets.

## KYC / EDD Analytical Workflow

**Customer Profile → Beneficial Ownership Review → Customer Risk Assessment → KYC/EDD Review → Risk Analytics & Prioritization**

The data model supports customer due diligence by combining customer profile information, ownership structures, review activity, and analytical risk measures. This allows the project to demonstrate KYC risk segmentation, EDD prioritization, beneficial-ownership analysis, and review-case monitoring.

## EDA & Feature Engineering Context

Exploratory analysis can be performed across customer risk attributes, beneficial ownership, KYC review outcomes, and customer segments. The `customer_risk_analytics.csv` dataset represents the analytics-ready layer and is classified as **Derived / Analytical** to make the project's feature-engineering and decision-support work visible to portfolio reviewers.

## Data Quality Conventions

- Customer and case identifiers should be checked for uniqueness within their natural entity tables.
- Ownership percentages should be validated for plausible ranges and ownership structures.
- Risk and KYC categorical fields should be standardized before aggregation.
- Date fields should be converted to consistent date types before review-cycle analysis.
- Missing values should be assessed according to business meaning rather than automatically removed.
- Derived risk measures should be reconciled to their underlying source attributes and project business rules.

---

*Prepared for the Financial Crime Customer Risk & KYC/EDD Analytics GitHub portfolio project.*