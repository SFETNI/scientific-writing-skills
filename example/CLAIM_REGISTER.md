# Claim Register — ILLUSTRATIVE EXAMPLE

> **ILLUSTRATIVE ONLY. All claims, values, and citations are synthetic.**

---

## Introduction claims

| ID | Claim (brief) | Label | Source | Citation tier | Section |
|---|---|---|---|---|---|
| I001 | Graphene has in-plane thermal conductivity ~5000 W/m/K | LITERATURE_SUPPORTED | Balandin2011_ILLUSTRATIVE | ABSTRACT_RELEVANT (illustrative) | §1.2 |
| I002 | Polymer matrix conductivity typically 0.1–0.3 W/m/K | LITERATURE_SUPPORTED | Bigg1995_ILLUSTRATIVE | ABSTRACT_RELEVANT (illustrative) | §1.2 |
| I003 | Filler concentration, aspect ratio, and matrix properties govern composite conductivity | LITERATURE_SUPPORTED | Chen2020_ILLUSTRATIVE, Liu2022_ILLUSTRATIVE | ABSTRACT_RELEVANT (illustrative) | §1.3 |
| I004 | Surrogate models have been applied to materials property prediction | LITERATURE_SUPPORTED | Park2021_ILLUSTRATIVE | ABSTRACT_RELEVANT (illustrative) | §1.3 |
| I005 | This paper develops a GBR surrogate for thermal conductivity of graphene composites | METHOD_DEFINITION | — | — | §1.4 |

## Methods claims

| ID | Claim (brief) | Label | Source | Registry ID | Section |
|---|---|---|---|---|---|
| M001 | Dataset contains 120 samples, 8 input features | METHOD_DEFINITION | data/dataset_fake_v1.csv | D001, D004 | §2.1 |
| M002 | 80/20 random train/test split | METHOD_DEFINITION | config/model_config_fake.yaml | D002, D003 | §2.1 |
| M003 | GBR with 200 estimators, max depth 5, learning rate 0.05 | METHOD_DEFINITION | config/model_config_fake.yaml | P001–P003 | §2.3 |
| M004 | Performance evaluated by 5-fold cross-validation | METHOD_DEFINITION | config/model_config_fake.yaml | D005 | §2.3 |

## Results claims

| ID | Claim (brief) | Label | Source | Registry ID | Section |
|---|---|---|---|---|---|
| RL001 | GBR achieves R² = 0.847 ± 0.031 on test set | RESULT_SUPPORTED | model_eval_fake.csv | R001 | §3.1 |
| RL002 | RMSE = 0.143 ± 0.018 W/m/K | RESULT_SUPPORTED | model_eval_fake.csv | R002 | §3.1 |
| RL003 | GBR outperforms linear regression baseline (R² 0.847 vs. 0.631) | RESULT_SUPPORTED | model_eval_fake.csv, baseline_eval_fake.csv | R001, R005 | §3.2 |
| RL004 | Filler content is the dominant predictor (38.4% importance) | RESULT_SUPPORTED | feature_importance_fake.csv | R007 | §3.3 |

## Discussion claims

| ID | Claim (brief) | Label | Notes | Registry ID | Section |
|---|---|---|---|---|---|
| DC001 | The test R² suggests the model generalises well to unseen compositions | INTERPRETATION | Hedged: "suggests" — appropriate | R001 | §4.1 |
| DC002 | The dominance of filler content is consistent with effective medium theories | INTERPRETATION | Should cite EMT literature | R007 | §4.2 |
| DC003 | Performance degradation at high filler loadings may be due to agglomeration | SPECULATION | Explicitly labeled as possible explanation; no direct evidence | — | §4.3 |

---

## Unresolved claims

| ID | Claim (brief) | Status | Required action |
|---|---|---|---|
| U001 | "The model is more accurate than most reported models" | UNSUPPORTED | Systematic comparison required or claim must be removed |

---

## Register integrity

- Last updated: 2026-05-16 (ILLUSTRATIVE)
- Sections covered: Introduction, Methods, Results, Discussion
- Total claims: 16
- UNSUPPORTED remaining: 1 ← illustrative — shows what a flagged unsupported claim looks like
- NEEDS_HUMAN_DECISION: 0
