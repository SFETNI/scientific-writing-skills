# Numerical Registry

This file is the single source of truth for all accepted quantitative claims in this manuscript. Every number that appears in the manuscript must appear here first.

**Do not add numbers to the manuscript unless they are registered here.**
**Do not change a registered number without updating both this file and the manuscript.**

---

## How to use

1. Before drafting any section, add all relevant numbers to this registry.
2. In each row, note the source artifact (figure file, table file, analysis output, or citation).
3. When a number is used in the manuscript, record which section uses it in the "Used in" column.
4. The integrity checker (`/srs-check`) will verify that all manuscript numbers appear here.

---

## Primary performance metrics

| ID | Metric | Value | Uncertainty | Condition | Source artifact | Used in |
|---|---|---|---|---|---|---|
| R001 | [e.g., R² test set] | [e.g., 0.847] | [e.g., ± 0.031] | [e.g., 5-fold CV, test fold] | [e.g., results/model_eval.csv row 12] | [e.g., §3.1, Table 2] |
| R002 | | | | | | |
| R003 | | | | | | |

## Dataset characteristics

| ID | Item | Value | Source | Used in |
|---|---|---|---|---|
| D001 | [e.g., Total sample size] | [e.g., 120] | [e.g., data/dataset_v3.csv] | [e.g., §2.1] |
| D002 | [e.g., Training set size] | [e.g., 96 (80%)] | | |
| D003 | [e.g., Test set size] | [e.g., 24 (20%)] | | |

## Model parameters and hyperparameters

| ID | Parameter | Value | Source | Used in |
|---|---|---|---|---|
| P001 | [e.g., Number of estimators] | [e.g., 200] | [e.g., config/model_config.yaml] | [e.g., §2.3] |
| P002 | | | | |

## Secondary analyses

| ID | Metric | Value | Uncertainty | Condition | Source | Used in |
|---|---|---|---|---|---|---|
| S001 | | | | | | |

## Physical / literature constants

| ID | Constant | Value | Citation key | Used in |
|---|---|---|---|---|
| C001 | | | | |

---

## Registry integrity

- Last verified: [YYYY-MM-DD]
- Verified by: [human name or /srs-check]
- Total registered values: [N]
- Values with source artifacts: [N]
- Values without source artifacts: [N] ← must be zero before submission
