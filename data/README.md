# Data Access and Documentation

## Dataset Summary

- Dataset name: `Telco Customer Churn Dataset`
- Source platform: `Kaggle`
- Source URL: `https://www.kaggle.com/datasets/mosapabdelghany/telcom-customer-churn-dataset`
- Prediction task: `Predict whether a customer will churn`
- Target variable: `Churn`
- Problem type: `Binary classification`

## Source and Licensing

- Access date: `2026-02-21`
- License/terms of use: `TBD`
- Redistribution allowed: `yes/no`

## Access Instructions

1. Open the dataset URL above while logged into Kaggle.
2. Download the CSV and place it at:
   - `data/raw/Telco-Customer-Churn.csv`
3. If your file has a different name, run:
   - `python -m src.pipeline --data-path "data/raw/<your_file_name>.csv"`
4. Keep credentials local only; never commit Kaggle API keys.

## Data Schema

| Column | Type | Description | Used in model |
|---|---|---|---|
| customerID | string | Customer unique identifier | no (dropped) |
| tenure | numeric | Months with company | yes |
| MonthlyCharges | numeric | Monthly bill amount | yes |
| TotalCharges | numeric/string | Total bill amount | yes |
| Churn | categorical | Churn label (Yes/No) | target |
| other service/account columns | mixed | Service and contract attributes | yes |

## Data Quality and Constraints

- Missingness considerations: `TotalCharges` may contain blanks; coerced to numeric with imputation.
- Leakage risks identified: Any post-outcome billing/termination indicators must be excluded if present.
- Known biases/limitations: Single-company telecom dataset may limit external generalization.

## Reproducibility Notes

- Random seed strategy: `42`
- Train/validation/test split rule: `60/20/20 stratified by Churn`
- Data version identifier (if any): `Kaggle snapshot at download time`
