# Numerical Registry - Concrete Ridge Worked Example

This registry is for the concrete compressive-strength worked example. The current generated artifacts are labelled `DETERMINISTIC_FALLBACK_NOT_UCI`; values below are demonstration outputs, not verified UCI benchmark results.

## Dataset And Split

| ID | Quantity | Value | Unit | Source artifact | Used in |
|---|---|---:|---|---|---|
| D001 | Local rows | 1030 | rows | `outputs/example_generation_log.txt`; `tables/table_dataset_summary.tex` | Abstract, Methods, Table 1 |
| D002 | Input variables | 8 | variables | `outputs/example_generation_log.txt`; `data/DATA_DICTIONARY.md` | Abstract, Methods |
| D003 | Training rows | 824 | rows | `outputs/example_generation_log.txt` | Abstract, Methods |
| D004 | Test rows | 206 | rows | `outputs/example_generation_log.txt` | Abstract, Methods |
| D005 | Missing numeric values | 0 | values | `outputs/example_generation_log.txt` | Methods |
| D006 | Target mean | 29.518 | MPa | `tables/table_dataset_summary.tex` | Methods |
| D007 | Target standard deviation | 18.190 | MPa | `tables/table_dataset_summary.tex` | Methods |
| D008 | Target minimum | 2.300 | MPa | `tables/table_dataset_summary.tex` | Methods |
| D009 | Target median | 30.907 | MPa | `tables/table_dataset_summary.tex` | Table 1 |
| D010 | Target maximum | 73.941 | MPa | `tables/table_dataset_summary.tex` | Methods |
| D011 | Strongest absolute target correlation | 0.822 | unitless | `outputs/example_generation_log.txt` | Results |

## Model Performance

| ID | Quantity | Value | Unit | Source artifact | Used in |
|---|---|---:|---|---|---|
| M001 | Selected ridge alpha | 1.000 | unitless | `outputs/example_generation_log.txt`; `tables/table_model_performance.tex` | Abstract, Methods, Table 2 |
| M002 | Ridge train RMSE | 6.366 | MPa | `tables/table_model_performance.tex` | Table 2 |
| M003 | Ridge test RMSE | 6.234 | MPa | `outputs/example_generation_log.txt`; `tables/table_model_performance.tex` | Abstract, Results, Conclusions |
| M004 | Ridge test MAE | 4.964 | MPa | `outputs/example_generation_log.txt`; `tables/table_model_performance.tex` | Abstract, Results, Conclusions |
| M005 | Ridge test R2 | 0.886 | unitless | `outputs/example_generation_log.txt`; `tables/table_model_performance.tex` | Abstract, Results, Conclusions |
| M006 | Ridge test bias | 0.032 | MPa | `outputs/example_generation_log.txt`; `tables/table_model_performance.tex` | Abstract, Results, Conclusions |
| M007 | OLS alpha | 0.000 | unitless | `tables/table_model_performance.tex` | Table 2 |
| M008 | OLS train RMSE | 6.366 | MPa | `tables/table_model_performance.tex` | Table 2 |
| M009 | OLS test RMSE | 6.234 | MPa | `tables/table_model_performance.tex` | Results, Table 2 |
| M010 | OLS test MAE | 4.964 | MPa | `tables/table_model_performance.tex` | Results, Table 2 |
| M011 | OLS test R2 | 0.886 | unitless | `tables/table_model_performance.tex` | Results, Table 2 |
| M012 | OLS test bias | 0.033 | MPa | `tables/table_model_performance.tex` | Table 2 |
| M013 | Training-mean baseline train RMSE | 18.115 | MPa | `tables/table_model_performance.tex` | Table 2 |
| M014 | Training-mean baseline test RMSE | 18.447 | MPa | `tables/table_model_performance.tex` | Results, Table 2 |
| M015 | Training-mean baseline test MAE | 15.525 | MPa | `tables/table_model_performance.tex` | Table 2 |
| M016 | Training-mean baseline test R2 | -0.002 | unitless | `tables/table_model_performance.tex` | Results, Table 2 |
| M017 | Training-mean baseline test bias | -0.740 | MPa | `tables/table_model_performance.tex` | Table 2 |

