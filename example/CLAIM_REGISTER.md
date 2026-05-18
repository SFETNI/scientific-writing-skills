# Claim Register - Concrete Ridge Worked Example

This claim register maps the current concrete compressive-strength worked example to its evidence sources. The current generated artifacts are labelled `DETERMINISTIC_FALLBACK_NOT_UCI`; therefore, local numerical claims are demonstration outputs only and must not be presented as verified UCI benchmark results.

## Claim Labels

| Label | Meaning |
|---|---|
| DATA_PROVENANCE | Supported by local generation log, data dictionary, or UCI repository metadata. |
| METHOD_DEFINITION | Describes the implemented modelling or evaluation workflow. |
| RESULT_SUPPORTED | Directly supported by generated tables, figures, logs, or numerical registry entries. |
| INTERPRETATION_LIMITED | Conservative interpretation that is bounded to local fallback data. |
| LITERATURE_CONTEXT | Background claim supported by bibliography metadata or cited sources. |
| HUMAN_DECISION | Requires maintainer or author decision before release as a completed example. |

## Provenance And Dataset Claims

| ID | Claim | Label | Evidence | Registry IDs | Location |
|---|---|---|---|---|---|
| P001 | The workflow is designed around the UCI Concrete Compressive Strength variable schema. | DATA_PROVENANCE | `data/DATA_LICENSE.md`; `Yeh1998_UCIConcreteDataset` | D001-D002 | Abstract, Introduction, Methods |
| P002 | The current local artifacts are labelled `DETERMINISTIC_FALLBACK_NOT_UCI`. | DATA_PROVENANCE | `outputs/example_generation_log.txt`; `data/DATA_DICTIONARY.md` | D001-D005 | Abstract, Introduction, Methods, Data availability |
| P003 | Local fallback results must not be interpreted as verified UCI observations. | INTERPRETATION_LIMITED | `data/DATA_LICENSE.md`; manuscript provenance statements | D001-D011 | Throughout manuscript |
| P004 | The local fallback dataset contains 1,030 rows and eight input variables. | RESULT_SUPPORTED | `outputs/example_generation_log.txt`; `tables/table_dataset_summary.tex` | D001-D002 | Abstract, Methods |
| P005 | The local data have no missing numeric values. | RESULT_SUPPORTED | `outputs/example_generation_log.txt` | D005 | Methods |

## Method Claims

| ID | Claim | Label | Evidence | Registry IDs | Location |
|---|---|---|---|---|---|
| M001 | The artifact pipeline used an 80/20 train/test split. | METHOD_DEFINITION | `outputs/example_generation_log.txt` | D003-D004 | Abstract, Methods |
| M002 | Numeric predictors were standardized for OLS and ridge models. | METHOD_DEFINITION | `scripts/generate_example_artifacts.py`; Methods text | M007-M012 | Methods |
| M003 | Ridge regression was used as a transparent regularized linear baseline. | METHOD_DEFINITION | Methods text; `HoerlKennard1970_Ridge` | M001-M006 | Methods |
| M004 | The selected ridge penalty was chosen using five-fold cross-validation on training data. | METHOD_DEFINITION | `tables/table_supplementary_cv.tex`; `Stone1974_CrossValidation` | CV001-CV005 | Methods, Supplementary |
| M005 | The ablation analysis is a model-dependence diagnostic rather than a causal analysis. | INTERPRETATION_LIMITED | Methods and Results text | A001-A008 | Methods, Results |

## Result Claims

| ID | Claim | Label | Evidence | Registry IDs | Location |
|---|---|---|---|---|---|
| R001 | The selected ridge model achieved test RMSE 6.234 MPa, MAE 4.964 MPa, R2 0.886, and bias 0.032 MPa. | RESULT_SUPPORTED | `outputs/example_generation_log.txt`; `tables/table_model_performance.tex` | M003-M006 | Abstract, Results, Conclusions |
| R002 | OLS and ridge gave nearly identical rounded test metrics in this generated run. | RESULT_SUPPORTED | `tables/table_model_performance.tex` | M003-M012 | Results, Discussion |
| R003 | Both linear models improved over the training-mean baseline in the local fallback split. | RESULT_SUPPORTED | `tables/table_model_performance.tex` | M003-M017 | Results |
| R004 | Cement had the strongest absolute target correlation in the generated registry candidates. | RESULT_SUPPORTED | `outputs/example_generation_log.txt` | D011 | Results |
| R005 | Removing cement produced the largest RMSE increase in the ablation table. | RESULT_SUPPORTED | `outputs/example_generation_log.txt`; `tables/table_ablation.tex` | A001 | Abstract, Results, Conclusions |
| R006 | The oldest age bin contained 19 test observations and had MAE 6.572 MPa. | RESULT_SUPPORTED | `tables/table_error_by_age.tex` | E004 | Results |
| R007 | Age-bin error summaries are descriptive and should not be generalized beyond the fallback split. | INTERPRETATION_LIMITED | `tables/table_error_by_age.tex`; Results text | E001-E004 | Results |

## Literature Context Claims

| ID | Claim | Label | Evidence | Citation tier | Location |
|---|---|---|---|---|
| L001 | The UCI repository describes the Concrete Compressive Strength dataset and its public dataset context. | LITERATURE_CONTEXT | `Yeh1998_UCIConcreteDataset` | METADATA_VERIFIED | Introduction, Data availability |
| L002 | Yeh's earlier modelling study established concrete-strength prediction from mixture variables and curing age as an applied data-driven modelling problem. | LITERATURE_CONTEXT | `Yeh1998_ConcreteANN` | METADATA_VERIFIED | Introduction |
| L003 | Computational-intelligence and ML methods have been used in concrete compressive-strength prediction. | LITERATURE_CONTEXT | `NunezMaraniFlahNehdi2021_ConcreteMLReview` | METADATA_VERIFIED | Introduction |
| L004 | Ridge regression adds an L2 penalty to least-squares estimation. | LITERATURE_CONTEXT | `HoerlKennard1970_Ridge` | METADATA_VERIFIED | Introduction, Methods |
| L005 | Cross-validation is a resampling-based approach for prediction assessment and model-selection support. | LITERATURE_CONTEXT | `Stone1974_CrossValidation` | METADATA_VERIFIED | Introduction, Methods |

## Human Decisions Remaining

| ID | Decision | Why it matters | Suggested resolution |
|---|---|---|---|
| H001 | Keep deterministic fallback data or verify official UCI data. | This determines whether the example remains a pure pipeline exercise or can describe official dataset observations. | Keep fallback framing unless maintainers authorize data retrieval and provenance verification. |
| H002 | Keep ridge-specific title or broaden to linear-baseline workflow framing. | OLS and ridge metrics are nearly identical in the current run. | Consider a broader title before final release. |
| H003 | Decide whether internal workflow phrasing belongs in the manuscript or only supporting docs. | Manuscript readability improves if internal audit language is moved to documentation. | Polish after registry and QC reports pass. |

## Integrity Notes

- Last refreshed: 2026-05-18.
- Unsupported claims remaining: none identified in the current conservative manuscript text.
- Human-decision items remaining: H001-H003.
