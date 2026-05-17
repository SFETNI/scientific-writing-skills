# Numerical Registry — ILLUSTRATIVE EXAMPLE

> **ILLUSTRATIVE ONLY. All values are synthetic and have no scientific validity.**

---

## Primary performance metrics

| ID | Metric | Value | Uncertainty | Condition | Source artifact | Used in |
|---|---|---|---|---|---|---|
| R001 | R² (test set) | 0.847 | ± 0.031 | 5-fold CV, test folds, 120 samples | results/model_eval_fake.csv row 4 | §3.1, Table 2 |
| R002 | RMSE (test set) | 0.143 W/m/K | ± 0.018 | Same as R001 | results/model_eval_fake.csv row 5 | §3.1, Table 2 |
| R003 | MAE (test set) | 0.112 W/m/K | ± 0.014 | Same as R001 | results/model_eval_fake.csv row 6 | §3.1 |
| R004 | R² (training set) | 0.924 | ± 0.012 | 5-fold CV, training folds | results/model_eval_fake.csv row 7 | §3.1 |
| R005 | R² (baseline linear regression) | 0.631 | ± 0.044 | Same conditions as GBR | results/baseline_eval_fake.csv row 3 | §3.2, Table 2 |
| R006 | Improvement vs. baseline (R²) | 0.216 | — | GBR minus linear regression | Computed from R001, R005 | §3.2 |
| R007 | Feature importance — filler content (%) | 38.4 | — | Mean decrease impurity, 200 trees | results/feature_importance_fake.csv row 1 | §3.3, Figure 4 |
| R008 | Feature importance — aspect ratio (%) | 27.1 | — | Same as R007 | results/feature_importance_fake.csv row 2 | §3.3, Figure 4 |
| R009 | Feature importance — matrix conductivity (%) | 19.6 | — | Same as R007 | results/feature_importance_fake.csv row 3 | §3.3, Figure 4 |
| R010 | Sensitivity: prediction range (W/m/K) | 0.21–3.84 | — | Full dataset, all conditions | results/sensitivity_fake.csv | §3.4, Figure 5 |
| R011 | Baseline RMSE (linear regression, test set) | 0.241 W/m/K | ± 0.031 | Same conditions as GBR | results/baseline_eval_fake.csv row 4 | §3.2, Table 2 |
| R012 | Baseline MAE (linear regression, test set) | 0.198 W/m/K | ± 0.025 | Same conditions as GBR | results/baseline_eval_fake.csv row 5 | §3.2, Table 2 |
| R013 | Feature importance — remaining 5 variables (%) | 14.9 | — | Complement of R007+R008+R009 | Computed from feature_importance_fake.csv | §3.3 |

## Dataset characteristics

| ID | Item | Value | Source | Used in |
|---|---|---|---|---|
| D001 | Total sample size | 120 | data/dataset_fake_v1.csv | §2.1 |
| D002 | Training set size | 96 | 80% random split | §2.1 |
| D003 | Test set size | 24 | 20% random split | §2.1 |
| D004 | Number of input features | 8 | data/dataset_fake_v1.csv header | §2.1 |
| D005 | Cross-validation folds | 5 | config/model_config_fake.yaml | §2.3 |
| D006 | Dataset filler content range (vol%) | 0.5–20.0 | data/dataset_fake_v1.csv | Table S1 |
| D007 | Dataset filler content mean (vol%) | 8.3 | data/dataset_fake_v1.csv | Table S1 |
| D008 | Dataset matrix conductivity range (W/m/K) | 0.10–0.32 | data/dataset_fake_v1.csv | Table S1 |
| D009 | Dataset output mean thermal conductivity (W/m/K) | 1.42 | data/dataset_fake_v1.csv | Table S1 |
| D010 | High-loading sensitivity threshold (vol%) for scatter increase | 15 | Qualitative analysis | §S2 |
| D011 | Scatter increase threshold in figure caption (W/m/K) | 2.5 | Figure S1 caption | §SM |

## Model parameters

| ID | Parameter | Value | Source | Used in |
|---|---|---|---|---|
| P001 | Number of estimators | 200 | config/model_config_fake.yaml | §2.3 |
| P002 | Max depth | 5 | config/model_config_fake.yaml | §2.3 |
| P003 | Learning rate (selected) | 0.05 | config/model_config_fake.yaml | §2.3 |
| P004 | Min samples leaf | 4 | config/model_config_fake.yaml | §2.3 |
| P005 | Grid search: learning rate low | 0.01 | Grid search config | §S1 |
| P006 | Grid search: learning rate high | 0.1 | Grid search config | §S1 |

## Physical constants (literature values, ILLUSTRATIVE)

| ID | Constant | Value | Citation key | Used in |
|---|---|---|---|---|
| C001 | Graphene in-plane thermal conductivity | ~5000 W/m/K | Balandin2011_ILLUSTRATIVE | §1.2 |
| C002 | Typical polymer matrix conductivity | 0.1–0.3 W/m/K | Bigg1995_ILLUSTRATIVE | §1.2 |

---

## Registry integrity

- Last verified: 2026-05-16 (ILLUSTRATIVE)
- Total registered values: 31
- Values with source artifacts: 31
- Values without source artifacts: 0