## Cross-Validation

| ID | Alpha | CV RMSE mean | CV RMSE SD | CV MAE mean | CV R2 mean | Source artifact |
|---|---:|---:|---:|---:|---:|---|
| CV001 | 0.000 | 6.432 | 0.277 | 5.018 | 0.872 | `tables/table_supplementary_cv.tex` |
| CV002 | 0.100 | 6.432 | 0.277 | 5.018 | 0.872 | `tables/table_supplementary_cv.tex` |
| CV003 | 1.000 | 6.432 | 0.276 | 5.018 | 0.872 | `tables/table_supplementary_cv.tex` |
| CV004 | 10.000 | 6.436 | 0.269 | 5.027 | 0.871 | `tables/table_supplementary_cv.tex` |
| CV005 | 100.000 | 6.805 | 0.192 | 5.498 | 0.857 | `tables/table_supplementary_cv.tex` |

## Ablation Diagnostics

| ID | Removed feature | Test RMSE | Delta RMSE | Unit | Source artifact |
|---|---|---:|---:|---|---|
| A001 | cement | 16.191 | 9.958 | MPa | `tables/table_ablation.tex` |
| A002 | blast furnace slag | 7.749 | 1.515 | MPa | `tables/table_ablation.tex` |
| A003 | age | 7.735 | 1.502 | MPa | `tables/table_ablation.tex` |
| A004 | water | 6.834 | 0.601 | MPa | `tables/table_ablation.tex` |
| A005 | fly ash | 6.492 | 0.258 | MPa | `tables/table_ablation.tex` |
| A006 | superplasticizer | 6.460 | 0.227 | MPa | `tables/table_ablation.tex` |
| A007 | fine aggregate | 6.236 | 0.002 | MPa | `tables/table_ablation.tex` |
| A008 | coarse aggregate | 6.221 | -0.013 | MPa | `tables/table_ablation.tex` |

## Age-Stratified Error Diagnostics

| ID | Age bin | N | Mean age | MAE | Bias | Mean strength | Source artifact |
|---|---|---:|---:|---:|---:|---:|---|
| E001 | <=7 days | 63 | 4.937 | 5.650 | 3.102 | 21.709 | `tables/table_error_by_age.tex` |
| E002 | 8-28 days | 79 | 25.342 | 4.225 | -0.420 | 29.903 | `tables/table_error_by_age.tex` |
| E003 | 29-90 days | 45 | 72.622 | 4.622 | -3.227 | 34.183 | `tables/table_error_by_age.tex` |
| E004 | >90 days | 19 | 246.579 | 6.572 | -0.552 | 49.178 | `tables/table_error_by_age.tex` |

## Decimal Coverage Tokens

The checker requires every decimal token in the manuscript and generated tables to appear in this registry. Some entries below are formatting parameters or table-only descriptive values; they are included to keep the mechanical audit explicit.

| ID | Value | Reason | Locations |
|---|---:|---|---|
| COV001 | -3.227 | Manuscript/table decimal coverage token | table_error_by_age.tex:10 |
| COV002 | -0.740 | Manuscript/table decimal coverage token | table_model_performance.tex:8 |
| COV003 | -0.552 | Manuscript/table decimal coverage token | table_error_by_age.tex:11 |
| COV004 | -0.420 | Manuscript/table decimal coverage token | table_error_by_age.tex:9 |
| COV005 | -0.013 | Manuscript/table decimal coverage token | table_ablation.tex:15 |
| COV006 | -0.002 | Manuscript/table decimal coverage token | 03_results.tex:19, table_model_performance.tex:8 |
| COV007 | 0.000 | Manuscript/table decimal coverage token | table_dataset_summary.tex:10, table_dataset_summary.tex:12, table_dataset_summary.tex:9, table_model_performance.tex:9, table_supplementary_cv.tex:8 |
| COV008 | 0.002 | Manuscript/table decimal coverage token | table_ablation.tex:14 |
| COV009 | 0.032 | Manuscript/table decimal coverage token | 03_results.tex:19, 04_conclusions.tex:13, main.tex:28, table_model_performance.tex:10 |
| COV010 | 0.033 | Manuscript/table decimal coverage token | table_model_performance.tex:9 |
| COV011 | 0.100 | Manuscript/table decimal coverage token | table_supplementary_cv.tex:9 |
| COV012 | 0.1 | Manuscript/table decimal coverage token | 05_supplementary.tex:13 |
| COV013 | 0.192 | Manuscript/table decimal coverage token | table_supplementary_cv.tex:12 |
| COV014 | 0.227 | Manuscript/table decimal coverage token | table_ablation.tex:13 |
| COV015 | 0.258 | Manuscript/table decimal coverage token | table_ablation.tex:12 |
| COV016 | 0.269 | Manuscript/table decimal coverage token | table_supplementary_cv.tex:11 |
| COV017 | 0.276 | Manuscript/table decimal coverage token | table_supplementary_cv.tex:10 |
| COV018 | 0.277 | Manuscript/table decimal coverage token | table_supplementary_cv.tex:8, table_supplementary_cv.tex:9 |
| COV019 | 0.601 | Manuscript/table decimal coverage token | table_ablation.tex:11 |
| COV020 | 0.78 | Manuscript/table decimal coverage token | 03_results.tex:25, 03_results.tex:37, 03_results.tex:46, 03_results.tex:58 |
| COV021 | 0.822 | Manuscript/table decimal coverage token | 03_results.tex:7 |
| COV022 | 0.857 | Manuscript/table decimal coverage token | table_supplementary_cv.tex:12 |
| COV023 | 0.871 | Manuscript/table decimal coverage token | table_supplementary_cv.tex:11 |
| COV024 | 0.872 | Manuscript/table decimal coverage token | table_supplementary_cv.tex:10, table_supplementary_cv.tex:8, table_supplementary_cv.tex:9 |
| COV025 | 0.886 | Manuscript/table decimal coverage token | 03_results.tex:19, 04_conclusions.tex:13, 04_conclusions.tex:4, main.tex:28, table_model_performance.tex:10, table_model_performance.tex:9 |
| COV026 | 0.95 | Manuscript/table decimal coverage token | 03_results.tex:11 |
| COV027 | 1.000 | Manuscript/table decimal coverage token | table_dataset_summary.tex:15, table_model_performance.tex:10, table_supplementary_cv.tex:10 |
| COV028 | 1.502 | Manuscript/table decimal coverage token | table_ablation.tex:10 |
| COV029 | 1.515 | Manuscript/table decimal coverage token | table_ablation.tex:9 |
| COV030 | 2.300 | Manuscript/table decimal coverage token | 02_methods.tex:14, table_dataset_summary.tex:16 |
| COV031 | 3.102 | Manuscript/table decimal coverage token | table_error_by_age.tex:8 |
| COV032 | 4.225 | Manuscript/table decimal coverage token | table_error_by_age.tex:9 |
| COV033 | 4.622 | Manuscript/table decimal coverage token | table_error_by_age.tex:10 |
| COV034 | 4.937 | Manuscript/table decimal coverage token | table_error_by_age.tex:8 |
| COV035 | 4.964 | Manuscript/table decimal coverage token | 03_results.tex:19, 04_conclusions.tex:13, main.tex:28, table_model_performance.tex:10, table_model_performance.tex:9 |
| COV036 | 5.018 | Manuscript/table decimal coverage token | table_supplementary_cv.tex:10, table_supplementary_cv.tex:8, table_supplementary_cv.tex:9 |
| COV037 | 5.027 | Manuscript/table decimal coverage token | table_supplementary_cv.tex:11 |
| COV038 | 5.498 | Manuscript/table decimal coverage token | table_supplementary_cv.tex:12 |
| COV039 | 5.650 | Manuscript/table decimal coverage token | table_error_by_age.tex:8 |
| COV040 | 6.221 | Manuscript/table decimal coverage token | table_ablation.tex:15 |
| COV041 | 6.234 | Manuscript/table decimal coverage token | 03_results.tex:19, 03_results.tex:54, 04_conclusions.tex:13, 04_conclusions.tex:4, main.tex:28, table_model_performance.tex:10, table_model_performance.tex:9 |
| COV042 | 6.236 | Manuscript/table decimal coverage token | table_ablation.tex:14 |
| COV043 | 6.366 | Manuscript/table decimal coverage token | table_model_performance.tex:10, table_model_performance.tex:9 |
| COV044 | 6.432 | Manuscript/table decimal coverage token | table_supplementary_cv.tex:10, table_supplementary_cv.tex:8, table_supplementary_cv.tex:9 |
| COV045 | 6.436 | Manuscript/table decimal coverage token | table_supplementary_cv.tex:11 |
| COV046 | 6.460 | Manuscript/table decimal coverage token | table_ablation.tex:13 |
| COV047 | 6.492 | Manuscript/table decimal coverage token | table_ablation.tex:12 |
| COV048 | 6.572 | Manuscript/table decimal coverage token | 03_results.tex:33, table_error_by_age.tex:11 |
| COV049 | 6.805 | Manuscript/table decimal coverage token | table_supplementary_cv.tex:12 |
| COV050 | 6.834 | Manuscript/table decimal coverage token | table_ablation.tex:11 |
| COV051 | 7.735 | Manuscript/table decimal coverage token | table_ablation.tex:10 |
| COV052 | 7.749 | Manuscript/table decimal coverage token | table_ablation.tex:9 |
| COV053 | 9.471 | Manuscript/table decimal coverage token | table_dataset_summary.tex:12 |
| COV054 | 9.958 | Manuscript/table decimal coverage token | 03_results.tex:54, main.tex:28, table_ablation.tex:8 |
| COV055 | 10.000 | Manuscript/table decimal coverage token | table_supplementary_cv.tex:11 |
| COV056 | 10.742 | Manuscript/table decimal coverage token | table_dataset_summary.tex:12 |
| COV057 | 11.085 | Manuscript/table decimal coverage token | table_dataset_summary.tex:12 |
| COV058 | 15.525 | Manuscript/table decimal coverage token | table_model_performance.tex:8 |
| COV059 | 16.191 | Manuscript/table decimal coverage token | 03_results.tex:54, table_ablation.tex:8 |
| COV060 | 18.115 | Manuscript/table decimal coverage token | table_model_performance.tex:8 |
| COV061 | 18.190 | Manuscript/table decimal coverage token | 02_methods.tex:14, table_dataset_summary.tex:16 |
| COV062 | 18.447 | Manuscript/table decimal coverage token | 03_results.tex:19, table_model_performance.tex:8 |
| COV063 | 21.709 | Manuscript/table decimal coverage token | table_error_by_age.tex:8 |
| COV064 | 25.342 | Manuscript/table decimal coverage token | table_error_by_age.tex:9 |
| COV065 | 28.000 | Manuscript/table decimal coverage token | table_dataset_summary.tex:15 |
| COV066 | 29.518 | Manuscript/table decimal coverage token | 02_methods.tex:14, table_dataset_summary.tex:16 |
| COV067 | 29.903 | Manuscript/table decimal coverage token | table_error_by_age.tex:9 |
| COV068 | 30.907 | Manuscript/table decimal coverage token | table_dataset_summary.tex:16 |
| COV069 | 31.988 | Manuscript/table decimal coverage token | table_dataset_summary.tex:12 |
| COV070 | 34.183 | Manuscript/table decimal coverage token | table_error_by_age.tex:10 |
| COV071 | 35.418 | Manuscript/table decimal coverage token | table_dataset_summary.tex:11 |
| COV072 | 39.397 | Manuscript/table decimal coverage token | table_dataset_summary.tex:9 |
| COV073 | 49.178 | Manuscript/table decimal coverage token | table_error_by_age.tex:11 |
| COV074 | 52.710 | Manuscript/table decimal coverage token | table_dataset_summary.tex:15 |
| COV075 | 53.574 | Manuscript/table decimal coverage token | table_dataset_summary.tex:10 |
| COV076 | 65.159 | Manuscript/table decimal coverage token | table_dataset_summary.tex:10 |
| COV077 | 72.622 | Manuscript/table decimal coverage token | table_error_by_age.tex:10 |
| COV078 | 73.941 | Manuscript/table decimal coverage token | 02_methods.tex:14, table_dataset_summary.tex:16 |
| COV079 | 78.089 | Manuscript/table decimal coverage token | table_dataset_summary.tex:15 |
| COV080 | 97.390 | Manuscript/table decimal coverage token | table_dataset_summary.tex:13 |
| COV081 | 100.000 | Manuscript/table decimal coverage token | table_supplementary_cv.tex:12 |
| COV082 | 102.084 | Manuscript/table decimal coverage token | table_dataset_summary.tex:9 |
| COV083 | 102.213 | Manuscript/table decimal coverage token | table_dataset_summary.tex:8 |
| COV084 | 115.824 | Manuscript/table decimal coverage token | table_dataset_summary.tex:14 |
| COV085 | 118.639 | Manuscript/table decimal coverage token | table_dataset_summary.tex:9 |
| COV086 | 122.312 | Manuscript/table decimal coverage token | table_dataset_summary.tex:11 |
| COV087 | 127.229 | Manuscript/table decimal coverage token | table_dataset_summary.tex:8 |
| COV088 | 186.071 | Manuscript/table decimal coverage token | table_dataset_summary.tex:11 |
| COV089 | 187.755 | Manuscript/table decimal coverage token | table_dataset_summary.tex:11 |
| COV090 | 199.959 | Manuscript/table decimal coverage token | table_dataset_summary.tex:10 |
| COV091 | 246.579 | Manuscript/table decimal coverage token | table_error_by_age.tex:11 |
| COV092 | 246.885 | Manuscript/table decimal coverage token | table_dataset_summary.tex:11 |
| COV093 | 317.053 | Manuscript/table decimal coverage token | table_dataset_summary.tex:8 |
| COV094 | 318.244 | Manuscript/table decimal coverage token | table_dataset_summary.tex:8 |
| COV095 | 358.927 | Manuscript/table decimal coverage token | table_dataset_summary.tex:9 |
| COV096 | 365.000 | Manuscript/table decimal coverage token | table_dataset_summary.tex:15 |
| COV097 | 539.367 | Manuscript/table decimal coverage token | table_dataset_summary.tex:8 |
| COV098 | 594.201 | Manuscript/table decimal coverage token | table_dataset_summary.tex:14 |
| COV099 | 787.164 | Manuscript/table decimal coverage token | table_dataset_summary.tex:14 |
| COV100 | 788.998 | Manuscript/table decimal coverage token | table_dataset_summary.tex:14 |
| COV101 | 801.274 | Manuscript/table decimal coverage token | table_dataset_summary.tex:13 |
| COV102 | 975.166 | Manuscript/table decimal coverage token | table_dataset_summary.tex:13 |
| COV103 | 975.549 | Manuscript/table decimal coverage token | table_dataset_summary.tex:13 |
| COV104 | 992.940 | Manuscript/table decimal coverage token | table_dataset_summary.tex:14 |
| COV105 | 1144.902 | Manuscript/table decimal coverage token | table_dataset_summary.tex:13 |

## Integrity Notes

- Last refreshed: 2026-05-18.
- Source label: `DETERMINISTIC_FALLBACK_NOT_UCI`.
- Values are fixed unless `example/scripts/generate_example_artifacts.py` is rerun and manuscript, tables, figures, registry, claim register, and review reports are refreshed together.
